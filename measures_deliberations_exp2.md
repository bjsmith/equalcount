# Measures deliberations: Experiment 2

*Context: Experiment 2 compares MMP, MMP-T (Overhang Transfer), MMP-BV (Backup Vote) and their -X and 141-seat variants. It does so on the actual 2005–2023 elections (Part A) and on 5,000 scenarios calibrated to them (Part B). The full write-up is `report_experiment2.md`.*

## Current measures

| Measure | Yardstick | Notes |
|---|---|---|
| Gallagher index | Each qualifying party's share of the qualifying party vote | Conventional; symmetric |
| Party seat deficit (raw, rounded, max) | Same | Shortfalls only |
| Bloc seat deficit | Each bloc's share of **all** party votes, including those for parties that missed the threshold | Shortfall of the worse-off bloc; centrists count with their ally |
| Extra seats (a) | Party yardstick | Seats to add beyond the base size so that no party is more than one seat short |
| Extra seats (b) | Bloc yardstick, minus voters who wasted both ticks | Seats to add so that no bloc is more than one seat short |
| Overhang, House size | – | At the base size |

## Issue 1: an "either-vote" measure, and the risk of circularity

**Aim:** measure proportionality with respect to *either* the party vote or the electorate vote, which is what the reforms set out to achieve.

There are two ways to define it:

**(a) The backup-vote yardstick.** Each voter counts for their party vote if that party qualifies, otherwise for their electorate candidate's party.
- This is exactly MMP-BV's counting rule. MMP-BV would excel by construction, and a reviewer would rightly call it circular.
- It was tried earlier and dropped. Under MMP and MMP-T it showed bloc gaps that no parliament size could close, because neither system counts votes that way.

**(b) The either-vote envelope (recommended).** Every voter counts exactly once, for either of their two choices, whichever brings the result closest to proportional. The measure is the smallest disproportionality achievable across every such way of counting the voters.

Formally it's a small linear programme:
1. Ballots with both choices for the same party, or only one qualifying choice, count for that party.
2. Split ballots with two qualifying choices can be counted for either party.
3. Ballots with no qualifying choice are left out.
4. Choose how to count each group of split ballots so the seat shares are as close as possible to the vote shares that result.

The inputs are the national party-vote × candidate-party crosstab and the qualifying parties.

Why (b) is better:
- **It isn't built from any system's mechanics.** MMP-T and MMP-BV have to earn their score, and their equal-fraction transfers won't always match the best counting.
- **It credits MMP where deserved.** A small MMP overhang covered by split ballots can score perfectly.
- **It penalises the double count directly.** Under MMP, the overhanging party's extra seats can only be justified by counting split voters for their electorate MP. But those same voters' party votes are also giving the partner its full share. Each voter counts once, so MMP scores badly in exactly the cases where splitting pays.
- **It works at party and bloc level, and at any size.**

Caveats:
- **It's lenient by design.** It shows a result *can* be read as proportional, not that it matches what voters intended with their party vote.
- **It complements the party-vote measures; it doesn't replace them.**
- **The expectation that MMP-T and MMP-BV do very well is a hypothesis, to be tested, not built in.**

## Issue 2: fixes to existing measures

- **Measure excess over the best achievable result.** At 121 seats, rounding alone leaves each party up to half a seat off, and the threshold leaves wasted votes. Report each system's excess over a benchmark: Sainte-Laguë on the same votes and size, ignoring electorates. Then any remaining gap is caused by the overhang rule.
- **Split the bloc deficit into its causes:** threshold (votes for parties that missed it), overhang, and rounding. Experiment 2's main finding, that wasted votes matter more than overhang, should be a measured quantity, not an inference.
- **Extra seats (a) is wrong for MMP-BV.** It can never be met, because the yardstick and the rule disagree permanently: in 42% of calibrated scenarios no size reaches it. Re-basing it on the either-vote envelope makes it well defined for every system.

## Issue 3: measures to add

- **Override rate (the reform's cost).** The share of voters whose party vote ends up counted for another party: through the transfer, the backup vote, or absorption that takes seats from their party. Report it overall and for the worst-hit party. The reform's case is that this cost is small, so it should be measured.
- **Minority-bloc majority.** The bloc with fewer votes holds a majority. Experiment 3 reports this; Experiments 1 and 2 don't. It's the outcome most people care about. Report it with centrists counted with their ally and with them left out.
- **Tail and worst-case measures.** For a constitutional rule, the 95th and 99th percentiles and the worst case matter more than the median. Extra seats already do this; do the same for bloc deficit and House size.
- **Equal vote value.** Compare how many seats each counted voter's share buys, across parties or blocs: the spread of seats per voter (coefficient of variation). It speaks directly to the "counting twice" argument.

## Issue 4: tidying

- **Add the Sainte-Laguë index alongside Gallagher.** Gallagher underweights errors for small parties. The Sainte-Laguë index matches the allocation formula used, and small parties are where the reforms bite.
- **Count surpluses as well as shortfalls.** Deficit measures only count parties that are short, so a bloc that gains seats is invisible unless the other bloc's shortfall shows it. Report bloc surplus and deficit together, or use symmetric measures (Gallagher, Loosemore–Hanby).
- **Make bloc assignment robust.** Centrists' ally is random in the scenarios and a judgement call in the history. Report bloc measures with centrists counted with their ally and with them as a third group, and check that the conclusions hold either way.

## Issue 5: process

- **Fix the set of measures before new runs, and report all of them.** Once a measure is designed around what the reform aims to do, the results only carry weight if the measures were chosen in advance and include ones where the reform is expected to do worse. Party-vote Sainte-Laguë or Gallagher, and the override rate, are those.

## Proposed headline set

| Measure | What it shows |
|---|---|
| Either-vote envelope (party and bloc) | Proportional on "everyone counts once": the reform's principle, measured neutrally |
| Party-vote Sainte-Laguë index and Gallagher | Conventional proportionality, where MMP-BV pays its cost |
| Bloc deficit, split into threshold / overhang / rounding | Whether the rule, rather than the threshold, causes imbalance |
| Minority-bloc majority | The governing-outcome risk |
| Override rate | The reform's cost to voters' party choices |
| House size and extra seats needed (95th / 99th percentile) | Worst-case size of Parliament |

## Open questions

1. Envelope norm: L1 (seats misallocated) or L2 (Gallagher-style)? L1 is easier to interpret, as a number of seats; L2 matches convention.
2. Should the envelope allow ballots with no qualifying choice to count for anything? Proposed: no, they are left out, as in the countable bloc yardstick.
3. Override rate: count only votes moved explicitly (transfer, backup vote), or also seats lost to absorption? Proposed: report both separately.
4. Is minority-bloc majority meaningful when centrists can go either way? Proposed: report both versions, with centrists counted with their ally and with them left out.
5. Should Experiments 1–3 share one measures module, so results are directly comparable? (Recommended.)
