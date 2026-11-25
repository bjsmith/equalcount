# 2026 General Election — preliminary count

Source: https://www.electionresults.govt.nz/electionresults_2026_preliminary/
(read 9 November 2026, 100% of preliminary results counted; special votes not included).

- `electorates.csv`: one row per electorate, from the `electorate-details-NN.html`
  pages and `successful-candidates.html`. Party votes for the 7 parties that
  qualify for seats, with all other parties summed as OTHER.
- `national.csv`: nationwide party votes from the overall results page.

Split-vote tables are not published for the preliminary count, so `model.py`
estimates them from the 2023 general/Māori electorate split patterns
(`data/raw/2023/split-votes-general.csv`, `split-votes-maori.csv`).
