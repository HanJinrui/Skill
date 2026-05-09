# 实验报告：保守层级 Skill RAG
- Scope: `multi`, eval source: `manifest:taco_test_family_difficulty_balanced_single120.jsonl`, RAG mode: `graph_subtype_rag`, retrieval only: `False`
- Total problems: 72, total runs: 216

## 核心指标
- **PASS@1** = 0.0509
- Sample pass rate = 0.0509
- First-sample pass rate (r0) = 0.0694
- **PASS@3** = 0.0694
- Single-skill PASS@3 = 0.0694 (5/72)
- Multi-skill PASS@3 = 0.0000 (0/0)

## 检索统计
- Total retrieval calls: 76
- Total hits: 67
- Overall correct-retrieval rate: 0.8816
- Router top1 acc: 0.8816
- Family recall@k: 0.8816
- Subtype recall@k: 0.0000
- Bundle recall@k: 0.0000
- Hit to pass conversion: 0.0702
- False mechanism rate: 0.0000
- Avg retrieval calls per problem: 1.06
- Avg correct retrievals per problem: 0.93

## 新旧流水线差异
- 旧路径以 family skill card 为主，弱 query 信号容易被 Graph RAG 放大。
- 新路径采用 router -> family -> subtype -> optional bundle，默认只注入 top1 subtype 和 1 个 prototype。
- multi-skill 只用于 bundle/composition，不再参与纯 subtype 定义。

## 新旧检索差异
- `flat_family_rag` 保留旧 family 粒度对照。
- `subtype_rag` 使用 Stage D v2 层级 skill，保守 family filter 后检索 subtype。
- `graph_subtype_rag` 使用 subtype-level graph，hydration 不再伪造 matched signals/mechanisms。

## 为什么更稳定
- 弱证据时 QuerySchema 不再开启全部 family。
- 在线 query 不再从 family_hint 展开全 mechanism。
- 泛目标信号如 maximize/minimize/construct 不再作为强传播证据。
- prompt 不再默认塞 3 张宽泛 card，减少误导生成。

## 当前问题
- subtype gold 依赖 Stage C primary_solution，测试集或 manifest 可能没有 subtype gold。
- `graph_subtype_rag` 需要先重建 `outputs/stage_e/graph_index_v2`。
- retrieval-only 只能衡量检索质量，不能替代完整 PASS@k 生成评测。

## Per-family breakdown

| family | problems | PASS@3 | PASS@1 | retrieval hit rate |
| --- | ---: | ---: | ---: | ---: |
| bit_manipulation | 11 | 0.1818 | 0.0909 | 1.0000 |
| complete_search | 11 | 0.0909 | 0.0909 | 0.8750 |
| data_structures | 13 | 0.0000 | 0.0000 | 0.7500 |
| dynamic_programming | 12 | 0.0000 | 0.0000 | 0.8571 |
| greedy_algorithms | 12 | 0.0000 | 0.0000 | 0.8462 |
| range_queries | 4 | 0.2500 | 0.1667 | 1.0000 |
| sorting | 9 | 0.1111 | 0.1111 | 1.0000 |
