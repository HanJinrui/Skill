#!/usr/bin/env bash
# End-to-end driver. Run `cp .env.example .env` and set ZHIPU_API_KEY first.
set -euo pipefail
cd "$(dirname "$0")/.."

python scripts/run_stage_a.py
python scripts/run_stage_b.py
python scripts/run_stage_c.py
python scripts/run_stage_d.py
python scripts/run_stage_e_build_index.py
python scripts/run_stage_f_eval.py

echo
echo "Done. Metrics → outputs/stage_f/metrics_summary.json"
echo "Report  → ../reports/experiment_report.md"
