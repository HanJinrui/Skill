# Multi-Algorithm Skill Generator

从 `composition_rows.jsonl` 蒸馏多算法组合 skill 库（按有序 `composition_signature` 聚类）。

## 快速开始

```bash
cd multi_skill_generator
pip install -r requirements.txt

# 统计输入与聚类（不调用 LLM）
python -m src.main --config configs/multi_skill_config.yaml --mode inspect

# 过滤、标准化、顺序修复、分组、生成 LLM 输入
python -m src.main --config configs/multi_skill_config.yaml --mode prepare

# 调用 DeepSeek 生成 / 审查 / 修订 skill
export DEEPSEEK_API_KEY=...
python -m src.main --config configs/multi_skill_config.yaml --mode generate

# 校验 skill bank
python -m src.main --config configs/multi_skill_config.yaml --mode validate
```

输入默认：`data/composition_rows.jsonl`（指向 `skill_data_factory` 的 pass3 输出）。

Prompts are in English (aligned with `single_skill_generator` and English skill JSON fields).

## MVP 范围

- 规则修复 `composition_order`（LLM 修复默认关闭）
- 仅对 `support_count >= 3` 的组合生成 skill
- 要求 `composition_order` 与 subtypes 一致后才进入聚类

## 输出

- `outputs/multi_skill_bank.jsonl` — 通过校验的 multi skill
- `outputs/multi_skill_generation_inputs.jsonl` — 每簇 LLM 输入
- `outputs/multi_skill_evidence_map.json` — 来源追踪
- `outputs/multi_skill_generation_report.json` — 运行报告
- `outputs/logs/` — 各阶段报告

## 测试

```bash
python -m pytest tests/ -q
```

## CodeContests 扩充发布

在 `skill_data_factory` 已生成 merged composition ledger 后，使用独立候选输出：

```bash
# 可直接复用 ../skill_data_factory/.env 中的：
# DEEPSEEK_API_KEYS=your_key_1,your_key_2,your_key_3
# configs/codecontests_merged_config.yaml 默认 9 workers + round_robin。
python -m src.main --config configs/codecontests_merged_config.yaml --mode inspect
python -m src.main --config configs/codecontests_merged_config.yaml --mode prepare
python -m src.main --config configs/codecontests_merged_config.yaml --mode generate
python -m src.main --config configs/codecontests_merged_config.yaml --mode validate
python -m src.main --config configs/codecontests_merged_config.yaml --mode publish
```

扩充版 skill 的 `evidence` 保存数据集、验证方式和源语言统计。
`publish` 只有在候选 bank 验证通过、包含全部当前基线 skill ID 且 skill
总数严格增长时才会覆盖主 `outputs/multi_skill_bank.jsonl`，并先写出基线快照。
遇到 provider 限流时，将配置中的 `llm.max_workers` 从 `9` 调低后重跑
`generate`；已缓存的成功调用不会再次消耗 API。
