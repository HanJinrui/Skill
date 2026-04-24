# `algo-skill-factory / rag_experiment` 项目阶段汇报

## 1. 项目背景与当前目标

本项目的总体目标，是围绕算法题构建一套“可复用的算法 skill 体系”，并验证这些 skill 能否帮助代码大模型在新题上更稳定地生成正确解法。

当前仓库实际上包含两条相关但定位不同的技术路线：

1. `algo-skill-factory` 主线  
   目标是从带标签的数据集中生成层级化技能体系，包括 `subtype skill -> family skill -> router skill`，更强调“技能包”的结构化生成与路由。

2. `rag_experiment` 实验线  
   目标是从 TACO 数据集中筛题、重标注、合成 skill card、建立检索索引，并在代码生成模型上验证 Skill RAG 是否能提升解题通过率。

本次汇报重点聚焦 `rag_experiment`，并结合 80 题测试集的现有结果，对当前方法的有效性与不足进行分析。

## 2. 项目整体实现方法

### 2.1 主项目 `algo-skill-factory` 的实现思路

主项目采取“层级 skill 生成”的思路：

1. 从题目数据集中读取带标签的问题样本。
2. 按 `family / subtype` 聚类样本。
3. 针对每个 subtype 生成可复用的 subtype skill。
4. 将同一家族下的多个 subtype skill 汇总，生成 family skill。
5. 将所有 family skill 再汇总，生成最顶层 router skill。
6. 最终输出技能目录和清单文件，供后续分类、路由和求解使用。

这条路线的核心特点是：  
它不直接把“算法家族”当成最终知识单元，而是进一步细化到 subtype 层面，因此更适合做可迁移、可组合的技能表达。

### 2.2 `rag_experiment` 的实现思路

`rag_experiment` 采用的是一条 A-F 的流水线：

1. Stage A：从原始 TACO 中选题并抽取测试数据。
2. Stage B：对题目进行问题级算法标签标注。
3. Stage C：对参考解进行解法级算法标签标注，并与 Stage B 做一致性判断。
4. Stage D：基于一致样本，合成 skill card。
5. Stage E：基于 skill card 建立检索索引。
6. Stage F：在评测题上做检索增强生成，并统计 PASS@1、PASS@3 和检索命中率。

这条路线的设计目标，是让模型在做代码生成前，先从 skill 库中检索到相关算法知识，再把这些知识注入到 prompt 中，从而提升最终的代码正确率。

## 3. `rag_experiment` 的完整流程

### 3.1 Stage A：题目筛选与数据准备

Stage A 直接从 Hugging Face 上的 `BAAI/TACO` 数据集读取原始记录，而不是使用主项目里已经整理好的 `datasets/` 目录。

这一阶段主要完成以下工作：

1. 解析 TACO 中的题面、solutions、input/output、`skill_types`、`tags`、难度、来源等字段。
2. 将 `skill_types + tags` 映射到 8 个核心算法家族：
   `amortized_analysis`、`bit_manipulation`、`complete_search`、`data_structures`、`dynamic_programming`、`greedy_algorithms`、`range_queries`、`sorting`。
3. 按家族选出训练候选题，并写出后续阶段需要的自包含 JSONL。
4. 额外抽取测试题集，供 Stage F 最终评测使用。

当前实验中，最终构造出的评测集 `taco_test_primary80_core10` 的统计如下：

| 指标 | 数值 |
| --- | ---: |
| 总题数 | 80 |
| 核心家族数 | 8 |
| 每个核心家族题数 | 10 |
| 单技能题 | 71 |
| 多技能题 | 9 |

这意味着当前 80 题测试集是一个“按 primary family 均衡采样”的测试集，便于观察不同算法家族下的效果差异。

### 3.2 Stage B：问题级标签标注

Stage B 的目标，是对题面做问题级算法分类。

当前实现采用“规则 + LLM 融合”的方式：

1. 规则层先根据题面文本、`original_skill_types` 和 `original_tags` 给出候选 family。
2. GLM 根据题目描述输出结构化标签，包括单技能、多技能、摘要和理由。
3. 系统再将规则结果与 LLM 输出融合，得到最终的问题级标签。

当前 Stage B 一共输出了 240 条题目标注结果，对应 240 个训练题。  
从结果看，Stage B 的最终 `normalized_single_skill` 与 Stage A 原始 `primary_family` 的一致率约为 `180 / 240 = 75%`。

这说明 Stage B 并不是只做轻微纠偏，而是在相当多样本上重写了原始题目标签。  
这既可能修正部分噪声，也可能引入新的标签漂移。

### 3.3 Stage C：解法级标签标注与一致性筛选

Stage C 的目标，是判断“每个参考解真正使用了什么算法”，并与 Stage B 的问题级标签进行一致性比较。

当前实现流程如下：

1. 对每个 solution 提取 AST 特征。
2. 将 AST 特征映射成初步的家族提示。
3. 调用 GLM 生成该解法的算法标签和机制摘要。
4. 将 LLM 输出与 AST 结果融合。
5. 将 solution-level 标签与 problem-level 标签比较，分为：
   `consistent`、`partial`、`inconsistent`、`unknown`。

当前 Stage C 的数据规模如下：

| 指标 | 数值 |
| --- | ---: |
| 已标注 solution 对数 | 1095 |
| `consistent` | 579 |
| `partial` | 215 |
| `inconsistent` | 301 |
| 进入 `solution_consistent.jsonl` 的样本数 | 794 |

这表明：

1. 多解数据确实为后续 skill 抽取提供了更多样本。
2. 但 problem-level 与 solution-level 的一致性并不高。
3. 因此后续 skill 构建实际上建立在一个“带有明显标签噪声和偏移”的样本池之上。

### 3.4 Stage D：skill card 构建

Stage D 是当前实验最关键的知识构建阶段。

当前实现方式是：

1. 对单技能样本，按核心 family 聚合。
2. 对多技能样本，按 family 组合聚合。
3. 从每组中抽取若干一致样本，交给 GLM 生成一张可迁移的 skill card。

当前 Stage D 的产物规模如下：

| 文件 | 数量 |
| --- | ---: |
| `skills_single.jsonl` | 8 |
| `skills_multi.jsonl` | 2 |
| `skills_merged.jsonl` | 10 |

但进入 `solution_consistent.jsonl` 的后续候选样本中，实际观察到的不同 skill 组合有 53 种。  
也就是说，当前实验把较丰富的解法分布，压缩成了只有 10 张 skill card 的知识库。

这些 skill card 的命名也说明其粒度并不稳定：

| `skill_id` | `skill_name` |
| --- | --- |
| `amortized_analysis` | Sliding Window with Amortized Analysis |
| `sorting` | Level-wise Sorting in Complete Binary Trees |
| `bit_manipulation` | XOR-based array transformation and validation |
| `complete_search` | Binary Search on Answer with Greedy Validation |
| `data_structures` | Linked List Traversal and String Conversion |
| `dynamic_programming` | State Transition DP with Constraints |
| `range_queries` | Prefix Sum and Difference Array Techniques |

可以看到，部分 skill 已经不像“算法家族技能”，而更像某一类具体题型摘要。  
这会导致两个问题：

1. skill 太粗，难以支撑精细检索。
2. skill 又不够通用，容易过拟合到代表样本，而不是形成稳定的可迁移算法骨架。

### 3.5 Stage E：RAG 索引构建

Stage E 会把 Stage D 的 skill card 构造成可检索索引。

当前实现支持两种模式：

1. 平面检索  
   将每张 skill card 展平成检索文本，再构建 BM25 和 dense embedding 索引。

2. 图式检索  
   进一步抽取机制、信号、原型题、原型解等节点与边，构建图式 RAG 索引。

目前实验中使用的是 skill 检索增强生成，即先根据题面检索到 skill，再将 skill 作为上下文注入生成 prompt。

### 3.6 Stage F：代码生成与评测

Stage F 是最终验证环节，流程如下：

1. 对每道评测题先做 skill retrieval。
2. 调用 `Qwen2.5-Coder-7B-Instruct` 生成 3 个候选程序。
3. 使用 TACO 官方测试用例逐个执行。
4. 统计 PASS@1、PASS@3，以及检索是否命中正确 skill。

因此，最终结果并不仅仅反映模型生成能力，也反映前面 skill 构建和检索质量。

## 4. 80 题测试集实验结果

### 4.1 整体结果

本次对比实验包含两组：

1. `RAG enabled = True`
2. `RAG enabled = False`

其结果如下：

| 指标 | 有 RAG | 无 RAG | 差值 |
| --- | ---: | ---: | ---: |
| PASS@1 | 0.0667 | 0.0625 | +0.0042 |
| PASS@3 | 0.1125 | 0.0875 | +0.0250 |
| 单技能 PASS@3 | 0.0845 | 0.0704 | +0.0141 |
| 多技能 PASS@3 | 0.3333 | 0.2222 | +0.1111 |
| 检索命中率 | 0.4750 | 0.0000 | +0.4750 |

从结果可以看出：

1. RAG 确实带来了一定提升。
2. 但提升幅度非常有限。
3. 在 80 道题上，PASS@3 只从 7 题提升到 9 题，净增 2 题。

因此，目前这套 Skill RAG 方案尚不能说明“已经显著提升了算法题求解能力”，更准确的结论应是：  
**RAG 在部分题型上有增益，但整体收益仍然较弱，且存在明显负迁移。**

### 4.2 各算法家族结果

| family | 题数 | RAG PASS@3 | no-RAG PASS@3 | 差值 | RAG 检索命中率 |
| --- | ---: | ---: | ---: | ---: | ---: |
| amortized_analysis | 10 | 0.3000 | 0.2000 | +0.1000 | 0.9000 |
| bit_manipulation | 10 | 0.0000 | 0.0000 | 0.0000 | 0.9000 |
| complete_search | 10 | 0.1000 | 0.0000 | +0.1000 | 0.9000 |
| data_structures | 10 | 0.0000 | 0.0000 | 0.0000 | 0.2000 |
| dynamic_programming | 10 | 0.1000 | 0.1000 | 0.0000 | 0.1000 |
| greedy_algorithms | 10 | 0.1000 | 0.0000 | +0.1000 | 0.2000 |
| range_queries | 10 | 0.2000 | 0.3000 | -0.1000 | 0.1000 |
| sorting | 10 | 0.1000 | 0.1000 | 0.0000 | 0.5000 |

可以观察到：

1. `amortized_analysis`、`complete_search`、`greedy_algorithms` 有一定提升。
2. `bit_manipulation` 和 `data_structures` 即使检索命中率不低，也没有转化为通过率提升。
3. `range_queries` 在加入 RAG 后反而下降，说明存在负迁移。
4. `dynamic_programming` 和 `range_queries` 的检索命中率都只有 0.1，表明这些家族的检索效果很差。

### 4.3 运行层面的失败分布

如果把 240 次生成运行对应的所有测试样例执行结果汇总，各类结果统计如下：

| 结果原因 | 有 RAG | 无 RAG |
| --- | ---: | ---: |
| `ok` | 988 | 1190 |
| `wrong_answer` | 2599 | 2454 |
| `runtime_error` | 849 | 816 |
| `timeout` | 154 | 130 |
| `skipped_fn_name` | 9 | 9 |

这组数据说明：

1. 当前 RAG 并没有显著减少错误答案。
2. 相反，`wrong_answer`、`runtime_error` 和 `timeout` 都比 no-RAG 更高。
3. 这意味着注入的 skill 信息有时并没有帮助模型稳定收敛，反而可能把生成过程带偏。

### 4.4 检索命中与最终通过之间的差距

RAG 组总检索命中率为 `0.475`，但最终 PASS@3 只有 `0.1125`。  
这说明“检索到了相关 skill”并不等于“模型因此写出了正确代码”。

进一步看：

| family | 检索命中且通过的运行数 | 检索命中但失败的运行数 |
| --- | ---: | ---: |
| amortized_analysis | 5 | 22 |
| bit_manipulation | 0 | 27 |
| complete_search | 1 | 26 |
| data_structures | 0 | 6 |
| dynamic_programming | 0 | 3 |
| greedy_algorithms | 0 | 6 |
| range_queries | 0 | 3 |
| sorting | 3 | 12 |

这说明：

1. 很多时候系统检索到了“看上去相关”的 skill，但对最终生成没有形成有效约束。
2. 尤其是 `bit_manipulation`、`complete_search` 这类 family，命中很多，但大多数情况下仍然失败。
3. 当前问题不只是“检索不到”，更是“检索到的 skill 不够可执行”。

## 5. 当前实验结果不理想的原因分析

结合现有流程和结果，我认为当前实验效果一般，主要有以下几个原因。

### 5.1 Stage D 的 skill 粒度过粗

这是当前最核心的问题。

现在的 skill 构建方式，本质上是一家族一张卡，再加极少数 multi-skill 组合卡。  
这种设计有两个明显局限：

1. family 级别过粗，无法区分真正决定解法结构的 subtype。
2. skill card 内容又容易被代表样本带偏，变成某个题型摘要，而不是稳定的算法骨架。

因此，当前 skill 既不够细，也不够稳。

### 5.2 Stage B 的问题级重标注可能引入标签漂移

当前 TACO 已经提供了 `skill_types` 和 `tags`。  
但 Stage B 又使用规则 + LLM 对题面重新标注，这会让后续 Stage C 的一致性判断建立在“重写后的 problem label”上。

从当前统计看，Stage B 与原始 `primary_family` 的一致率只有 75%。  
这说明 Stage B 的介入强度较大，它既可能修复噪声，也可能把问题带偏。

### 5.3 问题级标签与解法级标签被混在一起使用

当前实验里，“题面适合哪类算法”和“具体代码真正用了什么算法”这两个层次没有完全拆开。

但实际上这两件事不一样：

1. 题面语义更适合做 router。
2. 具体解法机制更适合做 implementation skill。

如果这两层信息混用，就容易造成检索阶段召回的是“题目像什么”，而不是“代码该怎么写”。

### 5.4 检索命中不等于生成可用

当前检索评估采用的是“是否命中 gold skill id”。  
但 gold hit 只能说明 family 方向相近，不能说明注入的信息真的足够指导代码生成。

目前结果表明，很多命中的 skill card 对模型来说仍然太泛，无法有效转化为：

1. 状态定义
2. 转移关系
3. 关键不变量
4. 数据结构维护方式

因此，检索成功并没有稳定转化为代码成功。

## 6. 当前阶段结论

基于现有实验，可以得出以下阶段性结论：

1. `rag_experiment` 已经完成了从数据筛选、标签构建、skill 合成、索引构建到代码评测的完整闭环。
2. 当前 Skill RAG 相比 no-RAG 有小幅提升，但提升有限，在 80 题测试集上仅多通过 2 题。
3. 问题的主要瓶颈不在 Stage F 单独的生成模型，而在前面的 skill 表达与检索链路。
4. 当前 skill card 仍以 family 级粗粒度表示为主，难以支撑复杂算法题的精细迁移。
5. 现有结果说明这条方向有研究价值，但仍需要对“数据构造方式、标签层次、skill 粒度和检索逻辑”做较大改进。

## 7. 下一步优化方向

结合当前结果，下一阶段建议重点推进以下工作：

1. 将 skill 构建改为层级化结构  
   参考主项目 `algo-skill-factory` 的思路，构建 `router skill -> family skill -> subtype skill`，而不是只保留 family 卡片。

2. 将题目级标签与解法级标签彻底拆开  
   使用题面的 `skill_types/tags` 和语义线索做 router；  
   使用 full-pass 的具体解法做 implementation skill 抽取。

3. 针对多解数据建立“主解筛选机制”  
   先做 correctness filter，再在所有 full-pass 解中挑选 `primary_solution`，用于构造高质量 skill 原型。

4. 将 LLM 从“全量重标注器”降级为“验证与纠偏器”  
   不再让 LLM 直接改写全部问题级标签，而是只负责：
   题目标签冲突消解、solution-level algorithm tag 验证、主解优选辅助判断。

5. 提升 skill 的可执行性  
   skill 不应只描述“适用场景”和“核心思想”，还需要更明确地表达：
   `trigger_signals`、`non_triggers`、`failure_modes`、`pattern_abstraction`、`transfer_strategy`。

## 8. 汇报时可直接使用的一句话总结

本阶段工作已经打通了算法题 Skill RAG 的完整实验闭环，并在 80 道 TACO 测试题上验证了该方向具有一定增益；但当前提升幅度仍然较小，说明瓶颈主要不在生成模型本身，而在于 skill 的构建粒度、标签体系和检索知识表达方式，下一阶段将重点转向“基于正确解和层级 subtype 的高质量 skill 构建”。
