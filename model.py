"""2023 NZ election under the proposed overhang-transfer rule.

Data: Electoral Commission official 2023 results (data/raw/2023), fetched
from electionresults.govt.nz/electionresults_2023/statistics/.

Split-ballot counts are reconstructed from the published percentages
(count = party-vote total x percentage), so they may be off by a vote or two.

Run:  python3 model.py          (writes results_2023.json)
"""
import csv
import json
from pathlib import Path

RAW = Path(__file__).parent / "data" / "raw" / "2023"
SEATS = 120
OVERHANG_PARTY = "Te Pāti Māori"
# Electorates won by Te Pāti Māori in 2023, by Commission file number.
TPM_ELECTORATES = [66, 68, 69, 70, 71, 72]

SHORT = {
    "National Party": "National",
    "Labour Party": "Labour",
    "Green Party": "Green",
    "ACT New Zealand": "ACT",
    "New Zealand First Party": "NZ First",
    "Te Pāti Māori": "Te Pāti Māori",
}


def load_party_votes():
    votes, electorates = {}, {}
    with open(RAW / "overall-results-summary.csv", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    start = next(i for i, r in enumerate(rows) if r and r[0] == "Registered Parties with List")
    end = next(i for i, r in enumerate(rows) if r and r[0] == "Unregistered Parties")
    for r in rows[start + 1:end]:
        name = r[0].strip()
        if r[2]:  # party-vote row
            votes[name] = int(r[2])
            electorates[name] = int(r[5] or 0)
    return votes, electorates


def load_splits(electorate_no, cand_party):
    """Ballots with electorate vote for cand_party's candidate, by party vote."""
    with open(RAW / f"split-votes-electorate-{electorate_no}.csv", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    col = next(i for i, h in enumerate(header) if h.endswith(f"({cand_party})"))
    out = {}
    for r in rows[1:]:
        name = r[0].strip()
        if name.startswith("Informal") or name.startswith("Total"):
            continue
        out[name] = round(int(r[1]) * float(r[col]) / 100)
    return header[0], out


def sainte_lague(votes, seats):
    """Return seats per party. votes: {party: float}."""
    quots = []
    for p, v in votes.items():
        for k in range(seats):
            quots.append((v / (2 * k + 1), p))
    quots.sort(reverse=True)
    alloc = {p: 0 for p in votes}
    for _, p in quots[:seats]:
        alloc[p] += 1
    return alloc


def main():
    votes, elec = load_party_votes()
    total = sum(votes.values())
    # Step 1: threshold (5% or one electorate), applied before any transfer.
    qual = [p for p in votes if votes[p] / total >= 0.05 or elec[p] > 0]
    qv = {p: float(votes[p]) for p in qual}
    E = elec[OVERHANG_PARTY]

    # --- Current law: allocate 120, overhang party keeps extra electorates.
    base = sainte_lague(qv, SEATS)
    current = {p: max(base[p], elec[p]) for p in qual}

    # --- Split ballots for winning TPM candidates.
    by_electorate = {}
    wasted = 0
    split_to = {p: 0 for p in qual if p != OVERHANG_PARTY}
    for no in TPM_ELECTORATES:
        name, s = load_splits(no, OVERHANG_PARTY)
        by_electorate[name] = s
        for party, n in s.items():
            if party == OVERHANG_PARTY:
                continue
            if party in split_to:
                split_to[party] += n
            else:
                wasted += n

    # Step 3: wasted votes first, only as many as needed.
    def tpm_seats(extra, f):
        v = dict(qv)
        v[OVERHANG_PARTY] += extra + f * sum(split_to.values())
        for p, n in split_to.items():
            v[p] -= f * n
        return sainte_lague(v, SEATS)[OVERHANG_PARTY], v

    if tpm_seats(wasted, 0)[0] >= E:
        lo, hi = 0.0, float(wasted)
        for _ in range(60):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if tpm_seats(mid, 0)[0] >= E else (mid, hi)
        used_wasted, f = hi, 0.0
    else:
        used_wasted = wasted
        # Step 4: smallest f that lifts TPM's entitlement to E.
        lo, hi = 0.0, 1.0
        assert tpm_seats(wasted, 1.0)[0] >= E, "transfer cannot cover overhang"
        for _ in range(60):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if tpm_seats(wasted, mid)[0] >= E else (mid, hi)
        f = hi
    _, adj_votes = tpm_seats(used_wasted, f)
    proposal = sainte_lague(adj_votes, SEATS)

    # --- Independent Electoral Review: TPM keeps E, others share 120 - E.
    others = {p: v for p, v in qv.items() if p != OVERHANG_PARTY}
    review = sainte_lague(others, SEATS - E)
    review[OVERHANG_PARTY] = E

    # --- Germany: seats capped at party-vote entitlement.
    germany = dict(base)

    left = ["Labour Party", "Green Party", OVERHANG_PARTY]
    right = ["National Party", "ACT New Zealand", "New Zealand First Party"]
    order = right[:1] + left[:2] + right[1:] + [OVERHANG_PARTY]

    def row(alloc):
        return {SHORT[p]: alloc[p] for p in order}

    result = {
        "party_votes": {SHORT[p]: votes[p] for p in order},
        "party_votes_total_qualifying": int(sum(qv.values())),
        "tpm_electorates": E,
        "tpm_entitlement": base[OVERHANG_PARTY],
        "split_ballots": {
            "wasted (non-qualifying parties)": wasted,
            **{SHORT[p]: n for p, n in sorted(split_to.items(), key=lambda x: -x[1])},
        },
        "wasted_used": round(used_wasted),
        "f": f,
        "moved": {SHORT[p]: round(f * n) for p, n in sorted(split_to.items(), key=lambda x: -x[1])},
        "adjusted_votes": {SHORT[p]: round(adj_votes[p]) for p in order},
        "seats": {
            "current_law": row(current),
            "review_rule": row(review),
            "germany_rule": row(germany),
            "proposal": row(proposal),
        },
        "per_electorate_tpm_ballots": {
            k: {"total_for_tpm_candidate": sum(v.values()),
                "party_vote_tpm": v.get(OVERHANG_PARTY, 0),
                "labour": v.get("Labour Party", 0),
                "green": v.get("Green Party", 0)}
            for k, v in by_electorate.items()
        },
    }
    for k, alloc in result["seats"].items():
        alloc["Total"] = sum(alloc.values())
        alloc["Left bloc"] = sum(alloc[SHORT[p]] for p in left)
        alloc["Right bloc"] = sum(alloc[SHORT[p]] for p in right)

    out = Path(__file__).parent / "results_2023.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
