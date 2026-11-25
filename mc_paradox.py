"""Monotonicity ("negative vote weight") tests for every seat rule.

Takes simulated elections from Experiment 1 (mc_overhang, wide stress test)
and Experiment 2 (mc_calibrated, NZ-like), perturbs the ballots a little, and
reallocates seats under every system on the perturbed ballots. A paradox is
a perturbation that should help a party (or bloc) but costs it seats.

Perturbations (k ballots in one electorate; k log-uniform 30–30,000):

  A  add      k new ballots (party vote q, electorate vote c)
  B  cand     k existing ballots (q, c') switch their electorate vote to c
  C  party    k existing ballots (q', c) switch their party vote to q

Paradox checks (seat COUNTS; shares are reported separately because the
House size varies under MMP and the -X variants):

  party      A, C: q gains party votes but loses seats
  cand       B: c gains electorate votes (party votes unchanged) but loses seats
  own_cand   B with c == q: a q voter switching to q's own candidate costs q
  split_cost B with c != q: q loses seats when its voter splits (the intended
             effect of a transfer; recorded, not counted as a paradox)
  bloc       A with q, c in the same bloc, or C with q' in the other bloc:
             the bloc gains votes but loses seats

Each perturbation is classified by what the electorate vote c was:
  straight (c == q), overhanger (c won this electorate and its party
  overhangs on raw votes), winner (c won, no overhang), loser.

Run:  python3 mc_paradox.py run N      (N scenarios per experiment)
      python3 mc_paradox.py summary    (paradox_results.csv → paradox_summary.md)
"""
import copy
import csv
import math
import random
import sys
from collections import defaultdict

import mc_overhang as m
import mc_calibrated as mc

SYSTEMS = ["MMP", "MMP-T", "MMP-T-X", "MMP-BV", "MMP-BV-X",
           "MMP141", "MMP-T-X141", "MMP-BV-X141"]
SYSTEMS_BASE = list(SYSTEMS)
PERTS_PER_SCENARIO = 80


def derive(parties, electorates):
    """Rebuild the scenario dict from ballots (same logic as gen_scenario)."""
    P = len(parties)
    minors = {i for i, x in enumerate(parties) if getattr(x, "minor", False)}
    for el in electorates:
        M = el["M"]
        cv = [sum(M[q][c] for q in range(P)) for c in range(P)]
        el["cv"] = cv
        el["winner"] = max(el["cands"], key=lambda c: cv[c])
    votes = [sum(el["pv"][i] for el in electorates) for i in range(P)]
    elec = [0] * P
    for el in electorates:
        elec[el["winner"]] += 1
    total = sum(votes)
    qual = [i for i in range(P) if i not in minors and (votes[i] / total >= m.THRESHOLD or elec[i] > 0)]
    qs = set(qual)
    vs = [votes[i] if i in qs else 0.0 for i in range(P)]
    for el in electorates:
        for q in range(P):
            if q not in qs:
                for c in qs:
                    vs[c] += el["M"][q][c]
    pools = {}
    for Pp in qual:
        if not elec[Pp]:
            continue
        split = {q: 0.0 for q in qual if q != Pp}
        wasted = 0.0
        for el in electorates:
            if el["winner"] == Pp:
                for q in split:
                    split[q] += el["M"][q][Pp]
                wasted += sum(el["M"][q][Pp] for q in range(P) if q not in qs)
        pools[Pp] = (wasted, split)
    bloc_votes = {b: sum(votes[i] for i in range(P) if parties[i].ally == b) for b in "LR"}
    return {"parties": parties, "votes": votes, "o2_votes": vs, "elec": elec, "qual": qual,
            "pools": pools, "total": total, "bloc_votes": bloc_votes,
            "bloc_votes_countable": bloc_votes, "electorates": electorates}


# ---- variant rule: re-check for overhang after other parties' transfers ----
# mc_overhang.proposed_system decides which parties overhang once, on the
# untransferred votes. A party pushed into overhang by another party's
# transfer is then absorbed without a transfer of its own. This variant adds
# such parties to the transfer and re-solves until the set is stable.

def proposed_system_recheck(s, H, mode, grow=False):
    elec, qual, pools = s["elec"], s["qual"], s["pools"]
    v0 = s["votes"] if mode == "T" else s["o2_votes"]
    use_wasted = mode == "T"
    base = m.sainte_lague(v0, qual, H)
    over = [i for i in qual if elec[i] > base[i]]
    if not over:
        return base, {"moved": 0.0, "absorbed_parties": []}
    lam = {}

    def adjusted(lam):
        v = list(v0)
        for P, l in lam.items():
            wasted, split = pools[P]
            if use_wasted:
                v[P] += wasted * min(l, 1.0)
            f = max(0.0, l - 1.0)
            for q, n in split.items():
                v[P] += f * n; v[q] -= f * n
        return v

    def final(lam):
        return m.absorb(adjusted(lam), elec, qual, H)

    for _ in range(len(qual)):
        for P in over:
            lam.setdefault(P, 0.0)
        for _ in range(20):
            prev = dict(lam)
            for P in over:
                lam[P] = 2.0
                a, fixed = final(lam)
                if P in fixed:
                    continue
                lo, hi = (0.0 if use_wasted else 1.0), 2.0
                for _ in range(40):
                    lam[P] = (lo + hi) / 2
                    lo, hi = (lo, lam[P]) if P not in final(lam)[1] else (lam[P], hi)
                lam[P] = hi
            if all(abs(lam[P] - prev[P]) < 1e-6 for P in over):
                break
        a, fixed = final(lam)
        new = [P for P in fixed if P not in over and P in pools]
        if not new:
            break
        over = over + new
    a, fixed = final(lam)
    v = adjusted(lam)
    moved = sum(max(0.0, v[P] - v0[P]) for P in over)
    if grow and fixed:
        b = m.sainte_lague(v, qual, H)
        return ({i: max(b[i], elec[i]) for i in qual},
                {"moved": moved, "absorbed_parties": [], "grown_by": sorted(fixed)})
    return a, {"moved": moved, "absorbed_parties": sorted(fixed)}


RECHECK = {
    "MMP-T*": (lambda s, H: proposed_system_recheck(s, H, "T"), 121, False),
    "MMP-T-X*": (lambda s, H: proposed_system_recheck(s, H, "T", grow=True), 121, False),
    "MMP-BV*": (lambda s, H: proposed_system_recheck(s, H, "BV"), 121, False),
    "MMP-BV-X*": (lambda s, H: proposed_system_recheck(s, H, "BV", grow=True), 121, False),
    "MMP-T-X141*": (lambda s, H: proposed_system_recheck(s, H, "T", grow=True), 141, False),
    "MMP-BV-X141*": (lambda s, H: proposed_system_recheck(s, H, "BV", grow=True), 141, False),
}


def allocate(s, system):
    rule, H, _ = (RECHECK if system.endswith("*") else m.SYSTEMS)[system]
    alloc, info = rule(s, H)
    return alloc, info


def outcome(s):
    out = {}
    for sysname in SYSTEMS:
        alloc, info = allocate(s, sysname)
        out[sysname] = (alloc, info)
    return out


def seats(alloc, i):
    return alloc.get(i, 0)


def bloc_seats(alloc, parties, b):
    return sum(n for i, n in alloc.items() if parties[i].ally == b)


def prepare(s):
    """Attach candidate lists to each electorate (anyone with electorate votes)."""
    P = len(s["parties"])
    minors = {i for i, x in enumerate(s["parties"]) if getattr(x, "minor", False)}
    for el in s["electorates"]:
        cv = [sum(el["M"][q][c] for q in range(P)) for c in range(P)]
        el["cands"] = [c for c in range(P) if c not in minors and cv[c] > 0]
    return s


def raw_overhangers(s):
    base = m.sainte_lague(s["votes"], s["qual"], m.SEATS)
    return {i for i in s["qual"] if s["elec"][i] > base[i]}


def classify(s, over, e, q, c):
    el = s["electorates"][e]
    if c == q:
        return "straight"
    if c == el["winner"]:
        return "overhanger" if c in over else "winner"
    return "loser"


def run_scenario(args):
    exp, k_seed = args
    gen = m.gen_scenario if exp == "exp1" else mc.gen_scenario
    seed = (10_000 if exp == "exp1" else 50_000) + k_seed
    s0 = prepare(gen(random.Random(seed)))
    parties = s0["parties"]
    P = len(parties)
    minors = {i for i, x in enumerate(parties) if getattr(x, "minor", False)}
    base = outcome(derive(parties, s0["electorates"]))
    over = raw_overhangers(s0)
    rng = random.Random(seed * 7 + 1)
    E = len(s0["electorates"])
    over_els = [e for e in range(E) if s0["electorates"][e]["winner"] in over]
    rows = []
    for t in range(PERTS_PER_SCENARIO):
        kind = rng.choices("ABC", weights=[0.4, 0.3, 0.3])[0]
        e = rng.choice(over_els) if over_els and rng.random() < 0.6 else rng.randrange(E)
        el0 = s0["electorates"][e]
        cands = el0["cands"]
        k = math.exp(rng.uniform(math.log(30), math.log(30_000)))
        els = copy.deepcopy(s0["electorates"])
        el = els[e]
        # party-vote choices: any party with votes here (incl. minors)
        pvs = [i for i in range(P) if el["pv"][i] > 0]
        if kind == "A":
            q = rng.choice(pvs)
            c = rng.choice(cands + [q] * 2 if q in cands else cands)
            el["pv"][q] += k
            el["M"][q][c] += k
            src = None
        elif kind == "B":
            # existing ballots (q, c') -> (q, c)
            pairs = [(q, cp) for q in pvs for cp in cands if el["M"][q][cp] > 1]
            q, cp = rng.choice(pairs)
            c = rng.choice([x for x in cands if x != cp] or [cp])
            if c == cp:
                continue
            k = min(k, el["M"][q][cp])
            el["M"][q][cp] -= k
            el["M"][q][c] += k
            src = cp
        else:
            # existing ballots (q', c) -> (q, c)
            pairs = [(qp, c) for qp in pvs for c in cands if el["M"][qp][c] > 1]
            qp, c = rng.choice(pairs)
            q = rng.choice([x for x in pvs if x != qp] or [qp])
            if q == qp:
                continue
            k = min(k, el["M"][qp][c])
            el["M"][qp][c] -= k
            el["M"][q][c] += k
            el["pv"][qp] -= k
            el["pv"][q] += k
            src = qp
        s1 = derive(parties, els)
        after = outcome(s1)
        cls = classify(s0, over, e, q, c)
        winner_changed = s1["electorates"][e]["winner"] != el0["winner"]
        qual_changed = set(s1["qual"]) != set(s0["qual"])
        for sysname in SYSTEMS:
            a0, i0 = base[sysname]
            a1, i1 = after[sysname]
            h0, h1 = sum(a0.values()), sum(a1.values())
            flags = []
            if kind in "AC" and q not in minors:
                if seats(a1, q) < seats(a0, q):
                    flags.append("party")
            # electorate-vote monotonicity: party votes held fixed (B only;
            # under A the added party vote can legitimately cost c a seat)
            if kind == "B" and seats(a1, c) < seats(a0, c):
                flags.append("own_cand" if c == q else "cand")
            # informational, not a paradox: a q voter splitting away costs q
            if kind == "B" and c != q and q not in minors and seats(a1, q) < seats(a0, q):
                flags.append("split_cost")
            b = parties[q].ally
            bloc_gain = (kind == "A" and parties[c].ally == b) or (kind == "C" and parties[src].ally != b)
            if bloc_gain and bloc_seats(a1, parties, b) < bloc_seats(a0, parties, b):
                flags.append("bloc")
            share_drop = (kind in "AC" and q not in minors and h0 and h1
                          and seats(a1, q) / h1 < seats(a0, q) / h0 - 1e-12)
            rows.append({
                "exp": exp, "scenario": k_seed, "pert": t, "kind": kind, "class": cls,
                "q": parties[q].name, "c": parties[c].name,
                "src": parties[src].name if src is not None else "",
                "k": round(k), "electorate": e, "system": sysname,
                "flags": "|".join(flags), "share_drop": int(bool(share_drop)),
                "q_seats": f"{seats(a0, q)}>{seats(a1, q)}", "c_seats": f"{seats(a0, c)}>{seats(a1, c)}",
                "house": f"{h0}>{h1}", "winner_changed": int(winner_changed), "qual_changed": int(qual_changed),
                "winner_before": parties[el0["winner"]].name,
                "winner_after": parties[s1["electorates"][e]["winner"]].name,
                "absorbed_before": "|".join(parties[i].name for i in i0.get("absorbed_parties", [])),
                "absorbed_after": "|".join(parties[i].name for i in i1.get("absorbed_parties", [])),
                "grown_after": "|".join(parties[i].name for i in i1.get("grown_by", [])),
                "moved_before": round(i0.get("moved", 0)), "moved_after": round(i1.get("moved", 0)),
                "overhang": int(bool(over)),
            })
    return rows


def cmd_recheck():
    """Rerun every scenario with a clean reform paradox under the re-check variant."""
    global SYSTEMS
    from multiprocessing import Pool
    rows = list(csv.DictReader(open("paradox_results.csv", encoding="utf-8")))
    jobs = sorted({(r["exp"], int(r["scenario"])) for r in rows
                   if r["flags"] and r["system"] not in ("MMP", "MMP141")
                   and r["winner_changed"] == "0" and r["qual_changed"] == "0"})
    print(len(jobs), "scenarios")
    with Pool() as pool, open("paradox_recheck.csv", "w", newline="", encoding="utf-8") as f:
        w = None
        for out in pool.imap_unordered(run_scenario_recheck, jobs, chunksize=2):
            if w is None:
                w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
                w.writeheader()
            w.writerows(out)
    print("wrote paradox_recheck.csv")


def run_scenario_recheck(job):
    global SYSTEMS
    SYSTEMS = SYSTEMS_BASE + list(RECHECK)
    return run_scenario(job)


def cmd_run(n):
    from multiprocessing import Pool
    jobs = [(exp, k) for exp in ("exp1", "exp2") for k in range(n)]
    with Pool() as pool, open("paradox_results.csv", "w", newline="", encoding="utf-8") as f:
        w = None
        for rows in pool.imap_unordered(run_scenario, jobs, chunksize=4):
            if not rows:
                continue
            if w is None:
                w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                w.writeheader()
            w.writerows(rows)
    print("wrote paradox_results.csv")


# ======================= summary =======================

def cmd_summary(path="paradox_results.csv", out="paradox_summary.md"):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    tests = [("party", "AC"), ("bloc", "AC"), ("cand", "B"), ("own_cand", "B")]
    lines = ["# Paradox search: summary", "",
             f"{len(rows) // len(SYSTEMS):,} perturbations × {len(SYSTEMS)} systems "
             f"({len({(r['exp'], r['scenario']) for r in rows})} scenarios).", ""]

    def eligible(r, test, kinds):
        if r["kind"] not in kinds:
            return False
        if test == "party" and r["q"].endswith("minor"):
            return False
        if test == "bloc":
            # bloc inferred from names; centrists (random ally) are skipped
            def ally(n):
                return "L" if n.startswith(("Left", "Māori")) else "R" if n.startswith("Right") else None
            bq = ally(r["q"])
            if bq is None:
                return False
            if r["kind"] == "A":
                return ally(r["c"]) == bq
            return ally(r["src"]) not in (None, bq)
        if test == "own_cand":
            return r["c"] == r["q"]
        if test == "cand":
            return r["c"] != r["q"]
        return True

    for exp in ("exp1", "exp2", "all"):
        sub = [r for r in rows if exp == "all" or r["exp"] == exp]
        lines += [f"## {exp}: paradox rate per 10,000 eligible perturbations (clean = no electorate winner or qualification change)", "",
                  "| System | " + " | ".join(f"{t}: all / clean" for t, _ in tests) + " | split_cost (intended) |",
                  "|---|" + "---|" * (len(tests) + 1)]
        for sysn in SYSTEMS:
            ss = [r for r in sub if r["system"] == sysn]
            cells = []
            for t, kinds in tests:
                el = [r for r in ss if eligible(r, t, kinds)]
                hit = [r for r in el if t in r["flags"].split("|")]
                cl = [r for r in el if r["winner_changed"] == "0" and r["qual_changed"] == "0"]
                hitc = [r for r in cl if t in r["flags"].split("|")]
                cells.append(f"{1e4 * len(hit) / max(1, len(el)):.1f} / {1e4 * len(hitc) / max(1, len(cl)):.1f}")
            elB = [r for r in ss if r["kind"] == "B" and r["c"] != r["q"]]
            sc = sum("split_cost" in r["flags"] for r in elB)
            cells.append(f"{1e4 * sc / max(1, len(elB)):.0f}")
            lines.append(f"| {sysn} | " + " | ".join(cells) + " |")
        lines.append("")

    # clean party / bloc paradoxes by class of electorate vote
    lines += ["## Clean party- and bloc-vote paradoxes by kind of ballot (counts)", "",
              "| System | Test | straight | overhanger | winner | loser | of which fallback active after (absorbed/grown) |",
              "|---|---|---|---|---|---|---|"]
    for sysn in SYSTEMS:
        for t in ("party", "bloc"):
            hit = [r for r in rows if r["system"] == sysn and t in r["flags"].split("|")
                   and r["winner_changed"] == "0" and r["qual_changed"] == "0"]
            if not hit:
                continue
            cnt = defaultdict(int)
            for r in hit:
                cnt[r["class"]] += 1
            fb = sum(1 for r in hit if r["absorbed_after"] or r["grown_after"])
            lines.append(f"| {sysn} | {t} | {cnt['straight']} | {cnt['overhanger']} | {cnt['winner']} | {cnt['loser']} | {fb} |")
    lines.append("")
    open(out, "w", encoding="utf-8").write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    if sys.argv[1] == "summary":
        cmd_summary()
    elif sys.argv[1] == "recheck":
        cmd_recheck()
    elif sys.argv[1] == "run":
        cmd_run(int(sys.argv[2]))
    elif sys.argv[1] == "one":
        rows = run_scenario((sys.argv[2], int(sys.argv[3])))
        print(len(rows), sum(1 for r in rows if r["flags"]))
        for r in rows:
            if r["flags"]:
                print(r)
