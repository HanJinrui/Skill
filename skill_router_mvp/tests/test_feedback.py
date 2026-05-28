from __future__ import annotations

from src.executor import PythonExecutor
from src.feedback import FeedbackController, better_report
from src.schemas import GateDecision


def test_executor_runs_stdio_and_blocks_unsafe_code(settings) -> None:
    executor = PythonExecutor(settings)
    tests = {"inputs": ["2 3\n"], "outputs": ["5\n"]}
    passed = executor.execute("a,b=map(int,input().split())\nprint(a+b)\n", tests)
    blocked = executor.execute("import os\nprint(5)\n", tests)
    assert passed.all_passed is True
    assert blocked.reason_summary == {"unsafe_code": 1}
    assert better_report(passed, blocked)


def test_feedback_reroutes_ambiguous_wrong_answer(settings) -> None:
    report = PythonExecutor(settings).execute("print(0)\n", {"inputs": ["\n"], "outputs": ["1\n"]})
    gate = GateDecision(
        assessments=[],
        selected_skill_ids=["a"],
        selection_type="single",
        runner_up_skill_id="b",
        margin=0.03,
    )
    decision = FeedbackController(settings).decide(report, gate, attempts=1)
    assert decision.action == "reroute"
