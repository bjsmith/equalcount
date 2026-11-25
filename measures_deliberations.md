# Measures deliberations

Notes on how the overhang experiments measure outcomes, what each measure captures and misses, and proposed changes. Written from Experiment 3 (future elections from 2026). Most points apply equally to Experiment 1 (wide synthetic space) and Experiment 2 (calibrated to 2005–2023).

## 1. Current measures

| Measure | Definition | What it captures | Known problems |
|---|---|---|---|
| **Gallagher index** | Least-squares gap between each qualifying party's seat share and its share of the qualifying party vote | Conventional party-level proportionality | Judges only against raw party votes, so it penalises the Backup Vote for its intended reassignment of wasted votes |
| **Party seat deficit (rounded)** | Each qualifying party's seat shortfall against its party-vote share, rounded, then summed | Which parties lose out | Ignores who gains; largely overlaps with Gallagher |
| **Bloc seat deficit** | Seats the worse-off bloc is short of its share of *all* party votes, including votes for parties below the threshold | Whether the blocs get seats in line with votes | Mixes two causes: the threshold and the overhang rule (see 3a). Depends on how parties are assigned to blocs (3e) |
| **Countable bloc yardstick** | The bloc yardstick without voters whose party vote and electorate vote both went to non-qualifying parties | Used for "extra seats needed" (Experiments 1–2) | Only meaningful where some rule could count those voters |
| **Minority-bloc majority** | The bloc with fewer party votes holds a House majority | Wrong-winner risk | Binary; driven by close elections; depends on bloc assignment |
| **Overhang** | Electorates won beyond entitlement on raw party votes at the system's size | The raw problem | Says nothing about who bears the cost |
| **House size** | Seats in the resulting House | Stability | Reported as median and maximum only; trajectory and volatility not captured |
| **Votes moved** | Party votes transferred under MMP-T / MMP-BV | Scale of the reform's intervention | Not expressed per voter (3c) |

## 2. Proposed new measure: one-share proportionality

### Rationale

The proposal's principle is that every voter fills **one share** of Parliament, through either their party vote or their electorate vote, never both. None of the current measures tests that directly.

Overhang seats under MMP are, in effect, voters counted twice. The Labour and Green voters who ticked Te Pāti Māori candidates elect TPM's MPs, and their party votes also fund Labour and Green list seats. A measure built on the one-share principle makes that flaw visible and measurable.

### Definition

- Each ballot is a pair (party vote *q*, electorate candidate's party *c*). It may fill its share through *q* if *q* qualifies, or through *c* if *c* qualifies. Ballots where neither qualifies are excluded, as in the countable bloc yardstick.
- An **assignment** decides, for every split ballot, which choice fills its share. Fractional assignments are allowed, since only totals matter. Every assignment counts each voter exactly once.
- **One-share Gallagher index:** the minimum, over all assignments, of the Gallagher index between seat shares and assigned vote shares.
- **One-share seat deficit:** the minimum, over all assignments, of the summed rounded party shortfall. A bloc version is defined the same way.
- **Slack:** for each party, the range of vote shares any assignment allows, from all its split ballots going out to all split ballots naming it coming in. Always report it alongside the measure.

Computation: a small convex quadratic programme over the split-ballot flows. Inputs are the party-vote × candidate-party tables we already have for every real and simulated election.

### Expected behaviour

| System | Expected one-share score | Why |
|---|---|---|
| MMP with overhang | Clearly positive | No assignment explains both the overhanging party's seats and its allies' full list seats |
| MMP-T / MMP-BV (no absorption) | About zero | The transfer is itself an assignment |
| MMP-T / MMP-BV (absorption) | Positive | Other parties lose seats that no assignment justifies |
| -X variants (House grows) | Positive | Leftover overhang seats are backed by no voter |
| Pure PR on party votes | About its ordinary Gallagher (~0.4) | Party votes are a valid assignment; the remainder is rounding |

### Caveats

1. **It's partly tautological.** The reform is built to satisfy this measure, so a near-zero score is evidence of internal consistency, not independent evidence of fairness. Frame it as *"does each system honour the one-share principle, and how badly does MMP violate it?"*
2. **It's permissive.** The best assignment is chosen after the result is known. Big parties attract many split ballots from voters who personally like their candidates: in 2023 National's candidate vote was 43.5% against a 38.1% party vote. An allocation giving such a party several extra seats could score zero. Hence the need to report slack, and always to pair this measure with the party-vote Gallagher index.

## 3. Other proposed changes

In order of value:

### a. Split the bloc seat deficit into threshold and system parts

The Experiment 3 benchmark (pure PR on the same ballots, `mc_future_floor.py`) showed that most of MMP's bloc imbalance comes from the 5% threshold. Of MMP's median bloc seat deficit of 2.2, about 1.4 remains even under pure PR.

- **Threshold component:** the pure-PR bloc deficit on the same ballots.
- **System-attributable component:** the system's bloc deficit minus the threshold component.

This isolates what the overhang rule is responsible for. On this basis MMP-BV-X141's system component is about zero.

### b. Partisan bias and responsiveness

Replace or supplement the binary minority-bloc measure with the standard seats–votes measures:

- **Bias:** a bloc's seat share at 50% of the vote, minus 50%.
- **Responsiveness:** seats gained per one-point vote swing.

Both are continuous, show which way any tilt runs, and can be estimated from the thousands of close simulated elections. They would also settle whether MMP's gaming systematically favours one side or roughly cancels.

### c. Voter-level cost of the reform

Critics will ask how many voters have part of their party vote reassigned. Report:

- the share of all voters, and of split voters, whose party vote is partly transferred;
- how often, and by how many seats, a party loses seats to transfers.

This is the legitimacy cost, and it belongs alongside the benefits.

### d. Stability and escalation

Experiment 3's strongest result concerns trajectory, so the measures should too:

- the distribution of the **largest House in each future**;
- the probability that the House exceeds the set size by **5, 10 or 20 seats**;
- **volatility:** the election-to-election change in House size;
- the **payoff to engineered splitting:** seats a bloc gains from split-list or Māori-seat strategies under each system. This is the incentive itself, and it explains why the reforms are immune to escalation.

### e. Robustness to how parties are assigned to blocs

Every bloc measure depends on assumptions: Opportunity as a left ally, centrists' allies, and Māori parties' alignment. Report the main bloc results under at least one alternative, for example:

- centrists excluded;
- centrists assigned by the government they supported;

so readers can see the conclusions don't hinge on these choices.

### f. A separate Gallagher index for the Backup Vote

For the MMP-BV systems only, also report Gallagher against backup-adjusted votes, since seats are allocated on that basis. The party-vote Gallagher index then shows the reassignment's cost, and the adjusted one shows whether the system works as designed. Don't use the adjusted yardstick for other systems; it measured them against a rule they don't apply.

### g. Uncertainty and pruning

- Report Monte Carlo error bars on headline rates. With 1,000 walks, a 5% rate is about ±0.6 points.
- Present the 10 hand-reasoned futures as illustration, not evidence.
- Retire the general voter-share yardstick (replaced by 2 and 3f).
- Once 2 and 3a are in place, consider dropping the rounded party seat deficit, which largely overlaps with Gallagher.

## 4. Suggested final set of measures

| Purpose | Measure |
|---|---|
| Conventional proportionality | Gallagher (party vote); Gallagher (backup-adjusted, BV systems only) |
| The reform's principle | One-share Gallagher and one-share seat deficit, with each party's slack |
| Bloc fairness | Bloc seat deficit, split into threshold and system parts; partisan bias and responsiveness |
| Wrong winners | Minority-bloc majority, per election and per future, shown alongside bias |
| Stability | House size distribution; largest House per future; probability of exceeding the set size by 5, 10 or 20 |
| Incentives | Payoff to engineered splitting, by system |
| Cost | Share of voters with part of their party vote transferred; seats lost to transfers |

## 5. Open questions

- **How permissive is too permissive?** Should the one-share measure cap each split ballot's influence, for example allowing reassignment only within a bloc? That was rejected as a *seat rule* because it's arbitrary, but it might be acceptable as a measurement convention.
- **The threshold.** Should the threshold be treated as a legitimate design choice, and excluded from fairness measures, or as a source of unfairness, and included? The answer decides whether the bloc yardstick should count votes for sub-threshold parties at all.
- **Which bloc assignment counts as canonical** for the headline results?
- **Wrong winners and coalitions.** Should a "minority-bloc majority" count when the decisive centrist party could join either side?
- **Weighting the escalation scenarios.** How should they be weighted against the baseline when summarising expected outcomes, or should they only ever be presented as conditional ("if escalation occurs")?
