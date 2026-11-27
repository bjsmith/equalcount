# Experiment 3: Where each system leads from 2026

## Summary

Experiment 3 asks what happens over the next five elections (2029–2041) if New Zealand keeps MMP, or adopts one of the overhang reforms in time for 2029, once voters and parties respond to the incentives each system creates.

Starting from the official 2026 result, 1,000 simulated futures were run under ten systems. In every future, voters and parties adapt between elections according to written reasoning about each group's interests.

- **Under current MMP, overhang becomes entrenched.** Splitting pays, so both blocs keep doing it. The median overhang is 11 seats per election and the House is typically 132 seats, reaching 155 in the worst case. Te Pāti Māori (TPM) keeps winning most Māori electorates on about half a percent of the party vote.
- **The reforms end the reward for splitting, and voters respond.** Partner parties campaign for two ticks, and under the absorbing reforms TPM rebuilds its party vote to about 5–6%. Overhang falls steadily under every reform.
- **At 121 seats, absorbing leftover overhang backfires.** Once splitting stops, the remaining overhang comes mostly from a large party winning electorates on plurality. Absorbing it within a fixed House costs the other bloc list seats. Under MMP-T and MMP-BV the bloc with fewer votes wins the majority in 7.6–7.8% of elections, against 5.6% under MMP.
- **Letting the House grow for leftover overhang (the "-X" variants) fixes that, at small cost.** MMP-T-X and MMP-BV-X bring minority-bloc wins back to MMP's level (5.6–5.7%). The House grows by about 2 seats typically and 17–18 at worst, against MMP's 34. The cost is that TPM's strategy survives, because its leftover overhang still adds seats for its bloc.
- **141 seats does most of the work.** With 71 electorates and 70 list seats, overhang under the reforms largely disappears by 2035. MMP-BV-X141 performs best overall: median bloc seat deficit 1.4, minority-bloc wins 3.5%, a House of 141 typically and at most 151.
- **Some imbalance remains under every system.** It comes mainly from votes wasted on parties below the threshold and from swings in the party system, not from overhang. Bloc seat deficits drift upward over the period under all ten systems.
- **Under MMP, things only get worse if gaming escalates, and that is the real risk.** The baseline futures hold the 2026 level flat; they don't recover it. Two scenarios add escalation: a bloc copies the Te Pāti Māori playbook in general seats, where a big party's supporters keep ticking its candidates but party-vote an ally.
  - If blocs copy only in reaction to the other side (the **copycat** scenario), little changes.
  - If they adopt it because it pays (the **escalation** scenario), MMP deteriorates steadily: by 2041 the median overhang is 30 seats, the median House 151 (up to 181), the Gallagher index 9.9, and the minority bloc wins 11% of elections. Over 2029–2041, 36% of futures have at least one minority-bloc government.
  - Every reform is unaffected, because the playbook gains nothing under a transfer rule.
  - MMP141 doesn't protect against escalation: its House reaches 198.
- **MMP-BV-X141 removes essentially all the imbalance an overhang fix can remove.** As a benchmark, seats were allocated by pure proportional representation (no electorates, so no overhang is possible) on the same simulated ballots. At the 5% threshold that gives a median bloc seat deficit of 1.4 and minority-bloc majorities in 4.1–4.5% of elections. MMP-BV-X141 matches it on bloc fairness (1.4) and does better on wrong winners (3.5%), because the Backup Vote rescues some votes the threshold would waste. Lowering the threshold to 3.5% would do more than any overhang rule: 0.7–0.8 and 2.4–2.7% on the same benchmark.
- **The results hold across reasoning assumptions.** How fast voters learn, how hard parties campaign and how much voters consolidate barely affect the outcomes (no correlation above 0.10). The differences between systems come from the rules themselves.

## Question

Experiments 1 and 2 compared the systems on fixed ballots: the same voter behaviour under every system. That shows how each set of rules handles a given election, but not how voters would behave once they understand those rules.

Experiment 3 adds that feedback. If a reform removes the payoff from strategic splitting, voters should split less, which shrinks the overhang the reform was built to handle. If a reform creates new incentives, voters should respond to those too. The question is where those dynamics lead, election by election, from where New Zealand is now.

## Design

### Systems compared

All systems keep 71 electorates (64 general and 7 Māori). The 141-seat versions add 20 list seats.

| System | Size | Rule |
|---|---|---|
| **MMP** | 121 | Current system. Overhanging parties keep their extra electorates and the House grows. |
| **MMP-T** | 121 | Overhang Transfer (the explainer's Option 1). Only when a party overhangs: wasted party votes on ballots for its winning candidates count for it, as many as needed; then the same fraction of every split ballot for its winners. Anything left is absorbed within 121 seats (the Independent Electoral Review rule). |
| **MMP-BV** | 121 | Backup Vote (the explainer's Option 2). At every election, a party vote for a party that doesn't qualify counts for the voter's electorate candidate's party, if that party qualifies. If a party still overhangs: split-ballot transfer, then absorption, as in MMP-T. |
| **MMP-T-X**, **MMP-BV-X** | 121+ | As MMP-T / MMP-BV, but overhang the transfer can't cover is handled as under current MMP: the party keeps its extra seats and the House grows. |
| **MMP141**, **MMP-T141**, **MMP-BV141**, **MMP-T-X141**, **MMP-BV-X141** | 141 | The same five rules with 141 seats. |

Every future runs MMP in 2026. The reformed systems take effect in 2029.

### Starting point: 2026 (fixed)

The official 2026 result is the starting point in every future. That includes national party votes, each electorate's party votes, and the resulting electoral map: each party's local strength relative to its national vote. Only elections from 2029 on are simulated.

Voter behaviour at 2026 was fitted so the model reproduces the 2026 electorate results. In a typical future it gives National 41 electorates (40 in reality), Labour 20 (22), and TPM 6 of the 7 Māori electorates (5). The same values were the best fit to the preliminary count. The fit implies:

| Behaviour | 2026 value |
|---|---|
| Left partners' voters (mainly Green) giving their electorate vote to Labour | 15% |
| Right partners' voters (ACT, NZ First) giving their electorate vote to National | 35% |
| Left voters in Māori electorates giving their electorate vote to TPM | 40% |
| Personal vote: voters backing a candidate they like regardless of party | 20%: the top of the range Experiment 2 fitted for 2005–2023 (12–20%, median 16%) |

Simulated under MMP at 121 seats, this 2026 starting point typically produces an 11-seat overhang (National 6, TPM 5) and a 132-seat House. The official result itself produced 130 seats at 120 (National 6, TPM 4).

### What changes between elections

**Events outside voters' strategy** are the same across all ten systems within a future:
- a swing between the blocs, sized from 2005–2026 and pulled back toward an even split over time;
- party drift within each bloc, larger for smaller parties;
- drift for centrist parties;
- a 15% chance each election of a new party starting with 1–4%;
- parties under 0.5% folding into their side's minor-party group;
- slow drift in the electoral map.

**Voters' and parties' responses** depend on what the last election taught them under their system. These were reasoned through election by election, putting each group of voters and each party in turn in their own position. Voters are treated as partly rational and partly attentive: a reform's effects are learned over several elections, faster when its effects are visible.

### The reasoning

The full reasoning before each election is in `futures/reasoning_2032.md` to `reasoning_2041.md`. In outline:

**Current MMP (and MMP141).** Splitting pays and nothing penalises it.
- Partner parties' voters split a little more each time their leader overhangs and keeps the seats.
- Where the left wins on an overhang, the right copies the cup-of-tea approach more openly: some National voters party-vote a partner while still ticking the National candidate.
- Where the right wins more seats than votes, the left pushes Green voters in marginal seats to tick Labour.
- TPM's Māori-seat strategy keeps paying, so it continues and strengthens.

**Reforms, first election (2029).** Voters have barely adapted, so large transfers happen: 38,000–288,000 party votes in the hand-reasoned runs. Partner parties lose seats, and that's public.

**Reforms, later elections:**
- **ACT and NZ First** lost seats because their voters ticked National candidates. They run "two ticks" campaigns. Their voters are engaged, so splitting falls fast.
- **Green and Opportunity voters** respond more slowly. Their splits are more often personal.
- **Left voters** who saw Labour lose list seats because some of them ticked a National MP they liked split less on personal grounds, but only somewhat.
- **TPM (absorbing reforms)** gains nothing from its overhang, and the left pays for it in list seats. It switches to asking for the party vote, rebuilding toward the roughly 3–5% that its Māori-seat wins require.
- **Consolidation (absorbing reforms, from 2038).** Once splitting has largely stopped, any remaining overhang comes from plurality wins, and it is absorbed from the other side's list seats. Backing your own side's strongest candidate where the other leader would otherwise win now costs nothing, so engaged partner voters in marginal seats begin doing it.
- **Backup Vote.** Voters learn that a vote for a small party isn't wasted if their electorate vote goes to a qualifying ally. Small parties gain a little, and their voters choose a qualifying candidate.
- **-X variants.** Leftover overhang still adds seats for its bloc, so TPM's strategy still pays and TPM doesn't change course. Only the Greens, whose voters' party votes are being transferred to TPM, push for two ticks in Māori seats.

### Two stages

1. **Ten hand-reasoned futures.** Each election's outcome in each future was reviewed before reasoning about the next. Those judgements were written down and encoded as rules.
2. **One thousand walks.** The same rules, applied automatically, with each future drawing its own strength for every rule. Each range brackets the hand-reasoned value; for example, the strength of ACT and NZ First's two-tick campaigns, and TPM's recovery speed and target. This spans a range of plausible reasoning trajectories rather than one.
   - The rules follow roles (left leader, right partners, and so on), not party names. That matters because about 23% of simulated elections reach a situation the hand-reasoned runs never saw. A change of bloc leader (the Greens leading the left, or ACT or NZ First leading the right) accounts for 15%, and Te Pāti Māori polling over 5% for 10%; some elections have both.

The ten hand-reasoned futures, rerun from the official 2026 count with the role-based rules, give results consistent with the thousand walks.

### Measures

These match Experiments 1 and 2.

- **Bloc seat deficit:** how many seats the worse-off bloc is short of its share of all party votes, including votes for parties that missed the threshold. Every party belongs to the left or right bloc; centrists count with their ally (Opportunity counts as a left ally throughout).
- **Gallagher index:** the conventional measure of how far each party's seat share is from its share of the qualifying party vote.
- **Minority-bloc majority:** the bloc with fewer party votes holds a majority of the House.
- **Overhang:** electorates won beyond the party's entitlement on raw party votes at the system's size.

## Results

### All elections, 2029–2041 (1,000 walks × 5 elections)

| System | Overhang: median / 90th / max | House: median / 99th / max | Bloc seat deficit: median / 90th / 99th | Blocs within 1 seat | Gallagher | Minority-bloc majority |
|---|---|---|---|---|---|---|
| MMP | 11 / 20 / 34 | 132 / 149 / 155 | 2.2 / 5.7 / 9.3 | 24% | 4.1 | 5.6% |
| MMP-T | 6 / 15 / 29 | 121 | 2.5 / 6.4 / 9.4 | 23% | 3.7 | 7.6% |
| MMP-BV | 7 / 16 / 30 | 121 | 2.4 / 6.5 / 9.6 | 24% | 4.3 | 7.8% |
| MMP-T-X | 5 / 14 / 28 | 122 / 133 / 138 | 2.2 / 5.3 / 8.3 | 24% | 3.2 | 5.7% |
| MMP-BV-X | 6 / 15 / 29 | 123 / 134 / 139 | 2.0 / 5.1 / 7.7 | 27% | 3.6 | 5.6% |
| MMP141 | 6 / 15 / 32 | 147 / 164 / 173 | 2.0 / 5.4 / 9.3 | 27% | 3.2 | 4.1% |
| MMP-T141 | 3 / 9 / 24 | 141 | 1.7 / 4.5 / 8.2 | 34% | 1.5 | 4.4% |
| MMP-BV141 | 3 / 10 / 25 | 141 | 1.4 / 3.9 / 6.8 | 39% | 1.9 | 4.1% |
| MMP-T-X141 | 1 / 8 / 22 | 141 / 146 / 150 | 1.7 / 4.4 / 7.9 | 33% | **0.8** | 4.4% |
| **MMP-BV-X141** | 2 / 9 / 24 | 141 / 147 / 151 | **1.4 / 3.7 / 6.2** | 37% | 1.5 | **3.5%** |

### Over a whole future (2029–2041, per walk)

| System | Futures with at least one minority-bloc majority | Largest House in the future: median / 95th / max | Worst bloc seat deficit in the future: median / 95th | Minority-bloc majority in close elections (blocs 48–52%) |
|---|---|---|---|---|
| MMP | 23% | 138 / 148 / 155 | 4.9 / 9.2 | 28% |
| MMP-T | 31% | 121 | 5.4 / 9.2 | 34% |
| MMP-BV | 32% | 121 | 5.4 / 9.4 | 34% |
| MMP-T-X | 25% | 125 / 133 / 138 | 4.7 / 8.2 | 29% |
| MMP-BV-X | 24% | 126 / 133 / 139 | 4.5 / 7.7 | 29% |
| MMP141 | 18% | 152 / 163 / 173 | 4.4 / 8.6 | 23% |
| MMP-T141 | 19% | 141 | 3.9 / 7.9 | 25% |
| MMP-BV141 | 18% | 141 | 3.4 / 6.7 | 23% |
| MMP-T-X141 | 20% | 143 / 145 / 150 | 3.9 / 7.7 | 24% |
| **MMP-BV-X141** | **16%** | 143 / 146 / 151 | **3.4 / 6.1** | **20%** |

### Election by election

**Median overhang / median House**

| Year | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2029 | 11 / 132 | 10 / 121 | 10 / 121 | 10 / 124 | 10 / 124 | 6 / 147 | 5 / 141 | 5 / 141 | 5 / 143 | 5 / 143 |
| 2032 | 11 / 132 | 8 / 121 | 8 / 121 | 6 / 122 | 6 / 123 | 6 / 147 | 3 / 141 | 4 / 141 | 3 / 141 | 3 / 141 |
| 2035 | 11 / 132 | 6 / 121 | 7 / 121 | 4 / 121 | 5 / 122 | 6 / 147 | 2 / 141 | 2 / 141 | 0 / 141 | 1 / 141 |
| 2038 | 11 / 132 | 4 / 121 | 6 / 121 | 4 / 121 | 5 / 122 | 6 / 147 | 0 / 141 | 1 / 141 | 0 / 141 | 0 / 141 |
| 2041 | 11 / 132 | 4 / 121 | 6 / 121 | 3 / 121 | 5 / 122 | 7 / 148 | 0 / 141 | 1 / 141 | 0 / 141 | 0 / 141 |

**Median bloc seat deficit (share of elections with a minority-bloc majority)**

| Year | MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2029 | 1.7 (4%) | 1.7 (5%) | 1.5 (4%) | 1.3 (3%) | 1.1 (2%) | 1.6 (3%) | 0.9 (3%) | 0.8 (2%) | 1.0 (3%) | 0.9 (2%) |
| 2032 | 2.2 (6%) | 2.6 (9%) | 2.4 (9%) | 2.4 (7%) | 2.1 (6%) | 1.8 (4%) | 1.6 (6%) | 1.4 (5%) | 1.7 (4%) | 1.3 (4%) |
| 2035 | 2.5 (6%) | 3.0 (9%) | 2.7 (10%) | 2.8 (6%) | 2.6 (7%) | 2.1 (4%) | 2.0 (4%) | 1.6 (4%) | 2.1 (5%) | 1.7 (4%) |
| 2038 | 2.5 (6%) | 2.9 (8%) | 2.9 (8%) | 2.6 (7%) | 2.5 (6%) | 2.2 (5%) | 2.0 (5%) | 1.8 (5%) | 2.1 (5%) | 1.7 (4%) |
| 2041 | 2.7 (6%) | 2.9 (7%) | 3.1 (8%) | 2.5 (6%) | 2.5 (6%) | 2.4 (4%) | 2.1 (4%) | 1.8 (4%) | 2.2 (5%) | 1.7 (3%) |

**Te Pāti Māori in 2041: median party vote / share of left voters in Māori seats ticking TPM**

| MMP | MMP-T | MMP-BV | MMP-T-X | MMP-BV-X | MMP141 | MMP-T141 | MMP-BV141 | MMP-T-X141 | MMP-BV-X141 |
|---|---|---|---|---|---|---|---|---|---|
| 0.6% / 50% | 5.6% / 15% | 5.7% / 15% | 0.6% / 23% | 0.6% / 23% | 0.6% / 50% | 5.6% / 15% | 5.6% / 15% | 0.6% / 23% | 0.6% / 23% |

### Benchmark: how close to the best an overhang fix could do?

On each simulated election's party votes, seats were also allocated by pure proportional representation: Sainte-Laguë at 121 seats over the parties that pass the threshold, with no electorates. No overhang is possible under that rule, so it shows how much imbalance would remain even if overhang were handled perfectly. Each pathway's own ballots are used, since behaviour differs between pathways.

| Ballots from | As run: bloc seat deficit / minority-bloc majority / Gallagher | Pure PR, 5% threshold | Pure PR, 3.5% threshold |
|---|---|---|---|
| MMP | 2.2 / 5.6% / 4.1 | 1.4 / 4.3% / 0.4 | 0.8 / 2.6% / 0.4 |
| MMP-T-X | 2.2 / 5.7% / 3.2 | 1.4 / 4.1% / 0.4 | 0.8 / 2.4% / 0.4 |
| MMP-BV-X | 2.0 / 5.6% / 3.6 | 1.4 / 4.5% / 0.4 | 0.7 / 2.7% / 0.4 |
| MMP-BV-X141 | 1.4 / 3.5% / 1.5 | 1.4 / 4.5% / 0.4 | 0.7 / 2.7% / 0.4 |

**How to read this:**
- Of MMP's median bloc seat deficit of 2.2, only about 0.8 seats comes from overhang. The other 1.4 is caused by the 5% threshold.
- Of MMP's 5.6% rate of minority-bloc majorities, only about 1.3 points comes from overhang.
- Overhang does account for almost all of MMP's Gallagher index: 4.1 against 0.4.
- **MMP-BV-X141 removes all of the overhang-caused bloc imbalance and goes slightly beyond it.** The Backup Vote rescues some votes the threshold would otherwise waste. Its remaining Gallagher of 1.5 is mostly the Backup Vote itself, which by design moves rescued votes away from raw party-vote shares.
- **Lowering the threshold to 3.5%** (the Independent Electoral Review's recommendation) would roughly halve what remains, more than any overhang rule can achieve.

### Scenarios: escalation under MMP

The baseline futures let existing players adjust their behaviour, but nobody adopts a new strategy. Two scenarios add the escalation people fear: a bloc copies the Te Pāti Māori playbook in general seats.

**The split-list playbook.** The bloc leader's supporters keep ticking its electorate candidates but give their party vote to an allied partner. The leader's list entitlement shrinks while it keeps its electorates, so its overhang grows, and the partner gains list seats. Once a bloc adopts it, a further 5–25% of the leader's voters shift each election, up to a cap.

Under the transfer reforms, those split ballots would be transferred straight back, so the playbook gains nothing and no bloc adopts it. All reform pathways therefore give identical results in every scenario.

| Scenario | Who adopts, and when | Share of leader voters moved per election (cap) |
|---|---|---|
| **Baseline** | Nobody | – |
| **Copycat** | A bloc reacts to the other side winning more seats than votes (chance up to 10–40% per election), or to the other side having adopted it (+20–50%) | 5–15% (cap 30–70%) |
| **Escalation** | As copycat, with stronger reactions (20–50%, +30–60%), plus a 10–30% chance each election of adopting it simply because it pays | 10–25% (cap 50–90%) |

**MMP under escalation, by year** (share of the 1,000 futures in which each bloc has adopted the playbook; medians unless stated)

| Year | Adopted: left / right | Overhang: median / 90th | House: median / 90th / max | Gallagher | Minority-bloc majority |
|---|---|---|---|---|---|
| 2029 | 20% / 32% | 13 / 23 | 134 / 144 / 153 | 4.4 | 5.4% |
| 2032 | 50% / 57% | 17 / 28 | 138 / 149 / 162 | 5.5 | 10.2% |
| 2035 | 68% / 74% | 21 / 35 | 142 / 156 / 171 | 6.8 | 10.0% |
| 2038 | 82% / 84% | 26 / 39 | 147 / 160 / 175 | 8.5 | 10.7% |
| 2041 | 89% / 90% | 30 / 44 | 151 / 165 / 181 | 9.9 | 10.6% |

**All elections 2029–2041, by scenario**

| System | Baseline: bloc seat deficit / House max / minority-bloc majority | Copycat: same | Escalation: same | Futures with at least one minority-bloc majority (baseline / escalation) |
|---|---|---|---|---|
| MMP | 2.2 / 155 / 5.6% | 2.3 / 167 / 6.1% | **3.9 / 181 / 9.4%** | 23% / **36%** |
| MMP141 | 2.0 / 173 / 4.1% | 2.0 / 183 / 4.3% | **3.1 / 198 / 7.8%** | 18% / **31%** |
| MMP-BV-X | 2.0 / 139 / 5.6% | unchanged | unchanged | 24% / 24% |
| MMP-BV-X141 | 1.4 / 151 / 3.5% | unchanged | unchanged | 16% / 16% |

**What the scenarios show:**
- **Reactive copying alone changes little.** Under MMP both blocs already game, so the other side rarely looks over-represented by much, and the trigger seldom fires.
- **If the playbook is adopted because it pays, MMP keeps deteriorating.**
  - By 2041 the median House is 151, three times the 2026 overhang.
  - Party-level disproportionality is about 10 times the 2005–2023 norm.
  - Minority-bloc governments are almost twice as likely as in the baseline (9.4% against 5.6%).
- **141 seats is no protection on its own.** MMP141 under escalation has a median House of 156 and a maximum of 198.
- **The reforms are immune by construction.** That's the strongest argument for them in this experiment. Their value is not that they make 2029 much fairer than MMP. It's that they remove the payoff that would let MMP get worse.

## Interpretation

**Why the gains look modest.** The imbalance that overhang causes under MMP in these futures is real but bounded. Both blocs game the system, and their overhangs partly cancel. So MMP's main harms in these futures are a large, unpredictable House and escalating gaming, more than a systematic tilt between the blocs. On bloc fairness and wrong winners, the remaining gap is caused by the threshold, and no overhang rule can close it. The reforms are close to the ceiling of what an overhang fix can do. If one bloc games much more effectively than the other, as in the asymmetric scenarios of Experiment 1, MMP's harm is far larger, and the reforms' protection is worth more.

**MMP: a stable arms race, unless the playbook spreads.** In the baseline, overhang doesn't grow without limit, but it doesn't shrink either: about 11 seats per election, and a House of 130–140 is normal. Both blocs game the system, and the two blocs' overhangs partly cancel. That keeps bloc imbalance moderate but makes it unpredictable: in close elections the minority bloc wins the majority 28% of the time. MMP141 halves the overhang, but the House still grows beyond 141 in most elections, reaching 173 at worst.

**MMP-T and MMP-BV at 121: the right incentives, the wrong fallback.** These reforms do what they were designed to do on behaviour: splitting falls, TPM rebuilds its party vote, and overhang shrinks year after year. But the overhang that remains comes from plurality wins, mostly a strong National winning electorates against a divided left. No split ballots can be transferred to cover it, and absorbing it within 121 seats hands the cost to the other bloc. That is why these two systems have the highest rates of minority-bloc majorities (7–8%, or one future in three over 15 years). This is the same failure mode identified at the very start of the work: once strategic splitting stops, the remaining overhang is the kind transfers can't fix.

**The -X variants at 121: a better fallback.** Growing the House for leftover overhang, as MMP already does, removes the absorption penalty. Wrong-winner risk returns to MMP's level, and the House grows by only 2–3 seats typically. The trade-off is incentive strength: leftover overhang still rewards the bloc that creates it, so TPM's strategy persists (party vote stays around 0.6%). The reward is far smaller than under MMP, because the transfer covers most of the overhang first.

**141 seats.** With 70 list seats against 71 electorates, overhang from plurality wins becomes rare. Under the reforms it has almost disappeared by 2035. All four 141-seat reforms beat MMP on bloc fairness and party-level proportionality, and MMP-BV-X141 does best on bloc fairness and wrong-winner risk. The Backup Vote's rescue of votes for sub-threshold parties is what separates the BV systems from the T systems at 141 seats.

**What no system fixes.** Bloc seat deficits drift up over the period under every system: about 2.2 → 2.7 under MMP, and 1.0 → 1.7 under MMP-BV-X141. Under MMP-BV-X141, the bloc seat deficit is correlated with the share of wasted votes (0.48), not with overhang (0.06). The remaining imbalance comes from the party system itself, through parties falling below the threshold and the threshold squeeze, not from how overhang is handled.

**How robust are these findings?** The strength drawn for each reasoning rule barely affects outcomes. Across the 1,000 walks, the correlation between any rule strength and a future's average bloc seat deficit is at most 0.10 in absolute value. The ranking of systems reflects their rules, not the precise reasoning assumptions.

## Limitations

- **Reasoning is modelled, not observed.** The responses are judgements about how voters and parties would react. They are written out and varied, but not tested against real behaviour under these systems.
- **The escalation scenarios are assumptions, not forecasts.** How likely a bloc is to adopt the split-list playbook, and how far it pushes it, are judgement calls, varied across the walks. The scenarios show what happens if escalation occurs, not how likely it is.
- **The 2026 starting point is fitted.** It uses the official count, with voter behaviour fitted to reproduce the electorate results (National, Labour and TPM each within one or two seats in a typical future). TPM's extreme split (0.6% party vote, five electorates) dominates the early elections.
- **Simplifications in the party system:**
  - Opportunity counts as a left ally throughout.
  - Māori parties' votes are modelled through the Māori electorates.
  - Drift between elections may be somewhat strong: leader swaps, which have never happened under MMP, occur in some futures.
- **Fixed electorates.** The number of electorates stays at 71, and boundaries are fixed apart from slow drift.
- **One rule per bloc.** Behaviour is modelled bloc-wide, by role. Local campaigns, candidate retirements and deals beyond the "standout candidate" mechanism aren't modelled individually.

## Reproducing

| File | Contents |
|---|---|
| `mc_future.py` | The engine: starting point, one election, behaviour rules, between-election events |
| `futures_reason.py` | The between-election reasoning rules, by election |
| `futures/reasoning_2032.md` … `reasoning_2041.md` | The written reasoning |
| `futures/digest_<year>.md`, `futures/summary.md` | The ten hand-reasoned futures (role-based rerun from the official 2026 count) |
| `mc_future_walks.py` | The 1,000-walk runner, with every rule's hand value and drawn range |
| `futures_walks/results.csv`, `futures_walks/summary.md` | All 50,000 simulated elections and their summary |
| `mc_future_floor.py` | The pure-PR benchmark (5% and 3.5% thresholds) on the same ballots |
| `futures_walks_copycat/`, `futures_walks_escalation/` | The two escalation scenarios (`mc_future_walks.py 1000 --copycat` / `--escalation`; playbook rules in `mc_future.copycat`) |

```bash
python3 mc_future.py init && python3 mc_future.py round 2029
for y in 2032 2035 2038 2041; do python3 futures_reason.py $y && python3 mc_future.py round $y; done
python3 mc_future_walks.py 1000
python3 mc_future_walks.py 1000 --copycat
python3 mc_future_walks.py 1000 --escalation
python3 mc_future_floor.py 1000
```
