"""Hybrid skill retriever (BM25 + dense bge, fused via RRF).

Usage:
    retriever = SkillRetriever.from_settings(settings)
    result = retriever.retrieve(problem_statement, top_k=3)
    # -> RetrievalResult(skill_ids=[...], skills=[...], scores=[...],
    #                    dense_ids=[...], bm25_ids=[...])

The graph retriever (see `graph_retrieve.py`) returns the same
`RetrievalResult` shape with the graph-specific fields populated.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

from ..io_utils import load_json, load_jsonl
from ..logging_utils import get_logger
from ..settings import Settings
from .build_index import _tokenize  # reuse tokenizer

LOG = get_logger(__name__)


@dataclass(frozen=True)
class RetrievalResult:
    """Unified retrieval result for both the flat and the graph retriever.

    Flat-mode consumers only need `skill_ids / skills / scores / dense_ids /
    bm25_ids / method`; the graph-specific fields default to empty so they
    are safe to ignore.
    """
    skill_ids: list[str]
    skills: list[dict[str, Any]]
    scores: list[float]
    dense_ids: list[str]
    bm25_ids: list[str]
    method: str
    # Graph-specific, all optional so flat callers don't need to set them.
    bundle_type: str = ""
    graph_evidence: list[dict[str, Any]] = field(default_factory=list)
    seed_ids: dict[str, list[str]] = field(default_factory=dict)
    supporting_prototypes: list[str] = field(default_factory=list)
    matched_signals: list[str] = field(default_factory=list)
    matched_mechanisms: list[str] = field(default_factory=list)
    query_schema: dict[str, Any] = field(default_factory=dict)


class SkillRetriever:
    def __init__(
        self,
        *,
        index_dir: Path,
        dense_model: str,
        device: str,
        bm25_k1: float,
        bm25_b: float,
        fusion: str,
        rrf_k: int,
    ) -> None:
        self.index_dir = index_dir
        self.fusion = fusion
        self.rrf_k = rrf_k

        meta = load_json(index_dir / "index_meta.json")
        self.skill_ids: list[str] = list(meta["skill_ids"])
        self.dense_dim: int = int(meta["dense_dim"])
        self.dense_model_name: str = meta["dense_model"]

        self.skills: list[dict[str, Any]] = load_jsonl(index_dir / "skills.jsonl")
        self.skill_by_id: dict[str, dict[str, Any]] = {s["skill_id"]: s for s in self.skills}

        # BM25
        bm25_payload = load_json(index_dir / "bm25_corpus.json")
        try:
            from rank_bm25 import BM25Okapi
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Install rank_bm25 (pip install rank_bm25).") from exc
        self._bm25 = BM25Okapi(bm25_payload["tokens"], k1=bm25_k1, b=bm25_b)
        self._bm25_skill_ids = list(bm25_payload["skill_ids"])

        # Dense
        self._dense = np.load(index_dir / "dense_embeddings.npy")
        if self._dense.dtype != np.float32:
            self._dense = self._dense.astype(np.float32)
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Install sentence-transformers.") from exc
        self._encoder = SentenceTransformer(dense_model, device=device)

    @classmethod
    def from_settings(cls, settings: Settings) -> "SkillRetriever":
        raw = settings.config["rag"]["index"]["index_dir"]
        p = Path(raw)
        if not p.is_absolute():
            p = settings.project_root / raw
        rag_cfg = settings.config["rag"]["retrieval"]
        return cls(
            index_dir=p,
            dense_model=settings.embed.model,
            device=settings.embed.device,
            bm25_k1=float(rag_cfg["bm25_k1"]),
            bm25_b=float(rag_cfg["bm25_b"]),
            fusion=str(rag_cfg["fusion"]),
            rrf_k=int(rag_cfg["rrf_k"]),
        )

    def _dense_topk(self, query: str, top_k: int) -> list[tuple[str, float]]:
        vec = self._encoder.encode([query], normalize_embeddings=True, convert_to_numpy=True)[0].astype(np.float32)
        sims = self._dense @ vec  # cosine since both normalized
        k = min(top_k, sims.shape[0])
        idx = np.argpartition(-sims, k - 1)[:k]
        idx = idx[np.argsort(-sims[idx])]
        return [(self.skill_ids[i], float(sims[i])) for i in idx]

    def _bm25_topk(self, query: str, top_k: int) -> list[tuple[str, float]]:
        tokens = _tokenize(query)
        scores = self._bm25.get_scores(tokens)
        k = min(top_k, len(scores))
        if k == 0:
            return []
        idx = np.argpartition(-scores, k - 1)[:k]
        idx = idx[np.argsort(-scores[idx])]
        return [(self._bm25_skill_ids[i], float(scores[i])) for i in idx]

    def retrieve(self, query: str, *, top_k: int) -> RetrievalResult:
        pool_k = max(top_k * 3, 10)
        dense = self._dense_topk(query, pool_k)
        bm25 = self._bm25_topk(query, pool_k)

        fusion = self.fusion
        if fusion == "dense_only":
            merged = dense[:top_k]
            method = "dense_only"
        elif fusion == "bm25_only":
            merged = bm25[:top_k]
            method = "bm25_only"
        else:
            merged = self._rrf(dense, bm25, top_k=top_k)
            method = "rrf"

        ids = [sid for sid, _ in merged]
        scores = [sc for _, sc in merged]
        skills = [self.skill_by_id[sid] for sid in ids if sid in self.skill_by_id]
        return RetrievalResult(
            skill_ids=ids,
            skills=skills,
            scores=scores,
            dense_ids=[sid for sid, _ in dense[:top_k]],
            bm25_ids=[sid for sid, _ in bm25[:top_k]],
            method=method,
        )

    def _rrf(
        self,
        dense: list[tuple[str, float]],
        bm25: list[tuple[str, float]],
        *,
        top_k: int,
    ) -> list[tuple[str, float]]:
        """Reciprocal Rank Fusion."""
        rrf: dict[str, float] = {}
        for rank, (sid, _) in enumerate(dense):
            rrf[sid] = rrf.get(sid, 0.0) + 1.0 / (self.rrf_k + rank + 1)
        for rank, (sid, _) in enumerate(bm25):
            rrf[sid] = rrf.get(sid, 0.0) + 1.0 / (self.rrf_k + rank + 1)
        ordered = sorted(rrf.items(), key=lambda kv: kv[1], reverse=True)
        return ordered[:top_k]
