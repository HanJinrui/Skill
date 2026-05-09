# Stage F 对比报告

- Manifest: `/home/hjr/algo-skill-factory/rag_experiment/outputs/eval_manifests/taco_test_family_difficulty_balanced_single120.jsonl`
- Retrieval only: `False`
- Run tag: `graph_subtype_hybrid_v3_l72`
- Limit: `72` problems
- RAG config extra: `config_graph_subtype_hybrid_v3.yaml`
- Baseline config: `<base config>`
- Modes: `no_rag, graph_subtype_rag`

## Overall

| mode | problems | runs | PASS@1 | r0 pass | PASS@3 | retrieval hit | router@1 | family@k | subtype@k | bundle@k | false mechanism |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| no_rag | 72 | 216 | 0.0463 | 0.0694 | 0.0694 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| graph_subtype_rag | 72 | 216 | 0.0509 | 0.0694 | 0.0694 | 0.8816 | 0.8816 | 0.8816 | 0.0000 | 0.0000 | 0.0000 |

## By Difficulty

### easy

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 22 | 0.1061 | 0.1364 | 0.0000 |
| graph_subtype_rag | 22 | 0.1212 | 0.1364 | 0.9600 |

### medium

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 24 | 0.0139 | 0.0417 | 0.0000 |
| graph_subtype_rag | 24 | 0.0139 | 0.0417 | 1.0000 |

### hard

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 26 | 0.0256 | 0.0385 | 0.0000 |
| graph_subtype_rag | 26 | 0.0256 | 0.0385 | 0.6923 |

### unknown

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| graph_subtype_rag | 0 | 0.0000 | 0.0000 | 0.0000 |

## By Scope

| scope | mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | --- | ---: | ---: | ---: | ---: |
| single | no_rag | 72 | 0.0463 | 0.0694 | 0.0000 |
| single | graph_subtype_rag | 72 | 0.0509 | 0.0694 | 0.8816 |
| multi | no_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| multi | graph_subtype_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| unknown | no_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| unknown | graph_subtype_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
