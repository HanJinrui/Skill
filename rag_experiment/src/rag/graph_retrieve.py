"""Online graph retriever.

Flow:

    raw problem text
      → query_analyzer.analyze  (Query Schema; no LLM)
      → dense/BM25 seed retrieval across 4 views
      → facet pre-filter / boost
      → typed constrained propagation
      → bundle assembly
      → hydration (evidence + core card)
      → RetrievalResult (flat-retriever compatible + graph-specific fields)

The retriever caches everything heavy (graph edges, dense matrices,
encoder) in memory, so per-query cost is dominated by one dense
encoding of the problem and short BM25 passes over tiny corpora.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Sequence

import numpy as np

from ..io_utils import load_json, load_jsonl
from ..logging_utils import get_logger
from ..settings import Settings
from .graph_bundle import Bundle, assemble_bundle
from .graph_hydrate import SkillEvidence, hydrate_bundle
from .graph_propagation import (
    build_slice,
    distribute_seeds_to_skills,
    facet_boost,
    propagate,
)
from .graph_schema import (
    EDGE_BUNDLE_CONTAINS_SKILL,
    EDGE_MECHANISM_CONFLICTS_MECHANISM,
    EDGE_PROTO_PROB_HAS_SIGNAL,
    EDGE_PROTO_PROB_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_SUPPORTS_SKILL,
    EDGE_PROTO_SOL_USES_MECHANISM,
    EDGE_SKILL_CONFLICTS_SKILL,
    EDGE_SKILL_COOCCURS_SKILL,
    EDGE_SKILL_HAS_FAMILY,
    EDGE_SKILL_IMPLEMENTS_MECHANISM,
    EDGE_SKILL_TRIGGERED_BY_SIGNAL,
    parse_node_id,
    skill_node_id,
)
from .graph_seed import ViewIndex, collect_seeds, load_view_index
from .query_analyzer import QuerySchema, analyze
from .retrieve import RetrievalResult

LOG = get_logger(__name__)


_DEFAULT_EDGE_WEIGHTS: Dict[str, float] = {
    EDGE_SKILL_HAS_FAMILY: 0.5,
    EDGE_SKILL_IMPLEMENTS_MECHANISM: 1.0,
    EDGE_SKILL_TRIGGERED_BY_SIGNAL: 0.9,
    EDGE_PROTO_PROB_SUPPORTS_SKILL: 0.8,
    EDGE_PROTO_SOL_SUPPORTS_SKILL: 1.2,
    EDGE_SKILL_COOCCURS_SKILL: 0.5,
    EDGE_BUNDLE_CONTAINS_SKILL: 0.6,
    EDGE_PROTO_PROB_HAS_SIGNAL: 0.4,
    EDGE_PROTO_SOL_USES_MECHANISM: 0.6,
    EDGE_SKILL_CONFLICTS_SKILL: 1.0,
    EDGE_MECHANISM_CONFLICTS_MECHANISM: 1.0,
}


class GraphRetriever:
    def __init__(
        self,
        *,
        graph_dir: Path,
        dense_model: str,
        device: str,
        seed_top_k: int,
        candidate_top_k: int,
        final_top_k: int,
        graph_alpha: float,
        graph_steps: int,
        conflict_penalty: float,
        max_bundle_size: int,
        max_prototype_per_skill: int,
        edge_weights: Dict[str, float],
        bm25_k1: float = 1.5,
        bm25_b: float = 0.75,
    ) -> None:
        self.graph_dir = graph_dir
        self.seed_top_k = seed_top_k
        self.candidate_top_k = candidate_top_k
        self.final_top_k = final_top_k
        self.graph_alpha = graph_alpha
        self.graph_steps = graph_steps
        self.conflict_penalty = conflict_penalty
        self.max_bundle_size = max_bundle_size
        self.max_prototype_per_skill = max_prototype_per_skill
        self.edge_weights = {**_DEFAULT_EDGE_WEIGHTS, **(edge_weights or {})}

        # ---- Load node / edge tables
        self.skill_nodes: List[Dict[str, Any]] = load_jsonl(graph_dir / "nodes_skill.jsonl")
        self.family_nodes: List[Dict[str, Any]] = load_jsonl(graph_dir / "nodes_family.jsonl")
        self.mechanism_nodes: List[Dict[str, Any]] = load_jsonl(graph_dir / "nodes_mechanism.jsonl")
        self.signal_nodes: List[Dict[str, Any]] = load_jsonl(graph_dir / "nodes_signal.jsonl")
        self.proto_problem_nodes: List[Dict[str, Any]] = load_jsonl(graph_dir / "nodes_prototype_problem.jsonl")
        self.proto_solution_nodes: List[Dict[str, Any]] = load_jsonl(graph_dir / "nodes_prototype_solution.jsonl")
        self.edges: List[Dict[str, Any]] = load_jsonl(graph_dir / "edges.jsonl")

        self.skills_by_id: Dict[str, Dict[str, Any]] = {s["skill_id"]: s for s in self.skill_nodes}
        self.proto_nodes_by_id: Dict[str, Dict[str, Any]] = {}
        for n in self.proto_problem_nodes:
            self.proto_nodes_by_id[n["node_id"]] = n
        for n in self.proto_solution_nodes:
            self.proto_nodes_by_id[n["node_id"]] = n

        self.graph = build_slice(
            skill_nodes=self.skill_nodes,
            proto_problem_nodes=self.proto_problem_nodes,
            proto_solution_nodes=self.proto_solution_nodes,
            family_nodes=self.family_nodes,
            mechanism_nodes=self.mechanism_nodes,
            signal_nodes=self.signal_nodes,
            edges=self.edges,
        )

        # ---- Load multi-view indices
        self.views: Dict[str, ViewIndex] = {}
        for v in ("skill_master", "signal_view", "prototype_problem", "prototype_solution"):
            try:
                self.views[v] = load_view_index(graph_dir, v, bm25_k1=bm25_k1, bm25_b=bm25_b)
            except FileNotFoundError:
                LOG.warning("Graph view %s missing — skipping.", v)

        # ---- Dense encoder
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("Install sentence-transformers.") from exc
        self._encoder = SentenceTransformer(dense_model, device=device)

        # ---- Facet index
        facet_path = graph_dir / "facet_index.json"
        self.facet_index: Dict[str, Dict[str, List[str]]] = (
            load_json(facet_path) if facet_path.exists() else {}
        )

    # ----------------------------------------------------------------- #
    # Factories
    # ----------------------------------------------------------------- #

    @classmethod
    def from_settings(cls, settings: Settings) -> "GraphRetriever":
        rag_cfg = settings.config["rag"]
        ret_cfg = rag_cfg.get("retrieval", {}) or {}
        idx_cfg = rag_cfg.get("graph_index", {}) or {}
        raw_dir = idx_cfg.get("dir") or "outputs/stage_e/graph_index"
        graph_dir = Path(raw_dir)
        if not graph_dir.is_absolute():
            graph_dir = settings.project_root / raw_dir
        return cls(
            graph_dir=graph_dir,
            dense_model=settings.embed.model,
            device=settings.embed.device,
            seed_top_k=int(ret_cfg.get("seed_top_k", 20)),
            candidate_top_k=int(ret_cfg.get("candidate_top_k", 50)),
            final_top_k=int(ret_cfg.get("final_top_k", ret_cfg.get("top_k", 3))),
            graph_alpha=float(ret_cfg.get("graph_alpha", 0.3)),
            graph_steps=int(ret_cfg.get("graph_steps", 3)),
            conflict_penalty=float(ret_cfg.get("conflict_penalty", 0.7)),
            max_bundle_size=int(ret_cfg.get("max_bundle_size", 3)),
            max_prototype_per_skill=int(ret_cfg.get("max_prototype_per_skill", 1)),
            edge_weights={**_DEFAULT_EDGE_WEIGHTS, **(ret_cfg.get("edge_weights") or {})},
            bm25_k1=float(ret_cfg.get("bm25_k1", 1.5)),
            bm25_b=float(ret_cfg.get("bm25_b", 0.75)),
        )

    # ----------------------------------------------------------------- #
    # Retrieval
    # ----------------------------------------------------------------- #

    def _encode(self, text: str) -> np.ndarray:
        if not text:
            return np.zeros((0,), dtype=np.float32)
        vec = self._encoder.encode(
            [text], normalize_embeddings=True, convert_to_numpy=True
        )[0]
        return vec.astype(np.float32)

    def analyze(self, problem_statement: str) -> QuerySchema:
        return analyze(problem_statement)

    def retrieve(self, problem_statement: str, *, top_k: int | None = None) -> RetrievalResult:
        final_k = int(top_k) if top_k is not None else self.final_top_k
        schema = self.analyze(problem_statement)
        q_vec = self._encode(schema.raw_problem_text[:2500])
        schema_text = " ".join(
            schema.candidate_families + schema.mechanism_hints + schema.signal_tags
            + schema.operation_tags + schema.goal_tags + schema.input_shapes + schema.keywords
        )
        s_vec = self._encode(schema_text) if schema_text.strip() else q_vec

        seeds = collect_seeds(
            views=self.views,
            schema=schema,
            query_vec=q_vec,
            schema_vec=s_vec,
            seed_top_k=self.seed_top_k,
        )

        # Distribute seeds across the graph into initial skill scores.
        seed_skill_scores = distribute_seeds_to_skills(
            seed_scores_by_view=seeds.scores_by_view,
            graph=self.graph,
            edge_weights=self.edge_weights,
        )
        # Facet boost / soft pre-filter.
        seed_skill_scores = facet_boost(
            base_scores=seed_skill_scores,
            skill_nodes_by_id=self.skills_by_id,
            candidate_families=schema.candidate_families,
        )

        # ---- Propagation
        all_scores = propagate(
            graph=self.graph,
            seed_skill_scores=seed_skill_scores,
            seed_signal_scores=None,
            seed_mechanism_scores=None,
            edge_weights=self.edge_weights,
            alpha=self.graph_alpha,
            steps=self.graph_steps,
            conflict_penalty=self.conflict_penalty,
            schema_signals=schema.signal_tags,
            schema_mechanisms=schema.mechanism_hints,
        )

        # ---- Bundle assembly
        bundle = assemble_bundle(
            scores=all_scores,
            skills_by_id=self.skills_by_id,
            edges_by_type=self.graph.edges_by_type,
            is_multi_skill_likely=schema.is_multi_skill_likely,
            max_bundle_size=max(self.max_bundle_size, final_k),
            max_aux=max(0, final_k - 1),
        )
        # Ensure we never emit an empty bundle when we have any skill with score > 0.
        if not bundle.primary_skill_id:
            # Fallback: pick the highest-scoring skill overall (ignoring bundles).
            ranked = sorted(
                [(sid, all_scores.get(skill_node_id(sid), 0.0))
                 for sid in self.skills_by_id],
                key=lambda kv: kv[1],
                reverse=True,
            )
            if ranked:
                bundle = Bundle(
                    primary_skill_id=ranked[0][0],
                    ordered_skill_ids=[ranked[0][0]],
                    scores={ranked[0][0]: ranked[0][1]},
                    bundle_type="fallback_top1",
                )

        ordered_sids = bundle.ordered_skill_ids[:final_k] if bundle.ordered_skill_ids else []

        # ---- Hydrate
        evidence_objs: List[SkillEvidence] = hydrate_bundle(
            ordered_skill_ids=ordered_sids,
            scores=bundle.scores,
            skills_by_id=self.skills_by_id,
            schema_signals=schema.signal_tags,
            schema_mechanisms=schema.mechanism_hints,
            edges_by_type=self.graph.edges_by_type,
            proto_nodes_by_id=self.proto_nodes_by_id,
            max_prototypes_per_skill=self.max_prototype_per_skill,
        )
        graph_evidence = [e.to_dict() for e in evidence_objs]

        # ---- Package
        skills_out = [self.skills_by_id[sid] for sid in ordered_sids if sid in self.skills_by_id]
        scores_out = [float(bundle.scores.get(sid, 0.0)) for sid in ordered_sids]

        # seed_ids per view (use top node ids from topk_by_view).
        seed_ids: Dict[str, List[str]] = {}
        for view, pairs in seeds.topk_by_view.items():
            # Strip namespace for cleaner logs (but keep full id if user wants).
            seed_ids[view] = [nid for nid, _ in pairs[: self.seed_top_k]]

        # supporting_prototypes (flattened, unique)
        supporting: List[str] = []
        seen: set = set()
        for ev in evidence_objs:
            for pp in ev.supporting_prototypes:
                if pp not in seen:
                    seen.add(pp)
                    supporting.append(pp)

        matched_signals_all: List[str] = []
        matched_mechs_all: List[str] = []
        sig_seen: set = set()
        mech_seen: set = set()
        for ev in evidence_objs:
            for s in ev.matched_signals:
                if s not in sig_seen:
                    sig_seen.add(s)
                    matched_signals_all.append(s)
            for m in ev.matched_mechanisms:
                if m not in mech_seen:
                    mech_seen.add(m)
                    matched_mechs_all.append(m)

        return RetrievalResult(
            skill_ids=list(ordered_sids),
            skills=skills_out,
            scores=scores_out,
            dense_ids=[
                parse_node_id(nid)[1]
                for nid, _ in (seeds.topk_by_view.get("skill_master") or [])[: final_k]
            ],
            bm25_ids=[
                parse_node_id(nid)[1]
                for nid, _ in (seeds.topk_by_view.get("signal_view") or [])[: final_k]
            ],
            method="graph",
            bundle_type=bundle.bundle_type,
            graph_evidence=graph_evidence,
            seed_ids=seed_ids,
            supporting_prototypes=supporting,
            matched_signals=matched_signals_all,
            matched_mechanisms=matched_mechs_all,
            query_schema=schema.to_dict(),
        )
