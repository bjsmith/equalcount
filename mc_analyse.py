"""Summarise mc_results.csv (from `python3 mc_overhang.py run N`) into mc_summary.md.

Run:  python3 mc_analyse.py [results.csv] [summary.md]
      (defaults: mc_results.csv → mc_summary.md)
"""
import csv
import statistics as st
import sys

IN_CSV = sys.argv[1] if len(sys.argv) > 1 else "mc_results.csv"
OUT_MD = sys.argv[2] if len(sys.argv) > 2 else "mc_summary.md"

BIG = 10_000  # stands in for "not reached within the search limit"
SYSTEMS = ["MMP", "MMP-T", "MMP-BV", "MMP-T-X", "MMP-BV-X",
           "MMP141", "MMP-T141", "MMP-BV141", "MMP-T-X141", "MMP-BV-X141"]
SEARCHED = ["MMP", "MMP-T", "MMP-BV", "MMP-T-X", "MMP-BV-X"]

INTRO = """\
# Overhang Monte Carlo: results

{n} synthetic elections (see `mc_overhang.py` for how they are generated).
Every system faces exactly the same ballots in each scenario.

## Systems

| Name | Size | Rule |
|---|---|---|
| **MMP** | 121 | Current system. Overhanging parties keep their extra electorates; the House grows. |
| **MMP-T** | 121 | Overhang Transfer (explainer's Option 1). Only when a party overhangs: wasted party votes on ballots for its winning candidates count for it, as many as needed; then the same fraction of every split ballot for its winners; anything left is absorbed within the fixed size. |
| **MMP-BV** | 121 | Backup Vote (explainer's Option 2). At every election, a party vote for a party that doesn't qualify counts for the voter's electorate candidate's party, if that qualifies. If a party still overhangs: split-ballot transfer, then absorption, as in MMP-T. |
| **MMP-T-X**, **MMP-BV-X** | 121+ | As MMP-T / MMP-BV, but overhang the transfer can't cover is handled as under current MMP: the party keeps its extra seats and the House grows. |
| **MMP141**, **MMP-T141**, **MMP-BV141** | 141 | The same three rules with 141 seats (still 71 electorates). |

## Measures

- **Party yardstick**: each qualifying party's share of the qualifying party vote (raw party votes).
- **Bloc yardstick**: each bloc's share of *all* party votes, including its parties that missed the threshold. Centrists count with their ally.
- **Countable bloc yardstick**: the bloc yardstick without voters who wasted both ticks (used only for extra seats (b)).
- **Bloc seat deficit**: seats the worse-off bloc is short of its fair share, at the system's own size.
- **Party seat deficit (rounded)**: each party's shortfall rounded to whole seats, then summed.
- **Either-choice yardstick**: every voter counts once, for either their party vote or their electorate candidate's party, whichever makes the result most proportional (voters who wasted both ticks are left out; a party vote for a party that doesn't qualify counts for the candidate's party). The either-choice deficits are the smallest achievable over every such assignment.
- **Extra seats (a) / (b)**: seats to add beyond 121 so that no party (a) / no bloc (b, countable yardstick) is more than one seat short. **(c) / (d)**: the same on the either-choice yardstick. Searched only for the 121-seat systems; ">279" means not reached within 400 seats.

**Caveat:** voters' strategic behaviour is drawn independently of the system, so how much
strategic voting each system would actually produce is not captured.
"""


def load():
    with open(IN_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k, v in r.items():
            if v == "":
                r[k] = BIG
            else:
                try:
                    r[k] = float(v)
                except ValueError:
                    pass
    return rows


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def seats(x):
    return ">279" if x >= BIG else f"{x:.0f}"


def share(rows, cond):
    return f"{100 * sum(1 for r in rows if cond(r)) / len(rows):.0f}%"


def table(rows, title):
    n = len(rows)
    if not n:
        return f"\n## {title}\n\nNo scenarios in this group."
    L = [f"\n## {title} (n = {n})\n", "| Measure | " + " | ".join(SYSTEMS) + " |",
         "|---|" + "---|" * len(SYSTEMS)]

    def row(label, f, systems=SYSTEMS):
        L.append(f"| {label} | " + " | ".join(f(t) if t in systems else "–" for t in SYSTEMS) + " |")

    row("Bloc seat deficit: median", lambda t: f"{st.median(r[t + '_bloc_deficit'] for r in rows):.1f}")
    row("Bloc seat deficit: 90th percentile", lambda t: f"{pct([r[t + '_bloc_deficit'] for r in rows], .9):.1f}")
    row("Bloc seat deficit ≤ 1: share", lambda t: share(rows, lambda r: r[t + "_bloc_deficit"] <= 1))
    row("Party seat deficit (rounded): median",
        lambda t: f"{st.median(r[t + '_party_deficit_rounded'] for r in rows):.0f}")
    row("Party seat deficit (rounded): 90th percentile",
        lambda t: f"{pct([r[t + '_party_deficit_rounded'] for r in rows], .9):.0f}")
    row("Gallagher: median", lambda t: f"{st.median(r[t + '_gallagher'] for r in rows):.1f}")
    if "MMP_either_party_deficit" in rows[0]:
        row("Either-choice party deficit: median",
            lambda t: f"{st.median(r[t + '_either_party_deficit'] for r in rows):.1f}")
        row("Either-choice max party deficit ≤ 1: share",
            lambda t: share(rows, lambda r: r[t + "_either_max_party_deficit"] <= 1))
        row("Either-choice bloc deficit: median",
            lambda t: f"{st.median(r[t + '_either_bloc_deficit'] for r in rows):.1f}")
    row("House size: median / max",
        lambda t: f"{st.median(r[t + '_house'] for r in rows):.0f} / {max(r[t + '_house'] for r in rows):.0f}")
    keys = [("extra_b", "Extra seats (b) blocs"), ("extra_a", "Extra seats (a) parties")]
    if "MMP_extra_c" in rows[0]:
        keys += [("extra_c", "Extra seats (c) parties, either-choice"),
                 ("extra_d", "Extra seats (d) blocs, either-choice")]
    for key, lab in keys:
        row(f"{lab}: share needing 0", lambda t: share(rows, lambda r: r[t + "_" + key] == 0), SEARCHED)
        for q in (.5, .9, .95, .99):
            row(f"{lab}: {int(q * 100)}th percentile",
                lambda t, q=q: seats(pct([r[t + "_" + key] for r in rows], q)), SEARCHED)
        row(f"{lab}: never reached", lambda t: share(rows, lambda r: r[t + "_" + key] >= BIG), SEARCHED)
    return "\n".join(L)


def banded(rows):
    L = ["\n## By strategic voting: the higher bloc rate, max(s_L, s_R)\n",
         "Share of scenarios with a bloc seat deficit ≤ 1 (median bloc deficit in brackets).\n",
         "| max(s_L, s_R) | n | Overhang at 121: median | " + " | ".join(SYSTEMS) + " |",
         "|---|---|---|" + "---|" * len(SYSTEMS)]
    sb = lambda r: max(r["s_L"], r["s_R"])
    for lo in (0, .2, .4, .6, .8):
        g = [r for r in rows if lo <= sb(r) < lo + .2 or (lo == .8 and sb(r) >= 1)]
        if not g:
            continue
        cells = [f"{share(g, lambda r: r[t + '_bloc_deficit'] <= 1)} ({st.median(r[t + '_bloc_deficit'] for r in g):.1f})"
                 for t in SYSTEMS]
        L.append(f"| {lo:.0%}–{lo + .2:.0%} | {len(g)} | {st.median(r['overhang_base'] for r in g):.0f} | "
                 + " | ".join(cells) + " |")
    return "\n".join(L)


def head_to_head(rows):
    L = ["\n## Where a reform does worse than the current system on bloc fairness\n",
         "Share of scenarios where the reform's bloc seat deficit exceeds the current system's "
         "(same size) by more than the margin shown.\n",
         "| Comparison | > 0 | > 0.5 seat | > 1 seat | > 2 seats | > 3 seats |", "|---|---|---|---|---|---|"]
    for a, b in (("MMP-T", "MMP"), ("MMP-BV", "MMP"), ("MMP-T141", "MMP141"), ("MMP-BV141", "MMP141")):
        cells = [share(rows, lambda r, m=m: r[a + "_bloc_deficit"] - r[b + "_bloc_deficit"] > m)
                 for m in (0, .5, 1, 2, 3)]
        L.append(f"| {a} vs {b} | " + " | ".join(cells) + " |")
    return "\n".join(L)


def main():
    rows = load()
    out = [INTRO.format(n=len(rows))]
    out.append(table(rows, "All scenarios"))
    out.append(table([r for r in rows if max(r["s_L"], r["s_R"], r["s_M"]) <= .25],
                     "Low strategic voting: s_L, s_R and s_M all ≤ 25%"))
    out.append(table([r for r in rows if max(r["s_L"], r["s_R"]) <= .25],
                     "Low bloc strategic voting: s_L and s_R ≤ 25% (any s_M)"))
    out.append(banded(rows))
    out.append(head_to_head(rows))
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
