"""Summarise runs/<experiment>/measures.csv (from measures.py) into runs/summary_measures.md.

Scope (user decision, 24 Nov 2026): current MMP, the transfer family (MMP-T,
MMP-T-X, MMP-BV, MMP-BV-X at 121 and 141), MMP141 (the size increase) and the
Review's cap at 141 (CMP-Review141). Pure PR appears only as a labelled
measurement benchmark. Other comparators in measures.csv are not reported.

Main text uses only the HEADLINE measures. Everything else is in the appendix.
  1. Steps: each row builds on the one before (Experiment 3, with a fixed-ballot
     version from Experiment 2).
  2. Size options at 141: {no transfer, transfer} × {leftover grows, leftover absorbed}.
  3. One question per experiment about step 1 (the transfer alone).
  4. The proportionality bracket: does the conclusion depend on the measure?
  5. Where the transfer does worse, and the paired bloc seat–vote gap.
  Appendix: every measure, bloc variants, tails, paired comparisons.

Rates carry a 95% Monte Carlo margin (Experiment 3: clustered by walk).

Run:  python3 analyse_measures.py
"""
import csv
import json
import math
import statistics as st
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
RUNS = ROOT / "runs"
OUT = RUNS / "summary_measures.md"

# (column, label, how to summarise: "med", "medmax", "rate", "p90")
HEADLINE = [
    ("house_excess", "House above base: median / max", "medmax"),
    ("touched_pct", "Voters whose party vote counts differently: median / 90th %", "p90"),
    ("seats_lost_max", "Most seats a party loses: median / max", "medmax"),
    ("inversion_all", "Minority-bloc majority", "rate"),
    ("bloc_gap_pts", "Bloc seat–vote gap, points: median", "med"),
    ("gallagher_all", "Gallagher (standard)", "med"),
    ("os_C_win", "Gallagher (adjusted: one-share + rescued voters)", "med"),
    ("overhang", "Overhang: median", "med0"),
]
SHORT = {"house_excess": "House above base", "touched_pct": "Voters counted differently (%)",
         "seats_lost_max": "Most seats a party loses", "inversion_all": "Minority-bloc majority",
         "bloc_gap_pts": "Bloc seat–vote gap (points)",
         "gallagher_all": "Gallagher, standard", "os_C_win": "Gallagher, adjusted (one-share + rescued voters)",
         "overhang": "Overhang"}
# The four Gallagher-form indices, in increasing adjustment. One-share + rescued voters uses winning
# candidates only (os_C_win), matching one-share (os_D_win); see measures_deliberations_combined.md.
BRACKET = [("gallagher_all", "Standard"), ("gallagher_qual", "Qualifying parties"),
           ("os_D_win", "One-share"), ("os_C_win", "One-share + rescued voters")]
LABEL = {
    "MMP": "MMP (current, 121)", "MMP-T-X": "Transfer, leftover grows (MMP-T-X)",
    "MMP-T": "Transfer, leftover absorbed (MMP-T)", "MMP-BV-X": "Transfer + Backup Vote (MMP-BV-X)",
    "MMP-BV": "Transfer + Backup Vote, absorbed (MMP-BV)", "MMP141": "MMP at 141, grows (MMP141)",
    "CMP-Review141": "MMP at 141, capped (Review rule)", "CMP-Review140": "MMP at 140, capped (Review rule)",
    "MMP-T-X141": "Transfer at 141, grows (MMP-T-X141)", "MMP-T141": "Transfer at 141, capped (MMP-T141)",
    "MMP-BV-X141": "Transfer + Backup Vote at 141 (MMP-BV-X141)", "MMP-BV141": "Transfer + BV at 141, capped",
    "MMP140": "MMP at 140", "MMP-T-X140": "Transfer at 140", "MMP-BV-X140": "Transfer + Backup Vote at 140",
    "PR5": "Benchmark: pure PR, 5%", "PR3.5": "Benchmark: pure PR, 3.5%",
    "PR5-141": "Benchmark: pure PR at 141, 5%", "PR3.5-141": "Benchmark: pure PR at 141, 3.5%",
}
SCOPE = ["MMP", "MMP-T-X", "MMP-T", "MMP-BV-X", "MMP-BV", "MMP141", "CMP-Review141", "MMP-T-X141", "MMP-T141",
         "MMP-BV-X141", "MMP-BV141", "PR5", "PR3.5"]
STEPS = [("MMP", "Current MMP"), ("MMP-T-X", "1. + transfer (leftover grows the House)"),
         ("MMP-T-X141", "2. + 20 list seats"), ("MMP-BV-X141", "3. + Backup Vote")]
SIZE = ["MMP", "MMP141", "CMP-Review141", "MMP-T-X141", "MMP-T141"]
PAIRS = [("MMP-T-X", "MMP"), ("MMP-T-X141", "MMP141")]
LOWER_IS_BETTER = ["house_excess", "touched_pct", "seats_lost_max", "inversion_all", "bloc_gap_pts", "gallagher_all",
                   "gallagher_qual", "os_D_win", "os_C_win", "bloc_deficit_all", "bloc_deficit_qual", "overhang"]


# ======================= loading and stats =======================

def load(name):
    path = RUNS / name / "measures.csv"
    if not path.exists():
        return None
    rows = []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            for k, v in r.items():
                if k in ("exp", "system", "majority"):
                    continue
                if v == "":
                    r[k] = None
                else:
                    try:
                        r[k] = float(v)
                    except ValueError:
                        pass
            r["bloc_gap_pts"] = bloc_gap_pts(r)
            rows.append(r)
    return rows


def bloc_gap_pts(r):
    """Bloc seat–vote gap in percentage points: |Left seats − Left's share of all party votes × House|
    as a share of the House. With two blocs this equals the Gallagher index computed on blocs."""
    g, h = r.get("bloc_gap_L"), r.get("house")
    return 100 * abs(g) / h if isinstance(g, float) and isinstance(h, float) and h else None


def by_system(rows):
    g = defaultdict(list)
    for r in rows:
        g[r["system"]].append(r)
    return g


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))]


def margin(vals, clusters=None):
    """Mean and 95% margin; clustered if cluster ids are given."""
    n = len(vals)
    mean = sum(vals) / n
    if clusters:
        c = defaultdict(list)
        for v, k in zip(vals, clusters):
            c[k].append(v)
        means = [sum(v) / len(v) for v in c.values()]
        se = st.pstdev(means) / math.sqrt(len(means)) if len(means) > 1 else 0.0
    else:
        se = st.pstdev(vals) / math.sqrt(n) if n > 1 else 0.0
    return mean, 1.96 * se


def stat(x, col, how, cluster=None):
    vals = [r[col] or 0.0 for r in x]
    if how == "rate":
        mean, m = margin(vals, [r[cluster] for r in x] if cluster else None)
        return f"{100 * mean:.1f}% ±{100 * m:.1f}"
    if how == "medmax":
        return f"{st.median(vals):.0f} / {max(vals):.0f}"
    if how == "p90":
        return f"{st.median(vals):.1f} / {q(vals, .9):.1f}"
    if how == "med0":
        return f"{st.median(vals):.0f}"
    return f"{st.median(vals):.2f}"


def center(x, col, how):
    vals = [r[col] or 0.0 for r in x]
    return sum(vals) / len(vals) if how == "rate" else st.median(vals)


def fmt_delta(d, how):
    if how == "rate":
        return f"{100 * d:+.1f} pts"
    if how == "med0":
        return f"{d:+.0f}"
    if how == "med" and abs(d) < 10:
        return f"{d:+.2f}"
    return f"{d:+.1f}"


# ======================= tables =======================

def headline_table(rows, systems, cluster=None, labels=None, deltas=False, note=None):
    g = by_system(rows)
    L = ["| System | " + " | ".join(h[1] for h in HEADLINE) + " |", "|---|" + "---|" * len(HEADLINE)]
    prev = None
    for s in systems:
        if s not in g:
            continue
        x = g[s]
        cells = []
        for col, _, how in HEADLINE:
            c = stat(x, col, how, cluster)
            if deltas and prev is not None:
                c += f" ({fmt_delta(center(x, col, how) - center(prev, col, how), how)})"
            cells.append(c)
        L.append(f"| {(labels or {}).get(s, LABEL.get(s, s))} | " + " | ".join(cells) + " |")
        prev = x
    if note:
        L.append(f"\n{note}")
    return "\n".join(L)


def bracket_box(sets):
    L = ["\n## Box: does the conclusion depend on how proportionality is measured?\n",
         "Medians, Gallagher form (0 = perfect). The four indices, in increasing adjustment: "
         "**Standard**: every party, share of all party votes. "
         "**Qualifying parties**: only parties that won seats, against their share of the qualifying vote (what the earlier "
         "reports used; leans towards MMP over the Backup Vote). "
         "**One-share**: each voter whose party vote counts is counted once, through the party vote or, if it elected someone, "
         "the electorate vote (leans towards the transfer, by design). "
         "**One-share + rescued voters** (the adjusted Gallagher in the headline tables): as one-share, plus voters whose "
         "party vote missed the threshold count for their electorate candidate's party if that candidate won (leans towards "
         "the Backup Vote).\n",
         "Also shown: the Sainte-Laguë index (SLI, all votes; the standard index matching the allocation formula, which weights "
         "small parties' over- or under-representation heavily) and minority-bloc majority counted on all party votes (headline) "
         "and on qualifying party votes.\n",
         "| Experiment | Comparison | " + " | ".join(l for _, l in BRACKET) + " | SLI | Minority-bloc majority: all votes / qualifying votes |",
         "|---|---|---|---|---|---|---|---|"]
    for name, rows in sets:
        if not rows:
            continue
        g = by_system(rows)
        for a, b in PAIRS:
            if a not in g or b not in g:
                continue
            cells = [f"{st.median(r[c] for r in g[b]):.2f} → {st.median(r[c] for r in g[a]):.2f}" for c, _ in BRACKET]
            cells.append(f"{st.median(r['sli_all'] for r in g[b]):.1f} → {st.median(r['sli_all'] for r in g[a]):.1f}")
            inv = lambda x, c: 100 * sum(r[c] for r in x) / len(x)
            cells.append(f"{inv(g[b], 'inversion_all'):.1f}% → {inv(g[a], 'inversion_all'):.1f}% / "
                         f"{inv(g[b], 'inversion_qual'):.1f}% → {inv(g[a], 'inversion_qual'):.1f}%")
            L.append(f"| {name} | {b} → {a} | " + " | ".join(cells) + " |")
    e3 = by_system(dict(sets).get("Exp 3") or [])
    ex = ""
    if "MMP-T-X141" in e3:
        md = lambda c: st.median(r[c] for r in e3["MMP-T-X141"])
        ex = (f" (with the transfer at 141, the qualifying-parties index is {md('gallagher_qual'):.2f} but the standard "
              f"index is {md('gallagher_all'):.2f})")
    L.append("\nWhy the standard index moves so little: it counts votes for parties below the threshold (about 4% of the "
             f"vote in Experiment 3), which win no seats under any rule here. That floor dominates it{ex}, so differences "
             "between overhang rules show up mainly in the adjusted indices.\n")
    L.append("\nCaveat: the one-share indices (and to a lesser extent the standard and qualifying-parties indices) reward a "
             "larger House through finer rounding. Where MMP's House grows and the transfer's doesn't, part of any MMP "
             "advantage on them is that granularity, "
             "not a better fit (see the 2005–2023 note).")
    return "\n".join(L)


def worse_table(sets):
    """Every headline and bracket measure where the transfer is worse than its no-transfer counterpart."""
    head = {c for c, _, _ in HEADLINE}
    cols = [(c, SHORT[c], h) for c, l, h in HEADLINE] + [(c, l, "med") for c, l in BRACKET if c not in head] + \
           [("bloc_deficit_all", "Bloc deficit (all votes)", "med"), ("bloc_deficit_qual", "Bloc deficit (qualifying)", "med")]
    L = ["\n## Where the transfer does worse\n",
         "Every headline and bracket measure on which the transfer (MMP-T-X, or MMP-T-X141) does worse than the same rule "
         "without it, on the same elections. Gap = mean of (transfer − counterpart) over paired elections, with a 95% margin; "
         "'worse in' = share of elections where the transfer is worse by more than a small margin. Only gaps whose margin "
         "excludes zero are listed.\n",
         "| Experiment | Comparison | Measure | Counterpart → transfer (centre) | Gap (mean, 95%) | Worse in / better in |",
         "|---|---|---|---|---|---|"]
    n_rows = 0
    for name, rows, keyf, cluster in sets:
        if not rows:
            continue
        idx = {(keyf(r), r["system"]): r for r in rows}
        keys = sorted({keyf(r) for r in rows}, key=str)
        g = by_system(rows)
        for a, b in PAIRS:
            if a not in g or b not in g:
                continue
            for col, lab, how in cols:
                pairs = [(idx[(k, a)], idx[(k, b)]) for k in keys if (k, a) in idx and (k, b) in idx]
                d = [(x[col] or 0) - (y[col] or 0) for x, y in pairs]
                cl = [x[cluster] for x, _ in pairs] if cluster else None
                mean, m = margin(d, cl)
                if not (mean - m > 1e-9):
                    continue
                tol = 0.5 if col in ("house_excess", "seats_lost_max", "overhang") else 0.05 if how != "rate" else 0.5
                worse = 100 * sum(v > tol for v in d) / len(d)
                better = 100 * sum(v < -tol for v in d) / len(d)
                c0, c1 = center(g[b], col, how), center(g[a], col, how)
                cc = f"{100 * c0:.1f}% → {100 * c1:.1f}%" if how == "rate" else f"{c0:.2f} → {c1:.2f}"
                gap = f"{100 * mean:+.1f} pts ±{100 * m:.1f}" if how == "rate" else f"{mean:+.2f} ±{m:.2f}"
                L.append(f"| {name} | {b} → {a} | {lab} | {cc} | {gap} | {worse:.0f}% / {better:.0f}% |")
                n_rows += 1
    if not n_rows:
        L.append("| – | – | none | – | – | – |")
    return "\n".join(L)


def gap_paired_table(sets):
    """Paired mean difference in the bloc seat–vote gap, transfer minus counterpart, on the same elections."""
    L = ["\n### Bloc seat–vote gap: paired difference\n",
         "Mean of (transfer − counterpart) in percentage points over the same elections, with its standard error "
         "(Experiment 3: clustered by walk) and 95% margin. Positive means the transfer's gap is wider.\n",
         "| Experiment | Comparison | Median gap: counterpart → transfer | Mean difference | SE | 95% margin |",
         "|---|---|---|---|---|---|"]
    for name, rows, keyf, cluster in sets:
        if not rows:
            continue
        idx = {(keyf(r), r["system"]): r for r in rows}
        keys = sorted({keyf(r) for r in rows}, key=str)
        g = by_system(rows)
        for a, b in PAIRS:
            if a not in g or b not in g:
                continue
            pairs = [(idx[(k, a)], idx[(k, b)]) for k in keys if (k, a) in idx and (k, b) in idx]
            d = [(x["bloc_gap_pts"] or 0) - (y["bloc_gap_pts"] or 0) for x, y in pairs]
            mean, m = margin(d, [x[cluster] for x, _ in pairs] if cluster else None)
            L.append(f"| {name} | {b} → {a} | {center(g[b], 'bloc_gap_pts', 'med'):.2f} → "
                     f"{center(g[a], 'bloc_gap_pts', 'med'):.2f} | {mean:+.2f} | {m / 1.96:.2f} | ±{m:.2f} |")
    return "\n".join(L)


def history_table(rows):
    sysl = ["MMP", "MMP-T-X", "MMP-BV-X"]
    by = {(int(r["year"]), r["system"]): r for r in rows}
    years = sorted({int(r["year"]) for r in rows})
    cols = [("house", "House"), ("touched_pct", "Voters counted differently %"), ("seats_lost_max", "Most seats lost"),
            ("inversion_all", "Minority-bloc majority"), ("gallagher_all", "Gallagher (standard)"),
            ("os_C_win", "Gallagher (adjusted: one-share + rescued voters)"), ("os_D_win", "One-share")]
    L = ["| Year | Overhang | System | " + " | ".join(c[1] for c in cols) + " |", "|---|---|---|" + "---|" * len(cols)]
    for y in years:
        for s in sysl:
            r = by.get((y, s))
            if r is None:
                continue
            cells = [f"{r[c]:.0f}" if c in ("house", "seats_lost_max", "inversion_all") else f"{r[c]:.2f}" for c, _ in cols]
            L.append(f"| {y} | {r['overhang']:.0f} | {s} | " + " | ".join(cells) + " |")
    return "\n".join(L)


def one_share_2026(d, seats):
    """Approximate one-share indices for 2026: (one-share, one-share + rescued voters), winning candidates only.
    Counted votes are the qualifying parties' party votes; the flexible ballots are the estimated split ballots
    behind National's and Te Pāti Māori's winners (results_2026.json, from 2023 split patterns), and the rescued
    voters are the estimated sub-threshold party votes behind those winners. Split ballots behind other parties'
    winners are not estimated, so this is approximate."""
    import numpy as np
    import measures as ms
    names = list(d["party_votes"])
    idx = {n: i for i, n in enumerate(names)}
    base = np.array([float(d["party_votes"][n]) for n in names])
    flows, rescued = {}, np.zeros(len(names))
    for P, rows in d["per_electorate_estimates"].items():
        for r in rows:
            for q in names:
                if q != P and r.get(q, 0) > 0:
                    flows[(idx[q], idx[P])] = flows.get((idx[q], idx[P]), 0.0) + r[q]
            rescued[idx[P]] += r.get("not_in_parliament", 0)
    fr = np.array([k[0] for k in flows], dtype=int)
    to = np.array([k[1] for k in flows], dtype=int)
    amt = np.array(list(flows.values()), dtype=float)
    st_ = np.array([float(seats[n]) for n in names])
    return (ms.one_share_gallagher(base, fr, to, amt, st_)[0],
            ms.one_share_gallagher(base + rescued, fr, to, amt, st_)[0])


def row_2026():
    """The 2026 official result (results_2026.json, split votes estimated from 2023)."""
    path = ROOT / "results_2026.json"
    if not path.exists():
        return ""
    import mc_overhang as m
    d = json.loads(path.read_text(encoding="utf-8"))
    votes = {}
    with open(ROOT / "data/raw/2026_official/national.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            votes[r["party"] if r["code"] == "OTHER" else {"NAT": "National", "LAB": "Labour", "GRN": "Green",
                                                            "ACT": "ACT", "NZF": "NZ First", "TOP": "Opportunity",
                                                            "TPM": "Te Pāti Māori"}[r["code"]]] = int(r["party_votes"])
    total = sum(votes.values())
    names = list(d["party_votes"])
    elec = d["electorates"]
    adj = d["adjusted_votes"]
    a = m.sainte_lague([adj[n] for n in names], list(range(len(names))), 120)
    tx = {n: max(a[i], elec[n]) for i, n in enumerate(names)}
    ent = d["entitlement_120"]
    left = {"Labour", "Green", "Te Pāti Māori", "Opportunity"}  # Opportunity with the left, as in Experiment 3
    lv = sum(v for n, v in votes.items() if n in left)
    rv = sum(v for n, v in votes.items() if n in ("National", "ACT", "NZ First"))
    touched = sum(t["wasted_used"] + (sum(t["split_available"].values()) if t["f"] > 0 else 0)
                  for t in d["transfers"].values())
    ovh = sum(max(0, elec[n] - ent[n]) for n in names)
    other = sum(v for n, v in votes.items() if n not in names)
    lv_all = lv + other / 2  # sub-threshold parties split evenly between the blocs, as in Experiment 3's 2026 start
    out = ["| Rule | House above 120 | Voters whose party vote counts differently | Most seats a party loses | "
           "Minority-bloc majority | Bloc seat–vote gap, points | Gallagher (standard) | "
           "Gallagher (adjusted: one-share + rescued voters, approximate) | One-share (approximate) | Overhang |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for lab, seats, moved in (("MMP (current law)", {n: d["seats"]["current_law"][n] for n in names}, False),
                              ("Transfer, leftover grows (MMP-T-X)", tx, True),
                              ("Transfer, leftover absorbed (MMP-T)", {n: d["seats"]["proposal"][n] for n in names}, True)):
        house = sum(seats.values())
        g = math.sqrt(0.5 * sum((100 * seats.get(n, 0) / house - 100 * v / total) ** 2 for n, v in votes.items()))
        ls = sum(s for n, s in seats.items() if n in left)
        maj = "L" if 2 * ls > house else "R" if 2 * (house - ls) > house else "none"
        inv = "yes" if maj not in ("none", "L" if lv > rv else "R") else "no"
        lost = max(0, max(ent[n] - seats[n] for n in names))
        gap = 100 * abs(ls - house * lv_all / total) / house
        osd, osc = one_share_2026(d, seats)
        out.append(f"| {lab} | {house - 120} | {100 * touched / total if moved else 0:.1f}% | {lost} | {inv} | {gap:.2f} | "
                   f"{g:.2f} | {osc:.2f} | {osd:.2f} | {ovh} |")
    out.append("\nSeats under the transfer-with-growth rule: " + ", ".join(f"{n} {tx[n]}" for n in names) +
               f". Overridden party votes (qualifying votes counted for another party): "
               f"{sum(t['total_moved'] - t['wasted_used'] for t in d['transfers'].values()):,}. "
               "Left bloc includes Opportunity, as in Experiment 3; for the bloc seat–vote gap, votes for parties below the "
               "threshold are split evenly between the blocs. The one-share indices are approximate: split ballots are "
               "estimated only behind National's and Te Pāti Māori's winners.")
    return "\n".join(out)


def escalation_table(sets):
    L = ["| Scenario | System | " + " | ".join(h[1] for h in HEADLINE) + " |", "|---|---|" + "---|" * len(HEADLINE)]
    for name, rows in sets:
        if not rows:
            continue
        g = by_system(rows)
        for s in ("MMP", "MMP-T-X", "MMP141", "MMP-T-X141"):
            if s in g:
                L.append(f"| {name} | {LABEL.get(s, s)} | " +
                         " | ".join(stat(g[s], c, h, "walk") for c, _, h in HEADLINE) + " |")
    return "\n".join(L)


# ======================= appendix =======================

def appendix_all(rows, title, cluster=None, systems=SCOPE):
    g = by_system(rows)
    systems = [s for s in systems if s in g]
    L = [f"\n### {title}: every measure\n",
         "Medians unless stated. Standard, qualifying parties, one-share, one-share + rescued voters: the four Gallagher-form "
         "indices (see the box). LH: Loosemore–Hanby (all votes). SLI: Sainte-Laguë index. "
         "Bloc deficits in seats against all votes / qualifying votes / countable votes / one-share. "
         "Minority-bloc majority with centrists counted with their ally (all votes / qualifying votes) and with centrists set aside.\n",
         "| System | n | Standard | Qualifying parties | One-share | One-share + rescued | LH | SLI | Bloc deficit: all / qual / countable / one-share | Bloc seat–vote gap, points: median / 90th | Minority-bloc majority: all / qual / no centrists | House: median / 95th / 99th / max |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in systems:
        x = g[s]
        md = lambda c: st.median(r[c] for r in x)
        hs = [r["house"] for r in x]
        bg = [r["bloc_gap_pts"] or 0.0 for r in x]
        L.append(f"| {LABEL.get(s, s)} | {len(x)} | {md('gallagher_all'):.2f} | {md('gallagher_qual'):.2f} | {md('os_D_win'):.2f} | "
                 f"{md('os_C_win'):.2f} | {md('lh_all'):.2f} | {md('sli_all'):.2f} | "
                 f"{md('bloc_deficit_all'):.1f} / {md('bloc_deficit_qual'):.1f} / {md('bloc_deficit_countable'):.1f} / {md('bloc_deficit_os'):.1f} | "
                 f"{st.median(bg):.2f} / {q(bg, .9):.2f} | "
                 f"{stat(x, 'inversion_all', 'rate', cluster)} / {stat(x, 'inversion_qual', 'rate', cluster)} / "
                 f"{stat(x, 'inversion_nocentre', 'rate', cluster)} | "
                 f"{st.median(hs):.0f} / {q(hs, .95):.0f} / {q(hs, .99):.0f} / {max(hs):.0f} |")
    L += ["\nCosts and tails.\n",
          "| System | Overridden % of votes: median / 90th / max | Rescued %: median | Touched %: median / 99th | "
          "Worst-hit party's vote moved: median / 90th | A party loses 2+ seats | Bloc deficit (all): 90th / 99th | "
          "House > base +5 / +10 / +20 |",
          "|---|---|---|---|---|---|---|---|"]
    for s in systems:
        x = g[s]
        ov = [r["overridden_pct"] for r in x]
        tc = [r["touched_pct"] for r in x]
        wp = [r["max_party_overridden_pct"] for r in x]
        bd = [r["bloc_deficit_all"] for r in x]
        he = [r["house_excess"] for r in x]
        L.append(f"| {LABEL.get(s, s)} | {st.median(ov):.2f} / {q(ov, .9):.2f} / {max(ov):.2f} | "
                 f"{st.median(r['rescued_pct'] for r in x):.2f} | {st.median(tc):.2f} / {q(tc, .99):.2f} | "
                 f"{st.median(wp):.1f}% / {q(wp, .9):.1f}% | {100 * sum(r['parties_lost_2plus'] > 0 for r in x) / len(x):.0f}% | "
                 f"{q(bd, .9):.1f} / {q(bd, .99):.1f} | "
                 + " / ".join(f"{100 * sum(h > k for h in he) / len(he):.0f}%" for k in (5, 10, 20)) + " |")
    return "\n".join(L)


def appendix_paired(rows, title, keyf):
    idx = {(keyf(r), r["system"]): r for r in rows}
    keys = {keyf(r) for r in rows}
    cols = [("gallagher_all", .05), ("gallagher_qual", .05), ("os_D_win", .05), ("bloc_deficit_all", .5), ("house", 1)]
    L = [f"\n### {title}: paired comparisons\n",
         "Share of the same elections where the first system is better / worse than the second by more than a small margin "
         "(0.05 on the indices, 0.5 seats on bloc deficit, 1 seat on House size).\n",
         "| Comparison | Standard | Qualifying parties | One-share | Bloc deficit | House smaller / larger |", "|---|---|---|---|---|---|"]
    for a, b in PAIRS + [("MMP-T", "MMP"), ("MMP-BV-X", "MMP-T-X"), ("MMP-BV-X141", "MMP-T-X141"),
                         ("CMP-Review141", "MMP141"), ("MMP-T141", "MMP-T-X141")]:
        cells = []
        for k, tol in cols:
            d = [idx[(x, a)][k] - idx[(x, b)][k] for x in keys if (x, a) in idx and (x, b) in idx]
            cells.append("–" if not d else
                         f"{100 * sum(v < -tol + 1e-9 for v in d) / len(d):.0f}% / {100 * sum(v > tol - 1e-9 for v in d) / len(d):.0f}%")
        L.append(f"| {a} vs {b} | " + " | ".join(cells) + " |")
    return "\n".join(L)


# ======================= main =======================

def main():
    e3, e2, e1, h = load("exp3_baseline"), load("exp2"), load("exp1"), load("exp2_history")
    esc, cop = load("exp3_escalation"), load("exp3_copycat")
    L = ["# Shared measures across Experiments 1–3\n",
         "Computed by `measures.py` from the raw ballot states in `runs/<experiment>/records.jsonl.gz` "
         "(definitions in the `measures.py` docstring). Scope: current MMP, the transfer family, the 141-seat size increase, "
         "and the Review's cap applied at 141. Pure PR appears only as a labelled benchmark for what no overhang rule can fix.\n",
         "**Headline measures** (main text): House above its base size; voters whose party vote is counted, in whole or in "
         "part, for a party other than the one ticked; the most seats any party loses against its raw entitlement; "
         "minority-bloc majority (the bloc with fewer party votes holds a majority; centrists with their ally); the standard "
         "Gallagher index (all parties, all votes); overhang (raw, at the base size). Lower is better on every one.\n"]

    if e3:
        L += ["\n## 1. Steps: what each change adds (Experiment 3, voters adapt; 1,000 walks × 5 elections, 2029–2041)\n",
              "Each row builds on the one before; brackets show the change from the row above.\n",
              headline_table(e3, [s for s, _ in STEPS] + ["PR3.5"], "walk", labels={**dict(STEPS),
                             "PR3.5": "Benchmark: pure PR, 3.5% (MMP-pathway ballots)"}, deltas=True,
                             note="The benchmark row's change is against step 3; it is a measurement floor, not an option.")]
    if e2:
        L += ["\nThe same steps on fixed ballots (Experiment 2, 5,000 calibrated scenarios; voters don't adapt):\n",
              headline_table(e2, [s for s, _ in STEPS], labels=dict(STEPS), deltas=True)]
    if e3:
        L += ["\n## 2. Size options at 141: does the size increase need a cap?\n",
              "{no transfer, transfer} × {leftover overhang grows the House, leftover absorbed within 141}, against MMP at 121. "
              "Experiment 3; the capped rule without a transfer (Review rule at 141) is applied to the MMP141 pathway's ballots, "
              "so its voters are not modelled as adapting to a cap.\n",
              headline_table(e3, SIZE, "walk")]
    if e2:
        L += ["\nFixed ballots (Experiment 2):\n", headline_table(e2, SIZE)]

    L.append("\n## 3. Step 1, the transfer alone: one question per experiment\n")
    if h:
        L += ["\n### Real elections: what would it have done? (2005–2023 at 120 seats, and 2026)\n",
              history_table(h),
              "\nOne-share differences in the table are House-size granularity, not fit: allocate the transfer-adjusted votes "
              "at MMP's House size and the one-share index matches MMP exactly (2023: 0.257 at 122 seats; 2005: 0.226 at 121). Every 2005–2023 "
              "overhang was fully covered by the transfer, so its House stays at 120 and the grow fallback never fires.\n",
              "\n**2026 official result** (split votes estimated from 2023):\n", row_2026()]
    if e1:
        L += ["\n### Where does it break? (Experiment 1: 5,000 deliberately extreme synthetic elections)\n",
              headline_table(e1, ["MMP", "MMP-T-X", "MMP-T"])]
    if e2:
        L += ["\n### Typical New Zealand elections (Experiment 2: 5,000 scenarios calibrated to 2005–2023)\n",
              headline_table(e2, ["MMP", "MMP-T-X", "MMP-T"])]
    if e3:
        L += ["\n### When voters adapt, and if gaming escalates (Experiment 3)\n",
              escalation_table([("Baseline", e3), ("Copycat", cop), ("Escalation", esc)])]

    sets = [(n, r) for n, r in (("Exp 2 history", h), ("Exp 1", e1), ("Exp 2", e2), ("Exp 3", e3)) if r]
    L.append(bracket_box(sets))
    paired_sets = [("Exp 2 history", h, lambda r: r["year"], None), ("Exp 1", e1, lambda r: r["scenario"], None),
                   ("Exp 2", e2, lambda r: r["scenario"], None),
                   ("Exp 3", e3, lambda r: (r["walk"], r["year"]), "walk")]
    L.append(worse_table(paired_sets))
    L.append(gap_paired_table(paired_sets))

    L.append("\n---\n\n# Appendix\n")
    if e3:
        L += [appendix_all(e3, "Experiment 3 (baseline)", "walk"),
              appendix_paired(e3, "Experiment 3 (baseline)", lambda r: (r["walk"], r["year"]))]
    if esc:
        L.append(appendix_all(esc, "Experiment 3 (escalation)", "walk"))
    if e2:
        L += [appendix_all(e2, "Experiment 2 (calibrated)"), appendix_paired(e2, "Experiment 2", lambda r: r["scenario"])]
    if e1:
        L += [appendix_all(e1, "Experiment 1 (stress test)"), appendix_paired(e1, "Experiment 1", lambda r: r["scenario"])]
    if h:
        L.append(appendix_all(h, "2005–2023 elections (7 elections; rates are counts out of 7)",
                              systems=["MMP", "MMP-T-X", "MMP-T", "MMP-BV-X", "MMP140", "CMP-Review140", "MMP-T-X140",
                                       "MMP-BV-X140", "PR5", "PR3.5"]))
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
