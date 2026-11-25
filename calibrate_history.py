"""Estimate Monte Carlo parameters from the 2005–2023 elections.

Reads data/raw/history/<year>.json and writes calibration.json, with one
record per election plus the pooled values the calibrated model samples from.

Roles (matching mc_overhang's synthetic parties):
  Left 1 / Right 1  Labour / National.
  Māori parties     Māori Party / Te Pāti Māori, Mana, Internet Mana.
  Centre            NZ First, United Future, TOP (bloc = ally).
  Bloc parties      every other party with at least 1% of the party vote.
  Minor             parties under 1% (pooled, like "Left/Right/Centre minor").

Strategic and personal voting (general electorates unless stated):
  personal π        share of Labour and National party voters whose electorate
                    vote went to another party's candidate.
  s_L, s_R          share of the bloc's other parties' voters (vote-weighted)
                    whose electorate vote went to Labour / National, less the
                    share a typical voter gives the leader through personal
                    votes, rescaled: s = (to_leader − π·w) / (1 − π) with
                    w = 0.4, the leader's typical slice of personal votes.
  s_M               Māori electorates: share of Labour and Green party voters
                    whose electorate vote went to a Māori party's candidate.

Geography (general electorates):
  lean σ            SD across electorates of logit(Left share of Left+Right
                    party vote).
  party σ           for each party, the residual SD of log(local share /
                    national share) after removing 0.5·lean (as the
                    generator applies it), split into leaders vs other parties.

Validation targets: general electorates won by a party other than Labour or
National, and the leader-vs-leader margin distribution.
"""
import json
import math
import statistics as st
from pathlib import Path

import mc_history as h

ROOT = Path(__file__).parent
LAB, NAT = "LABOUR PARTY", "NATIONAL PARTY"
CENTRE = {"NEW ZEALAND FIRST PARTY", "UNITED FUTURE", "UNITED FUTURE NEW ZEALAND",
          "THE OPPORTUNITIES PARTY (TOP)"}
MAORI = h.MAORI_PARTIES
W_LEADER = 0.4


def logit(p):
    return math.log(p / (1 - p))


def year_stats(y):
    d = h.load(y)
    tot = d["total"]
    v = d["votes"]
    bloc = {p: h.bloc_of(d, y, p)[0] for p in v}
    big = [p for p in v if v[p] / tot >= 0.01]
    minor = sum(v[p] for p in v if p not in big) / tot
    role = {}
    for p in big:
        role[p] = ("leader" if p in (LAB, NAT) else "maori" if p in MAORI
                   else "centre" if p in CENTRE else "bloc")
    L = sum(v[p] for p in v if bloc[p] == "L") / tot
    R = sum(v[p] for p in v if bloc[p] == "R") / tot
    left_gen = [p for p in big if bloc[p] == "L" and role[p] in ("leader", "bloc")]
    right_gen = [p for p in big if bloc[p] == "R" and role[p] in ("leader", "bloc")]
    centre = [p for p in big if role[p] == "centre"]
    maori = [p for p in big if role[p] == "maori"]

    # personal vote and strategic rates from the national crosstabs
    g = d["xt"]["gen"]

    def row(p, xt=g):
        r = xt.get(p, {})
        n = sum(x for c, x in r.items() if c not in ("#INF", "#PVO"))
        return r, n
    pis = []
    for ldr in (LAB, NAT):
        r, n = row(ldr)
        pis.append(1 - r.get(ldr, 0) / n)
    pi = st.mean(pis)

    def s_bloc(members, leader):
        num = den = 0.0
        for p in members:
            if p == leader:
                continue
            r, n = row(p)
            if n:
                num += r.get(leader, 0); den += n
        if not den:
            return None, None
        raw = num / den
        return raw, max(0.0, min(1.0, (raw - pi * W_LEADER) / (1 - pi)))
    rawL, sL = s_bloc(left_gen + [p for p in centre if bloc[p] == "L"], LAB)
    rawR, sR = s_bloc(right_gen + [p for p in centre if bloc[p] == "R"], NAT)
    mx = d["xt"]["mao"]
    num = den = 0.0
    for p in ("LABOUR PARTY", "GREEN PARTY"):
        r, n = row(p, mx)
        num += sum(r.get(mp, 0) for mp in MAORI); den += n
    sM = num / den if den else None

    # Māori electorates: Māori-party share of the party vote
    pl = d["plist"]
    mi = [i for i, p in enumerate(pl) if p in MAORI]
    maori_share = [sum(e[4][i] for i in mi) / 1000 for e in d["el"] if e[1] == 1]

    # geography in general electorates
    gen = [e for e in d["el"] if e[1] == 0]
    li = [i for i, p in enumerate(pl) if bloc[p] == "L"]
    ri = [i for i, p in enumerate(pl) if bloc[p] == "R"]
    nat_L = sum(v[p] for p in pl if bloc[p] == "L")
    nat_R = sum(v[p] for p in pl if bloc[p] == "R")
    leans = []
    for e in gen:
        l_, r_ = sum(e[4][i] for i in li), sum(e[4][i] for i in ri)
        leans.append(logit(l_ / (l_ + r_)) - logit(nat_L / (nat_L + nat_R)))
    lean_sd = st.pstdev(leans)
    resid = {}
    for i, p in enumerate(pl):
        if p in MAORI or v[p] / tot < 0.01:
            continue
        sgn = 0.5 if bloc[p] == "L" else -0.5
        if p in CENTRE:
            sgn = 0.0
        share_nat = v[p] / tot
        xs = [math.log(max(e[4][i], 1) / 1000 / share_nat) - sgn * lean for e, lean in zip(gen, leans)]
        resid[p] = st.pstdev(xs)

    # validation: general electorates won by non-leaders; leader margins
    nonleader_wins = sum(1 for e in gen if pl[e[2]] not in (LAB, NAT)) if gen else 0
    margins = []
    il, inn = pl.index(LAB), pl.index(NAT)
    for e in gen:
        if len(e) > 6:
            continue
        cs = e[5]
        margins.append(abs(cs[il] - cs[inn]) / 1000)

    return {
        "year": y,
        "left_share_all": L, "right_share_all": R, "left_frac": L / (L + R),
        "minor_under_1pct": minor,
        "n_left_gen": len(left_gen), "n_right_gen": len(right_gen),
        "n_centre": len(centre), "n_maori": len(maori),
        "leader_share_left": v[LAB] / sum(v[p] for p in left_gen),
        "leader_share_right": v[NAT] / sum(v[p] for p in right_gen),
        "centre_shares": {p: v[p] / tot for p in centre},
        "centre_ally": {p: bloc[p] for p in centre},
        "maori_party_share_mean": st.mean(maori_share) if maori_share else 0.0,
        "personal": pi, "s_L_raw": rawL, "s_L": sL, "s_R_raw": rawR, "s_R": sR, "s_M": sM,
        "lean_sd": lean_sd,
        "party_sigma": {p: round(x, 3) for p, x in resid.items()},
        "sigma_leaders": st.mean(resid[p] for p in resid if p in (LAB, NAT)),
        "sigma_others": st.mean(resid[p] for p in resid if p not in (LAB, NAT)),
        "nonleader_general_wins": nonleader_wins,
        "leader_margin_median": st.median(margins), "leader_margin_lt5": sum(x < .05 for x in margins) / len(margins),
        "electorate_turnout_general": st.mean(e[3] for e in gen),
        "electorate_turnout_maori": st.mean(e[3] for e in d["el"] if e[1] == 1),
    }


def main():
    years = [year_stats(y) for y in h.YEARS]
    keys = ["left_frac", "minor_under_1pct", "n_left_gen", "n_right_gen", "n_centre", "n_maori",
            "leader_share_left", "leader_share_right", "maori_party_share_mean", "personal",
            "s_L_raw", "s_L", "s_R_raw", "s_R", "s_M", "lean_sd", "sigma_leaders", "sigma_others",
            "nonleader_general_wins", "leader_margin_median", "leader_margin_lt5",
            "electorate_turnout_general", "electorate_turnout_maori"]
    print("| " + " | ".join(["key"] + [str(y["year"]) for y in years]) + " |")
    print("|" + "---|" * (len(years) + 1))
    for k in keys:
        print("| " + " | ".join([k] + [f"{y[k]:.3f}" if isinstance(y[k], float) else str(y[k]) for y in years]) + " |")
    print("\ncentre parties:", [(y["year"], {p: round(s, 3) for p, s in y["centre_shares"].items()}, y["centre_ally"]) for y in years])
    print("party sigma:", [(y["year"], y["party_sigma"]) for y in years])
    (ROOT / "calibration.json").write_text(json.dumps(years, indent=2))


if __name__ == "__main__":
    main()
