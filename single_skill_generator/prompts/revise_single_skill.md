You are an expert editor of algorithm skills for LLM code generation.

You are given a draft skill and a critique. Revise the skill according to the critique.

Requirements:

1. Keep the JSON schema unchanged (same keys and structure).
2. Remove problem-specific wording.
3. Remove problem-specific variable names and I/O details.
4. Strengthen applicability and non-applicability conditions.
5. Improve the generality of code_template, ensure it parses as valid Python, and mark
   templates containing `pass` or `...` as `pseudocode_python`.
6. Do not add algorithm mechanisms not supported by the original evidence.
7. Output strict JSON only (no markdown fences, no prose outside JSON).
8. Keep related_subtypes entries as normalized subtype identifiers without prose annotations.

Draft skill:

{{skill_json}}

Critique:

{{critique_json}}

Return the revised skill as a single JSON object.
