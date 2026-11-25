"""Shared measures for Experiments 1–3, computed from stored raw results.

Every simulated or historical election is stored as a compact *ballot state*:
enough to rerun any seat rule and recompute any measure without rerunning the
Monte Carlo. The runs write one JSON line per state to
runs/<experiment>/records.jsonl.gz:

  {"exp": "exp1", "key": {...ids...}, "meta": {...scenario parameters...},
   "state": {
     "names": [...], "ally": ["L"|"R", ...],
     "kind":  ["bloc"|"maori"|"centre"|"minor", ...],
     "votes": [party votes], "elec": [electorates won], "qual": [qualifying idx],
     "threshold": 0.05,
     "N": P×P national ballots, N[q][c] = party vote q, electorate vote for c's candidate
          (c = P means no candidate / informal electorate vote),
     "W": P×P, the same but only ballots for the winning candidate in their electorate,
     "el": per electorate [maori 0/1, valid votes, winner, winner votes, runner-up, runner-up votes]
   },
   "systems": {name: {"H0": nominal size, "alloc": [seats per party],
                      "info": {...transfer details...}, "extra": [a, b, c, d] or absent}}}

Ballot counts are rounded to whole votes. Experiments 1 and 2 store all ten
systems against one state per scenario. Experiment 3 stores one state per
walk × pathway × year, because each pathway's voters behave differently.

Then:
    python3 measures.py recompute runs/<experiment>   → runs/<experiment>/measures.csv

recomputes every measure below (and the comparator rules) from the stored
states, in parallel. Changing a measure means editing this file and
recomputing, never rerunning the simulations.

Measures (decided before the rerun; see measures_deliberations_combined.md):

  Proportionality bracket (Gallagher form, 0 = perfect)
    gallagher_all    A  standard Gallagher: every party, share of all party votes
    gallagher_qual   B  qualifying parties only (what Experiments 1–3 reported)
    os_D_win         D  one-share: each voter whose party vote qualifies counts once,
                        for their party vote or, if it elected someone, their
                        electorate vote; best case over every such counting
    os_D_any            as D, but any qualifying electorate candidate may carry the share
    os_C_win         C  as D, plus voters whose party vote failed the threshold
                        count for their electorate candidate's party if that
                        candidate won (they are rescued, as under the Backup Vote)
    os_C_any            as C, any qualifying candidate
    lh_all, lh_qual     Loosemore–Hanby (half the summed absolute gaps, %)
    sli_all             Sainte-Laguë index (Σ (s−v)²/v, %)
  Bloc fairness (seats; Left/Right with centrists counted with their ally)
    bloc_deficit_all        worse-off bloc's shortfall against its share of all party votes
    bloc_deficit_qual       … against its share of qualifying party votes
    bloc_deficit_countable  … all votes minus voters who wasted both ticks
    bloc_deficit_os         … against the one-share (D, winning-candidate) counting
    bloc_gap_L              signed: Left seats minus Left's fair share (all votes)
    inversion_all           the bloc with fewer party votes (all) holds a majority
    inversion_qual          … fewer qualifying party votes
    inversion_nocentre      centrists set aside: a bloc with fewer non-centrist votes
                            holds a majority of the House on its own
  Cost of the rule
    overridden_pct          qualifying party votes counted for another party (% of all votes)
    rescued_pct             sub-threshold party votes counted for a candidate's party
    touched_pct             voters any part of whose party vote was moved
    max_party_overridden_pct  the worst-hit party: share of its party vote moved away
    seats_lost_max          most seats any party loses against its raw entitlement at H0
    parties_lost_2plus      parties losing two or more seats that way
    unseated                electorates whose winner does not take the seat
  Size
    house, house_excess (house − H0), overhang (raw, at H0)

Comparator rules (fixed ballots; Spinoff "ten ways to fix MMP", 19 Nov 2026).
In scope for the reports: CMP-Review141 and the PR benchmarks. The others are
computed for completeness but kept out of the tables (user decision, 24 Nov 2026).
    CMP-Review141   the Review's cap at the enlarged size: overhang absorbed within a
                    fixed 141 seats (140 for the 2005–2023 elections); in Experiment 3
                    applied to the MMP141 pathway's ballots
    CMP-Review      Option 1: overhang absorbed within H0 (2012 and 2023 reviews)
    CMP-German      Option 4: a party gets no more than its entitlement; its
                    lowest-margin electorate winners are not seated
    CMP-German-gen  Option 4 for general electorates only: Māori-electorate
                    winners are always seated (any excess grows the House)
    CMP-Letter2     open letter: each party keeps up to 2 overhang seats, then Option 4
    CMP-Compensate  Option 3: the House grows until no party has fewer seats than electorates
                    (searched to 400 seats; "capped" in info if not reached)
    CMP-Compensate-gen  Option 3 for general-electorate overhang only; Māori-electorate
                    overhang stays as overhang seats
    PR5, PR3.5      Option 9: pure PR on party votes (no electorates), 5% / 3.5% threshold
"""
import csv
import gzip
import json
import math
import sys
from pathlib import Path

import numpy as np

import mc_overhang as m

ROOT = Path(__file__).parent


# ======================= states =======================

def build_state(meta_parties, els, votes, elec, qual, threshold=0.05):
    """meta_parties: list of (name, ally, kind). els: list of dicts with
    "M" (P×P ballots), "cv" (candidate votes), "winner", "maori" (bool)."""
    P = len(meta_parties)
    N = [[0.0] * (P + 1) for _ in range(P)]
    W = [[0.0] * P for _ in range(P)]
    el_out = []
    for e in els:
        M, w = e["M"], e["winner"]
        for q in range(P):
            row, out = M[q], N[q]
            for c in range(P):
                if row[c]:
                    out[c] += row[c]
            W[q][w] += row[w]
        cv = e["cv"]
        order = sorted(range(P), key=lambda c: -cv[c])
        second = next((c for c in order if c != w), w)
        el_out.append([int(bool(e["maori"])), round(sum(cv)), w, round(cv[w]), second, round(cv[second])])
    return {
        "names": [x[0] for x in meta_parties], "ally": [x[1] for x in meta_parties],
        "kind": [x[2] for x in meta_parties],
        "votes": [round(v) for v in votes], "elec": list(elec), "qual": list(qual), "threshold": threshold,
        "N": [[round(x) for x in r] for r in N], "W": [[round(x) for x in r] for r in W], "el": el_out,
    }


def meta_from_party_objs(parties):
    """Experiments 1–2 Party objects → (name, ally, kind)."""
    out = []
    for x in parties:
        kind = ("minor" if getattr(x, "minor", False) else "maori" if x.bloc == "M"
                else "centre" if x.bloc == "C" else "bloc")
        out.append((x.name, x.ally, kind))
    return out


def alloc_list(alloc, P):
    return [int(alloc.get(i, 0)) for i in range(P)]


def info_json(info):
    out = {}
    for k, v in (info or {}).items():
        if k == "lam":
            out[k] = {str(i): round(x, 6) for i, x in v.items()}
        elif isinstance(v, float):
            out[k] = round(v, 1)
        else:
            out[k] = v
    return out


def scenario(st, threshold=None):
    """Rebuild the scenario dict mc_overhang's seat rules expect from a state."""
    P = len(st["names"])
    votes = [float(v) for v in st["votes"]]
    elec = st["elec"]
    total = sum(votes)
    if threshold is None:
        qual = list(st["qual"])
    else:
        qual = [i for i in range(P) if st["kind"][i] != "minor" and (votes[i] / total >= threshold or elec[i] > 0)]
    qs = set(qual)
    N, W = st["N"], st["W"]
    o2 = [votes[i] if i in qs else 0.0 for i in range(P)]
    for q in range(P):
        if q not in qs:
            for c in qual:
                o2[c] += N[q][c]
    pools = {}
    for Pp in qual:
        if elec[Pp]:
            pools[Pp] = (float(sum(W[q][Pp] for q in range(P) if q not in qs)),
                         {q: float(W[q][Pp]) for q in qual if q != Pp})
    parties = []
    for n, a, k in zip(st["names"], st["ally"], st["kind"]):
        x = m.Party(n, a)
        x.ally = a
        x.bloc = "M" if k == "maori" else "C" if k == "centre" else a
        if k == "minor":
            x.minor = True
        parties.append(x)
    bloc_votes = {b: sum(votes[i] for i in range(P) if st["ally"][i] == b) for b in "LR"}
    both = {b: 0.0 for b in "LR"}
    for q in range(P):
        if q not in qs:
            both[st["ally"][q]] += sum(N[q][c] for c in range(P + 1) if c not in qs)
    return {"params": {}, "parties": parties, "votes": votes, "o2_votes": o2, "elec": list(elec), "qual": qual,
            "pools": pools, "total": total, "bloc_votes": bloc_votes,
            "bloc_votes_countable": {b: bloc_votes[b] - both[b] for b in "LR"},
            "both_wasted": sum(both.values())}


# ======================= one-share counting =======================

def _one_share_parts(st, units, variant):
    """Counted votes for the one-share measure.

    units: party index -> unit index (qualifying parties only, or blocs).
    variant: "D_win", "D_any", "C_win", "C_any" (see module docstring).
    Returns (base vector with every flexible ballot counted for its party
    vote, edge from-units, edge to-units, edge amounts)."""
    P = len(st["names"])
    N, W = st["N"], st["W"]
    qual = set(st["qual"])
    n = max(units.values()) + 1
    base = np.zeros(n)
    flows = {}
    win = variant.endswith("win")
    rescue = variant.startswith("C")
    for q in range(P):
        for c in range(P + 1):
            x = N[q][c]
            if not x:
                continue
            w = W[q][c] if c < P else 0
            if q in qual:
                uq = units[q]
                base[uq] += x
                if c < P and c in qual and c != q:
                    uc = units[c]
                    amt = w if win else x
                    if uc != uq and amt > 0:
                        flows[(uq, uc)] = flows.get((uq, uc), 0.0) + amt
            elif rescue and c < P and c in qual:
                base[units[c]] += w if win else x
    if flows:
        keys = list(flows)
        fr = np.array([k[0] for k in keys]); to = np.array([k[1] for k in keys])
        amt = np.array([flows[k] for k in keys])
    else:
        fr = to = np.zeros(0, dtype=int); amt = np.zeros(0)
    return base, fr, to, amt


def one_share_gallagher(base, fr, to, amt, seats, iters=20000, tol=1e-10):
    """min over countings of the Gallagher index. Convex QP over the flows
    (box-constrained), solved by accelerated projected gradient."""
    T = base.sum()
    house = seats.sum()
    if T <= 0 or house <= 0:
        return float("nan"), None
    n = len(base)
    t = seats / house
    b = base / T
    a = amt / T
    if len(a) == 0:
        V = b
    else:
        deg = np.bincount(fr, minlength=n) + np.bincount(to, minlength=n)
        L = 4.0 * deg.max()
        x = np.zeros_like(a); y = x.copy(); tk = 1.0

        def resid(z):
            return b + np.bincount(to, z, n) - np.bincount(fr, z, n) - t

        for it in range(iters):
            r = resid(y)
            g = 2 * (r[to] - r[fr])
            xn = np.clip(y - g / L, 0.0, a)
            tn = (1 + math.sqrt(1 + 4 * tk * tk)) / 2
            y = xn + ((tk - 1) / tn) * (xn - x)
            x, tk = xn, tn
            if it % 25 == 24:
                r = resid(x)
                g = 2 * (r[to] - r[fr])
                pg = np.where(x <= 0, np.minimum(g, 0), np.where(x >= a, np.maximum(g, 0), g))
                if np.abs(pg).max() < tol:
                    break
                if it % 500 == 499:  # restart momentum
                    y = x.copy(); tk = 1.0
        V = b + np.bincount(to, x, n) - np.bincount(fr, x, n)
    return math.sqrt(0.5 * float(((100 * V - 100 * t) ** 2).sum())), V


def one_share_bloc(st, alloc, house):
    """Bloc deficit (seats) under the best one-share counting (D, winning candidates)."""
    qual = st["qual"]
    units = {p: "LR".index(st["ally"][p]) for p in qual}
    base, fr, to, amt = _one_share_parts(st, units, "D_win")
    T = base.sum()
    if T <= 0:
        return float("nan")
    sL = sum(alloc[p] for p in qual if st["ally"][p] == "L")
    inL = amt[(to == 0)].sum() if len(amt) else 0.0
    outL = amt[(fr == 0)].sum() if len(amt) else 0.0
    lo, hi = base[0] - outL, base[0] + inL
    target = sL / house * T
    VL = min(max(target, lo), hi)
    fairL = house * VL / T
    return max(fairL - sL, (house - fairL) - (house - sL), 0.0)


# ======================= comparator rules =======================

def _margin_order(st, party):
    """Electorates won by `party`, highest winning margin (share) first."""
    out = []
    for k, (mao, tot, w, wv, sec, sv) in enumerate(st["el"]):
        if w == party:
            out.append(((wv - sv) / tot if tot else 1.0, k, mao))
    return sorted(out, reverse=True)


def rule_review(s, st, H):
    a, fixed = m.absorb(s["votes"], s["elec"], s["qual"], H)
    return a, {"absorbed_parties": sorted(fixed)}


def rule_german(s, st, H, keep_extra=0, exempt_maori=False):
    ent = m.sainte_lague(s["votes"], s["qual"], H)
    alloc, unseated = dict(ent), 0
    for p in s["qual"]:
        e = s["elec"][p]
        if e <= ent[p]:
            continue
        cap = ent[p] + keep_extra
        if exempt_maori:  # Māori-electorate winners always seated; general ones up to the cap
            maori = sum(1 for x in _margin_order(st, p) if x[2])
            seated = maori + min(e - maori, max(0, cap - maori))
        else:  # lowest-margin winners lose out first (only the count matters for seats)
            seated = min(cap, e)
        unseated += e - seated
        alloc[p] = max(ent[p], seated)
    return alloc, {"unseated": unseated}


def rule_compensate(s, st, H, H_max=400, general_only=False):
    """Grow the House until no party has fewer seats than electorates.
    general_only: Māori-electorate overhang is left as overhang seats (as now)
    and only general-electorate overhang is compensated."""
    need = list(s["elec"])
    if general_only:
        for p in s["qual"]:
            need[p] = sum(1 for e in st["el"] if e[2] == p and not e[0])
    def ok(h):
        a = m.sainte_lague(s["votes"], s["qual"], h)
        return a if all(a[p] >= need[p] for p in s["qual"]) else None

    # Sainte-Laguë is house-monotone, so the smallest sufficient size can be bisected
    if ok(H_max) is None:
        a = m.sainte_lague(s["votes"], s["qual"], H_max)
        return {p: max(a[p], s["elec"][p]) for p in s["qual"]}, {"capped": True}
    lo, hi = H - 1, H_max
    while hi - lo > 1:
        mid = (lo + hi) // 2
        lo, hi = (lo, mid) if ok(mid) is not None else (mid, hi)
    a = ok(hi)
    return {p: max(a[p], s["elec"][p]) for p in s["qual"]}, {}


def rule_pr(st, H, thr):
    votes = st["votes"]
    total = sum(votes)
    q = [i for i in range(len(votes)) if st["kind"][i] != "minor" and votes[i] / total >= thr]
    return m.sainte_lague([float(v) for v in votes], q, H), {"qual": q}


COMPARATORS = {
    "CMP-Review": lambda s, st, H: rule_review(s, st, H),
    "CMP-German": lambda s, st, H: rule_german(s, st, H),
    "CMP-German-gen": lambda s, st, H: rule_german(s, st, H, exempt_maori=True),
    "CMP-Letter2": lambda s, st, H: rule_german(s, st, H, keep_extra=2),
    "CMP-Compensate": lambda s, st, H: rule_compensate(s, st, H),
    "CMP-Compensate-gen": lambda s, st, H: rule_compensate(s, st, H, general_only=True),
}


# ======================= measures =======================

def _gallagher(seat_sh, vote_sh):
    return math.sqrt(0.5 * sum((100 * a - 100 * b) ** 2 for a, b in zip(seat_sh, vote_sh)))


def compute(st, alloc, info, H0, system=""):
    """All measures for one allocation (list of seats per party) on one state."""
    P = len(st["names"])
    votes = [float(v) for v in st["votes"]]
    total = sum(votes)
    qual = st["qual"]
    qs = set(qual)
    ally = st["ally"]
    house = sum(alloc)
    out = {"house": house, "H0": H0, "house_excess": house - H0}
    seat_sh = [x / house for x in alloc]
    vote_sh = [v / total for v in votes]
    vq = sum(votes[i] for i in qual)
    out["gallagher_all"] = _gallagher(seat_sh, vote_sh)
    out["gallagher_qual"] = _gallagher([seat_sh[i] for i in qual], [votes[i] / vq for i in qual])
    out["lh_all"] = 50 * sum(abs(a - b) for a, b in zip(seat_sh, vote_sh))
    out["lh_qual"] = 50 * sum(abs(seat_sh[i] - votes[i] / vq) for i in qual)
    out["sli_all"] = sum((100 * a - 100 * b) ** 2 / (100 * b) for a, b in zip(seat_sh, vote_sh) if b > 0)

    seats_q = np.array([alloc[p] for p in qual], dtype=float)
    units = {p: k for k, p in enumerate(qual)}
    for variant in ("D_win", "D_any", "C_win", "C_any"):
        parts = _one_share_parts(st, units, variant)
        out[f"os_{variant}"] = one_share_gallagher(*parts, seats_q)[0]
    out["bloc_deficit_os"] = one_share_bloc(st, alloc, house)

    # blocs
    N = st["N"]
    both = {b: 0.0 for b in "LR"}
    for q in range(P):
        if q not in qs:
            both[ally[q]] += sum(N[q][c] for c in range(P + 1) if c not in qs)
    bv_all = {b: sum(votes[i] for i in range(P) if ally[i] == b) for b in "LR"}
    bv_qual = {b: sum(votes[i] for i in qual if ally[i] == b) for b in "LR"}
    bv_cnt = {b: bv_all[b] - both[b] for b in "LR"}
    bseats = {b: sum(alloc[i] for i in qual if ally[i] == b) for b in "LR"}

    def bloc_def(bv):
        t = sum(bv.values())
        return max(max(0.0, house * bv[b] / t - bseats[b]) for b in "LR")

    out["bloc_deficit_all"] = bloc_def(bv_all)
    out["bloc_deficit_qual"] = bloc_def(bv_qual)
    out["bloc_deficit_countable"] = bloc_def(bv_cnt)
    out["bloc_gap_L"] = bseats["L"] - house * bv_all["L"] / sum(bv_all.values())
    out["left_vote_all"] = 100 * bv_all["L"] / sum(bv_all.values())
    maj = next((b for b in "LR" if 2 * bseats[b] > house), "none")
    out["majority"] = maj

    def inv(bv):
        more = "L" if bv["L"] > bv["R"] else "R"
        return int(maj not in ("none", more))

    out["inversion_all"] = inv(bv_all)
    out["inversion_qual"] = inv(bv_qual)
    nc = [i for i in range(P) if st["kind"][i] != "centre"]
    bv_nc = {b: sum(votes[i] for i in nc if ally[i] == b) for b in "LR"}
    bs_nc = {b: sum(alloc[i] for i in nc if i in qs and ally[i] == b) for b in "LR"}
    more = "L" if bv_nc["L"] > bv_nc["R"] else "R"
    out["inversion_nocentre"] = int(any(2 * bs_nc[b] > house and b != more for b in "LR"))

    # overhang and cost
    raw = m.sainte_lague(votes, qual, H0)
    out["overhang"] = 0 if system.startswith("PR") else sum(max(0, st["elec"][p] - raw[p]) for p in qual)
    W = st["W"]
    lam = {int(k): v for k, v in (info or {}).get("lam", {}).items()}
    mode = (info or {}).get("mode")
    overridden = touched = rescued = 0.0
    moved_from = {q: 0.0 for q in qual}
    for Pp, l in lam.items():
        f = max(0.0, l - 1.0)
        wasted = sum(W[q][Pp] for q in range(P) if q not in qs)
        if mode == "T":
            used = wasted * min(l, 1.0)
            rescued += used
            touched += used
        if f > 0:
            for q in qual:
                if q != Pp and W[q][Pp]:
                    moved_from[q] += f * W[q][Pp]
                    touched += W[q][Pp]
    overridden = sum(moved_from.values())
    if mode == "BV":
        r = sum(N[q][c] for q in range(P) if q not in qs for c in qual)
        rescued += r
        touched += r
    out["overridden_pct"] = 100 * overridden / total
    out["rescued_pct"] = 100 * rescued / total
    out["touched_pct"] = 100 * touched / total
    out["max_party_overridden_pct"] = max([100 * moved_from[q] / votes[q] for q in qual if votes[q]] or [0.0])
    loss = [raw[p] - alloc[p] for p in qual]
    out["seats_lost_max"] = max([0] + loss)
    out["parties_lost_2plus"] = sum(1 for x in loss if x >= 2)
    out["absorbed"] = int(bool((info or {}).get("absorbed_parties")))
    out["unseated"] = (info or {}).get("unseated", 0)
    out["wasted_pct"] = 100 * sum(votes[i] for i in range(P) if i not in qs) / total
    out["both_wasted_pct"] = 100 * sum(both.values()) / total
    return out


# ======================= recompute =======================

ROUND = 4


def _row(rec, system, H0, alloc, info, extra=None, state=None):
    out = {"exp": rec["exp"], **rec["key"], "system": system}
    out.update(compute(state or rec["state"], alloc, info, H0, system))
    if extra is not None:
        for k, x in zip("abcd", extra):
            out[f"extra_{k}"] = "" if x is None else x
    return {k: (round(v, ROUND) if isinstance(v, float) else v) for k, v in out.items()}


def comparators_for(rec):
    """Which comparator rules to apply to a record, at which sizes."""
    systems = rec["systems"]
    if rec["exp"].startswith("exp3"):
        own = next(iter(systems))
        if own == "MMP":
            return [("C", 121)]
        if own == "MMP141":  # the size-increase pathway: its ballots carry the 141-seat cap
            return [("R", 141), ("PR", 141)]
        return [("PR", 141 if own.endswith("141") else 121)]
    H = min(v["H0"] for v in systems.values())
    return [("C", H), ("R", H + 20)]


def rows_for(rec):
    st = rec["state"]
    P = len(st["names"])
    rows = []
    for name, x in rec["systems"].items():
        rows.append(_row(rec, name, x["H0"], x["alloc"], x.get("info"), x.get("extra")))
    s = None
    for kind, H in comparators_for(rec):
        if kind == "R":  # the Review's cap applied at the enlarged size (a hard limit of 141)
            s = s or scenario(st)
            a, info = rule_review(s, st, H)
            rows.append(_row(rec, f"CMP-Review{H}", H, alloc_list(a, P), info))
            continue
        if kind == "C":
            s = s or scenario(st)
            for name, fn in COMPARATORS.items():
                a, info = fn(s, st, H)
                rows.append(_row(rec, name, H, alloc_list(a, P), info))
        for thr, name in ((0.05, "PR5"), (0.035, "PR3.5")):
            a, info = rule_pr(st, H, thr)
            # judged against its own qualifying parties (no electorate waiver)
            rows.append(_row(rec, name + ("-141" if H == 141 else ""), H, alloc_list(a, P), {},
                             state=dict(st, qual=info["qual"])))
    return rows


def read_records(path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


class RecordWriter:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.f = gzip.open(path, "wt", encoding="utf-8", compresslevel=6)

    def write(self, rec):
        self.f.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")

    def close(self):
        self.f.close()


def recompute(run_dir, processes=None):
    from multiprocessing import Pool
    run_dir = Path(run_dir)
    recs = read_records(run_dir / "records.jsonl.gz")
    out = run_dir / "measures.csv"
    fields = None
    n = 0
    with Pool(processes) as pool, open(out, "w", newline="", encoding="utf-8") as fh:
        for rows in pool.imap(rows_for, recs, chunksize=16):
            if fields is None:
                fields = list(rows[0])
                for r in rows[1:]:
                    fields += [k for k in r if k not in fields]
                if "extra_a" not in fields:
                    fields += ["extra_a", "extra_b", "extra_c", "extra_d"]
                w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
                w.writeheader()
            w.writerows(rows)
            n += 1
    print(f"{run_dir}: {n} records → {out.name}")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "recompute":
        for d in sys.argv[2:]:
            recompute(d)
    else:
        print(__doc__)
