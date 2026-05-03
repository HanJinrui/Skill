"""Stage E runner — build the skill retrieval index.

By default we respect `rag.retrieval.mode` from `config.yaml`:

* `flat`  — hybrid BM25 + dense index (legacy).
* `graph` — full heterogeneous Skill Graph RAG index.

CLI flags override the config mode, and `--both` builds both indices so
A/B evaluation can toggle `rag.retrieval.mode` without rebuilding.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.logging_utils import setup_logging, get_logger  # noqa: E402
from src.rag.build_index import build_index  # noqa: E402
from src.settings import get_settings  # noqa: E402


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stage E: build skill retrieval index")
    p.add_argument("--mode", choices=["flat", "graph", "subtype", "graph_subtype", "both", "both_v2"], default=None,
                   help="force a build mode; defaults to rag.retrieval.mode in config.yaml")
    return p.parse_args()


def main() -> int:
    args = _parse_args()
    settings = get_settings()
    setup_logging(settings.config["logging"]["level"], settings.output_dir / "run.log")
    log = get_logger("stage_e")

    configured = str(settings.config["rag"]["retrieval"].get("mode") or "flat").lower()
    mode = args.mode or configured
    log.info("Starting Stage E — mode=%s (configured=%s)", mode, configured)

    if mode == "both":
        flat_dir = build_index(settings, mode="flat")
        graph_dir = build_index(settings, mode="graph")
        log.info("Flat index: %s", flat_dir)
        log.info("Graph index: %s", graph_dir)
    elif mode == "both_v2":
        subtype_dir = build_index(settings, mode="subtype")
        graph_subtype_dir = build_index(settings, mode="graph_subtype")
        log.info("Subtype flat index: %s", subtype_dir)
        log.info("Graph subtype index: %s", graph_subtype_dir)
    else:
        out_dir = build_index(settings, mode=mode)
        log.info("Index built at %s", out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
