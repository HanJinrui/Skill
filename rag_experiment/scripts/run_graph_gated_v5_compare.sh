#!/usr/bin/env bash
# Full Stage F compare (no_rag + graph_subtype_rag) with graph_gated_v5 extra config.
# Run from repo root. Optional: STAGE_F_LIMIT=12 to cap problems (forwarded as --limit).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

export RAG_CONFIG_EXTRA="${RAG_CONFIG_EXTRA:-config_graph_gated_v5.yaml}"
RUN_TAG="${STAGE_F_RUN_TAG:-graph_gated_v5}"
SEED="${STAGE_F_SEED:-0}"
LIMIT_ARGS=()
if [[ -n "${STAGE_F_LIMIT:-}" ]]; then
  LIMIT_ARGS=(--limit "${STAGE_F_LIMIT}")
fi
BASELINE_CONFIG_ARGS=()
if [[ "${STAGE_F_ISOLATE_BASELINE_CONFIG:-1}" != "0" ]]; then
  BASELINE_CONFIG_ARGS+=(--isolate-baseline-config)
fi
if [[ -n "${STAGE_F_BASELINE_CONFIG_EXTRA:-}" ]]; then
  BASELINE_CONFIG_ARGS+=(--baseline-config-extra "${STAGE_F_BASELINE_CONFIG_EXTRA}")
fi

run_one() {
  local manifest="$1"
  shift
  echo "=== Compare manifest=$manifest run_tag=$RUN_TAG RAG_CONFIG_EXTRA=$RAG_CONFIG_EXTRA ==="
  python3 rag_experiment/scripts/run_stage_f_compare.py \
    --eval-manifest "$manifest" \
    --baseline-vs-graph \
    --run-tag "$RUN_TAG" \
    --seed "$SEED" \
    --skip-graph-build \
    "${BASELINE_CONFIG_ARGS[@]}" \
    "${LIMIT_ARGS[@]}" \
    "$@"
}

run_one rag_experiment/outputs/eval_manifests/taco_test_family_difficulty_balanced_multi72.jsonl "$@"
run_one rag_experiment/outputs/eval_manifests/taco_test_family_difficulty_balanced_single120.jsonl "$@"

echo "=== Done. comparison_*_${RUN_TAG}.json under rag_experiment/outputs/stage_f/ ; reports comparison_report_*_${RUN_TAG}.md under reports/ ==="
