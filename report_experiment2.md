# Experiment 2: Calibrating to New Zealand elections, 2005–2023

## Summary

Experiment 2 asks how the overhang reforms perform on New Zealand's actual elections, and on synthetic elections that look like them.

It has two parts. **Part A** reruns the seven elections from 2005 to 2023 under every system, using the Electoral Commission's ballot-level split-vote data. **Part B** repeats Experiment 1's Monte Carlo, with 5,000 scenarios, but draws every parameter from what those seven elections show. Where a parameter can't be read directly from the results, such as how much voters split strategically, it was fitted to each election's electorate results by approximate Bayesian computation (ABC).

- **Real overhangs have been small, and every reform handles them.** From 2005 to 2023 overhangs were 0–2 seats. MMP-T and MMP-BV covered every one by transferring 4,000–37,000 party votes. Only one needed absorbing or House growth: the Māori Party's 2011 overhang under MMP-BV.
- **On the actual elections, the reforms change little except where votes were wasted.** Bloc seat deficits were small under every system. The largest, in 2008 (4.4 seats), came from NZ First falling below the threshold, not from overhang. MMP-BV cut it to 3.5 seats.
- **In elections like New Zealand's, overhangs are modest.** The calibrated scenarios have no overhang in a third of cases, a median of 2 seats and a 99th percentile of 10. Most of it (83%) comes from Māori parties.
- **MMP-BV is the clear winner on bloc fairness.** At 121 seats its median bloc seat deficit is 1.1, against 2.1 under MMP and 1.7 under MMP-T. 65% of scenarios need no extra seats to bring both blocs within one seat, and 99% need at most 58. Under MMP, 41% never get there at any size.
- **Most bloc imbalance in realistic elections comes from wasted votes, not overhang.** With no overhang at all, MMP's median bloc deficit is still 1.7 seats; MMP-BV's is 0.9.
- **The cost of MMP-BV is party-level proportionality.** Its Gallagher index is higher (2.1 against MMP's 1.4). In 42% of scenarios no parliament size brings every party within one seat of its raw party-vote share, against 5% under MMP.
- **The reforms almost never do worse than MMP on bloc fairness.** MMP-BV is more than one seat worse in 1% of scenarios and never more than two seats worse.
- **The -X variants make little difference here.** With overhangs this small, the transfer usually covers them. The House grows by at most 5–6 seats under the -X variants, against 18 under MMP.

## Question

Experiment 1 tested the systems across a deliberately wide range of synthetic party systems: 2–5 parties per bloc, blocs from 30:70 to 50:50, and strategic voting anywhere from 0% to 100%. That showed where each rule can fail, but many of its scenarios look nothing like New Zealand. Half had overhangs of 11 seats or more.

Experiment 2 asks two narrower questions:

1. How would each system have handled the elections New Zealand actually had?
2. Across elections that resemble New Zealand's in party structure, geography and voter behaviour, how do the systems compare?

Like Experiment 1, it holds ballots fixed: every system faces the same votes. How voters would respond to each system's incentives is Experiment 3's question.

## Design

### Data

For 2005, 2008, 2011, 2014, 2017, 2020 and 2023, the Electoral Commission publishes a split-vote table for every electorate. Each table records, for each party's voters, how their electorate votes were distributed across the candidates. 2002 and earlier have no per-electorate tables. That is 495 electorate tables, plus 2005's party votes by electorate, which its split-vote tables lack. From them:

- national party votes, the electorates each party won, and the qualifying parties;
- every party's vote share in every electorate;
- the national split-vote table for general and Māori electorates;
- each electorate's candidate vote shares;
- for each party that won electorates, the ballots for its winning candidates, by party vote. These are the pools MMP-T and MMP-BV transfer from.

**Port Waikato 2023:** the poll was cancelled after a candidate died. Its seat is credited to National, which won the by-election, within National's normal allocation. In reality the by-election added a 123rd seat.

**Blocs.** A party that supported a government after the election is in that government's bloc: confidence and supply, or coalition. Any other party is placed by where its voters' general-electorate votes went: towards Labour's candidates, Left; towards National's, Right.

### Systems compared

These are the same ten systems as Experiment 3. In Part A the base size is 120, the size actually used at these elections. In Part B it is 121, as in Experiments 1 and 3.

| System | Rule |
|---|---|
| **MMP** | Current system. Overhanging parties keep their extra electorates and the House grows. |
| **MMP-T** | Overhang Transfer (the explainer's Option 1). Only when a party overhangs: wasted party votes on ballots for its winning candidates count for it, as many as needed; then the same fraction of every split ballot for its winners. Anything left is absorbed within the fixed size. |
| **MMP-BV** | Backup Vote (the explainer's Option 2). At every election, a party vote for a party that doesn't qualify counts for the voter's electorate candidate's party, if that party qualifies. If a party still overhangs: split-ballot transfer, then absorption. |
| **MMP-T-X**, **MMP-BV-X** | As MMP-T / MMP-BV, but overhang the transfer can't cover is handled as under MMP: the party keeps its extra seats and the House grows. |
| **…141** | The same rules with 141 seats (71 electorates, 70 list). Part B only. |

### Part A: the actual elections

Each election is rerun under each system at 120 seats, using its actual votes, electorate winners and split-ballot pools.

As a check, MMP reproduces every Parliament: 121, 122, 121, 121, 120, 120 and 122 seats. The 2023 figure differs from the real 123 only because of the Port Waikato treatment above.

### Part B: the calibrated Monte Carlo

The scenario generator is Experiment 1's:
- 64 general and 7 Māori electorates;
- a left and right bloc, each with a leading party and partners;
- centrists allied to a random bloc;
- sub-threshold minor parties;
- Māori parties standing only in the Māori electorates;
- a random left–right lean and local strength for each party in each electorate;
- ballots built voter by voter.

What changes is where its parameters come from.

#### Parameters measured directly

These are drawn uniformly over the range seen in the seven elections. The bloc split and strategic voting are made symmetric, so neither bloc is favoured.

| Parameter | Drawn from | Seen 2005–2023 |
|---|---|---|
| Left share of Left + Right party vote | 36–64% | 44–64% |
| Parties of 1%+ per bloc, including the leader | resampled from history | left 2–3, right 1–3 |
| Leader's share of its bloc's vote | 70–96% | Labour 70–86%, National 74–100% |
| Centrist parties (NZ First, United Future, TOP) | 1 or 2, as observed; 2.6–8.7% and 1.5–2.7% | as left |
| Parties under 1%, no candidates | 1.2–4.3% in total | 1.2–4.3% |
| Māori parties | 1 (5 elections in 7) or 2 | 1–2 |
| Māori-party share of the Māori electorates' party vote | 12–30% | 12–30% |
| Left–right lean across electorates (log-odds SD) | 0.43–0.53 | 0.43–0.53 |
| Local spread of a party's vote (log SD): leaders / others | 0.06–0.13 / 0.21–0.48 | as left |
| Valid votes per electorate: general / Māori | 33–42k / 18–27k | as left |

**Smaller parties' local support is far more uneven than the big parties'.** After allowing for the left–right lean, a smaller party's local vote varies three to four times as much as Labour's or National's. A party with 9% nationally can poll 20–30% in its best seats. The Greens are the most concentrated (0.33–0.48) and ACT the least (0.21–0.34).

#### Behaviour fitted by approximate Bayesian computation

Strategic and personal voting can't simply be read off the split-vote tables. When a Green voter ticks Labour's candidate, the table doesn't say whether that was strategy or a liking for the local MP. The parameters below were therefore fitted election by election.

**Model.** Each electorate's actual party votes are kept. Only how each party's voters cast their electorate vote is simulated:

| Mechanism | Parameter |
|---|---|
| Personal vote: a share of every party's voters back a candidate they like, spread across the candidates by local strength and a random appeal | π; appeal spread σ_a |
| Strategic voting: a share of each partner party's remaining voters back their bloc leader's candidate | s_q, one per partner party |
| Māori electorates: Labour voters / other Left voters backing the locally strongest Māori-party candidate | s_M / s_Mo |
| Standout candidates: a few smaller-party candidates in their side's stronger seats draw a share d of the voters who would otherwise back their bloc leader. This is the Epsom, Ōhāriu, Wigram and Auckland Central pattern. | number n_st; strength d |

**Fitting.**
1. 200,000 parameter sets were drawn per election from broad prior ranges.
2. Each draw was scored against what actually happened:
   - the national split-vote rows;
   - each electorate's Labour and National candidate shares;
   - the Māori-party candidates' shares in the Māori electorates;
   - the number of general electorates won by parties other than Labour or National, and the top three such vote shares;
   - the number of Māori electorates won by Māori parties.
3. The closest 2% were kept and weighted by closeness.
4. The well-identified parameters were then regression-adjusted (the standard Beaumont–Zhang–Balding correction): π, s_M, s_Mo, and the strategic rates of partner parties with 2%+ of the vote.

Centrists' voters split towards both leaders, which a one-ally rule can't represent. Centrists are therefore simulated but left out of the fit.

**Fitted values** (median [5th–95th percentile]):

| Year | Personal vote π | Māori electorates: Labour voters s_M | Māori electorates: other Left s_Mo | Standouts n_st | Standout strength d |
|---|---|---|---|---|---|
| 2005 | 0.16 [0.16–0.17] | 0.32 [0.31–0.34] | 0.31 [0.26–0.35] | 5 [3–8] | 0.74 [0.56–0.96] |
| 2008 | 0.14 [0.14–0.15] | 0.46 [0.45–0.47] | 0.57 [0.53–0.61] | 5–6 [3–8] | 0.81 [0.59–0.98] |
| 2011 | 0.20 [0.20–0.20] | 0.30 [0.28–0.31] | 0.52 [0.49–0.55] | 3 [1–7] | 0.64 [0.40–0.93] |
| 2014 | 0.18 [0.17–0.18] | 0.29 [0.28–0.31] | 0.37 [0.34–0.40] | 3 [1–7] | 0.63 [0.41–0.92] |
| 2017 | 0.16 [0.16–0.17] | 0.22 [0.21–0.23] | 0.22 [0.18–0.25] | 4 [2–8] | 0.57 [0.36–0.88] |
| 2020 | 0.18 [0.17–0.18] | 0.29 [0.28–0.30] | 0.52 [0.49–0.56] | 4 [1–8] | 0.63 [0.36–0.95] |
| 2023 | 0.12 [0.12–0.13] | 0.43 [0.42–0.44] | 0.80 [0.77–0.80] | 6 [3–8] | 0.73 [0.51–0.94] |
| **All** | **0.16 [0.12–0.20]** | **0.30 [0.22–0.46]** | **0.51 [0.21–0.80]** | **4 [2–8]** | **0.69 [0.41–0.95]** |

Strategic rates for the main partner parties:

| Party | Rate of backing the bloc leader's candidate, by election |
|---|---|
| Greens | 0.69 (2005), 0.59, 0.57, 0.55, 0.61, 0.67, 0.46 (2023) |
| ACT | 0.82 (2008), 0.72 (2020), 0.66 (2023); poorly identified in 2005, 2014 and 2017, when ACT effectively stood only in Epsom |
| Conservatives | 0.42 (2011), 0.51 (2014) |
| NZ Loyal (2023) | about 0.25, with a wide range: its voters mostly backed their own candidates |

The spread of candidate appeal, and the rates for parties under about 2%, are poorly identified. They are used with their full uncertainty.

**Fit.** Re-simulating the fitted parameters reproduces the actual elections closely on the partner parties' splits:

| | Observed (range across years) | Model |
|---|---|---|
| Green voters backing Labour's candidate | 0.47–0.62 | within 0.06 every year |
| ACT voters backing National's candidate | 0.62–0.75 | within 0.05 every year |

It is weaker on electorate wins:
- **Māori parties' Māori-seat wins are over-predicted in 2008, 2011 and 2014.** The worst year is 2014: 4.1 predicted against an actual 1.
- **Labour voters backing a Māori-party candidate run about 5 points high.**
- **Smaller parties' general-electorate wins are under-predicted:** for example 3.3 against 5 in 2023.

#### How the Monte Carlo uses the fits

- Each scenario takes one joint draw of π, s_M, s_Mo, σ_a, n_st and d from a randomly chosen election.
- Each partner and centrist party takes its own strategic rate from a random historical partner party's fitted rate. So a scenario can have an ACT-like partner on one side and a Greens-like or NZ Loyal-like partner on the other.

**Validation** against the seven elections:

| | Calibrated scenarios | 2005–2023 |
|---|---|---|
| Overhang at 121 (120): median / max | 2 / 15 (99th percentile 10) | 1 / 2 |
| Smaller-party general-electorate wins per election | 2.5 | 2.6 |
| Māori-party Māori-electorate wins | 3.6 | 3.0 |
| Votes on ballots wasting both ticks: median | 1.3% | – |

The scenarios' overhangs are a little larger than history's, mainly through the over-prediction of Māori-party seat wins.

### Measures

These match Experiments 1 and 3.

- **Bloc seat deficit:** how many seats the worse-off bloc is short of its share of all party votes, including votes for parties that missed the threshold. Every party belongs to the left or right bloc, and centrists count with their ally.
- **Party seat deficit (rounded):** each qualifying party's shortfall against its share of the qualifying party vote, rounded to whole seats, then summed.
- **Gallagher index:** the conventional measure of party-level disproportionality.
- **Extra seats (b):** the list seats to add beyond the base size so that no bloc is more than one seat short. This uses the bloc yardstick without voters who wasted both ticks.
- **Extra seats (a):** the same, so that no party is more than one seat short.
- **Overhang:** electorates won beyond the party's entitlement on raw party votes at the base size.

## Results

### Part A: the actual elections, 2005–2023 (120 seats)

**Bloc seat deficit (House size where it grows)**

| Year | Overhang | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | Votes transferred: MMP-T / MMP-BV |
|---|---|---|---|---|---|---|---|
| 2005 | Māori Party 1 | 0.1 (121) | 0.5 | 0.5 | 0.5 | 0.5 | 16,978 / 16,307 |
| 2008 | Māori Party 2 | 4.4 (122) | 4.5 | **3.5** | 4.5 | **3.5** | 26,596 / 24,113 |
| 2011 | Māori Party 1 | 0.2 (121) | 0.7 | 0.3 | 0.7 | 0.2 (121) | 13,154 / 13,518 |
| 2014 | United Future 1 | 0.4 (121) | 0.9 | **0.1** | 0.9 | **0.1** | 4,195 / 3,990 |
| 2017 | none | 1.8 | 1.8 | **0.8** | 1.8 | **0.8** | – |
| 2020 | none | 0.2 | 0.2 | 1.2 | 0.2 | 1.2 | – |
| 2023 | Te Pāti Māori 2 | 1.5 (122) | **0.4** | **0.4** | **0.4** | **0.4** | 35,038 / 36,526 |

**Gallagher index**

| Year | MMP | MMP-T | MMP-BV |
|---|---|---|---|
| 2005 | 0.95 | 1.12 | 1.12 |
| 2008 | 1.42 | 1.34 | 1.59 |
| 2011 | 0.84 | 0.93 | 0.92 |
| 2014 | 0.68 | 0.87 | 0.64 |
| 2017 | 0.35 | 0.35 | 0.69 |
| 2020 | 0.37 | 0.37 | 0.83 |
| 2023 | 1.44 | 1.51 | 1.51 |

Seat effects of the transfers were at most one or two seats per party. In 2023, for example, Labour and the Greens each lost one seat under MMP-T and MMP-BV, keeping Te Pāti Māori's six electorates within a 120-seat House. National, ACT and NZ First were unchanged.

### Part B: calibrated Monte Carlo (5,000 scenarios)

**All scenarios, 121 seats**

| Measure | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X |
|---|---|---|---|---|---|
| Bloc seat deficit: median / 90th percentile | 2.1 / 5.1 | 1.7 / 4.5 | **1.1 / 2.7** | 1.7 / 4.6 | **1.1 / 2.7** |
| Blocs within one seat | 25% | 31% | 45% | 30% | **46%** |
| Extra seats (b): none needed | 30% | 37% | 65% | 38% | **67%** |
| Extra seats (b): 90th / 95th / 99th percentile | never / never / never | never / never / never | 10 / 20 / 58 | never / never / never | **9 / 18 / 57** |
| Extra seats (b): never reached within 400 seats | 41% | 35% | **0%** | 35% | **0%** |
| Gallagher: median | **1.4** | 1.6 | 2.1 | 1.5 | 2.1 |
| Party seat deficit (rounded): median / 90th percentile | 2 / 6 | 2 / 6 | 3 / 6 | 2 / 6 | 3 / 6 |
| Extra seats (a): none needed | **48%** | 45% | 27% | 45% | 27% |
| Extra seats (a): never reached within 400 seats | **5%** | 9% | 42% | 9% | 42% |
| House: median / max | 123 / 139 | 121 | 121 | 122 / 127 | 122 / 126 |

**All scenarios, 141 seats**

| Measure | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|
| Bloc seat deficit: median / 90th percentile | 2.2 / 5.5 | 1.8 / 5.1 | **1.1 / 2.8** | 1.8 / 5.1 | **1.0 / 2.9** |
| Blocs within one seat | 24% | 29% | **48%** | 30% | **48%** |
| Gallagher: median | **0.9** | **0.9** | 1.7 | **0.9** | 1.7 |
| House: median / max | 142 / 151 | 141 | 141 | 141 / 145 | 141 / 145 |

**Median bloc seat deficit at 121, by overhang size**

| Overhang at 121 | Share of scenarios | MMP | MMP-T | MMP-BV |
|---|---|---|---|---|
| None | 34% | 1.7 | 1.7 | **0.9** |
| 1–2 seats | 18% | 1.7 | 1.7 | **0.9** |
| 3–5 seats | 32% | 2.5 | 1.8 | **1.3** |
| 6 or more | 16% | 2.7 | 1.7 | **1.5** |

**Where a reform does worse than MMP on bloc fairness** (share of scenarios where its bloc seat deficit exceeds MMP's at the same size by more than the margin)

| Comparison | > 0 | > 0.5 seat | > 1 seat | > 2 seats |
|---|---|---|---|---|
| MMP-T vs MMP | 18% | 9% | 3% | 0% |
| MMP-BV vs MMP | 13% | 6% | 1% | 0% |
| MMP-T-X vs MMP | 17% | 9% | 3% | 0.1% |
| MMP-BV-X vs MMP | 12% | 6% | 1% | 0% |
| MMP-T141 vs MMP141 | 16% | 9% | 4% | 0% |
| MMP-BV141 vs MMP141 | 12% | 6% | 1% | 0% |

Strategic voting in these scenarios never falls far: the higher bloc's rate is 43–86% in 90% of them. Results barely vary across that range. MMP-BV has its blocs within one seat in 43–50% of scenarios in every band of strategic voting.

### Comparison with Experiment 1

| Bloc seat deficit, 121 seats: median / 90th percentile | MMP | MMP-T | MMP-BV |
|---|---|---|---|
| Experiment 1 (wide synthetic range) | 6.2 / 14.5 | 4.1 / 10.3 | 2.0 / 7.7 |
| Experiment 2 (calibrated to NZ) | 2.1 / 5.1 | 1.7 / 4.5 | 1.1 / 2.7 |

The ranking is the same, but realistic elections are much less extreme. Experiment 1's large failures came from fragmented party systems with heavy one-sided strategic voting, which New Zealand hasn't produced.

## Interpretation

**Overhang has been a small problem so far, and the reforms solve it cheaply.** Every historical overhang was 1–2 seats, and every one was covered by transferring a small share of split ballots: at most about 37,000 votes, or 1.3% of the party vote. Under the reforms the House would have stayed at 120 in every election from 2005 to 2023. Only one case, the Māori Party's 2011 overhang under MMP-BV, could not be fully covered.

**Wasted votes matter more than overhang.** In both the real elections and the calibrated ones, the largest bloc imbalances come from parties falling below the threshold:
- NZ First in 2008;
- the Conservatives in 2011 and 2014;
- TOP, New Conservative and NZ Loyal more recently.

MMP-BV is the only system that addresses this. Its backup vote rescues those voters wherever their electorate vote went to a qualifying ally. That is why it beats MMP-T even in scenarios with no overhang at all.

**MMP-T is a targeted fix.** It does nothing when there is no overhang. When there is one, it holds the bloc deficit roughly flat as the overhang grows (1.7–1.8 seats), while MMP's rises to 2.5–2.7.

**The trade-off for MMP-BV is real and permanent.** Counting backup votes moves seats away from what raw party votes would give each party. A bigger Parliament can't undo that, so the party-level target is never met in 42% of scenarios. This is a choice between two notions of proportionality:
- proportional to the party vote as cast (MMP and MMP-T are closer);
- proportional to voters' qualifying choices across both ticks, by bloc (MMP-BV is closer).

**The fallback rule matters little in realistic conditions.** The -X variants differ from the absorbing versions by at most a few hundredths of a seat at the median here, because transfers usually cover the whole overhang. Experiment 3 shows the fallback matters more once voters respond to the reforms and strategic splitting dries up.

**Te Pāti Māori is the main source of overhang.** 83% of overhang seats in the calibrated scenarios come from Māori parties. That reflects both the structure of the Māori electorates, where turnout is lower and the Māori-party vote is concentrated, and the model's tendency to over-predict Māori-party wins.

## Limitations

- **Fixed behaviour.** As in Experiment 1, voters behave the same way under every system. How behaviour would shift under each system is Experiment 3's subject.
- **Identification.** The ABC separates personal from strategic voting well. It separates the spread of candidate appeal and the standout effects poorly. The rates for small partner parties are wide, and ACT's are poorly identified in years when it stood almost only in Epsom.
- **Fit gaps:**
  - Māori-party Māori-seat wins are over-predicted for 2008–2014, and Labour voters backing Māori-party candidates by about 5 points. That probably makes the calibrated overhangs somewhat larger than reality.
  - Smaller parties' general-electorate wins are under-predicted in some years.
- **Model simplifications:**
  - Māori electorates vote only for Māori and Left parties, and Māori parties get no votes elsewhere.
  - Centrists are allied to one bloc at random, and are not fitted.
  - Parties under 0.5% are pooled.
  - A party counts as standing in an electorate only if its candidate got at least 1%.
- **Data:**
  - The split-vote tables are given as percentages, so counts can be off by a vote or two.
  - TOP's candidates are filed under "TOP" in the saved data, so TOP's split-vote row isn't used. TOP never qualified, so seat results are unaffected.
  - Port Waikato 2023 is treated as described above.
- **Bloc assignments are judgement calls** where a party supported neither government. Those parties are placed by their voters' electorate votes.

## Reproducing

| File | Contents |
|---|---|
| `data/raw/history/<year>.json` | Per-election data built from the Electoral Commission's split-vote tables |
| `mc_history.py` | Part A: every system on the actual elections → `results_history.json` |
| `calibrate_history.py` | Directly measured parameters → `calibration.json` |
| `abc_history.py` | ABC fit of the behavioural parameters → `abc_posterior.json`, `abc_summary.md` (draws cached in `abc_cache/`) |
| `mc_calibrated.py` | Part B: calibrated scenario generator and runner → `mc_results_calibrated.csv` |
| `mc_analyse.py` | Summary tables → `mc_summary_calibrated.md` |
| `mc_overhang.py` | Seat rules and measures shared with Experiments 1 and 3 |

```bash
python3 mc_history.py
python3 calibrate_history.py
python3 abc_history.py 200000
python3 mc_calibrated.py run 5000
python3 mc_analyse.py mc_results_calibrated.csv mc_summary_calibrated.md
```
