#!/usr/bin/env bash
# One line per new labeled/quarantine row (polling — no inotify, no grep on run.log).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
TRACK=single
INTERVAL=2
while [[ $# -gt 0 ]]; do
  case "$1" in
    --track) TRACK="$2"; shift 2 ;;
    --interval) INTERVAL="$2"; shift 2 ;;
    *) echo "Usage: $0 [--track single|multi|both] [--interval SEC]"; exit 1 ;;
  esac
done
exec python3 scripts/follow_pass2_progress.py --track "$TRACK" --interval "$INTERVAL"
