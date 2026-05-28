"""Export pass3 artifacts and write distillation profile report."""
from __future__ import annotations

from pathlib import Path

from sdf.io_utils import load_jsonl, save_json
from sdf.factory_settings import Settings

TRACKS = ("single_algorithm", "multi_algorithm")


def _md_profile(settings: Settings) -> str:
    lines = ["# Skill distillation profile\n"]
    for track in TRACKS:
        p2_sum = settings.pass2_dir(track) / "primary_summary.json"
        p3_sum = settings.pass3_dir(track) / "pass3_summary.json"
        lines.append(f"## {track}\n")
        if p2_sum.exists():
            import json
            data = json.loads(p2_sum.read_text(encoding="utf-8"))
            lines.append(f"- primary_count: {data.get('primary_count')}")
            lines.append(f"- tier_counts: {data.get('tier_counts')}")
            lines.append(f"- keys: {data.get('subtype_or_key_counts')}\n")
        if p3_sum.exists():
            import json
            data = json.loads(p3_sum.read_text(encoding="utf-8"))
            lines.append(f"- pass3: {data}\n")
        dist = settings.pass3_dir(track)
        if track == "single_algorithm":
            rows = load_jsonl(dist / "distillation_rows.jsonl")
            packets = load_jsonl(dist / "evidence_packets.jsonl")
        else:
            rows = load_jsonl(dist / "composition_rows.jsonl")
            packets = load_jsonl(dist / "composition_evidence_packets.jsonl")
        lines.append(f"- distillation_rows: {len(rows)}")
        lines.append(f"- evidence_packets: {len(packets)}\n")

    shared = settings.output_dir / "pass1_manifest"
    route = shared / "route_summary.json"
    if route.exists():
        import json
        lines.append("## Pass1 route\n")
        lines.append(f"```json\n{route.read_text(encoding='utf-8')}\n```\n")
    return "\n".join(lines)


def run_pass3_export(settings: Settings) -> Path:
    report_path = settings.reports_dir / "distillation_profile.md"
    settings.reports_dir.mkdir(parents=True, exist_ok=True)
    report_path.write_text(_md_profile(settings), encoding="utf-8")
    manifest = {
        "single_root": str(settings.pass3_dir("single_algorithm")),
        "multi_root": str(settings.pass3_dir("multi_algorithm")),
        "single_distillation": str(settings.pass3_dir("single_algorithm") / "distillation_rows.jsonl"),
        "multi_composition": str(settings.pass3_dir("multi_algorithm") / "composition_rows.jsonl"),
    }
    save_json(settings.output_dir / "export_manifest.json", manifest)
    return report_path
