# Experiment Report — Qwen2.5-Coder-7B + Skill RAG
- Scope: `multi`, eval source: `manifest:taco_test_primary80_core10.jsonl`, RAG enabled: `True`
- Total problems: 80, total runs: 240

## Core metrics
- **PASS@1** = 0.0667
- **PASS@3** = 0.1125
- Single-skill PASS@3 = 0.0845 (6/71)
- Multi-skill PASS@3 = 0.3333 (3/9)

## Retrieval statistics
- Total retrieval calls: 240
- Total hits: 114
- Overall correct-retrieval rate: 0.4750
- Avg retrieval calls per problem: 3.00
- Avg correct retrievals per problem: 1.43

## Per-family breakdown

| family | problems | PASS@3 | PASS@1 | retrieval hit rate |
| --- | ---: | ---: | ---: | ---: |
| amortized_analysis | 10 | 0.3000 | 0.1667 | 0.9000 |
| bit_manipulation | 10 | 0.0000 | 0.0000 | 0.9000 |
| complete_search | 10 | 0.1000 | 0.0333 | 0.9000 |
| data_structures | 10 | 0.0000 | 0.0000 | 0.2000 |
| dynamic_programming | 10 | 0.1000 | 0.1000 | 0.1000 |
| greedy_algorithms | 10 | 0.1000 | 0.0333 | 0.2000 |
| range_queries | 10 | 0.2000 | 0.1000 | 0.1000 |
| sorting | 10 | 0.1000 | 0.1000 | 0.5000 |
