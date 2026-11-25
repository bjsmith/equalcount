# One ballot, counted twice: overhang reform under MMP

Analysis of overhang seats in New Zealand's MMP system, and of the **Overhang Transfer**: when a party wins more electorate seats than its party vote entitles it to, count just enough of the split ballots behind those seats as though the party vote had followed the electorate vote.

**Website:** the GitHub Pages site is built into [`docs/`](docs/):

- `docs/index.html`: interactive explainer using the 2023 election (`docs/2026/` for the 2026 preliminary count)
- `docs/report/`: the full report and its appendices (Experiments 1–3)
- `docs/data/`: index of every dataset and script

This is a working draft. The analysis is still being refined.

## Layout

| Where | What |
|---|---|
| `overall_report.md` | The full report. `experiment1_report.md`, `report_experiment2.md` and `report_experiment3.md` are its appendices |
| `overhang-transfer-explainer.md` | Plain-language explainer of the proposal |
| `site/` | Source of the interactive explainers |
| `data/raw/` | Electoral Commission inputs, 2005–2026 |
| `mc_*.py`, `model*.py`, `measures.py` | Simulation and seat-allocation code (see `docs/data/` for a one-line description of each) |
| `runs/`, `futures*/`, `mc_results*.csv`, `results_*.json` | Simulation outputs |

The raw ballot states (`runs/*/records.jsonl.gz`), per-run measures (`runs/*/measures.csv`) and paradox-search tables are too large for git. `make_data_release.sh` bundles them for a GitHub Release.

## Rebuilding

```bash
pip install -r requirements.txt
python3 build_site.py                                                      # regenerate docs/ from the sources above
OVERHANG_REPO_URL=https://github.com/<user>/<repo> python3 build_site.py   # also link file names to GitHub
./run_all_measures.sh                                                      # rerun every experiment (several hours)
```

Preview locally with `python3 -m http.server 8765 --directory docs`.

## Publishing

On GitHub: Settings → Pages → Deploy from a branch → `main` / `/docs`.
