"""Experiment 3 at scale: 1,000 random walks from 2026 to 2041.

Each walk is a world started from the fixed 2026 official result and run
through five elections (2029–2041) under all ten pathways, with the same
random events (swings, drift, new parties) in every pathway of a walk.

Voters respond between elections by the reasoning rules written out for the
10 hand-reasoned runs (mc_future.respond, futures_reason.py,
futures/reasoning_<year>.md). Here each walk draws its own strength for every
rule, so the walks span a range of reasoning trajectories: faster or slower
learning, weaker or stronger party campaigns, more or less consolidation.
The hand-reasoned value is always inside the range drawn.

| Rule (where)                                   | Hand value | Drawn from   |
|------------------------------------------------|------------|--------------|
| Awareness before first reformed election       | 0.20       | U(0.10, 0.30)|
| Awareness gain after a visible / quiet election| 0.30 / 0.15| U(.15,.45) / U(.05,.25) |
| Two-tick cut, party that lost seats / others   | 0.45 / 0.15| U(.25,.65) / U(.05,.25) |
| MMP: partners' extra splitting per overhang    | 0.03       | U(0.01, 0.05)|
| MMP: decoy party-voting step                   | 0.01       | U(0.00, 0.02)|
| MMP: Māori-seat strategy growth                | 0.02       | U(0.00, 0.04)|
| MMP: Green "tick Labour" push (2032/35/38)     | 1.4/1.3/1.2| ±0.25 each   |
| MMP: National decoy shift to partner (pts)     | 1.0        | U(0.5, 1.5)  |
| Reform: ACT/NZF two-tick campaign (big/small loss) | 0.55 / 0.70 | U(.40,.75) / U(.55,.85) |
| Reform: Green/TOP two-tick campaign            | 0.75       | U(0.60, 0.90)|
| Reform: repeat two-tick campaign (2035)        | 0.70       | U(0.55, 0.85)|
| Reform: TPM recovery share of gap (2032–35 / 38–41) | 0.5 / 0.4 | U(.25,.75) / U(.2,.6) |
| Reform: TPM party-vote targets (2032 / later)  | 3.0 / 4.0% | U(2.5,3.5) / U(3,5) |
| Reform: Māori-seat splitting after 2029        | 0.32       | U(0.26, 0.38)|
| Reform: TPM general recovery rate / s_M decay  | 0.5 / 0.25 | U(.25,.75) / U(.1,.4) |
| -X: Green two-tick push in Māori seats         | 0.10       | U(0.05, 0.20)|
| Reform: left personal-split cut (2035 / 38–41) | 0.85 / 0.90| U(.75,.95) / U(.8,.97) |
| Reform: consolidation behind own leader        | ×2 +0.05, cap 0.35 | ×U(1.3,2.7) +U(0,.1), cap U(.2,.5) |
| Threshold fear (squeeze of parties under 5%)   | 0.15       | U(0.08, 0.22)|
| Backup vote: expressive shift / sub-threshold split | 0.012 / 0.2 | U(.005,.02) / U(.1,.3) |

Scenarios (mc_future.copycat): under MMP-family systems a bloc may adopt the
split-list playbook (leader's supporters tick its candidates but party-vote a
partner). --copycat: adopted only in reaction to the other side; --escalation:
stronger reactions plus adoption because it pays. Ranges in COPY_RANGES /
ESC_RANGES. No reform pathway adopts it (it gains nothing under a transfer).

Run:  python3 mc_future_walks.py N                 (baseline → futures_walks/)
      add --store to write everything, with raw ballot states, to runs/exp3_<scenario>/
      (then python3 measures.py recompute runs/exp3_<scenario>)
      python3 mc_future_walks.py N --copycat       (→ futures_walks_copycat/)
      python3 mc_future_walks.py N --escalation    (→ futures_walks_escalation/)
"""
import copy
import csv
import random
import statistics as st
import sys
from multiprocessing import Pool
from pathlib import Path

import mc_future as f
import futures_reason as fr

OUT = Path(__file__).parent / "futures_walks"
RANGES = {
    "aware_start": (0.10, 0.30), "aware_visible": (0.15, 0.45), "aware_quiet": (0.05, 0.25),
    "cut_loser": (0.25, 0.65), "cut_other": (0.05, 0.25),
    "mmp_escalate": (0.01, 0.05), "decoy_step": (0.0, 0.02), "mmp_sM_step": (0.0, 0.04),
    "green_push": (1.15, 1.65), "green_push2": (1.05, 1.55), "green_push3": (0.95, 1.45),
    "decoy_shift": (0.5, 1.5),
    "two_tick_big": (0.40, 0.75), "two_tick_small": (0.55, 0.85), "two_tick_left": (0.60, 0.90),
    "two_tick_again": (0.55, 0.85),
    "tpm_recover": (0.25, 0.75), "tpm_recover2": (0.20, 0.60),
    "tpm_target1": (2.5, 3.5), "tpm_target2": (3.0, 5.0), "sM_after": (0.26, 0.38),
    "tpm_rate": (0.25, 0.75), "sM_decay": (0.10, 0.40), "x_sM_decay": (0.05, 0.20),
    "pi_cut": (0.75, 0.95), "pi_cut2": (0.80, 0.97),
    "consol_mult": (1.3, 2.7), "consol_add": (0.0, 0.10), "consol_cap": (0.20, 0.50),
    "fear": (0.08, 0.22), "bv_expressive": (0.005, 0.02), "bv_sub_split": (0.10, 0.30),
}
# copycat scenario only (see mc_future.copycat)
COPY_RANGES = {"copy_base": (0.10, 0.40), "copy_follow": (0.20, 0.50),
               "dl_step": (0.05, 0.15), "dl_cap": (0.30, 0.70)}
# escalation scenario: the playbook is adopted because it pays, not only in
# reaction to the other side, and pushed harder
ESC_RANGES = {"copy_base": (0.20, 0.50), "copy_follow": (0.30, 0.60), "copy_hazard": (0.10, 0.30),
              "dl_step": (0.10, 0.25), "dl_cap": (0.50, 0.90)}
COPYCAT = False
ESCALATION = False
STORE = False  # --store: also write raw ballot states (runs/exp3_<scenario>/records.jsonl.gz)
EXP = "exp3_baseline"
_STANDOUTS = None


def apply_overrides(w, o):
    """As in mc_future.cmd_round."""
    for k, v in o.items():
        if k == "s":
            w["beh"]["s"].update(v)
        elif k == "s_scale":
            for p, x in v.items():
                if p in w["beh"]["s"]:
                    w["beh"]["s"][p] = min(0.9, max(0.02, w["beh"]["s"][p] * x))
        elif k == "shift":
            for src, dst, pts in v:
                src = [p for p in src if p in w["shares"]]
                if dst not in w["shares"] or not src:
                    continue
                pool = sum(w["shares"][p] for p in src)
                amt = min(pts / 100, 0.5 * pool)
                for p in src:
                    w["shares"][p] -= amt * w["shares"][p] / pool
                w["shares"][dst] += amt
        else:
            w["beh"][k] = v


def flags(w):
    """Situations the hand reasoning never saw (worth reviewing)."""
    lead = f.leaders(w)
    sh = w["shares"]
    out = []
    if lead["L"] != "Labour":
        out.append(f"left leader {lead['L']}")
    if lead["R"] != "National":
        out.append(f"right leader {lead['R']}")
    if sh.get("Te Pāti Māori", 0) >= 0.05:
        out.append("TPM over 5%")
    return out


def run_walk(r):
    global _STANDOUTS
    if _STANDOUTS is None:
        _STANDOUTS = f.fit_2026()[1]
    rng = random.Random(777_000 + r)
    temper = {k: rng.uniform(*v) for k, v in RANGES.items()}
    if COPYCAT:
        crng = random.Random(888_000 + r)
        temper.update({k: crng.uniform(*v) for k, v in (ESC_RANGES if ESCALATION else COPY_RANGES).items()})
    base = f.new_world(200_000 + r)
    base["beh"]["s"] = {p: (f.FIT_2026["s_L"] if x["ally"] == "L" else f.FIT_2026["s_R"])
                        for p, x in base["parties"].items() if x["role"] in ("bloc", "centre")}
    base["beh"]["s_M"] = f.FIT_2026["s_M"]
    base["beh"]["standouts"] = _STANDOUTS
    base["beh"]["temper"] = temper
    base["beh"]["copycat"] = COPYCAT
    base["history"].append(f.simulate(base, "MMP"))
    rows, records = [], []
    for system in f.PATHWAYS:
        w = copy.deepcopy(base)
        key = f"{r}|{system}"
        for year in f.YEARS:
            last = w["history"][-1]
            f.respond(w, last, system)
            f.exogenous(w, random.Random(w["seed"] * 100 + year))
            f.copycat(w, last, system, random.Random(w["seed"] * 7 + year))
            if year in fr.REASONERS:
                apply_overrides(w, fr.REASONERS[year](key, w, last))
            w["year"] = year
            res = f.simulate(w, system, keep_state=STORE)
            raw = {k: res.pop(k) for k in ("_state", "_alloc", "_info") if k in res}
            w["history"] = w["history"][-1:] + [res]
            bv = res["bloc_vote_pct"]
            more = "L" if bv["L"] > bv["R"] else "R"
            rows.append({
                "walk": r, "system": system, "year": year,
                "overhang": sum(res["overhang_raw"].values()),
                "overhang_tpm": res["overhang_raw"].get("Te Pāti Māori", 0),
                "overhang_nat": res["overhang_raw"].get("National", 0),
                "house": res["house"], "bloc_deficit": res["bloc_deficit"],
                "party_deficit_rounded": res["party_deficit_rounded"], "gallagher": res["gallagher"],
                "left_vote": bv["L"], "right_vote": bv["R"], "majority": res["majority"],
                "inversion": int(res["majority"] not in ("none", more)),
                "votes_moved": res["votes_moved"], "absorbed": int(bool(res["absorbed"])),
                "tpm_vote": res["shares"].get("Te Pāti Māori", 0), "wasted": res["wasted_pct"],
                "s_M": round(w["beh"]["s_M"], 3), "pi": round(w["beh"]["pi"], 3),
                "flags": "; ".join(flags(w)),
                "split_list_L": round(res["decoy_list"].get("L", -1), 3),
                "split_list_R": round(res["decoy_list"].get("R", -1), 3),
            })
            if STORE:
                meta = {k: v for k, v in rows[-1].items() if k not in ("walk", "system", "year")}
                meta["shares"] = res["shares"]
                meta["leaders"] = f.leaders(w)
                if year == f.YEARS[0]:
                    meta["temper"] = {k: round(v, 4) for k, v in temper.items()}
                records.append({"exp": EXP, "key": {"walk": r, "year": year}, "meta": meta, "state": raw["_state"],
                                "systems": {system: {"H0": f.size_of(system), "alloc": raw["_alloc"],
                                                     "info": raw["_info"]}}})
    return (rows, records) if STORE else rows


def summarise(rows):
    q = lambda xs, p: sorted(xs)[min(len(xs) - 1, int(p * len(xs)))]
    walks = len({r["walk"] for r in rows})
    L = [f"# Experiment 3 at scale{' — escalation scenario' if ESCALATION else ' — copycat scenario' if COPYCAT else ''}: {walks} walks × 5 elections (2029–2041)\n",
         "Each walk starts from the fixed 2026 result; voters respond by the written reasoning rules, "
         "with each rule's strength drawn per walk (see mc_future_walks.py).\n",
         "## All elections 2029–2041\n",
         "| System | Overhang: median / 90th / max | House: median / 90th / 99th / max | Bloc deficit: median / 90th / 99th "
         "| Blocs within 1 seat | Gallagher | Minority bloc won | Votes moved: median | Leftover absorbed |",
         "|---|---|---|---|---|---|---|---|---|"]
    for sysname in f.PATHWAYS:
        g = [r for r in rows if r["system"] == sysname]
        ov, hs, bd = [r["overhang"] for r in g], [r["house"] for r in g], [r["bloc_deficit"] for r in g]
        L.append(f"| {sysname} | {st.median(ov):.0f} / {q(ov,.9)} / {max(ov)} | "
                 f"{st.median(hs):.0f} / {q(hs,.9)} / {q(hs,.99)} / {max(hs)} | "
                 f"{st.median(bd):.1f} / {q(bd,.9):.1f} / {q(bd,.99):.1f} | "
                 f"{100*sum(x <= 1 for x in bd)/len(bd):.0f}% | {st.median(r['gallagher'] for r in g):.1f} | "
                 f"{100*sum(r['inversion'] for r in g)/len(g):.1f}% | {st.median(r['votes_moved'] for r in g)/1000:.0f}k | "
                 f"{100*sum(r['absorbed'] for r in g)/len(g):.0f}% |")
    L += ["\n## By election year: median bloc deficit (minority-bloc wins in brackets)\n",
          "| Year | " + " | ".join(f.PATHWAYS) + " |", "|---|" + "---|" * len(f.PATHWAYS)]
    for y in f.YEARS:
        cells = []
        for sysname in f.PATHWAYS:
            g = [r for r in rows if r["system"] == sysname and r["year"] == y]
            cells.append(f"{st.median(r['bloc_deficit'] for r in g):.1f} ({100*sum(r['inversion'] for r in g)/len(g):.0f}%)")
        L.append(f"| {y} | " + " | ".join(cells) + " |")
    L += ["\n## By election year: median overhang / median House\n",
          "| Year | " + " | ".join(f.PATHWAYS) + " |", "|---|" + "---|" * len(f.PATHWAYS)]
    for y in f.YEARS:
        cells = []
        for sysname in f.PATHWAYS:
            g = [r for r in rows if r["system"] == sysname and r["year"] == y]
            cells.append(f"{st.median(r['overhang'] for r in g):.0f} / {st.median(r['house'] for r in g):.0f}")
        L.append(f"| {y} | " + " | ".join(cells) + " |")
    L += ["\n## Te Pāti Māori in 2041: median party vote / Māori-seat splitting s_M\n",
          "| " + " | ".join(f.PATHWAYS) + " |", "|" + "---|" * len(f.PATHWAYS)]
    L.append("| " + " | ".join(
        f"{st.median(r['tpm_vote'] for r in rows if r['system'] == s_ and r['year'] == 2041):.1f}% / "
        f"{st.median(r['s_M'] for r in rows if r['system'] == s_ and r['year'] == 2041):.2f}" for s_ in f.PATHWAYS) + " |")
    fl = [r for r in rows if r["flags"]]
    L += ["\n## Situations the hand reasoning didn't cover\n",
          f"{len(fl)} of {len(rows)} world-elections ({100*len(fl)/len(rows):.1f}%) had at least one:"]
    kinds = {}
    for r in fl:
        for k in r["flags"].split("; "):
            kinds[k] = kinds.get(k, 0) + 1
    for k, n in sorted(kinds.items(), key=lambda x: -x[1]):
        L.append(f"- {k}: {n}")
    return "\n".join(L) + "\n"


def main(n):
    OUT.mkdir(parents=True, exist_ok=True)
    with Pool(initializer=_init, initargs=(COPYCAT, ESCALATION, STORE, EXP)) as pool:
        if STORE:  # raw results for measures.py, written as walks finish
            import measures as ms
            wr = ms.RecordWriter(OUT / "records.jsonl.gz")
            rows = []
            for k, (rs, recs) in enumerate(pool.imap_unordered(run_walk, range(n), chunksize=4)):
                rows += rs
                for rec in recs:
                    wr.write(rec)
                if (k + 1) % 100 == 0:
                    print(f"  {k + 1}/{n} walks", flush=True)
            wr.close()
        else:
            rows = [row for rs in pool.imap_unordered(run_walk, range(n), chunksize=4) for row in rs]
    rows.sort(key=lambda r: (r["walk"], r["system"], r["year"]))
    with open(OUT / "results.csv", "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0]))
        wr.writeheader(); wr.writerows(rows)
    (OUT / "summary.md").write_text(summarise(rows))
    print(f"wrote {n} walks to {OUT.name}/results.csv and summary.md")


def _init(copycat, escalation, store=False, exp="exp3_baseline"):
    global COPYCAT, ESCALATION, STORE, EXP
    COPYCAT, ESCALATION, STORE, EXP = copycat, escalation, store, exp


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--copycat" in sys.argv:
        COPYCAT = True
        OUT = Path(__file__).parent / "futures_walks_copycat"
    if "--escalation" in sys.argv:
        COPYCAT = ESCALATION = True
        OUT = Path(__file__).parent / "futures_walks_escalation"
    if "--store" in sys.argv:
        STORE = True
        EXP = "exp3_" + ("escalation" if ESCALATION else "copycat" if COPYCAT else "baseline")
        OUT = Path(__file__).parent / "runs" / EXP
    main(int(args[0]) if args else 1000)
