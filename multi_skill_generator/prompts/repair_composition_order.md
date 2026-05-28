You are an expert annotator repairing multi-algorithm composition labels.

You are given one solution sample where composition_order may be missing or inconsistent.
Infer the correct ordered composition_order from composition_subtypes, core_composition_summary, and code structure.

Input sample:
{{row_json}}

Return strict JSON only (no markdown fences):

{
  "decision": "valid | repair | reject",
  "original_composition_order": [],
  "repaired_composition_order": [],
  "reason": "",
  "confidence": 0.0
}
