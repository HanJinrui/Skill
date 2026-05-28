"""Evaluation aggregation for run traces and manually reviewed route labels."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from .schemas import AnnotationRow, RunTrace


def _set_f1(predicted: set[str], gold: set[str]) -> float:
    if not predicted and not gold:
        return 1.0
    if not predicted or not gold:
        return 0.0
    overlap = len(predicted & gold)
    precision = overlap / len(predicted)
    recall = overlap / len(gold)
    return 2.0 * precision * recall / (precision + recall) if precision + recall else 0.0


def aggregate(traces: list[RunTrace], annotations: list[AnnotationRow] | None = None) -> dict[str, Any]:
    by_mode: dict[str, list[RunTrace]] = defaultdict(list)
    for trace in traces:
        by_mode[trace.mode].append(trace)
    gold = {row.problem_id: row for row in (annotations or []) if row.review_status == "reviewed" and not row.out_of_bank}
    output: dict[str, Any] = {}
    for mode, rows in sorted(by_mode.items()):
        sample0 = [row.samples[0].final_execution().all_passed for row in rows if row.samples]
        ac3 = [
            any(sample.final_execution().all_passed for sample in row.samples[:3])
            for row in rows
            if row.samples
        ]
        plans = [row for row in rows if mode.startswith("routed_plan")]
        extra_attempts = [
            sum(max(0, len(sample.attempts) - 1) for sample in row.samples)
            for row in rows
        ]
        route_single: list[bool] = []
        route_multi: list[float] = []
        for row in rows:
            annotation = gold.get(row.problem_id)
            if annotation is None:
                continue
            predicted = set(row.selected_skill_ids)
            expected = set(annotation.gold_skill_ids)
            if annotation.scope == "single":
                route_single.append(bool(predicted & expected))
            elif annotation.scope == "multi":
                route_multi.append(_set_f1(predicted, expected))
        output[mode] = {
            "problems": len(rows),
            "sample_pass_at_1": sum(sample0) / len(sample0) if sample0 else 0.0,
            "ac_at_3": sum(ac3) / len(ac3) if ac3 else 0.0,
            "plan_json_valid_rate": len([row for row in plans if row.plan is not None]) / len(plans) if plans else None,
            "mean_extra_iterations": sum(extra_attempts) / len(extra_attempts) if extra_attempts else 0.0,
            "single_top1_accuracy": sum(route_single) / len(route_single) if route_single else None,
            "multi_skill_set_f1": sum(route_multi) / len(route_multi) if route_multi else None,
            "fallback_count": sum(1 for row in rows if row.fallback_reason),
            "mean_latency_ms": {
                key: sum(row.latency_ms.get(key, 0) for row in rows) / len(rows)
                for key in sorted({key for row in rows for key in row.latency_ms})
            }
            if rows
            else {},
        }
    return output
