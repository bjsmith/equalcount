# Overhang Monte Carlo: results

5000 synthetic elections (see `mc_overhang.py` for how they are generated).
Every system faces exactly the same ballots in each scenario.

## Systems

| Name | Size | Rule |
|---|---|---|
| **MMP** | 121 | Current system. Overhanging parties keep their extra electorates; the House grows. |
| **MMP-T** | 121 | Overhang Transfer (explainer's Option 1). Only when a party overhangs: wasted party votes on ballots for its winning candidates count for it, as many as needed; then the same fraction of every split ballot for its winners; anything left is absorbed within the fixed size. |
| **MMP-BV** | 121 | Backup Vote (explainer's Option 2). At every election, a party vote for a party that doesn't qualify counts for the voter's electorate candidate's party, if that qualifies. If a party still overhangs: split-ballot transfer, then absorption, as in MMP-T. |
| **MMP-T-X**, **MMP-BV-X** | 121+ | As MMP-T / MMP-BV, but overhang the transfer can't cover is handled as under current MMP: the party keeps its extra seats and the House grows. |
| **MMP141**, **MMP-T141**, **MMP-BV141** | 141 | The same three rules with 141 seats (still 71 electorates). |

## Measures

- **Party yardstick**: each qualifying party's share of the qualifying party vote (raw party votes).
- **Bloc yardstick**: each bloc's share of *all* party votes, including its parties that missed the threshold. Centrists count with their ally.
- **Countable bloc yardstick**: the bloc yardstick without voters who wasted both ticks (used only for extra seats (b)).
- **Bloc seat deficit**: seats the worse-off bloc is short of its fair share, at the system's own size.
- **Party seat deficit (rounded)**: each party's shortfall rounded to whole seats, then summed.
- **Either-choice yardstick**: every voter counts once, for either their party vote or their electorate candidate's party, whichever makes the result most proportional (voters who wasted both ticks are left out; a party vote for a party that doesn't qualify counts for the candidate's party). The either-choice deficits are the smallest achievable over every such assignment.
- **Extra seats (a) / (b)**: seats to add beyond 121 so that no party (a) / no bloc (b, countable yardstick) is more than one seat short. **(c) / (d)**: the same on the either-choice yardstick. Searched only for the 121-seat systems; ">279" means not reached within 400 seats.

**Caveat:** voters' strategic behaviour is drawn independently of the system, so how much
strategic voting each system would actually produce is not captured.


## All scenarios (n = 5000)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 6.2 | 4.1 | 2.0 | 3.8 | 1.8 | 5.2 | 3.7 | 1.5 | 3.6 | 1.4 |
| Bloc seat deficit: 90th percentile | 14.5 | 10.3 | 7.7 | 9.2 | 5.9 | 13.5 | 9.7 | 5.1 | 9.6 | 4.8 |
| Bloc seat deficit ≤ 1: share | 9% | 14% | 30% | 15% | 33% | 11% | 16% | 37% | 16% | 38% |
| Party seat deficit (rounded): median | 8 | 13 | 15 | 13 | 14 | 5 | 6 | 10 | 6 | 10 |
| Party seat deficit (rounded): 90th percentile | 22 | 31 | 31 | 29 | 30 | 19 | 25 | 27 | 25 | 26 |
| Gallagher: median | 4.4 | 8.2 | 8.8 | 7.6 | 8.2 | 2.6 | 3.5 | 5.2 | 3.5 | 5.1 |
| Either-choice party deficit: median | 0.9 | 0.2 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Either-choice max party deficit ≤ 1: share | 69% | 87% | 87% | 94% | 95% | 84% | 98% | 98% | 99% | 99% |
| Either-choice bloc deficit: median | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| House size: median / max | 134 / 171 | 121 / 121 | 121 / 121 | 122 / 146 | 122 / 146 | 147 / 188 | 141 / 141 | 141 / 141 | 141 / 160 | 141 / 160 |
| Extra seats (b) blocs: share needing 0 | 10% | 16% | 52% | 16% | 55% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 94 | 66 | 0 | 66 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 22 | >279 | 20 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 32 | >279 | 30 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 68 | >279 | 66 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 45% | 44% | 0% | 44% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 14% | 11% | 2% | 12% | 2% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 40 | 48 | >279 | 48 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 137 | 165 | >279 | 165 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 175 | 225 | >279 | 225 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 1% | 3% | 86% | 3% | 86% | – | – | – | – | – |
| Extra seats (c) parties, either-choice: share needing 0 | 69% | 87% | 87% | 94% | 95% | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 50th percentile | 0 | 0 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 90th percentile | 29 | 3 | 3 | 0 | 0 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 95th percentile | 47 | 11 | 10 | 2 | 0 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 99th percentile | 84 | 27 | 26 | 17 | 15 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: never reached | 0% | 0% | 0% | 0% | 0% | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: share needing 0 | 60% | 83% | 86% | 90% | 94% | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 50th percentile | 0 | 0 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 90th percentile | 42 | 6 | 4 | 1 | 0 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 95th percentile | 61 | 15 | 12 | 8 | 3 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 99th percentile | 106 | 32 | 28 | 27 | 20 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: never reached | 0% | 0% | 0% | 0% | 0% | – | – | – | – | – |

## Low strategic voting: s_L, s_R and s_M all ≤ 25% (n = 81)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 6.3 | 6.4 | 5.1 | 5.5 | 3.8 | 4.5 | 4.7 | 3.0 | 4.3 | 2.7 |
| Bloc seat deficit: 90th percentile | 11.1 | 11.9 | 10.3 | 10.8 | 8.2 | 11.5 | 11.4 | 7.9 | 11.4 | 6.9 |
| Bloc seat deficit ≤ 1: share | 10% | 7% | 10% | 5% | 11% | 9% | 11% | 20% | 12% | 23% |
| Party seat deficit (rounded): median | 7 | 11 | 11 | 9 | 10 | 2 | 3 | 7 | 3 | 7 |
| Party seat deficit (rounded): 90th percentile | 15 | 22 | 22 | 18 | 18 | 11 | 15 | 16 | 14 | 15 |
| Gallagher: median | 3.6 | 7.0 | 7.0 | 5.7 | 5.8 | 1.4 | 1.9 | 3.9 | 1.9 | 3.5 |
| Either-choice party deficit: median | 1.4 | 2.9 | 2.9 | 1.7 | 1.7 | 0.1 | 0.3 | 0.1 | 0.2 | 0.0 |
| Either-choice max party deficit ≤ 1: share | 70% | 54% | 59% | 72% | 75% | 95% | 91% | 89% | 94% | 98% |
| Either-choice bloc deficit: median | 0.1 | 1.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| House size: median / max | 132 / 155 | 121 / 121 | 121 / 121 | 126 / 144 | 126 / 143 | 144 / 171 | 141 / 141 | 141 / 141 | 142 / 158 | 142 / 157 |
| Extra seats (b) blocs: share needing 0 | 11% | 10% | 27% | 10% | 28% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 55 | 50 | 11 | 49 | 9 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 40 | >279 | 38 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 54 | >279 | 53 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 37% | 36% | 1% | 36% | 1% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 22% | 16% | 6% | 16% | 6% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 20 | 24 | >279 | 23 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 58 | 63 | >279 | 63 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 72 | 88 | >279 | 88 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | 184 | 189 | >279 | 189 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 0% | 0% | 68% | 0% | 68% | – | – | – | – | – |
| Extra seats (c) parties, either-choice: share needing 0 | 70% | 54% | 59% | 72% | 75% | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 50th percentile | 0 | 0 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 90th percentile | 12 | 19 | 21 | 11 | 10 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 95th percentile | 18 | 25 | 23 | 17 | 13 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 99th percentile | 52 | 52 | 52 | 40 | 41 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: never reached | 0% | 0% | 0% | 0% | 0% | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: share needing 0 | 60% | 47% | 56% | 64% | 75% | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 50th percentile | 0 | 1 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 90th percentile | 22 | 23 | 19 | 15 | 13 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 95th percentile | 26 | 29 | 24 | 22 | 14 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 99th percentile | 74 | 66 | 66 | 59 | 61 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: never reached | 0% | 0% | 0% | 0% | 0% | – | – | – | – | – |

## Low bloc strategic voting: s_L and s_R ≤ 25% (any s_M) (n = 285)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 5.3 | 6.5 | 5.1 | 5.2 | 3.9 | 4.6 | 4.4 | 3.1 | 3.9 | 2.5 |
| Bloc seat deficit: 90th percentile | 11.4 | 12.0 | 10.7 | 11.1 | 8.7 | 11.2 | 11.5 | 8.4 | 10.4 | 7.5 |
| Bloc seat deficit ≤ 1: share | 11% | 11% | 12% | 11% | 13% | 12% | 12% | 19% | 14% | 22% |
| Party seat deficit (rounded): median | 6 | 10 | 11 | 9 | 9 | 4 | 5 | 7 | 5 | 7 |
| Party seat deficit (rounded): 90th percentile | 17 | 25 | 25 | 20 | 20 | 13 | 18 | 19 | 16 | 16 |
| Gallagher: median | 3.5 | 6.0 | 6.4 | 5.0 | 5.4 | 2.1 | 2.7 | 3.6 | 2.7 | 3.5 |
| Either-choice party deficit: median | 0.9 | 2.3 | 2.5 | 1.3 | 1.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Either-choice max party deficit ≤ 1: share | 75% | 58% | 60% | 74% | 77% | 93% | 88% | 88% | 94% | 94% |
| Either-choice bloc deficit: median | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| House size: median / max | 131 / 156 | 121 / 121 | 121 / 121 | 125 / 145 | 126 / 145 | 146 / 173 | 141 / 141 | 141 / 141 | 141 / 160 | 142 / 159 |
| Extra seats (b) blocs: share needing 0 | 15% | 14% | 31% | 14% | 33% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 58 | 52 | 10 | 50 | 8 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 43 | >279 | 42 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 57 | >279 | 54 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 86 | >279 | 85 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 40% | 39% | 1% | 39% | 1% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 17% | 13% | 4% | 13% | 5% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 27 | 36 | >279 | 37 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 131 | 157 | >279 | 157 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 152 | 267 | >279 | 267 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 2% | 3% | 76% | 3% | 76% | – | – | – | – | – |
| Extra seats (c) parties, either-choice: share needing 0 | 75% | 58% | 60% | 74% | 77% | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 50th percentile | 0 | 0 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 90th percentile | 16 | 22 | 21 | 12 | 11 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 95th percentile | 28 | 29 | 32 | 20 | 18 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: 99th percentile | 57 | 52 | 52 | 40 | 41 | – | – | – | – | – |
| Extra seats (c) parties, either-choice: never reached | 0% | 0% | 0% | 0% | 0% | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: share needing 0 | 65% | 54% | 59% | 66% | 76% | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 50th percentile | 0 | 0 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 90th percentile | 25 | 26 | 24 | 19 | 13 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 95th percentile | 44 | 37 | 29 | 33 | 18 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: 99th percentile | 67 | 59 | 55 | 55 | 44 | – | – | – | – | – |
| Extra seats (d) blocs, either-choice: never reached | 0% | 0% | 0% | 0% | 0% | – | – | – | – | – |

## By strategic voting: the higher bloc rate, max(s_L, s_R)

Share of scenarios with a bloc seat deficit ≤ 1 (median bloc deficit in brackets).

| max(s_L, s_R) | n | Overhang at 121: median | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0%–20% | 174 | 10 | 11% (5.0) | 9% (6.3) | 11% (5.0) | 9% (5.0) | 13% (3.9) | 10% (4.1) | 11% (4.0) | 20% (3.1) | 13% (3.6) | 22% (2.4) |
| 20%–40% | 605 | 12 | 10% (5.9) | 11% (5.8) | 15% (4.3) | 12% (4.9) | 17% (3.4) | 13% (4.9) | 14% (4.1) | 21% (2.7) | 15% (3.9) | 23% (2.5) |
| 40%–60% | 1009 | 13 | 10% (6.1) | 11% (4.7) | 21% (3.0) | 13% (4.2) | 24% (2.4) | 11% (5.2) | 16% (3.7) | 31% (1.8) | 15% (3.6) | 32% (1.7) |
| 60%–80% | 1414 | 14 | 9% (6.2) | 16% (3.9) | 33% (1.8) | 17% (3.7) | 35% (1.6) | 12% (5.2) | 18% (3.6) | 40% (1.4) | 19% (3.6) | 41% (1.3) |
| 80%–100% | 1798 | 14 | 8% (6.5) | 16% (3.5) | 40% (1.3) | 16% (3.4) | 43% (1.2) | 10% (5.5) | 15% (3.5) | 45% (1.1) | 16% (3.5) | 45% (1.1) |

## Where a reform does worse than the current system on bloc fairness

Share of scenarios where the reform's bloc seat deficit exceeds the current system's (same size) by more than the margin shown.

| Comparison | > 0 | > 0.5 seat | > 1 seat | > 2 seats | > 3 seats |
|---|---|---|---|---|---|
| MMP-T vs MMP | 23% | 15% | 10% | 3% | 1% |
| MMP-BV vs MMP | 13% | 8% | 5% | 2% | 1% |
| MMP-T141 vs MMP141 | 20% | 13% | 7% | 2% | 0% |
| MMP-BV141 vs MMP141 | 11% | 7% | 3% | 1% | 0% |
