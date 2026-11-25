#!/bin/bash
# Bundle the large raw outputs (gitignored) into one archive for a GitHub Release.
# Usage: ./make_data_release.sh   -> dist/overhang-raw-data-YYYYMMDD.tar.gz
# Then attach it to a release, e.g. on github.com: Releases > Draft a new release.
set -e
cd "$(dirname "$0")"
mkdir -p dist
out="dist/overhang-raw-data-$(date +%Y%m%d).tar.gz"
files=$(ls runs/*/records.jsonl.gz runs/*/measures.csv paradox_results.csv paradox_recheck.csv 2>/dev/null)
tar -czf "$out" $files
echo "wrote $out ($(du -h "$out" | cut -f1))"
