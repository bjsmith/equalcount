"""Why does MMP-BV141 leave a bloc more than one seat short?

Re-generates each scenario (same seeds as mc_overhang.py) and records what
happened inside MMP-BV141, then classifies every scenario whose bloc seat
deficit is above 1 by its main cause:

  Wasted both ticks   the countable bloc deficit is ≤ 1: the whole gap is
                      voters whose party and electorate votes both went to
                      parties that don't qualify (no seat rule can count them).
  Overhang absorbed   still short on the countable yardstick, and a party's
                      overhang could not be covered by transfers, so the rest
                      was absorbed within 141 seats.
  Transfers           still short on the countable yardstick; an overhang was
                      fully covered by transferring split ballots.
  Backup votes cross  still short on the countable yardstick with no overhang:
                      e.g. sub-threshold voters whose electorate vote went to
                      the other bloc's candidate, or rounding.

Run:  python3 mc_diagnose_bv141.py [N]   (writes mc_diagnose_bv141.md)
"""
import random
import statistics as st
import sys
from multiprocessing import Pool

import mc_overhang as m

H = 141


def diag(k):
    s = m.gen_scenario(random.Random(1000 + k))
    p, parties, qual, elec = s["params"], s["parties"], s["qual"], s["elec"]
    alloc, info = m.proposed_system(s, H, "BV")
    me = m.measures(s, alloc)
    mc = m.measures(s, alloc, "bloc_votes_countable")
    base = m.sainte_lague(s["o2_votes"], qual, H)
    over = {i: elec[i] - base[i] for i in qual if elec[i] > base[i]}
    short = max("LR", key=lambda b: me["bloc_short"][b])
    # split ballots for overhanging parties' winners that came from the other bloc
    cross = sum(n for P in over for q, n in s["pools"][P][1].items() if parties[q].ally != parties[P].ally)
    tot = s["total"]
    left1 = next(i for i, x in enumerate(parties) if x.name == "Left 1")
    right1 = next(i for i, x in enumerate(parties) if x.name == "Right 1")
    lead = max(left1, right1, key=lambda i: s["votes"][i])
    return {
        "k": k, "bloc_def": me["bloc_deficit"], "bloc_def_countable": mc["bloc_deficit"], "short_bloc": short,
        "overhang141": sum(over.values()),
        "overhang_blocs": "".join(sorted({parties[i].ally for i in over})),
        "maori_overhang141": sum(n for i, n in over.items() if parties[i].bloc == "M"),
        "absorbed": len(info.get("absorbed_parties", [])),
        "absorbed_maori": sum(parties[i].bloc == "M" for i in info.get("absorbed_parties", [])),
        "short_is_overhang_bloc": short in {parties[i].ally for i in over},
        "cross_split_pct": 100 * cross / tot,
        "both_wasted_pct": 100 * s["both_wasted"] / tot,
        "s_L": p["s_L"], "s_R": p["s_R"], "s_M": p["s_M"], "personal": p["personal"],
        "minor": p["minor"], "left_frac": p["left_frac"],
        "n_maori": p["n_maori"], "n_left": p["n_left"], "n_right": p["n_right"], "n_centre": p["n_centre"],
        "leader_pct": 100 * s["votes"][lead] / tot,
        "leader_elec": elec[lead],
        "subthreshold_pct": 100 * sum(s["votes"][i] for i in range(len(parties)) if i not in qual) / tot,
        "n_qual": len(qual),
    }


def cause(r):
    if r["bloc_def_countable"] <= 1:
        return "Wasted both ticks"
    if r["absorbed"]:
        return "Overhang absorbed"
    if r["overhang141"]:
        return "Transfers"
    return "Backup votes cross"


def med(g, k, f="{:.1f}"):
    return f.format(st.median(r[k] for r in g)) if g else "–"


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    with Pool() as pool:
        rows = pool.map(diag, range(n), chunksize=16)
    bad = [r for r in rows if r["bloc_def"] > 1]
    ok = [r for r in rows if r["bloc_def"] <= 1]
    causes = ["Overhang absorbed", "Transfers", "Wasted both ticks", "Backup votes cross"]
    groups = {c: [r for r in bad if cause(r) == c] for c in causes}

    L = [f"# MMP-BV141: scenarios with a bloc seat deficit above 1\n",
         f"{len(bad)} of {n} scenarios ({100 * len(bad) / n:.0f}%). Causes are defined in "
         "`mc_diagnose_bv141.py`.\n",
         "## By main cause\n",
         "| Cause | Scenarios | Share of all | Bloc deficit: median / 90th | Countable bloc deficit: median |",
         "|---|---|---|---|---|"]
    for c, g in groups.items():
        if g:
            d = sorted(r["bloc_def"] for r in g)
            L.append(f"| {c} | {len(g)} | {100 * len(g) / n:.0f}% | {st.median(d):.1f} / "
                     f"{d[int(.9 * len(d))]:.1f} | {med(g, 'bloc_def_countable')} |")

    L += ["\n## Profile (medians unless noted)\n",
          "| | Deficit ≤ 1 | " + " | ".join(causes) + " |", "|---|---|" + "---|" * len(causes)]
    cols = [ok] + [groups[c] for c in causes]
    spec = [("Scenarios", lambda g: str(len(g))),
            ("Bloc strategic rate, higher of s_L / s_R", lambda g: med(g, "s_hi", "{:.0%}")),
            ("Māori strategic rate s_M", lambda g: med(g, "s_M", "{:.0%}")),
            ("Personal vote", lambda g: med(g, "personal", "{:.0%}")),
            ("Largest party's vote", lambda g: med(g, "leader_pct", "{:.0f}%")),
            ("Largest party's electorates (of 71)", lambda g: med(g, "leader_elec", "{:.0f}")),
            ("Qualifying parties", lambda g: med(g, "n_qual", "{:.0f}")),
            ("Vote for sub-threshold parties", lambda g: med(g, "subthreshold_pct", "{:.1f}%")),
            ("Voters wasting both ticks", lambda g: med(g, "both_wasted_pct", "{:.1f}%")),
            ("Overhang at 141 (after backup votes)", lambda g: med(g, "overhang141", "{:.0f}")),
            ("Has a Māori party (share)", lambda g: f"{100 * sum(r['n_maori'] > 0 for r in g) / len(g):.0f}%" if g else "–"),
            ("Māori-party overhang absorbed (share)", lambda g: f"{100 * sum(r['absorbed_maori'] > 0 for r in g) / len(g):.0f}%" if g else "–"),
            ("Short bloc is the overhanging bloc (share)", lambda g: f"{100 * sum(r['short_is_overhang_bloc'] for r in g) / len(g):.0f}%" if g else "–"),
            ("Cross-bloc split ballots for overhang winners", lambda g: med(g, "cross_split_pct", "{:.1f}%"))]
    for r in rows:
        r["s_hi"] = max(r["s_L"], r["s_R"])
    for lab, f in spec:
        L.append(f"| {lab} | " + " | ".join(f(g) for g in cols) + " |")

    # ---- head to head with the current system (needs mc_results.csv) ----
    import mc_analyse
    res = {int(r["scenario"]): r for r in mc_analyse.load()}
    for r in rows:
        c = res[r["k"]]
        r["mmp_def"], r["mmp141_def"] = c["MMP_bloc_deficit"], c["MMP141_bloc_deficit"]
        r["mmp141_house"], r["mmp_house"] = c["MMP141_house"], c["MMP_house"]
        r["overhang121"] = c["overhang_base"]
    w141 = [r for r in rows if r["bloc_def"] - r["mmp141_def"] >= 1]
    w121 = [r for r in rows if r["bloc_def"] - r["mmp_def"] >= 1]
    both = [r for r in w141 if r in w121]
    heads = [("All scenarios", rows), ("≥ 1 seat worse than MMP141", w141),
             ("≥ 1 seat worse than MMP", w121), ("Worse than both", both)]
    L += ["\n## Where MMP-BV141 is at least one seat worse than the current system\n",
          "Bloc seat deficit of MMP-BV141 minus that of MMP141 (same size) or MMP (121 seats), "
          "each against the bloc yardstick.\n",
          "| | " + " | ".join(h for h, _ in heads) + " |", "|---|" + "---|" * len(heads)]
    pc = lambda g, f: f"{100 * sum(1 for r in g if f(r)) / len(g):.0f}%" if g else "–"
    spec2 = [("Scenarios", lambda g: f"{len(g)} ({100 * len(g) / n:.0f}%)"),
             ("Bloc deficit: MMP-BV141", lambda g: med(g, "bloc_def")),
             ("Bloc deficit: MMP141", lambda g: med(g, "mmp141_def")),
             ("Bloc deficit: MMP", lambda g: med(g, "mmp_def")),
             ("House size: MMP141", lambda g: med(g, "mmp141_house", "{:.0f}")),
             ("Overhang at 121 (raw votes)", lambda g: med(g, "overhang121", "{:.0f}")),
             ("Overhang at 141 (after backup votes)", lambda g: med(g, "overhang141", "{:.0f}"))] + spec[1:-1]
    spec2 += [("Cause: wasted both ticks", lambda g: pc(g, lambda r: cause(r) == "Wasted both ticks")),
              ("Cause: overhang absorbed", lambda g: pc(g, lambda r: cause(r) == "Overhang absorbed")),
              ("Cause: transfers", lambda g: pc(g, lambda r: cause(r) == "Transfers")),
              ("Cause: backup votes cross", lambda g: pc(g, lambda r: cause(r) == "Backup votes cross"))]
    for lab, f in spec2:
        if lab.startswith("Overhang at 141") and lab in [x for x, _ in spec2[:7]] and f is not spec2[6][1]:
            continue
        L.append(f"| {lab} | " + " | ".join(f(g) for _, g in heads) + " |")

    with open("mc_diagnose_bv141.md", "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[L.index(next(x for x in L if x.startswith("\n## Where"))):]))


if __name__ == "__main__":
    main()
