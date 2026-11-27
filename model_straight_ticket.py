"""Counterfactual: every voter gives their electorate vote to the candidate of
the party they gave their party vote to ("straight-ticket").

Each electorate is then won by whichever party has the most party votes there.
Candidate effects (personal votes, Epsom-style deals) disappear by assumption.

With no split ballots, the proposed transfer rule has nothing to transfer
(Steps 3-4 find no qualifying ballots), so the proposal falls back entirely to
the Independent Electoral Review rule: the overhanging party keeps its
electorates and the other parties share the remaining seats.

Qualification (5% or an electorate) is applied to the counterfactual
electorate winners.

Run:  python3 model_straight_ticket.py   (writes results_straight_ticket.json)
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent
SEATS = 120
THRESHOLD = 0.05
SHORT = {"NAT": "National", "LAB": "Labour", "GRN": "Green", "ACT": "ACT",
         "NZF": "NZ First", "TOP": "Opportunity", "TPM": "Te Pāti Māori"}
BLOCS = {"Right bloc": ["NAT", "ACT", "NZF"], "Left bloc": ["LAB", "GRN", "TPM"]}


def sainte_lague(votes, seats):
    quots = sorted(((v / (2 * k + 1), p) for p, v in votes.items() for k in range(seats)),
                   reverse=True)
    alloc = {p: 0 for p in votes}
    for _, p in quots[:seats]:
        alloc[p] += 1
    return alloc


def load_2023():
    col = {"NAT": "National Party", "LAB": "Labour Party", "GRN": "Green Party",
           "ACT": "ACT New Zealand", "NZF": "New Zealand First Party",
           "TOP": "The Opportunities Party (TOP)", "TPM": "Te Pāti Māori"}
    path = ROOT / "data/raw/2023/votes-for-registered-parties-by-electorate.csv"
    with open(path, encoding="utf-8") as f:
        rows = list(csv.reader(f))[1:]
    hdr, body = rows[0], rows[1:]
    idx = {p: hdr.index(c) for p, c in col.items()}
    total_i = hdr.index("Total Valid Party Votes")
    elecs, national, total = [], None, None
    for r in body:
        if r[0] == "Combined Totals":
            national = {p: int(r[i]) for p, i in idx.items()}
            total = int(r[total_i])
        elif "Totals" not in r[0]:
            elecs.append((r[0], {p: int(r[i]) for p, i in idx.items()}))
    actual = {"NAT": 43, "LAB": 17, "GRN": 3, "ACT": 2, "NZF": 0, "TOP": 0, "TPM": 6}
    return elecs, national, total, actual


def load_2026():
    raw = ROOT / "data/raw/2026_official"
    with open(raw / "electorates.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    elecs = [(r["electorate"], {p: int(r[p]) for p in SHORT}) for r in rows]
    actual = {p: 0 for p in SHORT}
    for r in rows:
        actual[r["winner_party"]] += 1
    national, total = {p: 0 for p in SHORT}, 0
    with open(raw / "national.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            total += int(r["party_votes"])
            if r["code"] in national:
                national[r["code"]] += int(r["party_votes"])
    return elecs, national, total, actual


def run(year, loader):
    elecs, votes, total, actual = loader()
    winners = {p: 0 for p in votes}
    detail = []
    for name, pv in elecs:
        ranked = sorted(pv, key=pv.get, reverse=True)
        w, ru = ranked[0], ranked[1]
        winners[w] += 1
        detail.append({"electorate": name, "winner": SHORT[w], "runner_up": SHORT[ru],
                       "margin_pct": round(100 * (pv[w] - pv[ru]) / sum(pv.values()), 1)})

    qual = [p for p in votes if votes[p] / total >= THRESHOLD or winners[p] > 0]
    qv = {p: votes[p] for p in qual}
    qtot = sum(qv.values())
    ent = sainte_lague(qv, SEATS)
    over = {p: winners[p] - ent[p] for p in qual if winners[p] > ent[p]}

    current = {p: max(ent[p], winners[p]) for p in qual}
    keep = {p: winners[p] for p in over}
    rest = sainte_lague({p: v for p, v in qv.items() if p not in keep},
                        SEATS - sum(keep.values()))
    review = {**rest, **keep}

    def table(alloc):
        t = {SHORT[p]: alloc[p] for p in qual}
        t["Total"] = sum(alloc.values())
        for b, ps in BLOCS.items():
            t[b] = sum(alloc.get(p, 0) for p in ps)
        return t

    def bloc_share(alloc):
        n = sum(alloc.values())
        return {b: round(100 * sum(alloc.get(p, 0) for p in ps) / n, 1)
                for b, ps in BLOCS.items()}

    return {
        "year": year,
        "qualifying": [SHORT[p] for p in qual],
        "party_vote_pct_of_qualifying": {SHORT[p]: round(100 * qv[p] / qtot, 1) for p in qual},
        "bloc_vote_pct_of_qualifying": {b: round(100 * sum(qv.get(p, 0) for p in ps) / qtot, 1)
                                        for b, ps in BLOCS.items()},
        "electorates_actual": {SHORT[p]: n for p, n in actual.items() if n},
        "electorates_straight_ticket": {SHORT[p]: n for p, n in winners.items() if n},
        "entitlement_120": {SHORT[p]: ent[p] for p in qual},
        "overhang": {SHORT[p]: n for p, n in over.items()},
        "seats": {"current_law": table(current), "proposal_equals_review_rule": table(review)},
        "bloc_seat_pct": {"current_law": bloc_share(current),
                          "proposal_equals_review_rule": bloc_share(review)},
        "electorates": detail,
    }


def main():
    out = {"note": __doc__.strip().splitlines()[0],
           "2023": run(2023, load_2023), "2026": run(2026, load_2026)}
    with open(ROOT / "results_straight_ticket.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    for y in ("2023", "2026"):
        show = {k: v for k, v in out[y].items() if k != "electorates"}
        print(json.dumps(show, ensure_ascii=False, indent=1))
        close = sorted(out[y]["electorates"], key=lambda e: e["margin_pct"])[:8]
        print("closest:", [(e["electorate"], e["winner"], e["runner_up"], e["margin_pct"]) for e in close])


if __name__ == "__main__":
    main()
