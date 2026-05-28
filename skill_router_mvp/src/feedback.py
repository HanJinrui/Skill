"""Deterministic repair/reroute policy for the closed-loop mode."""
from __future__ import annotations

from .config import Settings
from .schemas import ExecutionReport, FeedbackDecision, GateDecision


class FeedbackController:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def decide(self, report: ExecutionReport, gate: GateDecision | None, *, attempts: int) -> FeedbackDecision:
        if report.all_passed:
            return FeedbackDecision(action="accept", reason="all_tests_passed")
        if attempts >= 2:
            return FeedbackDecision(action="stop", reason="maximum_attempts_reached")
        reasons = set(report.reason_summary)
        if reasons & {"compile_error", "runtime_error", "unsafe_code"}:
            return FeedbackDecision(action="repair", reason="implementation_failure")
        if "timeout" in reasons:
            return FeedbackDecision(action="reroute", reason="timeout_suggests_complexity_mismatch")
        if "wrong_answer" in reasons:
            margin = gate.margin if gate is not None else 1.0
            if gate and gate.runner_up_skill_id and margin < float(self.settings.data["routing"]["reroute_margin"]):
                return FeedbackDecision(action="reroute", reason="wrong_answer_with_ambiguous_route")
            return FeedbackDecision(action="repair", reason="wrong_answer_with_confident_route")
        return FeedbackDecision(action="repair", reason="unclassified_execution_failure")


def better_report(new: ExecutionReport, previous: ExecutionReport) -> bool:
    if new.all_passed and not previous.all_passed:
        return True
    if new.num_passed != previous.num_passed:
        return new.num_passed > previous.num_passed
    previous_failures = sum(previous.reason_summary.get(key, 0) for key in ("compile_error", "runtime_error", "timeout"))
    new_failures = sum(new.reason_summary.get(key, 0) for key in ("compile_error", "runtime_error", "timeout"))
    return new_failures < previous_failures
