You are an expert reviewer of multi-algorithm composition skills for LLM code generation.

Review the multi-algorithm skill below and decide whether it is ready to ship.

Check:

1. Does it preserve the given composition_signature order?
2. Does algorithm_flow match composition_signature step-for-step?
3. Does each algorithm_flow step have clear role, input, output, and (where needed) handoff_to_next?
4. Does state_interface clearly describe data passed between algorithms?
5. Does why_multiple_algorithms_are_needed justify the combination (not just name two algorithms)?
6. Do composition_invariants explain combination correctness, not generic single-algorithm facts?
7. Does implementation_template reflect a multi-stage collaboration workflow?
8. Are non_applicability_conditions strong enough to prevent misuse?
9. Are common_pitfalls specific and actionable?
10. Is it merely two single-algorithm skills pasted together?
11. Does it leak problem statements, variable names, or code snippets from samples?
12. Does it over-generalize beyond what the samples support?

Input skill:

{{skill_json}}

Expected composition_signature:

{{composition_signature}}

Representative sample summaries:

{{representative_samples_summary}}

Return strict JSON only (no markdown fences):

{
  "decision": "pass | revise | reject",
  "problems": [],
  "revision_suggestions": [],
  "order_consistency_score": 0.0,
  "interface_clarity_score": 0.0,
  "composition_abstraction_score": 0.0,
  "invariant_quality_score": 0.0,
  "template_score": 0.0,
  "non_leakage_score": 0.0,
  "evidence_support_score": 0.0,
  "final_score": 0.0
}
