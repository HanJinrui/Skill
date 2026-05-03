"""End-to-end offline graph-index build.

Reads Stage A/B/C/D artifacts, produces the full heterogeneous skill
graph + multi-view indices, and persists everything under
`outputs/stage_e/graph_index/`.

The public entry point is `build_graph_index(settings)`. The flat index
built by `build_index.build_index(...)` is untouched — callers can build
both.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Sequence

import numpy as np

from ..io_utils import load_jsonl, save_json, write_jsonl
from ..logging_utils import get_logger
from ..settings import Settings
from .graph_edges import (
    build_bundle_contains_edges,
    build_family_mechanism_edges,
    build_mechanism_conflict_edges,
    build_prototype_problem_edges,
    build_prototype_solution_edges,
    build_skill_conflict_edges,
    build_skill_cooccur_edges,
    build_skill_family_edges,
    build_skill_mechanism_edges,
    build_skill_signal_edges,
)
from .graph_nodes import (
    build_family_nodes,
    build_mechanism_nodes,
    build_prototype_nodes,
    build_signal_nodes,
    build_skill_nodes,
)
from .prototype_index import build_multi_view_indices

LOG = get_logger(__name__)


def _resolve_graph_dir(settings: Settings, *, skill_source: str = "legacy") -> Path:
    cfg = settings.config["rag"].get("graph_index", {}) or {}
    raw = cfg.get("dir") or "outputs/stage_e/graph_index"
    if skill_source == "v2":
        v2_raw = cfg.get("v2_dir")
        if v2_raw:
            raw = v2_raw
        else:
            return settings.output_dir / "stage_e" / "graph_index_v2"
    p = Path(raw)
    if not p.is_absolute():
        parts = p.parts
        if parts and parts[0] == "outputs":
            p = settings.output_dir.joinpath(*parts[1:])
        else:
            p = settings.project_root / p
    return p


def _router_rows_to_labels(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in rows:
        fams = [f for f in (row.get("candidate_families") or []) if isinstance(f, str)]
        out.append({
            "problem_id": row.get("problem_id"),
            "problem_summary": (row.get("problem_statement") or "")[:500],
            "rule_candidates": fams,
            "normalized_single_skill": fams[0] if fams else None,
            "normalized_multi_skills": fams,
            "is_multi_skill": bool(row.get("is_multi_skill_problem")) or len(fams) >= 2,
            "original_tags": list(row.get("original_tags") or []),
        })
    return out


def _load_sources(settings: Settings, *, skill_source: str = "legacy") -> Dict[str, Any]:
    out_dir = settings.output_dir
    if skill_source == "v2":
        skills = load_jsonl(out_dir / "stage_d_v2" / "skills_merged_v2.jsonl")
        # Only primary full-pass solutions become graph prototypes in v2.
        solutions = [
            row for row in load_jsonl(out_dir / "stage_c" / "solution_labeled.jsonl")
            if row.get("is_primary_solution")
        ]
        router_rows = load_jsonl(out_dir / "stage_c0" / "router_dataset.jsonl")
        problem_labels = _router_rows_to_labels(router_rows)
        problems_multi = router_rows
        multi_compositions = load_jsonl(out_dir / "stage_c0" / "multi_skill_composition_dataset.jsonl")
    else:
        skills = load_jsonl(out_dir / "stage_d" / "skills_merged.jsonl")
        solutions = load_jsonl(out_dir / "stage_c" / "solution_consistent.jsonl")
        problem_labels = load_jsonl(out_dir / "stage_b" / "problem_labels.jsonl")
        problems_multi = load_jsonl(out_dir / "stage_a" / "selected_problems_multi.jsonl")
        multi_compositions = []
    return {
        "skills": skills,
        "solutions": solutions,
        "problem_labels": problem_labels,
        "problems_multi": problems_multi,
        "multi_compositions": multi_compositions,
    }


def _default_encoder(settings: Settings) -> Callable[[Sequence[str]], np.ndarray]:
    """Return a L2-normalised batch encoder using the configured bge model."""
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "Install sentence-transformers first (pip install sentence-transformers)."
        ) from exc
    model_name = settings.embed.model
    device = settings.embed.device
    LOG.info("Loading dense encoder for graph build: %s (device=%s)", model_name, device)
    model = SentenceTransformer(model_name, device=device)

    def _encode(texts: Sequence[str]) -> np.ndarray:
        if not texts:
            return np.zeros((0, model.get_sentence_embedding_dimension() or 0), dtype=np.float32)
        return model.encode(
            list(texts),
            batch_size=16,
            normalize_embeddings=True,
            show_progress_bar=False,
            convert_to_numpy=True,
        ).astype(np.float32)

    return _encode


def build_graph_index(
    settings: Settings,
    *,
    encoder: Callable[[Sequence[str]], np.ndarray] | None = None,
    skill_source: str = "legacy",
) -> Path:
    """Build and persist the full graph index. Returns the output dir."""
    sources = _load_sources(settings, skill_source=skill_source)
    if not sources["skills"]:
        raise FileNotFoundError(
            "skills_merged.jsonl missing or empty — run Stage D first."
        )

    graph_dir = _resolve_graph_dir(settings, skill_source=skill_source)
    graph_dir.mkdir(parents=True, exist_ok=True)

    # ---------------- Nodes ----------------
    skill_nodes = build_skill_nodes(sources["skills"])
    family_nodes = build_family_nodes()
    mechanism_nodes = build_mechanism_nodes()
    signal_nodes = build_signal_nodes()

    problems_by_id = {p["problem_id"]: p for p in sources["problems_multi"] if isinstance(p, dict)}
    labels_by_id = {p["problem_id"]: p for p in sources["problem_labels"] if isinstance(p, dict)}

    rag_cfg = settings.config["rag"].get("retrieval", {})
    max_proto_per_skill = int(settings.config["rag"].get("graph_index", {}).get(
        "max_prototype_per_skill_build", 8
    ))

    proto_problem_nodes, proto_solution_nodes = build_prototype_nodes(
        solutions=sources["solutions"],
        problems_by_id=problems_by_id,
        problem_labels_by_id=labels_by_id,
        existing_skill_ids=[s["skill_id"] for s in skill_nodes],
        max_prototype_per_skill=max_proto_per_skill,
    )

    # ---------------- Edges ----------------
    edges: List[Dict[str, Any]] = []
    edges += build_skill_family_edges(skill_nodes)
    edges += build_family_mechanism_edges()
    edges += build_skill_mechanism_edges(skill_nodes)
    edges += build_skill_signal_edges(skill_nodes)
    edges += build_prototype_problem_edges(proto_problem_nodes)
    edges += build_prototype_solution_edges(proto_solution_nodes)
    edges += build_bundle_contains_edges(skill_nodes)
    edges += build_skill_cooccur_edges(
        skill_nodes=skill_nodes,
        problem_labels=sources["problem_labels"],
        solutions=sources["solutions"],
        composition_rows=sources.get("multi_compositions") or None,
    )
    edges += build_skill_conflict_edges(skill_nodes)
    edges += build_mechanism_conflict_edges()

    # ---------------- Persist node + edge tables ----------------
    write_jsonl(graph_dir / "nodes_skill.jsonl", skill_nodes)
    write_jsonl(graph_dir / "nodes_family.jsonl", family_nodes)
    write_jsonl(graph_dir / "nodes_mechanism.jsonl", mechanism_nodes)
    write_jsonl(graph_dir / "nodes_signal.jsonl", signal_nodes)
    write_jsonl(graph_dir / "nodes_prototype_problem.jsonl", proto_problem_nodes)
    write_jsonl(graph_dir / "nodes_prototype_solution.jsonl", proto_solution_nodes)
    write_jsonl(graph_dir / "edges.jsonl", edges)

    # ---------------- Multi-view indices ----------------
    encoder = encoder or _default_encoder(settings)
    index_summary = build_multi_view_indices(
        skill_nodes=skill_nodes,
        proto_problem_nodes=proto_problem_nodes,
        proto_solution_nodes=proto_solution_nodes,
        encoder=encoder,
        out_dir=graph_dir,
    )

    # ---------------- Meta ----------------
    meta = {
        "schema_version": "graph_rag@v2" if skill_source == "v2" else "graph_rag@v1",
        "skill_source": skill_source,
        "counts": {
            "skill_nodes": len(skill_nodes),
            "family_nodes": len(family_nodes),
            "mechanism_nodes": len(mechanism_nodes),
            "signal_nodes": len(signal_nodes),
            "prototype_problem_nodes": len(proto_problem_nodes),
            "prototype_solution_nodes": len(proto_solution_nodes),
            "edges": len(edges),
        },
        "edge_types": _edge_type_counts(edges),
        "indices": index_summary,
        "source_files": {
            "skills": "outputs/stage_d_v2/skills_merged_v2.jsonl" if skill_source == "v2" else "outputs/stage_d/skills_merged.jsonl",
            "solutions": "outputs/stage_c/solution_labeled.jsonl" if skill_source == "v2" else "outputs/stage_c/solution_consistent.jsonl",
            "problem_labels": "outputs/stage_c0/router_dataset.jsonl" if skill_source == "v2" else "outputs/stage_b/problem_labels.jsonl",
            "problems_multi": "outputs/stage_c0/router_dataset.jsonl" if skill_source == "v2" else "outputs/stage_a/selected_problems_multi.jsonl",
            "multi_compositions": "outputs/stage_c0/multi_skill_composition_dataset.jsonl" if skill_source == "v2" else "",
        },
        "dense_model": settings.embed.model,
    }
    save_json(graph_dir / "graph_meta.json", meta)

    LOG.info(
        "Graph index built at %s (nodes=%s, edges=%d)",
        graph_dir, {k: v for k, v in meta["counts"].items()}, len(edges),
    )
    return graph_dir


def _edge_type_counts(edges: Sequence[Dict[str, Any]]) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for e in edges:
        out[e["edge_type"]] = out.get(e["edge_type"], 0) + 1
    return out
