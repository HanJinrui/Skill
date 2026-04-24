# Experiment Report — Qwen2.5-Coder-7B + Skill RAG
- Scope: `multi`, eval source: `manifest:taco_test_multi_balanced12.jsonl`, RAG enabled: `False`
- Total problems: 12, total runs: 36

## Core metrics
- **PASS@1** = 0.0278
- **PASS@3** = 0.0833
- Single-skill PASS@3 = 0.0000 (0/0)
- Multi-skill PASS@3 = 0.0833 (1/12)

## Retrieval statistics
- Total retrieval calls: 0
- Total hits: 0
- Overall correct-retrieval rate: 0.0000
- Avg retrieval calls per problem: 0.00
- Avg correct retrievals per problem: 0.00

## Per-family breakdown

| family | problems | PASS@3 | PASS@1 | retrieval hit rate |
| --- | ---: | ---: | ---: | ---: |
| amortized_analysis | 3 | 0.0000 | 0.0000 | 0.0000 |
| bit_manipulation | 1 | 1.0000 | 0.3333 | 0.0000 |
| complete_search | 1 | 0.0000 | 0.0000 | 0.0000 |
| data_structures | 2 | 0.0000 | 0.0000 | 0.0000 |
| dynamic_programming | 4 | 0.0000 | 0.0000 | 0.0000 |
| sorting | 1 | 0.0000 | 0.0000 | 0.0000 |
