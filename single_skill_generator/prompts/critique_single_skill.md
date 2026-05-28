You are an expert reviewer of algorithm skills for LLM code generation.

Review the single-algorithm skill below and decide whether it is ready to ship.

Check:

1. Is it overfitted to specific problems (too problem-specific)?
2. Does it leak the original problem statement or solution code?
3. Does it match the declared primary_subtype?
4. Does it mix in a different algorithm family or subtype?
5. Are trigger_signals useful for retrieval?
6. Are applicability_conditions clear and actionable?
7. Are non_applicability_conditions sufficient to prevent misuse?
8. Is code_template generic enough to reuse?
9. Are common_pitfalls specific and helpful?
10. Is it suitable as a reusable skill during code generation?
11. Is code_template valid parseable Python, and is template_type honest about `pass` or `...` placeholders?
12. Does related_subtypes contain only normalized subtype identifiers rather than explanatory prose?

Input skill:

{{skill_json}}

Return strict JSON only (no markdown fences):

{
  "decision": "pass | revise | reject",
  "problems": [],
  "revision_suggestions": [],
  "abstraction_score": 0.0,
  "consistency_score": 0.0,
  "retrieval_score": 0.0,
  "template_score": 0.0,
  "leakage_score": 0.0,
  "final_score": 0.0
}

Scoring guidance: each score is 0.0–1.0. final_score should reflect overall readiness.
Use decision "pass" only if the skill is clearly reusable and subtype-consistent.
