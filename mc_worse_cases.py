"""Scenarios where MMP-BV141 leaves a bloc at least one seat further short than
BOTH MMP (121) and MMP141 do, with the mechanism behind each.

Run:  python3 mc_worse_cases.py [N]   (writes mc_worse_cases.md)
"""
import random
import sys
from multiprocessing import Pool

import mc_overhang as m


def bloc_of(s, i):
    return s["parties"][i].ally


def features(k):
    s = m.gen_scenario(random.Random(1000 + k))
    parties, qual, elec, votes, tot = s["parties"], s["qual"], s["elec"], s["votes"], s["total"]
    qs = set(qual)
    res = {}
    for name, H, fn in (("MMP", 121, m.current_system), ("MMP141", 141, m.current_system),
                        ("BV141", 141, lambda s, H: m.proposed_system(s, H, "BV"))):
        alloc, info = fn(s, H)
        me, mc = m.measures(s, alloc), m.measures(s, alloc, "bloc_votes_countable")
        res[name] = {"alloc": alloc, "info": info, "short": me["bloc_short"], "def": me["bloc_deficit"],
                     "short_c": mc["bloc_short"], "def_c": mc["bloc_deficit"], "house": sum(alloc.values())}
    worse = all(res["BV141"]["def"] - res[x]["def"] >= 1 for x in ("MMP", "MMP141"))
    if not worse:
        return None
    short = max("LR", key=lambda b: res["BV141"]["short"][b])
    other = "R" if short == "L" else "L"

    # voters who wasted both ticks, by bloc (% of all votes)
    bw = {b: 0.0 for b in "LR"}
    # backup votes (Option 2) by the bloc they came from and the bloc they went to
    backup = {(a, b): 0.0 for a in "LR" for b in "LR"}
    for el in s["electorates"]:
        for q in range(len(parties)):
            if q in qs:
                continue
            for c in range(len(parties)):
                n = el["M"][q][c]
                if c in qs:
                    backup[(bloc_of(s, q), bloc_of(s, c))] += n
                else:
                    bw[bloc_of(s, q)] += n
    pc = lambda x: 100 * x / tot

    def overhang(H, v):
        base = m.sainte_lague(v, qual, H)
        return {i: elec[i] - base[i] for i in qual if elec[i] > base[i]}

    ov121 = overhang(121, votes)
    ov141_raw = overhang(141, votes)
    ov141_bv = overhang(141, s["o2_votes"])
    absorbed = res["BV141"]["info"].get("absorbed_parties", [])
    fair = lambda H, b: H * s["bloc_votes"][b] / tot
    return {
        "k": k, "p": s["params"], "s": s, "res": res, "short": short, "other": other,
        "bw_short": pc(bw[short]), "bw_other": pc(bw[other]),
        "backup_short_to_other": pc(backup[(short, other)]), "backup_other_to_short": pc(backup[(other, short)]),
        "backup_short_own": pc(backup[(short, short)]), "backup_other_own": pc(backup[(other, other)]),
        "ov121": {parties[i].name: n for i, n in ov121.items()},
        "ov141_raw": {parties[i].name: n for i, n in ov141_raw.items()},
        "ov141_bv": {parties[i].name: n for i, n in ov141_bv.items()},
        "ov121_short_bloc": sum(n for i, n in ov121.items() if bloc_of(s, i) == short),
        "ov141_short_bloc": sum(n for i, n in ov141_raw.items() if bloc_of(s, i) == short),
        "absorbed": [parties[i].name for i in absorbed],
        "absorbed_other_bloc": any(bloc_of(s, i) == other for i in absorbed),
        "countable_worse": all(res["BV141"]["def_c"] - res[x]["def_c"] >= 1 for x in ("MMP", "MMP141")),
    }


def classify(f):
    """Assign the main mechanism."""
    if f["absorbed_other_bloc"] and f["countable_worse"]:
        return "C. Other bloc's overhang absorbed"
    if f["backup_short_to_other"] - f["backup_other_to_short"] >= 0.8 and f["countable_worse"]:
        return "D. Backup votes cross to the other bloc"
    if f["ov121_short_bloc"] > 0 or f["ov141_short_bloc"] > 0:
        return "A. Current system's overhang offsets the short bloc's wasted votes"
    return "B. Short bloc simply has more wasted-both-ticks voters"


def describe(f):
    s, p, res, sh, ot = f["s"], f["p"], f["res"], f["short"], f["other"]
    parties, qual, tot = s["parties"], s["qual"], s["total"]
    name = {"L": "Left", "R": "Right"}
    L = [f"#### Scenario {f['k']}\n",
         f"Left:Right {p['left_frac']:.0%}:{1 - p['left_frac']:.0%} · strategic s_L {p['s_L']:.0%}, "
         f"s_R {p['s_R']:.0%}, s_M {p['s_M']:.0%} · personal vote {p['personal']:.0%} · "
         f"short bloc under MMP-BV141: **{name[sh]}**\n",
         "| Party | Bloc | Vote | Backup-vote total | Electorates | MMP | MMP141 | MMP-BV141 |",
         "|---|---|---|---|---|---|---|---|"]
    for i, x in enumerate(parties):
        if i not in qual and s["votes"][i] / tot < 0.01:
            continue
        seat = lambda r: str(res[r]["alloc"][i]) if i in qual else "out"
        L.append(f"| {x.name} | {x.ally} | {100 * s['votes'][i] / tot:.1f}% | {100 * s['o2_votes'][i] / tot:.1f}% | "
                 f"{s['elec'][i]} | {seat('MMP')} | {seat('MMP141')} | {seat('BV141')} |")
    for b in "LR":
        seats = lambda r: sum(res[r]["alloc"][i] for i in qual if parties[i].ally == b)
        sd = lambda r: f" (−{res[r]['short'][b]:.1f})" if res[r]["short"][b] >= 0.05 else ""
        L.append(f"| **{name[b]} bloc** | | {100 * s['bloc_votes'][b] / tot:.1f}% | | | "
                 f"{seats('MMP')}{sd('MMP')} | {seats('MMP141')}{sd('MMP141')} | {seats('BV141')}{sd('BV141')} |")
    L.append(f"| House | | | | | {res['MMP']['house']} | {res['MMP141']['house']} | {res['BV141']['house']} |")
    L.append("")
    L.append(f"- Voters who wasted both ticks: {name[sh]} {f['bw_short']:.1f}%, {name[ot]} {f['bw_other']:.1f}% of all votes.")
    L.append(f"- Backup votes crossing blocs: {name[sh]}→{name[ot]} {f['backup_short_to_other']:.1f}%, "
             f"{name[ot]}→{name[sh]} {f['backup_other_to_short']:.1f}%.")
    L.append(f"- Overhang under raw votes: at 121 {f['ov121'] or 'none'}; at 141 {f['ov141_raw'] or 'none'}. "
             f"Under MMP-BV141 (after backup votes): {f['ov141_bv'] or 'none'}"
             + (f"; absorbed: {', '.join(f['absorbed'])}." if f["absorbed"] else "."))
    L.append(f"- Bloc deficit, leaving out voters who wasted both ticks: MMP {res['MMP']['def_c']:.1f}, "
             f"MMP141 {res['MMP141']['def_c']:.1f}, MMP-BV141 {res['BV141']['def_c']:.1f}.\n")
    return "\n".join(L)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    with Pool() as pool:
        feats = [f for f in pool.map(features, range(n), chunksize=16) if f]
    groups = {}
    for f in feats:
        groups.setdefault(classify(f), []).append(f)
    L = [f"# MMP-BV141 at least one seat worse than both MMP and MMP141 on bloc fairness\n",
         f"{len(feats)} of {n} scenarios. Seat shortfalls are against the bloc yardstick "
         "(each bloc's share of all party votes).\n", "| Type | Scenarios |", "|---|---|"]
    for g in sorted(groups):
        L.append(f"| {g} | {len(groups[g])} |")
    for g in sorted(groups):
        fs = sorted(groups[g], key=lambda f: -(f["res"]["BV141"]["def"] - max(f["res"]["MMP"]["def"], f["res"]["MMP141"]["def"])))
        L.append(f"\n## {g} ({len(fs)} scenarios)\n")
        L.append("Scenarios: " + ", ".join(str(f["k"]) for f in fs) + "\n")
        for f in fs[:2]:
            L.append(describe(f))
    with open("mc_worse_cases.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L[:8 + len(groups)]))


if __name__ == "__main__":
    main()
