#!/usr/bin/env python3
"""Verify that the configured local Qwen directory can be used offline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import load_settings  # noqa: E402
from src.qwen_client import QwenLocalClient  # noqa: E402


REQUIRED_FILES = [
    "config.json",
    "generation_config.json",
    "tokenizer.json",
    "tokenizer_config.json",
    "model.safetensors.index.json",
]


def inspect_local_model(model_dir: Path) -> dict[str, object]:
    if not model_dir.is_dir():
        raise FileNotFoundError(f"Configured local model directory is missing: {model_dir}")
    missing = [name for name in REQUIRED_FILES if not (model_dir / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Local model is incomplete; missing files: {missing}")
    config = json.loads((model_dir / "config.json").read_text(encoding="utf-8"))
    index = json.loads((model_dir / "model.safetensors.index.json").read_text(encoding="utf-8"))
    shards = sorted(set((index.get("weight_map") or {}).values()))
    missing_shards = [name for name in shards if not (model_dir / name).is_file()]
    if missing_shards:
        raise FileNotFoundError(f"Local model index references missing shards: {missing_shards}")
    return {
        "model_dir": str(model_dir),
        "model_type": config.get("model_type"),
        "architectures": config.get("architectures") or [],
        "indexed_shards": shards,
        "indexed_shard_bytes": sum((model_dir / name).stat().st_size for name in shards),
        "extra_broken_shard_ignored": (model_dir / "model-00001-of-00004.safetensors.broken").exists(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify local Qwen assets configured for skill_router_mvp.")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--tokenizer", action="store_true", help="Load tokenizer from the configured local directory.")
    parser.add_argument("--generate-smoke", action="store_true", help="Load the model on GPU and run a short generation.")
    args = parser.parse_args()
    settings = load_settings(args.config)
    model_dir = Path(settings.model_ref()).resolve()
    result = inspect_local_model(model_dir)
    if args.tokenizer:
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(str(model_dir), local_files_only=True, trust_remote_code=False)
        result["tokenizer_class"] = type(tokenizer).__name__
        result["chat_template_available"] = bool(getattr(tokenizer, "chat_template", None))
    if args.generate_smoke:
        llm = QwenLocalClient(settings)
        completion = llm.generate(
            "You are a code generator. Output only Python code.",
            "Write a Python expression that prints 42.",
            temperature=0.0,
            max_new_tokens=32,
        )
        result["generation_smoke_output"] = completion.strip()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
