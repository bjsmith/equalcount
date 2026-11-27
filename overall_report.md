# Counting each vote once: the Overhang Transfer

### What one change to how votes are counted would do about overhang in New Zealand, tested on the elections since 2005, the 2026 result, and 160,000 simulated elections

*Draft for discussion, 27 November 2026. The 2026 figures use the official count, published on 27 November; split votes are still estimated from 2023 patterns, and will be updated when the Electoral Commission publishes its split-vote statistics (due by 18 December). The code behind every figure is on [GitHub](https://github.com/bjsmith/equalcount).*

---

## Summary

**The context.** New Zealand has elected its Parliament by [MMP](#gloss-mmp) since 1996. Each voter has two ticks: a **party vote**, which sets each party's share of the 120 seats, and an **electorate vote** for a local MP. A party's electorate MPs come out of its share, and its list fills the rest. When a party wins more electorates than its share allows, it keeps the extra seats. That is an [overhang](#gloss-overhang), and the House grows to fit it.

Until 2026 overhangs were 0–2 seats. The 2026 election produced the largest yet, and Parliament grew to **130 seats**, ten above its base:
- National won 6 more electorates than its party vote entitled it to.
- Te Pāti Māori won 5 electorates on about 0.6% of the party vote, 4 more than its entitlement.

**The problem.** With two ticks but only one Parliament to make up, MMP works because each voter has an equal hand in that Parliament's party make-up. Usually the party vote carries that hand, and the electorate vote only decides who fills some of a party's seats. The 2026 overhangs came mostly from [split ballots](#gloss-split): an electorate vote for one party's candidate and a party vote for another party. Those ballots shaped Parliament twice. They elected an MP whose seat no party votes cover, and their party votes still counted in full for another party. Nothing in the rules discourages this, and the simulations here show that if it spreads, Parliament can reach 180 seats or more.

**Three changes, tested together and apart:**
1. **Twenty more list seats (141 in all).** The simple fix, in the direction the 2023 Independent Electoral Review recommended when it called for more list seats as Parliament grows. It can be combined with a hard limit on the House.
2. **The Overhang Transfer.** When, and only when, a party wins more electorates than its party vote entitles it to, count just enough of the party votes on the ballots that elected its winning candidates for that party. Every electorate MP keeps their seat, and the House doesn't need to grow to fit them.
3. **The Backup Vote.** Built on the transfer's machinery: at every election, a party vote for a party below the [threshold](#gloss-threshold) counts for the voter's electorate candidate's party, if that party is in Parliament.

**What each change adds.** The table comes from [Experiment 3](#gloss-exp3), a behavioural simulation: 1,000 simulated futures of five elections each (2029–2041), starting from the 2026 result. Between elections, voters and parties change their strategies in response to the incentives each system creates; for example, a partner party that loses seats to the transfer campaigns for both ticks. **Those responses are modelled rules, reasoned out by the author and varied in strength, not observed behaviour.** Lower is better in every column.

| Option | [House above base](#gloss-house): median / max | [Voters whose party vote counts differently](#gloss-touched) | [Minority-bloc majority](#gloss-mbm) | [Bloc seat–vote gap](#gloss-blocgap), points | [Standard Gallagher](#gloss-gallagher) | [Adjusted Gallagher](#gloss-adj) |
|---|---|---|---|---|---|---|
| Current MMP (121) | 11 / 34 | 0% | 5.7% | 1.70 | 4.82 | 1.37 |
| 1. 20 more list seats (141) | 6 / 32 | 0% | 4.2% | 1.33 | 3.84 | 0.92 |
| 2. … + the transfer | 0 / 9 | 0.9% | 4.4% | 1.22 | 3.35 | 0.26 |
| 3. … + the Backup Vote | 0 / 10 | 4.0% | 3.7% | 1.00 | 3.58 | 0.21 |
| *The transfer without the extra seats (121)* | 1 / 17 | 3.9% | 5.9% | 1.82 | 4.67 | 0.65 |
| *Benchmark: pure proportional representation, 3.5% threshold* | *0 / 0* | *0%* | *2.9%* | *0.70* | *1.61* | *0.24* |

**What the evidence shows:**
- **More list seats do real work on their own.** They cut the risk of the bloc with fewer votes winning a majority from 5.7% to 4.2% of elections. But the House still grows (by a median of 6 seats, up to 32), and nothing stops engineered splitting: if it spreads, MMP at 141 reaches 198 seats.
- **The transfer adds control of the House and immunity to gaming.** At 141 seats, the House stays within 9 seats of base, the split-list strategy gains nothing, and both proportionality indices improve. It does not lower wrong-winner risk further (4.2% → 4.4%, within the margin of error).
- **The Backup Vote is what lowers wrong-winner risk further** (to 3.7%), at the cost of touching more voters (4.0%, at every election).
- **Both reforms need the extra list seats.** Without them, the transfer controls the House but leaves wrong-winner risk and the bloc gap no better than MMP, because the overhang left over comes from [plurality wins](#gloss-plurality) with few split ballots behind them.

**Conclusion.** If voters and parties adapt to the incentives each system creates, 141 seats with a reform is clearly better than 141 seats alone. Between the two reforms the choice turns on one judgement: whether votes for parties below the threshold should count towards a bloc's fair share. If they should, the Backup Vote version is best; if not, the transfer version is best and touches far fewer voters. **That voters adapt is an assumption, not a finding**, and it matters: on [fixed ballots](#gloss-fixed) the reforms are slightly worse than MMP at 141 on the standard index (section 4).

**What it costs.** On the official 2026 result, the transfer would count part of the party vote of 12.6% of voters for another party, about 204,000 votes' worth, and ACT would lose 3 of its 13 seats. The cost falls in the simulations as voters stop splitting behind overhanging winners: at 141 seats the median share of voters affected is 0.9%. 2026 is also the one test where the transfer looks worst on proportionality, because the two blocs' overhangs happened to balance out. Relying on that balance is itself a cost of doing nothing (section 5). Section 5 also lists every measure on which the reforms do worse.

**Still to come:** 2026 figures recalculated from the official split-vote statistics (due by 18 December), and results for a narrower variant that transfers only pivotal ballots (section 7).

---

## 1. Overhang in New Zealand

**Overhang was small until 2026.** From 2005 to 2023 overhangs were 0–2 seats per election, almost all from Māori parties winning Māori electorates.

**2023.** Te Pāti Māori won 6 electorates on 3.08% of the party vote, which entitled it to 4 seats, and Parliament grew to 122. The left bloc won 44.1% of the counted party vote and 45.1% of the seats.

**2026 (official count).** Both blocs overhung:
- National won 40 electorates against an entitlement of 34.
- Te Pāti Māori won 5 against an entitlement of 1.
- Parliament grew to **130**.

Because both blocs gained, the effects largely cancelled between them. The right won 48.9% of the party vote for parties in Parliament and 50.0% of the seats (65 of 130, one short of a majority). The case against the status quo in 2026 is not a tilt between the blocs. It is ten extra MPs, a balance that depended on both sides gaming the rules about equally, and an incentive that nothing limits (section 5).

**Who can game the status quo.** Three plays are open, in rising order of difficulty:
1. **Te Pāti Māori's built-in advantage.** It can win Māori electorates while its supporters give their party vote elsewhere. The message is simple, but the play is capped by the 7 Māori seats, at about 6 overhang seats.
2. **The major-party [split-list](#gloss-splitlist) play.** It is open to whichever of National or Labour wins many electorates: its supporters tick the party's candidates and party-vote a partner. The overhang scales with electorates won, so it needs a competitive major party with a reliable partner. On the 2026 map that is National's 40 electorates against Labour's 22, but Labour won 46 in 2020.
3. **The left's combined play.** It needs two instructions: on the Māori roll, tick Te Pāti Māori and party-vote Labour; on the general roll, tick Labour and party-vote Green. Mechanically this is no harder than the right's play, since each voter is on one roll and gets one instruction, and the two plays don't compete for the same seats. The difficulty is messaging: a national campaign with two different asks, one of which tells Labour supporters not to give Labour their party vote. In our judgement it is a messaging problem rather than a structural one, and the left's real limit is how many general electorates Labour wins.

Once one bloc games the rules, the other has every reason to copy, so the realistic risk is escalation on both sides. The current rules reward whichever bloc dominates the electorates. The transfer applies the same rule to both.

---

## 2. The principle: one voter, one share

MMP gives each voter two ticks, but there is only one Parliament to make up. What the system promises is that every voter has an equal hand in its party make-up: **one share each**.

Usually the **party vote** carries that share. It sets each party's total number of seats. The party's electorate MPs are drawn from that total, and its list fills the rest. So for most voters the party vote decides the shape of Parliament, and the electorate vote decides who their local MP is within some party's share.

**Overhang breaks this.** An overhang seat isn't covered by any party votes, but someone's ballot elected that MP. Under current law, if those voters split their ballot, their party votes still count in full for another party. Their ballots have shaped the make-up of Parliament twice: once for the seat with no party votes behind it, and again for their party's list seats. Parliament grows to fit both, and every other voter's share is diluted.

There are only two ways to keep such a voter at one share:
- **grow Parliament**, so everyone else counts for a little less. This is current law.
- **count the voter once.** The transfer does this, with one refinement: the voter's share isn't thrown away but filled by their other tick. Their electorate vote, which already elected an MP of that party, counts for that party.

| Your ballot | Current MMP | With the transfer |
|---|---|---|
| Both ticks for the same party | One share, to that party | Same |
| Split; your MP's seat is covered by their party's own votes | One share, by party vote | Same |
| Split; your MP holds an overhang seat | **More than one share**: the MP's seat plus your full party vote | One share: just enough of these ballots count for the MP's party to cover the seat |
| Party vote for a party below the threshold; electorate vote elected an overhanging party's candidate | **No share** | One share, for the MP's party, used before any other ballot |
| Party vote below the threshold, electorate vote for anyone else | No share | No share (the Backup Vote changes this) |

Nobody has a choice taken away; the question is only which of a voter's two choices fills their one share. A voter who wants to be sure their share goes to a particular party can give that party both ticks. A straight ballot is never counted differently.

**Why this matters for governments.** Governments in New Zealand are formed by groups of parties ([blocs](#gloss-bloc)), and strategic splitting happens inside those groups: an ACT voter ticks the National candidate; a Labour voter ticks the Te Pāti Māori candidate. When the transfer counts some of those ballots for the electorate MP's party, votes move from one partner to another, and the group's total barely changes. Under current law, the group that overhangs gets seats on top of its share.

---

## 3. Three changes

### 3.1 More list seats, with or without a hard limit

The simplest change is a larger list tier. Overhang happens when a party wins more electorates than its share of the House, so more list seats mean a party needs a smaller share to cover its electorates. With 71 electorates and 50 list seats, a party winning 40 electorates needs about 33% of the qualifying vote to cover them; with 70 list seats it needs about 28%. Twenty more list seats (141 in all) is the size tested here.

The idea isn't new. The 1986 Royal Commission thought the ideal House would have about 140 seats, though it recommended 120. The 2023 Independent Electoral Review recommended fixing the ratio of electorate to list seats at 60:40 and letting Parliament grow with the population, so that there are always enough list seats to keep Parliament proportional (Recommendation R10). The Electoral Commission had suggested the same ratio in 2012. 141 seats goes further than the Review's ratio: 71 electorates with 70 list seats is close to 50:50.

More list seats reduce overhang but don't remove it, and they do nothing about engineered splitting: a bloc that gains from overhang at 121 seats still gains at 141. A **hard limit** at 141 would stop the House growing. It applies the 2023 Review's rule at the larger size: any overhang is absorbed within the 141 seats by taking list seats from other parties.

Reducing the number of electorates is another way to change the ratio. It was not tested.

### 3.2 The Overhang Transfer

The count is unchanged unless a party overhangs. When one does:

1. **Apply the threshold** on raw party votes, before anything is moved, so no transfer can push a party in or out of Parliament.
2. **Check for an overhang.** Allocate seats by Sainte-Laguë. If no party has won more electorates than its entitlement, the result stands. Once voters adapt, most counts end here.
3. **Use wasted votes first.** On ballots where the electorate vote went to a *winning* candidate of the overhanging party and the party vote went to a party below the threshold, count the party vote for the overhanging party, only as many as needed.
4. **Then transfer the same fraction of other split ballots.** On ballots where the electorate vote went to one of its winning candidates and the party vote went to another qualifying party, count the same fraction *f* of every such party vote for the overhanging party, with *f* just high enough to cover the overhang. Nothing is chosen at random, so a recount gives the same answer, and each party loses votes in proportion to how many of its voters split this way.
5. **Leftover overhang is treated exactly as now.** If even *f* = 1 isn't enough, the party keeps its extra electorates and the House grows by the remainder. (Absorbing the remainder within a fixed House instead was also tested. At 121 seats it makes wrong-winner outcomes *more* likely than MMP once voters adapt, 7.8% against 5.7%, so it is not the version shown.)
6. **Allocate seats** on the adjusted votes. The overhanging party's entitlement now matches its electorates, and every other party's seats are proportional to its counted votes.

**Example: 2023.** Te Pāti Māori's two-seat overhang was covered by 35,038 votes: all 3,010 wasted party votes on ballots for its winning candidates, then 84% of every other split party vote behind them (*f* = 0.842). The fraction is high because the overhang was concentrated in six electorates: in Waiariki, 59% of Labour party voters ticked Rawiri Waititi.

| 2023 | Current law (House grows) | With the transfer |
|---|---|---|
| Size of Parliament | 122 | 120 |
| Te Pāti Māori seats (all 6 electorates kept) | 6 | 6 |
| Labour / Green seats | 34 / 15 | 33 / 14 |
| Left bloc's share of seats (its share of counted party votes: 44.1%) | 45.1% | **44.2%** |

Te Pāti Māori keeps every electorate MP. The cost of its overhang falls on the parties whose voters created it.

**Example: 2026 (official count, split votes estimated).**

| Seats | National | Labour | Green | ACT | NZ First | Opportunity | Te Pāti Māori | House |
|---|---|---|---|---|---|---|---|---|
| Current law | 40 | 36 | 17 | 13 | 12 | 7 | 5 | 130 |
| With the transfer | 40 | 34 | 15 | **10** | 10 | 7 | 5 | **121** |

- **National's overhang (6 seats)** is covered by moving 45% of the party votes on split ballots behind its 40 winners. About 75,000 of those are ACT votes, 31,000 NZ First, 11,000 Opportunity, 9,900 Labour and 4,800 Green.
- **Te Pāti Māori's overhang can't be fully covered.** Even moving every split ballot behind its winners leaves one seat over, so the House grows to 121. The ballots moved include about 66,000 Labour and Green party votes cast in the Māori electorates.
- **The right's seat share** moves from 50.0% to 49.6%, closer to its 48.9% share of the party vote for parties in Parliament.

**Properties:**
- **Targeted.** Nothing changes in an election without overhang: 2017 and 2020 would have been counted exactly as they were.
- **Every electorate MP keeps their seat**, including every Māori-electorate MP.
- **No blocs need to be defined.** The rule works on parties; the effect on blocs follows because splitting mostly happens within them.
- **Cross-bloc splitters are counted the same way.** A Labour voter who ticks a popular local National MP whose seat is an overhang is treated like an ACT voter who does.
- **Decoys gain nothing.** The transfer follows each voter's own ballot, not a declared link between a candidate and a list. That is the flaw that let decoy lists defeat Italy's *scorporo* (section 6.2).

### 3.3 The Backup Vote

The transfer already uses wasted votes, but only when an overhang needs them. Its first step counts sub-threshold party votes on ballots behind an overhanging party's winners, and only as many as the overhang requires.

The Backup Vote uses the same mechanism **at every election, for every sub-threshold voter**: a party vote for a party below the threshold is counted for the party of the voter's electorate candidate, if that party is in Parliament, whether or not the candidate won. In effect the electorate vote becomes a contingent second preference, close to the "spare vote" the 2023 Review discussed, with no change to the ballot paper. Any overhang that remains is then handled by the transfer as above.

It answers a different problem (wasted votes, not overhang), so it belongs as much to the threshold debate as to this one. It is included because it makes Parliament more proportional between the blocs, which is what decides who governs: it gives the lowest bloc seat–vote gap and wrong-winner rate of any option tested, on fixed and adapting ballots alike. It does not improve the standard Gallagher index, which it makes slightly worse than the transfer alone (section 4), because it counts some party votes for a party other than the one ticked.

---

## 4. What the evidence shows

### 4.1 How it was tested

Every rule was applied to the same ballots, held as a table of party vote × electorate candidate for each electorate, so each rule can see which ballots elected which MP. There were four tests (details in Appendix A):

- **Real elections.** The 2005–2023 elections recounted from the Electoral Commission's split-vote tables, and 2026 with split votes estimated.
- **Experiment 1, a stress test.** 5,000 synthetic elections far more fragmented and split than New Zealand's, to find where each rule breaks.
- **Experiment 2, typical New Zealand elections.** 5,000 synthetic elections calibrated to 2005–2023.
- **Experiment 3, adapting futures.** 1,000 futures of five elections from the 2026 result, in which voters and parties respond to each system's incentives. Two further scenarios let the split-list strategy spread under current rules.

The real elections and Experiments 1 and 2 use **fixed ballots**: voters behave the same whatever the rules. Only Experiment 3 lets them adapt.

**The key assumption.** Every rule here changes incentives, and voters and parties respond to incentives. A party that loses seats to the transfer has reason to ask its supporters for both ticks; a strategy that stops paying is abandoned. Experiment 3 models those responses, and its results are the main evidence. But the responses are judgements about behaviour, written as rules and varied in strength, not observations. Where results differ between fixed and adapting ballots, both are shown.

The same six measures are used throughout (defined in Appendix B): House above base, voters whose party vote counts differently, minority-bloc majority, the bloc seat–vote gap, and two versions of the Gallagher index. The **standard** index compares seats with all party votes as cast: it makes no allowance for the threshold or for the reforms' aim. The **adjusted** index makes both allowances, counting each voter once and counting sub-threshold voters for their electorate candidate's party. One leans towards current MMP and the other towards the reforms, so they are always shown together.

### 4.2 Step by step

**Experiment 3, voters and parties adapt** (1,000 futures × 5 elections, 2029–2041; minority-bloc majority with its 95% margin):

| Option | House above base: median / max | Voters counted differently | Minority-bloc majority | Bloc seat–vote gap, points | Standard Gallagher | Adjusted Gallagher |
|---|---|---|---|---|---|---|
| Current MMP (121) | 11 / 34 | 0% | 5.7% ±0.7 | 1.70 | 4.82 | 1.37 |
| 1. 20 more list seats (141) | 6 / 32 | 0% | 4.2% ±0.6 | 1.33 | 3.84 | 0.92 |
| 2. … + the transfer | 0 / 9 | 0.9% | 4.4% ±0.6 | 1.22 | 3.35 | 0.26 |
| 3. … + the Backup Vote | 0 / 10 | 4.0% | 3.7% ±0.5 | 1.00 | 3.58 | 0.21 |
| *The transfer at 121* | 1 / 17 | 3.9% | 5.9% ±0.7 | 1.82 | 4.67 | 0.65 |
| *Benchmark: pure PR, 3.5%* | *0 / 0* | *0%* | *2.9% ±0.4* | *0.70* | *1.61* | *0.24* |

**Experiment 2, fixed ballots** (5,000 elections calibrated to 2005–2023; voters behave the same under every system):

| Option | House above base: median / max | Voters counted differently | Minority-bloc majority | Bloc seat–vote gap, points | Standard Gallagher | Adjusted Gallagher |
|---|---|---|---|---|---|---|
| Current MMP (121) | 2 / 18 | 0% | 6.8% ±0.7 | 1.70 | 3.70 | 0.79 |
| 1. 20 more list seats (141) | 1 / 10 | 0% | 6.5% ±0.7 | 1.54 | 3.41 | 0.56 |
| 2. … + the transfer | 0 / 4 | 0.7% | 5.8% ±0.6 | 1.29 | 3.50 | 0.55 |
| 3. … + the Backup Vote | 0 / 4 | 5.3% | 3.5% ±0.5 | 0.74 | 3.70 | 0.58 |
| *The transfer at 121* | 1 / 6 | 0.9% | 5.9% ±0.7 | 1.41 | 3.88 | 0.78 |
| *Benchmark: pure PR, 3.5%* | *0 / 0* | *0%* | *6.0% ±0.7* | *1.22* | *3.79* | *0.28* |

**How to read the steps:**
- **Step 1, more list seats,** improves every measure in the adapting futures, and is the step that deals with overhang from plurality wins. On fixed ballots it barely moves wrong-winner risk.
- **Step 2, the transfer,** holds the House near base and, when voters adapt, cuts both Gallagher indices. On fixed ballots it is slightly worse on the standard index (3.41 → 3.50) and level on the adjusted one. Its wrong-winner rate is level with step 1 when voters adapt and slightly better on fixed ballots.
- **Step 3, the Backup Vote,** gives the lowest wrong-winner rate and bloc gap in both tests, but touches 4–5% of voters at every election and slightly worsens the standard index.
- **The transfer at 121** shows why the list seats matter: without them, the overhang left over comes from plurality wins, and wrong-winner risk and the bloc gap are no better than MMP's.
- **In Experiment 2 the pure-PR benchmark is not a floor:** at a 3.5% threshold it still produces a minority-bloc majority in 6.0% of elections, because sub-threshold votes still elect no one.

### 4.3 Does the conclusion depend on the measure?

Four versions of the Gallagher index were computed for every election (defined in Appendix B). Two lean in known directions:

| Test | Option at 141 | Standard | Qualifying parties | One-share | Adjusted (one-share + rescued voters) | Sainte-Laguë index | Minority-bloc majority: all votes / qualifying votes |
|---|---|---|---|---|---|---|---|
| Exp 3 (adapt) | MMP | 3.84 | 3.23 | 0.88 | 0.92 | 26.2 | 4.2% / 4.1% |
| Exp 3 (adapt) | + transfer | 3.35 | 0.80 | 0.18 | 0.26 | 6.3 | 4.4% / 1.7% |
| Exp 3 (adapt) | + Backup Vote | 3.58 | 1.52 | 0.18 | 0.21 | 6.5 | 3.7% / 2.3% |
| Exp 2 (fixed) | MMP | 3.41 | 0.87 | 0.27 | 0.56 | 9.4 | 6.5% / 2.5% |
| Exp 2 (fixed) | + transfer | 3.50 | 0.93 | 0.26 | 0.55 | 9.5 | 5.8% / 1.1% |
| Exp 2 (fixed) | + Backup Vote | 3.70 | 1.70 | 0.55 | 0.58 | 9.6 | 3.5% / 3.2% |

- **When voters adapt, every proportionality measure favours the reforms over MMP at 141.**
- **On fixed ballots, it depends on the measure.** The indices built on votes as cast slightly favour MMP; the one-share indices are level, except that the Backup Vote does worse on plain one-share. The transfer is better than MMP on wrong winners on both yardsticks. The Backup Vote is much better on the headline yardstick but slightly worse than MMP on qualifying votes.
- **Between the two reforms, the bloc yardstick decides.** Counting votes for parties below the threshold in each bloc's total (the headline yardstick) favours the Backup Vote, because it counts exactly those votes. Counting only qualifying votes favours the transfer, in both tests.

---

## 5. Costs, and where the changes do worse

**Some voters' party votes count for another party.** Two figures describe it, and both should be given together: the share of voters any part of whose party vote is moved (the cautious headline figure), and the votes' worth actually moved.
- On the official 2026 result: 12.6% of voters, about 204,000 votes' worth (about 7% of the party vote).
- In the adapting futures at 141 seats: a median of 0.9% of voters for the transfer and 4.0% for the Backup Vote. At 121 seats the transfer's median is 3.9%.

**Partner parties lose seats.** In 2026 ACT would fall from 13 to 10, NZ First from 12 to 10, and Labour and the Greens by 2 each. These are the parties that campaign openly for split votes, and several are in government, so they hold a veto over any change.

**Losses can be concentrated.** The most seats any party loses against its entitlement on raw votes, in the adapting futures:

| Option | Most seats a party loses: median / max | Worst-hit party's vote moved: median / 1 election in 10 | Elections where some party loses 2+ seats |
|---|---|---|---|
| The transfer at 121 | 2 / 12 | 7.6% / 22.1% | 54% |
| The transfer at 141 | 1 / 11 | 1.0% / 11.8% | 32% |
| … + the Backup Vote | 1 / 11 | 2.7% / 13.8% | 41% |
| MMP at 141 with a hard limit | 3 / 10 | – | 91% |

**The first election is a shock.** Before voters adapt, almost every election involves a transfer: at 121 seats, 8.3% of voters are affected in the first simulated election and some party loses two or more seats in 82% of them. This falls to 3.1% and 38% by 2041. With 20 more list seats it falls faster, and by 2035 the median election has no transfer at all. The fall is the modelled adaptation, and it is also the political price of the transition.

**Splitters who are not gaming pay too.** The same fraction is moved from every split ballot behind an overhanging winner: safe seats as well as marginal ones, personal votes as well as tactical ones. A variant that moves only *pivotal* ballots (in seats where the split votes exceeded the winning margin) would answer this more directly. It is being tested.

**The Māori electorates.** In 2026 about 66,000 Labour and Green party votes cast in Māori electorates would be counted for Te Pāti Māori. Every Māori-electorate MP keeps their seat, and the votes are counted for the party those voters elected locally.

**If splitting becomes extreme and voters don't respond** (Experiment 1, the stress test), the transfer still controls the House (median 1 seat above base, against 13) and reduces wrong winners (9.5% → 7.5%), but a median 13% of voters are affected, and in half of elections the worst-hit party loses a quarter or more of its party vote to transfers.

**Where the transfer does worse.** Each row is a measure on which the transfer (with leftover growing the House) does worse than the same system without it, on the same elections:

| Where | Measure | Without → with the transfer |
|---|---|---|
| Every test | Voters whose party vote counts differently | 0 → 0.6–13.1% |
| 2005–2023 | Standard Gallagher | slightly worse in 3 of 5 overhang years |
| 2026 | Standard Gallagher | 3.39 → 4.87 |
| 2026 | Adjusted Gallagher (approximate) | 0.64 → 0.71 |
| Typical NZ, fixed ballots (Exp 2) | Standard Gallagher | 3.70 → 3.88 at 121; 3.41 → 3.50 at 141 |
| Extreme, fixed ballots (Exp 1) | Standard Gallagher | 8.45 → 10.73 at 121; 7.24 → 8.14 at 141 |
| Adapting futures (Exp 3), at 121 only | Bloc seat–vote gap | 1.70 → 1.82 (mean difference +0.08 ±0.05) |
| Small vote changes (paradox test) | A party gains party votes and loses a seat | 0 → about 10 in 10,000 changes (7 at 141) |

The [monotonicity paradox](#gloss-paradox) is rare and confined to elections where leftover overhang grows the House. Absorbing the leftover instead almost removes it (0.4 in 10,000), but at 121 seats that raises wrong-winner risk.

**Why 2026 looks bad for the transfer.** On the official 2026 result the transfer is clearly worse on the standard index (3.39 → 4.87) and slightly worse on the adjusted one (0.64 → 0.71). That is because the overhangs on the left and the right largely cancelled out: National's 6 seats against Te Pāti Māori's 4. Each bloc's double count offset the other's, so Parliament as a whole stayed roughly in line with the party vote. The transfer removes both overhangs, and moving about 204,000 votes' worth to do it shows up as a gap against the ticks as cast. Even so, it narrows the gap between the blocs (1.07 → 0.66 points).

**The real costs of not changing.** A Parliament that is proportional only because both sides overhang by similar amounts is proportional by accident, and that cuts against the spirit of MMP:
- **It is brittle.** The balance holds only while the two sides game the rules about equally. Section 1 shows they can't: Te Pāti Māori's play is capped at about 6 seats, while the major-party split-list play grows with the electorates a party wins. When one side finds it can engineer more overhang than the other, the balance breaks. In the escalation scenario, minority-bloc majorities rise from 5.7% to 9.6% of elections.
- **It makes voters cast votes they wouldn't otherwise cast.** To keep their side level, supporters are asked to split their ballots strategically: to tick a candidate or party they wouldn't otherwise choose, just so their bloc isn't outdone. A system in which each side must match the other's gaming asks voters to vote for the rules rather than for what they want.

**The defence.** The transfer moves a voter's party vote only when that voter's own electorate vote has elected an MP their party vote does not pay for. Without it, that voter shapes Parliament twice, and everyone else pays through a larger House, or through an arms race that keeps the two sides level only for as long as neither gets ahead.

---

## 6. The debate

### 6.1 Alternatives: why not the other proposals?

The debate after the 2026 election has produced plenty of proposals. [The Spinoff listed ten](https://thespinoff.co.nz/politics/19-11-2026/ten-ways-to-fix-mmp-explained), and 46 experts have called for a select committee inquiry. None of them reassigns votes. Each is a different answer to one question: **when a party wins an electorate seat that its party vote doesn't cover, who pays for it?**

| Proposal | Who pays for the uncovered seat | On the 2026 official count |
|---|---|---|
| Current law ("tune the system, don't scapegoat it") | Every other voter, through a bigger House | 130 seats |
| More list seats (Spinoff Option 2) | The same, less often | Tested as step 1 (sections 3.1 and 4) |
| Absorb within a fixed House (Option 1; the 2012 and 2023 reviews) | The other parties' list seats, mostly the other bloc's | 120 seats; the right goes from 50.0% to 50.8% of seats on 48.9% of the vote |
| Compensation seats (Option 3) | Every voter, through a much bigger House | About 142 seats if Te Pāti Māori's overhang is left alone; about 700 if it isn't |
| Party vote overrides electorate wins (Option 4; Germany since 2023) | The electorate winners, who aren't seated | 10 electorates without the MP they elected, 4 of them Māori electorates |
| One combined vote (Option 5) | Every voter, who loses the split ballot at every election | A different ballot paper |
| Weighted voting in the House (Option 6) | No one in divisions; everyone through a bigger House | 130 seats, with unequal votes |
| **The Overhang Transfer** | **The voters whose ballots elected the uncovered MPs.** Part of their party vote counts for the party they elected locally | 121 seats; every electorate MP seated; about 204,000 votes' worth moved (section 5) |

These alternatives weren't run through the simulations. The evidence in section 4 compares the transfer only with current MMP, with 20 more list seats, and with a hard limit at 141. The figures below are seat arithmetic on the 2026 official count, with split votes estimated where they matter.

**Keep growing the House** (current law). This is the strongest rival, because it is already the law and moves no votes. The best case for it is 2026 itself: the two blocs' overhangs largely cancelled, and the right won 50.0% of the seats on 48.9% of the vote. Against it:
- **It costs ten extra MPs now and sets no limit later.** In the adapting futures, if the split-list play spreads (section 4), MMP's House reaches 60 seats above base, and 57 above base even at 141 seats. The bloc with fewer votes wins a majority in 9.6% of elections.
- **It rewards whichever bloc dominates the electorates.** In those futures, 457 of the 469 minority-bloc majorities under MMP went to the bloc holding more electorates (on today's map, the right). Not all of that tilt comes from gaming: under the transfer, 271 of 286 still go the same way, because plurality wins and wasted votes also favour that bloc. But gaming makes it much worse. The tilt would reverse in a year like 2020, when Labour won 46 electorates. Either way the rule hands an advantage to whoever is already winning.
- **Nothing in the rules discourages any of this.** Section 1 sets out who can game the status quo and how.

**Absorb the overhang within a fixed House** (Option 1, recommended by both the 2012 and 2023 reviews). It keeps the House at 120 and unseats no one, but it moves the cost to the parties that didn't create the overhang.
- **In 2026 it would turn a near-even result into a tilt.** Labour would lose 4 seats, and the Greens, ACT and NZ First 2 each. The right would end up with 61 of 120 seats (50.8%) on 48.9% of the vote. This is the Spinoff's main objection.
- **It doesn't remove the payoff from splitting.** The bloc that creates the overhang keeps it, and everyone shares the cost.
- **At 141 seats it is affordable only with the transfer**, because the transfer leaves little overhang to absorb:

| Experiment 3, at 141 seats | House above base: median / max | Voters counted differently | Minority-bloc majority | Bloc seat–vote gap, points | Standard Gallagher | Adjusted Gallagher |
|---|---|---|---|---|---|---|
| MMP, House grows | 6 / 32 | 0% | 4.2% ±0.6 | 1.33 | 3.84 | 0.92 |
| MMP, hard limit | 0 / 0 | 0% | 6.1% ±0.7 | 1.65 | 4.34 | 1.15 |
| Transfer, House grows | 0 / 9 | 0.9% | 4.4% ±0.6 | 1.22 | 3.35 | 0.26 |
| Transfer, hard limit | 0 / 0 | 1.7% | 4.6% ±0.6 | 1.19 | 3.40 | 0.26 |
| Backup Vote, House grows | 0 / 10 | 4.0% | 3.7% ±0.5 | 1.00 | 3.58 | 0.21 |
| Backup Vote, hard limit | 0 / 0 | 4.4% | 4.2% ±0.6 | 1.00 | 3.64 | 0.26 |

Without the transfer, a hard limit puts wrong-winner risk back at MMP-at-121 levels, and some party loses two or more list seats in 91% of elections. If gaming escalates it is the worst option tested: minority-bloc majorities reach 11.2% of elections, and 41% of futures have at least one. (The limited House without a transfer is run on the ballots of the uncapped MMP141 futures, so its voters aren't modelled as adapting to the limit.)

**More list seats or fewer electorates** (Option 2). This is step 1 of the evidence. Twenty more list seats do real work on their own (section 4), and the evidence favours the transfer *with* them, not instead of them. They reduce overhang but don't remove it, and they leave engineered splitting as profitable as before. Fewer electorates would work the same way, at the cost of larger electorates and new boundaries. It wasn't tested.

**Compensation seats** (Option 3; Germany 2013–2021). Give the other parties extra list seats until the result is proportional again. It moves no votes and unseats no one, but in New Zealand the arithmetic rules it out:
- **About 142 seats in 2026 if only National's overhang is compensated** (the Spinoff's figure). Te Pāti Māori's 4 extra seats would then sit uncompensated on top, so its play would keep paying.
- **About 700 seats to compensate Te Pāti Māori too**, because it holds 5 electorates on 0.6% of the party vote.
- **Germany abandoned the rule** after the Bundestag grew from a standard 598 seats to 736.

**Party vote overrides electorate wins** (Option 4; Germany's 2023 rule). An overhanging party's electorate winners with the lowest vote shares aren't seated. This is the cleanest fix on paper: the House is fixed, no votes move, and it is exactly proportional. Germany's Constitutional Court upheld the principle in 2024. On 2026 its bloc result is the same as the transfer's. The difference is who pays:
- **It would unseat 10 electorate MPs in 2026**: National's 6 with the lowest shares, and 4 of Te Pāti Māori's 5.
- **Two of the Te Pāti Māori MPs unseated won outright majorities**: Debbie Ngarewa-Packer in Te Tai Hauāuru (54.5%) and Oriini Kaipara in Tāmaki Makaurau (52.5%). The other two are Rawiri Waititi in Waiariki (44.5%) and Aperahama Edwards in Te Tai Tokerau (30.2%). Only Hauraki-Waikato (67.9%) would keep its MP.
- **Removing majority-elected MPs from Māori electorates would be widely criticised as anti-Māori**, with some justification. We regard that as politically decisive.
- **The open letter's softer version**, letting each party keep up to two overhang seats, would still unseat Waititi and Edwards, and four National MPs.
- **A version that exempts the Māori electorates** would remove National's overhang and keep Te Pāti Māori's. The right would see that as rigged, and it would be hard to argue otherwise.
- **The transfer seats every electorate MP and applies one rule to both blocs.**

**One combined vote** (Option 5). One tick elects the local MP and counts as the party vote. That ends split ballots, and with them almost all overhang, but:
- **It takes away a choice many voters use**, at every election, including the many splits that never create an overhang. Changing the ballot would probably need a referendum, given that 2011 endorsed MMP as it is.
- **It squeezes small parties.** A Green voter in a marginal seat who wants to keep National out would have to give Labour their party vote as well.
- **It doesn't end overhang from concentrated support.** Te Pāti Māori's electorate candidates won about 3% of all candidate votes in 2026. Counted as party votes, that would still leave it about one seat over.

The transfer is the same idea applied only where it's needed. It counts a split ballot as a single vote only when that ballot elected an MP whose seat isn't covered, and only to the extent needed to cover it. Every other split is left alone.

**Weighted voting in the House** (Option 6, proposed in the open letter). Overhang MPs take their seats, but each party's votes in the House are weighted by its party vote.
- **It removes the overhang's effect on divisions**, including confidence and supply, without moving any votes.
- **It leaves everything else in place.** The House still grows. Overhang MPs still bring select-committee places, speaking time, funding and ministerial posts. MPs would no longer have equal votes. Conscience votes would need their own rule.
- **It treats the symptom in one place** rather than changing what the ballot does.

**The rest of the list.**
- **Ranked-choice or multi-member electorates** (Option 7) address plurality winners. They don't stop the split-list play: an ACT voter can rank the National candidate first as easily as tick them.
- **Abolishing the Māori seats** (Option 8) is a political non-starter, and it wouldn't touch National's overhang, which was 6 of the 10 extra seats in 2026.
- **Abolishing electorates** (Option 9) is the pure-PR benchmark in section 4. It ends overhang by ending local representation.

**Lowering the threshold and ending coat-tailing** (the 2023 Review) answer a different problem: votes for parties that miss the threshold. They complement any overhang rule rather than replacing one. The Backup Vote (section 3.3) is this project's contribution to that debate.

**Where this leaves the transfer.** It is the only proposal on the list that does all four of these:
- seats every electorate winner, including every Māori-electorate MP;
- keeps the House at or near its base: a median of 0–1 seats above it, and at most 9 above at 141 seats. Gaming can't push it higher;
- applies one rule to both blocs;
- leaves straight ballots, and splits that create no overhang, untouched.

Its price is that some split voters' party votes count partly for the party they elected locally. Section 5 sets out that cost in full.

### 6.2 What critics will say

**"This isn't new."** Agreed, in principle.
- Since 1956, German law has excluded the party votes of voters who elect an independent, to stop them gaining a "double vote weight". The Constitutional Court upheld the rule in 1957 and 1988. In 1988 it named overhang as the exception that splitting can exploit.
- The transfer extends that rule to overhang, and counts the vote for the party the voter elected rather than discarding it.
- New Zealand gives the opposite answer for independents: the list seats shared out are reduced, so every other party pays. The 2023 Review recommended the same treatment for overhang.
- No published proposal of the ballot-level, overhang-only transfer was found. The search was not exhaustive; see the [review of prior art](literature_prior_art.md).

**"Vote linkage has been gamed before."** Yes, but through a different kind of link.
- Italy's [*scorporo*](https://en.wikipedia.org/wiki/Scorporo) subtracted votes from the list linked to a winning candidate, and was defeated by decoy lists in 2001.
- The transfer follows each voter's own ballot, not a declared link. A decoy party gains nothing, because the transfer counts back the party votes actually cast on the ballots that elected the winner.

**"The party vote is the one that counts"** (the MMP defender; compare Tom Peoples, ["In defence of MMP"](https://thespinoff.co.nz/politics/23-11-2026/in-defence-of-mmp), The Spinoff, 23 November). The split voter is "weighting local representation", and a rule that changes the value of their party vote penalises a choice the ballot invites.
- When the seat is covered by the party's own votes, nothing changes. The transfer bites only when the voter's electorate vote has created a seat that their party vote doesn't pay for. At that point the voter isn't just choosing a local MP, but adding a seat to one party while funding another.
- Expect a call for a referendum.

**"You're giving my voters' votes to National"** (the partner-party politician). There is a real weakness here. The uniform fraction includes safe-seat and cross-bloc personal votes: in 2026, about 9,900 Labour and 4,800 Green votes counted for National. The pivotal-ballot variant is the answer being tested.

**"The problem is 71 electorates against 50 list seats"** (the structuralist). Conceded. Once splitting stops, the remaining overhang comes from plurality wins, which the transfer can't fix. That is why the evidence favours the transfer *with* more list seats.

**"Nobody can say which voter caused which overhang seat."** This was one of the German Court's reasons in 1997 for not treating overhang as double vote weight. The transfer doesn't try to identify individuals. It attributes the overhang collectively to the split ballots behind the overhanging party's winners. Straight-ticket ballots aren't double counted, which is why the transfer leaves them alone.

**"It needs new counting machinery"** (the administrator). True. The official count would need the party-vote × candidate table for each electorate, which is currently published only as statistics after the count.

**"The models are yours"** (the methodologist). Also true. The adaptation and escalation responses are reasoned judgements, varied across ranges but not observed, and the 2026 split votes are estimated. The code, inputs and stored results are published so the results can be checked (Appendix A).

---

## 7. Conclusion

**The finding.** If voters and parties adapt to the incentives each system creates, 141 seats with a reform is clearly better than 141 seats alone. It holds the House near its base size, removes the payoff from engineered splitting, and is more proportional on every proportionality measure. The two reforms differ on one judgement:
- **The Backup Vote at 141** is best if votes for parties below the threshold should count towards a bloc's fair share: it has the lowest wrong-winner rate (3.7%) and bloc gap (1.00 points).
- **The transfer at 141** is best if they shouldn't: it has the lowest wrong-winner rate on qualifying votes (1.7%) and the best standard index, and it affects far fewer voters (0.9% against 4.0%).

**The assumption it rests on.** That voters adapt. In the simulations, the transfer's cost falls and its proportionality gains appear because splitting behind overhanging winners declines once it stops paying. That is a modelled response. If voters kept splitting regardless, the fixed-ballot results would apply instead, and there the reforms are slightly *less* proportional than MMP at 141 on the standard index, while still better on House size and, for the transfer, on wrong winners.

**Other limitations:**
- **The escalation scenarios show what happens if gaming spreads, not how likely it is.**
- **2026 split votes are estimated** from 2023 patterns. The official statistics may change how much of National's overhang came from splitting rather than plurality wins; if much of it is plurality wins, the transfer covers less and looks more like a penalty on personal voting. Public claims about 2026 should wait for them.
- **Bloc assignments are judgements.** Opportunity is counted with the left in the simulations. The transfer itself needs no blocs.
- **The Māori electorates are simplified**, and the calibrated model over-predicts Māori-party wins in some years.
- **Costs outside the model** are likely to decide the question in practice: the fiscal cost of extra MPs, new counting machinery, public acceptance, and how well the rule can be explained.

**Still to come.** This is a working draft, and two additions are planned:
- **2026 with real split votes.** The Electoral Commission's split-vote statistics are due by 18 December. The 2026 figures in this report will then be recalculated from actual ballots instead of estimates.
- **A narrower transfer.** A variant that moves only *pivotal* ballots, in seats where the split votes exceeded the winning margin, is being tested. It would spare split voters in safe seats and personal votes for popular MPs.

Other variants have not been tested yet: a limit of one seat lost per party per election, the transfer without its wasted-vote first step, and fewer electorates instead of more list seats.

---

## Appendix A. Method

### Common framework

- **Ballots, not just totals.** Every election, real or simulated, is held as a table of party vote × electorate candidate for each electorate. That is how each rule can see which ballots elected which MP, and where their party votes went.
- **Seat rules.** Sainte-Laguë allocation; a 5% threshold, waived for any party winning an electorate; qualification decided on raw party votes before anything is moved.
- **Base size.** 121 seats, so that 71 electorates sit with 50 list seats (120 for the real 2005–2023 elections, as used at the time), and 141 for the larger House.
- **The systems.** Every system was run on identical ballots: current MMP, the transfer (leftover grows or is absorbed), the transfer with the Backup Vote, all at 121 and 141 seats, and the Review's hard limit at 141.

### Real elections

The 2005–2023 elections recounted at 120 seats from the Electoral Commission's split-vote tables (MMP → transfer in each cell):

| Year | Overhang | House | Voters counted differently | Bloc seat–vote gap, points | Standard Gallagher | Adjusted Gallagher |
|---|---|---|---|---|---|---|
| 2005 | Māori Party 1 | 121 → 120 | 0.9% | 0.05 → 0.40 | 1.18 → 1.29 | 0.22 → 0.26 |
| 2008 | Māori Party 2 | 122 → 120 | 1.4% | 3.62 → 3.73 | 3.94 → 4.03 | 0.34 → 0.13 |
| 2011 | Māori Party 1 | 121 → 120 | 0.6% | 0.17 → 0.56 | 2.38 → 2.32 | 0.45 → 0.53 |
| 2014 | United Future 1 | 121 → 120 | 0.6% | 0.35 → 0.75 | 3.76 → 3.68 | 0.40 → 0.52 |
| 2017 | none | 120 | 0 | 1.48 | 2.81 | 0.07 |
| 2020 | none | 120 | 0 | 0.21 | 4.22 | 0.11 |
| 2023 | Te Pāti Māori 2 | 122 → 120 | 1.4% | 1.25 → 0.34 | 2.82 → 2.96 | 0.26 → 0.37 |

Every historical overhang was fully covered, so the House would have stayed at 120 every time; at most one party lost one seat; no election produced a minority-bloc majority under either rule. The differences in the indices are within a seat's rounding: one seat at 120 is 0.83 points of seat share.

**2026**, with split votes estimated: House 130 → 121; 12.6% of voters counted differently; no minority-bloc majority under either rule; bloc seat–vote gap 1.07 → 0.66 points; standard Gallagher 3.39 → 4.87; adjusted Gallagher 0.64 → 0.71. Two caveats. The adjusted index is approximate, because only the split ballots behind National's and Te Pāti Māori's winners are estimated. The bloc gap needs the 0.86% of votes for sub-threshold parties assigned to blocs; they are split evenly here, and the gap ranges from 0.64 to 1.50 under MMP depending on that choice, but the transfer narrows it by about 0.4 points under every allocation.

### The experiments

- **Experiment 1, a stress test.** 5,000 synthetic elections spanning far more fragmented party systems and splitting rates than New Zealand has had: 2–5 parties per bloc, blocs from 30:70 to 70:30, and strategic splitting anywhere from 0% to 100%. Ballots are fixed. The median overhang is 13. See `experiment1_report.md`.
- **Experiment 2, New Zealand.** 5,000 synthetic elections, every parameter drawn from the seven elections from 2005 to 2023 (495 per-electorate split-vote tables). Voter behaviour is fitted to each election's electorate results by approximate Bayesian computation. Ballots are fixed. See `report_experiment2.md`.
- **Experiment 3, adaptation.**
  - 1,000 futures of five elections (2029–2041) from the 2026 result. Events outside strategy (swings, party drift, new parties) are shared across systems within a future.
  - Voters' and parties' responses depend on what each system's last election taught them. Examples: partners campaign for two ticks after losing seats to transfers; Te Pāti Māori rebuilds its party vote when its overhang no longer pays.
  - The responses were reasoned through by hand for ten futures, encoded as rules, and run with each rule's strength drawn per future from a range around the hand-reasoned value. The ranking of systems doesn't hinge on those strengths: no drawn strength correlates with a future's bloc fairness beyond 0.10. The rules' form was not varied, and they were written by the same analyst who proposed the transfer.
  - Two scenarios add escalation of the split-list strategy under current rules. Under escalation MMP reaches 20 seats above base at the median and up to 181 seats, with minority-bloc majorities in 9.6% of elections; MMP at 141 reaches 198 seats and 8.0%. The reforms are unaffected by construction, because the split ballots behind an engineered overhang are exactly what the transfer counts back.
  - See `report_experiment3.md`.
- **Paradox test.** Small changes to the ballots of 2,000 elections from Experiments 1 and 2 (160,000 perturbations), checking whether any party or bloc gains votes but loses seats (`paradox_summary.md`).

Rates carry a 95% Monte Carlo margin, clustered by future in Experiment 3.

### Reproducibility

- **All the experimental code, inputs and summary results are public** in the [project's GitHub repository](https://github.com/bjsmith/equalcount). The raw ballot states are too large for the repository and are attached to its latest release.
- **The raw ballot state of every election is stored**, real and simulated: 7 + 5,000 + 5,000 + 3 × 50,000 elections in `runs/<experiment>/records.jsonl.gz`. Each state holds national party × candidate tables, the ballots behind each winner, each electorate's winner and margin, and every system's seat allocation and transfer details.
- **Every measure in this report is computed from those files** by `measures.py`. Changing a measure means recomputing, not rerunning the simulations. Full tables, including everything not shown here, are in `runs/summary_measures.md`, generated by `analyse_measures.py`.

---

## Appendix B. Measures

**Headline measures** (lower is better on every one):

| Measure | Definition |
|---|---|
| House above base | Seats beyond 121 (or 141, or 120); median and maximum |
| Voters whose party vote counts differently | Share of all voters any part of whose party vote is counted for a party other than the one ticked |
| Minority-bloc majority | The bloc with fewer party votes (sub-threshold votes included; centrists counted with their ally) holds a majority of seats; % of elections |
| Bloc seat–vote gap | The difference, in percentage points, between a bloc's share of seats and its share of all party votes. With two blocs this is exactly the Gallagher index computed on blocs. Medians shown; 90th percentiles and paired differences are in `runs/summary_measures.md` |
| Standard Gallagher | Least-squares gap between seat shares and shares of all party votes as cast |
| Adjusted Gallagher | The one-share index with rescued voters (below) |

**The four Gallagher versions**, in increasing order of adjustment:

| Name | Compares seats with | Leans towards | Column in `measures.py` |
|---|---|---|---|
| Standard | All party votes, as cast | Current MMP | `gallagher_all` |
| Qualifying parties | Party votes for parties that won seats | MMP over the Backup Vote | `gallagher_qual` |
| One-share | Each qualifying voter counted once: through the party vote, or through the electorate vote if it elected an MP | The transfer | `os_D_win` |
| Adjusted (one-share + rescued voters) | As one-share, plus sub-threshold voters counted for their winning electorate candidate's party | The reforms, the Backup Vote slightly | `os_C_win` |

Versions of the one-share indices that let *any* qualifying electorate candidate carry a voter's share, not only winners, were computed as a sensitivity check. They are much more permissive and read close to zero for almost every system.

**Properties that matter for reading the results:**
- **The standard index has a floor.** It counts votes for parties below the threshold (about 4% of the vote in Experiment 3), which win no seats under any rule. That floor dominates it: with the transfer at 141, the qualifying-parties index is 0.80 but the standard index is 3.35.
- **The one-share indices are best cases, so they can reach zero.** A Gallagher index on fixed vote shares can't reach zero, because seats are whole numbers. The one-share indices instead pick, among all the ways of counting each voter once, the one that fits the seats best, and fractions of split ballots can absorb the rounding. They read zero in 12–24% of adapting-future elections under the reforms and pure PR, and in 1–2% under MMP. A zero means "consistent with one share per voter", not "perfectly proportional".
- **The one-share indices don't penalise a larger House.** They compare seat *shares* with vote shares. Under MMP the double count shows up as a bigger House that dilutes everyone else, and these indices can't see that, which is why they must be read alongside House size.
- **The minority-bloc majority depends on the yardstick.** Counting sub-threshold votes in the bloc totals (the headline) favours the Backup Vote, which counts exactly those votes. Counting qualifying votes favours the transfer.

The Sainte-Laguë and Loosemore–Hanby indices, bloc deficits in seats on four yardsticks, minority-bloc majority with centrists set aside, and the tails of every measure are in `runs/summary_measures.md`. How the measures were chosen is set out in `measures_deliberations_combined.md`.

---

## Appendix C. Glossary

**MMP (mixed-member proportional).** New Zealand's electoral system since 1996. Each voter casts a party vote and an electorate vote. Party votes decide each party's share of the seats; electorate votes elect local MPs, who count towards their party's share. List MPs fill the rest.
{: #gloss-mmp }

**Overhang.** When a party wins more electorates than its party vote entitles it to. Under current law the party keeps the extra seats and the House grows to fit them, so other parties keep their full share.
{: #gloss-overhang }

**House above base.** How many seats Parliament has beyond its intended size: 120 today, 121 in the simulations (71 electorates plus 50 list seats) or 141 with 20 more list seats. Under current law every overhang seat adds one.
{: #gloss-house }

**Split ballot.** A ballot whose two ticks go to different parties: an electorate vote for one party's candidate and a party vote for another. Often tactical, as when a minor party's supporters tick a larger ally's local candidate; sometimes a personal vote for a popular MP.
{: #gloss-split }

**Split-list strategy.** A deliberate version of splitting: a bloc's main party wins electorates while its supporters give their party votes to a partner. The electorate seats become overhang, and the bloc gains seats beyond its share of the vote.
{: #gloss-splitlist }

**Threshold.** A party needs 5% of the party vote, or one electorate, to share in list seats. Party votes for parties below it elect no one.
{: #gloss-threshold }

**Plurality win.** Winning an electorate with the most votes but well short of half, usually against a divided opposition. Overhang from plurality wins has few split ballots behind it, so the transfer has little to work with.
{: #gloss-plurality }

**Gallagher index.** The standard measure of how far seat shares are from vote shares. Square each party's gap between its percentage of seats and its percentage of votes, add them up, halve the total and take the square root. 0 means seats match votes exactly, which whole seats almost never allow; New Zealand's elections since 2005 score about 1 to 4 on the standard version, which uses all party votes as cast.
{: #gloss-gallagher }

**Adjusted Gallagher index.** A Gallagher index measured against what each voter would contribute if counted exactly once: through their party vote, or through their electorate vote if that vote elected an MP. Voters whose party vote is below the threshold are counted for their winning electorate candidate's party. It is a best case over the ways of counting, so unlike the standard index it can reach zero. It leans towards the reforms and is always shown next to the standard index (Appendix B).
{: #gloss-adj }

**Sainte-Laguë.** The formula New Zealand uses to share out seats in proportion to party votes. The *Sainte-Laguë index* is a proportionality measure built on the same logic. It weights each gap by the party's size, so small parties that are over- or under-represented count heavily.
{: #gloss-sli }

**Bloc.** The group of parties that would govern together: left (Labour, Green, Te Pāti Māori; Opportunity in the simulations) or right (National, ACT, NZ First). The transfer itself doesn't use blocs; they are used only to measure who would govern.
{: #gloss-bloc }

**Minority-bloc majority.** An election in which the bloc with fewer party votes wins a majority of seats. Political scientists also call this a *majority reversal* or *electoral inversion*; this report sometimes says "wrong winner". Sub-threshold votes count towards their bloc's total.
{: #gloss-mbm }

**Bloc seat–vote gap.** The difference, in percentage points, between a bloc's share of seats and its share of party votes. A gap of 2 points means one bloc holds about 2.4 seats more than its vote share at 121 seats. With two blocs this equals the Gallagher index computed on blocs instead of parties.
{: #gloss-blocgap }

**Voters whose party vote counts differently.** The share of all voters any part of whose party vote is counted for a party other than the one they ticked. It is the reforms' direct cost. It counts a voter even when only a fraction of their vote is moved, so it overstates the votes' worth actually moved.
{: #gloss-touched }

**Backup Vote.** An extension of the transfer: at every election, a party vote for a party below the threshold is counted for the voter's electorate candidate's party, if that party is in Parliament.
{: #gloss-bv }

**Fixed ballots.** Tests in which voters cast the same ballots whatever the rules: the real elections from 2005 to 2026, and Experiments 1 and 2. They show what each rule does to a given set of votes, but not how voters would respond to it.
{: #gloss-fixed }

**Experiment 3 (adapting futures).** A behavioural simulation of five future elections, from 2029 to 2041, run 1,000 times from the 2026 result. Between elections, voters and parties change strategy in response to what each system rewarded or punished last time. The responses are rules the author reasoned out and varied in strength, not observed behaviour.
{: #gloss-exp3 }

**Monotonicity paradox.** A party gains party votes and ends up with fewer seats. It can happen under the transfer because extra votes can change how much overhang has to be covered.
{: #gloss-paradox }

---

## Appendix D. Sources

| Source | Contents |
|---|---|
| `overhang-transfer-explainer.md` | Plain-language explainer of the transfer, with 2023 and 2026 worked examples |
| `experiment1_report.md`, `report_experiment2.md`, `report_experiment3.md` | The three experiments in full |
| [Prior art](literature_prior_art.md) | Germany's independents rule, vote linkage, the 2012 and 2023 reviews, the 2026 debate |
| `runs/summary_measures.md` | Every measure, for every system and experiment, from the stored raw results |
| `runs/<experiment>/records.jsonl.gz`, `measures.csv` | Raw ballot states and allocations; derived measures |
| `measures.py`, `analyse_measures.py` | Shared measures and comparator rules; the summary tables |
| `measures_deliberations_combined.md` | How the measures were chosen, and the reasoning behind this report's framing |
| `paradox_summary.md` | Monotonicity test |
| `results_2026.json` | 2026 official result and transfer estimate (split votes estimated) |
| The Spinoff, ["Ten ways to fix MMP, explained"](https://thespinoff.co.nz/politics/19-11-2026/ten-ways-to-fix-mmp-explained) (19 November 2026) and ["In defence of MMP"](https://thespinoff.co.nz/politics/23-11-2026/in-defence-of-mmp) (23 November 2026) | The current debate |
| Independent Electoral Review, Final Report (2023), paras. 4.88–4.103 and 4.106–4.111, Recommendations R9–R10 | The absorption rule and its stated drawbacks; the 60:40 ratio of electorate to list seats |
| Royal Commission on the Electoral System, Report (1986), pp. 126–127 | An ideal House of about 140 seats |
