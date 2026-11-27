# Shared measures across Experiments 1–3

Computed by `measures.py` from the raw ballot states in `runs/<experiment>/records.jsonl.gz` (definitions in the `measures.py` docstring). Scope: current MMP, the transfer family, the 141-seat size increase, and the Review's cap applied at 141. Pure PR appears only as a labelled benchmark for what no overhang rule can fix.

**Headline measures** (main text): House above its base size; voters whose party vote is counted, in whole or in part, for a party other than the one ticked; the most seats any party loses against its raw entitlement; minority-bloc majority (the bloc with fewer party votes holds a majority; centrists with their ally); the standard Gallagher index (all parties, all votes); overhang (raw, at the base size). Lower is better on every one.


## 1. Steps: what each change adds (Experiment 3, voters adapt; 1,000 walks × 5 elections, 2029–2041)

Each row builds on the one before; brackets show the change from the row above.

| System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|
| Current MMP | 11 / 34 | 0.0 / 0.0 | 0 / 0 | 5.7% ±0.7 | 1.70 | 4.82 | 1.37 | 11 |
| 1. + transfer (leftover grows the House) | 1 / 17 (-10.0) | 3.9 / 8.6 (+3.9) | 2 / 12 (+2.0) | 5.9% ±0.7 (+0.2 pts) | 1.82 (+0.13) | 4.67 (-0.15) | 0.65 (-0.72) | 5 (-6) |
| 2. + 20 list seats | 0 / 9 (-1.0) | 0.9 / 8.3 (-3.0) | 1 / 11 (-1.0) | 4.4% ±0.6 (-1.5 pts) | 1.22 (-0.60) | 3.35 (-1.31) | 0.26 (-0.40) | 1 (-4) |
| 3. + Backup Vote | 0 / 10 (+0.0) | 4.0 / 9.5 (+3.1) | 1 / 11 (+0.0) | 3.7% ±0.5 (-0.8 pts) | 1.00 (-0.22) | 3.58 (+0.23) | 0.21 (-0.05) | 2 (+1) |
| Benchmark: pure PR, 3.5% (MMP-pathway ballots) | 0 / 0 (+0.0) | 0.0 / 0.0 (-4.0) | 0 / 0 (-1.0) | 2.9% ±0.4 (-0.7 pts) | 0.70 (-0.30) | 1.61 (-1.97) | 0.24 (+0.03) | 0 (-2) |

The benchmark row's change is against step 3; it is a measurement floor, not an option.

The same steps on fixed ballots (Experiment 2, 5,000 calibrated scenarios; voters don't adapt):

| System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|
| Current MMP | 2 / 18 | 0.0 / 0.0 | 0 / 0 | 6.8% ±0.7 | 1.70 | 3.70 | 0.79 | 2 |
| 1. + transfer (leftover grows the House) | 1 / 6 (-1.0) | 0.9 / 3.7 (+0.9) | 1 / 10 (+1.0) | 5.9% ±0.7 (-0.9 pts) | 1.41 (-0.30) | 3.88 (+0.18) | 0.78 (-0.01) | 2 (+0) |
| 2. + 20 list seats | 0 / 4 (-1.0) | 0.7 / 2.4 (-0.2) | 1 / 7 (+0.0) | 5.8% ±0.6 (-0.1 pts) | 1.29 (-0.12) | 3.50 (-0.38) | 0.55 (-0.23) | 1 (-1) |
| 3. + Backup Vote | 0 / 4 (+0.0) | 5.3 / 8.3 (+4.6) | 1 / 9 (+0.0) | 3.5% ±0.5 (-2.2 pts) | 0.74 (-0.55) | 3.70 (+0.20) | 0.58 (+0.03) | 1 (+0) |

## 2. Size options at 141: does the size increase need a cap?

{no transfer, transfer} × {leftover overhang grows the House, leftover absorbed within 141}, against MMP at 121. Experiment 3; the capped rule without a transfer (Review rule at 141) is applied to the MMP141 pathway's ballots, so its voters are not modelled as adapting to a cap.

| System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 11 / 34 | 0.0 / 0.0 | 0 / 0 | 5.7% ±0.7 | 1.70 | 4.82 | 1.37 | 11 |
| MMP at 141, grows (MMP141) | 6 / 32 | 0.0 / 0.0 | 0 / 1 | 4.2% ±0.6 | 1.33 | 3.84 | 0.92 | 6 |
| MMP at 141, capped (Review rule) | 0 / 0 | 0.0 / 0.0 | 3 / 10 | 6.1% ±0.7 | 1.65 | 4.34 | 1.15 | 6 |
| Transfer at 141, grows (MMP-T-X141) | 0 / 9 | 0.9 / 8.3 | 1 / 11 | 4.4% ±0.6 | 1.22 | 3.35 | 0.26 | 1 |
| Transfer at 141, capped (MMP-T141) | 0 / 0 | 1.7 / 8.6 | 1 / 12 | 4.6% ±0.6 | 1.19 | 3.40 | 0.26 | 3 |

Fixed ballots (Experiment 2):

| System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 2 / 18 | 0.0 / 0.0 | 0 / 0 | 6.8% ±0.7 | 1.70 | 3.70 | 0.79 | 2 |
| MMP at 141, grows (MMP141) | 1 / 10 | 0.0 / 0.0 | 0 / 0 | 6.5% ±0.7 | 1.54 | 3.41 | 0.56 | 1 |
| MMP at 141, capped (Review rule) | 0 / 0 | 0.0 / 0.0 | 1 / 6 | 7.0% ±0.7 | 1.56 | 3.46 | 0.61 | 1 |
| Transfer at 141, grows (MMP-T-X141) | 0 / 4 | 0.7 / 2.4 | 1 / 7 | 5.8% ±0.6 | 1.29 | 3.50 | 0.55 | 1 |
| Transfer at 141, capped (MMP-T141) | 0 / 0 | 0.7 / 2.4 | 1 / 7 | 6.2% ±0.7 | 1.30 | 3.52 | 0.56 | 1 |

## 3. Step 1, the transfer alone: one question per experiment


### Real elections: what would it have done? (2005–2023 at 120 seats, and 2026)

| Year | Overhang | System | House | Voters counted differently % | Most seats lost | Minority-bloc majority | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | One-share |
|---|---|---|---|---|---|---|---|---|---|
| 2005 | 1 | MMP | 121 | 0.00 | 0 | 0 | 1.18 | 0.22 | 0.23 |
| 2005 | 1 | MMP-T-X | 120 | 0.90 | 1 | 0 | 1.29 | 0.26 | 0.26 |
| 2005 | 1 | MMP-BV-X | 120 | 1.57 | 1 | 0 | 1.29 | 0.26 | 0.26 |
| 2008 | 2 | MMP | 122 | 0.00 | 0 | 0 | 3.94 | 0.34 | 0.31 |
| 2008 | 2 | MMP-T-X | 120 | 1.44 | 1 | 0 | 4.03 | 0.13 | 0.23 |
| 2008 | 2 | MMP-BV-X | 120 | 5.89 | 2 | 0 | 3.84 | 0.46 | 0.42 |
| 2011 | 1 | MMP | 121 | 0.00 | 0 | 0 | 2.38 | 0.45 | 0.36 |
| 2011 | 1 | MMP-T-X | 120 | 0.62 | 1 | 0 | 2.32 | 0.53 | 0.42 |
| 2011 | 1 | MMP-BV-X | 121 | 2.59 | 0 | 0 | 2.38 | 0.45 | 0.36 |
| 2014 | 1 | MMP | 121 | 0.00 | 0 | 0 | 3.76 | 0.40 | 0.15 |
| 2014 | 1 | MMP-T-X | 120 | 0.55 | 1 | 0 | 3.68 | 0.52 | 0.25 |
| 2014 | 1 | MMP-BV-X | 120 | 4.03 | 1 | 0 | 3.90 | 0.16 | 0.04 |
| 2017 | 0 | MMP | 120 | 0.00 | 0 | 0 | 2.81 | 0.07 | 0.07 |
| 2017 | 0 | MMP-T-X | 120 | 0.00 | 0 | 0 | 2.81 | 0.07 | 0.07 |
| 2017 | 0 | MMP-BV-X | 120 | 2.91 | 1 | 0 | 2.82 | 0.07 | 0.07 |
| 2020 | 0 | MMP | 120 | 0.00 | 0 | 0 | 4.22 | 0.11 | 0.11 |
| 2020 | 0 | MMP-T-X | 120 | 0.00 | 0 | 0 | 4.22 | 0.11 | 0.11 |
| 2020 | 0 | MMP-BV-X | 120 | 4.11 | 1 | 0 | 4.08 | 0.11 | 0.11 |
| 2023 | 2 | MMP | 122 | 0.00 | 0 | 0 | 2.82 | 0.26 | 0.26 |
| 2023 | 2 | MMP-T-X | 120 | 1.44 | 1 | 0 | 2.96 | 0.37 | 0.37 |
| 2023 | 2 | MMP-BV-X | 120 | 4.54 | 1 | 0 | 2.96 | 0.37 | 0.37 |

One-share differences in the table are House-size granularity, not fit: allocate the transfer-adjusted votes at MMP's House size and the one-share index matches MMP exactly (2023: 0.257 at 122 seats; 2005: 0.226 at 121). Every 2005–2023 overhang was fully covered by the transfer, so its House stays at 120 and the grow fallback never fires.


**2026 official result** (split votes estimated from 2023):

| Rule | House above 120 | Voters whose party vote counts differently | Most seats a party loses | Minority-bloc majority | Bloc seat–vote gap, points | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters, approximate) | One-share (approximate) | Overhang |
|---|---|---|---|---|---|---|---|---|---|
| MMP (current law) | 10 | 0.0% | 0 | no | 1.07 | 3.39 | 0.64 | 0.67 | 10 |
| Transfer, leftover grows (MMP-T-X) | 1 | 12.6% | 3 | no | 0.66 | 4.87 | 0.71 | 0.74 | 10 |
| Transfer, leftover absorbed (MMP-T) | 0 | 12.6% | 4 | no | 0.24 | 5.16 | 0.74 | 0.76 | 10 |

Seats under the transfer-with-growth rule: Labour 34, Green 15, Te Pāti Māori 5, Opportunity 7, National 40, ACT 10, NZ First 10. Overridden party votes (qualifying votes counted for another party): 203,681. Left bloc includes Opportunity, as in Experiment 3; for the bloc seat–vote gap, votes for parties below the threshold are split evenly between the blocs. The one-share indices are approximate: split ballots are estimated only behind National's and Te Pāti Māori's winners.

### Where does it break? (Experiment 1: 5,000 deliberately extreme synthetic elections)

| System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 13 / 50 | 0.0 / 0.0 | 0 / 0 | 9.5% ±0.8 | 4.64 | 8.45 | 1.78 | 13 |
| Transfer, leftover grows (MMP-T-X) | 1 / 25 | 13.1 / 26.4 | 5 / 25 | 7.5% ±0.7 | 3.10 | 10.73 | 1.08 | 13 |
| Transfer, leftover absorbed (MMP-T) | 0 / 0 | 13.1 / 26.4 | 6 / 26 | 8.4% ±0.8 | 3.43 | 11.17 | 1.19 | 13 |

### Typical New Zealand elections (Experiment 2: 5,000 scenarios calibrated to 2005–2023)

| System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 2 / 18 | 0.0 / 0.0 | 0 / 0 | 6.8% ±0.7 | 1.70 | 3.70 | 0.79 | 2 |
| Transfer, leftover grows (MMP-T-X) | 1 / 6 | 0.9 / 3.7 | 1 / 10 | 5.9% ±0.7 | 1.41 | 3.88 | 0.78 | 2 |
| Transfer, leftover absorbed (MMP-T) | 0 / 0 | 0.9 / 3.7 | 1 / 11 | 6.4% ±0.7 | 1.44 | 3.95 | 0.80 | 2 |

### When voters adapt, and if gaming escalates (Experiment 3)

| Scenario | System | House above base: median / max | Voters whose party vote counts differently: median / 90th % | Most seats a party loses: median / max | Minority-bloc majority | Bloc seat–vote gap, points: median | Gallagher (standard) | Gallagher (adjusted: one-share + rescued voters) | Overhang: median |
|---|---|---|---|---|---|---|---|---|---|
| Baseline | MMP (current, 121) | 11 / 34 | 0.0 / 0.0 | 0 / 0 | 5.7% ±0.7 | 1.70 | 4.82 | 1.37 | 11 |
| Baseline | Transfer, leftover grows (MMP-T-X) | 1 / 17 | 3.9 / 8.6 | 2 / 12 | 5.9% ±0.7 | 1.82 | 4.67 | 0.65 | 5 |
| Baseline | MMP at 141, grows (MMP141) | 6 / 32 | 0.0 / 0.0 | 0 / 1 | 4.2% ±0.6 | 1.33 | 3.84 | 0.92 | 6 |
| Baseline | Transfer at 141, grows (MMP-T-X141) | 0 / 9 | 0.9 / 8.3 | 1 / 11 | 4.4% ±0.6 | 1.22 | 3.35 | 0.26 | 1 |
| Copycat | MMP (current, 121) | 12 / 46 | 0.0 / 0.0 | 0 / 0 | 6.2% ±0.7 | 1.75 | 4.89 | 1.39 | 12 |
| Copycat | Transfer, leftover grows (MMP-T-X) | 1 / 17 | 3.9 / 8.6 | 2 / 12 | 5.9% ±0.7 | 1.82 | 4.67 | 0.65 | 5 |
| Copycat | MMP at 141, grows (MMP141) | 7 / 42 | 0.0 / 0.0 | 0 / 0 | 4.4% ±0.6 | 1.36 | 3.90 | 0.93 | 7 |
| Copycat | Transfer at 141, grows (MMP-T-X141) | 0 / 9 | 0.9 / 8.3 | 1 / 11 | 4.4% ±0.6 | 1.22 | 3.35 | 0.26 | 1 |
| Escalation | MMP (current, 121) | 20 / 60 | 0.0 / 0.0 | 0 / 0 | 9.6% ±0.9 | 2.80 | 6.88 | 1.60 | 20 |
| Escalation | Transfer, leftover grows (MMP-T-X) | 1 / 17 | 3.9 / 8.6 | 2 / 12 | 5.9% ±0.7 | 1.82 | 4.67 | 0.65 | 5 |
| Escalation | MMP at 141, grows (MMP141) | 15 / 57 | 0.0 / 0.0 | 0 / 0 | 8.0% ±0.8 | 2.04 | 5.18 | 1.07 | 15 |
| Escalation | Transfer at 141, grows (MMP-T-X141) | 0 / 9 | 0.9 / 8.3 | 1 / 11 | 4.4% ±0.6 | 1.22 | 3.35 | 0.26 | 1 |

## Box: does the conclusion depend on how proportionality is measured?

Medians, Gallagher form (0 = perfect). The four indices, in increasing adjustment: **Standard**: every party, share of all party votes. **Qualifying parties**: only parties that won seats, against their share of the qualifying vote (what the earlier reports used; leans towards MMP over the Backup Vote). **One-share**: each voter whose party vote counts is counted once, through the party vote or, if it elected someone, the electorate vote (leans towards the transfer, by design). **One-share + rescued voters** (the adjusted Gallagher in the headline tables): as one-share, plus voters whose party vote missed the threshold count for their electorate candidate's party if that candidate won (leans towards the Backup Vote).

Also shown: the Sainte-Laguë index (SLI, all votes; the standard index matching the allocation formula, which weights small parties' over- or under-representation heavily) and minority-bloc majority counted on all party votes (headline) and on qualifying party votes.

| Experiment | Comparison | Standard | Qualifying parties | One-share | One-share + rescued voters | SLI | Minority-bloc majority: all votes / qualifying votes |
|---|---|---|---|---|---|---|---|
| Exp 2 history | MMP → MMP-T-X | 2.82 → 2.96 | 0.84 → 0.93 | 0.23 → 0.25 | 0.26 → 0.26 | 6.8 → 7.0 | 0.0% → 0.0% / 0.0% → 0.0% |
| Exp 1 | MMP → MMP-T-X | 8.45 → 10.73 | 4.42 → 7.60 | 1.82 → 1.27 | 1.78 → 1.08 | 19.2 → 25.5 | 9.5% → 7.5% / 8.1% → 5.9% |
| Exp 1 | MMP141 → MMP-T-X141 | 7.24 → 8.14 | 2.59 → 3.46 | 0.89 → 0.55 | 1.40 → 0.84 | 16.9 → 19.4 | 8.1% → 6.5% / 5.7% → 3.6% |
| Exp 2 | MMP → MMP-T-X | 3.70 → 3.88 | 1.37 → 1.54 | 0.50 → 0.48 | 0.79 → 0.78 | 10.4 → 10.7 | 6.8% → 5.9% / 3.0% → 1.5% |
| Exp 2 | MMP141 → MMP-T-X141 | 3.41 → 3.50 | 0.87 → 0.93 | 0.27 → 0.26 | 0.56 → 0.55 | 9.4 → 9.5 | 6.5% → 5.8% / 2.5% → 1.1% |
| Exp 3 | MMP → MMP-T-X | 4.82 → 4.67 | 4.12 → 3.19 | 1.36 → 0.75 | 1.37 → 0.65 | 33.7 → 7.4 | 5.7% → 5.9% / 4.7% → 3.5% |
| Exp 3 | MMP141 → MMP-T-X141 | 3.84 → 3.35 | 3.23 → 0.80 | 0.88 → 0.18 | 0.92 → 0.26 | 26.2 → 6.3 | 4.2% → 4.4% / 4.1% → 1.7% |

Why the standard index moves so little: it counts votes for parties below the threshold (about 4% of the vote in Experiment 3), which win no seats under any rule here. That floor dominates it (with the transfer at 141, the qualifying-parties index is 0.80 but the standard index is 3.35), so differences between overhang rules show up mainly in the adjusted indices.


Caveat: the one-share indices (and to a lesser extent the standard and qualifying-parties indices) reward a larger House through finer rounding. Where MMP's House grows and the transfer's doesn't, part of any MMP advantage on them is that granularity, not a better fit (see the 2005–2023 note).

## Where the transfer does worse

Every headline and bracket measure on which the transfer (MMP-T-X, or MMP-T-X141) does worse than the same rule without it, on the same elections. Gap = mean of (transfer − counterpart) over paired elections, with a 95% margin; 'worse in' = share of elections where the transfer is worse by more than a small margin. Only gaps whose margin excludes zero are listed.

| Experiment | Comparison | Measure | Counterpart → transfer (centre) | Gap (mean, 95%) | Worse in / better in |
|---|---|---|---|---|---|
| Exp 2 history | MMP → MMP-T-X | Voters counted differently (%) | 0.00 → 0.62 | +0.71 ±0.41 | 71% / 0% |
| Exp 2 history | MMP → MMP-T-X | Most seats a party loses | 0.00 → 1.00 | +0.71 ±0.33 | 71% / 0% |
| Exp 1 | MMP → MMP-T-X | Voters counted differently (%) | 0.00 → 13.14 | +13.39 ±0.26 | 92% / 0% |
| Exp 1 | MMP → MMP-T-X | Most seats a party loses | 0.00 → 5.00 | +6.22 ±0.14 | 91% / 0% |
| Exp 1 | MMP → MMP-T-X | Gallagher, standard | 8.45 → 10.73 | +3.00 ±0.08 | 85% / 3% |
| Exp 1 | MMP → MMP-T-X | Qualifying parties | 4.42 → 7.60 | +3.39 ±0.08 | 88% / 1% |
| Exp 1 | MMP141 → MMP-T-X141 | Voters counted differently (%) | 0.00 → 8.29 | +10.81 ±0.28 | 83% / 0% |
| Exp 1 | MMP141 → MMP-T-X141 | Most seats a party loses | 0.00 → 3.00 | +4.37 ±0.12 | 82% / 0% |
| Exp 1 | MMP141 → MMP-T-X141 | Gallagher, standard | 7.24 → 8.14 | +1.59 ±0.06 | 69% / 6% |
| Exp 1 | MMP141 → MMP-T-X141 | Qualifying parties | 2.59 → 3.46 | +1.90 ±0.06 | 77% / 1% |
| Exp 2 | MMP → MMP-T-X | Voters counted differently (%) | 0.00 → 0.93 | +1.92 ±0.09 | 66% / 0% |
| Exp 2 | MMP → MMP-T-X | Most seats a party loses | 0.00 → 1.00 | +1.15 ±0.03 | 64% / 0% |
| Exp 2 | MMP → MMP-T-X | Gallagher, standard | 3.70 → 3.88 | +0.17 ±0.01 | 45% / 5% |
| Exp 2 | MMP → MMP-T-X | Qualifying parties | 1.37 → 1.54 | +0.19 ±0.01 | 50% / 4% |
| Exp 2 | MMP → MMP-T-X | One-share | 0.50 → 0.48 | +0.01 ±0.00 | 27% / 12% |
| Exp 2 | MMP141 → MMP-T-X141 | Voters counted differently (%) | 0.00 → 0.73 | +1.03 ±0.04 | 59% / 0% |
| Exp 2 | MMP141 → MMP-T-X141 | Most seats a party loses | 0.00 → 1.00 | +1.08 ±0.03 | 59% / 0% |
| Exp 2 | MMP141 → MMP-T-X141 | Gallagher, standard | 3.41 → 3.50 | +0.06 ±0.00 | 38% / 6% |
| Exp 2 | MMP141 → MMP-T-X141 | Qualifying parties | 0.87 → 0.93 | +0.08 ±0.00 | 44% / 4% |
| Exp 3 | MMP → MMP-T-X | Voters counted differently (%) | 0.00 → 3.88 | +4.05 ±0.09 | 79% / 0% |
| Exp 3 | MMP → MMP-T-X | Most seats a party loses | 0.00 → 2.00 | +1.82 ±0.05 | 79% / 0% |
| Exp 3 | MMP → MMP-T-X | Bloc seat–vote gap (points) | 1.70 → 1.82 | +0.08 ±0.05 | 50% / 46% |
| Exp 3 | MMP141 → MMP-T-X141 | Voters counted differently (%) | 0.00 → 0.92 | +2.55 ±0.11 | 55% / 0% |
| Exp 3 | MMP141 → MMP-T-X141 | Most seats a party loses | 0.00 → 1.00 | +1.11 ±0.05 | 55% / 0% |

### Bloc seat–vote gap: paired difference

Mean of (transfer − counterpart) in percentage points over the same elections, with its standard error (Experiment 3: clustered by walk) and 95% margin. Positive means the transfer's gap is wider.

| Experiment | Comparison | Median gap: counterpart → transfer | Mean difference | SE | 95% margin |
|---|---|---|---|---|---|
| Exp 2 history | MMP → MMP-T-X | 0.35 → 0.56 | +0.05 | 0.16 | ±0.31 |
| Exp 1 | MMP → MMP-T-X | 4.64 → 3.10 | -1.47 | 0.03 | ±0.06 |
| Exp 1 | MMP141 → MMP-T-X141 | 3.49 → 2.54 | -0.92 | 0.02 | ±0.05 |
| Exp 2 | MMP → MMP-T-X | 1.70 → 1.41 | -0.25 | 0.01 | ±0.02 |
| Exp 2 | MMP141 → MMP-T-X141 | 1.54 → 1.29 | -0.21 | 0.01 | ±0.02 |
| Exp 3 | MMP → MMP-T-X | 1.70 → 1.82 | +0.08 | 0.03 | ±0.05 |
| Exp 3 | MMP141 → MMP-T-X141 | 1.33 → 1.22 | -0.17 | 0.03 | ±0.05 |

---

# Appendix


### Experiment 3 (baseline): every measure

Medians unless stated. Standard, qualifying parties, one-share, one-share + rescued voters: the four Gallagher-form indices (see the box). LH: Loosemore–Hanby (all votes). SLI: Sainte-Laguë index. Bloc deficits in seats against all votes / qualifying votes / countable votes / one-share. Minority-bloc majority with centrists counted with their ally (all votes / qualifying votes) and with centrists set aside.

| System | n | Standard | Qualifying parties | One-share | One-share + rescued | LH | SLI | Bloc deficit: all / qual / countable / one-share | Bloc seat–vote gap, points: median / 90th | Minority-bloc majority: all / qual / no centrists | House: median / 95th / 99th / max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 5000 | 4.82 | 4.12 | 1.36 | 1.37 | 7.65 | 33.74 | 2.2 / 1.8 / 2.0 / 0.3 | 1.70 / 4.27 | 5.7% ±0.7 / 4.7% ±0.7 / 2.0% ±0.4 | 132 / 144 / 149 / 155 |
| Transfer, leftover grows (MMP-T-X) | 5000 | 4.67 | 3.19 | 0.75 | 0.65 | 6.90 | 7.39 | 2.2 / 1.1 / 1.4 / 0.0 | 1.82 / 4.26 | 5.9% ±0.7 / 3.5% ±0.5 / 1.3% ±0.3 | 122 / 129 / 133 / 138 |
| Transfer, leftover absorbed (MMP-T) | 5000 | 5.03 | 3.73 | 1.13 | 1.08 | 7.77 | 8.14 | 2.5 / 1.3 / 1.6 / 0.0 | 2.07 / 5.28 | 7.8% ±0.8 / 5.5% ±0.7 / 1.8% ±0.4 | 121 / 121 / 121 / 121 |
| Transfer + Backup Vote (MMP-BV-X) | 5000 | 5.01 | 3.63 | 0.97 | 0.85 | 7.44 | 7.83 | 2.0 / 1.2 / 1.2 / 0.0 | 1.63 / 4.03 | 5.8% ±0.7 / 4.0% ±0.6 / 0.9% ±0.3 | 123 / 130 / 134 / 139 |
| Transfer + Backup Vote, absorbed (MMP-BV) | 5000 | 5.50 | 4.30 | 1.42 | 1.31 | 8.55 | 8.78 | 2.4 / 1.5 / 1.5 / 0.2 | 2.00 / 5.39 | 8.0% ±0.8 / 6.4% ±0.7 / 1.6% ±0.4 | 121 / 121 / 121 / 121 |
| MMP at 141, grows (MMP141) | 5000 | 3.84 | 3.23 | 0.88 | 0.92 | 5.51 | 26.24 | 2.0 / 1.9 / 2.0 / 0.4 | 1.33 / 3.62 | 4.2% ±0.6 / 4.1% ±0.6 / 2.5% ±0.5 | 147 / 159 / 164 / 173 |
| MMP at 141, capped (Review rule) | 5000 | 4.34 | 3.54 | 1.11 | 1.15 | 6.49 | 29.80 | 2.3 / 2.0 / 2.2 / 0.5 | 1.65 / 4.34 | 6.1% ±0.7 / 5.8% ±0.7 / 2.7% ±0.5 | 141 / 141 / 141 / 141 |
| Transfer at 141, grows (MMP-T-X141) | 5000 | 3.35 | 0.80 | 0.18 | 0.26 | 5.16 | 6.28 | 1.7 / 0.5 / 0.8 / 0.0 | 1.22 / 3.14 | 4.4% ±0.6 / 1.7% ±0.4 / 1.2% ±0.3 | 141 / 144 / 146 / 150 |
| Transfer at 141, capped (MMP-T141) | 5000 | 3.40 | 1.50 | 0.20 | 0.26 | 5.15 | 5.95 | 1.7 / 0.5 / 0.8 / 0.0 | 1.19 / 3.17 | 4.6% ±0.6 / 2.2% ±0.4 / 1.1% ±0.3 | 141 / 141 / 141 / 141 |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 5000 | 3.58 | 1.52 | 0.18 | 0.21 | 5.38 | 6.48 | 1.4 / 0.8 / 0.6 / 0.0 | 1.00 / 2.65 | 3.7% ±0.5 / 2.3% ±0.4 / 0.8% ±0.3 | 141 / 144 / 147 / 151 |
| Transfer + BV at 141, capped | 5000 | 3.64 | 1.85 | 0.28 | 0.26 | 5.45 | 6.19 | 1.4 / 0.7 / 0.6 / 0.0 | 1.00 / 2.75 | 4.2% ±0.6 / 2.8% ±0.5 / 1.1% ±0.3 | 141 / 141 / 141 / 141 |
| Benchmark: pure PR, 5% | 25000 | 3.05 | 0.42 | 0.13 | 0.24 | 5.02 | 5.31 | 1.6 / 0.3 / 0.6 / 0.0 | 1.33 / 3.52 | 5.3% ±0.6 / 0.6% ±0.1 / 1.4% ±0.3 | 121 / 121 / 121 / 121 |
| Benchmark: pure PR, 3.5% | 25000 | 1.61 | 0.44 | 0.17 | 0.24 | 2.77 | 2.78 | 0.8 / 0.3 / 0.4 / 0.0 | 0.70 / 2.17 | 2.9% ±0.4 / 0.6% ±0.1 / 0.5% ±0.2 | 121 / 121 / 121 / 121 |

Costs and tails.

| System | Overridden % of votes: median / 90th / max | Rescued %: median | Touched %: median / 99th | Worst-hit party's vote moved: median / 90th | A party loses 2+ seats | Bloc deficit (all): 90th / 99th | House > base +5 / +10 / +20 |
|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 5.7 / 9.3 | 87% / 54% / 10% |
| Transfer, leftover grows (MMP-T-X) | 2.60 / 7.24 / 13.35 | 0.28 | 3.88 / 11.78 | 7.6% / 22.1% | 54% | 5.3 / 8.3 | 12% / 2% / 0% |
| Transfer, leftover absorbed (MMP-T) | 2.96 / 7.47 / 13.45 | 0.29 | 4.20 / 11.76 | 7.8% / 22.0% | 70% | 6.4 / 9.4 | 0% / 0% / 0% |
| Transfer + Backup Vote (MMP-BV-X) | 3.02 / 7.38 / 13.37 | 1.90 | 5.77 / 12.78 | 8.9% / 24.6% | 63% | 5.1 / 7.7 | 16% / 3% / 0% |
| Transfer + Backup Vote, absorbed (MMP-BV) | 3.38 / 7.59 / 13.46 | 1.86 | 6.07 / 12.74 | 8.8% / 24.9% | 76% | 6.5 / 9.6 | 0% / 0% / 0% |
| MMP at 141, grows (MMP141) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 5.4 / 9.3 | 74% / 25% / 2% |
| MMP at 141, capped (Review rule) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 91% | 6.1 / 9.9 | 0% / 0% / 0% |
| Transfer at 141, grows (MMP-T-X141) | 0.34 / 4.25 / 12.56 | 0.00 | 0.92 / 11.78 | 1.0% / 11.8% | 32% | 4.4 / 7.9 | 1% / 0% / 0% |
| Transfer at 141, capped (MMP-T141) | 1.20 / 4.87 / 12.86 | 0.02 | 1.73 / 11.80 | 3.7% / 12.7% | 45% | 4.5 / 8.2 | 0% / 0% / 0% |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 0.89 / 4.64 / 12.62 | 1.93 | 4.00 / 12.79 | 2.7% / 13.8% | 41% | 3.7 / 6.2 | 1% / 0% / 0% |
| Transfer + BV at 141, capped | 1.52 / 5.13 / 13.28 | 1.91 | 4.39 / 12.74 | 4.5% / 14.5% | 52% | 3.9 / 6.8 | 0% / 0% / 0% |
| Benchmark: pure PR, 5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 4.3 / 7.5 | 0% / 0% / 0% |
| Benchmark: pure PR, 3.5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 2.6 / 4.7 | 0% / 0% / 0% |

### Experiment 3 (baseline): paired comparisons

Share of the same elections where the first system is better / worse than the second by more than a small margin (0.05 on the indices, 0.5 seats on bloc deficit, 1 seat on House size).

| Comparison | Standard | Qualifying parties | One-share | Bloc deficit | House smaller / larger |
|---|---|---|---|---|---|
| MMP-T-X vs MMP | 53% / 44% | 67% / 32% | 62% / 33% | 41% / 37% | 98% / 1% |
| MMP-T-X141 vs MMP141 | 67% / 29% | 82% / 17% | 75% / 18% | 50% / 32% | 99% / 0% |
| MMP-T vs MMP | 45% / 52% | 53% / 45% | 52% / 44% | 35% / 44% | 99% / 0% |
| MMP-BV-X vs MMP-T-X | 20% / 67% | 18% / 66% | 22% / 41% | 30% / 17% | 5% / 29% |
| MMP-BV-X141 vs MMP-T-X141 | 17% / 67% | 14% / 68% | 24% / 27% | 34% / 14% | 2% / 8% |
| CMP-Review141 vs MMP141 | 1% / 87% | 1% / 91% | 5% / 84% | 24% / 39% | 99% / 0% |
| MMP-T141 vs MMP-T-X141 | 50% / 39% | 25% / 60% | 31% / 38% | 25% / 21% | 32% / 0% |

### Experiment 3 (escalation): every measure

Medians unless stated. Standard, qualifying parties, one-share, one-share + rescued voters: the four Gallagher-form indices (see the box). LH: Loosemore–Hanby (all votes). SLI: Sainte-Laguë index. Bloc deficits in seats against all votes / qualifying votes / countable votes / one-share. Minority-bloc majority with centrists counted with their ally (all votes / qualifying votes) and with centrists set aside.

| System | n | Standard | Qualifying parties | One-share | One-share + rescued | LH | SLI | Bloc deficit: all / qual / countable / one-share | Bloc seat–vote gap, points: median / 90th | Minority-bloc majority: all / qual / no centrists | House: median / 95th / 99th / max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 5000 | 6.88 | 6.55 | 1.61 | 1.60 | 11.36 | 35.41 | 3.9 / 3.2 / 3.5 / 1.6 | 2.80 / 6.60 | 9.6% ±0.9 / 8.3% ±0.8 / 2.7% ±0.5 | 141 / 162 / 169 / 181 |
| Transfer, leftover grows (MMP-T-X) | 5000 | 4.67 | 3.19 | 0.75 | 0.65 | 6.90 | 7.39 | 2.2 / 1.1 / 1.4 / 0.0 | 1.82 / 4.26 | 5.9% ±0.7 / 3.5% ±0.5 / 1.3% ±0.3 | 122 / 129 / 133 / 138 |
| Transfer, leftover absorbed (MMP-T) | 5000 | 5.03 | 3.73 | 1.13 | 1.08 | 7.77 | 8.14 | 2.5 / 1.3 / 1.6 / 0.0 | 2.07 / 5.28 | 7.8% ±0.8 / 5.5% ±0.7 / 1.8% ±0.4 | 121 / 121 / 121 / 121 |
| Transfer + Backup Vote (MMP-BV-X) | 5000 | 5.01 | 3.63 | 0.97 | 0.85 | 7.44 | 7.83 | 2.0 / 1.2 / 1.2 / 0.0 | 1.63 / 4.03 | 5.8% ±0.7 / 4.0% ±0.6 / 0.9% ±0.3 | 123 / 130 / 134 / 139 |
| Transfer + Backup Vote, absorbed (MMP-BV) | 5000 | 5.50 | 4.30 | 1.42 | 1.31 | 8.55 | 8.78 | 2.4 / 1.5 / 1.5 / 0.2 | 2.00 / 5.39 | 8.0% ±0.8 / 6.4% ±0.7 / 1.6% ±0.4 | 121 / 121 / 121 / 121 |
| MMP at 141, grows (MMP141) | 5000 | 5.18 | 4.48 | 1.06 | 1.07 | 8.56 | 27.30 | 3.1 / 2.6 / 2.8 / 1.2 | 2.04 / 5.45 | 8.0% ±0.8 / 7.0% ±0.8 / 2.7% ±0.5 | 156 / 178 / 186 / 198 |
| MMP at 141, capped (Review rule) | 5000 | 7.10 | 6.79 | 1.63 | 1.60 | 11.71 | 36.54 | 4.2 / 3.4 / 3.7 / 1.9 | 2.99 / 7.73 | 11.2% ±1.0 / 10.1% ±0.9 / 3.7% ±0.6 | 141 / 141 / 141 / 141 |
| Transfer at 141, grows (MMP-T-X141) | 5000 | 3.35 | 0.80 | 0.18 | 0.26 | 5.16 | 6.28 | 1.7 / 0.5 / 0.8 / 0.0 | 1.22 / 3.14 | 4.4% ±0.6 / 1.7% ±0.4 / 1.2% ±0.3 | 141 / 144 / 146 / 150 |
| Transfer at 141, capped (MMP-T141) | 5000 | 3.40 | 1.50 | 0.20 | 0.26 | 5.15 | 5.95 | 1.7 / 0.5 / 0.8 / 0.0 | 1.19 / 3.17 | 4.6% ±0.6 / 2.2% ±0.4 / 1.1% ±0.3 | 141 / 141 / 141 / 141 |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 5000 | 3.58 | 1.52 | 0.18 | 0.21 | 5.38 | 6.48 | 1.4 / 0.8 / 0.6 / 0.0 | 1.00 / 2.65 | 3.7% ±0.5 / 2.3% ±0.4 / 0.8% ±0.3 | 141 / 144 / 147 / 151 |
| Transfer + BV at 141, capped | 5000 | 3.64 | 1.85 | 0.28 | 0.26 | 5.45 | 6.19 | 1.4 / 0.7 / 0.6 / 0.0 | 1.00 / 2.75 | 4.2% ±0.6 / 2.8% ±0.5 / 1.1% ±0.3 | 141 / 141 / 141 / 141 |
| Benchmark: pure PR, 5% | 25000 | 3.02 | 0.42 | 0.14 | 0.25 | 4.99 | 5.26 | 1.6 / 0.3 / 0.6 / 0.0 | 1.32 / 3.49 | 5.3% ±0.6 / 0.6% ±0.1 / 1.4% ±0.3 | 121 / 121 / 121 / 121 |
| Benchmark: pure PR, 3.5% | 25000 | 1.60 | 0.44 | 0.18 | 0.25 | 2.77 | 2.77 | 0.8 / 0.3 / 0.4 / 0.0 | 0.70 / 2.16 | 2.9% ±0.4 / 0.6% ±0.1 / 0.5% ±0.2 | 121 / 121 / 121 / 121 |

Costs and tails.

| System | Overridden % of votes: median / 90th / max | Rescued %: median | Touched %: median / 99th | Worst-hit party's vote moved: median / 90th | A party loses 2+ seats | Bloc deficit (all): 90th / 99th | House > base +5 / +10 / +20 |
|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 10.0 / 15.4 | 96% / 81% / 49% |
| Transfer, leftover grows (MMP-T-X) | 2.60 / 7.24 / 13.35 | 0.28 | 3.88 / 11.78 | 7.6% / 22.1% | 54% | 5.3 / 8.3 | 12% / 2% / 0% |
| Transfer, leftover absorbed (MMP-T) | 2.96 / 7.47 / 13.45 | 0.29 | 4.20 / 11.76 | 7.8% / 22.0% | 70% | 6.4 / 9.4 | 0% / 0% / 0% |
| Transfer + Backup Vote (MMP-BV-X) | 3.02 / 7.38 / 13.37 | 1.90 | 5.77 / 12.78 | 8.9% / 24.6% | 63% | 5.1 / 7.7 | 16% / 3% / 0% |
| Transfer + Backup Vote, absorbed (MMP-BV) | 3.38 / 7.59 / 13.46 | 1.86 | 6.07 / 12.74 | 8.8% / 24.9% | 76% | 6.5 / 9.6 | 0% / 0% / 0% |
| MMP at 141, grows (MMP141) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 9.1 / 14.6 | 89% / 64% / 33% |
| MMP at 141, capped (Review rule) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 97% | 10.9 / 16.0 | 0% / 0% / 0% |
| Transfer at 141, grows (MMP-T-X141) | 0.34 / 4.25 / 12.56 | 0.00 | 0.92 / 11.78 | 1.0% / 11.8% | 32% | 4.4 / 7.9 | 1% / 0% / 0% |
| Transfer at 141, capped (MMP-T141) | 1.20 / 4.87 / 12.86 | 0.02 | 1.73 / 11.80 | 3.7% / 12.7% | 45% | 4.5 / 8.2 | 0% / 0% / 0% |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 0.89 / 4.64 / 12.62 | 1.93 | 4.00 / 12.79 | 2.7% / 13.8% | 41% | 3.7 / 6.2 | 1% / 0% / 0% |
| Transfer + BV at 141, capped | 1.52 / 5.13 / 13.28 | 1.91 | 4.39 / 12.74 | 4.5% / 14.5% | 52% | 3.9 / 6.8 | 0% / 0% / 0% |
| Benchmark: pure PR, 5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 4.2 / 7.4 | 0% / 0% / 0% |
| Benchmark: pure PR, 3.5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 2.6 / 4.7 | 0% / 0% / 0% |

### Experiment 2 (calibrated): every measure

Medians unless stated. Standard, qualifying parties, one-share, one-share + rescued voters: the four Gallagher-form indices (see the box). LH: Loosemore–Hanby (all votes). SLI: Sainte-Laguë index. Bloc deficits in seats against all votes / qualifying votes / countable votes / one-share. Minority-bloc majority with centrists counted with their ally (all votes / qualifying votes) and with centrists set aside.

| System | n | Standard | Qualifying parties | One-share | One-share + rescued | LH | SLI | Bloc deficit: all / qual / countable / one-share | Bloc seat–vote gap, points: median / 90th | Minority-bloc majority: all / qual / no centrists | House: median / 95th / 99th / max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 5000 | 3.70 | 1.37 | 0.50 | 0.79 | 5.93 | 10.43 | 2.1 / 0.9 / 1.7 / 0.0 | 1.70 / 4.11 | 6.8% ±0.7 / 3.0% ±0.5 / 1.5% ±0.3 | 123 / 128 / 131 / 139 |
| Transfer, leftover grows (MMP-T-X) | 5000 | 3.88 | 1.54 | 0.48 | 0.78 | 6.30 | 10.68 | 1.7 / 0.6 / 1.4 / 0.0 | 1.41 / 3.75 | 5.9% ±0.7 / 1.5% ±0.3 / 1.1% ±0.3 | 122 / 124 / 125 / 127 |
| Transfer, leftover absorbed (MMP-T) | 5000 | 3.95 | 1.57 | 0.49 | 0.80 | 6.38 | 10.83 | 1.7 / 0.6 / 1.4 / 0.0 | 1.44 / 3.75 | 6.4% ±0.7 / 2.0% ±0.4 / 1.2% ±0.3 | 121 / 121 / 121 / 121 |
| Transfer + Backup Vote (MMP-BV-X) | 5000 | 4.02 | 2.11 | 0.83 | 0.83 | 6.55 | 10.82 | 1.1 / 1.1 / 0.7 / 0.0 | 0.90 / 2.24 | 4.0% ±0.5 / 3.6% ±0.5 / 1.1% ±0.3 | 122 / 124 / 125 / 126 |
| Transfer + Backup Vote, absorbed (MMP-BV) | 5000 | 4.08 | 2.14 | 0.86 | 0.86 | 6.62 | 10.99 | 1.1 / 1.1 / 0.7 / 0.0 | 0.92 / 2.26 | 4.6% ±0.6 / 4.2% ±0.6 / 1.2% ±0.3 | 121 / 121 / 121 / 121 |
| MMP at 141, grows (MMP141) | 5000 | 3.41 | 0.87 | 0.27 | 0.56 | 5.74 | 9.36 | 2.2 / 0.7 / 1.8 / 0.0 | 1.54 / 3.86 | 6.5% ±0.7 / 2.5% ±0.4 / 1.4% ±0.3 | 142 / 147 / 148 / 151 |
| MMP at 141, capped (Review rule) | 5000 | 3.46 | 0.90 | 0.29 | 0.61 | 5.77 | 9.53 | 2.2 / 0.7 / 1.8 / 0.0 | 1.56 / 3.96 | 7.0% ±0.7 / 3.1% ±0.5 / 1.5% ±0.3 | 141 / 141 / 141 / 141 |
| Transfer at 141, grows (MMP-T-X141) | 5000 | 3.50 | 0.93 | 0.26 | 0.55 | 5.89 | 9.48 | 1.8 / 0.4 / 1.4 / 0.0 | 1.29 / 3.58 | 5.8% ±0.6 / 1.1% ±0.3 / 1.2% ±0.3 | 141 / 144 / 144 / 145 |
| Transfer at 141, capped (MMP-T141) | 5000 | 3.52 | 0.93 | 0.26 | 0.56 | 5.89 | 9.53 | 1.8 / 0.4 / 1.4 / 0.0 | 1.30 / 3.60 | 6.2% ±0.7 / 1.5% ±0.3 / 1.2% ±0.3 | 141 / 141 / 141 / 141 |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 5000 | 3.70 | 1.70 | 0.55 | 0.58 | 6.11 | 9.56 | 1.0 / 1.2 / 0.6 / 0.0 | 0.74 / 2.01 | 3.5% ±0.5 / 3.2% ±0.5 / 1.1% ±0.3 | 141 / 144 / 144 / 145 |
| Transfer + BV at 141, capped | 5000 | 3.72 | 1.71 | 0.56 | 0.59 | 6.15 | 9.63 | 1.1 / 1.2 / 0.6 / 0.0 | 0.75 / 2.01 | 3.9% ±0.5 / 3.5% ±0.5 / 1.1% ±0.3 | 141 / 141 / 141 / 141 |
| Benchmark: pure PR, 5% | 5000 | 5.28 | 0.35 | 0.00 | 0.34 | 9.39 | 10.38 | 2.0 / 0.3 / 1.3 / 0.0 | 1.68 / 4.27 | 7.7% ±0.7 / 0.3% ±0.2 / 2.6% ±0.4 | 121 / 121 / 121 / 121 |
| Benchmark: pure PR, 3.5% | 5000 | 3.79 | 0.38 | 0.04 | 0.28 | 6.88 | 7.41 | 1.5 / 0.3 / 1.0 / 0.0 | 1.22 / 3.00 | 6.0% ±0.7 / 0.5% ±0.2 / 1.0% ±0.3 | 121 / 121 / 121 / 121 |

Costs and tails.

| System | Overridden % of votes: median / 90th / max | Rescued %: median | Touched %: median / 99th | Worst-hit party's vote moved: median / 90th | A party loses 2+ seats | Bloc deficit (all): 90th / 99th | House > base +5 / +10 / +20 |
|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 5.1 / 8.4 | 16% / 1% / 0% |
| Transfer, leftover grows (MMP-T-X) | 0.79 / 2.57 / 11.72 | 0.00 | 0.93 / 14.62 | 2.2% / 9.6% | 34% | 4.6 / 7.7 | 0% / 0% / 0% |
| Transfer, leftover absorbed (MMP-T) | 0.79 / 2.57 / 11.72 | 0.00 | 0.93 / 14.62 | 2.2% / 9.6% | 46% | 4.5 / 7.7 | 0% / 0% / 0% |
| Transfer + Backup Vote (MMP-BV-X) | 0.82 / 2.66 / 11.80 | 4.22 | 5.69 / 17.78 | 2.4% / 10.9% | 47% | 2.7 / 4.6 | 0% / 0% / 0% |
| Transfer + Backup Vote, absorbed (MMP-BV) | 0.82 / 2.66 / 11.80 | 4.22 | 5.69 / 17.78 | 2.4% / 10.9% | 60% | 2.7 / 4.6 | 0% / 0% / 0% |
| MMP at 141, grows (MMP141) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 5.5 / 9.3 | 7% / 0% / 0% |
| MMP at 141, capped (Review rule) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 37% | 5.6 / 9.1 | 0% / 0% / 0% |
| Transfer at 141, grows (MMP-T-X141) | 0.52 / 2.29 / 4.55 | 0.00 | 0.73 / 4.41 | 1.5% / 7.4% | 33% | 5.1 / 8.9 | 0% / 0% / 0% |
| Transfer at 141, capped (MMP-T141) | 0.52 / 2.29 / 4.55 | 0.00 | 0.73 / 4.41 | 1.5% / 7.4% | 41% | 5.1 / 8.8 | 0% / 0% / 0% |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 0.57 / 2.31 / 4.71 | 4.22 | 5.31 / 11.76 | 1.6% / 7.5% | 49% | 2.9 / 5.0 | 0% / 0% / 0% |
| Transfer + BV at 141, capped | 0.57 / 2.31 / 4.71 | 4.22 | 5.31 / 11.76 | 1.6% / 7.5% | 58% | 2.8 / 5.0 | 0% / 0% / 0% |
| Benchmark: pure PR, 5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 5.2 / 8.6 | 0% / 0% / 0% |
| Benchmark: pure PR, 3.5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 3.6 / 6.1 | 0% / 0% / 0% |

### Experiment 2: paired comparisons

Share of the same elections where the first system is better / worse than the second by more than a small margin (0.05 on the indices, 0.5 seats on bloc deficit, 1 seat on House size).

| Comparison | Standard | Qualifying parties | One-share | Bloc deficit | House smaller / larger |
|---|---|---|---|---|---|
| MMP-T-X vs MMP | 5% / 45% | 4% / 50% | 12% / 27% | 34% / 9% | 64% / 0% |
| MMP-T-X141 vs MMP141 | 6% / 38% | 4% / 44% | 16% / 19% | 33% / 9% | 59% / 0% |
| MMP-T vs MMP | 6% / 49% | 3% / 54% | 8% / 40% | 34% / 9% | 66% / 0% |
| MMP-BV-X vs MMP-T-X | 12% / 60% | 16% / 60% | 12% / 31% | 57% / 9% | 1% / 9% |
| MMP-BV-X141 vs MMP-T-X141 | 11% / 66% | 14% / 66% | 13% / 36% | 60% / 9% | 0% / 10% |
| CMP-Review141 vs MMP141 | 9% / 31% | 6% / 39% | 6% / 36% | 11% / 10% | 59% / 0% |
| MMP-T141 vs MMP-T-X141 | 9% / 16% | 10% / 24% | 2% / 20% | 6% / 8% | 44% / 0% |

### Experiment 1 (stress test): every measure

Medians unless stated. Standard, qualifying parties, one-share, one-share + rescued voters: the four Gallagher-form indices (see the box). LH: Loosemore–Hanby (all votes). SLI: Sainte-Laguë index. Bloc deficits in seats against all votes / qualifying votes / countable votes / one-share. Minority-bloc majority with centrists counted with their ally (all votes / qualifying votes) and with centrists set aside.

| System | n | Standard | Qualifying parties | One-share | One-share + rescued | LH | SLI | Bloc deficit: all / qual / countable / one-share | Bloc seat–vote gap, points: median / 90th | Minority-bloc majority: all / qual / no centrists | House: median / 95th / 99th / max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 5000 | 8.45 | 4.42 | 1.82 | 1.78 | 13.79 | 19.24 | 6.2 / 4.1 / 5.3 / 3.5 | 4.64 / 10.00 | 9.5% ±0.8 / 8.1% ±0.8 / 5.9% ±0.7 | 134 / 156 / 163 / 171 |
| Transfer, leftover grows (MMP-T-X) | 5000 | 10.73 | 7.60 | 1.27 | 1.08 | 17.59 | 25.49 | 3.8 / 2.0 / 3.0 / 1.5 | 3.10 / 7.41 | 7.5% ±0.7 / 5.9% ±0.7 / 4.6% ±0.6 | 122 / 132 / 138 / 146 |
| Transfer, leftover absorbed (MMP-T) | 5000 | 11.17 | 8.22 | 1.34 | 1.19 | 18.21 | 26.43 | 4.1 / 2.2 / 3.3 / 1.7 | 3.43 / 8.48 | 8.4% ±0.8 / 7.0% ±0.7 / 5.7% ±0.6 | 121 / 121 / 121 / 121 |
| Transfer + Backup Vote (MMP-BV-X) | 5000 | 11.25 | 8.24 | 1.81 | 1.30 | 18.60 | 26.70 | 1.8 / 2.4 / 0.9 / 2.0 | 1.44 / 4.59 | 5.4% ±0.6 / 6.5% ±0.7 / 3.6% ±0.5 | 122 / 133 / 139 / 146 |
| Transfer + Backup Vote, absorbed (MMP-BV) | 5000 | 11.80 | 8.85 | 1.98 | 1.49 | 19.34 | 28.14 | 2.0 / 2.6 / 0.9 / 2.2 | 1.63 / 6.34 | 6.8% ±0.7 / 7.8% ±0.7 / 4.8% ±0.6 | 121 / 121 / 121 / 121 |
| MMP at 141, grows (MMP141) | 5000 | 7.24 | 2.59 | 0.89 | 1.40 | 12.52 | 16.89 | 5.2 / 2.3 / 4.2 / 1.8 | 3.49 / 8.53 | 8.1% ±0.8 / 5.7% ±0.6 / 4.6% ±0.6 | 147 / 171 / 179 / 188 |
| MMP at 141, capped (Review rule) | 5000 | 8.12 | 3.35 | 1.32 | 1.83 | 14.04 | 19.14 | 6.2 / 3.1 / 5.1 / 2.6 | 4.37 / 10.83 | 9.7% ±0.8 / 7.8% ±0.7 / 6.2% ±0.7 | 141 / 141 / 141 / 141 |
| Transfer at 141, grows (MMP-T-X141) | 5000 | 8.14 | 3.46 | 0.55 | 0.84 | 14.53 | 19.40 | 3.6 / 1.2 / 2.7 / 0.7 | 2.54 / 6.73 | 6.5% ±0.7 / 3.6% ±0.5 / 3.4% ±0.5 | 141 / 144 / 150 / 160 |
| Transfer at 141, capped (MMP-T141) | 5000 | 8.20 | 3.51 | 0.56 | 0.86 | 14.61 | 19.64 | 3.7 / 1.2 / 2.7 / 0.8 | 2.61 / 6.87 | 6.9% ±0.7 / 4.1% ±0.5 / 3.7% ±0.5 | 141 / 141 / 141 / 141 |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 5000 | 8.96 | 5.09 | 1.28 | 0.95 | 15.30 | 20.86 | 1.4 / 2.4 / 0.5 / 1.9 | 1.01 / 3.37 | 4.1% ±0.5 / 5.0% ±0.6 / 2.4% ±0.4 | 141 / 145 / 151 / 160 |
| Transfer + BV at 141, capped | 5000 | 9.02 | 5.17 | 1.30 | 0.98 | 15.38 | 21.05 | 1.5 / 2.4 / 0.5 / 2.0 | 1.06 / 3.64 | 4.7% ±0.6 / 5.4% ±0.6 / 2.7% ±0.4 | 141 / 141 / 141 / 141 |
| Benchmark: pure PR, 5% | 5000 | 6.37 | 0.42 | 0.29 | 1.72 | 12.90 | 14.85 | 3.0 / 0.3 / 2.1 / 0.0 | 2.50 / 6.76 | 7.6% ±0.7 / 0.5% ±0.2 / 3.6% ±0.5 | 121 / 121 / 121 / 121 |
| Benchmark: pure PR, 3.5% | 5000 | 4.84 | 0.44 | 0.32 | 1.35 | 9.54 | 10.58 | 2.1 / 0.3 / 1.7 / 0.0 | 1.76 / 4.71 | 6.0% ±0.7 / 0.5% ±0.2 / 2.5% ±0.4 | 121 / 121 / 121 / 121 |

Costs and tails.

| System | Overridden % of votes: median / 90th / max | Rescued %: median | Touched %: median / 99th | Worst-hit party's vote moved: median / 90th | A party loses 2+ seats | Bloc deficit (all): 90th / 99th | House > base +5 / +10 / +20 |
|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 14.5 / 21.6 | 73% / 58% / 30% |
| Transfer, leftover grows (MMP-T-X) | 6.26 / 17.45 / 34.49 | 2.61 | 13.14 / 36.47 | 26.3% / 59.5% | 82% | 9.2 / 14.9 | 13% / 5% / 0% |
| Transfer, leftover absorbed (MMP-T) | 6.26 / 17.45 / 34.49 | 2.61 | 13.14 / 36.47 | 26.3% / 59.5% | 85% | 10.3 / 15.7 | 0% / 0% / 0% |
| Transfer + Backup Vote (MMP-BV-X) | 6.95 / 18.40 / 34.77 | 8.29 | 17.74 / 41.52 | 29.6% / 63.4% | 94% | 5.9 / 11.1 | 17% / 6% / 0% |
| Transfer + Backup Vote, absorbed (MMP-BV) | 6.95 / 18.40 / 34.77 | 8.29 | 17.74 / 41.52 | 29.6% / 63.4% | 95% | 7.7 / 13.9 | 0% / 0% / 0% |
| MMP at 141, grows (MMP141) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 13.5 / 21.2 | 54% / 40% / 17% |
| MMP at 141, capped (Review rule) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 67% | 15.3 / 22.5 | 0% / 0% / 0% |
| Transfer at 141, grows (MMP-T-X141) | 2.34 / 12.40 / 27.46 | 1.31 | 8.29 / 36.36 | 8.1% / 41.1% | 67% | 9.6 / 15.9 | 3% / 1% / 0% |
| Transfer at 141, capped (MMP-T141) | 2.34 / 12.40 / 27.46 | 1.31 | 8.29 / 36.36 | 8.1% / 41.1% | 69% | 9.7 / 15.9 | 0% / 0% / 0% |
| Transfer + Backup Vote at 141 (MMP-BV-X141) | 2.83 / 13.61 / 28.95 | 8.29 | 15.25 / 41.52 | 10.5% / 45.2% | 91% | 4.8 / 9.9 | 3% / 1% / 0% |
| Transfer + BV at 141, capped | 2.83 / 13.61 / 28.95 | 8.29 | 15.25 / 41.52 | 10.5% / 45.2% | 92% | 5.1 / 10.6 | 0% / 0% / 0% |
| Benchmark: pure PR, 5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 8.2 / 13.8 | 0% / 0% / 0% |
| Benchmark: pure PR, 3.5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 5.7 / 9.6 | 0% / 0% / 0% |

### Experiment 1: paired comparisons

Share of the same elections where the first system is better / worse than the second by more than a small margin (0.05 on the indices, 0.5 seats on bloc deficit, 1 seat on House size).

| Comparison | Standard | Qualifying parties | One-share | Bloc deficit | House smaller / larger |
|---|---|---|---|---|---|
| MMP-T-X vs MMP | 3% / 85% | 1% / 88% | 53% / 34% | 66% / 11% | 91% / 0% |
| MMP-T-X141 vs MMP141 | 6% / 69% | 1% / 77% | 52% / 24% | 54% / 12% | 82% / 0% |
| MMP-T vs MMP | 3% / 86% | 1% / 89% | 46% / 41% | 62% / 15% | 92% / 0% |
| MMP-BV-X vs MMP-T-X | 21% / 66% | 23% / 63% | 39% / 47% | 74% / 6% | 5% / 33% |
| MMP-BV-X141 vs MMP-T-X141 | 7% / 84% | 8% / 81% | 29% / 59% | 74% / 7% | 4% / 16% |
| CMP-Review141 vs MMP141 | 6% / 68% | 1% / 76% | 9% / 68% | 11% / 50% | 83% / 0% |
| MMP-T141 vs MMP-T-X141 | 2% / 25% | 2% / 25% | 8% / 18% | 3% / 10% | 30% / 0% |

### 2005–2023 elections (7 elections; rates are counts out of 7): every measure

Medians unless stated. Standard, qualifying parties, one-share, one-share + rescued voters: the four Gallagher-form indices (see the box). LH: Loosemore–Hanby (all votes). SLI: Sainte-Laguë index. Bloc deficits in seats against all votes / qualifying votes / countable votes / one-share. Minority-bloc majority with centrists counted with their ally (all votes / qualifying votes) and with centrists set aside.

| System | n | Standard | Qualifying parties | One-share | One-share + rescued | LH | SLI | Bloc deficit: all / qual / countable / one-share | Bloc seat–vote gap, points: median / 90th | Minority-bloc majority: all / qual / no centrists | House: median / 95th / 99th / max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 7 | 2.82 | 0.84 | 0.23 | 0.26 | 5.58 | 6.84 | 0.4 / 0.4 / 0.9 / 0.0 | 0.35 / 3.62 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 121 / 122 / 122 / 122 |
| Transfer, leftover grows (MMP-T-X) | 7 | 2.96 | 0.93 | 0.25 | 0.26 | 5.58 | 6.97 | 0.7 / 0.4 / 0.7 / 0.0 | 0.56 / 3.73 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 120 / 120 / 120 / 120 |
| Transfer, leftover absorbed (MMP-T) | 7 | 2.96 | 0.93 | 0.25 | 0.26 | 5.58 | 6.97 | 0.7 / 0.4 / 0.7 / 0.0 | 0.56 / 3.73 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 120 / 120 / 120 / 120 |
| Transfer + Backup Vote (MMP-BV-X) | 7 | 2.96 | 0.84 | 0.26 | 0.26 | 5.58 | 6.97 | 0.5 / 0.6 / 0.4 / 0.0 | 0.40 / 2.90 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 120 / 121 / 121 / 121 |
| MMP at 140 | 7 | 2.83 | 0.81 | 0.00 | 0.22 | 5.58 | 6.24 | 1.2 / 0.4 / 0.8 / 0.0 | 0.84 / 3.09 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 141 / 141 / 141 / 141 |
| MMP at 140, capped (Review rule) | 7 | 2.83 | 0.67 | 0.00 | 0.09 | 5.58 | 6.27 | 0.6 / 0.4 / 0.5 / 0.0 | 0.46 / 2.78 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 140 / 140 / 140 / 140 |
| Transfer at 140 | 7 | 2.83 | 0.67 | 0.00 | 0.09 | 5.58 | 6.27 | 0.6 / 0.4 / 0.5 / 0.0 | 0.46 / 2.78 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 140 / 140 / 140 / 140 |
| Transfer + Backup Vote at 140 | 7 | 2.83 | 0.81 | 0.05 | 0.15 | 5.58 | 6.27 | 0.6 / 0.6 / 0.3 / 0.0 | 0.41 / 2.06 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 140 / 140 / 140 / 140 |
| Benchmark: pure PR, 5% | 7 | 4.67 | 0.33 | 0.02 | 0.25 | 8.66 | 9.50 | 1.5 / 0.3 / 0.8 / 0.0 | 1.23 / 2.23 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 120 / 120 / 120 / 120 |
| Benchmark: pure PR, 3.5% | 7 | 4.00 | 0.39 | 0.09 | 0.33 | 7.55 | 8.20 | 1.2 / 0.4 / 0.4 / 0.0 | 1.04 / 2.23 | 0.0% ±0.0 / 0.0% ±0.0 / 0.0% ±0.0 | 120 / 120 / 120 / 120 |

Costs and tails.

| System | Overridden % of votes: median / 90th / max | Rescued %: median | Touched %: median / 99th | Worst-hit party's vote moved: median / 90th | A party loses 2+ seats | Bloc deficit (all): 90th / 99th | House > base +5 / +10 / +20 |
|---|---|---|---|---|---|---|---|
| MMP (current, 121) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 4.4 / 4.4 | 0% / 0% / 0% |
| Transfer, leftover grows (MMP-T-X) | 0.57 / 1.12 / 1.12 | 0.02 | 0.62 / 1.44 | 1.4% / 4.2% | 0% | 4.5 / 4.5 | 0% / 0% / 0% |
| Transfer, leftover absorbed (MMP-T) | 0.57 / 1.12 / 1.12 | 0.02 | 0.62 / 1.44 | 1.4% / 4.2% | 0% | 4.5 / 4.5 | 0% / 0% / 0% |
| Transfer + Backup Vote (MMP-BV-X) | 0.60 / 1.28 / 1.28 | 3.21 | 4.03 / 5.89 | 1.4% / 4.4% | 14% | 3.5 / 3.5 | 0% / 0% / 0% |
| MMP at 140 | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 4.4 / 4.4 | 0% / 0% / 0% |
| MMP at 140, capped (Review rule) | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 3.9 / 3.9 | 0% / 0% / 0% |
| Transfer at 140 | 0.29 / 0.52 / 0.52 | 0.02 | 0.62 / 1.44 | 0.6% / 2.1% | 0% | 3.9 / 3.9 | 0% / 0% / 0% |
| Transfer + Backup Vote at 140 | 0.31 / 0.60 / 0.60 | 3.21 | 4.03 / 5.89 | 0.6% / 2.3% | 14% | 2.9 / 2.9 | 0% / 0% / 0% |
| Benchmark: pure PR, 5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 2.7 / 2.7 | 0% / 0% / 0% |
| Benchmark: pure PR, 3.5% | 0.00 / 0.00 / 0.00 | 0.00 | 0.00 / 0.00 | 0.0% / 0.0% | 0% | 2.7 / 2.7 | 0% / 0% / 0% |
