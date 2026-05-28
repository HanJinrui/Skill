You are a competitive-programming expert and a code-generation systems designer.

You are given several {{evidence_description}}.
All samples passed their declared validation checks and share the same primary_subtype.

Your task is to distill one reusable single-algorithm skill that an LLM can invoke during code generation.

Requirements:

1. Do not restate any specific problem.
2. Do not copy solution_code from the samples.
3. Do not put problem-specific variable names, I/O formats, or story context into the skill.
4. Abstract the common algorithm mechanism only.
5. State clear applicability and non-applicability conditions.
6. Provide a generic executable Python code template.
7. List concrete common implementation pitfalls.
8. Name similar subtypes and subtypes that are easy to confuse with this one.
9. Output must be strict JSON only (no markdown fences, no prose outside JSON).
10. Do not invent algorithm mechanisms that are not supported by the input samples.
11. Prefer a complete `executable_python` code_template. If an application-specific placeholder
    such as `pass` or `...` is unavoidable, set template_type to `pseudocode_python`.
12. related_subtypes values must contain normalized subtype identifiers only, without prose notes.

Input:

Algorithm family:
{{algorithm_family}}

Primary subtype:
{{primary_subtype}}

Skill status:
{{status}}

Mechanism boundary:
{{mechanism_boundary}}

Representative samples:
{{representative_samples}}

Produce JSON in exactly this shape:

{
  "skill_id": "single.{{primary_subtype}}.v1",
  "skill_name": "",
  "skill_type": "single_algorithm",
  "version": "v1",
  "status": "{{status}}",
  "algorithm_family": "{{algorithm_family}}",
  "primary_subtype": "{{primary_subtype}}",
  "source_dataset": "{{source_dataset}}",
  "generation_method": "{{generation_method}}",
  "trigger_signals": [],
  "applicability_conditions": [],
  "non_applicability_conditions": [],
  "core_mechanism": "",
  "algorithm_steps": [],
  "state_or_structure_design": "",
  "transition_or_decision_rule": "",
  "complexity_pattern": {
    "time": "",
    "space": "",
    "notes": ""
  },
  "code_template": "",
  "template_type": "executable_python | pseudocode_python",
  "implementation_notes": [],
  "common_pitfalls": [],
  "retrieval_keywords": [],
  "related_subtypes": {
    "similar": [],
    "prerequisite": [],
    "often_combined_with": [],
    "should_not_confuse_with": []
  },
  "representative_examples": [
    {
      "problem_id": "",
      "solution_id": "",
      "why_representative": ""
    }
  ],
  "evidence": {
    "num_source_rows": 0,
    "num_representative_rows": 0,
    "evidence_tiers": {},
    "avg_subtype_confidence": 0.0,
    "source_problem_ids": []
  },
  "quality_control": {
    "schema_valid": false,
    "abstraction_check": "",
    "leakage_check": "",
    "consistency_check": "",
    "final_decision": ""
  }
}
