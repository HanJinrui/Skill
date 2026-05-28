#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}/src:${ROOT}/../rag_experiment/src:${PYTHONPATH:-}"
cd "$ROOT"
exec python -m sdf.pipeline --phase pass3 --tracks single "$@"
