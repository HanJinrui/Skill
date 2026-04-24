# Experiment Report — Qwen2.5-Coder-7B + Skill RAG
- Scope: `multi`, eval source: `manifest:taco_test_multi_balanced12.jsonl`, RAG enabled: `True`
- Total problems: 12, total runs: 36

## Core metrics
- **PASS@1** = 0.0833
- **PASS@3** = 0.1667
- Single-skill PASS@3 = 0.0000 (0/0)
- Multi-skill PASS@3 = 0.1667 (2/12)

## Retrieval statistics
- Total retrieval calls: 36
- Total hits: 30
- Overall correct-retrieval rate: 0.8333
- Avg retrieval calls per problem: 3.00
- Avg correct retrievals per problem: 2.50

## Per-family breakdown

| family | problems | PASS@3 | PASS@1 | retrieval hit rate |
| --- | ---: | ---: | ---: | ---: |
| amortized_analysis | 3 | 0.6667 | 0.3333 | 1.0000 |
| bit_manipulation | 1 | 0.0000 | 0.0000 | 1.0000 |
| complete_search | 1 | 0.0000 | 0.0000 | 1.0000 |
| data_structures | 2 | 0.0000 | 0.0000 | 0.0000 |
| dynamic_programming | 4 | 0.0000 | 0.0000 | 1.0000 |
| sorting | 1 | 0.0000 | 0.0000 | 1.0000 |
