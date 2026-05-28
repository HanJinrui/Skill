#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}:${ROOT}/../rag_experiment:${PYTHONPATH:-}"
cd "$ROOT"
exec python -m sdf.pipeline --phase pass1 "$@"
