# Keeping Parliament proportional when votes are split

### A proposal for handling overhang seats under MMP

> This explainer describes a **proposed change**. It is not current law.

---

## In brief

- **Everyone counts once.** Every voter gets an equal share of Parliament's proportionality. You fill that share with your party vote or with your electorate vote, but never with both.
- Normally your party vote fills it. Your electorate vote fills it only if the MP you elected has no party votes behind their seat, which is what an **overhang seat** is.
- Want to be sure your share goes to one party? Tick that party twice.
- Today, a split ballot that elects an overhang MP counts twice: once for the MP and again, in full, for another party. Groups of parties can use this deliberately to win more seats than their combined party vote earns.
- The proposal keeps every electorate MP and keeps Parliament at 120. It counts only as many split ballots as needed towards the electorate MP's party, and uses party votes that would otherwise be wasted first.
- **It's fair between blocs.** Each group of parties ends up with about its combined share of the party vote.
- **It changes the incentives.** Splitting your vote no longer wins your side extra seats, so parties stop asking for it. If that works, the rule will rarely be needed.

---

## How MMP works now

When you vote, you tick:

1. **a party**: this decides how many seats each party gets in Parliament overall
2. **a candidate in your electorate**: this decides who represents your local area.

After the election, each party that gets at least 5% of the party vote (or wins an electorate) is given a share of the 120 seats based on its party vote. This uses a calculation called the **Sainte-Laguë formula**.

Electorate MPs are seated first. Each party's remaining seats are filled from its list.

### What is an overhang?

An overhang happens when a party wins **more electorates than its party vote entitles it to**.

For example, if a party's party vote gives it 37 seats but it wins 40 electorates, it has 3 overhang seats.

Under current law, the party keeps all 40 electorate seats and the other parties keep their full share. Parliament grows to fit everyone in. In 2023, overhang seats took Parliament to 123 seats.

---

## The problem: split voting by design

Overhangs used to happen by accident. Now some voters split their votes **on purpose**, to give a group of parties more seats than their combined party vote would earn.

It works like this:

- Voters who support a group of parties give their **electorate vote** to the biggest party in the group, which wins the electorates.
- They give their **party vote** to a smaller partner party.
- The big party wins more electorates than its party vote entitles it to.
- The partner party gets its full share of list seats as well.
- Together, the group ends up with more seats than its share of the party vote.

This can be done by any group of parties. It undermines the main purpose of MMP: that Parliament reflects how people voted.

---

## The principle: everyone counts once

The best way to think about this proposal isn't as moving anyone's vote. It's as **everyone getting an equal say in what Parliament looks like**.

Under MMP, the party vote decides each party's share of Parliament, **including** its electorate seats. A party's electorate MPs come out of the share its party vote earns. So for most voters, the electorate vote decides *who* their local MP is, and the party vote decides *how Parliament is made up*.

An overhang seat breaks this. It's a seat with no party votes behind it. The voters who elected that MP have already shaped Parliament's make-up through their party vote for another party, and now they've added a seat on top. Their ballot counts twice. Everyone else's counts once.

The proposal fixes this by giving every voter **one equal share** of Parliament's proportionality:

| Your ballot | What fills your share |
|---|---|
| Both ticks for the same party | That party. Always. |
| Split, and your electorate MP's seat is covered by their own party's votes | Your party vote, exactly as today |
| Split, and your electorate MP would be an overhang seat | Your electorate vote, or part of it, only as much as is needed to cover that seat |
| Party vote for a party that didn't qualify | Your electorate vote, if your MP needs it. Today this vote counts for nothing. |

Nobody's vote is thrown away. The question is only *which* of your two choices fills your one share. And if you want to be certain it's a particular party, you can tick that party twice.

---

## The proposal

When a party would have an overhang, a share of the split ballots that helped cause it fill their voters' share of Parliament through the **electorate vote** rather than the party vote. In practice, these ballots are counted **as if the party vote followed the electorate vote**. Only as many as are needed are counted this way, and the size of Parliament stays the same.

### How it works, step by step

**Step 1: Apply the threshold**
Work out which parties qualify for seats, using the normal rules. This is done **before** any votes are moved, so no party can drop below the threshold because of a transfer.

**Step 2: Check for an overhang**
Allocate seats using Sainte-Laguë as normal. If any party has won more electorates than its seat entitlement, continue. If not, the result stands.

**Step 3: Use wasted votes first**
Look at ballots where:

- the electorate vote went to a **winning candidate** of the overhanging party, **and**
- the party vote went to a party that **didn't qualify** for seats.

Those party votes would otherwise count for nothing. Count them for the party whose candidate the voter chose, **only as many as needed** to cover the overhang. If that's enough, stop here.

**Step 4: Transfer a proportional share of other split votes**
If an overhang remains, look at ballots where:

- the electorate vote went to a winning candidate of the overhanging party, **and**
- the party vote went to a **different qualifying party**.

The same small fraction (called *f*) of each of these party votes is transferred to the overhanging party. Every eligible ballot is treated the same way. No ballots are chosen at random.

Because every eligible ballot gives up the same fraction, each party loses votes in proportion to how many of its voters split this way. Parties whose voters rarely split this way lose very little.

**Optional safeguard: cap the loss**
No party can lose more than one seat through transfers. If an overhang remains after the cap is reached, the remaining overhang is handled by giving other parties fewer list seats, as the Independent Electoral Review recommended. (See [Concerns about small parties](#concerns-about-small-parties).)

**Step 5: Allocate seats**
Allocate the 120 seats using Sainte-Laguë with the adjusted party votes. The overhanging party's entitlement now matches its electorate seats, and every other party's share is proportional.

---

## Worked example

This example uses made-up parties and numbers. Party B is Party A's likely coalition partner.

- Party A wins **40 electorates**.
- Party E gets 96,000 party votes but doesn't reach the threshold.

### Split ballots for Party A's winning candidates

| Party vote went to | Number of ballots |
|---|---|
| Party E (didn't qualify) | 12,000 |
| Party B | 150,000 |
| Party C | 20,000 |
| Party D | 10,000 |

### Results

| Party | Party votes (before) | Seats under current law | After Step 3 | Party votes (after) | Final seats |
|---|---|---|---|---|---|
| A | 720,000 | 40 *(37 + 3 overhang)* | 38 | 759,967 | **40** |
| B | 360,000 | 19 | 19 | 336,694 | **17** |
| C | 840,000 | 44 | 43 | 836,893 | **43** |
| D | 384,000 | 20 | 20 | 382,446 | **20** |
| E | 96,000 | 0 | 0 | 84,000 | 0 |
| **Total** | | **123** | 120 | | **120** |

**What happened:**

1. **Step 3:** All 12,000 wasted Party E votes were counted for Party A. This took Party A from 37 to 38 seats. It still needed 2 more.
2. **Step 4:** The fraction needed was *f* = 0.1554, or about 15.5% of each eligible split vote:
   - 23,306 votes moved from Party B
   - 3,107 votes moved from Party C
   - 1,554 votes moved from Party D
3. **Step 5:** Party A's entitlement now equals its 40 electorates. Parliament stays at 120.

**The effect:**

- Under current law, Parliament has 123 seats and Parties A and B together hold **59**.
- Under the proposal, Parliament has 120 seats and Parties A and B together hold **57**. That's close to their combined share of the party vote (about 47%, or 56 seats). The small difference comes from wasted Party E votes, and a small number of votes from Parties C and D, that followed their voters' electorate choice.

---

## A real example: the 2023 general election

In 2023, Te Pāti Māori won **6 electorates** but its party vote (3.08%) entitled it to only **4 seats**. That created **2 overhang seats**, and Parliament grew to 122.¹

### Who split their vote

These are voters in the six electorates Te Pāti Māori won who gave their electorate vote to the Te Pāti Māori candidate but their party vote to another party.

| Where the party vote went | Split ballots (electorate vote for Te Pāti Māori's winning candidate) | Of those, party votes counted for Te Pāti Māori under the proposal |
|---|---|---|
| Parties below the threshold (wasted) | 3,010 | 3,010 *(all of them, Step 3)* |
| Labour | 23,696 | 19,953 |
| Green | 8,248 | 6,945 |
| National | 2,920 | 2,459 |
| NZ First | 2,637 | 2,220 |
| ACT | 536 | 451 |
| **Total** | **41,047** | **35,038** *(84% of the rest, Step 4)* |

The wasted votes alone weren't enough to cover even one seat. Step 4 needed *f* = 0.842, meaning **84% of each eligible split vote** was moved. That's a large share, because the overhang was concentrated in just six electorates. In Waiariki, for example, 59% of people who party-voted Labour also voted for Rawiri Waititi.

### Seats under each approach

| Seats won | Current law (House grows) | 2023 Review's rule (overhang absorbed in 120) | Germany's 2023 rule (uncovered winners not seated) | This proposal (Overhang Transfer) |
|---|---|---|---|---|
| National | 48 | 47 | 48 | 48 |
| Labour | 34 | 34 | 34 | 33 |
| Green | 15 | 14 | 15 | 14 |
| ACT | 11 | 11 | 11 | 11 |
| NZ First | 8 | 8 | 8 | 8 |
| Te Pāti Māori | 6 | 6 | 4 | 6 |
| **Size of Parliament** | **122** | **120** | **120** | **120** |
| *Left bloc: Labour + Green + Te Pāti Māori (44.1% of counted party votes)* | *55 (45.1%)* | *54 (45.0%)* | *53 (44.2%)* | *53 (44.2%)* |
| *Right bloc: National + ACT + NZ First* | *67 (54.9%)* | *66 (55.0%)* | *67 (55.8%)* | *67 (55.8%)* |

### What this shows

**Te Pāti Māori keeps its 6 seats, and that's all.** Its share of Parliament rises only because Parliament shrinks: from 6 of 122 seats to 6 of 120.

**The cost falls on its allies.** The votes that make up Te Pāti Māori's 6 seats come mostly from Labour and Green party votes, so Labour and the Greens each lose a seat. The left bloc's share of Parliament falls from 45.1% to 44.2%. Every other party's share rises, and National's rises most (from 39.3% to 40.0%).

**This is the intended result.** The left bloc won 44.1% of the party votes that counted towards seats, but the overhang gave it 45.1% of Parliament. The proposal brings the bloc back to 44.2%, almost exactly its proportional share.

**It's worse for the left bloc than the review's rule.** The review's rule takes the overhang seats from all other parties, so National would have lost a seat. Under this proposal, the parties whose voters created the overhang bear its cost.

**Germany's rule gives the same bloc totals, but at a high price.** The two Te Pāti Māori candidates with the lowest vote shares (in Te Tai Tokerau and Tāmaki Makaurau) would not have taken their seats. Two of the seven Māori electorates would have been left without the MP their voters chose.

¹ *National's later 123rd seat came from the Port Waikato by-election, held because a candidate died during the campaign. It isn't covered by this example.*

*Split-ballot figures are calculated from the Electoral Commission's published split-voting percentages for each electorate, so they may differ from exact counts by a few votes.*

---

## Fair between blocs

Governments in New Zealand are formed by groups of parties, so the question that matters most is whether each **group** gets its fair share of Parliament.

### Why the proposal gets blocs right

Strategic splitting happens **inside** a group: an ACT voter ticks the National candidate, or a Labour voter ticks the Te Pāti Māori candidate. When the proposal counts some of those ballots for the electorate MP's party, the votes move from one partner to the other. **The group's total party vote doesn't change.**

Once the overhang is covered, every party's seats are proportional to its counted votes. So each group's seats end up close to its **combined party vote**, which is the share it would get if nobody split at all.

| | Group's share of party vote | Current law | This proposal |
|---|---|---|---|
| **2023:** Labour, Green, Te Pāti Māori | 44.1% (52.9 of 120) | 55 of 122 (45.1%) | 53 of 120 (44.2%) |
| **2023:** National, ACT, NZ First | 55.9% (67.1 of 120) | 67 of 122 (54.9%) | 67 of 120 (55.8%) |
| **2026\*:** Labour, Green, Te Pāti Māori | 45.0% (54.0 of 120) | 58 of 130 (44.6%) | 54 of 120 (45.0%) |
| **2026\*:** National, ACT, NZ First | 48.9% (58.7 of 120) | 65 of 130 (50.0%) | 59 of 120 (49.2%) |
| **2026\*:** Opportunity | 6.1% (7.3 of 120) | 7 of 130 (5.4%) | 7 of 120 (5.8%) |

*\*2026 uses the official count, with split votes estimated from 2023 patterns.*

The rule works on parties, not blocs. Nobody has to define which parties are allies. Fairness between blocs is a result of the rule, not a separate step in it.

### Where it isn't exact

The bloc result is close, but not perfect, for four reasons:

- **Some splitters cross blocs.** A Labour voter who ticks a popular local National MP gets counted the same way as an ACT voter who does. Those ballots move votes **into** the overhanging party's group. In the 2026 estimate, about 25,000 Labour, Green and Opportunity votes would move to National. That's part of why the right gets 59 seats, not 58.7. That seems fair: those voters did choose a National MP.
- **Wasted votes join the group.** Party votes for parties that didn't qualify are used first, and they go to the overhanging party's group. Today they count for nobody.
- **Rounding.** Sainte-Laguë works in whole seats, so each group can be up to about half a seat off.
- **Very large overhangs.** If there aren't enough split votes to cover the overhang, the remainder is handled by the review's rule, which takes seats from every other party. This happens in the 2026 estimate for Te Pāti Māori, whose party vote was very small compared with its five electorates.

### What changes inside a bloc

The proposal keeps each group's total about right, but it changes the **split within** the group. In the 2026 estimate, National keeps 40 seats while ACT drops from 13 to 9 and NZ First from 12 to 10. In 2023, Labour and the Greens each lose a seat while Te Pāti Māori keeps 6.

This is the point of the rule. ACT's 13 seats under current law include the share of ACT voters who had already filled their share of Parliament by electing a National MP. Under the proposal, each of those voters counts once.

### When both blocs split

The 2026 estimate shows something the 2023 example doesn't. When **both** groups create overhangs, the effects roughly cancel at the bloc level. The parties that lose out are the ones **in neither group**. Opportunity won 6.1% of the counted party vote but would get only 5.4% of a 130-seat Parliament. The proposal brings it back to 5.8%.

---

## It changes the incentives

The biggest effect of the proposal may not be the votes it counts differently. It's what it does to how parties campaign.

### Splitting no longer pays

Today, a group of parties can win extra seats by asking its supporters to split: electorate vote for the big partner, party vote for the small one. Under the proposal, that tactic gains the group **nothing**. Any overhang it creates is covered by the group's own party votes, and its total seats stay about where its combined party vote puts them.

For anyone trying to change the government, the double-counted split vote stops being a way to get there.

### Partners start competing for electorates

Once splitting stops paying the group, it starts **costing the smaller partner**. Every electorate its supporters win for the big partner beyond its entitlement is paid for out of the smaller partner's party vote.

- **Small parties that rely on the party vote, alongside a big party that wins electorates** (ACT and NZ First alongside National): they'll want to stop National winning more electorates than its party vote covers. So they'll stand serious candidates, contest electorates, and ask their supporters to tick ACT or NZ First twice.
- **Big parties that rely on the party vote, alongside a small party that wins electorates** (Labour and the Greens alongside Te Pāti Māori): they'll want to stop Te Pāti Māori winning electorates its party vote doesn't cover. So they'll put more into their own electorate campaigns, especially in the Māori electorates, and ask their supporters to tick Labour or Green twice.

Normally, competing for electorates inside your own group carries a risk: split the vote between partners and the other side might win the seat. Under MMP without overhangs, that doesn't change the group's total seats. Losing an electorate only changes **which** MP represents it. The other side's electorate seat comes out of its own party vote.

### The rule that makes itself unnecessary

If parties stop asking for strategic splits, and partners compete for electorates instead of handing them over, overhangs become rare. Then the rule rarely has to move any votes at all.

**The incentive change is the whole point.** The counting rule is mainly there to make strategic splitting pointless. If it works, voters will hardly ever see it used.

### What won't go away

Some overhangs aren't planned:

- **Local MPs with a strong personal vote.** Some voters will always back a well-liked local MP from a party they don't party-vote for.
- **Parties built around electorates.** A party can be strongest where it stands candidates, as Te Pāti Māori is in the Māori electorates, while its party vote nationally is small.
- **Fragmented Parliaments.** When many parties share the vote, big parties can win most electorates on less than half the vote in each.

For these, the counting rule still does the work. These are also the cases where the safeguards in [Concerns about small parties](#concerns-about-small-parties) matter most.

---

## Doing the calculation on paper

The calculation can be shown in a short table. It doesn't need a computer.

Sainte-Laguë works by dividing each party's votes by 1, 3, 5, 7 and so on. These results are called **quotients**. The 120 highest quotients win seats.

The overhanging party needs its quotient for its last electorate seat to make the top 120. For a party with **E** electorate seats, that quotient is its votes divided by **(2E − 1)**.

As *f* goes up, the overhanging party's quotients rise and the rival parties' quotients fall. For each rival quotient that's currently ahead, the point where the overhanging party catches it is:

> **f = [(2E − 1) × v<sub>p</sub> − (2k − 1) × v<sub>A</sub>] ÷ [(2k − 1) × S + (2E − 1) × s<sub>p</sub>]**

where:

- **v<sub>A</sub>** = the overhanging party's votes (after Step 3)
- **v<sub>p</sub>** = rival party p's votes
- **k** = which of party p's quotients this is (1st, 2nd, 3rd…)
- **S** = the total number of eligible split votes
- **s<sub>p</sub>** = how many of those went to party p.

**To find *f*:**

1. Count how many rival quotients the overhanging party needs to overtake. Call this **m**.
2. Work out the catch-up point for each rival quotient near the line.
3. Sort them from smallest to largest. The m-th one is *f*.

In the example, Party A needed to overtake **5** rival quotients. The fifth catch-up point was *f* = 0.1554.

---

## Why transfer a proportional share?

| Approach | What it does | Drawback |
|---|---|---|
| **Current law** | Overhang party keeps its extra seats; Parliament grows | Groups of parties can gain seats by splitting votes |
| **Independent Electoral Review (2023)** | Overhang party keeps its seats; other parties get fewer list seats | The overhanging group still gains; the seats just come from the other side |
| **Germany (since 2023)** | Electorate winners only take their seat if the party vote covers it | Some electorates end up without the candidate who won the most votes. In New Zealand, this would mainly affect Māori electorates, which makes it unworkable here |
| **This proposal** | A calculated share of split votes follows the electorate vote | Overrides some voters' party choice, in a small and predictable way |

The proposal:

- keeps every electorate MP
- keeps Parliament at a fixed size
- treats every eligible ballot the same way
- gives the same result on a recount
- removes the reason to split votes strategically, because the group no longer gains seats by doing it.

If voters know that splitting won't increase their group's seats, most will stop doing it. In practice, transfers may rarely be needed.

---

## Alternatives worth considering

### Option 1: Partial wasted-vote transfer (as above)

Wasted votes are used first, but **only as many as needed** to cover the overhang. This still needs the catch-up calculation, but keeps the change narrow: it only applies when there's an overhang.

### Option 2: All wasted party votes follow the electorate vote

A simpler, broader rule: whenever a party vote goes to a party that doesn't qualify for seats, it's counted for the party of the voter's electorate candidate instead (if that party qualifies).

- **Benefit:** No calculation needed for this step. Fewer votes are wasted at every election, not just when there's an overhang.
- **Drawback:** It's a bigger change to how votes are counted. It's similar to the "spare vote" idea, which the Independent Electoral Review discussed in its 2023 report.

Under either option, Step 4 still applies if an overhang remains.

---

## Concerns about small parties

Some people may worry that this proposal is unfair to small parties. Small parties rarely win electorates, so many of their supporters give their electorate vote to a big party's candidate. If that big party has an overhang, some of those small-party votes could be moved.

### Where the concern is fair

The concern is strongest when Parliament is fragmented. If small parties together win a large share of the party vote, big parties can win most electorates with less than half the votes in each. That can create an overhang that nobody planned.

In that case, small-party supporters who sincerely voted for a big party's local candidate could lose part of their party vote, even though nobody was trying to game the system. Asking them to give both votes to their own party isn't a full answer, because it means giving up a say in who their local MP is.

### Why the proposal is still fairer than the alternatives

**The cost has to fall on someone.** An overhang seat isn't free under any rule:

- Under **current law**, Parliament grows and every vote is worth a little less.
- Under the **review's rule**, the seats come out of every other party's list.
- Under **this proposal**, the cost falls on the parties whose voters helped create the overhang.

In the [worked example](#worked-example), Party D, a small party whose voters rarely split, does **better** under this proposal than under the review's rule (20 seats compared to 19). The question isn't really big parties against small parties. It's which small parties pay.

**It isn't big parties against small parties.** Every overhang in New Zealand so far has been created by a small party winning electorates. In 2023, the proposal moved votes **towards** Te Pāti Māori, a small party. The rule applies to whichever party has the overhang, whatever its size.

**The effect is limited.** Each overhang seat needs roughly 22,000–24,000 votes to be moved, spread across every eligible split ballot. A party only loses a seat if its voters make up a large share of the split ballots.

**No party can be pushed out of Parliament.** The threshold is applied before any votes are moved.

**The current system isn't neutral either.** When an overhang happens now, the bloc that creates it gets more seats per vote than everyone else. Small parties outside that bloc lose out, but quietly.

### Safeguards that could help

**Cap the loss.** No party loses more than one seat through transfers. Anything left over is handled the way the review recommended. This still removes most of the reward for strategic splitting, while making sure no small party can be badly hurt by an overhang it didn't plan.

**Fix the ratio of electorate seats to list seats.** The review recommended keeping electorate seats at 60% of Parliament. That would make unplanned overhangs by large parties very rare, so transfers would mostly apply when voters split on purpose.

**An exemption that wouldn't work:** excusing voters whose party didn't stand a candidate in their electorate. Allied parties could simply withdraw their candidates to avoid the rule.

---

## "Isn't this disregarding my vote?"

This is the most important objection to the proposal, and it deserves a straight answer.

### What the proposal does change

For some voters, the electorate vote, not the party vote, fills their share of Parliament. That means their share goes to a different party from the one they ticked for their party vote. This is a real cost. The proposal is only justified if it brings a bigger gain in fairness.

### Every voter still gets the same share

It helps to look at what each voter **gets**, not what they give up. Every voter gets exactly one equal share of Parliament's make-up. A voter whose electorate vote elects an overhang MP has already used their share: their MP holds a seat that no party votes paid for. Counting their party vote in full as well would give them two shares.

So the proposal doesn't take something away from those voters. It stops them getting more than everyone else.

### Your vote isn't thrown away

If your share is filled by your electorate vote, it still counts in full towards seats in Parliament. It counts for the party of the candidate you chose in your electorate. Both parties were chosen by you, on the same ballot paper. And if you want to be sure your share goes to one party, you can give that party both your ticks.

Compare this with current law: a party vote for a party that doesn't reach the threshold counts for nothing at all.

### The aim is equal votes, not smaller ones

Under MMP, the party vote decides each party's share of Parliament, **including** its electorate seats. A party's electorate seats are normally taken out of the share its party vote earns.

When a party has an overhang, its extra electorate seats aren't taken out of anything. So a split ballot that helps elect an overhang MP counts twice:

- once to win the electorate seat
- and again, in full, towards another party's share of seats.

That gives those ballots more weight than other people's. Everyone else's vote ends up worth a little less.

### What this looked like in 2023

| | Party votes | Seats | Party votes per seat |
|---|---|---|---|
| **Current law** | | | |
| Labour, Green and Te Pāti Māori | 1,186,291 | 55 of 122 | 21,569 |
| National, ACT and NZ First | 1,505,877 | 67 of 122 | 22,476 |
| **This proposal** | | | |
| Labour, Green and Te Pāti Māori | 1,186,291 | 53 of 120 | 22,383 |
| National, ACT and NZ First | 1,505,877 | 67 of 120 | 22,476 |

*Party votes are the votes each group of parties actually received, before any transfer.*

Under current law, the group of parties with the overhang needed about 900 fewer votes to win each seat. Under the proposal, the gap almost disappears. The same would apply in the other direction if National, ACT or NZ First created an overhang.

### This principle isn't new

- The **Royal Commission on the Electoral System**, which recommended MMP in 1986, listed fairness between political parties as one of its main tests for a voting system.
- In 2012, **Germany's Federal Constitutional Court** ruled that large numbers of overhang seats breached the principle that every vote should carry equal weight.

### Votes are already transferred in other systems

New Zealand voters already accept a vote being partly moved to another choice they made. Under the **Single Transferable Vote (STV)**, used in some New Zealand local elections, when a candidate gets more votes than they need, a fraction of every one of their ballots is passed on to each voter's next choice.

This proposal works the same way. The only difference is that the "next choice" is the other tick on your own ballot paper.

### The rules are known in advance

Every voting system has rules that decide how votes turn into seats, such as the 5% threshold. This rule would be published before the election, so voters know how their ballot will be counted.

### In short

Voters who split their vote still get both of their choices: their candidate is elected, and their party vote still counts. What they don't get is a ballot that counts for more than everyone else's.

---

## Questions and answers

**Is my vote being thrown away?**
No. Every voter gets one equal share of Parliament's make-up. If your electorate vote fills that share, it still counts in full, for the party of the candidate you voted for. The rule only stops one ballot from counting twice. (See ["Isn't this disregarding my vote?"](#isnt-this-disregarding-my-vote))

**How do I make sure my share goes to the party I want?**
Give that party both your ticks. A ballot with the same party for both votes is never counted differently.

**Won't this just be gamed in some new way?**
The usual workaround for overhang rules is a "decoy" party that only stands electorate candidates while its supporters party-vote a partner. Under this proposal, the decoy's overhang is covered by its partner's party votes, so the group gains nothing. (See [It changes the incentives](#it-changes-the-incentives).)

**Does this change who wins my electorate?**
No. Every electorate winner keeps their seat.

**Could my party vote be moved?**
Only if all of these are true:

- you split your vote
- your electorate vote went to a winning candidate
- that candidate's party has an overhang.

Even then, only a fraction of your party vote is counted differently, and only as much as is needed across everyone in the same situation.

**Could a party fall below the threshold because of this?**
No. The threshold is applied before any votes are transferred.

**Does it favour any party?**
No. It applies the same way to any party with an overhang, whatever its politics. In 2023 it would have cost the left bloc a seat. In 2026 it could cost the right bloc seats.

**Why not just copy Germany?**
Germany doesn't seat electorate winners whose party vote doesn't cover them. In New Zealand, most overhangs have come from Māori electorates. Under Germany's rule, two Māori electorates would have been left without the MP their voters chose in 2023. That isn't workable here.

**Why not just pick ballots at random?**
Random selection could give a different result each time votes are counted. Using the same fraction for every ballot gives the same result on any recount.

---

*This explainer describes a proposal for discussion. It does not describe current electoral law in Aotearoa New Zealand.*
