"""How many extra list seats does full proportionality need, with and without the fix?

"Levelling" = grow Parliament (Sainte-Laguë on the same votes) until every
party's entitlement covers its electorates, so no overhang is left and every
other party is topped up (the German 2013-2020 approach).

Scenarios, for 2023 and the 2026 official count:

  A. Actual ballots (real split voting).
     - current law, Review rule, proposal (adjusted votes from model.py /
       model_2026.py), levelling on raw party votes, and proposal + levelling
       (levelling applied to the proposal's adjusted votes, for any overhang
       the transfer could not cover).
  B. Straight-ticket, with Te Pāti Māori aligned: every voter gives both ticks
     to one party; anyone who ticked TPM in either vote ticks TPM in both.
     TPM keeps the electorates it actually won; every other electorate goes to
     the party-vote plurality winner. There are no split ballots, so the
     proposal = the Review rule.

Proportionality is measured against each scenario's own raw party votes for
qualifying parties: Gallagher index, plus how many seats each bloc holds above
its proportional share of the chamber.

Run:  python3 model_levelling.py   (writes results_levelling.json)
"""
import csv
import json
from pathlib import Path

import model_2026
from model_straight_ticket import SHORT, load_2023, load_2026, sainte_lague

ROOT = Path(__file__).parent
SEATS = 120
BLOCS = {"Right": ["NAT", "ACT", "NZF"], "Left": ["LAB", "GRN", "TPM"]}
CODE = {v: k for k, v in SHORT.items()}
NAMES23 = {"National Party": "NAT", "Labour Party": "LAB", "Green Party": "GRN",
           "ACT New Zealand": "ACT", "New Zealand First Party": "NZF",
           "The Opportunities Party (TOP)": "TOP", "Te Pāti Māori": "TPM"}
# Te Pāti Māori's overhang comes mainly from low turnout in the Māori
# electorates, not from strategic splitting, so it is set aside: TPM keeps its
# electorates as uncompensated extra seats (as under current law), and neither
# the fix nor levelling acts on it.
IGNORED = {"TPM"}
TPM_WON_2023 = {"Hauraki-Waikato", "Tāmaki Makaurau", "Te Tai Hauāuru",
                "Te Tai Tokerau", "Te Tai Tonga", "Waiariki"}


# ---------- seat rules ----------

def qualify(votes, elec, total):
    return [p for p in votes if votes[p] / total >= 0.05 or elec.get(p, 0) > 0]


def current_law(v, elec):
    ent = sainte_lague(v, SEATS)
    return {p: max(ent[p], elec.get(p, 0)) for p in v}


def review_rule(v, elec):
    ent = sainte_lague(v, SEATS)
    over = {p for p in v if elec.get(p, 0) > ent[p]}
    out = sainte_lague({p: x for p, x in v.items() if p not in over},
                       SEATS - sum(elec[p] for p in over))
    out.update({p: elec[p] for p in over})
    return out


def levelled(v, elec):
    """Smallest house >= 120 where Sainte-Laguë covers every party's electorates."""
    n = SEATS
    while True:
        a = sainte_lague(v, n)
        if all(a[p] >= elec.get(p, 0) for p in v):
            return a
        n += 1


# ---------- proportionality ----------

def measure(alloc, raw):
    n = sum(alloc.values())
    vt = sum(raw.values())
    lsq = (0.5 * sum((100 * alloc.get(p, 0) / n - 100 * raw[p] / vt) ** 2 for p in raw)) ** 0.5
    bloc_excess = {}
    for b, ps in BLOCS.items():
        seats = sum(alloc.get(p, 0) for p in ps)
        fair = n * sum(raw.get(p, 0) for p in ps) / vt
        bloc_excess[b] = round(seats - fair, 1)
    # Same, with the ignored parties' seats and votes left out entirely.
    a2 = {p: x for p, x in alloc.items() if p not in IGNORED}
    r2 = {p: x for p, x in raw.items() if p not in IGNORED}
    n2, vt2 = sum(a2.values()), sum(r2.values())
    ex = {b: round(sum(a2.get(p, 0) for p in ps) - n2 * sum(r2.get(p, 0) for p in ps) / vt2, 1)
          for b, ps in BLOCS.items()}
    return {"house": n, "added_seats": n - SEATS, "gallagher": round(lsq, 2),
            "bloc_seats_above_fair_share": bloc_excess,
            "bloc_seats_above_fair_share_ex_tpm": ex,
            "seats": {SHORT[p]: alloc.get(p, 0) for p in raw}}


def effective(elec):
    return {p: (0 if p in IGNORED else n) for p, n in elec.items()}


def with_ignored(alloc, elec, raw):
    """Apply a rule, then add any ignored party's uncovered electorates on top."""
    before = sum(alloc.values())
    out = dict(alloc)
    for p in IGNORED:
        if p in out:
            out[p] = max(out[p], elec.get(p, 0))
    m = measure(out, raw)
    m["added_for_overhang_rule"] = before - SEATS
    m["ignored_tpm_extra"] = sum(out.values()) - before
    return m


def proposal_votes_for(raw, elec_eff, pool):
    """Smallest transfer (wasted first, then a share f of split ballots) that
    covers each non-ignored overhang. pool: {party: (wasted, {q: split})}."""
    ent = sainte_lague(raw, SEATS)
    over = [p for p in raw if elec_eff.get(p, 0) > ent[p]]
    v = dict(raw)
    for P in over:
        wasted, split = pool[P]
        S = sum(split.values())

        def adj(a):
            x = dict(v)
            x[P] += a
            f = max(0.0, a - wasted) / S
            for q, n in split.items():
                x[q] -= f * n
            return x
        lo, hi = 0.0, wasted + S
        assert sainte_lague(adj(hi), SEATS)[P] >= elec_eff[P], "transfer cannot cover"
        for _ in range(60):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if sainte_lague(adj(mid), SEATS)[P] >= elec_eff[P] else (mid, hi)
        v = adj(hi)
    return v


def scenario(raw, elec, pool=None):
    eff = effective(elec)
    ent = sainte_lague(raw, SEATS)
    out = {"party_votes": {SHORT[p]: round(raw[p]) for p in raw},
           "electorates": {SHORT[p]: elec.get(p, 0) for p in raw},
           "entitlement_120": {SHORT[p]: n for p, n in ent.items()},
           "overhang_considered": {SHORT[p]: eff[p] - ent[p] for p in raw if eff.get(p, 0) > ent[p]},
           "rules": {}}
    r = out["rules"]
    r["current_law"] = with_ignored(current_law(raw, eff), elec, raw)
    r["review_rule"] = with_ignored(review_rule(raw, eff), elec, raw)
    r["levelling_raw_votes"] = with_ignored(levelled(raw, eff), elec, raw)
    if pool is not None:
        pv = proposal_votes_for(raw, eff, pool)
        out["proposal_adjusted_votes"] = {SHORT[p]: round(x) for p, x in pv.items()}
        r["proposal"] = with_ignored(review_rule(pv, eff), elec, raw)
        r["proposal_plus_levelling"] = with_ignored(levelled(pv, eff), elec, raw)
    else:
        r["proposal"] = dict(r["review_rule"], note="no split ballots: same as Review rule")
    return out


# ---------- scenario A: actual ballots ----------

def actual(year):
    res = json.loads((ROOT / f"results_{year}.json").read_text(encoding="utf-8"))
    raw = {CODE[k]: float(v) for k, v in res["party_votes"].items()}
    # Split-ballot pools for overhanging parties (only National's is used once
    # TPM is set aside; 2023 has no National overhang).
    pool = {CODE[k]: (t["wasted_available"], {CODE[q]: n for q, n in t["split_available"].items()})
            for k, t in res.get("transfers", {}).items()}
    if year == 2023:
        elec = {"NAT": 43, "LAB": 17, "GRN": 3, "ACT": 2, "NZF": 0, "TPM": 6}
    else:
        elec = {CODE[k]: v for k, v in res["electorates"].items()}
    return scenario(raw, elec, pool)


# ---------- scenario B: straight-ticket, TPM aligned ----------

def tpm_cross_2023():
    """National count of ballots with a TPM candidate vote and a non-TPM party vote."""
    cross = {}
    for fname in ("split-votes-general.csv", "split-votes-maori.csv"):
        with open(ROOT / "data/raw/2023" / fname, encoding="utf-8") as f:
            rows = list(csv.reader(f))
        col = rows[0].index("Te Pāti Māori")
        for r in rows[1:]:
            name = r[0].strip()
            if name.startswith("Total") or name == "Te Pāti Māori":
                continue
            key = NAMES23.get(name, "OTHER")
            cross[key] = cross.get(key, 0) + int(r[1]) * float(r[col]) / 100
    return cross


def tpm_cross_2026():
    """Estimated ballots for each winning TPM candidate by party vote (model_2026)."""
    cross = {}
    with open(ROOT / "data/raw/2026_official/electorates.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["winner_party"] != "TPM":
                continue
            est, _ = model_2026.estimate_splits(row, "TPM")
            for q, n in est.items():
                if q != "TPM":
                    cross[q] = cross.get(q, 0) + n
    return cross, {r for r in []}


def straight(year):
    if year == 2023:
        elecs, votes, total, _ = load_2023()
        cross = tpm_cross_2023()
        tpm_seats = lambda name: name in TPM_WON_2023
    else:
        elecs, votes, total, _ = load_2026()
        cross, _ = tpm_cross_2026()
        with open(ROOT / "data/raw/2026_official/electorates.csv", encoding="utf-8") as f:
            won = {r["electorate"] for r in csv.DictReader(f) if r["winner_party"] == "TPM"}
        tpm_seats = lambda name: name in won
    v = {p: float(x) for p, x in votes.items()}
    gained = sum(cross.values())
    v["TPM"] += gained
    for q, n in cross.items():
        if q in v and q != "TPM":
            v[q] -= n
    # informal / other-party party votes become TPM votes, so the valid total grows
    total = total + cross.get("INF", 0)
    elec = {p: 0 for p in v}
    for name, pv in elecs:
        elec["TPM" if tpm_seats(name) else max(pv, key=pv.get)] += 1
    qual = qualify(v, elec, total)
    raw = {p: v[p] for p in qual}
    out = scenario(raw, {p: elec[p] for p in qual})
    out["tpm_votes_gained_from_alignment"] = round(gained)
    out["tpm_party_vote_pct"] = round(100 * v["TPM"] / total, 2)
    return out


def main():
    out = {"note": __doc__.strip().splitlines()[0]}
    for y in (2023, 2026):
        out[str(y)] = {"A_actual_ballots": actual(y), "B_straight_ticket_tpm_aligned": straight(y)}
    (ROOT / "results_levelling.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    for y in ("2023", "2026"):
        for s, d in out[y].items():
            print(f"\n=== {y} {s}")
            print(" electorates:", {k: n for k, n in d["electorates"].items() if n})
            print(" entitlement:", d["entitlement_120"])
            print(" overhang considered:", d["overhang_considered"])
            for k in ("tpm_party_vote_pct", "tpm_votes_gained_from_alignment"):
                if k in d:
                    print(f" {k}: {d[k]}")
            for rule, m in d["rules"].items():
                print(f"  {rule:24s} house={m['house']:3d} levelling/overhang+={m['added_for_overhang_rule']:2d} tpm+={m['ignored_tpm_extra']} "
                      f"LSq={m['gallagher']:5.2f} bloc_ex_tpm={m['bloc_seats_above_fair_share_ex_tpm']} "
                      f"{m['seats']}")


if __name__ == "__main__":
    main()
