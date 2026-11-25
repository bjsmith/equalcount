# Measures deliberations from Experiment 1

Notes on how the measures used in Experiment 1 (the synthetic Monte Carlo comparison of MMP, MMP-T and MMP-BV at 121 and 141 seats; see `experiment1_report.md`) could be improved. None of these changes has been implemented yet.

## Measures used in Experiment 1

| Measure | Yardstick | Notes |
|---|---|---|
| Gallagher index | Party vote (qualifying parties) | Conventional |
| Party seat deficit (rounded) | Party vote | Each party's shortfall rounded to whole seats, then summed |
| Bloc seat deficit | Bloc share of all party votes | Shown for each system |
| Extra seats (a) | Party vote | Seats to add until no party is more than one seat short; searched to 400 seats |
| Extra seats (b) | Countable bloc share (excludes voters who wasted both ticks) | Seats to add until no bloc is more than one seat short |

Problems found while using these:

- **The two bloc yardsticks are mixed.** The bloc deficit uses all party votes, but extra seats (b) uses the countable version. Both systems are penalised for voters no rule can count.
- **Rounding hides near misses.** A shortfall of 0.4 seats counts as zero, and 0.6 as a whole seat.
- **The deficits only measure under-representation**, never who is over-represented.
- **The extra-seats figures are censored at 400 seats** (">279"), and they blend two different things:
  - overhang, which a larger House can fix
  - permanent reassignment, which it can't. For example, MMP-BV's backup votes mean it never reaches test (a) at any size.
- **No measure captures the political stakes** (who forms the government) or **the cost of the reforms** (how many party votes they override).

## 1. A principle-aligned measure: "either vote" proportionality

**Aim:** measure what the proposal sets out to do. Every voter counts once, for either their party vote or their electorate vote.

### The circular version (not recommended as evidence)

"Count each voter for their party vote if that party qualifies, otherwise for their electorate candidate's party" is MMP-BV's counting rule word for word. It was tried in Experiment 1 as the "voter-share yardstick" and dropped. A system scored against its own rule will look nearly perfect by construction, and reviewers would rightly discount it.

### Recommended version: the dual-choice deficit

Ask whether there is any way to count each voter exactly once, for either of their own two choices, that reproduces the seat result:

- Each ballot is a pair: party vote *q* and electorate candidate's party *c*.
- Its single share may be assigned to *q* or to *c*, provided that party qualifies. Shares can be split fractionally across many identical ballots.
- Voters for whom neither choice qualifies are left out.
- The **dual-choice deficit** is the smallest party seat deficit (or Gallagher index) achievable over all such assignments. It's a small linear programme per scenario, essentially a transportation problem.

**Advantages:**
- **It matches the principle**, not any one rule, so MMP, MMP-T, MMP-BV and the Review's absorption rule are all judged against the same standard.
- **It tests the double-counting claim directly.** An overhang seat under the current system has to be supported by voters' shares. The only shares available come from split ballots whose party votes already count elsewhere. Where overhang exists, no assignment covers every seat, and the deficit shows it.
- **It isolates the reforms' remaining failures.** Absorbed overhang produces seats that no assignment supports. These are the plurality sweeps and the Māori-party overhangs that transfers couldn't cover.

**Caveats:**
- **It's lenient.** With a lot of split voting, many assignments are possible and almost any result passes. It discriminates least in high-strategy scenarios, which is where the reforms already do well. It should always be paired with a cost measure (section 3).
- **Present it as principle-aligned**, alongside the conventional measures, never in place of them.

## 2. Changes to existing measures

| Change | Why |
|---|---|
| **Use one bloc yardstick throughout.** Make the countable bloc share primary, and keep the all-votes version as a secondary line | Removes the mismatch between the shown deficit and the extra-seats test, and stops penalising every system for votes none can count |
| **Add a wrong-majority rate.** The share of scenarios where the bloc with more countable votes fails to win a majority, or a bloc with under 50% wins one | The bloc measure with the highest stakes. A two-seat bloc deficit matters little at 60:40 and decides the government at 50:50 |
| **Replace rounding with a tolerance.** Report the number of parties short by at least one full seat, and the total shortfall above half a seat per party | Stops near misses flipping between 0 and 1 |
| **Add the Loosemore–Hanby index** (half the sum of absolute seat–vote share gaps) | Captures over-representation as well as under-representation. Overhang creates winners as well as losers |
| **Split the extra-seats measure in two:** seats needed to remove overhang, and the permanent disproportionality floor that remains at any size | Separates what a larger House can fix from what it can't |
| **Show extra seats as a curve** (share of scenarios covered at each House size) rather than percentiles with a ">279" cap | Handles censoring honestly, and answers "how big must Parliament be to cover X% of outcomes?" directly |

## 3. New measures to balance the principle-aligned one

**Override rate: the cost of the reforms.** Report two quantities separately:
- **Rescued votes:** party votes for parties that don't qualify that were counted for the voter's electorate choice. This is arguably a benefit, since those votes would otherwise be wasted.
- **Overridden votes:** qualifying party votes moved to the electorate choice by split-ballot transfers. This is the real cost, and the core of the "isn't this disregarding my vote?" objection.

A reform that does well on the dual-choice deficit while overriding 0.5% of votes is a strong result. One that overrides 4% needs that shown.

**Vote weight.**
- Seats per 1,000 votes for each party, and the ratio of the highest to the lowest.
- The most intuitive statement of "everyone counts once".
- Easy to explain to non-specialists, and comparable across Houses of different sizes.

**Minor-party sincerity penalty.**
- The share of small-party supporters who waste both ticks because they voted for their own party's candidate.
- Experiment 1 found this drives most cases where MMP-BV141 does worse than the current system on bloc fairness (types A and B in `mc_worse_cases.md`). Under the backup vote, a small-party supporter who gives their electorate vote to a big ally keeps a counted vote; one who votes for their own candidate doesn't.
- This measures directly whether a rule rewards the strategic electorate voting it is meant to discourage.

## 4. Proposed reporting structure

Group the measures into a scorecard, so no single number carries the argument:

| Family | Measures |
|---|---|
| Conventional proportionality | Gallagher index, Loosemore–Hanby index, parties short by at least one seat |
| Bloc fairness | Countable bloc deficit, wrong-majority rate |
| Principle-aligned | Dual-choice deficit |
| Cost | Override rate (rescued vs overridden), House size, vote-weight ratio, minor-party sincerity penalty |

The case for a reform is then strong if it does well on its own principle at a visible and modest cost, and holds up on the conventional measures. A reform that does well only on the measure written for it won't persuade a sceptical reader.

## Open questions

1. **Should the dual-choice deficit be computed per party or per bloc?** Per party is stricter, but more assignments are possible at bloc level.
2. **Should voters whose party vote is wasted but whose electorate choice qualifies count in the conventional party yardstick?** They count under MMP-BV, not under MMP or MMP-T. The answer changes how much MMP-BV's party-level "disproportionality" is a cost and how much a correction.
3. **For the wrong-majority rate, which bloc do centrist parties count with?** Experiment 1 assigns each to a random ally. A real assessment might need several coalition scenarios per election.
4. **What tolerance is right?** Experiment 1 used one seat for parties and blocs alike. Seats may matter more for blocs (government formation) than for individual parties.
