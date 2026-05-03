"""Multi-view index builder.

Given the node tables produced by `graph_nodes`, build & persist:

* `skill_master` — one doc per skill_id (broad retrieval text),
* `signal_view` — one doc per skill_id (signal / constraint / mechanism keywords only),
* `prototype_problem` — one doc per prototype problem,
* `prototype_solution` — one doc per prototype solution,
* `facet_inverted_index` — facet → skill_id[] (exact-match filtering).

Each view is persisted as:

    {view}_dense.npy          # shape (N, D) float32, normalised
    {view}_meta.json          # order of node_ids + a few stats
    sparse_corpus_{view}.json # tokens/texts for BM25 at query time

This module is intentionally small — the heavy lifting is done by the
dense encoder the caller passes in (we don't know if we're on CPU/GPU).
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Sequence, Tuple

import numpy as np

from ..io_utils import save_json


_TOKEN_RE = re.compile(r"[A-Za-z0-9]+")
_GENERIC_SIGNAL_VIEW_TAGS = frozenset({"maximize", "minimize", "construct"})
_GENERIC_SIGNAL_WORD_RE = re.compile(r"\b(maximize|minimize|construct\w*)\b", re.IGNORECASE)


def tokenize(text: str) -> List[str]:
    return [t.lower() for t in _TOKEN_RE.findall(text or "")]


# --------------------------------------------------------------------------- #
# Per-view text assembly
# --------------------------------------------------------------------------- #

def skill_master_text(skill: Dict[str, Any]) -> str:
    """Broad retrieval text for a skill — mirrors the flat retriever's
    blob so the graph retriever has equivalent lexical coverage."""
    parts: List[str] = []
    parts.append(skill.get("skill_name") or skill.get("skill_id", ""))
    parts.append("Families: " + ", ".join(skill.get("families") or []))
    if skill.get("core_idea"):
        parts.append("Core idea: " + str(skill["core_idea"]))
    if skill.get("applicable_when"):
        parts.append("Applicable when: " + "; ".join(skill["applicable_when"]))
    if skill.get("problem_signals"):
        parts.append("Problem signals: " + "; ".join(skill["problem_signals"]))
    if skill.get("template_strategy"):
        parts.append("Template strategy: " + " | ".join(skill["template_strategy"]))
    if skill.get("complexity_pattern"):
        parts.append("Complexity: " + str(skill["complexity_pattern"]))
    if skill.get("retrieval_text"):
        parts.append(str(skill["retrieval_text"]))
    return "\n".join(p for p in parts if p)


def signal_view_text(skill: Dict[str, Any]) -> str:
    """Retrieval doc focused on signals / mechanisms / constraints only.

    This view is meant to be matched against the Query Schema, not the
    raw problem — it's short and keyword-dense on purpose.
    """
    facets = skill.get("facets") or {}
    parts: List[str] = []
    parts.append(skill.get("skill_name") or skill.get("skill_id", ""))
    parts.append("Families: " + " ".join(skill.get("families") or []))
    if facets.get("mechanism_tags"):
        parts.append("Mechanisms: " + " ".join(facets["mechanism_tags"]))
    signal_tags = [s for s in (facets.get("signal_tags") or []) if s not in _GENERIC_SIGNAL_VIEW_TAGS]
    if signal_tags:
        parts.append("Signals: " + " ".join(signal_tags))
    if facets.get("operation_tags"):
        parts.append("Operations: " + " ".join(facets["operation_tags"]))
    if facets.get("input_shape_tags"):
        parts.append("Shapes: " + " ".join(facets["input_shape_tags"]))
    goal_tags = [s for s in (facets.get("goal_tags") or []) if s not in _GENERIC_SIGNAL_VIEW_TAGS]
    if goal_tags:
        parts.append("Goals: " + " ".join(goal_tags))
    if facets.get("complexity_tags"):
        parts.append("Complexity: " + " ".join(facets["complexity_tags"]))
    if skill.get("problem_signals"):
        filtered = [
            str(item) for item in skill["problem_signals"]
            if str(item).lower() not in _GENERIC_SIGNAL_VIEW_TAGS
        ]
        parts.append(" ".join(filtered))
    text = "\n".join(p for p in parts if p)
    return _GENERIC_SIGNAL_WORD_RE.sub(" ", text)


def prototype_problem_text(node: Dict[str, Any]) -> str:
    parts: List[str] = []
    parts.append(f"skill:{node.get('skill_id', '')}")
    parts.append(str(node.get("problem_summary") or ""))
    parts.append(str(node.get("problem_text_snippet") or ""))
    facets = node.get("facets") or {}
    for k in ("signal_tags", "operation_tags", "input_shape_tags", "goal_tags"):
        vals = facets.get(k) or []
        if vals:
            parts.append(" ".join(vals))
    return "\n".join(p for p in parts if p)


def prototype_solution_text(node: Dict[str, Any]) -> str:
    parts: List[str] = []
    parts.append(f"skill:{node.get('skill_id', '')}")
    parts.append(str(node.get("core_mechanism_summary") or ""))
    mechs = node.get("mechanism_tags") or []
    if mechs:
        parts.append("Mechanisms: " + " ".join(mechs))
    hints = node.get("ast_hints") or []
    if hints:
        parts.append("Hints: " + " ".join(str(h) for h in hints))
    facets = node.get("facets") or {}
    for k in ("signal_tags", "operation_tags"):
        vals = facets.get(k) or []
        if vals:
            parts.append(" ".join(vals))
    return "\n".join(p for p in parts if p)


# --------------------------------------------------------------------------- #
# Dense + sparse persistence
# --------------------------------------------------------------------------- #

def _persist_dense(
    *,
    view: str,
    node_ids: Sequence[str],
    texts: Sequence[str],
    encoder: Callable[[Sequence[str]], np.ndarray],
    out_dir: Path,
) -> int:
    if not texts:
        embeddings = np.zeros((0, 0), dtype=np.float32)
    else:
        embeddings = encoder(list(texts)).astype(np.float32)
    np.save(out_dir / f"{view}_dense.npy", embeddings)
    dim = int(embeddings.shape[1]) if embeddings.size else 0
    save_json(out_dir / f"{view}_meta.json", {
        "view": view,
        "n_items": len(node_ids),
        "dense_dim": dim,
        "node_ids": list(node_ids),
    })
    return dim


def _persist_sparse(
    *,
    view: str,
    node_ids: Sequence[str],
    texts: Sequence[str],
    out_dir: Path,
) -> None:
    tokens = [tokenize(t) for t in texts]
    save_json(out_dir / f"sparse_corpus_{view}.json", {
        "view": view,
        "node_ids": list(node_ids),
        "tokens": tokens,
        "texts": list(texts),
    })


def _build_view(
    *,
    view: str,
    items: Sequence[Dict[str, Any]],
    text_fn: Callable[[Dict[str, Any]], str],
    key: str,
    encoder: Callable[[Sequence[str]], np.ndarray],
    out_dir: Path,
) -> Tuple[int, int]:
    node_ids: List[str] = []
    texts: List[str] = []
    for item in items:
        nid = item.get(key)
        if not isinstance(nid, str):
            continue
        node_ids.append(nid)
        texts.append(text_fn(item))
    dim = _persist_dense(
        view=view, node_ids=node_ids, texts=texts,
        encoder=encoder, out_dir=out_dir,
    )
    _persist_sparse(view=view, node_ids=node_ids, texts=texts, out_dir=out_dir)
    return len(node_ids), dim


def build_multi_view_indices(
    *,
    skill_nodes: Sequence[Dict[str, Any]],
    proto_problem_nodes: Sequence[Dict[str, Any]],
    proto_solution_nodes: Sequence[Dict[str, Any]],
    encoder: Callable[[Sequence[str]], np.ndarray],
    out_dir: Path,
) -> Dict[str, Any]:
    """Build and persist all four dense / sparse views + the facet index.

    `encoder(texts)` must return an (N, D) numpy array of L2-normalised
    float32 embeddings. The caller is responsible for picking the model.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    summary: Dict[str, Any] = {}

    n, dim = _build_view(
        view="skill_master", items=skill_nodes, text_fn=skill_master_text,
        key="node_id", encoder=encoder, out_dir=out_dir,
    )
    summary["skill_master"] = {"n_items": n, "dense_dim": dim}

    n, dim = _build_view(
        view="signal_view", items=skill_nodes, text_fn=signal_view_text,
        key="node_id", encoder=encoder, out_dir=out_dir,
    )
    summary["signal_view"] = {"n_items": n, "dense_dim": dim}

    n, dim = _build_view(
        view="prototype_problem", items=proto_problem_nodes,
        text_fn=prototype_problem_text, key="node_id",
        encoder=encoder, out_dir=out_dir,
    )
    summary["prototype_problem"] = {"n_items": n, "dense_dim": dim}

    n, dim = _build_view(
        view="prototype_solution", items=proto_solution_nodes,
        text_fn=prototype_solution_text, key="node_id",
        encoder=encoder, out_dir=out_dir,
    )
    summary["prototype_solution"] = {"n_items": n, "dense_dim": dim}

    # Facet inverted index for exact-match filtering.
    facet_idx = build_facet_inverted_index(skill_nodes)
    save_json(out_dir / "facet_index.json", facet_idx)
    summary["facet_index"] = {k: len(v) for k, v in facet_idx.items()}
    return summary


def build_facet_inverted_index(
    skill_nodes: Sequence[Dict[str, Any]],
) -> Dict[str, Dict[str, List[str]]]:
    """Return {facet_type: {value: [skill_id, ...]}}."""
    facet_types = (
        "mechanism_tags",
        "signal_tags",
        "input_shape_tags",
        "operation_tags",
        "goal_tags",
        "complexity_tags",
        "negative_tags",
    )
    out: Dict[str, Dict[str, List[str]]] = {k: {} for k in facet_types}
    # Also index families directly.
    out["families"] = {}
    for s in skill_nodes:
        sid = s.get("skill_id")
        if not isinstance(sid, str):
            continue
        for fam in s.get("families") or []:
            out["families"].setdefault(fam, []).append(sid)
        for ftype in facet_types:
            for val in (s.get(ftype) or []):
                out[ftype].setdefault(val, []).append(sid)
    return out
