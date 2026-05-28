"""Cross-encoder reranking for the small retrieved candidate pool."""
from __future__ import annotations

import math
from collections.abc import Callable
from typing import Any

from .config import Settings
from .schemas import RetrievalCandidate


ScoreFunction = Callable[[str, list[str]], list[float]]


class SkillReranker:
    def __init__(self, settings: Settings, *, score_fn: ScoreFunction | None = None) -> None:
        self.settings = settings
        self._score_fn = score_fn
        self._model: Any = None

    def _load_score_fn(self) -> ScoreFunction:
        if self._score_fn is not None:
            return self._score_fn
        try:
            from sentence_transformers import CrossEncoder
        except ImportError as exc:
            raise RuntimeError("Install sentence-transformers to run the reranker.") from exc
        self._model = CrossEncoder(
            str(self.settings.data["retrieval"]["reranker_model"]),
            device=str(self.settings.data["retrieval"].get("device", "cpu")),
        )

        def score(query: str, passages: list[str]) -> list[float]:
            logits = self._model.predict([(query, passage) for passage in passages])
            return [1.0 / (1.0 + math.exp(-float(item))) for item in logits]

        self._score_fn = score
        return score

    def rerank(self, query: str, candidates: list[RetrievalCandidate], *, top_k: int | None = None) -> list[RetrievalCandidate]:
        if not candidates:
            return []
        score_fn = self._load_score_fn()
        scores = score_fn(query, [candidate.card.retrieval_text for candidate in candidates])
        reranked: list[RetrievalCandidate] = []
        for candidate, score in zip(candidates, scores):
            reranked.append(
                candidate.model_copy(
                    update={
                        "rerank_score": float(score),
                        "final_score": 0.70 * float(score) + 0.30 * candidate.router_score,
                    }
                )
            )
        limit = int(top_k or self.settings.data["retrieval"]["rerank_limit"])
        return sorted(reranked, key=lambda item: item.final_score, reverse=True)[:limit]
