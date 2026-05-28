"""Orchestrate pass1 -> pass2 -> pass3 for skill_data_factory."""
from __future__ import annotations

import argparse
from pathlib import Path

from sdf.pass1_route import run_pass1_route
from sdf.pass1_verify import Pass1Options, run_pass1
from sdf.pass2_llm_label_multi import run_pass2_multi
from sdf.pass2_llm_label_single import run_pass2_single
from sdf.pass2_primary import run_pass2_primary
from sdf.pass3_evidence_multi import run_pass3_multi
from sdf.pass3_evidence_single import run_pass3_single
from sdf.pass3_export import run_pass3_export
from sdf.merge_compositions import merge_composition_ledgers
from sdf.factory_settings import get_settings
from sdf.shared import bootstrap  # noqa: F401

from src.logging_utils import get_logger, setup_logging

LOG = get_logger(__name__)


def run_pipeline(
    *,
    phase: str = "all",
    tracks: list[str] | None = None,
    resume: bool = False,
    limit_problems: int = 0,
    budget: int = 0,
    verified_source: str | None = None,
    retry_quarantine: bool = False,
    config_path: str | Path | None = None,
) -> None:
    settings = get_settings(config_path)
    setup_logging(settings.config.get("logging", {}).get("level", "INFO"), settings.factory_root / "run.log")
    tracks = tracks or ["single_algorithm", "multi_algorithm"]

    if phase in {"all", "pass1", "1"}:
        LOG.info("=== Pass1 verify ===")
        run_pass1(
            settings,
            Pass1Options(
                limit_problems=limit_problems,
                resume=resume,
                verified_source=verified_source,
            ),
        )
        LOG.info("=== Pass1 route ===")
        run_pass1_route(settings)

    if phase in {"all", "pass2", "2"}:
        if "single_algorithm" in tracks:
            LOG.info("=== Pass2 single ===")
            run_pass2_single(settings, resume=resume, budget=budget, retry_quarantine=retry_quarantine)
            run_pass2_primary(settings, "single_algorithm")
        if "multi_algorithm" in tracks:
            LOG.info("=== Pass2 multi ===")
            run_pass2_multi(settings, resume=resume, budget=budget, retry_quarantine=retry_quarantine)
            run_pass2_primary(settings, "multi_algorithm")

    if phase in {"all", "pass3", "3"}:
        if "single_algorithm" in tracks:
            LOG.info("=== Pass3 single ===")
            run_pass3_single(settings)
        if "multi_algorithm" in tracks:
            LOG.info("=== Pass3 multi ===")
            run_pass3_multi(settings)
        LOG.info("=== Pass3 export ===")
        run_pass3_export(settings)

    if phase in {"merge", "4"}:
        LOG.info("=== Merge multi-source composition ledgers ===")
        merge_composition_ledgers(settings)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="skill_data_factory pipeline")
    parser.add_argument("--phase", default="all", help="all | pass1 | pass2 | pass3 | merge")
    parser.add_argument("--config", default=None, help="Config YAML path relative to skill_data_factory or absolute")
    parser.add_argument("--tracks", default="single,multi", help="single,multi or single_algorithm,multi_algorithm")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit-problems", type=int, default=0)
    parser.add_argument("--budget", type=int, default=0, help="Max LLM labeling calls per track; 0=unlimited")
    parser.add_argument(
        "--verified-source",
        default=None,
        choices=["local", "taco-verified", "codecontests-local"],
        help="Pass1 source/verification strategy (default from selected config YAML)",
    )
    parser.add_argument(
        "--retry-quarantine",
        action="store_true",
        help="Pass2 resume: re-attempt solutions that only appear in quarantine.jsonl",
    )
    args = parser.parse_args(argv)

    track_map = {
        "single": "single_algorithm",
        "multi": "multi_algorithm",
        "single_algorithm": "single_algorithm",
        "multi_algorithm": "multi_algorithm",
    }
    tracks = [track_map.get(t.strip(), t.strip()) for t in args.tracks.split(",") if t.strip()]

    run_pipeline(
        phase=args.phase,
        tracks=tracks,
        resume=args.resume,
        limit_problems=args.limit_problems,
        budget=args.budget,
        verified_source=args.verified_source,
        retry_quarantine=args.retry_quarantine,
        config_path=args.config,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
