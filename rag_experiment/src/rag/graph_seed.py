"""Multi-view seed retrieval over the persisted graph index.

The graph retriever consults four views:

* `skill_master`       — dense + BM25 over the full skill text.
* `signal_view`        — dense + BM25 over signal-heavy short docs.
* `prototype_problem`  — dense over prototype problem statements.
* `prototype_solution` — dense over prototype solution summaries.

This module keeps no knowledge of the graph itself — it only turns a
`QuerySchema` + dense query vector into per-view ranked lists. Scores
are rank-normalised so downstream propagation can treat all four views
on the same footing.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

from ..io_utils import load_json
from .prototype_index import tokenize
from .query_analyzer import QuerySchema


@dataclass
class ViewIndex:
    view: str
    node_ids: List[str]
    dense: np.ndarray                  # (N, D) float32 or empty
    sparse_tokens: List[List[str]]
    bm25_backend: object | None        # rank_bm25.BM25Okapi or None if N == 0

    @property
    def size(self) -> int:
        return len(self.node_ids)


@dataclass
class SeedScores:
    """Aggregated seed scores per view.

    scores_by_view[view] : {node_id: score}
    """
    scores_by_view: Dict[str, Dict[str, float]] = field(default_factory=dict)
    topk_by_view: Dict[str, List[Tuple[str, float]]] = field(default_factory=dict)


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

def load_view_index(graph_dir: Path, view: str, *, bm25_k1: float = 1.5, bm25_b: float = 0.75) -> ViewIndex:
    meta = load_json(graph_dir / f"{view}_meta.json")
    node_ids: List[str] = list(meta.get("node_ids") or [])
    dense_path = graph_dir / f"{view}_dense.npy"
    if dense_path.exists():
        dense = np.load(dense_path)
        if dense.size == 0:
            dense = np.zeros((0, 0), dtype=np.float32)
        elif dense.dtype != np.float32:
            dense = dense.astype(np.float32)
    else:
        dense = np.zeros((0, 0), dtype=np.float32)

    sparse = load_json(graph_dir / f"sparse_corpus_{view}.json")
    tokens: List[List[str]] = list(sparse.get("tokens") or [])

    bm25_backend = None
    if tokens:
        try:
            from rank_bm25 import BM25Okapi
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Install rank_bm25 (pip install rank_bm25).") from exc
        bm25_backend = BM25Okapi(tokens, k1=bm25_k1, b=bm25_b)

    return ViewIndex(
        view=view,
        node_ids=node_ids,
        dense=dense,
        sparse_tokens=tokens,
        bm25_backend=bm25_backend,
    )


# --------------------------------------------------------------------------- #
# Seed scoring helpers
# --------------------------------------------------------------------------- #

def _normalize_rank_scores(pairs: Sequence[Tuple[str, float]], *, k: int = 20) -> Dict[str, float]:
    """Convert a ranked list of (node_id, raw_score) into a rank-normalised map."""
    out: Dict[str, float] = {}
    if not pairs:
        return out
    top = pairs[:k]
    max_rank = len(top)
    for rank, (nid, _) in enumerate(top):
        # Linear decay from 1.0 down to ~1/max_rank.
        out[nid] = max(out.get(nid, 0.0), 1.0 - rank / max(max_rank, 1))
    return out


def _dense_topk(index: ViewIndex, query_vec: np.ndarray, top_k: int) -> List[Tuple[str, float]]:
    if index.dense.size == 0 or query_vec.size == 0:
        return []
    sims = index.dense @ query_vec
    k = min(top_k, sims.shape[0])
    if k <= 0:
        return []
    idx = np.argpartition(-sims, k - 1)[:k]
    idx = idx[np.argsort(-sims[idx])]
    return [(index.node_ids[i], float(sims[i])) for i in idx]


def _bm25_topk(index: ViewIndex, tokens: Sequence[str], top_k: int) -> List[Tuple[str, float]]:
    if index.bm25_backend is None or not tokens:
        return []
    scores = index.bm25_backend.get_scores(list(tokens))
    k = min(top_k, len(scores))
    if k <= 0:
        return []
    idx = np.argpartition(-scores, k - 1)[:k]
    idx = idx[np.argsort(-scores[idx])]
    return [(index.node_ids[i], float(scores[i])) for i in idx]


def _fuse_dense_bm25(
    dense: Sequence[Tuple[str, float]],
    bm25: Sequence[Tuple[str, float]],
    *,
    top_k: int,
) -> List[Tuple[str, float]]:
    """RRF-style fusion (stable on tiny corpora)."""
    rrf: Dict[str, float] = {}
    for rank, (nid, _) in enumerate(dense):
        rrf[nid] = rrf.get(nid, 0.0) + 1.0 / (60 + rank + 1)
    for rank, (nid, _) in enumerate(bm25):
        rrf[nid] = rrf.get(nid, 0.0) + 1.0 / (60 + rank + 1)
    ordered = sorted(rrf.items(), key=lambda kv: kv[1], reverse=True)
    return ordered[:top_k]


# --------------------------------------------------------------------------- #
# Main entry point
# --------------------------------------------------------------------------- #

def collect_seeds(
    *,
    views: Dict[str, ViewIndex],
    schema: QuerySchema,
    query_vec: np.ndarray,
    schema_vec: np.ndarray | None,
    seed_top_k: int,
) -> SeedScores:
    """Return seed scores for each of the four views.

    * skill_master / prototype_* views are matched against the *problem*
      dense vector (and, where useful, BM25 over problem tokens).
    * signal_view is matched against the *schema* dense vector (built
      from the Query Schema) — if that's None we fall back to the
      problem vector.
    """
    result = SeedScores()

    problem_tokens = tokenize(schema.raw_problem_text)
    schema_tokens = tokenize(
        " ".join(
            schema.candidate_families
            + schema.mechanism_hints
            + schema.signal_tags
            + schema.operation_tags
            + schema.goal_tags
            + schema.input_shapes
            + schema.keywords
        )
    )
    effective_schema_vec = schema_vec if schema_vec is not None and schema_vec.size else query_vec

    plans = [
        ("skill_master", query_vec, problem_tokens),
        ("signal_view", effective_schema_vec, schema_tokens),
        ("prototype_problem", query_vec, problem_tokens),
        ("prototype_solution", query_vec, problem_tokens),
    ]
    for view_name, dvec, stokens in plans:
        idx = views.get(view_name)
        if idx is None:
            continue
        dense = _dense_topk(idx, dvec, seed_top_k)
        bm25 = _bm25_topk(idx, stokens, seed_top_k)
        fused = _fuse_dense_bm25(dense, bm25, top_k=seed_top_k)
        result.topk_by_view[view_name] = fused
        result.scores_by_view[view_name] = _normalize_rank_scores(fused, k=seed_top_k)

    return result
