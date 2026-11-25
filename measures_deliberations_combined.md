# Measures and framing: combined deliberations across Experiments 1–3

*Replaces `measures_deliberations_exp1.md`, `measures_deliberations_exp2.md` and `measures_deliberations.md` (Experiment 3) as the working document. None of the changes below has been implemented. Numbers quoted are from the existing reports (`experiment1_report.md`, `report_experiment2.md`, `report_experiment3.md`) and `results_2026.json`.*

---

## 0. The short version

1. **Lead with the Overhang Transfer on its own, not the package.** Present MMP-BV and the 141-seat House as separable add-ons. The transfer is the idea nobody in the current debate is discussing. Its case rests on measures nobody disputes (House size, local representation, the incentive to game). The package's headline advantage, bloc fairness, mostly comes from the Backup Vote's effect on threshold-wasted votes, and that belongs to a different argument.
2. **The transfer needs a fallback, and the honest default is "grow" (MMP-T-X), not "absorb".** Absorbing within a fixed House is the Spinoff's Option 1 problem, and it is what made MMP-T at 121 worse than MMP on wrong winners in Experiment 3 (7.8% against 5.6%).
3. **Report proportionality as a bracket.** Use a standard baseline with neither tweak, one measure tilted towards MMP and one tilted towards the reform, disclosed as such. On your bundling question: for a transfer-only pitch, bundling the two tweaks is right, because together they isolate the double counting from the threshold. Section 3 explains why.
4. **Our current Gallagher index already excludes sub-threshold votes.** The "MMP-favouring" version you proposed is what all three experiments have been reporting. The standard index, which includes every party, is the one we haven't been computing.
5. **Make the cost measures headline, not footnotes.** On the 2026 provisional result the transfer moves about 192,000 party votes (8% of qualifying votes), and ACT drops from 13 seats to 9. That is the number critics will lead with, so we should publish it first.
6. **Add the Spinoff's options as comparator systems** run on the same ballots. Two already exist in `model_2026.py` (the Review's cap, and the German rule). The transfer is best shown as the option that avoids each of their failures.

---

## 1. The framing decision: the package, or the transfer alone?

### Recommendation: the transfer alone, with an ablation ladder

The public debate ([Spinoff, 19 Nov 2026](https://thespinoff.co.nz/politics/19-11-2026/ten-ways-to-fix-mmp-explained)) lists ten fixes, and none reassigns party votes to follow electorate votes. Every fix on that list either:

- **removes seats from other parties** (Option 1, the Review's cap),
- **adds seats** (Options 2 and 3),
- **unseats electorate winners** (Option 4, the German rule, and the open letter's softer version),
- **removes the split ballot** (Option 5),
- **changes how Parliament votes** (Option 6), or
- **abolishes some or all electorates** (Options 8 and 9).

The article doesn't mention the threshold or wasted votes at all. The threshold already has its own conversation: the Review's 3.5% recommendation.

So the most useful contribution is a clean answer to one question: **how much difference does the transfer, by itself, make?** That argues for:

- **Treat the transfer as the reform** and everything else as an optional extra, each with its own measured increment.
- **Keep the Backup Vote out of the headline.** It is a threshold remedy, a contingent second preference, and it moves votes at every election, not only when there's an overhang. That is a bigger and more contestable change. Bundling it with the transfer lets critics attack the transfer with objections that only apply to the Backup Vote. It also muddies attribution: in the package results it isn't clear which component did what.
- **Keep 141 seats out of the headline too.** More MPs is Option 2 on the Spinoff list and is unpopular. The transfer's case shouldn't depend on it.

### The ablation ladder

Show each step as a change from the step before. These are existing Experiment 3 results (baseline, all elections 2029–2041):

| Step | System | Overhang (median) | House: median / max | Gallagher | Bloc seat deficit | Minority-bloc majority | Under escalation: House max / minority-bloc |
|---|---|---|---|---|---|---|---|
| 0 | MMP | 11 | 132 / 155 | 4.1 | 2.2 | 5.6% | 180 / 9.4% |
| **1** | **+ transfer, leftover grows (MMP-T-X)** | **5** | **122 / 138** | **3.2** | **2.2** | **5.7%** | **unchanged** |
| 1′ | + transfer, leftover absorbed (MMP-T) | 6 | 121 | 3.8 | 2.5 | 7.8% | unchanged |
| 2 | + Backup Vote (MMP-BV-X) | 6 | 123 / 140 | 3.6 | 2.0 | 5.2% | unchanged |
| 3 | + 20 list seats (MMP-T-X141) | 1 | 141 / 150 | 0.7 | 1.7 | 4.6% | unchanged |
| 3 | + both (MMP-BV-X141) | 2 | 141 / 152 | 1.4 | 1.4 | 3.6% | unchanged |
| ref | MMP141 (seats, no transfer) | 6 | 147 / 171 | 3.2 | 2.0 | 4.3% | 197 / 7.7% |
| ref | Pure PR, no electorates (Option 9) | 0 | 121 | 0.4 | 1.4 | 4.8% | – |

The transfer's own marginal effect, measured at both sizes:

| Comparison | House | Gallagher | Bloc seat deficit | Minority-bloc majority | Escalation |
|---|---|---|---|---|---|
| MMP → MMP-T-X (121) | 132/155 → 122/138 | 4.1 → 3.2 | 2.2 → 2.2 | 5.6% → 5.7% | Removed |
| MMP141 → MMP-T-X141 | 147/171 → 141/150 | 3.2 → 0.7 | 2.0 → 1.7 | 4.3% → 4.6% | Removed |
| Fixed ballots, Exp 2 (121) | 123/139 → 122/127 | 1.4 → 1.5 | 2.1 → 1.7 | – | – |

### What this means for the message

The honest story for the transfer alone is narrower than the package story, but harder to dispute:

- **It caps House growth without charging anyone else.** No other option does that without unseating electorate MPs.
- **It removes the payoff from splitting**, so the system can't be gamed into a 150–180-seat House. This is the strongest single result in the project.
- **Once voters adapt, it improves proportionality on MMP's own yardstick**: party votes as cast, qualifying parties only. With fixed ballots it is slightly *worse* on that yardstick (1.4 → 1.5), which we should say plainly.
- **It does not, by itself, improve bloc fairness or wrong-winner risk** in the baseline futures. Those gaps come mainly from the threshold and from plurality-driven overhang, and the transfer can't touch either. Claiming otherwise would be the package's argument carried over.

That's a smaller claim, but each part survives an MMP-favourable measure. That is the test of whether it will persuade anyone.

### Who can game the status quo: capacity, not willingness

A one-sided gaming scenario, where one bloc games and the other doesn't, isn't realistic: once one side games, the other copies. What does differ between the blocs is how much overhang each *can* engineer.

**Why the capacities differ:**
- **Te Pāti Māori's play is capped by the 7 Māori seats**, at about 6 overhang seats.
- **The split-list play scales with how many electorates the bloc leader wins.** From 2026, that's National's 42 against Labour's 21.

**What the existing Experiment 3 escalation runs show** (MMP, 5,000 simulated elections, grouped by which bloc has adopted the split-list play):

| Adopted by | Elections | Median overhang | National's overhang | Te Pāti Māori's | Minority-bloc majorities: right / left |
|---|---|---|---|---|---|
| Neither | 1,427 | 11 | 5 | 6 | 55 / 13 |
| Left only | 211 | 14 | 7 | 6 | 14 / 2 |
| Right only | 494 | 16 | 10 | 6 | 41 / 3 |
| Both | 2,868 | 27 | 15 | 6 | 340 / 2 |

When both blocs play, the left leader's general-seat overhang has a median of 1, rising to 7 by 2041. National's is 15. Te Pāti Māori's stays at 6 throughout.

**Minority-bloc majorities, all elections 2029–2041, right / left (of 5,000):**

| System | Baseline | Escalation |
|---|---|---|
| MMP | 215 / 64 | 450 / 20 |
| MMP-T-X | 265 / 21 | 265 / 21 (unchanged) |
| MMP141 | 78 / 136 | 327 / 59 |
| MMP-T-X141 | 183 / 46 | 183 / 46 (unchanged) |

**How to read this:**
- **Under MMP, escalation roughly doubles the right's minority-bloc majorities**, from 215 to 450, and cuts the left's from 64 to 20. That jump is the effect of gaming. The left can't keep up, because its strongest play is capped by the Māori seats.
- **Not all of the right tilt comes from gaming.** It persists under MMP-T-X (265 to 21), where gaming pays nothing. Two things cause it:
  - Under the grow fallback, National's plurality wins still add seats.
  - Under the bloc assignments, more of the threshold-wasted votes in these futures fall on the left (Opportunity counts as a left ally).
- **The asymmetry depends on geography and would flip** in an election like 2020, when Labour won 46 electorates. These are model results starting from the 2026 electoral map.

**For publicity:**
- Don't say "the status quo favours the right". That reads as partisan and isn't true in general.
- The defensible version is that **the current rules let whichever bloc dominates the electorates manufacture extra seats.** Today that's the right. In 2020 it would have been the left.
- The transfer applies the same rule to both sides. This symmetry is the transfer's best argument for an audience on the right. By contrast, applying the German rule in general seats only, with the Māori seats exempt, would delete National's overhang and keep Te Pāti Māori's. The right would see that as rigged.

### The fallback is part of the idea

The transfer needs a rule for overhang it can't cover. "Absorb" is the Review's rule, and the Spinoff piece's main objection to Option 1 applies to it directly. In Experiment 3 it is the only reform that does worse than MMP. So the transfer should be presented with the grow fallback: whatever the transfer can't cover is treated exactly as MMP treats it now. That also makes the comparison with MMP a clean one-variable change.

**"Grow" is the -X rule at today's size (MMP-T-X, 120/121), not the 141-seat House.** The 141-seat House is a separate add-on with a separate job. The obvious objection is "this doesn't stop the House growing". The answer is that the transfer changes *what* can make it grow. Under MMP, any overhang can grow the House, including engineered splitting. Under MMP-T-X, only overhang with no split ballots behind it can, which in practice means plurality sweeps. Experiment 3, share of elections in which the House exceeds its base size:

| System | > base | > base + 5 | > base + 10 | Max | Max if gaming escalates |
|---|---|---|---|---|---|
| MMP | 99% | 88% | 53% | +34 | +59 |
| MMP-T-X (121) | 56% | 11% | 1.9% | +17 | +17 (unchanged) |
| MMP141 | 99% | 74% | 24% | +30 | +56 |
| MMP-T-X141 | 31% | 0.4% | 0% | +9 | +9 (unchanged) |

What remains at 121 isn't transitional. Growth of more than 5 seats happens in 10–14% of elections every year from 2032 to 2041. The elections where it happens have a median raw overhang of about 15, mostly the leading party winning electorates on plurality. It is a structural consequence of 71 electorates against 49 list seats. The ways to deal with it are:

- **Grow** (MMP-T-X). There is no hard ceiling, but no gaming can push the House up.
- **Absorb** (MMP-T). It has a hard ceiling but hands seats to the plurality winner's bloc. It is the worst option on wrong winners.
- **Shrink the plurality residue at source**, with more list seats (141) or fewer electorates. This is the only route that solves it rather than choosing who bears it.

A capped hybrid (grow by up to N seats, then absorb) was considered and rejected. Critics value simplicity, and the transfer plus "leftover overhang is treated exactly as now" is one rule with no new parameters.

So 141 should be presented as the answer to plurality overhang, a problem the transfer doesn't claim to solve, not as part of the transfer.

---

## 2. Comparator systems: the Spinoff options on the same ballots

To show where the transfer sits among the ideas people are discussing, run as many of the ten options as practical on identical ballots.

| Spinoff option | System | Status |
|---|---|---|
| 1. Cap at 120; overhang absorbed (2012 and 2023 reviews) | MMP-A: absorption without transfer | In `model_2026.py` as `review_rule`; trivial to add to the Monte Carlo engines |
| 2. More list seats / fewer electorates | MMP141 exists. A 60:60 or 60:40 variant with fewer electorates doesn't | Fewer electorates needs merged-electorate geography. Medium effort; the main gap flagged in the overall report |
| 3. Compensation seats (Germany 2013–21) | Grow the House until no party is short by more than a seat | Already computed as "extra seats (a)"; promote it to a system |
| 4. Party vote overrides electorate wins (Germany 2023) | MMP-O: drop the overhanging party's lowest-margin winners | In `model_2026.py` as `germany_rule`; the simulations need electorate margins, which they have |
| 4′. Open letter: keep 1–2 overhang seats, then override | MMP-O2 | Small variant of MMP-O |
| 5. One combined vote | Force straight-ticket ballots | Easy: zero the split rates |
| 6. Weighted voting in the House | Voting weight equals party vote | No simulation needed: it is pure PR by construction. Note it only |
| 7. Ranked / multi-member electorates | – | Out of scope |
| 8. Abolish the Māori seats | – | Out of scope politically; omit |
| 9. Abolish electorates | Pure-PR benchmark | Already run (`mc_future_floor.py`) |

Each option's failure mode then has its own measure: list seats taken from the other bloc (1), House size (2, 3), unrepresented electorates (4), split ballots removed (5), and party votes reassigned (the transfer).

### The 2026 provisional result under the options (already in `results_2026.json`)

Fair share on qualifying party votes at 120 seats: Left (Labour, Green, TPM) 52.4 seats, Right 60.4, Opportunity 7.2.

| Rule | House | Left / Right | Right's gap from fair share | Electorates without their winner | Party votes reassigned | Who loses seats compared with current law |
|---|---|---|---|---|---|---|
| Current law | 131 | 57 / 67 | +1.0 (of a fair 66.0) | 0 | 0 | – |
| Option 1: Review cap | 120 | 50 / 64 | **+3.6** | 0 | 0 | Labour −5, Green −2, Opportunity −1, NZ First −2, ACT −1 |
| Option 4: German rule | 120 | 53 / 60 | −0.4 | **11** (7 National, 4 TPM) | 0 | National −7, TPM −4 |
| **Transfer (absorbing leftover)** | 120 | 52 / 61 | +0.6 | 0 | **~192,000 (8%)** | ACT −4, Labour −3, Green −2, NZ First −2 |
| Option 3: compensation (Spinoff figure) | ~142 | – | ~0 | 0 | 0 | none; 22 more MPs |

Split votes for 2026 are estimated from 2023 patterns. They should be rerun when the Electoral Commission publishes official results and split-vote tables.

**What this table shows:**

- **In 2026 current law is roughly bloc-fair.** National's and TPM's overhangs roughly cancel, which matches Experiment 3's "overhangs partly cancel" finding. The case against the status quo in 2026 is the 11 extra MPs and the incentive, not a tilt between the blocs.
- **The Review's cap is clearly the worst option**, as the Spinoff piece says.
- **The German rule is the transfer's real rival.** It is as proportional and costs no reassigned votes, but it leaves 11 electorates, four of them Māori seats, without the MP they elected.
- **The transfer's cost is concentrated.** About 28% of ACT's party votes and 11% of the Greens' are counted for the party whose candidates those voters elected. This is what needs defending, and the one-share argument is the way to defend it: those voters' ticks elected MPs beyond National's (or TPM's) entitlement, so without the transfer each of them counts twice.

**Proposed addition:** add a 2026 row to Experiment 2 Part A, with every comparator, as the headline table of the public-facing write-up. Also add the transfer with the grow fallback to `model_2026.py`: TPM's leftover can't be fully covered (f = 1.0), so the -X version gives a House of about 121.

---

## 3. Proportionality measures: a disclosed bracket

### The problem

We built one measure (one-share proportionality) that the reform satisfies almost by construction. A sceptical reader will discount any result that relies on it. The fix is to pair it with a measure tilted the other way, plus a standard baseline with no tweaks. Then report all three, and say which way each leans.

### Two tweaks, as two axes

There are two separate departures from the textbook index:

- **Threshold axis.** Are votes for parties below the threshold included in the yardstick?
  - *Included* is the standard Gallagher convention.
  - *Excluded* is what our "Gallagher" does now (`mc_overhang.py` `measures()`: `vt` sums qualifying parties only).
  - Excluding them takes the threshold out of the measure. That favours MMP and MMP-T over MMP-BV, which gets no credit for rescuing those votes.
- **Yardstick axis.** Is each ballot judged by its party vote as cast, or by the best one-share assignment (either the party vote or the electorate vote, never both)?
  - *As cast* favours MMP: it never credits the transfer.
  - *One-share* favours the reforms: it credits the transfer by construction.

That gives four measures:

| | Sub-threshold votes included | Sub-threshold votes excluded |
|---|---|---|
| **Party votes as cast** | **A. Baseline**: the standard Gallagher index. No tweak | **B.** Our current Gallagher. Leans towards MMP relative to the Backup Vote |
| **One-share (either vote)** | **C.** Leans towards MMP-BV most: rescued votes count | **D. The bundled measure.** The one-share principle among voters whose party vote counts |

### On your bundling question

Your intuition was to bundle the MMP-favouring tweak with the one-share measure, and keep a baseline with neither. For the transfer-only pitch that is exactly right, and here's why. Measure D isolates *only* the double-counting flaw:

- It doesn't credit the Backup Vote for rescuing sub-threshold votes, so it is neutral between MMP-T and MMP-BV.
- It doesn't penalise any system for the threshold, so it is neutral on the threshold debate.
- It does test whether every seat can be backed by one share per counted voter. That is the transfer's actual claim.

So the headline pair for the transfer pitch is **A (baseline) and D (the double-count measure)**. B and C go in an appendix, so a reader can see what each tweak does on its own. If the package (MMP-BV) were the pitch, C would matter and the threshold axis would be the main fight. That is another reason not to lead with the package.

One caveat on calling B "MMP-favouring": it favours MMP over MMP-BV, but it barely separates MMP from MMP-T, because both treat sub-threshold votes the same way (apart from the transfer's first step, which uses wasted votes on overhang ballots first). Against the transfer alone, the measure that genuinely favours MMP is **party votes counted as cast**. That is the cost measure in section 4, and it should sit next to the bracket.

### Making the one-share measure less permissive

All three earlier notes flagged that the one-share measure is too lenient. It picks the best assignment after the result is known. Large parties attract many split ballots: National's candidate vote was 43.5% against a 38.1% party vote in 2023. That lets almost any result pass. Proposed fix:

- **A split ballot's electorate vote may fill its share only if that candidate won.** A vote for a losing candidate elected no one, so it has no claim to count. This matches the principle (one share, through the vote that actually elected someone). It also cuts the slack hugely: only ballots behind winning candidates can move, which are exactly the transfer's pools.
- **Report each party's slack** (the range of vote shares the allowed assignments permit) alongside the score.
- **Keep the unrestricted version only as a sensitivity check.**

This also answers the open question in the Experiment 3 note ("how permissive is too permissive?") without an arbitrary within-bloc rule.

### Bloc-level versions

Apply the same two axes to the bloc seat deficit. The current bloc yardstick includes sub-threshold votes, which is what gives MMP-BV its bloc advantage. The overall report already concedes this. Report the bloc deficit as:

- **all votes** (current),
- **qualifying votes only** (the MMP-favouring version), and
- **split into threshold and system parts** using the pure-PR benchmark.

For the transfer pitch, the system part is the one that matters.

### What counts as a convincing result

- **Strong:** the transfer beats or ties MMP on A and B, the MMP-leaning measures, under adapted behaviour, and its cost on "votes counted as cast" is shown and modest.
- **Weak:** the transfer wins only on D. That shows internal consistency, nothing more.
- **On current evidence:**
  - With fixed ballots the transfer loses narrowly on B (Exp 2: 1.4 against 1.5).
  - Under adaptation it wins on B (Exp 3: 4.1 → 3.2 at 121, and 3.2 → 0.7 at 141).
  - A and D haven't been computed yet.

---

## 4. Consolidated measure set

This merges the three notes. The priority column reflects the transfer-first framing.

| Family | Measure | Leans towards | Priority | Source note |
|---|---|---|---|---|
| **Proportionality bracket** | A: standard Gallagher (all votes, as cast) | Neutral | Headline | New |
| | D: one-share Gallagher, qualifying voters, winning-candidate restriction, with slack | Reform (disclosed) | Headline | Exp 1–3, refined |
| | B: Gallagher, qualifying votes as cast (current) | MMP over MMP-BV | Appendix | Current |
| | C: one-share including rescued votes | MMP-BV | Appendix | Exp 1–3 |
| | Loosemore–Hanby and Sainte-Laguë index alongside Gallagher | Neutral; Sainte-Laguë weights small parties properly | Appendix | Exp 1, 2 |
| **Cost** | Party votes reassigned: overall, per party, and as a share of split voters | **MMP** | **Headline** | Exp 1–3 |
| | Seats each party loses to transfers (and how often a party loses 2 or more) | MMP | Headline | Exp 3 |
| | Electorates left without their winner | Penalises Option 4 | Headline (with comparators) | New |
| | Rescued as against overridden votes (distinguishes the transfer from the Backup Vote) | – | Appendix | Exp 1 |
| **Size and stability** | House: median, 95th, 99th, max; largest House per future; P(House > base + 5/10/20) | Penalises MMP, Option 3 | Headline | Exp 2, 3 |
| | Election-to-election change in House size | – | Appendix | Exp 3 |
| **Incentives** | Seats a bloc gains from engineered splitting, by system | Penalises MMP | Headline | Exp 3 |
| | Escalation scenarios, always shown as conditional ("if gaming spreads") | – | Headline | Exp 3 |
| | Minor-party sincerity penalty (supporters who waste both ticks by voting for their own candidate) | Penalises MMP-BV | Appendix (BV section) | Exp 1 |
| **Bloc fairness** | Bloc deficit: all votes / qualifying only / threshold part and system part | All-votes version favours MMP-BV | Secondary for the transfer pitch | Exp 1–3 |
| | Minority-bloc majority, with centrists counted with their ally and as a third group | – | Secondary | Exp 2, 3 |
| | Partisan bias at 50% and responsiveness | Neutral; shows which way a tilt runs | Secondary | Exp 3 |
| **Uncertainty** | Monte Carlo error bars; tails (95th/99th/worst) for every headline measure | – | Everywhere | Exp 2, 3 |

**Retire:**
- the general voter-share yardstick (circular);
- the rounded party seat deficit (overlaps with Gallagher);
- "extra seats (a)" as a measure. It becomes comparator Option 3.

**Re-base "extra seats (b)"** on the countable bloc yardstick, and show it as a curve: share of scenarios covered at each House size. That avoids the ">279" censoring.

---

## 5. Other project-level tweaks

**Method and comparability**
1. **One shared measures module** used by all three experiments (`mc_overhang.py`, `mc_calibrated.py`, `mc_future.py`), so every number is comparable. All three notes recommend this.
2. **Fix the measure set before rerunning, and report all of it.** Write section 4 into the module first, then rerun. That includes the measures where the transfer is expected to lose (B under fixed ballots, votes reassigned).
3. **Add the comparators in section 2** to every experiment's system list. Minimum: MMP-A (Review cap), MMP-O (German rule), and the compensation rule.
4. **Add the transfer with the grow fallback to the 2026 recount**, and rerun 2026 on official results and the published split-vote tables when they appear. The current 2026 numbers use estimated splits.

**Variants worth testing because of 2026**
5. **The explainer's optional cap**: no party loses more than one seat to transfers, with the remainder grown. ACT losing 4 of 13 seats in 2026 makes this politically important, and it hasn't been simulated.
6. **Transfer without its first step** (no use of sub-threshold votes first). This is the purest version of "the electorate vote counts instead". It tells us whether the first step is doing any of the work, and whether it drags Backup Vote objections into the transfer.
7. **Fewer electorates** (60 general and Māori electorates rather than 71) as an alternative to more list seats. It is Spinoff Option 2, and the main untested route to fixing plurality overhang without more MPs.

**Presentation**
8. **The ten hand-reasoned futures are illustration, not evidence.** Lead with the 1,000 walks.
9. **Bloc assignment robustness**: report the main bloc results with centrists as a third group, and with Opportunity unassigned (it is excluded from the blocs in the 2026 recount but counted as a left ally in Experiment 3, so these should be reconciled).
10. **Restructure `overall_report.md`** around the transfer. Proposed outline:
    - the principle;
    - the 2026 comparator table;
    - the ablation ladder;
    - the bracket of measures;
    - costs;
    - the escalation result;
    - then "optional extras": Backup Vote, 141 seats, lower threshold, each with its measured increment.

    The current bottom line (prefer MMP-BV-X141) becomes the answer to "if you want to go further".

---

## 6. Open questions for you

1. **Fallback in the headline.** Settled: MMP-T-X (grow), with no capped hybrid, for simplicity.
2. **Does the Backup Vote stay in the public piece at all**, or move to a separate threshold note alongside the 3.5% recommendation?
3. **Canonical bloc assignment**, especially Opportunity and Te Pāti Māori, for the headline figures.
4. **Escalation scenarios**: always conditional, or given a stated (if subjective) weight in any summary?
5. **The 2026 framing**: since current law is roughly bloc-fair in 2026 (the overhangs cancel), are we comfortable leading with House size and the incentive rather than unfairness? I'd recommend we are. It is what the data show, and it is the argument the Spinoff piece's "the genie is out of the bottle" line already accepts.
