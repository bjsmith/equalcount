"""Monte Carlo comparison of the Current System and the Proposed System.

Each scenario builds a synthetic New Zealand election from scratch:

  Parliament       121 seats; 64 general electorates and 7 Māori electorates.
  Left bloc        2–5 general parties ("Left 1" is the largest), plus 0–2
                   Māori electorate parties ("Māori 1", "Māori 2").
  Right bloc       2–5 general parties ("Right 1" is the largest).
  Centrist         0–2 parties ("Centre 1", "Centre 2"), each 2–10% of the
                   general vote, each allied to a randomly chosen bloc.
  Minor parties    1–10% of the general vote in total, split randomly between
                   "Left minor", "Right minor" and "Centre minor" (allied to a
                   random bloc). They never qualify and stand no candidates;
                   their voters give electorate votes to their bloc's largest
                   party (Left 1 or Right 1).
  Bloc balance     Left : Right anywhere from 30:70 to 70:30.
  Within a bloc    party shares drawn from a flat Dirichlet, so some parties
                   fall below 5%.
  Māori seats      vote only for Māori parties and general Left parties (a
                   simplification). Māori parties get no votes elsewhere.
  Geography        each general electorate has a random left-right lean, and
                   each party a random local concentration; national totals
                   are then matched by iterative proportional fitting.
  Turnout          general ~40,000 valid votes per electorate; Māori 24–30k.

Electorate votes (built ballot by ballot as a party × candidate table):

  Personal vote     a share π (0–15% per scenario) of every party's voters
                    vote for a candidate they like, by random local appeal.
  Strategic: bloc   a share s_L / s_R (0–100%) of the rest of each minor bloc
                    party's voters (centrists use their ally's s) give their
                    electorate vote to their bloc's largest party.
  Strategic: Māori  in Māori electorates, a share s_M (0–100%) of left voters,
                    and of the weaker Māori party's voters, give their
                    electorate vote to the locally strongest Māori party.
  Sincere           everyone else votes for their own party's candidate.

Strategic behaviour is drawn independently of the electoral system, so both
systems face exactly the same ballots. The model does not capture how voters
would respond to each system's incentives.

Systems (the number is the nominal size H; no number means 121):

  MMP, MMP141       Current system. Sainte-Laguë over H; overhanging parties
                    keep their extra electorates and the house grows.
  MMP-T, MMP-T141   Overhang Transfer (explainer's Option 1).
                    1 threshold on raw party votes; 2 Sainte-Laguë on raw
                    votes; if a party overhangs, 3 count wasted party votes on
                    ballots for its winning candidates (party vote for a party
                    that doesn't qualify) for it, only as many as needed;
                    4 then the same fraction f of every split ballot for its
                    winning candidates (party vote for another qualifying
                    party); 5 any overhang still left is absorbed within H
                    (the Independent Electoral Review rule).
  MMP-BV, MMP-BV141 Backup Vote (explainer's Option 2).
                    1 threshold on raw party votes;
                    2 every party vote for a non-qualifying party counts for
                      the party of that voter's electorate candidate, if it
                      qualifies (at every election, overhang or not);
                    3 Sainte-Laguë on those votes; if a party still overhangs,
                      the same fraction f of every split ballot for its
                      winning candidates (party vote for another qualifying
                      party) is counted for it, only as much as needed;
                    4 any overhang still left is absorbed within H
                      (the Independent Electoral Review rule).

Yardsticks:

  Party yardstick   each qualifying party's share of the qualifying party vote
                    (raw party votes, the conventional measure).
  Bloc yardstick    each bloc's share of ALL party votes, including votes for
                    its parties that missed the threshold. Every party belongs
                    to the Left or Right bloc (centrists count with their ally),
                    so the two blocs' fair shares add up to the whole house.
                    Used for the Bloc seat deficit shown for each system.
  Countable bloc    the same, but leaving out voters who wasted both ticks
  yardstick         (party vote and electorate candidate both for parties that
                    don't qualify). No seat rule can count them, so they are
                    excluded when working out the extra seats needed (b).
  Either-choice     every voter counts once, for EITHER their party vote OR
  yardstick         their electorate candidate's party, whichever makes the
                    result look most proportional. A voter whose party vote
                    went to a party that doesn't qualify may count for their
                    candidate's party OR for nobody (as the threshold treats
                    them today), so ordinary party-vote proportionality is
                    always one of the allowed countings; one whose
                    candidate's party doesn't qualify counts for their party
                    vote; voters who wasted both ticks are left out. The measure is the best case
                    over every such assignment, so a result is "either-choice
                    proportional" if some way of counting each voter by one
                    of their own two choices makes it proportional.

Measures:

  Gallagher index and Party seat deficit (sum of every party's shortfall),
  Party seat deficit rounded (each shortfall rounded to whole seats first),
  Max party deficit — all against the party yardstick; Bloc seat deficit
  (shortfall of the worse-off bloc) against the bloc yardstick; and the
  smallest nominal size H at which (a) no party is short by more than one
  seat and (b) no bloc is.
  Either-choice party deficit (smallest possible sum of party shortfalls),
  Either-choice max party deficit (smallest possible worst shortfall),
  Either-choice bloc deficit, and extra seats (c) no party / (d) no bloc
  more than one seat short on the either-choice yardstick.

  The either-choice minimums come from Gale's supply–demand theorem applied
  to every group of parties (see _either_minmax / _either_sum): the worst
  shortfall is exact to bisection precision; the total shortfall is minimised
  over the number of counted voters on a fine grid.

Run:  python3 mc_overhang.py test        (10 scenarios, printed in detail)
      python3 mc_overhang.py run N       (N scenarios → mc_results.csv)
      python3 mc_overhang.py store N     (N scenarios' raw results → runs/exp1/records.jsonl.gz;
                                          then python3 measures.py recompute runs/exp1)
"""
import csv
import math
import random
import sys

import numpy as np

SEATS = 121
N_GEN, N_MAORI = 64, 7
THRESHOLD = 0.05
H_MAX = 400
TOL = 1.0  # seat tolerance for the required-size search


# ======================= scenario generation =======================

class Party:
    def __init__(self, name, bloc, share=0.0, sigma=0.3):
        self.name, self.bloc, self.share, self.sigma = name, bloc, share, sigma
        self.ally = bloc  # for centrists: 'L' or 'R'

    def __repr__(self):
        return self.name


def dirichlet_sorted(rng, n):
    x = sorted((rng.expovariate(1.0) for _ in range(n)), reverse=True)
    s = sum(x)
    return [v / s for v in x]


def ipf(rows, targets, iters=30):
    """rows: list of (size, [weights]); scale columns to national targets
    (fractions of the summed size) while keeping each row's total = size."""
    total = sum(sz for sz, _ in rows)
    m = [[w for w in ws] for _, ws in rows]
    for i, (sz, _) in enumerate(rows):
        s = sum(m[i]); m[i] = [sz * w / s for w in m[i]]
    for _ in range(iters):
        col = [sum(m[i][j] for i in range(len(m))) for j in range(len(targets))]
        k = [targets[j] * total / col[j] if col[j] > 0 else 0 for j in range(len(targets))]
        for i, (sz, _) in enumerate(rows):
            r = [m[i][j] * k[j] for j in range(len(targets))]
            s = sum(r); m[i] = [sz * v / s for v in r]
    return m


def gen_scenario(rng):
    p = {}
    p["n_left"], p["n_right"] = rng.randint(2, 5), rng.randint(2, 5)
    p["n_maori"], p["n_centre"] = rng.randint(0, 2), rng.randint(0, 2)
    p["minor"] = rng.uniform(0.01, 0.10)
    mx = [rng.expovariate(1.0) for _ in range(3)]
    p["minor_left"], p["minor_right"], p["minor_centre"] = (p["minor"] * x / sum(mx) for x in mx)
    p["minor_centre_ally"] = rng.choice("LR")
    p["left_frac"] = rng.uniform(0.30, 0.70)
    p["s_L"], p["s_R"], p["s_M"] = rng.random(), rng.random(), rng.random()
    p["personal"] = rng.uniform(0.0, 0.15)
    p["maori_party_share"] = rng.uniform(0.10, 0.60) if p["n_maori"] else 0.0

    parties = []
    centre = [rng.uniform(0.02, 0.10) for _ in range(p["n_centre"])]
    blocs = 1 - p["minor"] - sum(centre)
    L, R = blocs * p["left_frac"], blocs * (1 - p["left_frac"])
    for i, sh in enumerate(dirichlet_sorted(rng, p["n_left"])):
        parties.append(Party(f"Left {i+1}", "L", L * sh, 0.15 if i == 0 else rng.uniform(0.2, 0.6)))
    for i, sh in enumerate(dirichlet_sorted(rng, p["n_maori"]) if p["n_maori"] else []):
        parties.append(Party(f"Māori {i+1}", "M", sh, 0.3))  # share = of Māori-party vote
    for i, sh in enumerate(dirichlet_sorted(rng, p["n_right"])):
        parties.append(Party(f"Right {i+1}", "R", R * sh, 0.15 if i == 0 else rng.uniform(0.2, 0.6)))
    for i, sh in enumerate(centre):
        c = Party(f"Centre {i+1}", "C", sh, 0.3)
        c.ally = rng.choice("LR")
        parties.append(c)
    for name, bloc, sh, ally in (("Left minor", "L", p["minor_left"], "L"),
                                 ("Right minor", "R", p["minor_right"], "R"),
                                 ("Centre minor", "C", p["minor_centre"], p["minor_centre_ally"])):
        x = Party(name, bloc, sh, 0.2)
        x.ally, x.minor = ally, True
        parties.append(x)
    for x in parties:
        if x.bloc == "M":
            x.ally = "L"
    idx = {x.name: i for i, x in enumerate(parties)}
    P = len(parties)
    gen_parties = [i for i, x in enumerate(parties) if x.bloc != "M"]
    maori_parties = [i for i, x in enumerate(parties) if x.bloc == "M"]
    left_gen = [i for i, x in enumerate(parties) if x.bloc == "L" and not getattr(x, "minor", False)]
    minors = {i for i, x in enumerate(parties) if getattr(x, "minor", False)}

    # ---- party votes by electorate ----
    electorates = []  # dicts: kind, size, pv[list P]
    rows = []
    for e in range(N_GEN):
        size = max(30000, rng.gauss(40000, 3000))
        lean = rng.gauss(0, 0.4)
        w = [0.0] * P
        for i in gen_parties:
            x = parties[i]
            side = 0.5 * lean if x.bloc == "L" else -0.5 * lean if x.bloc == "R" else 0.0
            w[i] = x.share * math.exp(side + rng.gauss(0, x.sigma))
        rows.append((size, [w[i] for i in gen_parties]))
    fitted = ipf(rows, [parties[i].share for i in gen_parties])
    for e in range(N_GEN):
        pv = [0.0] * P
        for k, i in enumerate(gen_parties):
            pv[i] = fitted[e][k]
        electorates.append({"kind": "general", "size": rows[e][0], "pv": pv})

    left_total = sum(parties[i].share for i in left_gen)
    for e in range(N_MAORI):
        size = rng.uniform(24000, 30000)
        m = p["maori_party_share"] * math.exp(rng.gauss(0, 0.25))
        m = min(m, 0.9) if maori_parties else 0.0
        pv = [0.0] * P
        for i in maori_parties:
            pv[i] = size * m * parties[i].share * math.exp(rng.gauss(0, 0.3))
        mp = sum(pv[i] for i in maori_parties)
        if mp:
            for i in maori_parties:
                pv[i] *= size * m / mp
        lw = {i: parties[i].share / left_total * math.exp(rng.gauss(0, 0.2)) for i in left_gen}
        sw = sum(lw.values())
        for i in left_gen:
            pv[i] = size * (1 - m) * lw[i] / sw
        electorates.append({"kind": "maori", "size": size, "pv": pv})

    # ---- ballots: party vote × electorate candidate ----
    left1, right1 = idx["Left 1"], idx["Right 1"]
    s_bloc = {"L": p["s_L"], "R": p["s_R"]}
    for el in electorates:
        pv = el["pv"]
        cands = [i for i in range(P) if i not in minors and pv[i] > 0]
        appeal = {c: math.sqrt(pv[c]) * math.exp(rng.gauss(0, 0.8)) for c in cands}
        sa = sum(appeal.values())
        M = [[0.0] * P for _ in range(P)]  # M[party vote][candidate]
        mtarget = max(maori_parties, key=lambda i: pv[i]) if el["kind"] == "maori" and maori_parties else None
        for q in range(P):
            n = pv[q]
            if n <= 0:
                continue
            pers = p["personal"] * n
            for c in cands:
                M[q][c] += pers * appeal[c] / sa
            rest = n - pers
            if q in minors:
                M[q][left1 if parties[q].ally == "L" else right1] += rest
                continue
            x = parties[q]
            if mtarget is not None and x.ally == "L":
                target, s = mtarget, p["s_M"]
            else:
                target = left1 if x.ally == "L" else right1
                s = s_bloc[x.ally]
            if target == q:
                s = 0.0
            M[q][target] += rest * s
            M[q][q] += rest * (1 - s)
        el["M"] = M
        cv = [sum(M[q][c] for q in range(P)) for c in range(P)]
        el["winner"] = max(cands, key=lambda c: cv[c])
        el["cv"] = cv

    votes = [sum(el["pv"][i] for el in electorates) for i in range(P)]
    elec = [0] * P
    for el in electorates:
        elec[el["winner"]] += 1
    total = sum(votes)
    qual = [i for i in range(P) if i not in minors and (votes[i] / total >= THRESHOLD or elec[i] > 0)]

    # Option 2 votes: party vote if it qualifies, else the electorate
    # candidate's party if that qualifies
    qs = set(qual)
    vs = [votes[i] if i in qs else 0.0 for i in range(P)]
    for el in electorates:
        for q in range(P):
            if q in qs:
                continue
            for c in range(P):
                if c in qs:
                    vs[c] += el["M"][q][c]

    # split ballots for each party's winning candidates whose party vote went
    # to another qualifying party (wasted ones are already counted by Option 2)
    pools = {}
    for P_ in qual:
        if not elec[P_]:
            continue
        split = {q: 0.0 for q in qual if q != P_}
        wasted = 0.0
        for el in electorates:
            if el["winner"] == P_:
                for q in split:
                    split[q] += el["M"][q][P_]
                wasted += sum(el["M"][q][P_] for q in range(P) if q not in qs)
        pools[P_] = (wasted, split)

    bloc_votes = {b: sum(votes[i] for i in range(P) if parties[i].ally == b) for b in "LR"}
    # voters who wasted both ticks, by the bloc of their party vote
    both_wasted = {b: 0.0 for b in "LR"}
    for el in electorates:
        for q in range(P):
            if q in qs:
                continue
            both_wasted[parties[q].ally] += sum(el["M"][q][c] for c in range(P) if c not in qs)
    countable = {b: bloc_votes[b] - both_wasted[b] for b in "LR"}
    return {"params": p, "parties": parties, "votes": votes, "o2_votes": vs, "elec": elec, "qual": qual,
            "pools": pools, "total": total, "bloc_votes": bloc_votes, "bloc_votes_countable": countable,
            "both_wasted": sum(both_wasted.values()), "electorates": electorates}


# ======================= seat rules =======================

def sainte_lague(v, qual, H):
    """Seats for parties in `qual` (dict idx -> seats) via divisor bisection."""
    if H <= 0:
        return {i: 0 for i in qual}
    tot = sum(v[i] for i in qual)
    lo, hi = tot / (H + len(qual)) / 2, tot / max(H - len(qual), 1) * 2 + 1
    for _ in range(100):
        d = (lo + hi) / 2
        n = sum(math.floor(v[i] / d + 0.5) for i in qual)
        if n == H:
            return {i: math.floor(v[i] / d + 0.5) for i in qual}
        lo, hi = (d, hi) if n > H else (lo, d)
    # tie: fall back to exact quotients
    q = sorted(((v[i] / (2 * k + 1), i) for i in qual for k in range(H)), reverse=True)[:H]
    out = {i: 0 for i in qual}
    for _, i in q:
        out[i] += 1
    return out


def absorb(v, elec, qual, H):
    """Review rule: any party whose electorates exceed its share keeps them;
    everyone else shares what's left of H. Returns (alloc, absorbed set)."""
    fixed = set()
    while True:
        rest = [i for i in qual if i not in fixed]
        a = sainte_lague(v, rest, H - sum(elec[i] for i in fixed))
        new = {i for i in rest if elec[i] > a[i]}
        if not new:
            a.update({i: elec[i] for i in fixed})
            return a, fixed
        fixed |= new


def current_system(s, H):
    base = sainte_lague(s["votes"], s["qual"], H)
    return {i: max(base[i], s["elec"][i]) for i in s["qual"]}, {}


def proposed_system(s, H, mode, grow=False):
    """mode "T": Overhang Transfer (Option 1); "BV": Backup Vote (Option 2).

    grow=False: any overhang the transfer can't cover is absorbed within H
                (Independent Electoral Review rule).
    grow=True ("-X" systems): it is handled as under current MMP instead: the
                party keeps its extra electorates, other parties keep their
                entitlement on the adjusted votes, and the House grows.
    """
    elec, qual, pools = s["elec"], s["qual"], s["pools"]
    v0 = s["votes"] if mode == "T" else s["o2_votes"]
    use_wasted = mode == "T"  # under BV the wasted votes are already counted
    base = sainte_lague(v0, qual, H)
    over = [i for i in qual if elec[i] > base[i]]
    if not over:
        return base, {"moved": 0.0, "absorbed_parties": [], "mode": mode, "lam": {}}
    lam = {P: 0.0 for P in over}  # 0–1: share of wasted ballots used; 1–2: f = lam − 1

    def adjusted(lam):
        v = list(v0)
        for P, l in lam.items():
            wasted, split = pools[P]
            if use_wasted:
                v[P] += wasted * min(l, 1.0)
            f = max(0.0, l - 1.0)
            for q, n in split.items():
                m = f * n
                v[P] += m; v[q] -= m
        return v

    def final(lam):
        return absorb(adjusted(lam), elec, qual, H)

    def solve():
        for _ in range(20):
            prev = dict(lam)
            for P in over:
                lam[P] = 2.0
                a, fixed = final(lam)
                if P in fixed:
                    continue  # cannot be covered: residual → absorbed
                lo, hi = (0.0 if use_wasted else 1.0), 2.0
                for _ in range(40):
                    lam[P] = (lo + hi) / 2
                    lo, hi = (lo, lam[P]) if P not in final(lam)[1] else (lam[P], hi)
                lam[P] = hi
            if all(abs(lam[P] - prev[P]) < 1e-6 for P in over):
                break

    solve()
    a, fixed = final(lam)
    v = adjusted(lam)
    moved = sum(max(0.0, v[P] - v0[P]) for P in over)
    # lam per overhanging party: 0–1 share of its wasted ballots used (MMP-T),
    # then 1 + f, the fraction of its split ballots transferred (for measures.py)
    detail = {"mode": mode, "lam": dict(lam)}
    if grow and fixed:
        b = sainte_lague(v, qual, H)
        return ({i: max(b[i], elec[i]) for i in qual},
                {"moved": moved, "absorbed_parties": [], "grown_by": sorted(fixed), **detail})
    return a, {"moved": moved, "absorbed_parties": sorted(fixed), **detail}


# name: (seat rule, nominal size, search for extra seats needed?)
SYSTEMS = {
    "MMP":       (current_system, 121, True),
    "MMP-T":     (lambda s, H: proposed_system(s, H, "T"), 121, True),
    "MMP-BV":    (lambda s, H: proposed_system(s, H, "BV"), 121, True),
    "MMP-T-X":   (lambda s, H: proposed_system(s, H, "T", grow=True), 121, True),
    "MMP-BV-X":  (lambda s, H: proposed_system(s, H, "BV", grow=True), 121, True),
    "MMP141":    (current_system, 141, False),
    "MMP-T141":  (lambda s, H: proposed_system(s, H, "T"), 141, False),
    "MMP-BV141": (lambda s, H: proposed_system(s, H, "BV"), 141, False),
    "MMP-T-X141":  (lambda s, H: proposed_system(s, H, "T", grow=True), 141, False),
    "MMP-BV-X141": (lambda s, H: proposed_system(s, H, "BV", grow=True), 141, False),
}


# ======================= measures =======================

def measures(s, alloc, bloc_key="bloc_votes"):
    qual, v = s["qual"], s["votes"]
    bv = s[bloc_key]
    btot = sum(bv.values())
    house = sum(alloc.values())
    vt = sum(v[i] for i in qual)
    ideal = {i: house * v[i] / vt for i in qual}
    short = {i: max(0.0, ideal[i] - alloc[i]) for i in qual}
    lsq = math.sqrt(0.5 * sum((100 * alloc[i] / house - 100 * v[i] / vt) ** 2 for i in qual))
    bloc_short = {}
    for b in "LR":
        seats = sum(alloc[i] for i in qual if s["parties"][i].ally == b)
        bloc_short[b] = max(0.0, house * bv[b] / btot - seats)
    return {"house": house, "gallagher": lsq,
            "party_deficit": sum(short.values()),
            "party_deficit_rounded": sum(math.floor(x + 0.5) for x in short.values()),
            "max_party_deficit": max(short.values()),
            "bloc_deficit": max(bloc_short.values()),
            "bloc_short": bloc_short, "short": short}


def _zeta(arr, n):
    """Subset sums: out[S] = sum of arr[U] over every U ⊆ S."""
    a = arr.copy()
    for i in range(n):
        v = a.reshape(-1, 2, 1 << i)
        v[:, 1, :] += v[:, 0, :]
    return a


def _either_groups(s, unit_of):
    """Ballot groups for the either-choice yardstick over 'units' (parties or
    blocs). unit_of: party index -> unit index for qualifying parties.
    Returns subset sums of the votes forced into each group of units:
      Gm[S]  mandatory ballots whose every option lies in S;
      G[S]   the same plus droppable ones (party vote for a party that didn't
             qualify, candidate's party in S), which may also count for nobody."""
    P = len(s["parties"])
    n = max(unit_of.values()) + 1
    N = s.get("_ballots")
    if N is None:
        N = [[0.0] * P for _ in range(P)]
        for el in s["electorates"]:
            M = el["M"]
            for q in range(P):
                row, out = M[q], N[q]
                for c in range(P):
                    if row[c]:
                        out[c] += row[c]
        s["_ballots"] = N
    mand = np.zeros(1 << n)
    drop = np.zeros(1 << n)
    for q in range(P):
        for c in range(P):
            x = N[q][c]
            if not x:
                continue
            uq, uc = unit_of.get(q), unit_of.get(c)
            if uq is not None:
                mask = 1 << uq
                if uc is not None and c != q:
                    mask |= 1 << uc
                mand[mask] += x
            elif uc is not None:
                drop[1 << uc] += x
    masks = np.arange(1 << n)
    mem = ((masks[:, None] >> np.arange(n)) & 1).astype(float)
    Gm = _zeta(mand, n)
    G = Gm + _zeta(drop, n)
    return {"n": n, "Tm": mand.sum(), "Ta": mand.sum() + drop.sum(), "Gm": Gm[1:], "G": G[1:],
            "mem": mem[1:], "size": mem[1:].sum(axis=1)}


def _either_setup(s):
    if "_either" in s:
        return s["_either"]
    qual = list(s["qual"])
    party = _either_groups(s, {p: k for k, p in enumerate(qual)})
    bloc = _either_groups(s, {p: "LR".index(s["parties"][p].ally) for p in qual})
    s["_either"] = {"qual": qual, "party": party, "bloc": bloc}
    return s["_either"]


def _either_minmax(g, seats, house):
    """Smallest t such that some counting (each voter for one of their own
    choices, or for nobody if their party vote's party didn't qualify) leaves
    no unit more than t seats short. For a fixed t, a counted total T' works
    iff, for every group S (Gale's supply–demand condition, with r = share of
    the house S may hold, (seats_S + |S| t) / house):
        mandatory ballots forced into S  ≤ T' r          and
        all ballots forced into S − T_all ≤ T' (r − 1)."""
    seatsS = g["mem"] @ seats

    def feasible(t):
        r = (seatsS + g["size"] * t) / house
        with np.errstate(divide="ignore", invalid="ignore"):
            need = np.where(g["Gm"] > 0, g["Gm"] / np.where(r > 0, r, np.nan), 0.0)
        if np.isnan(need).any():
            return False
        lower = max(g["Tm"], need.max())
        up = r < 1
        upper = g["Ta"] if not up.any() else min(g["Ta"], ((g["Ta"] - g["G"][up]) / (1 - r[up])).min())
        return lower <= upper * (1 + 1e-12)

    if feasible(0.0):
        return 0.0
    lo, hi = 0.0, float(house)
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if feasible(mid) else (mid, hi)
    return hi


def _either_sum(g, seats, house):
    """Smallest total shortfall over every counting. For a counted total T',
    the votes that must go over the parties' fair caps are
    max(0, max_S [Gm_S − T' seats_S/house], max_S [G_S − T' seats_S/house] − (T_all − T'));
    shortfall in seats = that × house / T'. Minimised over T' on a fine grid."""
    seatsS = g["mem"] @ seats
    Tm, Ta = g["Tm"], g["Ta"]

    def f(T):
        over = max(0.0, (g["Gm"] - T * seatsS / house).max(), (g["G"] - T * seatsS / house).max() - (Ta - T))
        return over * house / T

    if Ta - Tm < 1e-9:
        return f(Ta)
    grid = np.linspace(Tm, Ta, 101)
    vals = [f(T) for T in grid]
    k = int(np.argmin(vals))
    lo, hi = grid[max(k - 1, 0)], grid[min(k + 1, 100)]
    fine = np.linspace(lo, hi, 101)
    return min(min(vals), min(f(T) for T in fine))


def either_measures(s, alloc):
    """Smallest achievable shortfalls when every voter counts for one of their
    own two choices, or for nobody if their party vote's party didn't qualify
    (see module docstring)."""
    e = _either_setup(s)
    house = sum(alloc.values())
    seats = np.array([alloc[p] for p in e["qual"]], dtype=float)
    bseats = np.array([sum(alloc[p] for p in e["qual"] if s["parties"][p].ally == b) for b in "LR"], dtype=float)
    return {"either_party_deficit": _either_sum(e["party"], seats, house),
            "either_max_party_deficit": _either_minmax(e["party"], seats, house),
            "either_bloc_deficit": _either_minmax(e["bloc"], bseats, house)}


def required_size(s, system):
    """Smallest nominal size H >= SEATS meeting (a) party and (b) bloc
    tolerance, and (c) party and (d) bloc tolerance on the either-choice
    yardstick. None = beyond H_MAX."""
    need = [None] * 4
    fn, H0, _ = SYSTEMS[system]
    for H in range(H0, H_MAX + 1):
        alloc = fn(s, H)[0]
        m = measures(s, alloc, "bloc_votes_countable")
        e = either_measures(s, alloc) if ("electorates" in s or "_ballots" in s) else \
            {"either_max_party_deficit": 0.0, "either_bloc_deficit": 0.0}  # history: (c), (d) not computed
        for k, x in enumerate((m["max_party_deficit"], m["bloc_deficit"],
                               e["either_max_party_deficit"], e["either_bloc_deficit"])):
            if need[k] is None and x <= TOL:
                need[k] = H
        if all(need):
            break
    return need


# ======================= runners =======================

def evaluate(s, search=True):
    out = {}
    for name, (fn, H0, do_search) in SYSTEMS.items():
        alloc, info = fn(s, H0)
        m = measures(s, alloc)
        m["bloc_deficit_countable"] = measures(s, alloc, "bloc_votes_countable")["bloc_deficit"]
        if "electorates" in s or "_ballots" in s:  # the 2005–2023 history has no ballot tables here
            m.update(either_measures(s, alloc))
        m["alloc"], m["info"] = alloc, info
        if search and do_search:
            for key, H in zip(("extra_a", "extra_b", "extra_c", "extra_d"), required_size(s, name)):
                m[key] = None if H is None else H - SEATS
        out[name] = m
    return out


def describe(k, s, res, out=sys.stdout):
    print_ = lambda *a: print(*a, file=out)
    p, parties, v, elec, qual = s["params"], s["parties"], s["votes"], s["elec"], s["qual"]
    tot = s["total"]
    base = sainte_lague(v, qual, SEATS)
    print_(f"\n{'=' * 100}\nScenario {k}: Left:Right {p['left_frac']:.0%}:{1-p['left_frac']:.0%} | "
          f"strategic s_L={p['s_L']:.0%} s_R={p['s_R']:.0%} s_M={p['s_M']:.0%} | personal π={p['personal']:.0%} | "
          f"minor parties {p['minor']:.1%} | wasted both ticks {s['both_wasted']/tot:.1%}")
    o2 = s["o2_votes"]
    print_(f"{'party':13s} {'bloc':4s} {'vote%':>6s} {'opt2%':>6s} {'elec':>4s} {'entl':>4s} "
          + " ".join(f"{n[:12]:>12s}" for n in SYSTEMS))
    for i, x in enumerate(parties):
        q = i in qual
        row = f"{x.name:13s} {x.ally:4s} {100*v[i]/tot:6.1f} {100*o2[i]/tot:6.1f} {elec[i]:4d} " \
              f"{base[i] if q else '-':>4} "
        row += " ".join(f"{(str(r['alloc'][i]) + (f' (-{r['short'][i]:.1f})' if r['short'][i] >= 0.05 else '')) if q else 'out':>12s}"
                        for r in res.values())
        print_(row)
    bv = s["bloc_votes"]
    for b in "LR":
        print_(f"{'Bloc ' + b:13s} {'':4s} {100*bv[b]/tot:6.1f} {'':6s} {'':4s} {'':4s} "
              + " ".join(f"{str(sum(r['alloc'][i] for i in qual if parties[i].ally == b)) + (f' (-{r['bloc_short'][b]:.1f})' if r['bloc_short'][b] >= 0.05 else ''):>12s}" for r in res.values()))
    print_("  (party shortfalls against the party yardstick; bloc shortfalls against the bloc yardstick)")
    for key, lab in [("gallagher", "Gallagher"), ("party_deficit", "Party seat deficit"),
                     ("party_deficit_rounded", "Party deficit (rounded)"), ("max_party_deficit", "Max party deficit"),
                     ("bloc_deficit", "Bloc seat deficit"),
                     ("bloc_deficit_countable", "Bloc deficit (countable)"),
                     ("either_party_deficit", "Either-choice party deficit"),
                     ("either_max_party_deficit", "Either-choice max party def."),
                     ("either_bloc_deficit", "Either-choice bloc deficit"),
                     ("extra_a", "Extra seats (a) party≤1"), ("extra_b", "Extra seats (b) bloc≤1"),
                     ("extra_c", "Extra (c) either-party≤1"), ("extra_d", "Extra (d) either-bloc≤1")]:
        vals = []
        for n in SYSTEMS:
            x = res[n].get(key)
            vals.append(("-" if not SYSTEMS[n][2] else ">" + str(H_MAX - SEATS)) if x is None and key.startswith("extra")
                        else f"{x:.2f}" if isinstance(x, float) else str(x))
        print_(f"  {lab:31s} " + " ".join(f"{x:>12s}" for x in vals))


def flat(k, s, res):
    p = s["params"]
    ov = sum(max(0, s["elec"][i] - b) for i, b in sainte_lague(s["votes"], s["qual"], SEATS).items())
    row = {"scenario": k, **{kk: round(vv, 4) if isinstance(vv, float) else vv for kk, vv in p.items()},
           "overhang_base": ov, "both_wasted_pct": round(100 * s["both_wasted"] / s["total"], 2),
           "maori_overhang_base": sum(max(0, s["elec"][i] - b) for i, b in
                                     sainte_lague(s["votes"], s["qual"], SEATS).items() if s["parties"][i].bloc == "M")}
    for name, m in res.items():
        tag = name
        for key in ("house", "gallagher", "party_deficit", "party_deficit_rounded", "max_party_deficit",
                    "bloc_deficit", "bloc_deficit_countable", "either_party_deficit",
                    "either_max_party_deficit", "either_bloc_deficit",
                    "extra_a", "extra_b", "extra_c", "extra_d"):
            x = m.get(key)
            row[f"{tag}_{key}"] = round(x, 3) if isinstance(x, float) else x
    return row


def run_one(k):
    rng = random.Random(1000 + k)
    s = gen_scenario(rng)
    return flat(k, s, evaluate(s))


def record(exp, key, s, res, meta=None):
    """Raw result of one scenario for runs/<exp>/records.jsonl.gz (see measures.py)."""
    import measures as ms
    els = [{"M": el["M"], "cv": el["cv"], "winner": el["winner"], "maori": el["kind"] == "maori"}
           for el in s["electorates"]]
    P = len(s["parties"])
    st = ms.build_state(ms.meta_from_party_objs(s["parties"]), els, s["votes"], s["elec"], s["qual"])
    systems = {}
    for name, r in res.items():
        x = {"H0": SYSTEMS[name][1], "alloc": ms.alloc_list(r["alloc"], P), "info": ms.info_json(r["info"])}
        if "extra_a" in r:
            x["extra"] = [r.get(f"extra_{c}") for c in "abcd"]
        systems[name] = x
    p = dict(meta if meta is not None else s["params"])
    return {"exp": exp, "key": key, "meta": {k: (round(v, 4) if isinstance(v, float) else v) for k, v in p.items()},
            "state": st, "systems": systems}


def store_one(k):
    s = gen_scenario(random.Random(1000 + k))
    return record("exp1", {"scenario": k}, s, evaluate(s))


def store(n, fn, out_dir):
    """Run n scenarios with fn(k) → record; write runs/<dir>/records.jsonl.gz."""
    from multiprocessing import Pool
    import measures as ms
    w = ms.RecordWriter(f"{out_dir}/records.jsonl.gz")
    with Pool() as pool:
        for i, rec in enumerate(pool.imap(fn, range(n), chunksize=4)):
            w.write(rec)
            if (i + 1) % 500 == 0:
                print(f"  {i + 1}/{n}", flush=True)
    w.close()
    print(f"wrote {n} records to {out_dir}/records.jsonl.gz")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    if mode == "test":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        with open("mc_test_output.txt", "w", encoding="utf-8") as f:
            for k in range(n):
                s = gen_scenario(random.Random(1000 + k))
                describe(k, s, evaluate(s), f)
        print(f"wrote {n} scenarios to mc_test_output.txt")
    elif mode == "store":  # raw results for measures.py
        store(int(sys.argv[2]), store_one, sys.argv[3] if len(sys.argv) > 3 else "runs/exp1")
    else:
        from multiprocessing import Pool
        n = int(sys.argv[2])
        with Pool() as pool:
            rows = pool.map(run_one, range(n), chunksize=8)
        with open("mc_results.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
        print(f"wrote {len(rows)} scenarios to mc_results.csv")
