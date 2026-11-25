"""2026 NZ election (preliminary count) under the proposed overhang-transfer rule.

Inputs (data/raw/2026_preliminary): party votes and electorate winners from the
preliminary count, treated as final (special votes ignored).

Split votes are not published for preliminary results, so they are estimated:
for each electorate won by an overhanging party, the number of ballots with an
electorate vote for its winner and a party vote for party q is

    est[q] = min(party_votes[q], k * party_votes[q] * rate_2023[q])

where rate_2023[q] is the 2023 share of party-q voters who gave their electorate
vote to that party's candidate (general electorates for National, Māori
electorates for Te Pāti Māori), and k is set so the estimates add up to the
winner's actual 2026 candidate vote.

When several parties overhang, each gets its own transfer share, solved jointly.
If even a 100% transfer can't cover a party's overhang, the rest is handled by
the Independent Electoral Review's rule (other parties get fewer list seats),
so Parliament stays at 120.

Run:  python3 model_2026.py      (writes results_2026.json)
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent
RAW23 = ROOT / "data" / "raw" / "2023"
RAW26 = ROOT / "data" / "raw" / "2026_preliminary"
SEATS = 120
Q = ["NAT", "LAB", "GRN", "ACT", "NZF", "TOP", "TPM"]
NAMES23 = {"NAT": "National Party", "LAB": "Labour Party", "GRN": "Green Party",
           "ACT": "ACT New Zealand", "NZF": "New Zealand First Party",
           "TOP": "The Opportunities Party (TOP)", "TPM": "Te Pāti Māori"}
SHORT = {"NAT": "National", "LAB": "Labour", "GRN": "Green", "ACT": "ACT",
         "NZF": "NZ First", "TOP": "Opportunity", "TPM": "Te Pāti Māori"}


def rates_2023(fname, target):
    """Share of each party's voters who electorate-voted for `target`'s candidate."""
    with open(RAW23 / fname, encoding="utf-8") as f:
        rows = list(csv.reader(f))
    col = rows[0].index(NAMES23[target])
    rate, other_n, other_w = {}, 0, 0.0
    inv = {v: k for k, v in NAMES23.items()}
    for r in rows[1:]:
        name, n, pct = r[0].strip(), int(r[1]), float(r[col]) / 100
        if name.startswith("Total"):
            continue
        if name.startswith("Informal"):
            rate["INF"] = pct
        elif name in inv:
            rate[inv[name]] = pct
        else:
            other_n += n
            other_w += n * pct
    rate["OTHER"] = other_w / other_n
    return rate


RATES = {"NAT": rates_2023("split-votes-general.csv", "NAT"),
         "TPM": rates_2023("split-votes-maori.csv", "TPM")}


def estimate_splits(row, party):
    pv = {q: int(row[q]) for q in Q + ["OTHER"]}
    pv["INF"] = int(row["party_informal"])
    target = int(row["winner_votes"])
    r = RATES[party]
    base = {q: pv[q] * r[q] for q in pv}
    assert sum(pv.values()) >= target
    lo, hi = 0.0, 100.0
    for _ in range(100):
        k = (lo + hi) / 2
        tot = sum(min(pv[q], k * base[q]) for q in pv)
        lo, hi = (k, hi) if tot < target else (lo, k)
    k = hi
    return {q: min(pv[q], k * base[q]) for q in pv}, k


def sainte_lague(votes, seats):
    quots = sorted(((v / (2 * k + 1), p) for p, v in votes.items() for k in range(seats)), reverse=True)
    alloc = {p: 0 for p in votes}
    for _, p in quots[:seats]:
        alloc[p] += 1
    return alloc


def main():
    nat = {}
    with open(RAW26 / "national.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            nat.setdefault(r["code"], [0, 0])
            nat[r["code"]][0] += int(r["party_votes"])
            nat[r["code"]][1] += int(r["electorates_won"])
    votes = {q: nat[q][0] for q in Q}
    elec = {q: nat[q][1] for q in Q}
    total_all = sum(v[0] for v in nat.values())
    qual = [q for q in Q if votes[q] / total_all >= 0.05 or elec[q] > 0]
    qv = {q: float(votes[q]) for q in qual}

    base = sainte_lague(qv, SEATS)
    current = {q: max(base[q], elec[q]) for q in qual}
    over = [q for q in qual if elec[q] > base[q]]

    # Estimated split ballots for each overhanging party's winners.
    with open(RAW26 / "electorates.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    pools, per_elec = {}, {}
    for P in over:
        wasted, split = 0.0, {q: 0.0 for q in qual if q != P}
        for row in rows:
            if row["winner_party"] != P:
                continue
            est, k = estimate_splits(row, P)
            wasted += est["OTHER"]
            for q in split:
                split[q] += est[q]
            per_elec.setdefault(P, []).append({
                "electorate": row["electorate"], "winner_votes": int(row["winner_votes"]),
                "own_party_vote": round(est[P]), "scale_k": round(k, 3),
                **{SHORT[q]: round(est[q]) for q in split}, "not_in_parliament": round(est["OTHER"]),
            })
        pools[P] = {"wasted": wasted, "split": split}

    def adjusted(t):
        v = dict(qv)
        for P, amt in t.items():
            w, S = pools[P]["wasted"], sum(pools[P]["split"].values())
            from_w = min(amt, w)
            f = max(0.0, amt - w) / S
            v[P] += amt
            for q, n in pools[P]["split"].items():
                v[q] -= f * n
        return v

    def cap(P):
        return pools[P]["wasted"] + sum(pools[P]["split"].values())

    def final_alloc(t, residual):
        """Seats after transfers; parties in `residual` keep their electorates
        and the rest of the 120 seats are shared by everyone else (Review rule)."""
        adj = adjusted(t)
        keep = {P: elec[P] for P in residual}
        rest = sainte_lague({q: v for q, v in adj.items() if q not in keep}, SEATS - sum(keep.values()))
        return {**rest, **keep}

    residual = []
    while True:
        t = {P: 0.0 for P in over}
        for _ in range(50):
            prev = dict(t)
            for P in over:
                if P in residual:
                    t[P] = cap(P)
                    continue
                def ok(a):
                    tt = dict(t); tt[P] = a
                    return final_alloc(tt, residual)[P] >= elec[P]
                if ok(cap(P)):
                    lo, hi = 0.0, cap(P)
                    for _ in range(60):
                        mid = (lo + hi) / 2
                        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
                    t[P] = hi
                else:
                    t[P] = cap(P)
            if all(abs(t[P] - prev[P]) < 0.5 for P in over):
                break
        alloc = final_alloc(t, residual)
        short = [P for P in over if P not in residual and alloc[P] < elec[P]]
        if not short:
            break
        residual += short
    adj = adjusted(t)
    proposal = alloc

    # Comparisons
    review = sainte_lague({q: v for q, v in qv.items() if q not in over}, SEATS - sum(elec[P] for P in over))
    review.update({P: elec[P] for P in over})
    germany = dict(base)

    transfers = {}
    for P in over:
        w, S = pools[P]["wasted"], sum(pools[P]["split"].values())
        f = max(0.0, t[P] - w) / S
        transfers[SHORT[P]] = {
            "electorates": elec[P], "entitled_before": base[P],
            "wasted_available": round(w), "wasted_used": round(min(t[P], w)),
            "split_available": {SHORT[q]: round(n) for q, n in sorted(pools[P]["split"].items(), key=lambda x: -x[1])},
            "f": f, "moved": {SHORT[q]: round(f * n) for q, n in sorted(pools[P]["split"].items(), key=lambda x: -x[1])},
            "total_moved": round(t[P]), "fully_covered": P not in residual,
        }

    order = ["LAB", "GRN", "TPM", "TOP", "NAT", "ACT", "NZF"]
    left, right = ["LAB", "GRN", "TPM"], ["NAT", "ACT", "NZF"]
    qual_total = sum(qv.values())

    def row(a):
        d = {SHORT[q]: a[q] for q in order}
        d["Total"] = sum(a.values())
        d["Left bloc"] = sum(a[q] for q in left)
        d["Right bloc"] = sum(a[q] for q in right)
        d["Opportunity"] = a["TOP"]
        return d

    result = {
        "note": "Preliminary count treated as final; split votes estimated from 2023 patterns.",
        "party_votes": {SHORT[q]: votes[q] for q in order},
        "qualifying_total": int(qual_total),
        "vote_share_of_qualifying": {
            "Left bloc": sum(votes[q] for q in left) / qual_total,
            "Right bloc": sum(votes[q] for q in right) / qual_total,
            "Opportunity": votes["TOP"] / qual_total,
        },
        "electorates": {SHORT[q]: elec[q] for q in order},
        "entitlement_120": {SHORT[q]: base[q] for q in order},
        "rates_2023": {P: {k: round(v, 4) for k, v in RATES[P].items()} for P in over},
        "transfers": transfers,
        "adjusted_votes": {SHORT[q]: round(adj[q]) for q in order},
        "residual_overhang": [SHORT[P] for P in residual],
        "seats": {"current_law": row(current), "review_rule": row(review),
                  "germany_rule": row(germany), "proposal": row(proposal)},
        "per_electorate_estimates": {SHORT[P]: v for P, v in per_elec.items()},
    }
    (ROOT / "results_2026.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    show = {k: v for k, v in result.items() if k != "per_electorate_estimates"}
    print(json.dumps(show, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
