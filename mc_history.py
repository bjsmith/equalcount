"""Current System vs Proposed System (Option 2) on actual elections, 2005–2023.

Data: data/raw/history/<year>.json, built from the Electoral Commission's
per-electorate split-vote tables (party vote × electorate candidate), with
party votes by electorate for 2005. Each file holds national party votes,
electorates won, the Option 2 reassignment of wasted party votes, the split
ballots for each party's winning candidates, and per-electorate shares.

2023: Port Waikato's poll was cancelled (candidate death); its seat is given
to National, who won the by-election.

Blocs: a party that supported a government after that election belongs to
that government's bloc; any other party is placed by where its voters' general
electorate votes went (Labour candidate → Left, National candidate → Right).

Uses the seat rules and measures from mc_overhang.py, with 120 seats (the
size actually used at these elections).

Run:  python3 mc_history.py        (prints tables, writes results_history.json)
"""
import json
from pathlib import Path

import mc_overhang as m

ROOT = Path(__file__).parent
YEARS = [2005, 2008, 2011, 2014, 2017, 2020, 2023]
LAB, NAT = "LABOUR PARTY", "NATIONAL PARTY"

# Parties that supported a government after each election (confidence and
# supply or coalition), by bloc.
GOVT = {
    2005: {"L": ["LABOUR PARTY", "JIM ANDERTON'S PROGRESSIVE", "NEW ZEALAND FIRST PARTY",
                 "UNITED FUTURE NEW ZEALAND", "GREEN PARTY"], "R": ["NATIONAL PARTY", "ACT NEW ZEALAND"]},
    2008: {"R": ["NATIONAL PARTY", "ACT NEW ZEALAND", "UNITED FUTURE", "MAORI PARTY"],
           "L": ["LABOUR PARTY", "GREEN PARTY", "JIM ANDERTON'S PROGRESSIVE"]},
    2011: {"R": ["NATIONAL PARTY", "ACT NEW ZEALAND", "UNITED FUTURE", "MAORI PARTY"],
           "L": ["LABOUR PARTY", "GREEN PARTY", "MANA"]},
    2014: {"R": ["NATIONAL PARTY", "ACT NEW ZEALAND", "UNITED FUTURE", "MAORI PARTY"],
           "L": ["LABOUR PARTY", "GREEN PARTY", "INTERNET MANA"]},
    2017: {"L": ["LABOUR PARTY", "NEW ZEALAND FIRST PARTY", "GREEN PARTY"],
           "R": ["NATIONAL PARTY", "ACT NEW ZEALAND"]},
    2020: {"L": ["LABOUR PARTY", "GREEN PARTY", "MAORI PARTY"], "R": ["NATIONAL PARTY", "ACT NEW ZEALAND"]},
    2023: {"R": ["NATIONAL PARTY", "ACT NEW ZEALAND", "NEW ZEALAND FIRST PARTY"],
           "L": ["LABOUR PARTY", "GREEN PARTY", "TE PATI MAORI"]},
}
MAORI_PARTIES = {"MAORI PARTY", "TE PATI MAORI", "MANA", "INTERNET MANA"}


def load(year):
    return json.loads((ROOT / f"data/raw/history/{year}.json").read_text(encoding="utf-8"))


def bloc_of(d, year, party):
    for b, ps in GOVT[year].items():
        if party in ps:
            return b, "government"
    # voter lean: general-electorate candidate votes for Labour vs National
    x = d["xt"]["gen"].get(party) or d["xt"]["gen"].get("#OTHER", {})
    lab, nat = x.get(LAB, 0), x.get(NAT, 0)
    return ("L" if lab >= nat else "R"), "voter lean"


def build(year):
    """Assemble a scenario dict in the shape mc_overhang's seat rules expect."""
    d = load(year)
    names = sorted(d["votes"], key=lambda p: -d["votes"][p])
    parties, how = [], {}
    for n in names:
        b, why = bloc_of(d, year, n)
        x = m.Party(n.title(), b)
        x.ally = b
        x.bloc = "M" if n in MAORI_PARTIES else b
        parties.append(x)
        how[n] = (b, why)
    idx = {n: i for i, n in enumerate(names)}
    votes = [float(d["votes"][n]) for n in names]
    elec = [d["elec"].get(n, 0) for n in names]
    qual = [idx[n] for n in d["qual"]]
    o2 = [votes[i] + d["o2"].get(n, 0) if i in qual else 0.0 for i, n in enumerate(names)]
    pools = {idx[P]: (float(d["wasted"].get(P, 0)), {idx[q]: float(v) for q, v in pq.items()})
             for P, pq in d["pools"].items()}
    bloc_votes = {b: sum(votes[i] for i in range(len(names)) if parties[i].ally == b) for b in "LR"}
    both = {b: 0.0 for b in "LR"}
    for n, v in d["both"].items():
        both[parties[idx[n]].ally] += v
    s = {"params": {}, "parties": parties, "votes": votes, "o2_votes": o2, "elec": elec, "qual": qual,
         "pools": pools, "total": float(d["total"]), "bloc_votes": bloc_votes,
         "bloc_votes_countable": {b: bloc_votes[b] - both[b] for b in "LR"},
         "both_wasted": sum(both.values())}
    return s, how, d


def main():
    m.SEATS = 120
    m.SYSTEMS = {
        "MMP": (m.current_system, 120, True),
        "MMP-T": (lambda s, H: m.proposed_system(s, H, "T"), 120, True),
        "MMP-BV": (lambda s, H: m.proposed_system(s, H, "BV"), 120, True),
        "MMP-T-X": (lambda s, H: m.proposed_system(s, H, "T", grow=True), 120, True),
        "MMP-BV-X": (lambda s, H: m.proposed_system(s, H, "BV", grow=True), 120, True),
    }
    out = {}
    rows = []
    for y in YEARS:
        s, how, d = build(y)
        res = m.evaluate(s)
        base = m.sainte_lague(s["votes"], s["qual"], 120)
        ov = {s["parties"][i].name: s["elec"][i] - base[i] for i in s["qual"] if s["elec"][i] > base[i]}
        info = res["MMP-BV"]["info"]
        out[y] = {
            "blocs": {n.title(): f"{b} ({w})" for n, (b, w) in how.items() if d["votes"][n] / d["total"] >= 0.005},
            "overhang_at_120": ov,
            "seats": {k: {s["parties"][i].name: r["alloc"][i] for i in s["qual"]} for k, r in res.items()},
            "measures": {k: {kk: (round(v, 2) if isinstance(v, float) else v) for kk, v in r.items()
                             if kk in ("house", "gallagher", "party_deficit", "party_deficit_rounded",
                                       "max_party_deficit", "bloc_deficit", "bloc_deficit_countable",
                                       "extra_a", "extra_b")} for k, r in res.items()},
            "bloc_short": {k: {b: round(v, 2) for b, v in r["bloc_short"].items()} for k, r in res.items()},
            "transfers": {k: {"votes_moved": round(r["info"].get("moved", 0)),
                              "absorbed": [s["parties"][i].name for i in r["info"].get("absorbed_parties", [])]}
                          for k, r in res.items() if k != "MMP"},
        }
        rows.append((y, s, res, ov, info))
    (ROOT / "results_history.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

    fx = lambda x: ">280" if x is None else x
    print("| Year | Overhang at 120 | System | House | Gallagher | Party def. (rounded) | Bloc def. (countable) | +a / +b | Votes moved · absorbed |")
    print("|---|---|---|---|---|---|---|---|---|")
    for y, s, res, ov, info in rows:
        for k, r in res.items():
            inf = r["info"]
            print(f"| {y} | {', '.join(f'{a} {b}' for a, b in ov.items()) or 'none'} | {k} | {r['house']} | "
                  f"{r['gallagher']:.2f} | {r['party_deficit_rounded']} | {r['bloc_deficit']:.1f} ({r['bloc_deficit_countable']:.1f}) | "
                  f"{fx(r['extra_a'])} / {fx(r['extra_b'])} | "
                  f"{round(inf.get('moved', 0)):,} · {', '.join(s['parties'][i].name for i in inf.get('absorbed_parties', [])) or '–'} |")
    for y, s, res, ov, info in rows:
        print(f"\n{y}: " + "; ".join(
            f"{s['parties'][i].name} ({s['parties'][i].ally}) " + "/".join(str(r['alloc'][i]) for r in res.values())
            for i in s["qual"]) + "   [MMP/MMP-T/MMP-BV]")
        print("   bloc short L/R:", {k: {b: round(v, 1) for b, v in r["bloc_short"].items()} for k, r in res.items()})


CENTRE = {"NEW ZEALAND FIRST PARTY", "UNITED FUTURE NEW ZEALAND", "UNITED FUTURE", "THE OPPORTUNITIES PARTY (TOP)"}


def history_state(year, s, how, d):
    """Ballot state for measures.py. Parties: those in the split-vote tables
    (d["plist"]), plus the rest grouped as "Other L" / "Other R" by bloc."""
    import measures as ms
    plist = d["plist"]
    names_all = sorted(d["votes"], key=lambda p: -d["votes"][p])
    rest = {b: [n for n in names_all if n not in plist and how[n][0] == b] for b in "LR"}
    names = plist + ["Other L", "Other R"]
    P = len(names)
    idx = {n: i for i, n in enumerate(names)}
    meta = [(n.title(), how[n][0], "maori" if n in MAORI_PARTIES else "centre" if n in CENTRE else "bloc")
            for n in plist] + [("Other L", "L", "minor"), ("Other R", "R", "minor")]
    votes = [d["votes"][n] for n in plist] + [sum(d["votes"][n] for n in rest[b]) for b in "LR"]
    elec = [d["elec"].get(n, 0) for n in plist] + [0, 0]
    qual = [idx[n] for n in d["qual"]]
    other_w = {b: votes[idx[f"Other {b}"]] for b in "LR"}
    ow = sum(other_w.values()) or 1
    N = [[0.0] * (P + 1) for _ in range(P)]
    for part in ("gen", "mao"):
        for q, row in d["xt"][part].items():
            rows = [(idx[q], 1.0)] if q in idx else [(idx[f"Other {b}"], other_w[b] / ow) for b in "LR"]
            for c, x in row.items():
                col = idx.get(c, P)  # minor candidates, informal and party-vote-only → no candidate
                for r, wgt in rows:
                    N[r][col] += x * wgt
    W = [[0.0] * P for _ in range(P)]
    for Pp, pq in d["pools"].items():
        for q, x in pq.items():
            W[idx[q]][idx[Pp]] += x
        W[idx["Other L"]][idx[Pp]] += d["wasted"].get(Pp, 0)  # wasted ballots for its winners (row immaterial)
    el = []
    for e in d["el"]:
        name, mao, w, tot, _pv, cv = e[:6]
        if len(e) > 6:  # Port Waikato 2023: cancelled poll, seat credited to National
            el.append([mao, tot, w, tot, w, 0])
            continue
        sec = max((c for c in range(len(cv)) if c != w), key=lambda c: cv[c])
        el.append([mao, tot, w, round(tot * cv[w] / 1000), sec, round(tot * cv[sec] / 1000)])
    return {"names": [x[0] for x in meta], "ally": [x[1] for x in meta], "kind": [x[2] for x in meta],
            "votes": votes, "elec": elec, "qual": qual, "threshold": 0.05,
            "N": [[round(x) for x in r] for r in N], "W": [[round(x) for x in r] for r in W], "el": el}


def store(out_dir="runs/exp2_history"):
    """Raw results for 2005–2023 → runs/exp2_history/records.jsonl.gz (see measures.py)."""
    import measures as ms
    m.SEATS = 120
    m.SYSTEMS = {
        "MMP": (m.current_system, 120, True),
        "MMP-T": (lambda s, H: m.proposed_system(s, H, "T"), 120, True),
        "MMP-BV": (lambda s, H: m.proposed_system(s, H, "BV"), 120, True),
        "MMP-T-X": (lambda s, H: m.proposed_system(s, H, "T", grow=True), 120, True),
        "MMP-BV-X": (lambda s, H: m.proposed_system(s, H, "BV", grow=True), 120, True),
        "MMP140": (m.current_system, 140, False),
        "MMP-T-X140": (lambda s, H: m.proposed_system(s, H, "T", grow=True), 140, False),
        "MMP-BV-X140": (lambda s, H: m.proposed_system(s, H, "BV", grow=True), 140, False),
    }
    w = ms.RecordWriter(f"{out_dir}/records.jsonl.gz")
    for y in YEARS:
        s, how, d = build(y)
        res = m.evaluate(s)
        st = history_state(y, s, how, d)
        sidx = {n: i for i, n in enumerate(st["names"])}
        systems = {}
        for k, r in res.items():
            alloc = [0] * len(st["names"])
            for i, x in r["alloc"].items():
                alloc[sidx[s["parties"][i].name]] = int(x)
            info = dict(r["info"])
            if "lam" in info:  # party indices → state indices
                info["lam"] = {sidx[s["parties"][i].name]: v for i, v in info["lam"].items()}
            x = {"H0": m.SYSTEMS[k][1], "alloc": alloc, "info": ms.info_json(info)}
            if "extra_a" in r:
                x["extra"] = [r.get(f"extra_{c}") for c in "abcd"]
            systems[k] = x
        w.write({"exp": "exp2_history", "key": {"year": y}, "meta": {}, "state": st, "systems": systems})
        print(y, {k: v["alloc"] for k, v in list(systems.items())[:1]})
    w.close()
    print(f"wrote {len(YEARS)} records to {out_dir}/records.jsonl.gz")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "store":
        store()
    else:
        main()
