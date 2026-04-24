"""Build BM25 + dense (bge) indices over the Stage D skill cards.

Index artefacts:
  outputs/stage_e/index/
    ├── skills.jsonl            # full skill records (one per id, dedup'ed)
    ├── bm25_corpus.json        # tokenised corpus (BM25 needs pre-tokens)
    ├── dense_embeddings.npy    # shape (N, D), float32, L2-normalised
    └── index_meta.json         # metadata (model name, dims, skill_ids order)
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import numpy as np

from ..io_utils import load_jsonl, save_json
from ..logging_utils import get_logger
from ..settings import Settings

LOG = get_logger(__name__)


def _skill_retrieval_text(skill: dict[str, Any]) -> str:
    """Flatten a skill card into a single retrievable text block."""
    parts: list[str] = []
    parts.append(skill.get("skill_name") or skill.get("skill_id", ""))
    parts.append("Families: " + ", ".join(skill.get("families") or []))
    if skill.get("core_idea"):
        parts.append("Core idea: " + skill["core_idea"])
    if skill.get("applicable_when"):
        parts.append("Applicable when: " + "; ".join(skill["applicable_when"]))
    if skill.get("problem_signals"):
        parts.append("Problem signals: " + "; ".join(skill["problem_signals"]))
    if skill.get("template_strategy"):
        parts.append("Template strategy: " + " | ".join(skill["template_strategy"]))
    if skill.get("complexity_pattern"):
        parts.append("Complexity: " + skill["complexity_pattern"])
    if skill.get("retrieval_text"):
        parts.append(skill["retrieval_text"])
    return "\n".join(p for p in parts if p)


_TOKEN_RE = re.compile(r"[A-Za-z0-9]+")


def _tokenize(text: str) -> list[str]:
    return [t.lower() for t in _TOKEN_RE.findall(text or "")]


def _load_dense_encoder(model_name: str, device: str):
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "Install sentence-transformers first (pip install sentence-transformers)."
        ) from exc
    LOG.info("Loading dense encoder: %s (device=%s)", model_name, device)
    return SentenceTransformer(model_name, device=device)


def build_index(settings: Settings, *, mode: str | None = None) -> Path:
    """Build the retrieval index.

    * `mode="flat"` — legacy hybrid BM25 + dense skill index (default when
      `rag.retrieval.mode == "flat"`).
    * `mode="graph"` — full heterogeneous Graph RAG index.
    * `mode=None` — pick based on `rag.retrieval.mode` in config.
    """
    effective = (mode or settings.config["rag"]["retrieval"].get("mode") or "flat").lower()
    if effective == "graph":
        from .graph_build import build_graph_index
        return build_graph_index(settings)
    return _build_flat_index(settings)


def _build_flat_index(settings: Settings) -> Path:
    skill_path = settings.stage_dir("stage_d") / "skills_merged.jsonl"
    if not skill_path.exists():
        raise FileNotFoundError(f"Stage D skills missing at {skill_path}")

    skills = load_jsonl(skill_path)
    # dedup by skill_id, keep first
    seen: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for s in skills:
        sid = s.get("skill_id")
        if not sid or sid in seen:
            continue
        seen.add(sid)
        deduped.append(s)

    index_dir_raw = settings.config["rag"]["index"]["index_dir"]
    index_dir = Path(index_dir_raw)
    if not index_dir.is_absolute():
        index_dir = settings.project_root / index_dir_raw
    index_dir.mkdir(parents=True, exist_ok=True)

    # Skill corpus
    texts = [_skill_retrieval_text(s) for s in deduped]
    tokens = [_tokenize(t) for t in texts]
    with open(index_dir / "skills.jsonl", "w", encoding="utf-8") as fh:
        for s in deduped:
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")
    save_json(index_dir / "bm25_corpus.json", {
        "skill_ids": [s["skill_id"] for s in deduped],
        "tokens": tokens,
        "texts": texts,
    })

    # Dense embeddings
    encoder = _load_dense_encoder(settings.embed.model, settings.embed.device)
    embeddings = encoder.encode(
        texts,
        batch_size=16,
        normalize_embeddings=True,
        show_progress_bar=True,
        convert_to_numpy=True,
    ).astype(np.float32)
    np.save(index_dir / "dense_embeddings.npy", embeddings)

    save_json(index_dir / "index_meta.json", {
        "dense_model": settings.embed.model,
        "dense_dim": int(embeddings.shape[1]),
        "n_skills": len(deduped),
        "skill_ids": [s["skill_id"] for s in deduped],
    })
    LOG.info("Index built at %s (n=%d, dim=%d)", index_dir, embeddings.shape[0], embeddings.shape[1])
    return index_dir
