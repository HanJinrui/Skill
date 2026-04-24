# TACO Skill-Aware RAG Experiment

End-to-end reproducible pipeline that:

1. Selects the top-30 problems from each of the 8 core algorithm families in TACO (240 total), in both single-label and multi-label views.
2. Re-labels problems and reference solutions with a rule+LLM hybrid judge (GLM).
3. Synthesizes a transferable `algorithm_skill` knowledge base.
4. Builds a hybrid (BM25 + dense) RAG index over those skills.
5. Generates code with **Qwen2.5-Coder-7B-Instruct** after skill retrieval, and reports PASS@3 plus retrieval-hit statistics.

## Quickstart

```bash
cd rag_experiment
cp .env.example .env          # fill ZHIPU_API_KEY + adjust paths
pip install -r requirements.txt

# Stage A: select 240 problems + fetch TACO tests
python scripts/run_stage_a.py

# Stage B: problem-level skill labels (GLM)
python scripts/run_stage_b.py

# Stage C: solution-level skill labels & consistency
python scripts/run_stage_c.py

# Stage D: synthesize algorithm-skill knowledge base
python scripts/run_stage_d.py

# Stage E: build hybrid index
python scripts/run_stage_e_build_index.py

# Stage F: 3-sample Qwen generation + PASS@3 + retrieval stats
python scripts/run_stage_f_eval.py
```

Every stage supports `--resume` (default ON via the on-disk cache) and writes streaming JSONL outputs under `outputs/stage_x/`.

## Reports

- `reports/dataset_profile.md` — field layout, family distributions, selection rules.
- `reports/labeling_guideline.md` — how rule+LLM fuse, consistency rules.
- `reports/experiment_report.md` — final metrics and ablations.
