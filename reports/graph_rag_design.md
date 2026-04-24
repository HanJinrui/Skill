# Graph RAG 设计文档：面向算法技能检索的机制感知异构图检索系统

## 1. 文档目的

本文档为 `algo-skill-factory/rag_experiment` 项目提供一套完整、可落地、可直接交给 Cursor 执行的 Graph RAG 设计方案。

目标不是复刻通用 GraphRAG，也不是简单照搬论文 *Graph of Skills*，而是设计一套更适合当前项目的数据形态和任务目标的 **Algorithm Skill Graph RAG**：

- 面向算法题技能检索，而不是工具脚本依赖检索
- 面向“机制匹配”和“多技能组合”，而不是单纯文本相似度
- 与现有 Stage A-F 流程兼容
- 可以逐步替换当前 `Stage E` 的平面 BM25 + dense + RRF 检索方案


## 2. 当前项目现状与核心问题

### 2.1 当前流水线

当前项目的主要流程为：

1. `Stage A`：从 TACO 中选题
2. `Stage B`：问题级技能标注
3. `Stage C`：解法级技能标注与一致性分类
4. `Stage D`：生成 skill card
5. `Stage E`：构建 RAG 检索索引
6. `Stage F`：使用 skill RAG 辅助代码生成并评估

### 2.2 当前 Stage E 的实现特点

当前 `Stage E` 的索引构建和检索逻辑具有以下特点：

- 每个 skill card 被拍平成一段长文本
- 对这段长文本做 BM25 token 化
- 对这段长文本做 dense embedding
- 在线检索时直接拿题面文本作为 query
- 用 BM25 + dense + RRF 得到 top-k skill

相关位置：

- `rag_experiment/src/rag/build_index.py`
- `rag_experiment/src/rag/retrieve.py`
- `rag_experiment/src/rag/pipeline.py`

### 2.3 当前方案的主要问题

对于算法技能检索，当前“单文档平面检索”的问题很明显：

1. **技能是结构化对象，不是单段文档**
   - `skill_name`
   - `families`
   - `applicable_when`
   - `problem_signals`
   - `core_idea`
   - `template_strategy`
   - `common_pitfalls`
   - `complexity_pattern`
   - `retrieval_text`

2. **算法题匹配需要“机制对齐”，而不仅仅是语义对齐**
   - 相似措辞不等于相同机制
   - 同一机制可以有完全不同题面叙述
   - 多技能组合在算法题中很常见

3. **长文本 flatten 会稀释关键信号**
   - 复杂度信号
   - 输入结构信号
   - 操作模式信号
   - 判定/构造/计数/最优值等目标信号

4. **当前检索无法显式区分“相近但错误”的技能**
   - 例如 `sorting` 与 `greedy_algorithms`
   - `complete_search` 与 `dynamic_programming`
   - `data_structures` 与 `range_queries`

5. **当前检索不显式建模 multi-skill**
   - 现有项目已经有 `skills_multi.jsonl`
   - 但检索时仍然主要把 skill 当成独立文本项


## 3. 设计目标

### 3.1 主要目标

新 Graph RAG 方案必须满足以下目标：

1. 优先匹配 **算法机制**
2. 支持 **单技能** 与 **多技能组合**
3. 能显式利用：
   - family 先验
   - 输入结构
   - 约束规模
   - 操作模式
   - 复杂度档位
   - 代表题原型
4. 支持“图证据”输出，便于解释检索结果
5. 能与现有 Stage B/C/D 产物直接对接
6. 先以离线构建、在线高效检索为目标

### 3.2 非目标

本方案不追求：

- 通用文档 GraphRAG
- 面向网页/API/工具调用的技能依赖检索
- 直接替换 Stage B/C/D 的标注逻辑
- 用 LLM 做重度在线推理式检索


## 4. 总体方案概览

### 4.1 核心思想

本项目应构建的是：

**Mechanism-Aware Heterogeneous Skill Graph RAG**

核心思想不是“skill 到 skill 的依赖图”，而是：

**题目信号 -> 算法机制 -> 技能卡 -> 代表题原型**

在线检索时，不是简单找 top-k 文本，而是：

1. 先从题面抽取结构化 Query Schema
2. 再进行多视图 seed retrieval
3. 在异构图上做受约束的 typed propagation
4. 再进行 bundle assembly
5. 最后输出预算内最优的技能子图

### 4.2 与论文 GoS 的关系

可借鉴 GoS 的部分：

- 离线建图
- hybrid semantic + lexical seeding
- typed propagation
- budgeted reranking

不直接照搬的部分：

- GoS 强调工具/脚本 prerequisite
- 本项目更需要机制节点、原型节点、负边、multi-skill 组合节点
- 本项目不是“执行链完整性”优先，而是“算法机制完整性”优先


## 5. 图 Schema 设计

本项目建议采用 **异构图**，图中至少包含以下节点类型和边类型。

### 5.1 节点类型

#### A. `SkillNode`

来源：

- `outputs/stage_d/skills_single.jsonl`
- `outputs/stage_d/skills_multi.jsonl`
- `outputs/stage_d/skills_merged.jsonl`

字段建议：

```json
{
  "node_type": "skill",
  "skill_id": "single__dynamic_programming",
  "skill_name": "Dynamic Programming",
  "scope": "single|multi",
  "families": ["dynamic_programming"],
  "applicable_when": [],
  "problem_signals": [],
  "core_idea": "",
  "template_strategy": [],
  "common_pitfalls": [],
  "complexity_pattern": "",
  "retrieval_text": "",
  "num_source_examples": 0
}
```

#### B. `FamilyNode`

来源：

- 当前 8 个 core family

字段建议：

```json
{
  "node_type": "family",
  "family_id": "dynamic_programming",
  "display_name": "dynamic_programming"
}
```

#### C. `MechanismNode`

含义：

- 比 family 更细粒度的算法机制单元

示例：

- `prefix_sum`
- `difference_array`
- `fenwick_tree`
- `segment_tree`
- `sliding_window`
- `monotonic_stack`
- `sort_then_greedy`
- `state_transition_dp`
- `bitmask_enumeration`
- `small_state_search`
- `offline_queries`
- `heap_maintenance`

字段建议：

```json
{
  "node_type": "mechanism",
  "mechanism_id": "sliding_window",
  "families": ["amortized_analysis"],
  "aliases": ["two_pointers", "window expansion and shrink"],
  "description": "maintain a valid moving window with amortized O(n) pointer movement"
}
```

#### D. `SignalNode`

含义：

- 题面中可观察到的高价值检索信号

示例：

- `many_range_queries`
- `point_update`
- `subarray`
- `n_le_20`
- `n_le_2e5`
- `maximize`
- `minimize`
- `count_ways`
- `tree_input`
- `string_input`

字段建议：

```json
{
  "node_type": "signal",
  "signal_id": "many_range_queries",
  "category": "operation|constraint|shape|goal|keyword",
  "surface_forms": ["many queries", "q queries", "range query", "queries on intervals"]
}
```

#### E. `PrototypeProblemNode`

来源：

- `Stage A` 题面
- `Stage B` 问题标签
- 与某个 skill 相关联的代表问题

作用：

- 作为 skill 的“题面原型检索视图”

字段建议：

```json
{
  "node_type": "prototype_problem",
  "prototype_problem_id": "proto_prob__single__dynamic_programming__001",
  "problem_id": "taco_train_000014",
  "problem_summary": "",
  "problem_text_snippet": "",
  "problem_skills": ["dynamic_programming"],
  "signals": [],
  "input_shape": [],
  "constraint_tags": []
}
```

#### F. `PrototypeSolutionNode`

来源：

- `Stage C` 中 consistent / partial 的 solution-level 记录

作用：

- 作为“代码机制原型”的证据节点

字段建议：

```json
{
  "node_type": "prototype_solution",
  "prototype_solution_id": "proto_sol__single__dynamic_programming__001",
  "problem_id": "taco_train_000014",
  "solution_id": "s0",
  "detected_multi_skills": ["dynamic_programming"],
  "core_mechanism_summary": "",
  "ast_hints": [],
  "ast_features": {},
  "consistency_type": "consistent"
}
```

#### G. `BundleSkillNode`

含义：

- 对应现有 `Stage D` 的 multi skill card
- 用于显式建模多技能组合

说明：

- 从物理上可以继续作为 `SkillNode(scope=multi)` 存储
- 逻辑上需要作为 bundle 型 skill 处理


## 6. 边类型设计

### 6.1 核心正向边

#### 1. `skill_has_family`

```text
SkillNode -> FamilyNode
```

权重：

- 固定为 `1.0`

#### 2. `family_has_mechanism`

```text
FamilyNode -> MechanismNode
```

作用：

- 建立 family 到细粒度机制的层次关系

#### 3. `skill_implements_mechanism`

```text
SkillNode -> MechanismNode
```

来源：

- `core_idea`
- `template_strategy`
- `problem_signals`
- `retrieval_text`
- 对应 family 的典型机制词典

#### 4. `skill_triggered_by_signal`

```text
SkillNode -> SignalNode
```

来源：

- `applicable_when`
- `problem_signals`
- 代表问题中的约束/关键词抽取

#### 5. `prototype_problem_supports_skill`

```text
PrototypeProblemNode -> SkillNode
```

作用：

- skill 的题面原型支持

#### 6. `prototype_solution_supports_skill`

```text
PrototypeSolutionNode -> SkillNode
```

作用：

- skill 的机制实现原型支持

#### 7. `prototype_problem_has_signal`

```text
PrototypeProblemNode -> SignalNode
```

#### 8. `prototype_solution_uses_mechanism`

```text
PrototypeSolutionNode -> MechanismNode
```

来源：

- `ast_features`
- `ast_hints`
- `core_mechanism_summary`

#### 9. `bundle_contains_skill`

```text
BundleSkillNode -> SkillNode
```

作用：

- 将 multi-skill bundle 与其组件单技能关联起来

#### 10. `skill_cooccurs_skill`

```text
SkillNode <-> SkillNode
```

来源：

- `Stage B/C` 中共同出现的多技能组合
- `Stage D` 中 multi skill card 的成分

权重建议：

- PMI
- 或归一化共现频率

### 6.2 负向边

#### 11. `skill_conflicts_skill`

```text
SkillNode -x- SkillNode
```

作用：

- 处理易混淆但不应同时高分的 skill

示例：

- `sorting` 与某些纯 `greedy_algorithms`
- `complete_search` 与某些伪 DP 描述
- `data_structures` 与 `range_queries` 的误召回

来源建议：

- family 层先验冲突表
- 历史误检样本
- 规则层显式定义

#### 12. `mechanism_conflicts_mechanism`

```text
MechanismNode -x- MechanismNode
```

示例：

- `segment_tree` 与 `sliding_window`
- `bitmask_dp` 与 `simple_sort_then_scan`


## 7. 离线构建流程设计

### 7.1 总体输入

离线图构建使用以下现有产物：

- `outputs/stage_a/selected_problems_multi.jsonl`
- `outputs/stage_b/problem_labels.jsonl`
- `outputs/stage_c/solution_consistent.jsonl`
- `outputs/stage_c/solution_inconsistent.jsonl`
- `outputs/stage_c/solution_labeled.jsonl`
- `outputs/stage_d/skills_merged.jsonl`

### 7.2 离线构建步骤

#### Step 1. 标准化 SkillNode

对 `skills_merged.jsonl` 中每条记录做标准化，生成 skill 节点主表。

要求：

- 保留所有原字段
- 新增标准化 facet 字段
- 新增多视图检索文本字段

建议新增字段：

- `mechanism_tags`
- `signal_tags`
- `input_shape_tags`
- `operation_tags`
- `goal_tags`
- `complexity_tags`
- `negative_tags`

#### Step 2. 构建机制词表与信号词表

创建项目内置的检索知识库：

- family -> mechanisms
- mechanism -> signals
- signal -> surface forms

建议完全规则优先，避免引入在线不稳定依赖。

#### Step 3. 从 Stage C 构建原型节点

从 `solution_consistent.jsonl` 和高质量 `partial` 中抽取：

- 代表题目原型
- 代表解法原型

选择策略建议：

- 每个 skill 最多 8 个 prototype problem
- 每个 skill 最多 8 个 prototype solution
- 优先保留：
  - `consistent`
  - `llm_confidence` 高
  - `label_source = glm_ast_fused`

#### Step 4. 自动抽取 query-facing facet

从题面和 skill 字段中抽取：

- 输入结构
- 约束规模
- 操作模式
- 优化目标
- 关键 artifact/关键词

这些 facet 不依赖模型，建议规则化实现。

#### Step 5. 建边

按前文 schema 建边，并在边上保存：

- `weight`
- `source`
- `evidence`
- `created_by`

例如：

```json
{
  "edge_type": "skill_triggered_by_signal",
  "src": "single__range_queries",
  "dst": "many_range_queries",
  "weight": 0.92,
  "source": "rule+skill_fields",
  "evidence": ["problem_signals[2]", "retrieval_text"]
}
```

#### Step 6. 构建多视图索引

不要只构建一个 skill 文本索引，至少构建以下几类索引：

1. `skill_master` 索引
2. `signal_view` 索引
3. `prototype_problem` 索引
4. `prototype_solution` 索引
5. `facet_inverted_index`

#### Step 7. 持久化图和索引

建议输出到：

```text
rag_experiment/outputs/stage_e/graph_index/
  nodes_skill.jsonl
  nodes_family.jsonl
  nodes_mechanism.jsonl
  nodes_signal.jsonl
  nodes_prototype_problem.jsonl
  nodes_prototype_solution.jsonl
  edges.jsonl
  skill_master_dense.npy
  skill_master_meta.json
  signal_view_dense.npy
  signal_view_meta.json
  prototype_problem_dense.npy
  prototype_problem_meta.json
  prototype_solution_dense.npy
  prototype_solution_meta.json
  sparse_corpus_skill_master.json
  sparse_corpus_signal_view.json
  sparse_corpus_prototype_problem.json
  sparse_corpus_prototype_solution.json
  facet_index.json
  graph_meta.json
```


## 8. 在线检索流程设计

### 8.1 Query Schema

在线检索第一步不是直接 embedding 原题面，而是先得到 Query Schema。

建议 Query Schema 如下：

```json
{
  "raw_problem_text": "...",
  "candidate_families": ["dynamic_programming", "greedy_algorithms"],
  "input_shapes": ["array"],
  "operation_tags": ["range_query", "point_update"],
  "goal_tags": ["count", "minimize"],
  "constraint_tags": ["n_le_2e5", "q_large"],
  "signal_tags": ["many_range_queries", "point_update"],
  "mechanism_hints": ["fenwick_tree", "segment_tree", "prefix_sum"],
  "keywords": ["query", "update", "range", "sum"],
  "is_multi_skill_likely": true
}
```

### 8.2 Query Schema 生成策略

推荐顺序：

1. 规则抽取
2. 复用 Stage B 的 family candidate logic
3. 可选的轻量 LLM rewrite

默认要求：

- 无 LLM 也能工作
- Query Schema 主要靠确定性规则生成


## 9. 检索算法设计

### 9.1 阶段一：Facet 预过滤

先根据 Query Schema 进行硬过滤或软过滤：

- family 过滤
- input shape 过滤
- complexity 档位过滤
- 明显冲突的 mechanism 过滤

目的：

- 缩小候选图
- 降低传播噪声

### 9.2 阶段二：多视图 Seed Retrieval

对以下视图分别做 dense + sparse 检索：

1. `SkillMaster`
2. `SignalView`
3. `PrototypeProblem`
4. `PrototypeSolution`

分别得到各自 top-k seed：

- `seed_skill`
- `seed_signal`
- `seed_proto_problem`
- `seed_proto_solution`

每类 seed 保留分数与来源。

### 9.3 阶段三：Typed Constrained Propagation

在候选异构子图上做带类型约束的传播，而不是简单 PPR。

建议分数更新公式：

```text
score_{t+1}(v) =
  alpha * seed(v)
  + (1 - alpha) * sum_r lambda_r * sum_{u -> v in r} w(u,v) * score_t(u)
  - delta * conflict_penalty(v)
```

其中：

- `seed(v)`：多视图 seed 聚合分数
- `lambda_r`：不同边类型权重
- `conflict_penalty(v)`：来自负边和 facet 冲突的惩罚

建议边权重优先级：

1. `prototype_solution_supports_skill`
2. `skill_implements_mechanism`
3. `skill_triggered_by_signal`
4. `prototype_problem_supports_skill`
5. `skill_cooccurs_skill`
6. `bundle_contains_skill`

不建议像 GoS 那样把“反向 prerequisite 扩散”作为主轴，而应把：

- signal -> mechanism -> skill
- prototype -> skill

作为主要传播路径。

### 9.4 阶段四：Skill Bundle Assembly

不是简单返回 top-k skill，而是组装一个小型技能子图。

目标：

- 1 个主 skill
- 0~2 个辅助 skill
- 可选 1 个 bundle skill

建议打分函数：

```text
BundleScore(B) =
  a * PrimaryRelevance(B)
  + b * MechanismCoverage(B)
  + c * FamilyAgreement(B)
  + d * ComplexityAgreement(B)
  + e * PrototypeSupport(B)
  + f * MultiSkillSynergy(B)
  - g * Redundancy(B)
  - h * Conflict(B)
  - j * PromptCost(B)
```

建议约束：

- 主 skill 必须是单 skill 或 multi skill 中得分最高者
- 辅助 skill 不能与主 skill 高冲突
- 同类重复 skill 需要惩罚

### 9.5 阶段五：Hydration

最终注入生成模型的不是整个节点图，而是压缩后的证据包。

每个 skill 的 hydration 内容建议包含：

1. `skill_name / skill_id`
2. `families`
3. `why_selected`
4. `matched_signals`
5. `matched_mechanisms`
6. `core_idea`
7. `template_strategy`
8. `pitfalls`
9. `prototype_evidence`

示例：

```text
### Skill: Range Queries (single__range_queries)
- Why selected: query contains many_range_queries + point_update; complexity suggests O((n+q)logn)
- Matched mechanisms: fenwick_tree, segment_tree
- Matched signals: many_range_queries, point_update, q_large
- Core idea: maintain dynamic aggregates under updates
- Template strategy:
  1. choose Fenwick if operation is additive and associative
  2. use segment tree if range operator is richer
  3. preprocess queries and updates
- Pitfalls:
  * prefix sum is insufficient under updates
  * O(nq) scan will time out
- Prototype evidence:
  * taco_train_xxx: many online range sum queries with updates
```


## 10. 为什么这套方案比论文 GoS 更适合本项目

### 10.1 GoS 的强项

GoS 非常适合：

- 工具调用
- 本地脚本技能库
- prerequisite helper recovery
- 需要把 parser / converter / setup utility 找齐的场景

### 10.2 本项目的关键差异

本项目更关注：

- 算法机制
- 复杂度档位
- 输入结构
- 多技能组合
- 易混淆技能的区分

### 10.3 本方案优于 GoS 的点

1. **异构图更贴合算法检索**
   - GoS 主要是 skill graph
   - 本方案是 signal / mechanism / skill / prototype 异构图

2. **显式支持 multi-skill**
   - 现有 `Stage D` 已经有 multi skill
   - 本方案将其作为一等公民

3. **有负边**
   - GoS 主要是正向补全
   - 本方案加入冲突边，减少错召回

4. **原型证据更强**
   - skill card 文本不够时，prototype problem / solution 是最有价值的检索视图

5. **目标从“依赖完整”变成“机制完整”**
   - 更符合算法技能场景


## 11. 与现有项目的具体对接方式

### 11.1 复用现有模块

建议直接复用：

- `Stage B` 的 problem-level family 结果
- `Stage C` 的 solution-level AST / mechanism 证据
- `Stage D` 的 skill card

### 11.2 保持兼容的原则

要求：

- 不破坏当前 flat index 流程
- Graph RAG 与现有检索器并存
- 通过配置切换检索模式

### 11.3 建议新增/改造的模块

建议 Cursor 新增以下文件：

```text
rag_experiment/src/rag/graph_schema.py
rag_experiment/src/rag/graph_build.py
rag_experiment/src/rag/graph_nodes.py
rag_experiment/src/rag/graph_edges.py
rag_experiment/src/rag/query_analyzer.py
rag_experiment/src/rag/graph_seed.py
rag_experiment/src/rag/graph_propagation.py
rag_experiment/src/rag/graph_bundle.py
rag_experiment/src/rag/graph_hydrate.py
rag_experiment/src/rag/graph_retrieve.py
rag_experiment/src/rag/facet_extract.py
rag_experiment/src/rag/prototype_index.py
```

建议改造以下文件：

```text
rag_experiment/src/rag/build_index.py
rag_experiment/src/rag/retrieve.py
rag_experiment/src/rag/pipeline.py
rag_experiment/scripts/run_stage_e_build_index.py
rag_experiment/config.yaml
```

### 11.4 配置项建议

建议新增：

```yaml
rag:
  retrieval:
    mode: graph            # flat | graph
    seed_top_k: 20
    candidate_top_k: 50
    final_top_k: 3
    dense_model: BAAI/bge-base-en-v1.5
    graph_alpha: 0.30
    graph_steps: 3
    edge_weights:
      skill_implements_mechanism: 1.0
      skill_triggered_by_signal: 0.9
      prototype_problem_supports_skill: 0.8
      prototype_solution_supports_skill: 1.2
      skill_cooccurs_skill: 0.5
      bundle_contains_skill: 0.6
    conflict_penalty: 0.7
    max_bundle_size: 3
    max_prototype_per_skill: 1
  graph_index:
    dir: outputs/stage_e/graph_index
    rebuild: false
```


## 12. 检索结果输出协议

Graph RAG 的返回对象建议扩展为：

```json
{
  "skill_ids": ["single__range_queries", "single__data_structures"],
  "skills": [...],
  "scores": [0.91, 0.74],
  "method": "graph",
  "bundle_type": "primary_plus_aux",
  "graph_evidence": [
    {
      "skill_id": "single__range_queries",
      "matched_signals": ["many_range_queries", "point_update"],
      "matched_mechanisms": ["fenwick_tree", "segment_tree"],
      "supporting_prototypes": ["proto_prob__...", "proto_sol__..."]
    }
  ],
  "seed_ids": {
    "skill": [],
    "signal": [],
    "prototype_problem": [],
    "prototype_solution": []
  }
}
```

要求：

- 保留当前 `RetrievalResult` 的兼容字段
- 新增 graph-specific evidence 字段


## 13. 评估方案

### 13.1 检索评估

在现有 `Stage F` 基础上新增：

1. `family_hit@k`
2. `skill_hit@k`
3. `multi_skill_hit@k`
4. `prototype_supported_hit@k`
5. `bundle_completeness`
6. `wrong_family_rate`

### 13.2 生成评估

沿用现有：

- PASS@1
- PASS@3
- retrieval hit rate

新增：

- `single-skill subset pass@3`
- `multi-skill subset pass@3`
- `graph evidence used rate`
- `top1 skill correctness`

### 13.3 基线对比

至少对比：

1. 当前 flat hybrid retriever
2. dense only
3. BM25 only
4. GoS-style skill-only graph
5. 本方案的异构 Skill Graph RAG


## 14. Cursor 实施计划

### Phase 1：图数据层

目标：

- 先把 graph index 建出来

任务：

1. 定义节点和边 schema
2. 从 Stage B/C/D 生成标准化 graph artifacts
3. 构建多视图 dense/sparse index

产出：

- `outputs/stage_e/graph_index/*`

### Phase 2：Query 分析与 seed 检索

目标：

- 从题面生成 Query Schema
- 支持多视图 seed retrieval

任务：

1. 实现 `query_analyzer.py`
2. 实现 family / signal / constraint 抽取
3. 实现多视图检索器

### Phase 3：图传播与 bundle 组装

目标：

- 从 seed 到 bundle

任务：

1. 实现 typed propagation
2. 实现 conflict penalty
3. 实现 bundle assembly
4. 实现 hydration

### Phase 4：与现有流水线集成

目标：

- Graph RAG 可通过配置切换

任务：

1. 改造 `build_index.py`
2. 改造 `retrieve.py`
3. 改造 `pipeline.py`
4. 更新 `config.yaml`

### Phase 5：评估与消融

任务：

1. 对比 flat vs graph
2. 对比是否加入 prototype
3. 对比是否加入负边
4. 对比是否启用 multi-skill bundle node


## 15. 最小可交付版本（MVP）

如果需要先做一版可运行 MVP，建议范围如下：

1. 节点只保留：
   - `SkillNode`
   - `MechanismNode`
   - `SignalNode`
   - `PrototypeProblemNode`

2. 边只保留：
   - `skill_has_family`
   - `skill_implements_mechanism`
   - `skill_triggered_by_signal`
   - `prototype_problem_supports_skill`
   - `skill_cooccurs_skill`

3. 查询只做：
   - family 抽取
   - constraint 抽取
   - operation / input shape 抽取

4. 在线只做：
   - multi-view seed retrieval
   - 3 步 typed propagation
   - top-1 primary skill + top-1 auxiliary skill

MVP 的目标不是一次做到最强，而是先验证：

- Graph RAG 是否优于当前 flat retriever
- prototype 视图是否显著提升 retrieval hit


## 16. 验收标准

Cursor 完成后，至少满足以下标准：

1. 能在不破坏现有 flat retriever 的前提下构建 `graph_index`
2. 能通过配置开关启用 Graph RAG
3. 在线返回结果包含 graph evidence
4. 在 `Stage F` 上可完成 A/B 对比
5. 至少能输出：
   - top-k skill
   - seed 来源
   - 传播后的图证据路径
   - bundle 组成原因

建议性能目标：

- Graph RAG 的 `retrieval_hit_rate` 高于当前 flat hybrid
- multi-skill 子集上的 PASS@3 明显提升
- prompt 预算不高于当前 flat hybrid 太多


## 17. 最终结论

对于本项目，不应继续把 skill 当成“单段文本文档”来检索，而应把它当成：

- 一个带结构化 facet 的技能实体
- 一个由机制、信号、原型支撑的图节点
- 一个可与其他技能组成 bundle 的算法单元

因此，最推荐的方向不是直接复刻论文 GoS，而是实现一套：

**Signal -> Mechanism -> Skill -> Prototype**

的异构 Skill Graph RAG。

这套方案相对于 GoS 的优势不在于更通用，而在于更贴合本项目的算法技能检索本质：  
**它优化的是“机制完整性”和“技能组合正确性”，而不仅仅是依赖补全。**
