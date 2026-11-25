# Overhang reform under MMP: the costs and benefits of the options

### Overhang Transfer and Backup Vote rules for New Zealand, compared with a larger Parliament and the status quo

This report assesses four options for handling overhang in New Zealand's MMP system: keeping the current rules (**MMP**); enlarging Parliament to 141 seats by adding 20 list seats (**MMP141**); and combining that enlargement with one of two counting reforms, the **Overhang Transfer (MMP-T141)** or the **Backup Vote (MMP-BV141)**.

---

## Summary

**The normative starting point.** Each voter should contribute one equal share to the party make-up of Parliament. In a compensatory system the party vote normally carries that share, and the electorate vote decides only which candidates fill part of a party's allocation. Overhang breaks this. Voters who split their ballot to elect an MP whose seat is not covered by that party's proportional entitlement shape the make-up of Parliament through both votes. Voters for parties below the threshold, conversely, contribute nothing. Restoring one share per voter requires that, for some voters, the **electorate vote** rather than the party vote counts towards proportionality.

**The reforms.**
- **MMP-T** applies only when a party overhangs. It counts just enough of the split ballots behind that party's winning electorate candidates as though the party vote had followed the electorate vote. It uses party votes for non-qualifying parties first, then a uniform fraction *f* of party votes for other qualifying parties. Any overhang left over is absorbed within a fixed House (the Independent Electoral Review's rule) or, in the "-X" variants, added to the House as under current law.
- **MMP-BV** applies at every election. A party vote for a non-qualifying party is counted for the party of the voter's electorate candidate, if that party qualifies. Any remaining overhang is then handled as under MMP-T. In effect the electorate vote becomes a contingent second preference, close to the "spare vote" the Review discussed, without any change to the ballot paper.

**How the options were tested.** Three complementary methods were used, referred to below as Experiments 1–3. All apply the seat rules to ballot-level data: party vote by electorate candidate, in every electorate.
1. **A synthetic stress test.** A Monte Carlo of 5,000 elections spanning party systems, geographies and levels of strategic ticket-splitting far more varied than New Zealand's. Ballots are held fixed across rules, to show where each rule fails.
2. **Empirical counterfactuals and a calibrated Monte Carlo.** The 2005–2023 elections were recounted under each rule from the Electoral Commission's split-vote tables. A further 5,000 synthetic elections were generated with parameters measured from those elections, or fitted to their electorate results by approximate Bayesian computation.
3. **A dynamic simulation.** 1,000 futures of five elections each, starting from the 2026 provisional result. Voters' and parties' strategies respond between elections to each rule's incentives. Further scenarios let split-list strategies escalate under current rules.

Outcomes are measured at party level (the Gallagher index) and at bloc level: each governing bloc's seat shortfall relative to its share of all party votes, and the frequency of **majority reversals**, where the bloc with fewer votes wins a majority of seats.

**What the evidence shows.**

| | Stay with MMP | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|
| Bloc-level proportionality | Worst | Little better | Better | **Best** |
| Majority reversals (dynamic simulation) | 5.6% | 4.3% | 4.6% | **4.0%** (3.6% with the grow fallback) |
| Party-level proportionality to votes as cast | Poor once splitting is entrenched | Good | **Best once voters adapt** | Good, but never exact by design |
| Size of Parliament | Variable: 131 in 2026, up to 155 (180 if splitting escalates) | 141 to 171 (197 if splitting escalates) | **Fixed at 141** | **Fixed at 141** |
| Removes the payoff from strategic splitting | No | No | **Yes** | **Yes** |
| Counts party votes exactly as cast | Yes | Yes | No, when there's an overhang | No, for sub-threshold votes and overhang |
| Extra MPs | None | 20 | 20 | 20 |

**The main conclusions.**

1. **The reforms trade a little party-level proportionality for a lot of bloc-level proportionality.** On fixed ballots, both have a higher Gallagher index than MMP141, because they deliberately count some votes for a party other than the one ticked. But they keep each *bloc* much closer to its combined vote. Since New Zealand governments are formed by blocs, that is the dimension of proportionality that decides who governs.
2. **Once voters adapt, the party-level cost largely disappears.** The reforms remove the reward for splitting, so splitting falls and overhang shrinks. In the dynamic simulation, MMP-T141's median Gallagher index is 0.45 by 2041, against 3.4 under MMP141 and 4.1 under MMP.
3. **The reforms need a larger list tier.** At 121 seats, overhang from plurality wins (a large party winning many electorates against a divided opposition) has few split ballots behind it to transfer. Absorbing it within a fixed House charges the other bloc. In the dynamic simulation that makes the absorbing reforms *more* prone to majority reversals than MMP (7–8% against 5.6%). At 141 seats this failure mode largely disappears.
4. **Their strongest benefit is insurance against escalation.** Under current rules the split-list strategy pays: a bloc leader's supporters tick its electorate candidates but party-vote a partner. If blocs adopt it because it pays, median overhang reaches 30 seats by 2041, the House up to 180, and majority reversals 11% of elections. Every reform is immune, because the strategy gains nothing under a transfer rule. Enlargement alone (MMP141) gives no such protection: its House reaches 197.
5. **MMP-BV141 comes closest to the equal-share principle.** Under all three methods it has the smallest bloc-level deviation, and it has the fewest majority reversals. It rescues many votes that the threshold wastes. Its costs are a larger departure from counting party votes as cast, a permanent (if small) party-level deviation, and a mild reward for small-party supporters who give their electorate vote to a large ally.
6. **MMP-T141 is the narrower reform.** It leaves the count unchanged unless a party overhangs, and is the most party-proportional option once voters adapt. It does less for bloc-level proportionality, because it does nothing about wasted votes.
7. **MMP141 alone buys party-level proportionality but not resistance to gaming.** It costs the same 20 seats as the reforms, leaves House size unbounded, and barely improves bloc-level proportionality on realistic elections.
8. **The status quo is cheapest now and riskiest later.** Overhang was 0–2 seats per election from 2005 to 2023, and 11 in 2026. The main risk is not today's distortion but the persistence of an incentive that nothing constrains.
9. **No overhang rule addresses the threshold.** Most bloc-level deviation remaining under every option comes from votes for parties below 5%. Lowering the threshold to 3.5% would reduce it more than any overhang rule. MMP-BV is the only option considered here that addresses it at all.

**Bottom line.** If the rules are to change, the evidence favours **MMP-BV141**, with overhang that transfers can't cover handled by letting the House grow (the "-X" fallback, MMP-BV-X141). **MMP-T141** is a sound alternative for those who give more weight to counting party votes as cast. Enlargement alone (MMP141) is the weakest of the three changes. Retaining MMP is defensible only on the expectation that split-list strategies will not escalate.

---

## 1. The starting intuition: every vote should count equally

### One voter, one share

A proportional system rests on a simple idea: every voter should have an equal say in what Parliament looks like. Under MMP, each voter has two ticks, but there is only one Parliament to make up, so each voter should get **one equal share** of its party make-up.

Normally the **party vote** fills that share. The party vote decides each party's total seats, *including* its electorate seats. A party's electorate MPs come out of the share its party vote earns, and its list fills the rest. So for most voters:

- the **party vote** decides the make-up of Parliament;
- the **electorate vote** decides who their local MP is, within some party's share.

### Where this breaks

**Overhang.** Overhang seats aren't covered by any party votes, but someone's ballot elected those MPs. Under current law, those same voters' party votes still count in full for another party. Their ballots have shaped Parliament's make-up twice: once for the seat with no party votes behind it, and again for their party's list seats. Parliament grows to fit both, and every other voter's share is diluted.

**Wasted votes.** A voter whose party vote goes to a party below the 5% threshold (and that wins no electorate) gets no share at all. Their party vote is discarded, and their electorate vote, which elected or helped elect someone, doesn't count towards proportionality either.

So today, some voters count more than once, and some count zero times.

### The fix: sometimes the electorate vote has to count

There are only two ways to keep a voter at one share when their electorate MP is an overhang seat: discount their party vote, or grow Parliament so that everyone else counts for a little less. Current law does the second. The reforms do the first, with one important refinement: **the voter's share isn't thrown away, it's filled by their other tick.** Their electorate vote, which already elected an MP of that party, counts for that party.

| Your ballot | Current MMP | MMP-T | MMP-BV |
|---|---|---|---|
| Both ticks for the same party | One share, to that party | Same | Same |
| Split; your MP's seat is covered by their party's own votes | One share, by party vote | Same | Same |
| Split; your MP holds an overhang seat | **More than one share**: the MP's seat plus your full party vote | One share: just enough of these ballots count for the MP's party to cover the seat | Same as MMP-T |
| Party vote for a party below the threshold; electorate vote for a qualifying party's candidate | **No share** | One share *only if* your MP's party overhangs and needs it; otherwise none | **One share**, to your electorate candidate's party, at every election |
| Both ticks for parties that don't qualify | No share | No share | No share |

Nobody has a choice taken away. The question is only *which* of a voter's two choices fills their one share. And anyone who wants to be sure their share goes to a particular party can give that party both ticks: a straight ballot is never counted differently.

### Why this matters at the level of blocs

Governments in New Zealand are formed by groups of parties. Strategic splitting happens *inside* those groups: an ACT voter ticks the National candidate; a Labour voter ticks the Te Pāti Māori candidate. When a reform counts some of those ballots for the electorate MP's party, the votes move from one partner to another. **The group's total doesn't change.** So once every voter counts once, each group's seats track its combined vote. Equal votes for voters and fair shares for blocs turn out to be the same goal.

---

## 2. The problem in numbers

**Overhang has been small, until now.** From 2005 to 2023, overhangs were 0–2 seats per election, almost all from Māori parties winning Māori electorates (Experiment 2, Part A).

**2023.** Te Pāti Māori won 6 electorates on 3.08% of the party vote, which entitled it to 4 seats. Parliament grew to 122. The left bloc won 44.1% of the counted party vote but 45.1% of Parliament. It needed about 21,600 party votes per seat; the right bloc needed about 22,500.

**2026 (provisional).** Both blocs overhung. National won 42 electorates on an entitlement of 35; Te Pāti Māori won 5 on about 0.6% of the party vote, an entitlement of 1. Parliament grew to **131**. Because both blocs gained, the effects largely cancelled between them. The party that lost out was the one in neither: Opportunity won 6.0% of the counted vote but 5.3% of the seats.

**The risk is escalation.** The 2026 pattern is the "split-list" playbook working on both sides: a bloc leader's voters tick its electorate candidates but give their party vote to a partner. Nothing in current law penalises it. Experiment 3 asks what happens if it spreads (Section 7.4).

---

## 3. The options

All options keep 71 electorates (64 general, 7 Māori), a 5% threshold waived for any party winning an electorate, and the Sainte-Laguë formula.

| Option | Seats | How overhang is handled |
|---|---|---|
| **MMP** (status quo) | 121, growing | Overhanging party keeps its extra electorates; the House grows. |
| **MMP141** | 141, growing | As MMP, with 20 more list seats (71 electorates, 70 list). |
| **MMP-T141** | 141 | Overhang Transfer (Section 4), then a fallback for anything left. |
| **MMP-BV141** | 141 | Backup Vote at every election, then the Overhang Transfer, then a fallback (Section 5). |

The experiments use 121 seats as the base so that a 71-electorate Parliament has 50 list seats; New Zealand's actual base is 120. The reforms were also tested at 121 seats (MMP-T and MMP-BV), which is how they would work without enlarging Parliament. That turns out to matter a great deal (Section 6.6).

**The fallback.** A transfer can only move as many votes as there are split ballots behind an overhanging party's winners. If that isn't enough, something else has to happen. Two fallbacks were tested:

- **Absorb** (the Independent Electoral Review's rule): the House stays fixed and other parties receive fewer list seats. This is the default in MMP-T141 and MMP-BV141.
- **Grow** (the "-X" variants, MMP-T-X141 and MMP-BV-X141): the remaining overhang is handled as under current law, and the House grows.

The choice matters less than the choice of system, but it does matter (Section 6.5).

---

## 4. How MMP-T (the Overhang Transfer) works

MMP-T changes nothing unless a party overhangs. When one does, it counts only as many split ballots as needed towards the overhanging party, starting with votes that would otherwise be wasted.

**Step 1: Apply the threshold.** Decide which parties qualify, using raw party votes. This happens before anything is moved, so no party can be pushed below the threshold by a transfer.

**Step 2: Check for an overhang.** Allocate seats by Sainte-Laguë. If no party has won more electorates than its entitlement, the result stands. At most elections under a reformed system, this is where the count ends.

**Step 3: Use wasted votes first.** Take ballots where the electorate vote went to a *winning* candidate of the overhanging party and the party vote went to a party that didn't qualify. Count those party votes for the overhanging party, only as many as needed.

**Step 4: Transfer the same fraction of other split ballots.** If an overhang remains, take ballots where the electorate vote went to a winning candidate of the overhanging party and the party vote went to *another qualifying party*. The same fraction *f* of every such party vote is counted for the overhanging party, with *f* set just high enough to cover the overhang. No ballots are chosen at random, so a recount gives the same answer, and each party loses votes in proportion to how many of its voters split this way.

**Step 5: Fallback.** If even *f* = 1 isn't enough, absorb the remainder (MMP-T141) or let the House grow (MMP-T-X141).

**Step 6: Allocate seats** with the adjusted votes. The overhanging party's entitlement now matches its electorates, and every other party's seats are proportional to its counted votes.

### A real example: 2023

Te Pāti Māori's two-seat overhang was covered by 35,038 votes: all 3,010 wasted party votes on ballots for its winning candidates, and then 84% of every other split party vote behind them (*f* = 0.842). The 84% is high because the overhang was concentrated in six electorates; in Waiariki, 59% of Labour party voters ticked Rawiri Waititi.

| | Current law | MMP-T |
|---|---|---|
| Parliament | 122 | 120 |
| Te Pāti Māori | 6 | 6 |
| Labour / Green | 34 / 15 | 33 / 14 |
| Left bloc share of seats (vote share 44.1%) | 45.1% | **44.2%** |
| Party votes per seat: left / right | 21,569 / 22,476 | **22,383 / 22,476** |

Te Pāti Māori keeps every electorate MP. The cost of its overhang falls on the parties whose voters created it, Labour and the Greens, and the left bloc's seat share returns almost exactly to its vote share.

### Properties of MMP-T

- **Targeted.** It does nothing in an election with no overhang.
- **Keeps every electorate MP.** Unlike Germany's 2023 rule, no electorate winner is denied their seat. In New Zealand, where most overhangs have come from the Māori electorates, that matters.
- **Fixed size.** With the absorbing fallback, Parliament never grows.
- **Works on parties, not blocs.** Nobody has to define which parties are allies. Bloc fairness falls out of the rule, because splitting happens within blocs.
- **Splitters who cross blocs are counted the same way.** A Labour voter who ticks a popular local National MP whose seat is an overhang is treated like an ACT voter who does. Their vote moves to the National bloc. That is arguably fair, since they chose a National MP, but it means the bloc correction is close rather than exact.
- **Does nothing for wasted votes** unless they sit on ballots behind an overhanging party.

---

## 5. How MMP-BV (the Backup Vote) works

MMP-BV adds one rule to MMP-T, applied at every election whether or not there is an overhang.

**Step 1: Apply the threshold** on raw party votes, as before.

**Step 2: The backup vote.** Every party vote for a party that didn't qualify is counted for the party of the voter's electorate candidate, *if that party qualifies*. If the electorate vote also went to a non-qualifying party, or to an independent, the ballot still counts for nothing.

**Step 3 onwards:** If a party still overhangs, apply MMP-T's split-ballot transfer (its Step 4), then the fallback.

In effect, the electorate vote doubles as a **second preference** for the party vote. It is close to the "spare vote" the Independent Electoral Review discussed in 2023, but it needs no change to the ballot paper.

### Example

Suppose a small party wins 3% of the party vote, below the threshold. Under current law, all those votes are discarded. Under MMP-BV, a supporter who gave their electorate vote to a Labour candidate counts for Labour, and one who ticked a National candidate counts for National. A supporter who ticked their own party's candidate still counts for nothing, because that candidate's party didn't qualify.

### Properties of MMP-BV

Everything listed for MMP-T applies, plus:

- **Fewer wasted votes at every election.** In the calibrated elections (Experiment 2), only a median 1.3% of voters wasted both ticks. Under current MMP, every sub-threshold party vote is wasted.
- **Reduces the threshold's bias between blocs.** When one bloc's minor party falls just short (NZ First in 2008, the Conservatives in 2011 and 2014), that bloc loses all those votes. Most such voters give their electorate vote to an ally, so MMP-BV returns most of them to their own bloc.
- **Removes the "wasted vote" fear for small parties.** Supporters of a small party can party-vote it sincerely without risking their share, provided they tick a qualifying candidate. Small parties gain a little as a result (Experiment 3).
- **A permanent, deliberate departure from party-vote shares.** Backup votes add seats to parties beyond their raw party-vote share at every election. No size of Parliament undoes that (Section 7.2).
- **A mild new incentive to split.** A small-party supporter who ticks their own party's candidate wastes both votes; one who ticks a big ally's candidate keeps their share. So MMP-BV rewards a particular kind of strategic electorate vote: by small-party supporters, for a qualifying ally. It accounts for most of the rare cases where MMP-BV141 does worse than current MMP on bloc fairness (Section 7.1). It is small in seats, but it runs against the general aim of reducing strategic electorate voting.

---

## 6. The properties that matter, and why

### 6.1 Slightly less proportional by party vote, by design

The **Gallagher index** is computed here against party votes *as cast*. Both reforms score worse on it than MMP141 on fixed ballots, for a simple reason: they count some votes for a party other than the one ticked, and the index measures the gap from the ticks.

That isn't the same as a loss of fairness. The yardstick itself counts every split ballot's party vote in full, including the ballots that already elected an overhang MP. Measured against "one share per voter", the reforms are *more* proportional, not less. Still, the cost is real in one sense: some voters' party choice does not determine where their share goes, and some parties (usually the partners of an overhanging party) receive fewer seats than their raw party vote would earn.

**How big is the cost?**

| Gallagher index, median | MMP | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|
| Experiment 1: wide synthetic range, fixed ballots | 4.4 | **2.6** | 3.5 | 5.2 |
| Experiment 2: calibrated to NZ, fixed ballots | 1.4 | **0.9** | **0.9** | 1.7 |
| Experiment 3: from 2026, voters adapt (all elections 2029–41) | 4.1 | 3.2 | **1.5** | 1.8 |
| Experiment 3: 2041 only | 4.1 | 3.4 | **0.45** | 1.3 |

Two patterns stand out:

- **On fixed ballots, MMP-T141 costs little and MMP-BV141 costs more.** MMP-T141 matches MMP141 on realistic elections (0.9 each). MMP-BV141 is a little worse, because its backup votes move seats at every election.
- **Once voters adapt, the reforms become the *most* party-proportional options.** Under current MMP, overhang is the main source of disproportionality (it accounts for almost all of MMP's Gallagher index of 4.1 in Experiment 3; pure proportional allocation on the same ballots scores 0.4). The reforms remove the reward for splitting, splitting falls, overhang shrinks, and with it the need to transfer anything. The share of elections with any overhang under MMP-T141 falls from 96% in 2029 to 41% in 2041, and its Gallagher index falls from 2.9 to 0.45. Under MMP141, overhang persists in 98% of elections and the index *rises*, from 3.1 to 3.4.

So "a bit less proportional by party vote" is true of the reforms on today's voting behaviour, and in the first election or two after a change. It is not true of where they lead.

### 6.2 More proportional at the bloc level

The **bloc seat deficit** measures how many seats the worse-off bloc is short of its share of all party votes. Each bloc is credited with every vote for its parties, including those below the threshold, and centrists count with their ally.

The reforms do better on this measure for two reasons:

1. **Transfers mostly stay inside blocs.** Strategic splitting is a within-bloc activity, so counting split ballots for the overhanging party moves votes between partners without changing the bloc's total. The bloc that overhangs no longer gets seats on top of its share.
2. **The Backup Vote rescues votes the threshold wastes, and mostly returns them to their own bloc.** Sub-threshold voters overwhelmingly tick candidates from their own side.

| Bloc seat deficit: median / 90th percentile | MMP | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|
| Experiment 1: wide synthetic range | 6.2 / 14.5 | 5.2 / 13.5 | 3.7 / 9.7 | **1.5 / 5.1** |
| Experiment 2: calibrated to NZ | 2.1 / 5.1 | 2.2 / 5.5 | 1.8 / 5.1 | **1.1 / 2.8** |
| Experiment 3: from 2026, voters adapt | 2.2 / 5.5 | 2.0 / 5.3 | 1.6 / 4.3 | **1.4 / 3.8** |

MMP-BV141 is best in every experiment. MMP-T141 is consistently better than MMP141. MMP141, on realistic elections, is no better than MMP at all (2.2 against 2.1 in Experiment 2): more list seats reduce overhang but do nothing about where the remaining overhang's seats go, or about wasted votes.

**A caution on the yardstick.** The bloc yardstick counts sub-threshold votes, which only MMP-BV can use, so it favours MMP-BV by construction. The experiments also report a "countable" bloc yardstick that leaves out voters who wasted both ticks, since no rule can count them. MMP-BV141's lead is even larger on that measure: a median of 0.6 seats in both Experiments 1 and 2, against 2.7 and 1.4 for MMP-T141, 4.2 and 1.8 for MMP141, and 5.3 and 1.7 for MMP. Its blocs are within one seat in 74–75% of scenarios, against 10–37% for the others.

### 6.3 Less likely to hand the minority bloc a majority

The outcome that matters most is whether the bloc with fewer votes ends up with a majority of seats. Experiment 3 is the only experiment that measured this directly.

| | MMP | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|
| Minority-bloc majority, all elections 2029–41 | 5.6% | 4.3% | 4.6% | 4.0% | 4.6% | **3.6%** |
| In close elections (blocs 48–52%) | 27% | 23% | 26% | 23% | 25% | **20%** |
| Futures with at least one, over five elections | 23% | 19% | 21% | 18% | 20% | **16%** |
| As above, if gaming escalates | **37%** | **31%** | 21% | 18% | 20% | 16% |

- **MMP-BV141 is less likely than any other option to produce a wrong-winner Parliament**, especially with the grow fallback.
- **MMP-T141 is about level with MMP141 in the baseline** (4.6% against 4.3%), and better than MMP. Its advantage shows when gaming escalates, when MMP141 deteriorates and MMP-T141 doesn't.
- **There is a floor.** Allocating seats by pure proportional representation on the same ballots, with no electorates and so no overhang, still gives the minority bloc a majority in 4.6–4.8% of elections at a 5% threshold. MMP-BV-X141 beats that floor, because the Backup Vote rescues votes the threshold would otherwise waste. Lowering the threshold to 3.5% would bring the floor down to 2.7–2.9%.

### 6.4 Resistance to gaming

This is the reforms' strongest property.

**The split-list playbook gains nothing.** If a bloc leader's voters tick its candidates but party-vote a partner, the leader overhangs. Under a transfer rule, the split ballots behind that overhang are counted back towards the leader, and the bloc ends up with about its combined vote: exactly what it would have had without splitting. The same applies to "decoy" parties that stand only electorate candidates.

**What happens if the playbook spreads** (Experiment 3's escalation scenario):

| If gaming escalates | MMP | MMP141 | Any reform |
|---|---|---|---|
| Median overhang in 2041 | 30 seats (11 in the baseline) | not reported | unchanged from baseline |
| Largest House | 180 (155 in the baseline) | 197 (171 in the baseline) | unchanged: 141, or at most 152 with -X |
| Gallagher index in 2041 | 9.7 (4.1 in the baseline) | not reported | unchanged |
| Bloc seat deficit, median, 2029–41 | 3.9 (2.2) | 3.0 (2.0) | unchanged |
| Minority-bloc majority, 2029–41 | 9.4% (5.6%) | 7.7% (4.3%) | unchanged: 3.6–4.6% at 141 |

Under MMP, escalation is self-reinforcing: each bloc that sees the other gain more seats than votes has a reason to copy it. Under the reforms there is nothing to copy. **A larger Parliament without a reform is no protection**: MMP141's House reaches 197.

**Other safeguards built into the rules:**
- The threshold is applied before any transfer, so a transfer can't push a party out of Parliament, and nobody can be pushed *in* by one either.
- There is no exemption for voters whose party stood no candidate locally. Such an exemption would be gamed by allied parties withdrawing candidates.
- Transfers use a fixed fraction of every eligible ballot, not a random selection, so results are reproducible on a recount.

**New incentives the reforms create:**
- **Partners compete for electorates.** Under either reform, a small party whose voters hand electorates to a big ally loses party votes when that ally overhangs. Experiment 3's reasoning has ACT and NZ First running "two ticks" campaigns after their first visible losses. That is a healthy incentive: it is the behaviour MMP was designed around.
- **Te Pāti Māori rebuilds its party vote.** Under the absorbing reforms, a Māori-seat overhang gains the left nothing, so TPM switches to asking for the party vote and rebuilds to about 5.7% by 2041 (from 0.5% under MMP).
- **Consolidation to deny the other side's plurality wins.** Under the absorbing reforms, once deliberate splitting has stopped, any remaining overhang comes from a big party winning electorates on a plurality, and it costs the *other* bloc list seats. Partner voters in marginal seats begin backing their own side's strongest candidate. This is ordinary electorate competition, not double-counting.
- **The Backup Vote's small reward for strategic electorate votes** by small-party supporters (Section 5).
- **Under the grow fallback, a small residual reward remains.** Overhang that transfers can't cover still adds seats for its bloc, so TPM's Māori-seat strategy partly survives (party vote stays about 0.5–0.6%). The reward is much smaller than under MMP, because transfers cover most of the overhang first.

### 6.5 The fallback: absorb or grow

| At 141 seats, Experiment 3 | MMP-T141 (absorb) | MMP-T-X141 (grow) | MMP-BV141 (absorb) | MMP-BV-X141 (grow) |
|---|---|---|---|---|
| Bloc seat deficit, median | 1.6 | 1.7 | 1.4 | 1.4 |
| Minority-bloc majority | 4.6% | 4.6% | 4.0% | **3.6%** |
| House: median / max | 141 | 141 / 150 | 141 | 141 / 152 |
| Gallagher | 1.5 | **0.7** | 1.8 | 1.4 |
| TPM party vote in 2041 | 5.6% | 0.5% | 5.7% | 0.6% |

**Absorbing** keeps Parliament fixed and gives the strongest incentives, but when the leftover overhang comes from plurality wins, it charges the *other* bloc for it. **Growing** avoids that, at the cost of a slightly variable House and a weaker incentive for parties built on electorates. At 141 seats, overhang is rare enough that either works. The grow fallback gives slightly better outcomes on every measure except the incentive on electorate-based parties.

At 121 seats the difference is large (next section).

### 6.6 Why the reforms need more list seats

There are two kinds of overhang:

- **Overhang from splitting:** voters tick one party's candidate and party-vote another. Transfers fix this, because the split ballots are there to transfer.
- **Overhang from plurality wins:** a large party wins many electorates on well under half the vote in each, against a divided opposition. There may be few split ballots behind those wins, so there is little to transfer.

The reforms are designed to make the first kind disappear. Once it does, the second kind is what's left, and it depends on the ratio of list seats to electorates. With 71 electorates and 50 list seats, a party winning 42 electorates needs about 35% of the qualifying vote to cover them. With 70 list seats, it needs about 30%. In 2026, National's 42 electorates on 29.5% of the counted vote gave it a seven-seat overhang at 120; at 141 seats the same vote share is worth about 41–42 seats.

That is why the reforms at 121 seats disappoint:

- In Experiment 1, with low strategic voting, MMP-T at 121 did slightly *worse* than current MMP on bloc fairness (median 6.5 against 5.3), and MMP-BV barely better (5.1).
- In Experiment 3, once voters adapted, MMP-T and MMP-BV at 121 gave the minority bloc a majority in 7.8% and 7.4% of elections, against 5.6% under MMP. Over 2029–2041, one future in three had at least one such Parliament.

The reforms succeed at removing the incentive, and that very success leaves behind the kind of overhang they can't cover. More list seats close that gap. With the grow fallback (MMP-T-X, MMP-BV-X), the reforms at 121 come back to MMP's level (5.2–5.7%) with a House that grows by about 2 seats typically. But only at 141 do they clearly beat MMP.

Adding 20 list seats is one way to get the ratio. Reducing the number of electorates is another; it wasn't tested here.

### 6.7 What no overhang rule fixes

Under every option, some bloc imbalance remains, and it drifts upward over 2029–2041 (from 1.0 to 1.7 seats under MMP-BV-X141; from 2.2 to 2.6 under MMP). Under MMP-BV-X141, the remaining imbalance is correlated with the share of wasted votes (0.48), not with overhang (0.04).

Of MMP's median bloc seat deficit of 2.2 seats in Experiment 3, only about 0.8 comes from overhang. The other 1.4 is caused by the 5% threshold. MMP-BV-X141 removes all of the overhang-caused part and a little of the threshold-caused part. Lowering the threshold to 3.5%, the Independent Electoral Review's recommendation, would roughly halve what remains (to 0.7–0.8 seats). That is complementary to any overhang reform, not an alternative.

---

## 7. The simulations: method and results

### 7.1 Common framework

All three experiments use the same seat-allocation engine (`mc_overhang.py`) and the same measures.

**Ballots, not just totals.** Each electorate's votes are held as a table of party vote × electorate candidate, so every rule can see exactly which ballots elected which MP and where their party votes went. That is what the transfer rules need.

**Seat rules.** Sainte-Laguë; 5% threshold, waived for any party winning an electorate; qualification decided on raw party votes before anything is moved.

**Measures.**

| Measure | What it captures |
|---|---|
| **Bloc seat deficit** | Seats the worse-off bloc is short of its share of all party votes, sub-threshold votes included. Every party is assigned to a bloc; centrists count with their ally. |
| **Gallagher index** | Conventional party-level disproportionality against qualifying party votes as cast. |
| **Party seat deficit** | Each party's shortfall against its party-vote share, rounded to whole seats and summed. |
| **Minority-bloc majority** | The bloc with fewer party votes holds a majority of seats (Experiment 3). |
| **Extra seats needed** | How many list seats would have to be added before (a) no party or (b) no bloc is more than one seat short. A diagnostic, not a proposal. |
| **Overhang** | Electorates won beyond entitlement on raw party votes at the system's base size. |

### 7.2 Experiment 1: a stress test

**Design.** 5,000 synthetic elections, deliberately spanning far more fragmented party systems than New Zealand has had: 2–5 parties per bloc, blocs from 30:70 to 70:30, strategic splitting anywhere from 0% to 100% per bloc, 0–2 Māori electorate parties, 0–2 centrists, random geography. The same ballots are counted under every system. Median overhang was 13 seats, far beyond New Zealand's history: the point was to see where each rule breaks, not to forecast.

**What it showed.**
- **The party–bloc trade-off is real.** MMP-BV141 had the best bloc fairness (median deficit 1.5, against 5.2 for MMP141) and the worst party-level proportionality (Gallagher 5.2, against 2.6). MMP-T141 sat between them on both, closer to MMP141 on party proportionality (median party seat deficit 6 against 5).
- **Size does much of the work.** 141 seats improved every rule.
- **The reforms do best when strategic splitting is high**, and least when it is low, because low splitting leaves little to transfer. In the scenarios with the least splitting, MMP-T at 121 was slightly worse than MMP. That is the first sign of the problem in Section 6.6.
- **Reforms rarely do worse than the status quo.** MMP-BV141 was more than one seat worse than MMP141 on bloc fairness in 3% of scenarios. Where it was at least a seat worse than both MMP and MMP141 (1.7% of scenarios), the main causes were uneven numbers of fully wasted ballots between blocs, and the Backup Vote's reward for small-party supporters who tick a big ally. Leaving out voters who wasted both ticks, MMP-BV141 was at least a seat worse than MMP141 in only 0.7% of scenarios.
- **No Parliament size fixes MMP's bloc unfairness in the hard cases.** In 45% of scenarios, no MMP House up to 400 seats brought both blocs within one seat. MMP-BV always got there, needing no extra seats at all in 52% of scenarios.

### 7.3 Experiment 2: New Zealand's actual elections, and elections like them

**Part A: rerunning 2005–2023.** Using the Electoral Commission's split-vote tables (495 electorate tables over seven elections), each election was recounted under every system at 120 seats. Current MMP reproduced every real Parliament.

| Year | Overhang | Bloc seat deficit: MMP / MMP-T / MMP-BV | Votes transferred (MMP-T) |
|---|---|---|---|
| 2005 | Māori Party 1 | 0.1 / 0.5 / 0.5 | 16,978 |
| 2008 | Māori Party 2 | 4.4 / 4.5 / **3.5** | 26,596 |
| 2011 | Māori Party 1 | 0.2 / 0.7 / 0.3 | 13,154 |
| 2014 | United Future 1 | 0.4 / 0.9 / **0.1** | 4,195 |
| 2017 | none | 1.8 / 1.8 / **0.8** | – |
| 2020 | none | **0.2** / **0.2** / 1.2 | – |
| 2023 | Te Pāti Māori 2 | 1.5 / **0.4** / **0.4** | 35,038 |

- Every historical overhang was covered by transferring at most about 37,000 votes (1.3% of the party vote). Parliament would have stayed at 120 every time.
- The largest bloc imbalance, in 2008, came from NZ First falling below the threshold, not from overhang. Only MMP-BV reduced it.
- MMP-BV did worse in one election, 2020, by one seat: the votes it rescued did not split between the blocs in proportion to the blocs' sub-threshold votes. MMP-T matched MMP in years without overhang, as it must.
- Party-level effects were small: one or two seats per party at most.

**Part B: 5,000 calibrated elections.** The Experiment 1 generator, with every parameter drawn from what the seven elections show. Party structure, geography and turnout were measured directly. Voter behaviour (personal votes, strategic splitting by each partner party, Māori-seat splitting, standout local candidates like Epsom's) was fitted to each election's electorate results by approximate Bayesian computation. The fitted behaviour reproduces the partner parties' observed splits within 5–6 points every year. The calibrated elections have a median overhang of 2 seats (99th percentile 10), 83% of it from Māori parties.

| Calibrated elections | MMP | MMP141 | MMP-T141 | MMP-BV141 | MMP-BV-X141 |
|---|---|---|---|---|---|
| Bloc seat deficit: median / 90th | 2.1 / 5.1 | 2.2 / 5.5 | 1.8 / 5.1 | **1.1 / 2.8** | **1.0 / 2.9** |
| Blocs within one seat | 25% | 24% | 29% | **48%** | **48%** |
| Gallagher | 1.4 | **0.9** | **0.9** | 1.7 | 1.7 |
| House: median / max | 123 / 139 | 142 / 151 | 141 | 141 | 141 / 145 |

- **Most bloc imbalance in realistic elections comes from wasted votes, not overhang.** With no overhang at all, MMP's median bloc deficit was still 1.7 seats; MMP-BV's was 0.9.
- **MMP-BV almost never does worse than MMP on bloc fairness**: more than one seat worse in 1% of scenarios, and never more than two.
- **MMP-BV's party-level cost is permanent.** In 42% of scenarios no Parliament size brings every party within one seat of its raw party-vote share, against 5% under MMP. That is the measurable form of "counting some votes for a different party".

### 7.4 Experiment 3: where each system leads from 2026

**Design.** Experiments 1 and 2 hold ballots fixed. Experiment 3 lets voters and parties respond. Starting from the 2026 provisional result, 1,000 futures were simulated over five elections (2029–2041) under ten systems, with each reform taking effect in 2029.

- **Events outside strategy** (bloc swings, party drift, new parties, map drift) are shared across systems within each future.
- **Strategic responses** depend on what each group learned from the last election under its own system. They were first reasoned through by hand, then encoded as rules and run at scale. Both stages are described below.
- **Two escalation scenarios** add the split-list playbook spreading under MMP: by reaction to the other side ("copycat"), or also because it pays ("escalation").
- **A benchmark** reallocates every simulated election by pure proportional representation, to show how much imbalance no overhang rule can remove.

#### What the reasoning acts on

Each future carries a small set of behavioural state variables, which the election simulator turns into ballots in every electorate:

| Variable | Meaning | 2026 value |
|---|---|---|
| *s*<sub>p</sub> | Share of partner party *p*'s voters who give their electorate vote to their bloc leader's candidate | 0.15 (left partners), 0.35 (right partners) |
| *s*<sub>M</sub> | Share of left voters in the Māori electorates who tick the Māori-party candidate | 0.40 |
| π | Personal vote: share of all voters who back a liked local candidate regardless of party | 0.20 |
| Party vote shares | National party votes, with each party's local strength from the 2026 electoral map | 2026 result |
| Split-list share | Share of a bloc leader's supporters who keep ticking its candidates but party-vote a partner | 0 |
| Awareness *a* | How well voters understand the reform in force (0–1); scales most responses under a reform | 0.2 before 2029 |

The reasoning changes these variables between elections. It never touches the seat rules or the ballots directly.

#### Stage 1: ten futures reasoned by hand

Ten futures were started from 2026, each with its own exogenous events (swings, drift, new parties), and run under all ten systems. After each election:

1. **A digest was produced** for every future × system: party votes, electorates won, overhang, votes transferred, which parties lost seats relative to their raw party vote, each bloc's seats against its fair share, and who won the majority (`futures/digest_<year>.md`).
2. **The digests were read and the reasoning written down** (`futures/reasoning_<year>.md`). For each system, the reasoning sets out what the election showed and then takes each group in turn (partner parties and their voters, leader parties' voters, Te Pāti Māori, voters in the Māori electorates, sub-threshold parties' voters) and asks what that group, in its own position and with partial attention, would do differently next time.
3. **The reasoning was translated into rules** that change the state variables, with explicit triggers read from the last result (for example, "this party lost seats to transfers" or "the other bloc's leader overhung by four or more").
4. **The next election was simulated** with the adjusted behaviour, and the cycle repeated through 2041.

The first version of the rules named parties. Because party systems drift (in about 22% of simulated elections the left or right leader, or TPM's size, ends up somewhere the hand-reasoned futures never went), the rules were rewritten by role (left leader, right partners, and so on) and the ten futures rerun. Two rules remain tied to particular parties because the reasoning is about them specifically: the fast "two ticks" response of ACT and NZ First, whose voters are unusually engaged, and Te Pāti Māori's party-vote strategy, which is specific to the Māori electorates.

#### An example: the reasoning before 2032

**What 2029 showed.** Under MMP, every future had an overhang of 11–17 seats, from the same two sources as 2026: National winning far more electorates than its party vote covers (ACT and NZ First voters ticking National candidates), and TPM winning 5–7 Māori electorates on well under 1% of the party vote. Under the reforms, in their first election, voters had barely adapted (*a* = 0.2), so the same overhangs had to be transferred: 55,000–220,000 party votes. ACT and NZ First each lost 2–5 seats where National overhung; Labour and the Greens lost 2–4 each, mostly through the transfer to TPM. TPM's overhang could not be fully covered, so under absorption the left paid for TPM's seats in list seats.

**How each group responds**, as written in the reasoning:

| Group | Reasoning | Rule |
|---|---|---|
| *Under MMP:* ACT and NZ First voters | Splitting worked and nothing penalised it, so they keep ticking National candidates, a little more each time National overhangs. | General rule: *s*<sub>p</sub> + 0.03 for each partner whenever its leader overhangs. |
| *Under MMP:* Green voters | Where the right won more seats than votes and the majority, left strategists run "tick Labour in marginals" campaigns. Many Greens still tick Green. | If the right won the majority with ≥1.5 seats above its fair share: left partners' *s*<sub>p</sub> × 1.4. |
| *Under MMP:* National voters | Where the left won on an overhang, National copies the split-list playbook more openly: about a point of its vote goes to a partner's list while those voters keep ticking National. | Mirror trigger: shift 1 point from the right leader to its largest partner, with those voters' electorate votes staying with the leader. |
| *Under a reform:* ACT and NZ First | They lost seats because their voters ticked National candidates. Both run "two ticks" campaigns. Their voters are engaged, so the response is fast. | *s*<sub>p</sub> × 0.55 if the party lost 3+ seats, × 0.70 otherwise, on top of the general learning rule. |
| *Under a reform:* Green and Opportunity voters | They respond more slowly: their splits are more often personal (a liked local MP) than tactical. | *s*<sub>p</sub> × 0.75. |
| *Under an absorbing reform:* Te Pāti Māori | Its electorates no longer bring the left extra seats, and the left now pays for them. TPM switches to asking for the party vote. That is party-led, so faster than ordinary voter learning. | If TPM overhung: move half the gap between its vote and about 3% from Labour and the Greens to TPM; *s*<sub>M</sub> → 0.32. |
| *Under a grow (-X) reform:* Te Pāti Māori | Whatever the transfer can't cover still adds seats for the left, so the strategy still pays and TPM does *not* change course. The Greens, whose voters' party votes are being transferred to TPM, push for two ticks in Māori seats. | No party-vote shift; *s*<sub>M</sub> − 0.02. |
| *Under MMP-BV:* sub-threshold parties' voters | After one visible election the backup vote is starting to be understood (*a* = 0.5). They fear wasting their vote less, and pick a qualifying candidate for their electorate vote. | Small parties gain a little vote share from their leader; sub-threshold parties' *s*<sub>p</sub> rises with *a*. |

**What it produced.** In one hand-reasoned future (run 0), by 2032 TPM's party vote had reached 4.7% under MMP-BV, against 1.6% under MMP-BV-X, and its overhang had fallen to 1 seat, against 4. The divergence between the absorbing and grow fallbacks on TPM's strategy, reported in Section 6.5, comes from this piece of reasoning.

#### A second example: the reasoning that found the failure mode

The digests after 2035 showed something not anticipated when the reforms were designed. Under MMP-T and MMP-BV at 121 seats, ACT and NZ First voters now rarely split (split rates of 0.06–0.2) and TPM's overhang had largely gone, yet National still overhung by 3–15 seats in right-leaning futures. That overhang came almost entirely from plurality wins against a divided left. With few split ballots behind it, it was absorbed, and the median bloc seat deficit under the reforms (3.4–4.0) was now *worse* than under MMP (2.8).

The reasoning before 2038 then asked how left voters would respond. Under a transfer rule, splitting *to* another party's winning candidate costs your own party. But backing *your own side's* strongest candidate where the other bloc's leader would otherwise win costs nothing, and shrinks the overhang that is costing your side list seats. So engaged partner voters in marginal seats begin to consolidate. The rule: where the other side's leader overhung by 4 or more, own-bloc partners' split rate becomes min(0.35, 2*s*<sub>p</sub> + 0.05), with a mirror rule for the right. By 2041 this had cut National's plurality overhang sharply in some futures (from 11 seats to 1 in one, 10 to 0 in another) but not where the left was most fragmented (9–15 seats remained). This is the evidence behind Section 6.6.

#### Stage 2: encoding for 1,000 walks

The rules fall into two groups.

- **General rules** (`mc_future.respond`) apply after every election under every system. They cover learning under MMP (partners split more each time their leader overhangs and keeps the seats; TPM's Māori-seat strategy strengthens while it pays), learning under the reforms (each partner's split rate falls by a share of itself, larger if the party lost seats to transfers, scaled by awareness *a*), awareness itself (rising faster after an election with visible transfers), the threshold squeeze on parties polling under 5% (weakened under MMP-BV in proportion to *a*), and the Backup Vote's effects on small parties.
- **Election-specific rules** (`futures_reason.py`) encode the conditional reasoning for 2032, 2035, 2038 and 2041, such as the two-tick campaigns, TPM's targets and recovery rates, the reduction in personal splitting from 2035 wherever left parties lost two or more seats to transfers at the last election, and consolidation from 2038. Each rule reads the triggering conditions from that future's own last result under that system, so the same rule fires in some futures and systems and not others.

**Drawing rule strengths.** Every numerical strength in the reasoning (32 in all) is a parameter. Each of the 1,000 walks draws its own value for each one, independently and uniformly from a range that brackets the hand-reasoned value. Some examples:

| Rule | Hand-reasoned value | Range drawn |
|---|---|---|
| Awareness before the first reformed election | 0.20 | 0.10–0.30 |
| Awareness gain after an election with visible / no transfers | 0.30 / 0.15 | 0.15–0.45 / 0.05–0.25 |
| General cut in a partner's split rate, if it lost seats / otherwise (× *a*) | 0.45 / 0.15 | 0.25–0.65 / 0.05–0.25 |
| MMP: partners' extra splitting per overhang | +0.03 | 0.01–0.05 |
| MMP: left "tick the leader" push (2032) | × 1.4 | 1.15–1.65 |
| Reform: ACT / NZ First two-tick campaign (large / small loss) | × 0.55 / × 0.70 | 0.40–0.75 / 0.55–0.85 |
| Reform: other partners' two-tick campaign | × 0.75 | 0.60–0.90 |
| Reform: TPM party-vote target (2032 / later) | 3% / 4% | 2.5–3.5% / 3–5% |
| Reform: TPM recovery, share of gap closed | 0.5 | 0.25–0.75 |
| Reform: cut in left personal splitting (2035) | × 0.85 | 0.75–0.95 |
| Reform: consolidation (multiplier / addition / cap) | × 2 / + 0.05 / 0.35 | 1.3–2.7 / 0–0.10 / 0.20–0.50 |
| Threshold squeeze on sub-5% parties | 15% of share | 8–22% |

The full list is in `mc_future_walks.py`.

**Each walk then runs as follows.**
1. The fixed 2026 result is simulated under MMP.
2. For each of the ten systems, and for each election from 2029 to 2041:
   1. the general rules respond to that system's last result;
   2. exogenous events are applied, drawn from a random seed that depends only on the walk and the year, so every system in a walk faces the same swings, drift and new parties;
   3. in the escalation scenarios only, the split-list adoption rule is applied (never under a reform, where it gains nothing);
   4. the election-specific rules for that year respond to the last result;
   5. the election is simulated under that system's seat rule.

Because every response is conditioned on that system's own previous result, the ten systems within a walk start from the same place and face the same events, but their voters' behaviour diverges as each learns from a different history.

**Checks.** Rerunning the ten hand-reasoned futures with the role-based, encoded rules gives results consistent with the 1,000 walks. Across the walks, the correlation between any drawn rule strength and a future's average bloc seat deficit is at most 0.12 in absolute value, so the ranking of systems does not hinge on the particular values chosen in the hand reasoning.

**What this approach can and can't establish.** The rules make the behavioural assumptions explicit and auditable, and the drawn ranges test sensitivity to their strength. They don't test their form: every walk assumes the same *kinds* of response (partners campaign for two ticks; TPM rebuilds its party vote; voters consolidate), triggered at the same thresholds, with strengths drawn independently of one another. Responses the hand reasoning never considered are absent. The reasoning was also written by the same analyst who proposed the reforms, although it was this reasoning that uncovered the reforms' main failure mode at 121 seats.

**Results across the four options** (all elections 2029–2041):

| | MMP | MMP141 | MMP-T141 | MMP-BV141 | MMP-BV-X141 |
|---|---|---|---|---|---|
| Overhang: median / 90th | 11 / 20 | 6 / 15 | 3 / 9 | 3 / 10 | 2 / 9 |
| House: median / max | 132 / 155 | 147 / 171 | 141 | 141 | 141 / 152 |
| Bloc seat deficit: median / 90th | 2.2 / 5.5 | 2.0 / 5.3 | 1.6 / 4.3 | 1.4 / 3.8 | **1.4 / 3.7** |
| Blocs within one seat | 24% | 27% | 34% | **39%** | 38% |
| Gallagher | 4.1 | 3.2 | **1.5** | 1.8 | 1.4 |
| Minority-bloc majority | 5.6% | 4.3% | 4.6% | 4.0% | **3.6%** |
| …if gaming escalates | 9.4% | 7.7% | 4.6% | 4.0% | **3.6%** |

**What it showed.**
- **Under MMP, overhang becomes entrenched** at about 11 seats per election, with a typical House of 132. Both blocs game and their overhangs partly cancel, so the main harm is a large, unpredictable Parliament and fragile outcomes in close elections, where the minority bloc wins 27% of the time.
- **Under the reforms, behaviour changes.** Partner parties campaign for two ticks; TPM rebuilds its party vote (under absorption); overhang falls election by election. At 141 seats it has largely gone by 2035.
- **The first election is the hardest.** Before voters adapt, transfers are large: a median of about 54,000 votes under MMP-T141 in 2029, and 160,000 in one election in ten. Partner parties lose seats visibly. That shock is what drives the adaptation, but it is also a political cost of the transition.
- **Results are robust to the reasoning assumptions.** The strength drawn for each rule correlates with a future's bloc fairness at most 0.12. The ranking of systems comes from the rules, not the precise assumptions about behaviour.

### 7.5 What the three experiments agree on

| Finding | Exp. 1 | Exp. 2 | Exp. 3 |
|---|---|---|---|
| MMP-BV141 has the smallest bloc imbalance | ✓ | ✓ | ✓ |
| MMP-T141 beats MMP and MMP141 on bloc fairness | ✓ | ✓ | ✓ |
| The reforms cost some party-level proportionality on fixed ballots, BV more than T | ✓ | ✓ | — |
| Once voters adapt, the reforms are more party-proportional than MMP or MMP141 | — | — | ✓ |
| At 121 seats, absorbing leftover overhang can make the reforms worse than MMP | ✓ (low splitting) | — (overhangs too small) | ✓ |
| Wasted votes, not overhang, drive most remaining bloc imbalance | ✓ | ✓ | ✓ |
| The reforms rarely do worse than MMP on bloc fairness | ✓ | ✓ | ✓ (at 141) |

---

## 8. Costs and benefits of each option

### Option A: Stay with MMP

**Benefits**
- No change: no legislation, no voter education, no transition shock.
- Party votes are counted exactly as cast.
- Historically, overhang has been small (0–2 seats from 2005 to 2023), and its effects on bloc fairness have been modest.
- When both blocs game, their gains partly cancel (Experiment 3), which limits systematic bias.

**Costs**
- **Unequal votes.** Voters whose split ballots elect overhang MPs count more than once; sub-threshold voters count not at all. In 2023 the left needed 900 fewer votes per seat than the right.
- **Unpredictable size.** 131 seats in 2026; a median of 132 and up to 155 in Experiment 3's baseline.
- **Fragile close elections.** In elections where the blocs are within 48–52%, the minority bloc wins a majority 27% of the time in Experiment 3.
- **Third parties pay quietly.** When both blocs overhang, the cost falls on parties in neither (Opportunity in 2026).
- **Open to escalation.** The incentive to split remains, and nothing limits it. If the split-list playbook spreads because it pays, overhang reaches a median 30 seats by 2041, the House up to 180, and 37% of futures see at least one Parliament where the bloc with fewer votes holds the majority.

**Verdict.** Low cost now, with an uncapped downside. Its case rests on the assumption that the 2026 pattern doesn't spread.

### Option B: MMP141 (20 more list seats, no reform)

**Benefits**
- Halves overhang (median 6 against 11 in Experiment 3) by raising each party's entitlement.
- The best party-level proportionality on fixed ballots (Gallagher 0.9 in Experiment 2).
- Somewhat fewer minority-bloc majorities than MMP in the baseline (4.3% against 5.6%).
- No change to how votes are counted.

**Costs**
- **20 more MPs**, with the cost and public resistance that brings. (In the 1999 citizens-initiated referendum, about 81% voted to reduce Parliament to 99 members.)
- **The House still grows**: median 147, up to 171 in Experiment 3's baseline.
- **Little gain in bloc fairness** on realistic elections (median deficit 2.2 against MMP's 2.1 in Experiment 2).
- **No protection against gaming.** Under escalation the House reaches 197 and minority-bloc majorities rise to 7.7%.
- Does nothing for wasted votes.

**Verdict.** It buys proportionality with seats, but leaves the incentive that causes the problem in place. It pays the main political cost of the reforms (more MPs) without their main benefit.

### Option C: MMP-T141 (Overhang Transfer, 141 seats)

**Benefits**
- **Removes the payoff from strategic splitting.** Immune to the split-list playbook and decoy parties.
- **Fixed size** with the absorbing fallback; at most 150 with the grow fallback.
- **Better bloc fairness** than MMP or MMP141 in every experiment.
- **Best party-level proportionality once voters adapt** (Gallagher 1.5 overall, 0.45 by 2041; 0.7 overall with the grow fallback).
- **Minimal intervention.** Votes are counted exactly as today unless a party overhangs, which becomes less common as voters adapt (96% of elections in 2029, 41% by 2041).
- Keeps every electorate MP; reproducible on recount; the calculation can be done on paper.

**Costs**
- **20 more MPs**, as for MMP141.
- **Some party votes are counted for another party** when there is an overhang. This is the most important objection ("isn't this disregarding my vote?"), and the answer, that each voter still gets one full share, has to be explained.
- **Partner parties lose seats** when their voters hand electorates to an overhanging ally (in the 2026 estimate at 120 seats, ACT would fall from 13 to 9 and NZ First from 12 to 10). They will oppose it, at least until they adapt.
- **A transition shock.** The first election under the rule transfers tens of thousands of votes, and the losses are visible.
- **Does nothing for wasted votes**, so its bloc fairness is limited by the threshold.
- **Wrong-winner risk about level with MMP141** (4.6% against 4.3%) in the baseline, though far better under escalation.

**Verdict.** A targeted, conservative reform that fixes the double-counting problem and its incentives, and ends up the most party-proportional option. It leaves the wasted-vote problem untouched.

### Option D: MMP-BV141 (Backup Vote, 141 seats)

**Benefits**
- **Everything MMP-T141 offers on gaming resistance and fixed size.**
- **The best bloc fairness in every experiment** (median deficit 1.5 / 1.1 / 1.4 across Experiments 1–3).
- **The fewest minority-bloc majorities**: 4.0% (3.6% with the grow fallback), below what pure proportional representation achieves at a 5% threshold.
- **Rescues wasted votes at every election.** It closes part of the gap caused by the threshold, which is the largest remaining source of bloc imbalance.
- **Lets small-party supporters vote sincerely** without wasting their share.
- **Comes closest to the principle of one equal share per voter**: it addresses both voters who count twice and voters who count zero times.

**Costs**
- **20 more MPs.**
- **A bigger change to counting.** Sub-threshold party votes are redirected at every election, not just when there is an overhang. That is more to explain and more to object to.
- **A permanent gap from party-vote shares.** Its Gallagher index is a little higher than MMP-T141's in every experiment, and in 42% of calibrated elections no Parliament size would bring every party within a seat of its raw party-vote share.
- **A small reward for strategic electorate votes** by small-party supporters, who keep their share only if they tick a qualifying candidate.
- **Occasionally worse than MMP** on bloc fairness when rescued votes are unevenly spread between blocs (2020; about 1–3% of simulated elections by more than a seat).
- The same partner-party losses and transition shock as MMP-T141.
- May encourage slightly more voting for small parties, since such votes are no longer wasted.

**Verdict.** The strongest option on fairness between voters and between blocs, and on wrong-winner risk. It asks the most of public understanding.

### Scorecard

| | MMP | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|
| Equal votes (one share per voter) | ✗ | ✗ | Fixes double-counting | Fixes double-counting and most wasted votes |
| Bloc fairness | Worst | Little better | Good | **Best** |
| Minority-bloc majority risk | Highest | Middling | Middling | **Lowest** |
| Party-vote proportionality, today's behaviour | Middling | **Best** | **Best** (ties MMP141) | Middling |
| Party-vote proportionality, adapted behaviour | Worst | Middling | **Best** | Good |
| Resistance to gaming | None | None | **Full** | **Full** |
| Predictable Parliament size | ✗ | ✗ | ✓ | ✓ |
| Simplicity / no change to counting | **✓** | ✓ | Change only when overhang | Change at every election |
| Extra MPs | **0** | 20 | 20 | 20 |
| Transition cost | **None** | Low | Visible partner losses at first | Visible partner losses at first |

---

## 9. Recommendation

1. **If the rules are going to change, change the counting rule, not just the size.** MMP141 pays the political cost of 20 extra MPs without fixing the incentive that drives overhang. Every reform at 141 beats it on bloc fairness and gaming resistance.
2. **Pair either reform with more list seats, or a lower electorate share.** At 121 seats with absorption, the reforms can be worse than MMP once voters adapt. If Parliament can't grow, use the grow fallback (MMP-BV-X or MMP-T-X), which brings wrong-winner risk back to MMP's level with a House that typically grows by about 2 seats.
3. **Prefer MMP-BV141, with the grow fallback (MMP-BV-X141).** It is the only option that gives voters below the threshold a share, has the smallest bloc imbalance, and has the lowest risk of a minority-bloc majority. The grow fallback improves on absorption at 141 seats on every outcome measure, at the cost of a House that occasionally reaches about 150 and a weaker incentive for electorate-based parties.
4. **Choose MMP-T141 if counting party votes as cast is the priority.** It is the smaller change, touches the count only when there's an overhang, and is the most party-proportional option once voters adapt. It does less for bloc fairness.
5. **Lower the threshold as well.** Moving from 5% to 3.5% would do more for bloc fairness than any overhang rule, and the two changes are complementary.

**What would change this recommendation?**
- **Strong evidence that gaming won't spread** weakens the case for any reform, and leaves MMP or MMP141 as cheaper options.
- **A firm cap on Parliament's size** at 120 makes the -X variants at 121 the only reform worth adopting, and narrows their advantage over MMP to gaming resistance and a more predictable House.
- **Weighting party-vote proportionality above bloc fairness** favours MMP-T141 over MMP-BV141.
- **Evidence that voters would not adapt** (that splitting would continue despite transfers) would keep transfers large and the party-level cost visible for longer.

---

## 10. Limitations and open questions

- **Behaviour is modelled, not observed.** Experiments 1 and 2 assume voters behave the same way under every system. Experiment 3 models adaptation, but the responses are reasoned judgements, varied across a range, not tested against real behaviour under these rules.
- **The escalation scenarios show what happens if gaming spreads, not how likely it is.**
- **Bloc assignments are judgements.** The bloc measures depend on allocating every party, including centrists and parties that supported neither government, to a bloc. The rules themselves don't need blocs defined.
- **The bloc yardstick favours MMP-BV** by counting sub-threshold votes; the countable yardstick, reported in the experiment reports, reduces but doesn't reverse its lead.
- **The Māori electorates are simplified**, and the calibrated model over-predicts Māori-party wins in some years. Most simulated overhang comes from Māori parties, so this probably overstates overhang somewhat.
- **The 2026 starting point is provisional**, and Te Pāti Māori's extreme split dominates the early elections in Experiment 3.
- **Only one way of changing the electorate–list ratio was tested.** Adding 20 list seats was modelled; reducing the number of electorates, or the Review's 60:40 electorate ratio, was not.
- **Untested refinements.** The explainer's optional cap (no party loses more than one seat to transfers) and hybrids between absorbing and growing were not simulated.
- **Costs outside the model.** The fiscal cost of 20 MPs, public acceptance, and how well each rule can be explained were not modelled, though they are likely to decide the question in practice.

---

## Sources

| File | Contents |
|---|---|
| `overhang-transfer-explainer.md` | Plain-language explainer of the transfer proposal, with 2023 and 2026 worked examples |
| `experiment1_report.md` | Experiment 1: wide synthetic stress test (5,000 scenarios) |
| `report_experiment2.md` | Experiment 2: actual elections 2005–2023, and 5,000 calibrated scenarios |
| `report_experiment3.md` | Experiment 3: 1,000 adaptive futures from 2026, escalation scenarios, pure-PR benchmark |
| `futures_walks/results.csv` | Experiment 3 election-level results, used here for the year-by-year Gallagher and overhang figures in Section 6.1 |
| `mc_results.csv`, `mc_results_calibrated.csv` | Experiment 1 and 2 scenario-level results, used here for the countable bloc yardstick figures in Section 6.2 |
| `results_2026.json` | 2026 provisional result and transfer estimate |
