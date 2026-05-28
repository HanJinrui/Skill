#!/usr/bin/env bash
# Live Pass2 DeepSeek labeling progress (run in a second terminal).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${ROOT}/../rag_experiment:${PYTHONPATH:-}"
cd "$ROOT"
INTERVAL=15
TRACK=both
ONCE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --interval) INTERVAL="$2"; shift 2 ;;
    --track) TRACK="$2"; shift 2 ;;
    --once) ONCE="--once"; shift ;;
    *) echo "Usage: $0 [--interval SEC] [--track single|multi|both] [--once]"; exit 1 ;;
  esac
done
exec python scripts/watch_pass2_progress.py --interval "$INTERVAL" --track "$TRACK" $ONCE
