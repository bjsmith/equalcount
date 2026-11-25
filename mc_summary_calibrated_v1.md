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
| Bloc seat deficit: median | 2.0 | 1.8 | 1.1 | 1.8 | 1.1 | 2.1 | 1.9 | 1.1 | 1.9 | 1.1 |
| Bloc seat deficit: 90th percentile | 4.9 | 4.6 | 2.7 | 4.6 | 2.7 | 5.4 | 5.1 | 2.9 | 5.1 | 2.9 |
| Bloc seat deficit ≤ 1: share | 27% | 30% | 46% | 30% | 47% | 25% | 29% | 48% | 29% | 48% |
| Party seat deficit (rounded): median | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 | 2 |
| Party seat deficit (rounded): 90th percentile | 5 | 5 | 6 | 5 | 6 | 5 | 5 | 5 | 5 | 5 |
| Gallagher: median | 0.7 | 0.7 | 1.6 | 0.7 | 1.6 | 0.5 | 0.5 | 1.3 | 0.5 | 1.3 |
| House size: median / max | 122 / 137 | 121 / 121 | 121 / 121 | 121 / 128 | 121 / 127 | 141 / 149 | 141 / 141 | 141 / 141 | 141 / 146 | 141 / 145 |
| Extra seats (b) blocs: share needing 0 | 34% | 38% | 70% | 39% | 71% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 7 | 3 | 0 | 3 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 7 | >279 | 7 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 19 | >279 | 18 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 69 | >279 | 67 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 38% | 35% | 0% | 35% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 62% | 57% | 33% | 57% | 34% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 0 | 0 | 7 | 0 | 7 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 123 | 205 | >279 | 205 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 173 | 263 | >279 | 263 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | 275 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 1% | 4% | 32% | 4% | 32% | – | – | – | – | – |

## Low strategic voting: s_L, s_R and s_M all ≤ 25% (n = 10)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 1.8 | 1.8 | 1.2 | 1.8 | 1.2 | 2.1 | 2.1 | 1.2 | 2.1 | 1.2 |
| Bloc seat deficit: 90th percentile | 6.5 | 6.5 | 5.5 | 6.5 | 5.5 | 8.1 | 8.1 | 7.1 | 8.1 | 7.1 |
| Bloc seat deficit ≤ 1: share | 30% | 30% | 30% | 30% | 30% | 30% | 30% | 20% | 30% | 20% |
| Party seat deficit (rounded): median | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 | 0 | 2 |
| Party seat deficit (rounded): 90th percentile | 2 | 2 | 3 | 2 | 3 | 1 | 1 | 3 | 1 | 3 |
| Gallagher: median | 0.4 | 0.4 | 0.9 | 0.4 | 0.9 | 0.3 | 0.3 | 0.8 | 0.3 | 0.8 |
| House size: median / max | 121 / 123 | 121 / 121 | 121 / 121 | 121 / 122 | 121 / 122 | 141 / 142 | 141 / 141 | 141 / 141 | 141 / 141 | 141 / 141 |
| Extra seats (b) blocs: share needing 0 | 50% | 50% | 90% | 50% | 90% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 5 | 5 | 0 | 5 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 3 | >279 | 2 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 3 | >279 | 2 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 3 | >279 | 2 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 40% | 40% | 0% | 40% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 90% | 90% | 50% | 90% | 50% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 0 | 0 | 1 | 0 | 1 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 1 | 5 | >279 | 4 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 1 | 5 | >279 | 4 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | 1 | 5 | >279 | 4 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 0% | 0% | 10% | 0% | 10% | – | – | – | – | – |

## Low bloc strategic voting: s_L and s_R ≤ 25% (any s_M) (n = 62)

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| Bloc seat deficit: median | 1.7 | 1.2 | 1.5 | 1.4 | 1.4 | 1.8 | 1.8 | 1.3 | 1.8 | 1.4 |
| Bloc seat deficit: 90th percentile | 4.4 | 4.0 | 3.1 | 4.0 | 3.0 | 5.0 | 5.0 | 3.4 | 4.7 | 3.6 |
| Bloc seat deficit ≤ 1: share | 31% | 42% | 34% | 40% | 37% | 24% | 29% | 34% | 29% | 35% |
| Party seat deficit (rounded): median | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 1 | 2 |
| Party seat deficit (rounded): 90th percentile | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 |
| Gallagher: median | 0.5 | 0.7 | 1.3 | 0.7 | 1.4 | 0.4 | 0.4 | 1.2 | 0.4 | 1.2 |
| House size: median / max | 122 / 126 | 121 / 121 | 121 / 121 | 121 / 125 | 121 / 125 | 141 / 146 | 141 / 141 | 141 / 141 | 141 / 144 | 141 / 144 |
| Extra seats (b) blocs: share needing 0 | 40% | 50% | 68% | 47% | 69% | – | – | – | – | – |
| Extra seats (b) blocs: 50th percentile | 3 | 1 | 0 | 1 | 0 | – | – | – | – | – |
| Extra seats (b) blocs: 90th percentile | >279 | >279 | 3 | >279 | 2 | – | – | – | – | – |
| Extra seats (b) blocs: 95th percentile | >279 | >279 | 4 | >279 | 4 | – | – | – | – | – |
| Extra seats (b) blocs: 99th percentile | >279 | >279 | 66 | >279 | 64 | – | – | – | – | – |
| Extra seats (b) blocs: never reached | 29% | 26% | 0% | 26% | 0% | – | – | – | – | – |
| Extra seats (a) parties: share needing 0 | 61% | 58% | 35% | 61% | 37% | – | – | – | – | – |
| Extra seats (a) parties: 50th percentile | 0 | 0 | 4 | 0 | 5 | – | – | – | – | – |
| Extra seats (a) parties: 90th percentile | 97 | 155 | >279 | 155 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 95th percentile | 138 | 205 | >279 | 205 | >279 | – | – | – | – | – |
| Extra seats (a) parties: 99th percentile | 204 | >279 | >279 | >279 | >279 | – | – | – | – | – |
| Extra seats (a) parties: never reached | 0% | 2% | 26% | 2% | 26% | – | – | – | – | – |

## By strategic voting: the higher bloc rate, max(s_L, s_R)

Share of scenarios with a bloc seat deficit ≤ 1 (median bloc deficit in brackets).

| max(s_L, s_R) | n | Overhang at 121: median | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0%–20% | 31 | 1 | 35% (1.8) | 45% (1.1) | 29% (1.6) | 42% (1.4) | 35% (1.5) | 29% (1.5) | 29% (1.7) | 19% (1.4) | 29% (1.9) | 23% (1.6) |
| 20%–40% | 292 | 1 | 28% (1.8) | 32% (1.6) | 47% (1.1) | 34% (1.6) | 48% (1.1) | 30% (1.8) | 32% (1.7) | 50% (1.0) | 33% (1.7) | 51% (1.0) |
| 40%–60% | 1621 | 1 | 27% (1.9) | 30% (1.8) | 45% (1.1) | 30% (1.8) | 45% (1.1) | 24% (2.1) | 27% (1.9) | 45% (1.1) | 27% (1.9) | 46% (1.1) |
| 60%–80% | 2584 | 1 | 26% (2.0) | 30% (1.8) | 47% (1.1) | 30% (1.8) | 48% (1.0) | 26% (2.1) | 29% (1.9) | 49% (1.0) | 29% (1.9) | 48% (1.0) |
| 80%–100% | 475 | 1 | 27% (1.8) | 31% (1.7) | 47% (1.1) | 31% (1.7) | 47% (1.1) | 24% (1.9) | 29% (1.8) | 53% (0.9) | 29% (1.8) | 52% (0.9) |

## Where a reform does worse than the current system on bloc fairness

Share of scenarios where the reform's bloc seat deficit exceeds the current system's (same size) by more than the margin shown.

| Comparison | > 0 | > 0.5 seat | > 1 seat | > 2 seats | > 3 seats |
|---|---|---|---|---|---|
| MMP-T vs MMP | 17% | 8% | 2% | 0% | 0% |
| MMP-BV vs MMP | 13% | 6% | 1% | 0% | 0% |
| MMP-T141 vs MMP141 | 14% | 7% | 3% | 0% | 0% |
| MMP-BV141 vs MMP141 | 12% | 6% | 1% | 0% | 0% |
