"""Metric aggregation for Stage F runs."""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable


def aggregate(run_rows: Iterable[dict[str, Any]], problem_labels: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Compute PASS@1, PASS@3, retrieval stats overall and by skill subset.

    `run_rows` is the JSONL emitted by Stage F — each row represents ONE of
    the 3 runs per problem.
    """
    rows = list(run_rows)
    by_problem: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_problem[row["problem_id"]].append(row)

    total_problems = len(by_problem)
    total_runs = len(rows)

    pass1_count = sum(1 for r in rows if r.get("passed"))
    pass3_problems = sum(1 for pid, runs in by_problem.items() if any(r.get("passed") for r in runs))

    retrieval_hits_total = sum(1 for r in rows if r.get("retrieval_hit"))
    retrieval_calls_total = sum(1 for r in rows if r.get("retrieved_skill_ids"))

    # per-problem
    per_problem_hits = []
    per_problem_retrieval_calls = []
    for pid, runs in by_problem.items():
        per_problem_retrieval_calls.append(sum(1 for r in runs if r.get("retrieved_skill_ids")))
        per_problem_hits.append(sum(1 for r in runs if r.get("retrieval_hit")))
    avg_retrievals_per_problem = _safe_mean(per_problem_retrieval_calls)
    avg_hits_per_problem = _safe_mean(per_problem_hits)
    correct_rate_overall = retrieval_hits_total / retrieval_calls_total if retrieval_calls_total else 0.0

    # single vs multi split based on problem labels
    single_ids: set[str] = set()
    multi_ids: set[str] = set()
    for pid, lbl in problem_labels.items():
        if lbl.get("is_multi_skill"):
            multi_ids.add(pid)
        else:
            single_ids.add(pid)

    def _split_pass3(pid_set: set[str]) -> tuple[int, int]:
        if not pid_set:
            return 0, 0
        rel = [pid for pid in by_problem if pid in pid_set]
        passed = sum(1 for pid in rel if any(r.get("passed") for r in by_problem[pid]))
        return passed, len(rel)

    single_pass3, single_total = _split_pass3(single_ids)
    multi_pass3, multi_total = _split_pass3(multi_ids)

    # Per-family grouping
    per_family: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "problems": 0, "passed_problems": 0, "runs": 0, "passed_runs": 0,
        "retrieval_hits": 0, "retrieval_calls": 0,
    })
    for pid, runs in by_problem.items():
        lbl = problem_labels.get(pid, {})
        fam = lbl.get("normalized_single_skill") or "unknown"
        bucket = per_family[fam]
        bucket["problems"] += 1
        bucket["passed_problems"] += int(any(r.get("passed") for r in runs))
        for r in runs:
            bucket["runs"] += 1
            if r.get("passed"):
                bucket["passed_runs"] += 1
            if r.get("retrieval_hit"):
                bucket["retrieval_hits"] += 1
            if r.get("retrieved_skill_ids"):
                bucket["retrieval_calls"] += 1

    per_family_out = {}
    for fam, stats in per_family.items():
        per_family_out[fam] = {
            **stats,
            "pass_at_3": stats["passed_problems"] / stats["problems"] if stats["problems"] else 0.0,
            "pass_at_1": stats["passed_runs"] / stats["runs"] if stats["runs"] else 0.0,
            "retrieval_hit_rate": stats["retrieval_hits"] / stats["retrieval_calls"] if stats["retrieval_calls"] else 0.0,
        }

    return {
        "total_problems": total_problems,
        "total_runs": total_runs,
        "pass_at_1": pass1_count / total_runs if total_runs else 0.0,
        "pass_at_3": pass3_problems / total_problems if total_problems else 0.0,
        "single_subset": {
            "problems": single_total,
            "passed": single_pass3,
            "pass_at_3": single_pass3 / single_total if single_total else 0.0,
        },
        "multi_subset": {
            "problems": multi_total,
            "passed": multi_pass3,
            "pass_at_3": multi_pass3 / multi_total if multi_total else 0.0,
        },
        "retrieval": {
            "avg_calls_per_problem": avg_retrievals_per_problem,
            "avg_correct_per_problem": avg_hits_per_problem,
            "overall_correct_rate": correct_rate_overall,
            "total_calls": retrieval_calls_total,
            "total_hits": retrieval_hits_total,
        },
        "per_family": per_family_out,
    }


def _safe_mean(values: list[int]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)
