# 2026 General Election — official count

Source: https://www.electionresults.govt.nz/electionresults_2026/
(read 27 November 2026, official count including special votes; not yet the
formal declaration in the NZ Gazette).

- `electorates.csv`: one row per electorate, from the `electorate-details-NN.html`
  pages. Winner and runner-up (party is the party whose party vote sits beside
  the candidate on the page; `IND` if none), and party votes for the 7 parties
  that qualify for seats, with all other parties summed as OTHER.
  `total_votes` is the party-vote total including informals;
  `candidate_total` is the electorate-vote total including informals.
  Checked: each electorate's party and candidate columns add up to its totals,
  and party votes summed over electorates equal the nationwide totals.
- `national.csv`: nationwide party votes from the overall results page.
  Seats: National 40, Labour 36, Green 17, ACT 13, NZ First 12,
  Opportunity 7, Te Pāti Māori 5 = 130 (10 overhang).

Split-vote tables are not yet published for the official count (the E9 report
is due by 18 December 2026), so `model_2026.py` still estimates them from the
2023 general/Māori electorate split patterns.
