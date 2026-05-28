#!/usr/bin/env python3
"""Freeze the 67-card bank and build its standalone retrieval index."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import load_settings  # noqa: E402
from src.retriever import HybridRetriever  # noqa: E402
from src.skill_bank import SkillBank  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the standalone bank67 retrieval index.")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument(
        "--lexical-only",
        action="store_true",
        help="Write bank/BM25 artifacts without loading the dense encoder; useful only for smoke checks.",
    )
    args = parser.parse_args()
    settings = load_settings(args.config)
    if args.lexical_only:
        formal_index = settings.path("index_dir")
        smoke_index = formal_index.with_name(formal_index.name + "_lexical_smoke")
        settings = load_settings(args.config, overrides={"paths": {"index_dir": str(smoke_index)}})
    bank = SkillBank.from_settings(settings)
    path = HybridRetriever.build_index(settings, bank, build_dense=not args.lexical_only)
    print(json.dumps({"index_dir": str(path), **bank.metadata}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
