# Experiment Report — Qwen2.5-Coder-7B + Skill RAG
- Scope: `multi`, eval source: `manifest:taco_test_primary80_core10.jsonl`, RAG enabled: `False`
- Total problems: 80, total runs: 240

## Core metrics
- **PASS@1** = 0.0625
- **PASS@3** = 0.0875
- Single-skill PASS@3 = 0.0704 (5/71)
- Multi-skill PASS@3 = 0.2222 (2/9)

## Retrieval statistics
- Total retrieval calls: 0
- Total hits: 0
- Overall correct-retrieval rate: 0.0000
- Avg retrieval calls per problem: 0.00
- Avg correct retrievals per problem: 0.00

## Per-family breakdown

| family | problems | PASS@3 | PASS@1 | retrieval hit rate |
| --- | ---: | ---: | ---: | ---: |
| amortized_analysis | 10 | 0.2000 | 0.1000 | 0.0000 |
| bit_manipulation | 10 | 0.0000 | 0.0000 | 0.0000 |
| complete_search | 10 | 0.0000 | 0.0000 | 0.0000 |
| data_structures | 10 | 0.0000 | 0.0000 | 0.0000 |
| dynamic_programming | 10 | 0.1000 | 0.1000 | 0.0000 |
| greedy_algorithms | 10 | 0.0000 | 0.0000 | 0.0000 |
| range_queries | 10 | 0.3000 | 0.2000 | 0.0000 |
| sorting | 10 | 0.1000 | 0.1000 | 0.0000 |
