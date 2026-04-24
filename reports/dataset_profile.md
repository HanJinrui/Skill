# Dataset Profile — Stage A
## Source
- HuggingFace dataset: `BAAI/TACO`, split `train` (pristine).
- No dependency on the parent project's `datasets/` tree.

## Parsed TACO fields
| field | handling |
| --- | --- |
| `question` | kept verbatim as `problem_statement` |
| `solutions` | JSON / python-literal decoded → `reference_solutions[].code`, first 5 kept |
| `input_output` | JSON decoded → `{inputs[], outputs[], fn_name?}` (for evaluation) |
| `skill_types` + `tags` | normalized and mapped to the 8 core families via `taxonomy` |
| `difficulty`, `source` | passed through for stratified reporting |

## Selection rule
- For every core family, take the **first 30** records (in TACO dataset order) that:
  - have at least one reference solution;
  - have a well-formed `input_output`;
  - map to that core family through `skill_types ∪ tags`.
- Those per-family baseline slices are deduplicated into one universe.
- If deduplication leaves the universe below **240** unique problems, Stage A keeps scanning later family candidates in round-robin order and backfills with unseen problems until the unique target is reached or candidates are exhausted.
- `selected_problems_single.jsonl` and `selected_problems_multi.jsonl` cover the same problem universe.
- The difference is only the view: the single file keeps one `primary_family` per problem, while the multi file also records multi-skill metadata.

## Counts
- Scanned records: **25443**
- Records with tests: **10252**
- Records with ≥1 solution: **8633**
- Records touching any core family: **10542**
- Unique problems selected: **240 / 240**
- Unique-universe shortfall: **0**
- Single-label rows: **105**
- Multi-label rows: **135**

### Per-family availability & selection

| family | available in TACO | selected after backfill (baseline target = 30) | shortfall |
| --- | ---: | ---: | ---: |
| amortized_analysis | 554 | 36 | 0 |
| bit_manipulation | 816 | 36 | 0 |
| complete_search | 1886 | 36 | 0 |
| data_structures | 4695 | 36 | 0 |
| dynamic_programming | 2585 | 36 | 0 |
| greedy_algorithms | 2649 | 36 | 0 |
| range_queries | 233 | 35 | 0 |
| sorting | 2234 | 35 | 0 |

## Output files
- `/home/hjr/algo-skill-factory/rag_experiment/outputs/stage_a/selected_problems_single.jsonl` — primary-family view (one row per unique selected problem)
- `/home/hjr/algo-skill-factory/rag_experiment/outputs/stage_a/selected_problems_multi.jsonl` — multi-skill metadata view (same universe, records all matching families)
- `/home/hjr/algo-skill-factory/rag_experiment/outputs/stage_a/taco_tests.jsonl` — sidecar test-cases for Stage F evaluation
