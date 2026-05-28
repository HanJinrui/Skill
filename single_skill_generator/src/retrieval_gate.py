from __future__ import annotations

import math
import re
from collections import Counter
from typing import Any


def tokenize(text: str) -> list[str]:
    normalized = str(text or "").replace("_", " ").lower()
    return re.findall(r"[a-z][a-z0-9]{1,}|[0-9]+", normalized)


def build_skill_document(skill: dict[str, Any]) -> str:
    fields: list[str] = [
        str(skill.get("canonical_subtype") or skill.get("primary_subtype") or ""),
        " ".join(str(value) for value in (skill.get("alias_subtypes") or [])),
        str(skill.get("algorithm_family") or ""),
        str(skill.get("skill_name") or ""),
        " ".join(str(value) for value in (skill.get("trigger_signals") or [])),
        " ".join(str(value) for value in (skill.get("applicability_conditions") or [])),
        " ".join(str(value) for value in (skill.get("retrieval_keywords") or [])),
        str(skill.get("core_mechanism") or ""),
    ]
    return " ".join(fields)


def rank_skills(query: str, skills: list[dict[str, Any]]) -> list[tuple[str, float]]:
    documents = [tokenize(build_skill_document(skill)) for skill in skills]
    query_terms = Counter(tokenize(query))
    doc_count = len(documents)
    avg_length = sum(len(tokens) for tokens in documents) / max(doc_count, 1)
    frequencies = Counter(term for tokens in documents for term in set(tokens))
    scored: list[tuple[str, float]] = []
    for skill, tokens in zip(skills, documents):
        tf = Counter(tokens)
        score = 0.0
        for term, qtf in query_terms.items():
            df = frequencies.get(term, 0)
            if not df or not tf.get(term):
                continue
            idf = math.log(1 + (doc_count - df + 0.5) / (df + 0.5))
            denom = tf[term] + 1.2 * (1 - 0.75 + 0.75 * len(tokens) / max(avg_length, 1))
            score += qtf * idf * (tf[term] * 2.2 / denom)
        scored.append((str(skill.get("canonical_subtype") or ""), round(score, 6)))
    scored.sort(key=lambda value: (-value[1], value[0]))
    return scored


def evaluate_retrieval_gate(
    skills: list[dict[str, Any]],
    held_out_queries: dict[str, list[dict[str, str]]],
    *,
    top_k: int = 3,
) -> dict[str, Any]:
    by_subtype: dict[str, Any] = {}
    for subtype in sorted(held_out_queries):
        results = []
        for query in held_out_queries[subtype]:
            ranked = rank_skills(query["problem_statement"], skills)
            retrieved = [skill_id for skill_id, _ in ranked[:top_k]]
            results.append(
                {
                    "problem_id": query["problem_id"],
                    "retrieved_subtypes": retrieved,
                    "hit": subtype in retrieved,
                }
            )
        by_subtype[subtype] = {
            "num_queries": len(results),
            "top_k": top_k,
            "all_hit": bool(results) and all(result["hit"] for result in results),
            "queries": results,
        }
    return {
        "method": "generator_local_bm25",
        "top_k": top_k,
        "num_skills": len(skills),
        "skills_tested": len(by_subtype),
        "results": by_subtype,
    }
