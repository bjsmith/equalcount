"""Experiment 3 benchmark (run: python3 mc_future_floor.py 1000): on each simulated election's party votes, allocate seats by pure
PR (Sainte-Laguë on parties over the threshold, no electorates) at 121 seats.
This is the best any overhang fix could do on those ballots."""
import copy, random, statistics as st, sys
from multiprocessing import Pool
import mc_future as f, futures_reason as fr, mc_future_walks as mw, mc_overhang as m

PATHS = ["MMP", "MMP-T-X", "MMP-BV-X", "MMP-BV-X141"]

def pr(w, res, thr, H=121):
    sh = res["shares"]; P = w["parties"]
    q = [p for p, v in sh.items() if not P[p]["minor"] and v >= 100 * thr]
    a = m.sainte_lague(sh, q, H)
    bs = {b: sum(a[p] for p in q if P[p]["ally"] == b) for b in "LR"}
    bv = res["bloc_vote_pct"]
    defi = max(max(0, H * bv[b] / (bv["L"] + bv["R"]) - bs[b]) for b in "LR")
    maj = next((b for b in "LR" if 2 * bs[b] > H), "none")
    more = "L" if bv["L"] > bv["R"] else "R"
    vq = sum(sh[p] for p in q)
    g = (0.5 * sum((100 * a[p] / H - 100 * sh[p] / vq) ** 2 for p in q)) ** 0.5
    return defi, int(maj not in ("none", more)), g

def walk(r):
    mw._STANDOUTS = mw._STANDOUTS or f.fit_2026()[1]
    rng = random.Random(777_000 + r)
    temper = {k: rng.uniform(*v) for k, v in mw.RANGES.items()}
    base = f.new_world(200_000 + r)
    base["beh"]["s"] = {p: (f.FIT_2026["s_L"] if x["ally"] == "L" else f.FIT_2026["s_R"])
                        for p, x in base["parties"].items() if x["role"] in ("bloc", "centre")}
    base["beh"]["s_M"] = f.FIT_2026["s_M"]; base["beh"]["standouts"] = mw._STANDOUTS; base["beh"]["temper"] = temper
    base["history"].append(f.simulate(base, "MMP"))
    out = []
    for system in PATHS:
        w = copy.deepcopy(base); key = f"{r}|{system}"
        for year in f.YEARS:
            last = w["history"][-1]
            f.respond(w, last, system); f.exogenous(w, random.Random(w["seed"] * 100 + year))
            if year in fr.REASONERS: mw.apply_overrides(w, fr.REASONERS[year](key, w, last))
            w["year"] = year; res = f.simulate(w, system); w["history"] = [res]
            bv = res["bloc_vote_pct"]; more = "L" if bv["L"] > bv["R"] else "R"
            out.append((system, res["bloc_deficit"], int(res["majority"] not in ("none", more)), res["gallagher"],
                        *pr(w, res, 0.05), *pr(w, res, 0.035)))
    return out

if __name__ == "__main__":
    with Pool() as pool:
        rows = [x for rs in pool.imap_unordered(walk, range(int(sys.argv[1])), chunksize=4) for x in rs]
    print("| Ballots from | System as run: bloc def / minority / Gallagher | Pure PR, 5%: same | Pure PR, 3.5%: same |")
    for p in PATHS:
        g = [r for r in rows if r[0] == p]
        c = lambda i: st.median(x[i] for x in g)
        s = lambda i: 100 * sum(x[i] for x in g) / len(g)
        print(f"| {p} | {c(1):.1f} / {s(2):.1f}% / {c(3):.1f} | {c(4):.1f} / {s(5):.1f}% / {c(6):.1f} | {c(7):.1f} / {s(8):.1f}% / {c(9):.1f} |")
