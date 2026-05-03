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


def family_ids_for_problem(problem: dict[str, Any], label: dict[str, Any] | None = None) -> list[str]:
    label = label or {}
    fams = [s for s in (label.get("normalized_multi_skills") or []) if s in CORE_FAMILY_SET]
    if not fams:
        fams = [s for s in (problem.get("candidate_families") or []) if s in CORE_FAMILY_SET]
    if not fams and label.get("normalized_single_skill") in CORE_FAMILY_SET:
        fams = [label["normalized_single_skill"]]
    return list(dict.fromkeys(fams))


def family_skill_ids(families: list[str]) -> list[str]:
    ids: list[str] = []
    for fam in families:
        for sid in (fam, skill_id_for_single(fam), f"family__{fam}"):
            if sid not in ids:
                ids.append(sid)
    return ids


def subtype_gold_ids(primary_rows_by_problem: dict[str, dict[str, Any]], problem_id: str) -> list[str]:
    row = primary_rows_by_problem.get(problem_id) or {}
    subtype = row.get("primary_subtype")
    family = row.get("detected_single_skill") or row.get("family")
    if isinstance(subtype, str) and subtype and isinstance(family, str) and family:
        return [f"subtype__{family}__{subtype}"]
    return []


def bundle_gold_ids(families: list[str]) -> list[str]:
    fams = sorted(set(f for f in families if f in CORE_FAMILY_SET))
    if len(fams) < 2:
        return []
    return [skill_id_for_multi(fams), "bundle__" + "__".join(fams)]
