# Skill Router MVP

这是一个独立的 Qwen2.5-Coder-7B 算法路由与代码生成实验目录。它只读取仓库中已经发布的
54 张 single skill、13 张 multi skill 以及 TACO 评测 manifest，不 import 或修改
`rag_experiment`、`single_skill_generator`、`multi_skill_generator`、`skill_data_factory`
中的实现或产物。

## Pipeline

```text
Problem -> Qwen ProblemProfile -> BM25 + bge-m3 retrieval
        -> bge-reranker-v2-m3 -> Qwen Gate -> Qwen AlgorithmPlan
        -> Qwen Python code -> restricted execution -> repair/reroute
```

所有派生产物写入本目录的 `outputs/`：

- `outputs/index/bank67_v1/`：冻结元数据、统一卡片、组件边、BM25 与 dense 向量索引
- `outputs/annotations/`：人工审校路由金标工作表
- `outputs/runs/`：完整 `RunTrace` JSONL
- `outputs/reports/`：聚合指标

## Setup

```bash
cd skill_router_mvp
python -m pip install -r requirements.txt
```

本地 Qwen 模型可在 `config.yaml` 设置 `model.local_model_dir`，或通过
`SKILL_ROUTER_QWEN_LOCAL_MODEL_DIR` 指定；否则使用 Hugging Face 模型 ID。

本仓库当前已配置为读取本地解包目录：

```text
../.hf-cache/models/Qwen__Qwen2.5-Coder-7B-Instruct
```

该目录是 `../Qwen__Qwen2.5-Coder-7B-Instruct.tar.gz` 的可加载本地模型副本。
推理阶段不会下载 Qwen 权重，也不需要再次解压 12 GB 的归档文件。

先校验模型文件与 tokenizer：

```bash
python scripts/verify_local_qwen.py --tokenizer
```

如需验证 GPU 推理是否可用，可先选择当前空闲 GPU，再运行一个极小生成：

```bash
nvidia-smi
export CUDA_VISIBLE_DEVICES=3  # 示例：替换为运行时空闲显存最多的 GPU 编号
python scripts/verify_local_qwen.py --tokenizer --generate-smoke
```

## Build Index

默认建立 BM25 与 `BAAI/bge-m3` exact dense 索引：

```bash
python scripts/build_index.py
```

第一次运行会按需下载 `BAAI/bge-m3`；后续会复用本机 Hugging Face 缓存。索引
规模只有 67 张卡，因此默认在 CPU 建立与查询，避免占用 Qwen 所在 GPU。

仅用于快速验证文件/schema 的轻量模式：

```bash
python scripts/build_index.py --lexical-only
```

轻量索引写入 `outputs/index/bank67_v1_lexical_smoke/`，不能代表正式 hybrid
retrieval 评测；正式运行前必须重新执行默认命令。

## Manual Route Gold

在已建立正式索引后，生成包含候选 skill 的审校表：

```bash
nvidia-smi
export CUDA_VISIBLE_DEVICES=1  # 示例：选择运行时空闲的物理 GPU
python scripts/build_annotation_sheet.py --device cuda:0 --overwrite
```

`bge-reranker-v2-m3` 在 CPU 上逐题重排会很慢；`config.yaml` 的安全默认值仍为
CPU，但生成完整审校表时建议通过 `--device` 临时使用空闲 GPU。设置
`CUDA_VISIBLE_DEVICES=1` 后，该物理 GPU 在脚本中对应 `cuda:0`。脚本会逐题
打印进度并在每题完成后立即写入文件；如运行中断，可继续：

```bash
export CUDA_VISIBLE_DEVICES=1
python scripts/build_annotation_sheet.py --device cuda:0 --resume
```

只需快速产生无二阶段重排的初始候选表时，可运行：

```bash
python scripts/build_annotation_sheet.py --no-rerank --overwrite
```

人工填写每行的 `gold_skill_ids`、`out_of_bank`、`annotation_reason`，并将
`review_status` 改为 `reviewed`。未审校行不会参与路由准确率统计。

### DeepSeek Silver Labels

如果无法独立判断算法标签，可以使用 DeepSeek V4 Pro 产生独立的模型银标。
银标不是严格人工金标：它适合用于初步量化 router 是否与强模型判断一致，但正式
结论仍应披露标签来源。

脚本会向 DeepSeek 提供完整的 67 张 skill 精简目录与完整题面，不提供 router
候选顺序；因此它能够识别 retrieval 漏掉的 skill。默认每题执行“初始标注 +
二次审计”，且仅将置信度不低于 `0.75`、无需额外复核的结果标记为 `reviewed`。
为提高 JSON 稳定性与吞吐，结构化标注默认以 `thinking=disabled` 调用
`deepseek-v4-pro`：

```bash
export DEEPSEEK_API_KEYS='key-1,key-2,key-3'

# 默认一把 key 一个并发 worker；先调用少量题，检查 API、输出格式与费用
python scripts/annotate_with_deepseek.py --limit 5 --overwrite

# 确认后生成完整银标；三把 key 默认并发处理三道题
python scripts/annotate_with_deepseek.py --overwrite
```

输出位于：

```text
outputs/annotations/bank67_route_deepseek_silver.jsonl
```

如调用中断或少数请求失败，可续跑：

```bash
python scripts/annotate_with_deepseek.py --resume
```

也支持只配置 `DEEPSEEK_API_KEY` 的单 key 兼容模式，或用 `--workers 1` 临时降低
并发。每个 worker 在同一道题内按顺序完成初标和二次审计，输出按请求完成顺序
增量写入，顺序不会影响后续指标统计。需要尝试 DeepSeek 思考模式时，可加
`--thinking enabled --max-tokens 4096`，但会增加耗时和格式重试概率。

该文件保留 `label_source=deepseek_silver`、模型名、置信度、初始决定与不确定性
说明。`needs_review` 行不会进入路由准确率指标；如数量较多，建议增加另一轮模型
复核，而不是直接将阈值降到很低。`run_eval.py` 的 metrics 报告也会记录所使用
的标注文件和 `label_source`。
其中 `reviewed_out_of_bank_rows` 可用于观察当前 67 张 skill 对评测题目的覆盖缺口；
这些题目不会混入路由准确率计算。

## Evaluation

先运行最小生成 smoke，确认 Qwen、检索和执行器能串起来：

```bash
export CUDA_VISIBLE_DEVICES=3  # 先按 nvidia-smi 结果选择
python scripts/run_eval.py \
  --device cuda:0 \
  --scope single \
  --modes direct_qwen,routed_plan \
  --limit 2 \
  --samples 1 \
  --run-tag single_smoke
```

如果使用 DeepSeek 银标进行路由指标统计，先指定标注文件：

```bash
ANNOTATIONS=outputs/annotations/bank67_route_deepseek_silver.jsonl
```

如果后续获得人工金标，则将 `ANNOTATIONS` 改为
`outputs/annotations/bank67_route_gold_workbook.jsonl`。然后执行 single 与
multi 的正式四模式 A/B：

```bash
# 继续使用上面通过 CUDA_VISIBLE_DEVICES 选中的空闲 GPU
python scripts/run_eval.py \
  --device cuda:0 \
  --scope single \
  --modes direct_qwen,legacy_hint,routed_plan,routed_plan_closed_loop \
  --run-tag single_bank67 \
  --annotations "$ANNOTATIONS"

python scripts/run_eval.py \
  --device cuda:0 \
  --scope multi \
  --modes direct_qwen,legacy_hint,routed_plan,routed_plan_closed_loop \
  --run-tag multi_bank67 \
  --annotations "$ANNOTATIONS"
```

已有运行结果可离线重新汇总：

```bash
python scripts/summarize_results.py \
  outputs/runs/single_bank67.jsonl \
  outputs/runs/multi_bank67.jsonl \
  --annotations "$ANNOTATIONS"
```

## Metrics

汇总包含 `sample_pass_at_1`、`ac_at_3`、`plan_json_valid_rate`、
`mean_extra_iterations`、`single_top1_accuracy`、`multi_skill_set_f1`、
fallback 数与各阶段平均延迟。执行器会在临时目录运行生成代码，并限制危险导入、
危险调用、CPU 时间、内存和单测超时。

## Tests

测试不下载模型，也不调用 Qwen；它们使用确定性 fake encoder、reranker 和 LLM：

```bash
pytest -q
```
