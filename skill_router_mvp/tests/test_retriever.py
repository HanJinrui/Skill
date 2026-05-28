from __future__ import annotations

from src.reranker import SkillReranker
from src.retriever import HybridRetriever

from conftest import FakeEncoder


def test_hybrid_index_and_rerank_retrieve_binary_search_answer(settings, bank) -> None:
    encoder = FakeEncoder()
    HybridRetriever.build_index(settings, bank, encoder=encoder)
    retriever = HybridRetriever.from_index(settings, encoder=encoder)
    candidates = retriever.retrieve("minimize maximum value using binary search monotonic feasible check")
    assert len(candidates) <= 12
    assert any(candidate.skill_id == "single.binary_search_on_answer.v1" for candidate in candidates)

    def scorer(query: str, passages: list[str]) -> list[float]:
        return [0.99 if "single.binary_search_on_answer.v1" in passage else 0.10 for passage in passages]

    reranked = SkillReranker(settings, score_fn=scorer).rerank("query", candidates)
    assert reranked[0].skill_id == "single.binary_search_on_answer.v1"
    assert reranked[0].rerank_score == 0.99
