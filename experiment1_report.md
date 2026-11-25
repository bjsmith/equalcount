# Experiment 1: A synthetic Monte Carlo comparison of overhang rules

## 1.1 Question

Under New Zealand's MMP, a party that wins more electorates than its party vote entitles it to keeps the extra seats ("overhang"), and Parliament grows. Groups of parties can exploit this by splitting their votes. This experiment asks how two proposed rules for handling overhang compare with the current system, across a wide range of possible future party systems and voting behaviour:

1. How proportional is Parliament to the **party vote**, party by party?
2. How proportional is Parliament between the two **blocs** that form governments?
3. How large would Parliament need to be for each rule to stay within one seat of proportional, for any outcome?

## 1.2 Systems compared

Every system is applied to exactly the same ballots in each scenario.

| Name | Size | Rule |
|---|---|---|
| **MMP** | 121 | The current system. Seats are allocated by Sainte-Laguë; a party keeps any electorates beyond its entitlement, and the House grows. |
| **MMP-T** | 121 | **Overhang Transfer.** Applies only when a party overhangs. (1) Party votes for parties that don't qualify, on ballots whose electorate vote elected one of the overhanging party's candidates, are counted for that party, only as many as needed. (2) If that isn't enough, the same fraction *f* of every other split ballot for its winning candidates is counted for it. (3) Any overhang still left is absorbed within the fixed size, with other parties receiving fewer list seats (the Independent Electoral Review's rule). |
| **MMP-BV** | 121 | **Backup Vote.** At every election, a party vote for a party that doesn't qualify is counted for the party of the voter's electorate candidate, if that party qualifies. If a party still overhangs, steps (2) and (3) of MMP-T apply. |
| **MMP141**, **MMP-T141**, **MMP-BV141** | 141 | The same three rules with 20 more list seats. |

All systems use a 5% party-vote threshold, waived for any party that wins an electorate. Qualification is decided on raw party votes before any votes are reassigned, so no party can be pushed out of Parliament by a transfer.

## 1.3 Method

### Scenario generator

Each of 5,000 scenarios builds a synthetic election from scratch. The design deliberately spans far more fragmented party systems than New Zealand has had, so as to stress-test each rule rather than to forecast.

| Element | Specification |
|---|---|
| Parliament | 121 seats (141 for the larger variants); 64 general electorates and 7 Māori electorates |
| Bloc balance | Left : Right vote anywhere from 30:70 to 70:30 (uniform) |
| Parties per bloc | 2–5 general parties in each bloc (uniform), with vote shares drawn at random (flat Dirichlet); "Left 1" and "Right 1" are each bloc's largest party |
| Māori electorate parties | 0–2, in the left bloc, drawing votes only in the Māori electorates; together 10–60% of the party vote there |
| Māori electorates | vote only for Māori electorate parties and general left parties (a simplification) |
| Centrist parties | 0–2, each 2–10% of the general vote, each allied to a randomly chosen bloc |
| Minor parties | 1–10% of the vote in total, split randomly between Left minor, Right minor and Centre minor (allied to a random bloc). They never qualify and stand no candidates; their voters give the electorate vote to their bloc's largest party |
| Geography | each general electorate has a random left–right lean (logit SD 0.4), and each party a random local concentration; national totals are matched by iterative proportional fitting |
| Turnout | about 40,000 valid votes per general electorate; 24,000–30,000 per Māori electorate |

Electorate votes are built ballot by ballot, as a table of party vote × electorate candidate for each electorate:

| Behaviour | Specification |
|---|---|
| Personal vote | a share π (0–15% per scenario) of every party's voters vote for a candidate they like, by random local appeal |
| Strategic: bloc | a share s_L or s_R (0–100% per scenario, independently) of each smaller bloc party's remaining voters give their electorate vote to their bloc's largest party. Centrists use their ally's rate |
| Strategic: Māori | in the Māori electorates, a share s_M (0–100%) of left voters, and of the weaker Māori party's voters, give their electorate vote to the locally strongest Māori party |
| Sincere | everyone else votes for their own party's candidate |

### Measures

**Yardsticks:**
- **Party yardstick:** each qualifying party's share of the qualifying party vote (raw party votes).
- **Bloc yardstick:** each bloc's share of *all* party votes, including its parties that missed the threshold. Every party belongs to a bloc (centrists count with their ally), so the two blocs' fair shares add up to the whole House.
- **Countable bloc yardstick:** the bloc yardstick without voters who wasted both ticks (party vote and electorate vote both for parties that don't qualify). No seat rule can count these voters.

**Measures for each system, at its own size:**
- **Gallagher index**, against the party yardstick.
- **Party seat deficit (rounded):** each party's shortfall against the party yardstick, rounded to whole seats, then summed.
- **Bloc seat deficit:** how many seats the worse-off bloc is short of its fair share, against the bloc yardstick.
- **Extra seats (a) and (b):** the smallest number of seats to add beyond 121 so that (a) no party, or (b) no bloc (countable bloc yardstick), is more than one seat short. This is searched only for the 121-seat systems, up to 400 seats; electorates stay at 71. These figures are not a proposed mechanism; they indicate how large Parliament would have to be to accommodate the range of outcomes.

## 1.4 Results

### Overview of the scenarios

- **Overhang** (raw party votes, 121 seats): median 13 seats. 8% of scenarios have none, and 58% have 11 or more.
- **Māori electorate parties:** present in 66% of scenarios, with a median overhang of 3 seats where present.
- **Voters wasting both ticks:** a median of 2.7% of voters.

### Headline results (all 5,000 scenarios)

| Measure | MMP | MMP-T | MMP-BV | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 6.2 | 4.1 | 2.0 | 5.2 | 3.7 | **1.5** |
| Bloc seat deficit: 90th percentile | 14.5 | 10.3 | 7.7 | 13.5 | 9.7 | **5.1** |
| Bloc seat deficit ≤ 1: share | 9% | 14% | 30% | 11% | 16% | **37%** |
| Party seat deficit (rounded): median | 8 | 13 | 15 | **5** | 6 | 10 |
| Gallagher index: median | 4.4 | 8.2 | 8.8 | **2.6** | 3.5 | 5.2 |
| House size: median (max) | 134 (171) | 121 | 121 | 147 (188) | 141 | 141 |
| Extra seats (b): share needing none | 10% | 16% | **52%** | – | – | – |
| Extra seats (b): median / 95th / 99th percentile | 94 / >279 / >279 | 66 / >279 / >279 | **0 / 32 / 68** | – | – | – |
| Extra seats (b): never reached within 400 seats | 45% | 44% | **0%** | – | – | – |
| Extra seats (a): median | **40** | 48 | >279 | – | – | – |
| Extra seats (a): never reached within 400 seats | **1%** | 3% | 86% | – | – | – |

### Low strategic voting

These are the 285 scenarios where both blocs' strategic rates are at or below 25%:

| Measure | MMP | MMP-T | MMP-BV | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 5.3 | 6.5 | 5.1 | 4.6 | 4.4 | **3.1** |
| Party seat deficit (rounded): median | 6 | 10 | 11 | **4** | 5 | 7 |
| Extra seats (b): median | 58 | 52 | **10** | – | – | – |

**By strategic voting:** share of scenarios with a bloc seat deficit of one seat or less, by the higher of the two blocs' strategic rates:

| max(s_L, s_R) | Scenarios | Overhang at 121: median | MMP | MMP-T | MMP-BV | MMP141 | MMP-T141 | MMP-BV141 |
|---|---|---|---|---|---|---|---|---|
| 0–20% | 174 | 10 | 11% | 9% | 11% | 10% | 11% | 20% |
| 20–40% | 605 | 12 | 10% | 11% | 15% | 13% | 14% | 21% |
| 40–60% | 1,009 | 13 | 10% | 11% | 21% | 11% | 16% | 31% |
| 60–80% | 1,414 | 14 | 9% | 16% | 33% | 12% | 18% | 40% |
| 80–100% | 1,798 | 14 | 8% | 16% | 40% | 10% | 15% | 45% |

### Where a reform does worse than the current system on bloc fairness

Share of scenarios where the reform's bloc seat deficit exceeds that of the current system at the same size by more than the margin shown:

| Comparison | > 0 | > 0.5 seat | > 1 seat | > 2 seats | > 3 seats |
|---|---|---|---|---|---|
| MMP-T vs MMP | 23% | 15% | 10% | 3% | 1% |
| MMP-BV vs MMP | 13% | 8% | 5% | 2% | 1% |
| MMP-T141 vs MMP141 | 20% | 13% | 7% | 2% | 0% |
| MMP-BV141 vs MMP141 | 11% | 7% | 3% | 1% | 0% |

At 121 seats, the cases where MMP-BV is worse share one pattern. A single party of 34–36% sweeps nearly every electorate in a fragmented field, with little strategic voting, while its bloc partners fall below the threshold. Few of its electorate voters split with a qualifying party, so there is little to transfer, and the remaining overhang is absorbed at the other bloc's expense. The current system instead lets the House grow, which happens to spread the overhang.

### Where MMP-BV141 falls short

MMP-BV141 leaves a bloc more than one seat short in 63% of scenarios. Classified by main cause:

| Cause | Share of all scenarios | Bloc seat deficit: median |
|---|---|---|
| **Wasted both ticks.** The countable bloc deficit is ≤ 1, so the whole gap is voters no rule can count | 40% | 2.1 |
| **Overhang absorbed.** An overhang the transfers can't cover is absorbed within 141 seats | 15% | 3.6 |
| **Transfers.** The overhang was covered, but seats still moved between blocs | 7% | 3.1 |
| **Other.** No overhang; some sub-threshold voters' electorate votes went to the other bloc | 1% | 2.7 |

On the countable bloc yardstick, MMP-BV141 is short by more than one seat in 23% of scenarios. The "overhang absorbed" cases have, in medians:
- lower bloc strategic voting (55%, against 77% where MMP-BV141 is within one seat)
- a smaller leading party (26% against 32%), which nonetheless wins 55 of the 71 electorates
- more qualifying parties (7 against 6)
- a larger overhang at 141 seats (14 against 4)
- an absorbed Māori-party overhang (56% against 22%)

In 79% of them, the bloc that ends up short is not the one that overhangs.

**Against the current system:** MMP-BV141 is at least one seat worse than both MMP and MMP141 in 84 scenarios (1.7%). They fall into three types:

| Type | Scenarios | Mechanism |
|---|---|---|
| A | 38 | One bloc has many more voters who wasted both ticks. Under the current system that bloc's overhang (a Māori party's in 18 of 38 cases, a general party's in the rest) happens to offset them with extra seats. MMP-BV141 covers the overhang by transferring votes within the bloc, so the offset disappears. |
| B | 43 | The same imbalance in wasted votes, with no overhang to offset it. One bloc's small-party supporters give their electorate vote to a big ally, so the backup vote counts their party vote. The other bloc's small-party supporters vote for their own candidates, so they waste both ticks. The current system counts neither group, so the imbalance never shows. |
| C | 3 | An overhang, usually a Māori party's, is too large for the transfers to cover even at 141 seats. It is absorbed at the other bloc's expense. |

In types A and B, MMP-BV141 is within about one seat of proportional on the countable bloc yardstick (for example 0.2 and 0.5 seats in the worked cases), while the current system is 2–4 seats short. Leaving out voters who wasted both ticks, MMP-BV141 is at least one seat worse in only 0.7% of scenarios against MMP141, and 0.2% against MMP.

## 1.5 Discussion

1. **There is a trade-off between party and bloc proportionality.**
   - MMP-BV gives the best bloc fairness and the worst proportionality to individual party votes, because it deliberately reassigns wasted party votes at every election.
   - The current system is the reverse: it keeps party votes intact, but lets overhang distort the balance between blocs.
   - MMP-T sits between the two on both measures.
2. **Size does much of the work.**
   - 141 seats improves every rule, mainly by preventing overhangs from arising.
   - MMP-T141 comes close to the current system's party proportionality (median party deficit 6, against 5 for MMP141), at a fixed size, while improving bloc fairness (3.7 against 5.2).
   - MMP-BV141 gives the best bloc fairness of all six systems.
3. **The reforms work best when strategic voting is high.**
   - Both reforms correct overhang by transferring split ballots, so they improve as strategic voting rises.
   - Where little strategic voting occurs, overhangs still arise from plurality wins in fragmented fields, leaving little to transfer. At 121 seats, MMP-T then does slightly worse than the current system on bloc fairness and MMP-BV barely better (median bloc deficit 6.5 and 5.1, against 5.3); at 141, MMP-BV141 does clearly better (3.1 against 4.6 for MMP141).
   - This matters because the reforms are intended to discourage strategic splitting: the world they aim to create is the one in which transfers do least, and Parliament's size matters most.
4. **The backup vote rewards strategic electorate votes by small-party supporters.**
   - A small-party supporter who votes for their own party's local candidate wastes both ticks.
   - One who gives the electorate vote to a big ally keeps their party vote, counted for that ally.
   - This effect accounts for most cases where MMP-BV141 does worse than the current system. It is small in seats, but it runs against the aim of reducing strategic electorate voting.
5. **Māori electorate parties are a recurring source of overhang** that transfers cannot always cover: a party winning several Māori electorates on 1–3% of the party vote.

## 1.6 Limitations

- **Behaviour is independent of the system.** The same ballots are cast under every rule, so how each rule would change strategic voting is not modelled. The distribution of strategic behaviour in each scenario should not be read as a prediction for any particular system.
- **Overhangs are much larger than New Zealand's history** (median 13 seats against 0–4 in real elections). This reflects the deliberately wide, fragmented range of party systems, and both electorate and list seats being fixed. The results describe how the rules behave under stress, not how likely each outcome is.
- **Simplifications:**
  - Māori electorates vote only for Māori electorate parties and left parties.
  - Māori electorate parties get no votes in general electorates.
  - Within-bloc vote shares are drawn from a flat distribution.
  - Minor parties stand no candidates.
  - Strategic voters always back their bloc's largest party nationally, not the locally strongest one.
  - Ballot counts are expected values with no sampling noise.
- **Yardstick choice shapes the comparison.** The party yardstick penalises MMP-BV for its reassignment, by design. The bloc yardstick counts sub-threshold votes that only MMP-BV can use. Both are reported.
- **The extra-seats figures** hold the number of electorates fixed at 71 and search only up to 400 seats.

## 1.7 Reproducibility

| File | Contents |
|---|---|
| `mc_overhang.py` | Scenario generator and seat rules (scenario *k* uses random seed 1000 + *k*) |
| `mc_results.csv` | One row per scenario, all measures (produced by `python3 mc_overhang.py run 5000`) |
| `mc_analyse.py` | Summary tables |
| `mc_diagnose_bv141.py`, `mc_diagnose_bv141.md` | Causes of MMP-BV141 bloc shortfalls |
| `mc_worse_cases.py`, `mc_worse_cases.md` | Scenarios where MMP-BV141 is worse than both MMP and MMP141, with worked examples |

`mc_overhang.py` has since gained further system variants for later experiments. The seat rules for the six systems here are unchanged: recomputing 300 scenarios with the current code reproduces the stored bloc deficits exactly.
