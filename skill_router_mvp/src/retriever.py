"""Hybrid BM25 + exact dense + rule retrieval over the frozen skill bank."""
from __future__ import annotations

import math
from collections import Counter
from pathlib import Path
from typing import Any, Protocol

import numpy as np

from .config import Settings
from .io_utils import load_json, load_jsonl, write_json
from .retrieval_text import tokenize
from .schemas import ProblemProfile, RetrievalCandidate, UnifiedSkillCard
from .skill_bank import SkillBank


class Encoder(Protocol):
    def encode(self, texts: list[str], **kwargs: Any) -> Any: ...


class SentenceEncoder:
    def __init__(self, model_name: str, device: str) -> None:
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:
            raise RuntimeError("Install sentence-transformers to build or query dense index.") from exc
        self.model = SentenceTransformer(model_name, device=device)

    def encode(self, texts: list[str], **kwargs: Any) -> np.ndarray:
        return np.asarray(
            self.model.encode(texts, normalize_embeddings=True, convert_to_numpy=True, **kwargs),
            dtype=np.float32,
        )


class SimpleBM25:
    def __init__(self, documents: list[list[str]], *, k1: float, b: float) -> None:
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.avgdl = sum(len(doc) for doc in documents) / max(1, len(documents))
        self.term_counts = [Counter(doc) for doc in documents]
        df: Counter[str] = Counter()
        for doc in documents:
            df.update(set(doc))
        n = len(documents)
        self.idf = {term: math.log(1.0 + (n - count + 0.5) / (count + 0.5)) for term, count in df.items()}

    def scores(self, query: str) -> np.ndarray:
        terms = tokenize(query)
        values: list[float] = []
        for doc, counts in zip(self.documents, self.term_counts):
            score = 0.0
            length_norm = 1.0 - self.b + self.b * len(doc) / max(self.avgdl, 1.0)
            for term in terms:
                freq = counts.get(term, 0)
                if not freq:
                    continue
                score += self.idf.get(term, 0.0) * (freq * (self.k1 + 1)) / (freq + self.k1 * length_norm)
            values.append(score)
        return np.asarray(values, dtype=np.float32)


def _normalize_positive(values: np.ndarray) -> np.ndarray:
    if values.size == 0:
        return values
    peak = float(np.max(values))
    if peak <= 0:
        return np.zeros_like(values)
    return values / peak


def _status_score(card: UnifiedSkillCard, settings: Settings) -> float:
    priors = settings.data["retrieval"].get("status_prior") or {}
    return float(priors.get(card.status, 0.55))


def _rule_score(query: str, profile: ProblemProfile | None, card: UnifiedSkillCard) -> tuple[float, float, list[str], list[str]]:
    query_text = query.lower()
    if profile:
        query_text += " " + " ".join(profile.algorithm_signals + profile.prohibited_operations).lower()
    query_terms = set(tokenize(query_text))
    signal_texts = card.trigger_signals + card.applicability_conditions
    matches = [item for item in signal_texts if set(tokenize(item)) & query_terms]
    keyword_terms = set(tokenize(card.retrieval_text))
    overlap = len(query_terms & keyword_terms) / max(1, min(16, len(query_terms)))
    signal_ratio = min(1.0, len(matches) / 3.0)
    score = min(1.0, 0.55 * signal_ratio + 0.45 * overlap)
    blockers: list[str] = []
    joined = card.retrieval_text.lower()
    if ("contiguous" in query_text or "subarray" in query_text) and "sorting" in joined and "window" not in joined:
        blockers.append("contiguous_order_conflict")
    if "negative" in query_text and "positive" in joined and "window" in joined:
        blockers.append("negative_values_break_positive_window")
    if ("unweighted" in query_text or "unit weight" in query_text) and "dijkstra" in joined:
        blockers.append("unweighted_graph_prefers_bfs")
    penalty = 1.0 if blockers else 0.0
    return score, penalty, matches[:5], blockers


class HybridRetriever:
    def __init__(
        self,
        settings: Settings,
        cards: list[UnifiedSkillCard],
        corpus_tokens: list[list[str]],
        dense_embeddings: np.ndarray | None,
        encoder: Encoder | None,
    ) -> None:
        self.settings = settings
        self.cards = cards
        cfg = settings.data["retrieval"]
        self.bm25 = SimpleBM25(corpus_tokens, k1=float(cfg["bm25_k1"]), b=float(cfg["bm25_b"]))
        self.dense_embeddings = dense_embeddings
        self.encoder = encoder

    @classmethod
    def build_index(
        cls,
        settings: Settings,
        bank: SkillBank,
        *,
        encoder: Encoder | None = None,
        build_dense: bool = True,
    ) -> Path:
        index_dir = settings.path("index_dir", create=True)
        bank.write_frozen_artifacts(index_dir)
        texts = [card.retrieval_text for card in bank.cards]
        tokens = [tokenize(text) for text in texts]
        write_json(index_dir / "bm25_corpus.json", {"skill_ids": [card.skill_id for card in bank.cards], "tokens": tokens})
        dense: np.ndarray | None = None
        if build_dense:
            use_encoder = encoder or SentenceEncoder(
                str(settings.data["retrieval"]["dense_model"]),
                str(settings.data["retrieval"].get("device", "cpu")),
            )
            dense = np.asarray(use_encoder.encode(texts), dtype=np.float32)
            norms = np.linalg.norm(dense, axis=1, keepdims=True)
            dense = dense / np.maximum(norms, 1e-12)
            np.save(index_dir / "dense_embeddings.npy", dense)
        write_json(
            index_dir / "index_meta.json",
            {
                **bank.metadata,
                "dense_enabled": dense is not None,
                "dense_model": settings.data["retrieval"]["dense_model"],
                "dense_dim": int(dense.shape[1]) if dense is not None else 0,
            },
        )
        return index_dir

    @classmethod
    def from_index(cls, settings: Settings, *, encoder: Encoder | None = None) -> "HybridRetriever":
        index_dir = settings.path("index_dir")
        cards = [UnifiedSkillCard.model_validate(row) for row in load_jsonl(index_dir / "unified_skill_cards.jsonl")]
        corpus = load_json(index_dir / "bm25_corpus.json")
        meta = load_json(index_dir / "index_meta.json")
        dense: np.ndarray | None = None
        use_encoder = encoder
        if bool(meta.get("dense_enabled")):
            dense = np.load(index_dir / "dense_embeddings.npy").astype(np.float32)
            use_encoder = use_encoder or SentenceEncoder(
                str(settings.data["retrieval"]["dense_model"]),
                str(settings.data["retrieval"].get("device", "cpu")),
            )
        return cls(settings, cards, list(corpus["tokens"]), dense, use_encoder)

    def retrieve(self, query: str, *, profile: ProblemProfile | None = None, top_k: int | None = None) -> list[RetrievalCandidate]:
        cfg = self.settings.data["retrieval"]
        sparse = _normalize_positive(self.bm25.scores(query))
        dense = np.zeros(len(self.cards), dtype=np.float32)
        if self.dense_embeddings is not None and self.encoder is not None:
            qvec = np.asarray(self.encoder.encode([query]), dtype=np.float32)[0]
            qvec = qvec / max(float(np.linalg.norm(qvec)), 1e-12)
            dense = (self.dense_embeddings @ qvec + 1.0) / 2.0
        weights = cfg["weights"]
        candidates: list[RetrievalCandidate] = []
        for i, card in enumerate(self.cards):
            rule, blocked, signals, blockers = _rule_score(query, profile, card)
            status = _status_score(card, self.settings)
            penalty = float(weights["hard_non_applicable"]) * blocked
            router = (
                float(weights["sparse"]) * float(sparse[i])
                + float(weights["dense"]) * float(dense[i])
                + float(weights["rule"]) * rule
                + float(weights["status"]) * status
                - penalty
            )
            candidates.append(
                RetrievalCandidate(
                    skill_id=card.skill_id,
                    skill_type=card.skill_type,
                    sparse_score=float(sparse[i]),
                    dense_score=float(dense[i]),
                    rule_score=rule,
                    status_score=status,
                    penalty_score=penalty,
                    router_score=router,
                    final_score=router,
                    matched_signals=signals,
                    blockers=blockers,
                    card=card,
                )
            )
        singles = sorted((item for item in candidates if item.skill_type == "single_algorithm"), key=lambda x: x.router_score, reverse=True)
        multis = sorted((item for item in candidates if item.skill_type == "multi_algorithm"), key=lambda x: x.router_score, reverse=True)
        pool = singles[: int(cfg["single_pool_limit"])] + multis[: int(cfg["multi_pool_limit"])]
        limit = int(top_k or cfg["candidate_limit"])
        return sorted(pool, key=lambda x: x.router_score, reverse=True)[:limit]
