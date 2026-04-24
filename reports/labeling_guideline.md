# Labeling Guideline

## Principles
- **Problem labels** come from reading the problem, constraints, and I/O shape.
  The LLM can use the original TACO tags as a hint but must never copy them blindly.
- **Solution labels** come from the code's actual mechanism — AST + regex fingerprint
  is the anchor, not the variable names or the surrounding problem statement.

## Rule ↔ LLM fusion
| signal from LLM | signal from rule | action |
| --- | --- | --- |
| in-set, agrees with rule candidates | any | accept LLM |
| in-set, disagrees, confidence ≥ 0.75 (problem) / 0.6 (solution) | any | accept LLM |
| in-set, disagrees, confidence low | rule suggests something | **override with top rule / AST hint** |
| out-of-set or missing | any | override with top rule / AST hint |

## Consistency classification (Stage C)
- `consistent`    — `detected_multi_skills` equals `problem_skills` as sets.
- `partial`       — intersection non-empty but sets differ. A multi-skill problem
                    whose solution implements only its primary family lands here.
- `inconsistent`  — empty intersection. The labels disagree entirely.
- `unknown`       — code could not be parsed or LLM refused.

Only `consistent` (and optionally `partial`) rows feed Stage D skill synthesis.
