from __future__ import annotations

import json

from src.pipeline import SkillRouterPipeline
from src.reranker import SkillReranker
from src.retriever import HybridRetriever

from conftest import FakeEncoder, FakeLLM, gate_payload


def test_routed_plan_smoke_executes_generated_solution(settings, bank) -> None:
    encoder = FakeEncoder()
    HybridRetriever.build_index(settings, bank, encoder=encoder)
    retriever = HybridRetriever.from_index(settings, encoder=encoder)
    chosen = "single.prefix_sum_1d.v1"
    responses = [
        json.dumps(
            {
                "problem_id": "p1",
                "statement_summary": "answer a range sum using prefix totals",
                "input_structures": ["array"],
                "constraint_profile": {"n": "large"},
                "objective_types": ["count"],
                "algorithm_signals": ["prefix sum", "range query"],
                "prohibited_operations": [],
                "likely_multi_skill": False,
            }
        ),
        gate_payload(chosen),
        json.dumps(
            {
                "problem_id": "p1",
                "selected_skills": [{"skill_id": chosen, "role": "main", "confidence": 0.9}],
                "problem_decomposition": ["read two integers", "output their sum"],
                "complexity": {"time": "O(1)", "constraint_fit": True},
            }
        ),
        "```python\na, b = map(int, input().split())\nprint(a + b)\n```",
    ]
    llm = FakeLLM(responses)

    def scorer(query: str, passages: list[str]) -> list[float]:
        return [1.0 if chosen in passage else 0.2 for passage in passages]

    pipeline = SkillRouterPipeline(settings, llm, bank, retriever, SkillReranker(settings, score_fn=scorer))
    trace = pipeline.run_problem(
        {
            "problem_id": "p1",
            "scope": "single",
            "problem_statement": "Given two values, output their range sum.",
            "input_output": {"inputs": ["2 3\n"], "outputs": ["5\n"]},
        },
        mode="routed_plan",
        n_samples=1,
    )
    assert trace.selected_skill_ids == [chosen]
    assert trace.samples[0].final_execution().all_passed is True
    code_prompt = llm.calls[-1][1]
    assert "single.graph_dijkstra_shortest_path.v1" not in code_prompt
