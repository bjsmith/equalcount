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
- **Extra seats (a) / (b)**: seats to add beyond 121 so that no party (a) / no bloc (b, countable yardstick) is more than one seat short. Searched only for the 121-seat systems; ">279" means not reached within 400 seats.

**Caveat:** voters' strategic behaviour is drawn independently of the system, so how much
strategic voting each system would actually produce is not captured.


## All scenarios (n = 5000)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 2.1 | 1.7 | 1.1 | 1.7 | 1.1 | 2.2 | 1.8 | 1.1 | 1.8 | 1.0 |
| Bloc seat deficit: 90th percentile | 5.1 | 4.5 | 2.7 | 4.6 | 2.7 | 5.5 | 5.1 | 2.8 | 5.1 | 2.9 |
| Bloc seat deficit ≤ 1: share | 25% | 31% | 45% | 30% | 46% | 24% | 29% | 48% | 30% | 48% |
| Party seat deficit (rounded): median | 2 | 2 | 3 | 2 | 3 | 1 | 1 | 3 | 1 | 3 |
| Party seat deficit (rounded): 90th percentile | 6 | 6 | 6 | 6 | 6 | 5 | 5 | 6 | 5 | 6 |
| Gallagher: median | 1.4 | 1.6 | 2.1 | 1.5 | 2.1 | 0.9 | 0.9 | 1.7 | 0.9 | 1.7 |
| House size: median / max | 123 / 139 | 121 / 121 | 121 / 121 | 122 / 127 | 122 / 126 | 142 / 151 | 141 / 141 | 141 / 141 | 141 / 145 | 141 / 145 |
| Extra seats (b) blocs: share needing 0 | 30% | 37% | 65% | 38% | 67% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 25 | 3 | 0 | 3 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 10 | >279 | 9 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 20 | >279 | 18 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 58 | >279 | 57 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 41% | 35% | 0% | 35% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 48% | 45% | 27% | 45% | 27% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 1 | 2 | 103 | 2 | 103 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 202 | 262 | >279 | 262 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 273 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 5% | 9% | 42% | 9% | 42% | – | – | – | – | – |

## Low strategic voting: s_L, s_R and s_M all ≤ 25% (n = 4)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 2.6 | 2.6 | 1.1 | 2.6 | 1.1 | 2.6 | 2.6 | 1.6 | 2.6 | 1.6 |
| Bloc seat deficit: 90th percentile | 3.2 | 3.2 | 2.2 | 3.2 | 2.2 | 3.1 | 3.1 | 2.1 | 3.1 | 2.1 |
| Bloc seat deficit ≤ 1: share | 0% | 0% | 50% | 0% | 50% | 0% | 0% | 25% | 0% | 25% |
| Party seat deficit (rounded): median | 0 | 0 | 2 | 0 | 2 | 1 | 1 | 2 | 1 | 2 |
| Party seat deficit (rounded): 90th percentile | 1 | 1 | 3 | 1 | 3 | 1 | 1 | 3 | 1 | 3 |
| Gallagher: median | 0.4 | 0.4 | 1.1 | 0.4 | 1.1 | 0.4 | 0.4 | 1.2 | 0.4 | 1.2 |
| House size: median / max | 121 / 122 | 121 / 121 | 121 / 121 | 121 / 121 | 121 / 121 | 141 / 141 | 141 / 141 | 141 / 141 | 141 / 141 | 141 / 141 |
| Extra seats (b) blocs: share needing 0 | 0% | 0% | 100% | 0% | 100% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 7 | 7 | 0 | 7 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 0 | >279 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 0 | >279 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 0 | >279 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 25% | 25% | 0% | 25% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 100% | 100% | 75% | 100% | 75% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 0 | 0 | 0 | 0 | 0 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 0 | 0 | >279 | 0 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 0 | 0 | >279 | 0 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | 0 | 0 | >279 | 0 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 0% | 0% | 25% | 0% | 25% | – | – | – | – | – |

## Low bloc strategic voting: s_L and s_R ≤ 25% (any s_M) (n = 39)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 2.2 | 1.2 | 1.3 | 1.2 | 1.3 | 2.0 | 1.4 | 1.2 | 1.4 | 1.2 |
| Bloc seat deficit: 90th percentile | 4.8 | 3.6 | 3.1 | 3.5 | 3.1 | 5.1 | 4.1 | 2.4 | 4.0 | 2.7 |
| Bloc seat deficit ≤ 1: share | 23% | 41% | 44% | 36% | 44% | 23% | 36% | 36% | 36% | 41% |
| Party seat deficit (rounded): median | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 3 |
| Party seat deficit (rounded): 90th percentile | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| Gallagher: median | 1.6 | 1.6 | 2.0 | 1.6 | 2.0 | 1.2 | 1.2 | 1.7 | 1.2 | 1.5 |
| House size: median / max | 123 / 127 | 121 / 121 | 121 / 121 | 122 / 125 | 122 / 125 | 143 / 147 | 141 / 141 | 141 / 141 | 142 / 144 | 142 / 144 |
| Extra seats (b) blocs: share needing 0 | 18% | 36% | 59% | 31% | 64% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 50 | 3 | 0 | 3 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 18 | >279 | 15 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 22 | >279 | 19 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 25 | >279 | 24 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 38% | 38% | 0% | 38% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 38% | 38% | 23% | 38% | 23% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 1 | 6 | 125 | 6 | 125 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | >279 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 10% | 18% | 38% | 18% | 38% | – | – | – | – | – |

## By strategic voting: the higher bloc rate, max(s_L, s_R)

Share of scenarios with a bloc seat deficit ≤ 1 (median bloc deficit in brackets).

| max(s_L, s_R) | n | Overhang at 121: median | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0%–20% | 19 | 2 | 21% (2.0) | 53% (0.8) | 47% (1.2) | 42% (1.1) | 47% (1.2) | 21% (1.9) | 42% (1.3) | 37% (1.3) | 47% (1.4) | 47% (1.2) |
| 20%–40% | 246 | 2 | 31% (1.7) | 33% (1.5) | 50% (1.0) | 33% (1.4) | 52% (0.9) | 26% (1.8) | 33% (1.6) | 54% (0.9) | 33% (1.6) | 54% (0.8) |
| 40%–60% | 1620 | 2 | 24% (2.1) | 29% (1.8) | 43% (1.2) | 29% (1.7) | 43% (1.2) | 22% (2.3) | 30% (1.8) | 44% (1.2) | 29% (1.8) | 45% (1.2) |
| 60%–80% | 2508 | 2 | 25% (2.1) | 32% (1.7) | 47% (1.1) | 31% (1.7) | 48% (1.1) | 24% (2.2) | 29% (1.8) | 49% (1.0) | 29% (1.8) | 50% (1.0) |
| 80%–100% | 609 | 2 | 23% (2.1) | 29% (1.8) | 45% (1.1) | 28% (1.8) | 46% (1.1) | 23% (2.2) | 30% (1.9) | 48% (1.0) | 29% (2.0) | 48% (1.0) |

## Where a reform does worse than the current system on bloc fairness

Share of scenarios where the reform's bloc seat deficit exceeds the current system's (same size) by more than the margin shown.

| Comparison | > 0 | > 0.5 seat | > 1 seat | > 2 seats | > 3 seats |
|---|---|---|---|---|---|
| MMP-T vs MMP | 18% | 9% | 3% | 0% | 0% |
| MMP-BV vs MMP | 13% | 6% | 1% | 0% | 0% |
| MMP-T141 vs MMP141 | 16% | 9% | 4% | 0% | 0% |
| MMP-BV141 vs MMP141 | 12% | 6% | 1% | 0% | 0% |
