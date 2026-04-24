"""Retrieval-correctness helpers.

"Correct retrieval" = the top-k retrieval set contains the problem's gold
skill. Gold skills are derived from Stage B labels (`normalized_multi_skills`)
mapped onto the skill-id space:
  * for every single family we allow the `single` skill card of that family;
  * we also allow the exact multi skill-id (sorted join of families) if that
    card exists in the index.
"""
from __future__ import annotations

from typing import Any

from ..taxonomy import CORE_FAMILY_SET, skill_id_for_multi, skill_id_for_single


def gold_skill_ids_for_problem(problem_label: dict[str, Any]) -> list[str]:
    multi = [s for s in (problem_label.get("normalized_multi_skills") or []) if s in CORE_FAMILY_SET]
    if not multi:
        single = problem_label.get("normalized_single_skill")
        if isinstance(single, str) and single in CORE_FAMILY_SET:
            multi = [single]
    ids: list[str] = []
    for fam in multi:
        single_id = skill_id_for_single(fam)
        if single_id not in ids:
            ids.append(single_id)
    if len(multi) >= 2:
        combo = skill_id_for_multi(multi)
        if combo not in ids:
            ids.append(combo)
    return ids


def is_retrieval_hit(retrieved_ids: list[str], gold_ids: list[str]) -> bool:
    if not gold_ids:
        return False
    return any(sid in gold_ids for sid in retrieved_ids)
