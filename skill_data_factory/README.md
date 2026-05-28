# skill_data_factory

TACO / CodeContests -> skill distillation dataset pipeline (dual-track:
**single_algorithm** / **multi_algorithm**).

Produces curated evidence for [`rag_experiment`](../rag_experiment/) Stage D (DeepSeek-V4-Pro skill writer).

## Layout

| Path | Purpose |
|------|---------|
| `outputs/pass1_manifest/` | Shared TACO scan + verify + route stats |
| `outputs/single_algorithm/` | Subtype track (one mechanism per solution) |
| `outputs/multi_algorithm/` | Bundle track (true multi-mechanism compositions) |
| `outputs/reports/distillation_profile.md` | Size/quality dashboard |

## Quickstart

```bash
cd skill_data_factory
cp .env.example .env   # or symlink ../rag_experiment/.env

# Pilot (no LLM)
PYTHONPATH=.:../rag_experiment python -m sdf.pipeline --phase pass1 --limit-problems 100

# Full pipeline (requires DEEPSEEK_API_KEY for pass2)
./scripts/run_all.sh --resume

# In another terminal: one line per newly written labeled/quarantine row (works immediately)
./scripts/follow_pass2.sh --track single --interval 2

# After restarting pipeline with latest code, optional log filter:
# tail --follow=name --retry -n 0 -f run.log 2>/dev/null | grep --line-buffered 'Pass2 .* progress \['

# Stage D consumes factory data when configured in rag_experiment/config.yaml
cd ../rag_experiment
PYTHONPATH=src python scripts/run_stage_d.py --v2 --skill-writer deepseek
```

## Pass summary

1. **Pass1** — Stream TACO train, run official tests (`min_tests>=5`), route to single/multi/quarantine.
2. **Pass2** — Rule candidates + **mandatory** DeepSeek-V4-Pro labeling (no `rule_only` finals).
3. **Pass3** — Evidence packets + `distillation_rows` / `composition_rows` for Stage D.

## Labeling policy

- Final `primary_subtype` (single track) or `composition_subtypes` (multi track) **must** come from DeepSeek.
- Failed / invalid LLM rows go to `pass2_label/quarantine.jsonl`.

## RAG retrieval

1. Retrieve **subtype** skills from single track first.
2. If query looks multi-skill, also retrieve **bundle** skills from multi track.

## CodeContests 多算法扩充

CodeContests 使用独立配置和输出目录，不覆盖当前 TACO evidence：

```bash
cd skill_data_factory
docker pull python:2.7.18-slim-buster  # 仅 PYTHON (Python 2) evidence 需要

# 在 .env 中配置三把 key；Pass2 默认以 9 workers 轮转调用（三把 key 各约 3 路）
# DEEPSEEK_API_KEYS=your_key_1,your_key_2,your_key_3

# 本地验证 CodeContests train 的 PYTHON3/PYTHON 正确解，默认每解最多 20 条分层测试
# CodeContests 配置默认 streaming=true，会边读 train 分片边验证并持续输出进度
PYTHONPATH=.:../rag_experiment python -m sdf.pipeline \
  --config configs/codecontests_multi.yaml --phase pass1 --tracks multi

# DeepSeek 组合标注与 evidence 导出
PYTHONPATH=.:../rag_experiment python -m sdf.pipeline \
  --config configs/codecontests_multi.yaml --phase pass2 --tracks multi
PYTHONPATH=.:../rag_experiment python -m sdf.pipeline \
  --config configs/codecontests_multi.yaml --phase pass3 --tracks multi

# 合并 TACO 与 CodeContests，自动排除重复题及现有 TACO test manifest 泄漏
PYTHONPATH=.:../rag_experiment python -m sdf.pipeline \
  --config configs/codecontests_multi.yaml --phase merge
```

新增来源字段包括 `source_dataset`、`source_language`、
`verification_source`、`source_problem_fingerprint`、`test_selection_policy`、
`selected_test_counts` 与 `family_evidence_method`。CodeContests 的 `PYTHON`
解在 Python 2.7 Docker 容器中验证，仅作为证据；最终生成模板仍为 Python 3。

合并后的多算法 ledger 位于
`outputs/merged_multi_algorithm/pass3_evidence/composition_rows.jsonl`，并附有
`merge_report.json` 与 `excluded_codecontests_rows.jsonl`。

`pass2.max_workers` 可在 `configs/codecontests_multi.yaml` 中调整；如果 API
限流明显，将默认的 `9` 下调为 `6` 或 `3` 后用 `--resume` 继续运行。
