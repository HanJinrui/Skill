You are a competitive-programming expert and a code-generation systems designer.

You are given several verified multi-algorithm solution annotations from an evidence ledger.
Evidence may come from TACO, CodeContests, or both.
All samples passed execution checks and share the same ordered composition pattern:

Composition signature:
{{composition_signature}}

Composition relation:
{{composition_relation}}

Status: {{status}}
Support count: {{support_count}}

Your task is to distill one reusable multi-algorithm composition skill that an LLM can invoke during code generation.

Requirements:

1. Produce a multi-algorithm composition skill, not a single-algorithm skill.
2. Do not restate any specific problem.
3. Do not copy solution_code from the samples.
4. Do not put problem-specific variable names, I/O formats, or story context into the skill.
5. Preserve the exact order in composition_signature.
6. Explain why multiple algorithms must work together (not just list them).
7. For each step in algorithm_flow, specify role, input, output, and handoff_to_next.
8. Explain how the output of one algorithm becomes the input of the next.
9. State composition_invariants that justify correctness of the combination (not single-algorithm trivia).
10. Provide a generic implementation_template in Python 3 style (pseudocode-style Python is fine); do not output a full problem solution.
11. List at least 3 concrete common_pitfalls.
12. Provide confusable_compositions (similar vs should_not_confuse_with).
13. Do not invent algorithm mechanisms unsupported by the input samples.
14. Output must be strict JSON only (no markdown fences, no prose outside JSON).
15. Write all skill text fields in English.
16. Set `quality_control` to `{}`. It is populated only by the program validator.
17. Set `representative_examples` to `[]`. The program attaches canonical evidence records.

Representative samples:
{{representative_samples}}

Produce JSON conforming to this schema (include every top-level field):

{{multi_skill_schema}}

Required skill_id format (use exactly):
{{expected_skill_id}}
