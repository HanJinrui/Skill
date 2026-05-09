# Stage F 对比报告

- Manifest: `/home/hjr/algo-skill-factory/rag_experiment/outputs/eval_manifests/taco_test_family_difficulty_balanced_multi72.jsonl`
- Retrieval only: `False`
- Run tag: `graph_subtype_hybrid_v3_l72`
- Limit: `72` problems
- RAG config extra: `config_graph_subtype_hybrid_v3.yaml`
- Baseline config: `<base config>`
- Modes: `no_rag, graph_subtype_rag`

## Overall

| mode | problems | runs | PASS@1 | r0 pass | PASS@3 | retrieval hit | router@1 | family@k | subtype@k | bundle@k | false mechanism |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| no_rag | 51 | 153 | 0.0327 | 0.0392 | 0.0392 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| graph_subtype_rag | 51 | 153 | 0.0392 | 0.0392 | 0.0588 | 0.9595 | 0.9595 | 0.9595 | 0.0000 | 0.0000 | 0.0000 |

## By Difficulty

### easy

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 18 | 0.0556 | 0.0556 | 0.0000 |
| graph_subtype_rag | 18 | 0.0741 | 0.1111 | 0.9231 |

### medium

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 15 | 0.0000 | 0.0000 | 0.0000 |
| graph_subtype_rag | 15 | 0.0000 | 0.0000 | 1.0000 |

### hard

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 18 | 0.0370 | 0.0556 | 0.0000 |
| graph_subtype_rag | 18 | 0.0370 | 0.0556 | 0.9565 |

### unknown

| mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | ---: | ---: | ---: | ---: |
| no_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| graph_subtype_rag | 0 | 0.0000 | 0.0000 | 0.0000 |

## By Scope

| scope | mode | problems | PASS@1 | PASS@3 | retrieval hit |
| --- | --- | ---: | ---: | ---: | ---: |
| single | no_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| single | graph_subtype_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| multi | no_rag | 51 | 0.0327 | 0.0392 | 0.0000 |
| multi | graph_subtype_rag | 51 | 0.0392 | 0.0588 | 0.9595 |
| unknown | no_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
| unknown | graph_subtype_rag | 0 | 0.0000 | 0.0000 | 0.0000 |
