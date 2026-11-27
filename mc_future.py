"""Experiment 3: five future elections (2029–2041) from the 2026 official result.

Each "world" carries a party system, a persistent electoral map and voter
behaviour forward from one election to the next. Three pathways share the same
random shocks in each run:

  MMP      the current system throughout (121 seats from 2029).
  MMP-T    Overhang Transfer from 2029.
  MMP-BV   Backup Vote from 2029.

Between elections the world changes in two ways:

  Exogenous   bloc swing (mean-reverting, sized from 2005–2026), party-level
              drift within blocs, centrist drift, small-party churn, new
              parties, slow drift in the electoral map.
  Behavioural voters' responses to what the last election taught them under
              their system (respond()), plus any per-world overrides written
              after reviewing each round (futures/overrides_<year>.json).

Starting point (2026): national party votes and each electorate's party votes
from the official count; the electoral map is each party's local share
relative to its national share. Behaviour starts from the ABC posterior
(abc_summary.md) and is fitted so the 2026 electorate winners are reproduced
(fit_2026()).

Run:
  python3 mc_future.py init            fit 2026, create 10 worlds × 3 pathways
  python3 mc_future.py round 2029      respond to the last round, simulate, digest
  python3 mc_future.py summary         tables across runs and rounds
"""
import copy
import csv
import json
import math
import random
import statistics as st
import sys
from pathlib import Path

import mc_overhang as m

ROOT = Path(__file__).parent
OUT = ROOT / "futures"
SEATS = 121
YEARS = [2029, 2032, 2035, 2038, 2041]
PATHWAYS = ["MMP", "MMP-T", "MMP-BV", "MMP-T-X", "MMP-BV-X",
            "MMP141", "MMP-T141", "MMP-BV141", "MMP-T-X141", "MMP-BV-X141"]


def is_reform(system):
    return "-T" in system or "-BV" in system


def size_of(system):
    return 141 if system.endswith("141") else SEATS
N_RUNS = 10
MAORI_SEATS = {"Hauraki-Waikato", "Ikaroa-Rāwhiti", "Tāmaki Makaurau", "Te Tai Hauāuru",
               "Te Tai Tokerau", "Te Tai Tonga", "Waiariki"}
CODES = ["NAT", "LAB", "GRN", "ACT", "NZF", "TOP", "TPM"]
NAMES = {"NAT": "National", "LAB": "Labour", "GRN": "Green", "ACT": "ACT", "NZF": "NZ First",
         "TOP": "Opportunity", "TPM": "Te Pāti Māori"}
ALLY = {"NAT": "R", "ACT": "R", "NZF": "R", "LAB": "L", "GRN": "L", "TPM": "L", "TOP": "L"}
ROLE = {"TPM": "maori", "TOP": "centre"}


# ======================= starting point =======================

def load_2026():
    raw = ROOT / "data/raw/2026_official"
    with open(raw / "electorates.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    nat = {}
    with open(raw / "national.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            nat[r["code"]] = nat.get(r["code"], 0) + int(r["party_votes"])
    tot = sum(nat.values())
    shares = {NAMES[c]: nat[c] / tot for c in CODES}
    shares["Other L"] = shares["Other R"] = nat["OTHER"] / tot / 2
    els = []
    for r in rows:
        pv = {NAMES[c]: int(r[c]) for c in CODES}
        pv["Other L"] = pv["Other R"] = int(r["OTHER"]) / 2
        els.append({"name": r["electorate"], "maori": r["electorate"] in MAORI_SEATS,
                    "pv": pv, "winner": NAMES[r["winner_party"]], "size": sum(pv.values())})
    return shares, els


def new_world(seed):
    rng = random.Random(seed)
    shares, els = load_2026()
    parties = {}
    for code in CODES:
        n = NAMES[code]
        parties[n] = {"ally": ALLY[code], "role": ROLE.get(code, "bloc"), "minor": False}
    for n, a in (("Other L", "L"), ("Other R", "R")):
        parties[n] = {"ally": a, "role": "minor", "minor": True}
    mult = {p: [(e["pv"][p] / e["size"]) / shares[p] if shares[p] else 1.0 for e in els] for p in parties}
    appeal = {p: [math.exp(rng.gauss(0, 0.34)) for _ in els] for p in parties}
    for k, e in enumerate(els):  # sitting MPs start with a personal following
        appeal[e["winner"]][k] *= 1.5
    return {
        "seed": seed, "year": 2026, "shares": shares, "parties": parties, "mult": mult, "appeal": appeal,
        "size": [e["size"] for e in els], "names": [e["name"] for e in els], "maori": [e["maori"] for e in els],
        "beh": {"pi": 0.20, "s": {}, "s_M": 0.0, "standouts": [], "awareness": 0.0,
                "decoy": 0.0},  # decoy: share of leader voters party-voting a partner
        "history": [],
    }


# ======================= one election =======================

def leaders(w):
    out = {}
    fixed = w["beh"].get("fixed_leader", {})
    for b in "LR":
        if b in fixed and fixed[b] in w["shares"]:
            out[b] = fixed[b]  # split-list playbook: the electorate party stays the leader
            continue
        c = [p for p, x in w["parties"].items() if x["ally"] == b and x["role"] == "bloc" and not x["minor"]]
        out[b] = max(c, key=lambda p: w["shares"][p])
    return out


def simulate(w, system, rng=None, keep_state=False):
    """Build ballots for world w and allocate seats under `system`.
    keep_state: also return the raw ballot state, allocation and transfer
    details (res["_state"], ["_alloc"], ["_info"]) for measures.py."""
    names = list(w["parties"])
    P = len(names)
    idx = {p: i for i, p in enumerate(names)}
    sh = w["shares"]
    tot_sh = sum(sh.values())
    nE = len(w["size"])
    rows = []
    for k in range(nE):
        rows.append((w["size"][k], [sh[p] / tot_sh * w["mult"][p][k] for p in names]))
    fitted = m.ipf(rows, [sh[p] / tot_sh for p in names])
    lead = leaders(w)
    beh = w["beh"]
    minors = {i for i, p in enumerate(names) if w["parties"][p]["minor"]}
    maori_ps = [i for i, p in enumerate(names) if w["parties"][p]["role"] == "maori"]
    els = []
    for k in range(nE):
        pv = fitted[k]
        cands = [i for i in range(P) if i not in minors and pv[i] > 1]
        app = {c: math.sqrt(pv[c]) * w["appeal"][names[c]][k] for c in cands}
        sa = sum(app.values())
        M = [[0.0] * P for _ in range(P)]
        mt = max(maori_ps, key=lambda i: pv[i]) if (w["maori"][k] and maori_ps) else None
        for q in range(P):
            n = pv[q]
            if n <= 0:
                continue
            x = w["parties"][names[q]]
            ally_leader = idx[lead[x["ally"]]]
            if q in minors:
                M[q][ally_leader] += n
                continue
            pers = beh["pi"] * n
            for c in cands:
                M[q][c] += pers * app[c] / sa
            rest = n - pers
            if mt is not None and x["ally"] == "L":
                target, s = mt, beh["s_M"]
            else:
                target, s = ally_leader, beh["s"].get(names[q], 0.0)
            if target == q:
                s = 0.0
            M[q][target] += rest * s
            M[q][q] += rest * (1 - s)
        els.append({"pv": pv, "M": M, "cands": cands})
    for p, k, d in beh["standouts"]:
        if p not in idx or idx[p] in minors:
            continue
        c = idx[p]
        ldr = idx[lead[w["parties"][p]["ally"]]]
        if ldr == c:
            continue
        M = els[k]["M"]
        for q in range(P):
            if q != c and w["parties"][names[q]]["ally"] == w["parties"][p]["ally"]:
                mv = d * M[q][ldr]
                M[q][ldr] -= mv; M[q][c] += mv
    for e in els:
        cv = [sum(e["M"][q][c] for q in range(P)) for c in range(P)]
        e["cv"] = cv
        e["winner"] = max(e["cands"], key=lambda c: cv[c])

    votes = [sum(e["pv"][i] for e in els) for i in range(P)]
    elec = [0] * P
    for e in els:
        elec[e["winner"]] += 1
    total = sum(votes)
    qual = [i for i in range(P) if i not in minors and (votes[i] / total >= 0.05 or elec[i] > 0)]
    qs = set(qual)
    o2 = [votes[i] if i in qs else 0.0 for i in range(P)]
    for e in els:
        for q in range(P):
            if q not in qs:
                for c in qs:
                    o2[c] += e["M"][q][c]
    pools = {}
    for Pp in qual:
        if elec[Pp]:
            split = {q: 0.0 for q in qual if q != Pp}
            wasted = 0.0
            for e in els:
                if e["winner"] == Pp:
                    for q in split:
                        split[q] += e["M"][q][Pp]
                    wasted += sum(e["M"][q][Pp] for q in range(P) if q not in qs)
            pools[Pp] = (wasted, split)
    party_objs = []
    for p in names:
        x = m.Party(p, w["parties"][p]["ally"])
        x.ally = w["parties"][p]["ally"]
        x.bloc = "M" if w["parties"][p]["role"] == "maori" else x.ally
        party_objs.append(x)
    bloc_votes = {b: sum(votes[i] for i in range(P) if party_objs[i].ally == b) for b in "LR"}
    both = {b: 0.0 for b in "LR"}
    for e in els:
        for q in range(P):
            if q not in qs:
                both[party_objs[q].ally] += sum(e["M"][q][c] for c in range(P) if c not in qs)
    s = {"params": {}, "parties": party_objs, "votes": votes, "o2_votes": o2, "elec": elec, "qual": qual,
         "pools": pools, "total": total, "bloc_votes": bloc_votes,
         "bloc_votes_countable": {b: bloc_votes[b] - both[b] for b in "LR"}, "both_wasted": sum(both.values())}
    H = size_of(system)
    if not is_reform(system):
        alloc, info = m.current_system(s, H)
    else:
        alloc, info = m.proposed_system(s, H, "T" if system.startswith("MMP-T") else "BV",
                                        grow="-X" in system)
    meas = m.measures(s, alloc)
    raw = m.sainte_lague(votes, qual, H)
    ent = raw if not system.startswith("MMP-BV") else m.sainte_lague(o2, qual, H)
    house = sum(alloc.values())
    seats = {names[i]: alloc[i] for i in qual}
    bseats = {b: sum(alloc[i] for i in qual if party_objs[i].ally == b) for b in "LR"}
    extra = {}
    if keep_state:
        import measures as ms
        kinds = []
        for p in names:
            x = w["parties"][p]
            kinds.append((p, x["ally"], "minor" if x["minor"] else "maori" if x["role"] == "maori"
                          else "centre" if x["role"] == "centre" else "bloc"))
        for k, e in enumerate(els):
            e["maori"] = w["maori"][k]
        extra = {"_state": ms.build_state(kinds, els, votes, elec, qual),
                 "_alloc": ms.alloc_list(alloc, P), "_info": ms.info_json(info)}
    return {**extra,
        "year": w["year"], "system": system,
        "shares": {p: round(100 * votes[idx[p]] / total, 2) for p in names},
        "electorates": {names[i]: elec[i] for i in range(P) if elec[i]},
        "maori_seat_winners": {names[i]: sum(1 for k, e in enumerate(els) if w["maori"][k] and e["winner"] == i)
                               for i in range(P) if any(w["maori"][k] and e["winner"] == i for k, e in enumerate(els))},
        "qualified": [names[i] for i in qual],
        "overhang_raw": {names[i]: elec[i] - raw[i] for i in qual if elec[i] > raw[i]},
        "overhang_sys": {names[i]: elec[i] - ent[i] for i in qual if elec[i] > ent[i]},
        "seats": seats, "house": house, "bloc_seats": bseats,
        "bloc_vote_pct": {b: round(100 * bloc_votes[b] / total, 1) for b in "LR"},
        "bloc_fair": {b: round(house * bloc_votes[b] / total, 1) for b in "LR"},
        "bloc_deficit": round(meas["bloc_deficit"], 2), "party_deficit_rounded": meas["party_deficit_rounded"],
        "gallagher": round(meas["gallagher"], 2),
        "seat_loss_vs_raw": {names[i]: raw[i] - alloc[i] for i in qual if alloc[i] < raw[i] and is_reform(system)},
        "votes_moved": round(info.get("moved", 0)), "absorbed": [names[i] for i in info.get("absorbed_parties", [])],
        "balancing_seats": info.get("balancing_seats", 0),
        "decoy_list": dict(w["beh"].get("decoy_list", {})),
        "majority": next((b for b in "LR" if bseats[b] * 2 > house), "none"),
        "wasted_pct": round(100 * sum(votes[i] for i in range(P) if i not in qs) / total, 2),
        "both_wasted_pct": round(100 * s["both_wasted"] / total, 2),
    }


# ======================= fitting 2026 =======================

def fit_2026():
    """Grid-search the 2026 strategic rates and standouts so the simulated
    winners match the official result."""
    shares, els = load_2026()
    w = new_world(0)
    actual = [e["winner"] for e in els]
    lead = leaders(w)
    sa = [k for k, e in enumerate(els) if e["winner"] not in (lead["L"], lead["R"]) and not e["maori"]]
    w["beh"]["standouts"] = [(els[k]["winner"], k, 0.6) for k in sa]
    best = None
    for sL in (0.2, 0.3, 0.4, 0.5):
        for sR in (0.4, 0.5, 0.6, 0.7, 0.8):
            for sM in (0.3, 0.45, 0.6, 0.75):
                w["beh"]["s"] = {p: (sL if x["ally"] == "L" else sR) for p, x in w["parties"].items()
                                 if x["role"] in ("bloc", "centre")}
                w["beh"]["s_M"] = sM
                r = simulate(w, "MMP")
                # compare electorate counts by party
                err = sum(abs(r["electorates"].get(p, 0) - sum(1 for a in actual if a == p)) for p in w["parties"])
                if best is None or err < best[0]:
                    best = (err, sL, sR, sM, r["electorates"])
    return best, w["beh"]["standouts"]


# ======================= behaviour =======================

def T(w, key, default):
    """A response strength: the value used in the 10 hand-reasoned runs is the
    default; the 1,000-walk version (mc_future_walks.py) draws one per world."""
    return w["beh"].get("temper", {}).get(key, default)


def respond(w, last, system):
    """Voters' and parties' response to the last election under `system`.
    Each rule is a piece of the reasoning written out in futures/reasoning_<year>.md.
    """
    b = w["beh"]
    sh = w["shares"]
    reform = is_reform(system)  # voters know which system the coming election uses
    lead = leaders(w)
    notes = []
    # awareness of how the reform works: some campaign coverage before the
    # first reformed election, then each visible transfer is news
    if reform:
        if w["year"] == 2026:
            b["awareness"] = T(w, "aware_start", 0.2)
        else:
            b["awareness"] = min(1.0, b["awareness"] + (T(w, "aware_visible", 0.3) if last["votes_moved"] > 0
                                                        else T(w, "aware_quiet", 0.15)))
    a = b["awareness"]

    if not reform:
        # Splitting pays under MMP: overhangs stay and the bloc keeps them.
        for bl in "LR":
            L = lead[bl]
            if last["overhang_raw"].get(L, 0) > 0:
                for p, x in w["parties"].items():
                    if x["ally"] == bl and p != L and p in b["s"]:
                        b["s"][p] = min(0.85, b["s"][p] + T(w, "mmp_escalate", 0.03))
                b["decoy"] = min(0.10, b["decoy"] + T(w, "decoy_step", 0.01))
                notes.append(f"{L} overhung and kept it: partners' voters split a little more; some {L} voters party-vote a partner")
        tpm = "Te Pāti Māori"
        if last["overhang_raw"].get(tpm, 0) > 0:
            b["s_M"] = min(0.85, b["s_M"] + T(w, "mmp_sM_step", 0.02))
            notes.append("Māori-seat strategy paid off again: it continues")
    else:
        # Under a transfer rule, splitting for an overhanging winner costs the
        # partner some party votes. Partners that lost seats campaign for two
        # ticks; others relax more slowly. Voters are only partly attentive.
        for p, x in w["parties"].items():
            if p in b["s"]:
                lost = last["seat_loss_vs_raw"].get(p, 0)
                cut = (T(w, "cut_loser", 0.45) if lost > 0 else T(w, "cut_other", 0.15)) * a
                b["s"][p] = max(0.05, b["s"][p] * (1 - cut))
        b["decoy"] = max(0.0, b["decoy"] * (1 - 0.6 * a))
        tpm = "Te Pāti Māori"
        if tpm in sh and "-X" in system:
            # Under the -X systems, whatever the transfer can't cover still
            # adds seats (as under MMP), so the TPM strategy still pays the
            # left. TPM doesn't change course; the Greens, whose voters' party
            # votes are transferred to TPM, campaign for two ticks in Māori seats.
            b["s_M"] = max(0.15, b["s_M"] * (1 - T(w, "x_sM_decay", 0.1) * a))
            notes.append(f"-X: TPM strategy still pays; Greens push two ticks; s_M → {b['s_M']:.2f}")
        elif tpm in sh:
            # TPM's overhang no longer adds seats for the left; its votes are
            # being transferred anyway, so TPM asks supporters for the party vote.
            cand_support = 0.020  # TPM candidate support beyond its party vote, nationally
            gain = min(cand_support, cand_support * T(w, "tpm_rate", 0.5) * a)
            take = min(gain, 0.5 * (sh["Green"] + sh["Labour"]) * 0.05)
            sh[tpm] += take
            tot_l = sh["Green"] + sh["Labour"]
            sh["Green"] -= take * sh["Green"] / tot_l
            sh["Labour"] -= take * sh["Labour"] / tot_l
            b["s_M"] = max(0.15, b["s_M"] * (1 - T(w, "sM_decay", 0.25) * a))
            notes.append(f"TPM asks for the party vote: +{100*take:.1f} pts from Green/Labour; s_M → {b['s_M']:.2f}")

    # Decoy party-voting: leader voters party-vote a partner (keeping the
    # electorate vote) — shift shares and make those voters split fully.
    # (applied as a share shift; their electorate votes follow via s)
    # Threshold squeeze and the backup vote
    for p, x in w["parties"].items():
        if x["minor"] or x["role"] in ("maori", "vehicle") or p in (lead["L"], lead["R"]):
            continue
        L = lead[x["ally"]]
        if sh[p] < 0.05:
            fear = T(w, "fear", 0.15) * (1 if not system.startswith("MMP-BV") else (1 - a))
            mv = fear * sh[p]
            if 0.04 <= sh[p] < 0.05:
                mv -= 0.004  # insurance votes from the leader's voters
            sh[p] -= mv; sh[L] += mv
            if abs(mv) > 0.0005:
                notes.append(f"{p} at {100*sh[p]:.1f}%: net {'squeeze' if mv > 0 else 'insurance'} {100*mv:+.1f} pts")
    if system.startswith("MMP-BV"):
        # A small-party vote is no longer wasted if the electorate vote is for
        # a qualifying ally: some voters move to small parties and minor groups.
        for bl in "LR":
            L = lead[bl]
            mv = T(w, "bv_expressive", 0.012) * a * sh[L]
            small = [p for p, x in w["parties"].items() if x["ally"] == bl and p != L
                     and x["role"] not in ("maori", "vehicle")]
            tot_small = sum(sh[p] for p in small) or 1
            for p in small:
                sh[p] += mv * sh[p] / tot_small
            sh[L] -= mv
            # their electorate votes go to a qualifying ally
            for p in small:
                if p in b["s"] and sh[p] < 0.05:
                    b["s"][p] = min(0.85, b["s"][p] + T(w, "bv_sub_split", 0.2) * a)
        notes.append(f"Backup vote understood (a={a:.2f}): small parties gain; sub-threshold voters pick a qualifying candidate")
    if b["decoy"] > 0:
        for bl in "LR":
            L = lead[bl]
            partners = [p for p, x in w["parties"].items() if x["ally"] == bl and p != L
                        and x["role"] == "bloc" and sh[p] >= 0.05]
            if partners:
                pt = max(partners, key=lambda p: sh[p])
                mv = b["decoy"] * 0.1 * sh[L]
                sh[L] -= mv; sh[pt] += mv
                b["s"][pt] = min(0.9, b["s"].get(pt, 0.4) + 0.5 * mv / max(sh[pt], 1e-6))
    return notes


def copycat(w, last, system, rng):
    """Copycat scenario (off unless w["beh"]["copycat"] is set).

    The Te Pāti Māori playbook for a big party: its supporters keep ticking
    its electorate candidates but give their party vote to an allied partner.
    The leader's list entitlement shrinks while it keeps its electorates, so
    its overhang grows, and the partner gains list seats: the bloc wins more
    seats than votes. Under MMP-family systems a bloc that watched the other
    side win more seats than votes may adopt it, and once adopted it is
    pushed further each election. Under the transfer reforms those split
    ballots would be transferred straight back, so it gains nothing and no
    bloc adopts it.
    """
    b = w["beh"]
    if not b.get("copycat") or is_reform(system):
        return []
    notes = []
    dl = b.setdefault("decoy_list", {})  # bloc -> cumulative share of leader voters moved
    other = {"L": "R", "R": "L"}
    lead = leaders(w)
    for bl in "LR":
        o = other[bl]
        if bl not in dl:
            gain_o = last["bloc_seats"][o] - last["bloc_fair"][o]
            p = T(w, "copy_base", 0.25) * min(1.0, gain_o / 5) if gain_o >= 2 else 0.0
            p += T(w, "copy_hazard", 0.0)  # adopting because it pays, whatever the other side did
            if o in dl:
                p += T(w, "copy_follow", 0.35)
            if rng.random() >= p:
                continue
            dl[bl] = 0.0
            b.setdefault("fixed_leader", {})[bl] = lead[bl]
            notes.append(f"bloc {bl} adopts the split-list playbook")
        step = T(w, "dl_step", 0.10)
        cap = T(w, "dl_cap", 0.5)
        add = min(step, cap - dl[bl])
        if add <= 0:
            continue
        L = lead[bl]
        partners = [p for p, x in w["parties"].items() if x["ally"] == bl and p != L
                    and x["role"] == "bloc" and not x["minor"]]
        if not partners:
            continue
        pt = max(partners, key=lambda p: w["shares"][p])
        mv = add * w["shares"][L]
        old = w["shares"][pt]
        w["shares"][L] -= mv
        w["shares"][pt] += mv
        # the moved voters tick the leader's candidate
        s_old = b["s"].get(pt, 0.35)
        b["s"][pt] = min(0.95, (s_old * old + 1.0 * mv) / (old + mv))
        dl[bl] += add
        notes.append(f"bloc {bl}: {100*mv:.1f} pts of {L}'s vote party-votes {pt} (cumulative {dl[bl]:.0%})")
    return notes


def exogenous(w, rng):
    """Swing, drift and churn between elections."""
    sh = w["shares"]
    P = w["parties"]
    L = sum(v for p, v in sh.items() if P[p]["ally"] == "L" and P[p]["role"] != "centre")
    R = sum(v for p, v in sh.items() if P[p]["ally"] == "R" and P[p]["role"] != "centre")
    lf = L / (L + R)
    lg = math.log(lf / (1 - lf))
    lg = 0.6 * lg + rng.gauss(0, 0.35)
    nlf = 1 / (1 + math.exp(-lg))
    kL, kR = nlf / lf, (1 - nlf) / (1 - lf)
    for p in sh:
        if P[p]["role"] == "centre":
            sh[p] *= math.exp(rng.gauss(0, 0.35))
        elif P[p]["ally"] == "L":
            sh[p] *= kL
        else:
            sh[p] *= kR
    for bl in "LR":
        members = [p for p in sh if P[p]["ally"] == bl and P[p]["role"] != "centre"]
        before = sum(sh[p] for p in members)
        for p in members:
            sh[p] *= math.exp(rng.gauss(0, 0.12 if p in leaders(w).values() else 0.3))
        after = sum(sh[p] for p in members)
        for p in members:
            sh[p] *= before / after
    if rng.random() < 0.15:  # a new party
        bl = rng.choice("LR")
        n = f"New {w['year']}"
        P[n] = {"ally": bl, "role": "bloc", "minor": False}
        share = rng.uniform(0.01, 0.04)
        for p in [q for q in sh if P[q]["ally"] == bl]:
            sh[p] *= 1 - share
        sh[n] = share
        w["mult"][n] = [math.exp(rng.gauss(0, 0.4)) for _ in w["size"]]
        w["appeal"][n] = [math.exp(rng.gauss(0, 0.34)) for _ in w["size"]]
        w["beh"]["s"][n] = st.mean(v for p, v in w["beh"]["s"].items() if P.get(p, {}).get("ally") == bl) \
            if any(P.get(p, {}).get("ally") == bl for p in w["beh"]["s"]) else 0.4
    for p in list(sh):  # parties under 0.5% fold into their side's minor group
        if not P[p]["minor"] and P[p]["role"] not in ("maori", "vehicle") and sh[p] < 0.005 \
                and p not in leaders(w).values():
            sh[f"Other {P[p]['ally']}"] += sh.pop(p)
            for d in (P, w["mult"], w["appeal"]):
                d.pop(p, None)
            w["beh"]["s"].pop(p, None)
            w["beh"]["standouts"] = [x for x in w["beh"]["standouts"] if x[0] != p]
    tot = sum(sh.values())
    for p in sh:
        sh[p] /= tot
    for p in w["mult"]:
        w["mult"][p] = [x * math.exp(rng.gauss(0, 0.05)) for x in w["mult"][p]]


# ======================= rounds =======================

def path(name):
    OUT.mkdir(exist_ok=True)
    return OUT / name


def save(worlds):
    path("worlds.json").write_text(json.dumps(worlds))


def load():
    return json.loads(path("worlds.json").read_text())


# Fitted to the 2026 winners (official count) on a finer grid across three
# seeds (electorate counts off by 2: Labour 21 vs 22, TPM 6 vs 5). The same
# values were also the best fit to the preliminary count.
FIT_2026 = {"s_L": 0.15, "s_R": 0.35, "s_M": 0.40}


def cmd_init():
    _, standouts = fit_2026()
    sL, sR, sM = FIT_2026["s_L"], FIT_2026["s_R"], FIT_2026["s_M"]
    print(f"2026 behaviour: s_L={sL} s_R={sR} s_M={sM}; standouts {standouts}")
    worlds = {}
    for r in range(N_RUNS):
        base = new_world(1000 + r)
        base["beh"]["s"] = {p: (sL if x["ally"] == "L" else sR) for p, x in base["parties"].items()
                            if x["role"] in ("bloc", "centre")}
        base["beh"]["s_M"] = sM
        base["beh"]["standouts"] = standouts
        res = simulate(base, "MMP")
        base["history"].append(res)
        for sysname in PATHWAYS:
            worlds[f"{r}|{sysname}"] = copy.deepcopy(base)
    save(worlds)
    print("2026 under MMP at 121:", json.dumps({k: res[k] for k in ("electorates", "seats", "house", "overhang_raw",
                                                                  "bloc_seats", "bloc_deficit")}))


def cmd_round(year):
    worlds = load()
    ov_file = path(f"overrides_{year}.json")
    overrides = json.loads(ov_file.read_text()) if ov_file.exists() else {}
    digest = []
    for key, w in worlds.items():
        r, sysname = key.split("|")
        system = sysname
        last = w["history"][-1]
        notes = respond(w, last, system)
        rng = random.Random(w["seed"] * 100 + year)  # same shocks across pathways
        exogenous(w, rng)
        for k, v in overrides.get(key, {}).items():  # per-world adjustments after review
            if k == "shares":
                for p, x in v.items():
                    w["shares"][p] = x
            elif k == "s":
                w["beh"]["s"].update(v)
            elif k == "s_scale":
                for p, f in v.items():
                    if p in w["beh"]["s"]:
                        w["beh"]["s"][p] = min(0.9, max(0.02, w["beh"]["s"][p] * f))
            elif k == "shift":  # [from parties, to party, points]
                for src, dst, pts in v:
                    src = [p for p in src if p in w["shares"]]
                    if dst not in w["shares"] or not src:
                        continue
                    pool = sum(w["shares"][p] for p in src)
                    amt = min(pts / 100, 0.5 * pool)
                    for p in src:
                        w["shares"][p] -= amt * w["shares"][p] / pool
                    w["shares"][dst] += amt
            else:
                w["beh"][k] = v
        w["year"] = year
        res = simulate(w, system)
        res["notes"] = notes
        w["history"].append(res)
        digest.append((int(r), sysname, res))
    save(worlds)
    lines = [f"# Round {year}\n"]
    for r, sysname, res in sorted(digest):
        top = ", ".join(f"{p} {v:.1f}" for p, v in sorted(res["shares"].items(), key=lambda x: -x[1]) if v >= 1)
        lines.append(f"## Run {r} · {sysname}\n- votes: {top}; wasted {res['wasted_pct']}%")
        lines.append(f"- electorates: {res['electorates']}; Māori seats: {res['maori_seat_winners']}")
        lines.append(f"- overhang (raw): {res['overhang_raw']}; under system: {res['overhang_sys']}; "
                     f"moved {res['votes_moved']:,}; seat losses vs raw: {res['seat_loss_vs_raw']}; absorbed {res['absorbed']}")
        lines.append(f"- seats: {res['seats']} (house {res['house']}); blocs {res['bloc_seats']} vs fair {res['bloc_fair']}; "
                     f"bloc deficit {res['bloc_deficit']}; majority {res['majority']}")
        if res["notes"]:
            lines.append("- responses applied: " + "; ".join(res["notes"]))
    path(f"digest_{year}.md").write_text("\n".join(lines) + "\n")
    print(f"wrote futures/digest_{year}.md")


def cmd_summary():
    worlds = load()
    # 2026 is the fixed starting point (the official result); only 2029 on is simulated
    years = sorted({h["year"] for w in worlds.values() for h in w["history"] if h["year"] >= 2029})
    out = ["| Year | System | Overhang (raw) median/max | House median | Bloc deficit median/max | Party def. median | "
           "Gallagher median | Wasted % median | Majority L/R/none |", "|---|---|---|---|---|---|---|---|---|"]
    for y in years:
        for sysname in PATHWAYS:
            hs = [h for k, w in worlds.items() if k.split("|")[1] == sysname for h in w["history"] if h["year"] == y]
            ov = [sum(h["overhang_raw"].values()) for h in hs]
            maj = [h["majority"] for h in hs]
            out.append(f"| {y} | {sysname} | {st.median(ov):.0f} / {max(ov)} | {st.median(h['house'] for h in hs):.0f} | "
                       f"{st.median(h['bloc_deficit'] for h in hs):.1f} / {max(h['bloc_deficit'] for h in hs):.1f} | "
                       f"{st.median(h['party_deficit_rounded'] for h in hs):.0f} | "
                       f"{st.median(h['gallagher'] for h in hs):.1f} | {st.median(h['wasted_pct'] for h in hs):.1f} | "
                       f"{maj.count('L')}/{maj.count('R')}/{maj.count('none')} |")
    path("summary.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if cmd == "init":
        cmd_init()
    elif cmd == "round":
        cmd_round(int(sys.argv[2]))
    else:
        cmd_summary()
