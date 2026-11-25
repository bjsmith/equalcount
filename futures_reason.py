"""Between-round reasoning for Experiment 3 (mc_future.py).

For each coming election, this reads what every world experienced at the last
one and writes per-world adjustments to futures/overrides_<year>.json, on top
of the general rules in mc_future.respond(). The reasoning behind each
adjustment is in futures/reasoning_<year>.md; the code here applies it.

Run:  python3 futures_reason.py 2032
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).parent / "futures"
TPM, GRN, LAB, NAT, ACT, NZF = "Te Pāti Māori", "Green", "Labour", "National", "ACT", "NZ First"


def T(w, key, default):
    """Response strength: the hand-reasoned value by default; drawn per world
    in the 1,000-walk version (mc_future_walks.py)."""
    return w["beh"].get("temper", {}).get(key, default)


def roles(w):
    """Leaders and partners by role, so the reasoning follows whoever holds
    each role (in the hand-reasoned runs: Labour, National, Greens, ACT...)."""
    P, sh = w["parties"], w["shares"]
    lead = {}
    fixed = w["beh"].get("fixed_leader", {})
    for b in "LR":
        c = [p for p, x in P.items() if x["ally"] == b and x["role"] == "bloc" and not x["minor"]]
        lead[b] = fixed[b] if fixed.get(b) in sh else max(c, key=lambda p: sh[p])
    part = {b: [p for p, x in P.items() if x["ally"] == b and p != lead[b] and not x["minor"]
                and x["role"] in ("bloc", "centre")] for b in "LR"}
    left_all = [p for p, x in P.items() if x["ally"] == "L" and not x["minor"] and x["role"] != "maori"]
    return lead, part, left_all


def is_reform(sysname):
    return "-T" in sysname or "-BV" in sysname


def reason_2032(key, w, last):
    """After the first election under each pathway (2029)."""
    sysname = key.split("|")[1]
    lead, part, left_all = roles(w)
    o = {}
    if not is_reform(sysname):
        # The left watched the right leader's overhang (built on its partners'
        # voters splitting) deliver seats; where the right won more seats than
        # votes and the majority, left strategists push left partners' voters
        # in marginal seats to tick the left leader's candidate.
        bs, fair = last["bloc_seats"], last["bloc_fair"]
        if bs["R"] - fair["R"] >= 1.5 and last["majority"] == "R":
            o["s_scale"] = {p: T(w, "green_push", 1.4) for p in part["L"]}
        # Where the left won on an overhang, the right copies the cup-of-tea
        # playbook more openly: right-leader supporters in safe seats party-vote
        # the biggest right partner, keeping their electorate tick.
        if bs["L"] - fair["L"] >= 1.5 and last["majority"] == "L" and part["R"]:
            partner = max(part["R"], key=lambda p: w["shares"][p])
            o["shift"] = [[[lead["R"]], partner, T(w, "decoy_shift", 1.0)]]
            o["s"] = {partner: min(0.9, w["beh"]["s"].get(partner, 0.35) + 0.08 * T(w, "decoy_shift", 1.0))}
        return o
    # Reform pathways: parties that lost seats to transfers run two-tick
    # campaigns. ACT and NZ First voters are engaged and respond fast; other
    # partners' voters (whose splits are more often personal) respond less.
    losers = last["seat_loss_vs_raw"]
    scale = {}
    for p, n in losers.items():
        if p in (lead["L"], lead["R"], TPM):
            continue
        if p in (ACT, NZF):
            scale[p] = T(w, "two_tick_big", 0.55) if n >= 3 else T(w, "two_tick_small", 0.7)
        else:
            scale[p] = T(w, "two_tick_left", 0.75)
    if scale:
        o["s_scale"] = scale
    # TPM: its overhang brings the left nothing under an absorbing reform, so
    # it campaigns for the party vote (party-led, so faster than voter
    # learning). Under -X its leftover still adds seats, so it doesn't.
    if "-X" in sysname:
        o["s_M"] = max(0.25, w["beh"]["s_M"] - 0.02)
    elif TPM in last["absorbed"] or last["overhang_sys"].get(TPM, 0) > 0:
        gap = T(w, "tpm_target1", 3.0) - last["shares"].get(TPM, 0)
        if gap > 0:
            o["shift"] = [[left_all, TPM, round(T(w, "tpm_recover", 0.5) * gap, 2)]]
        o["s_M"] = T(w, "sM_after", 0.32)
    return o


def reason_2035(key, w, last):
    """After the second election under each pathway (2032)."""
    sysname = key.split("|")[1]
    lead, part, left_all = roles(w)
    o = {}
    ovh = last["overhang_raw"]
    if not is_reform(sysname):
        # The arms race continues: where the right leader's overhang is large,
        # the left pushes harder for its partners' voters to tick its leader.
        if ovh.get(lead["R"], 0) >= 8:
            o["s_scale"] = {p: T(w, "green_push2", 1.3) for p in part["L"]}
        return o
    losers = last["seat_loss_vs_raw"]
    # Left voters have twice seen their parties lose list seats because some
    # of them ticked a right MP or a TPM candidate they liked; personal
    # splitting falls (somewhat — liking a local MP is not purely tactical).
    if sum(losers.get(p, 0) for p in left_all) >= 2:
        o["pi"] = round(max(0.12, w["beh"]["pi"] * T(w, "pi_cut", 0.85)), 3)
    # Partners still losing seats: their two-tick campaigns intensify.
    scale = {p: T(w, "two_tick_again", 0.7) for p in part["L"] + part["R"] if losers.get(p, 0) >= 2}
    if scale:
        o["s_scale"] = scale
    # TPM keeps rebuilding its party vote toward what 4–6 electorates need.
    gap = T(w, "tpm_target2", 4.0) - last["shares"].get(TPM, 0)
    if gap > 0.2 and "-X" not in sysname:
        o["shift"] = [[left_all, TPM, round(T(w, "tpm_recover", 0.5) * gap, 2)]]
    o["s_M"] = max(0.25, w["beh"]["s_M"] - (0.02 if "-X" in sysname else 0.03))
    return o


def reason_2038(key, w, last):
    """After the third election under each pathway (2035)."""
    sysname = key.split("|")[1]
    lead, part, left_all = roles(w)
    o = {}
    ovh = last["overhang_raw"]
    if not is_reform(sysname):
        if ovh.get(lead["R"], 0) >= 8:
            o["s_scale"] = {p: T(w, "green_push3", 1.2) for p in part["L"]}
        return o
    # Under a transfer rule a leader's remaining overhang comes from winning
    # electorates on plurality. Splitting *to* a winner costs your party, but
    # backing your own side's leader where the other leader would otherwise
    # win costs nothing, and it shrinks the overhang. Engaged partners'
    # voters in marginal seats start doing that.
    k, add, cap = T(w, "consol_mult", 2.0), T(w, "consol_add", 0.05), T(w, "consol_cap", 0.35)
    con = lambda p: round(min(cap, w["beh"]["s"].get(p, 0.05) * k + add), 3)
    if ovh.get(lead["R"], 0) >= 4:
        o.setdefault("s", {}).update({p: con(p) for p in part["L"]})
    if ovh.get(lead["L"], 0) >= 4:  # the mirror case
        o.setdefault("s", {}).update({p: con(p) for p in part["R"]})
    losers = last["seat_loss_vs_raw"]
    if sum(losers.get(p, 0) for p in left_all) >= 2:
        o["pi"] = round(max(0.12, w["beh"]["pi"] * T(w, "pi_cut2", 0.9)), 3)
    gap = T(w, "tpm_target2", 4.0) - last["shares"].get(TPM, 0)
    if gap > 0.2 and ovh.get(TPM, 0) > 0 and "-X" not in sysname:
        o["shift"] = [[left_all, TPM, round(T(w, "tpm_recover2", 0.4) * gap, 2)]]
    return o


def reason_2041(key, w, last):
    """After the fourth election under each pathway (2038). Same incentives as
    before 2038; voters who saw consolidation work keep at it, so the rule is
    applied again from the new starting point (doubling, capped at 0.35)."""
    return reason_2038(key, w, last)


REASONERS = {2032: reason_2032, 2035: reason_2035, 2038: reason_2038, 2041: reason_2041}


def main(year):
    worlds = json.loads((OUT / "worlds.json").read_text())
    fn = REASONERS[year]
    out = {}
    for key, w in worlds.items():
        o = fn(key, w, w["history"][-1])
        if o:
            out[key] = o
    (OUT / f"overrides_{year}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"wrote futures/overrides_{year}.json for {len(out)} worlds")
    for k, v in sorted(out.items()):
        print(" ", k, v)


if __name__ == "__main__":
    main(int(sys.argv[1]))
