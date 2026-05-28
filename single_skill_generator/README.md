# Single Skill Generator

本目录只保留当前发布版 Skill Bank 的可复现材料，以及在需要重新挖掘证据时使用的上游生成代码。本阶段不包含 RAG 索引、检索路由或 Stage E/F 评测。

## 应保存的内容

```text
single_skill_generator/
├── configs/
│   ├── final_release.yaml              # 当前发布构建配置
│   └── upstream/                       # 需要重建冻结输入时才使用
├── data/                               # catalog、curated evidence 与 alias registry
├── inputs/final_release/               # 构建最终 bank 的冻结输入快照
├── outputs/final_release/              # 当前可交付输出
├── prompts/                            # DeepSeek 生成/修订提示词
├── src/                                # 生成、规范化、retrieval gate 与校验代码
└── tests/                              # 回归测试
```

`inputs/final_release/` 是必要输入，不应删除：

| 文件 | 用途 |
| --- | --- |
| `base_skill_bank.jsonl` | 原始 19 条 single skill 快照 |
| `legacy_generation_inputs.jsonl` | legacy skill 的真实 TACO evidence ledger 来源 |
| `targeted_additions_bank.jsonl` | 35 条新增 skill 的初始生成快照 |
| `targeted_additions_evidence.jsonl` | 新增算法的 TACO/curated 混合证据 |
| `llm_cache/` | 已验收的 GCD 定向重生成结果缓存，避免重建时再次请求模型 |

## 当前发布输出

以 [single_skill_bank_merged.jsonl](outputs/final_release/single_skill_bank_merged.jsonl) 作为当前单算法 Skill Bank 主文件。

| 文件 | 用途 |
| --- | --- |
| `single_skill_bank_merged.jsonl` | 54 条 normalized canonical single skills |
| `single_skill_bank_additions.jsonl` | 本轮新增的 35 条 canonical single skills |
| `composed_skill_bank_additions.jsonl` | 隔离发布的 `graph_gcd_mst_dsu` 组合技能 |
| `normalized_evidence_rows.jsonl` | 成熟度和代表例选择所用的规范化 evidence ledger |
| `subtype_registry.json` | canonical、alias、present/planned 节点注册表 |
| `maturity_report.json` | unique TACO problem 与 maturity 结果 |
| `retrieval_gate_report.json` | generator-local top-3 retrieval gate 结果 |
| `evidence_routing_report.json` | binary-search 证据拆分记录 |
| `schema_validation_report.json` | schema 与 Python 模板校验报告 |
| `composition_evidence_quarantine.jsonl` | 从单算法隔离出的组合 evidence |
| `repair_report.json` | 本次发布构建摘要和输入校验和 |

## 重建发布版

已验收输出可以直接使用。需要根据冻结输入重新写出发布文件时：

```bash
cd single_skill_generator
python -m src.final_release --config configs/final_release.yaml --regenerate-gcd
python -m pytest tests/ -q
```

`--regenerate-gcd` 会优先命中保留的 `inputs/final_release/llm_cache/`；缓存不存在时才需要配置 `DEEPSEEK_API_KEY`。

## 重新构建上游输入

通常无需运行以下流程。仅当你希望从 verified solutions 重新挖掘证据或重新生成新增 skill 时使用；产物写到 `work/`，不会覆盖发布输出。

```bash
# 原始 TACO 蒸馏流程
python -m src.main --config configs/upstream/base_generation.yaml --mode prepare
python -m src.main --config configs/upstream/base_generation.yaml --mode generate

# 35 条 targeted additions 证据与生成流程
python -m src.main --config configs/upstream/targeted_additions.yaml --mode prepare-evidence
python -m src.main --config configs/upstream/targeted_additions.yaml --mode prepare
python -m src.main --config configs/upstream/targeted_additions.yaml --mode generate
```

## 安装与密钥

```bash
pip install -r requirements.txt
export DEEPSEEK_API_KEY=your_key
```

本地 `.env` 可用于存放密钥，不应对外发布。
