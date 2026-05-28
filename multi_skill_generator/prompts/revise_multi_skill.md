You are an expert editor of multi-algorithm composition skills for LLM code generation.

You are given a draft multi-algorithm skill and reviewer feedback. Revise the skill accordingly.

Requirements:

1. Keep the JSON schema unchanged.
2. Keep composition_signature unchanged.
3. Keep algorithm_flow algorithm order unchanged.
4. Remove problem-specific wording.
5. Remove problem-specific variable names.
6. Strengthen why_multiple_algorithms_are_needed.
7. Strengthen role, input, output, and handoff_to_next in algorithm_flow.
8. Strengthen state_interface (input_state, intermediate_state, output_state, handoff_description).
9. Strengthen composition_invariants for combination correctness.
10. Improve implementation_template generality.
11. Do not invent mechanisms unsupported by the samples.
12. Do not collapse the skill into a single-algorithm skill.
13. Write all skill text fields in English.
14. Output strict JSON only (no markdown fences).
15. Set `quality_control` to `{}`; only the program validator writes publication decisions.
16. Set `representative_examples` to `[]`; canonical evidence records are attached programmatically.

Draft skill:

{{skill_json}}

Reviewer feedback:

{{critique_json}}

Return the revised skill JSON.
