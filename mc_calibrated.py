"""Monte Carlo calibrated to New Zealand elections, 2005–2023.

Same structure, seat rules and measures as mc_overhang.py, but every scenario
parameter is drawn from the range actually seen across the seven elections
(see calibrate_history.py and calibration.json). Ranges are made symmetric
between the blocs, so neither side is favoured.

| Parameter                              | Drawn from          | Seen 2005–2023                 |
|----------------------------------------|---------------------|--------------------------------|
| Left share of the Left+Right vote      | U(0.36, 0.64)       | 0.44–0.64                      |
| Bloc parties ≥1% (incl. leader), each  | {1,2,3} as observed | left 2–3, right 1–3            |
| Leader's share of its bloc's vote      | U(0.70, 0.96)       | Labour 0.70–0.86, Nat 0.74–1.0 |
| Centrist parties                       | 1–2 as observed     | NZ First, United Future, TOP   |
|   first (NZ First-like) / second       | U(2.6, 8.7)% / U(1.5, 2.7)% |                        |
| Parties under 1% (no candidates)       | U(1.2, 4.3)% total  | 1.2–4.3%                       |
| Māori parties                          | 1 (5/7) or 2 (2/7)  | 1–2                            |
| Māori-party share in Māori electorates | U(0.12, 0.30)       | 0.12–0.30                      |
| Strategic rate, each partner/centrist  | ABC posterior, pooled over parties (see below) |      |
| Māori-electorate strategic s_M (Labour | ABC posterior, joint draw from one election    |      |
|   voters), s_Mo (other Left voters),   |                     |                                |
|   personal vote π, appeal              |                     |                                |
|   spread σ_a, standouts n_st and d     |                     |                                |
| Left–right lean SD (logit)             | U(0.43, 0.53)       | 0.43–0.53                      |
| Local spread SD: leaders / others      | U(0.06, 0.13) / U(0.21, 0.48) | as left             |
| Valid votes: general / Māori electorate| mean U(33k, 42k) / U(18k, 27k) | as left           |

Behavioural parameters come from abc_history.py, which fits them to each
election's actual electorate results and split-vote tables (approximate
Bayesian computation, abc_posterior.json):
  • each scenario takes one joint draw (π, s_M, s_Mo, σ_a, n_st, d) from the
    posterior of a randomly chosen election;
  • each partner party and centrist takes its own strategic rate from a
    random historical partner party's posterior (Greens, ACT, Progressive,
    Conservatives, NZ Loyal, ...), so blocs are treated symmetrically.
s_L and s_R are reported as the vote-weighted average of the rates of each
bloc's partners and allied centrists.

Standout candidates: at every election 1–5 general electorates were won by a
party other than Labour or National, almost always because the big ally's
voters backed that candidate (Epsom, Ōhāriu, Wigram) or a strong local
candidate drew them (Auckland Central, Wellington Central). Each scenario has
n_st standouts, each for a random smaller general party in one of its stronger
electorates (weight ∝ its local share³ × its bloc's local share⁶, so mostly
safe seats for its side); there a share d of the voters who would have backed
their bloc leader's candidate back the standout instead. They need not win.

Simplifications kept from mc_overhang.py: Māori electorates vote only for
Māori parties and Left parties; Māori parties get no votes elsewhere;
centrists' ally is chosen at random.

Run:  python3 mc_calibrated.py test [N]   (N scenarios → mc_calibrated_test.txt)
      python3 mc_calibrated.py run N      (N scenarios → mc_results_calibrated.csv)
      python3 mc_calibrated.py store N    (raw results → runs/exp2/records.jsonl.gz; then
                                           python3 measures.py recompute runs/exp2)
"""
import csv
import json
import math
import random
import sys
from pathlib import Path

import mc_overhang as m
from mc_overhang import Party, dirichlet_sorted, ipf, N_GEN, N_MAORI, THRESHOLD


_POST = None


def posterior():
    """(per-election joint draws, pooled per-party strategic-rate draws)."""
    global _POST
    if _POST is None:
        d = json.loads((Path(__file__).parent / "abc_posterior.json").read_text())
        joint = {y: v["posterior"] for y, v in d.items()}
        partners = [[t["s_party"][q] for t in v["posterior"]] for v in d.values() for q in v["partners"]]
        _POST = (joint, partners)
    return _POST


def draw_params(rng):
    p = {}
    p["left_frac"] = rng.uniform(0.36, 0.64)
    p["n_left"] = rng.choice([3, 2, 2, 2, 2, 2, 2])   # observed left counts
    p["n_right"] = rng.choice([2, 2, 3, 2, 1, 3, 3])  # observed right counts
    p["n_centre"] = rng.choice([2, 1, 1, 1, 2, 2, 2])
    p["n_maori"] = rng.choice([1, 1, 2, 2, 1, 1, 1])
    p["leader_L"], p["leader_R"] = rng.uniform(0.70, 0.96), rng.uniform(0.70, 0.96)
    p["minor"] = rng.uniform(0.012, 0.043)
    p["maori_party_share"] = rng.uniform(0.12, 0.30)
    joint, _ = posterior()
    p["abc_year"] = rng.choice(sorted(joint))
    t = rng.choice(joint[p["abc_year"]])
    p["personal"], p["s_M"], p["s_Mo"], p["sigma_a"] = t["pi"], t["s_M"], t["s_Mo"], t["sigma_a"]
    p["n_standout"], p["standout_d"] = t["n_st"], t["d"]
    p["lean_sd"] = rng.uniform(0.43, 0.53)
    p["gen_size"], p["maori_size"] = rng.uniform(33000, 42000), rng.uniform(18000, 27000)
    return p


def bloc_shares(rng, n, leader):
    if n == 1:
        return [1.0]
    rest = dirichlet_sorted(rng, n - 1)
    return [leader] + [(1 - leader) * x for x in rest]


def gen_scenario(rng):
    p = draw_params(rng)
    parties = []
    centre = [rng.uniform(0.026, 0.087)] + ([rng.uniform(0.015, 0.027)] if p["n_centre"] == 2 else [])
    mx = [rng.expovariate(1.0) for _ in range(3)]
    p["minor_left"], p["minor_right"], p["minor_centre"] = (p["minor"] * x / sum(mx) for x in mx)
    p["minor_centre_ally"] = rng.choice("LR")
    blocs = 1 - p["minor"] - sum(centre)
    L, R = blocs * p["left_frac"], blocs * (1 - p["left_frac"])
    sig = lambda i: rng.uniform(0.06, 0.13) if i == 0 else rng.uniform(0.21, 0.48)
    for i, sh in enumerate(bloc_shares(rng, p["n_left"], p["leader_L"])):
        parties.append(Party(f"Left {i+1}", "L", L * sh, sig(i)))
    for i, sh in enumerate(dirichlet_sorted(rng, p["n_maori"])):
        parties.append(Party(f"Māori {i+1}", "M", sh, 0.3))
    for i, sh in enumerate(bloc_shares(rng, p["n_right"], p["leader_R"])):
        parties.append(Party(f"Right {i+1}", "R", R * sh, sig(i)))
    for i, sh in enumerate(centre):
        c = Party(f"Centre {i+1}", "C", sh, rng.uniform(0.21, 0.48))
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
    # strategic rate for each partner party and centrist, from a random
    # historical partner party's posterior
    _, pool = posterior()
    for x in parties:
        if x.bloc in ("L", "R", "C") and not getattr(x, "minor", False) and x.name not in ("Left 1", "Right 1"):
            x.s = rng.choice(rng.choice(pool))
    for b in "LR":
        xs = [x for x in parties if hasattr(x, "s") and x.ally == b]
        w = sum(x.share for x in xs)
        p[f"s_{b}"] = sum(x.s * x.share for x in xs) / w if w else 0.0
    return build(rng, p, parties)


def build(rng, p, parties):
    """Electorate votes and ballots: as mc_overhang.gen_scenario, with
    calibrated lean, turnout and personal vote."""
    idx = {x.name: i for i, x in enumerate(parties)}
    P = len(parties)
    gen_parties = [i for i, x in enumerate(parties) if x.bloc != "M"]
    maori_parties = [i for i, x in enumerate(parties) if x.bloc == "M"]
    left_gen = [i for i, x in enumerate(parties) if x.bloc == "L" and not getattr(x, "minor", False)]
    minors = {i for i, x in enumerate(parties) if getattr(x, "minor", False)}

    electorates, rows = [], []
    for e in range(N_GEN):
        size = max(20000, rng.gauss(p["gen_size"], 3000))
        lean = rng.gauss(0, p["lean_sd"])
        w = [0.0] * P
        for i in gen_parties:
            x = parties[i]
            side = 0.5 * lean if x.ally == "L" and x.bloc != "C" else -0.5 * lean if x.ally == "R" and x.bloc != "C" else 0.0
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
        size = max(12000, rng.gauss(p["maori_size"], 2000))
        mshare = min(0.9, p["maori_party_share"] * math.exp(rng.gauss(0, 0.25)))
        pv = [0.0] * P
        for i in maori_parties:
            pv[i] = parties[i].share * math.exp(rng.gauss(0, 0.3))
        mp = sum(pv[i] for i in maori_parties)
        for i in maori_parties:
            pv[i] *= size * mshare / mp
        lw = {i: parties[i].share / left_total * math.exp(rng.gauss(0, 0.2)) for i in left_gen}
        sw = sum(lw.values())
        for i in left_gen:
            pv[i] = size * (1 - mshare) * lw[i] / sw
        electorates.append({"kind": "maori", "size": size, "pv": pv})

    left1, right1 = idx["Left 1"], idx["Right 1"]
    s_bloc = {"L": p["s_L"], "R": p["s_R"]}
    for el in electorates:
        pv = el["pv"]
        cands = [i for i in range(P) if i not in minors and pv[i] > 0]
        appeal = {c: math.sqrt(pv[c]) * math.exp(rng.gauss(0, p["sigma_a"])) for c in cands}
        sa = sum(appeal.values())
        M = [[0.0] * P for _ in range(P)]
        mtarget = max(maori_parties, key=lambda i: pv[i]) if el["kind"] == "maori" else None
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
                target, s = mtarget, (p["s_M"] if q == left1 else p["s_Mo"])
            else:
                target = left1 if x.ally == "L" else right1
                s = getattr(x, "s", s_bloc[x.ally])
            if target == q:
                s = 0.0
            M[q][target] += rest * s
            M[q][q] += rest * (1 - s)
        el["M"] = M
        el["cands"] = cands

    # standout local candidates
    leaders = {"L": left1, "R": right1}
    eligible = [i for i, x in enumerate(parties)
                if x.bloc in ("L", "R", "C") and i not in minors and i not in (left1, right1)]
    gens = [el for el in electorates if el["kind"] == "general"]
    used = set()
    p["standouts"] = []
    for _ in range(p["n_standout"] if eligible else 0):
        c = rng.choice(eligible)
        ally = parties[c].ally
        opts = [k for k in range(len(gens)) if k not in used]
        side = [i for i in range(P) if parties[i].ally == ally]
        wts = [(gens[k]["pv"][c] / gens[k]["size"]) ** 3
               * (sum(gens[k]["pv"][i] for i in side) / gens[k]["size"]) ** 6 for k in opts]
        k = rng.choices(opts, weights=wts)[0]
        used.add(k)
        d = p["standout_d"]
        ldr, M = leaders[ally], gens[k]["M"]
        for q in range(P):
            if q != c and parties[q].ally == ally:
                moved = d * M[q][ldr]
                M[q][ldr] -= moved; M[q][c] += moved
        p["standouts"].append((parties[c].name, k, round(d, 2)))

    for el in electorates:
        M = el["M"]
        cv = [sum(M[q][c] for q in range(P)) for c in range(P)]
        el["winner"] = max(el["cands"], key=lambda c: cv[c])
        el["cv"] = cv

    votes = [sum(el["pv"][i] for el in electorates) for i in range(P)]
    elec = [0] * P
    for el in electorates:
        elec[el["winner"]] += 1
    total = sum(votes)
    qual = [i for i in range(P) if i not in minors and (votes[i] / total >= THRESHOLD or elec[i] > 0)]
    qs = set(qual)
    vs = [votes[i] if i in qs else 0.0 for i in range(P)]
    for el in electorates:
        for q in range(P):
            if q in qs:
                continue
            for c in qs:
                vs[c] += el["M"][q][c]
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
    both_wasted = {b: 0.0 for b in "LR"}
    for el in electorates:
        for q in range(P):
            if q not in qs:
                both_wasted[parties[q].ally] += sum(el["M"][q][c] for c in range(P) if c not in qs)
    return {"params": p, "parties": parties, "votes": votes, "o2_votes": vs, "elec": elec, "qual": qual,
            "pools": pools, "total": total, "bloc_votes": bloc_votes,
            "bloc_votes_countable": {b: bloc_votes[b] - both_wasted[b] for b in "LR"},
            "both_wasted": sum(both_wasted.values()), "electorates": electorates}


def validation(s):
    """Features to compare with real elections."""
    parties, el = s["parties"], s["electorates"]
    l1, r1 = [i for i, x in enumerate(parties) if x.name in ("Left 1", "Right 1")]
    gen = [e for e in el if e["kind"] == "general"]
    nonleader = sum(1 for e in gen if e["winner"] not in (l1, r1))
    margins = []
    for e in gen:
        tot = sum(e["cv"])
        margins.append(abs(e["cv"][l1] - e["cv"][r1]) / tot)
    margins.sort()
    return {"nonleader_general_wins": nonleader,
            "leader_margin_median": margins[len(margins) // 2],
            "leader_margin_lt5": sum(x < .05 for x in margins) / len(margins),
            "maori_party_wins": sum(1 for e in el if parties[e["winner"]].bloc == "M")}


def run_one(k):
    s = gen_scenario(random.Random(50_000 + k))
    row = m.flat(k, s, m.evaluate(s))
    row.update(validation(s))
    return row


def store_one(k):
    """Raw result for runs/exp2/records.jsonl.gz (see measures.py)."""
    s = gen_scenario(random.Random(50_000 + k))
    meta = dict(s["params"])
    meta["standouts"] = json.dumps(meta.get("standouts", []))
    meta.update(validation(s))
    return m.record("exp2", {"scenario": k}, s, m.evaluate(s), meta)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    if mode == "store":
        m.store(int(sys.argv[2]), store_one, sys.argv[3] if len(sys.argv) > 3 else "runs/exp2")
        sys.exit()
    if mode == "test":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        with open("mc_calibrated_test.txt", "w", encoding="utf-8") as f:
            for k in range(n):
                s = gen_scenario(random.Random(50_000 + k))
                m.describe(k, s, m.evaluate(s), f)
                print("  validation:", validation(s), file=f)
        print(f"wrote {n} scenarios to mc_calibrated_test.txt")
    else:
        from multiprocessing import Pool
        n = int(sys.argv[2])
        with Pool() as pool:
            rows = pool.map(run_one, range(n), chunksize=8)
        with open("mc_results_calibrated.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
        print(f"wrote {len(rows)} scenarios to mc_results_calibrated.csv")
