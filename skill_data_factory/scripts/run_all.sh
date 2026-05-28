#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${ROOT}/../rag_experiment:${PYTHONPATH:-}"
cd "$ROOT"
TRACKS="single,multi"
RESUME=""
LIMIT=""
BUDGET=""
CONFIG=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --resume) RESUME="--resume"; shift ;;
    --limit-problems) LIMIT="--limit-problems $2"; shift 2 ;;
    --budget) BUDGET="--budget $2"; shift 2 ;;
    --tracks) TRACKS="$2"; shift 2 ;;
    --config) CONFIG="--config $2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done
exec python -m sdf.pipeline --phase all --tracks "$TRACKS" $RESUME $LIMIT $BUDGET $CONFIG
