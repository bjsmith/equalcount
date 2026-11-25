#!/bin/bash
# Rerun Experiments 1–3 storing raw ballot states, then compute every measure from them.
# Outputs: runs/<experiment>/records.jsonl.gz (raw), measures.csv (derived).
set -e
cd "$(dirname "$0")"
python3 mc_history.py store
python3 mc_future_walks.py 1000 --store
python3 mc_future_walks.py 1000 --copycat --store
python3 mc_future_walks.py 1000 --escalation --store
python3 mc_overhang.py store 5000
python3 mc_calibrated.py store 5000
python3 measures.py recompute runs/exp2_history runs/exp3_baseline runs/exp3_copycat runs/exp3_escalation runs/exp1 runs/exp2
echo ALL DONE
