"""Stage A — build a 240-problem universe directly from raw TACO.

Source of truth:  Hugging Face dataset `BAAI/TACO`, split = `train`.
NOT the parent project's already-imported `datasets/` tree.

For every record we:
  1. Parse TACO fields (`question`, `solutions`, `input_output`, `skill_types`,
     `tags`, `difficulty`, `source`) robustly (TACO stores lists as JSON strings).
  2. Map `skill_types ∪ tags` to the 8 core families via `taxonomy.tags_to_core_families`.
  3. Bucket the record under every core family it touches, preserving the dataset index.
  4. For each family take the first `top_n_per_family` records (deterministic — the
     original dataset ordering) as the baseline slice.
  5. Deduplicate across buckets into a single "selected" universe.
  6. If deduplication leaves us below the desired unique-universe size
     (`top_n_per_family * number_of_families`), keep scanning later records in a
     round-robin family order and backfill with unseen problems until the unique
     target is reached or no unseen candidates remain.
  7. Emit `selected_problems_single.jsonl` + `selected_problems_multi.jsonl` +
     `taco_tests.jsonl` + `dataset_profile.md`.

The JSONL records are self-contained: each carries problem text, reference solutions
and the test cases so downstream stages do not need to re-open TACO.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

# TACO has competitive-programming problems whose test-case inputs/outputs
# contain integers with >4300 decimal digits. Python 3.11+ limits
# int<->str conversions to 4300 digits by default (PEP 0006 / CVE-2020-10735),
# which trips `json.loads` when it tries to build such big ints. We uncap it
# for this stage — the data comes from a trusted local parquet file.
try:
    sys.set_int_max_str_digits(0)  # 0 == unlimited
except AttributeError:  # pragma: no cover — older Python
    pass

from .io_utils import save_json, write_jsonl
from .logging_utils import get_logger
from .settings import Settings
from .taxonomy import CORE_FAMILIES, tags_to_core_families

LOG = get_logger(__name__)


# ---------------------------------------------------------------------------
# TACO parsing helpers
# ---------------------------------------------------------------------------

def _safe_json_loads(value: Any) -> Any:
    """TACO stores many list fields as JSON-encoded strings; be permissive.

    `parse_int=str` keeps arbitrarily-large integer tokens as Python strings
    instead of materialising them as `int`. TACO test-case I/O often contains
    >4 kB integers which (1) blow past the int<->str length cap and (2) would
    be pointless to decode since we feed them back to a subprocess as text.
    """
    if value is None:
        return None
    if isinstance(value, (list, dict)):
        return value
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text:
        return None
    try:
        return json.loads(text, parse_int=str, parse_float=str)
    except json.JSONDecodeError:
        try:
            # TACO occasionally uses python-literal-repr for solutions.
            import ast as _ast
            return _ast.literal_eval(text)
        except Exception:  # pragma: no cover
            return None


def _extract_text_list(raw: Any) -> list[str]:
    parsed = _safe_json_loads(raw)
    if isinstance(parsed, list):
        return [str(x) for x in parsed if isinstance(x, (str, int, float))]
    if isinstance(parsed, str):
        return [parsed]
    return []


def _extract_solutions(raw: Any) -> list[str]:
    parsed = _safe_json_loads(raw)
    if isinstance(parsed, list):
        return [str(x) for x in parsed if isinstance(x, str) and x.strip()]
    if isinstance(parsed, str) and parsed.strip():
        return [parsed]
    return []


def _extract_input_output(raw: Any) -> dict[str, Any] | None:
    parsed = _safe_json_loads(raw)
    if not isinstance(parsed, dict):
        return None
    inputs = parsed.get("inputs")
    outputs = parsed.get("outputs")
    if not isinstance(inputs, list) or not isinstance(outputs, list):
        return None
    cleaned = {
        "inputs": [x if isinstance(x, (str, list)) else str(x) for x in inputs],
        "outputs": [x if isinstance(x, (str, list)) else str(x) for x in outputs],
    }
    fn_name = parsed.get("fn_name")
    if isinstance(fn_name, str) and fn_name.strip():
        cleaned["fn_name"] = fn_name.strip()
    return cleaned


def _canonical_problem_id(dataset_index: int, record: dict[str, Any]) -> str:
    explicit = record.get("id") or record.get("problem_id") or record.get("source_id")
    if isinstance(explicit, (int, str)) and str(explicit).strip():
        slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", str(explicit).strip()).strip("_")
        return f"taco_train_{int(dataset_index):06d}__{slug}"[:80]
    return f"taco_train_{int(dataset_index):06d}"


# ---------------------------------------------------------------------------
# Stage A core
# ---------------------------------------------------------------------------

@dataclass
class StageAStats:
    total_records_scanned: int = 0
    records_with_tests: int = 0
    records_with_solutions: int = 0
    records_with_core_family: int = 0
    per_family_available: dict[str, int] = field(default_factory=dict)
    per_family_selected: dict[str, int] = field(default_factory=dict)
    target_unique: int = 0
    selected_unique: int = 0
    unique_shortfall: int = 0
    single_label_count: int = 0
    multi_label_count: int = 0
    family_shortfall: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_records_scanned": self.total_records_scanned,
            "records_with_tests": self.records_with_tests,
            "records_with_solutions": self.records_with_solutions,
            "records_with_core_family": self.records_with_core_family,
            "per_family_available": self.per_family_available,
            "per_family_selected": self.per_family_selected,
            "target_unique": self.target_unique,
            "selected_unique": self.selected_unique,
            "unique_shortfall": self.unique_shortfall,
            "single_label_count": self.single_label_count,
            "multi_label_count": self.multi_label_count,
            "family_shortfall": self.family_shortfall,
        }


@dataclass
class _TacoRecord:
    index: int
    problem_id: str
    question: str
    solutions: list[str]
    input_output: dict[str, Any] | None
    difficulty: str | None
    source: str | None
    skill_types: list[str]
    raw_tags: list[str]
    core_families: list[str]


def _iterate_taco(hf_name: str, split: str, cache_dir: Path | None):
    """Load TACO.

    `datasets >= 4.0` no longer supports loading scripts, and TACO upstream
    exposes both a `TACO.py` script and native parquet shards under
    `ALL/<split>-*.parquet`. We therefore:

      1. First try `datasets.load_dataset("BAAI/TACO", "ALL", split=...)`
         which prefers the parquet files (fast path on modern `datasets`).
      2. If that fails (old cache pointing at TACO.py, or datasets<2.x),
         fall back to `huggingface_hub.snapshot_download` to fetch the
         `ALL/<split>-*.parquet` shards directly and iterate them via
         pyarrow — completely bypassing the loading-script machinery.
    """
    LOG.info("Loading TACO %s split=%s …", hf_name, split)
    try:
        from datasets import load_dataset
        ds = load_dataset(hf_name, "ALL", split=split)
        LOG.info("Loaded via datasets.load_dataset (parquet path). n=%d", len(ds))
        return ds
    except Exception as exc:
        LOG.warning("datasets.load_dataset failed (%s). Falling back to parquet shards.", exc)
    return _iter_taco_parquet(hf_name, split)


def _iter_taco_parquet(hf_name: str, split: str):
    """Download the parquet shards for one split and iterate rows lazily."""
    try:
        import pyarrow.parquet as pq
        from huggingface_hub import snapshot_download
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "Need pyarrow + huggingface_hub for the TACO parquet fallback: "
            "pip install pyarrow huggingface_hub"
        ) from exc

    pattern = f"ALL/{split}-*.parquet"
    LOG.info("Downloading TACO parquet shards matching %r …", pattern)
    repo_root = snapshot_download(
        repo_id=hf_name,
        repo_type="dataset",
        allow_patterns=[pattern],
    )
    split_dir = Path(repo_root) / "ALL"
    shard_paths = sorted(split_dir.glob(f"{split}-*.parquet"))
    if not shard_paths:
        raise FileNotFoundError(
            f"No parquet shards matched {pattern} in {repo_root}. "
            "Check network access / HF auth."
        )
    LOG.info("Got %d parquet shards under %s", len(shard_paths), split_dir)
    return _ParquetShardIterator(shard_paths)


class _ParquetShardIterator:
    """Minimal iterable that mimics the `datasets.Dataset` row interface.

    Only `__iter__` and `__len__` are actually consumed by `stage_a_filter`,
    so we deliberately keep this thin — no random access, no column slicing.
    """

    def __init__(self, shard_paths: list[Path]) -> None:
        import pyarrow.parquet as pq
        self._shard_paths = shard_paths
        self._pq = pq
        self._total: int | None = None

    def __len__(self) -> int:
        if self._total is None:
            total = 0
            for path in self._shard_paths:
                md = self._pq.read_metadata(str(path))
                total += md.num_rows
            self._total = total
        return self._total

    def __iter__(self):
        for path in self._shard_paths:
            table = self._pq.read_table(str(path))
            for batch in table.to_batches(max_chunksize=256):
                for row in batch.to_pylist():
                    yield row


def _parse_record(dataset_index: int, record: dict[str, Any]) -> _TacoRecord | None:
    question = record.get("question") or record.get("problem") or ""
    if not isinstance(question, str) or not question.strip():
        return None
    solutions = _extract_solutions(record.get("solutions"))
    input_output = _extract_input_output(record.get("input_output"))
    difficulty = record.get("difficulty") if isinstance(record.get("difficulty"), str) else None
    source = record.get("source") if isinstance(record.get("source"), str) else None
    skill_types = _extract_text_list(record.get("skill_types"))
    raw_tags = _extract_text_list(record.get("tags") or record.get("raw_tags"))
    core_families = tags_to_core_families(skill_types + raw_tags)
    if not core_families:
        return None
    return _TacoRecord(
        index=dataset_index,
        problem_id=_canonical_problem_id(dataset_index, record),
        question=question.strip(),
        solutions=solutions,
        input_output=input_output,
        difficulty=difficulty,
        source=source,
        skill_types=skill_types,
        raw_tags=raw_tags,
        core_families=core_families,
    )


def _is_qualifying_record(record: _TacoRecord) -> bool:
    return bool(record.solutions and record.input_output and record.input_output.get("inputs"))


def select_problems(settings: Settings) -> StageAStats:
    """Main entrypoint. Writes the Stage A artefacts and returns the summary stats."""
    cfg = settings.config
    top_n = settings.top_n_per_family
    target_unique = top_n * len(CORE_FAMILIES)
    hf_name = cfg["paths"]["taco_hf_name"]
    hf_split = cfg["paths"]["taco_hf_split"]
    hf_cache = settings.cache_dir / "hf_datasets"
    hf_cache.mkdir(parents=True, exist_ok=True)

    out_dir = settings.stage_dir("stage_a")
    single_path = out_dir / "selected_problems_single.jsonl"
    multi_path = out_dir / "selected_problems_multi.jsonl"
    tests_path = settings.taco_tests_path
    tests_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path = out_dir / "stage_a_stats.json"
    profile_path = settings.reports_dir / "dataset_profile.md"

    stats = StageAStats(
        per_family_available={f: 0 for f in CORE_FAMILIES},
        per_family_selected={f: 0 for f in CORE_FAMILIES},
        target_unique=target_unique,
        family_shortfall={f: 0 for f in CORE_FAMILIES},
    )

    # Pass 1 — stream the dataset, bucket every qualifying record per family.
    dataset = _iterate_taco(hf_name, hf_split, cache_dir=hf_cache)
    per_family_candidates: dict[str, list[_TacoRecord]] = {f: [] for f in CORE_FAMILIES}

    for i, record in enumerate(dataset):
        stats.total_records_scanned += 1
        parsed = _parse_record(i, record)
        if parsed is None:
            continue
        if parsed.solutions:
            stats.records_with_solutions += 1
        if parsed.input_output and parsed.input_output.get("inputs"):
            stats.records_with_tests += 1
        stats.records_with_core_family += 1
        for fam in parsed.core_families:
            stats.per_family_available[fam] = stats.per_family_available.get(fam, 0) + 1
            if _is_qualifying_record(parsed):
                per_family_candidates.setdefault(fam, []).append(parsed)

    # Pass 2 — materialise the baseline selection, then backfill until the
    # deduplicated universe reaches the target size.
    selected: dict[str, _TacoRecord] = {}
    family_to_ids: dict[str, list[str]] = {}
    family_cursors: dict[str, int] = {}
    for fam in CORE_FAMILIES:
        candidates = per_family_candidates.get(fam, [])
        baseline = candidates[:top_n]
        picked_ids = []
        for rec in baseline:
            selected.setdefault(rec.problem_id, rec)
            picked_ids.append(rec.problem_id)
        family_to_ids[fam] = picked_ids
        family_cursors[fam] = len(baseline)

    while len(selected) < target_unique:
        progressed = False
        for fam in CORE_FAMILIES:
            candidates = per_family_candidates.get(fam, [])
            cursor = family_cursors.get(fam, 0)
            while cursor < len(candidates):
                rec = candidates[cursor]
                cursor += 1
                if rec.problem_id in selected:
                    continue
                selected[rec.problem_id] = rec
                family_to_ids[fam].append(rec.problem_id)
                progressed = True
                break
            family_cursors[fam] = cursor
            if len(selected) >= target_unique:
                break
        if not progressed:
            break

    stats.selected_unique = len(selected)
    stats.unique_shortfall = max(0, target_unique - stats.selected_unique)
    for fam in CORE_FAMILIES:
        stats.per_family_selected[fam] = len(family_to_ids.get(fam, []))
        if stats.per_family_selected[fam] < top_n:
            stats.family_shortfall[fam] = top_n - stats.per_family_selected[fam]

    # Pass 3 — write outputs.
    single_rows: list[dict[str, Any]] = []
    multi_rows: list[dict[str, Any]] = []
    test_rows: list[dict[str, Any]] = []

    for pid, rec in selected.items():
        is_multi = len(rec.core_families) >= 2
        primary_family = rec.core_families[0]
        row_common = {
            "problem_id": pid,
            "source_dataset": "TACO",
            "split": "train",
            "source_index": rec.index,
            "source_id_field": rec.problem_id,
            "source": rec.source,
            "difficulty": rec.difficulty,
            "problem_statement": rec.question,
            "reference_solutions": [
                {"solution_id": f"s{idx}", "code": code}
                for idx, code in enumerate(rec.solutions[:5])  # cap at 5 refs
            ],
            "original_skill_types": rec.skill_types,
            "original_tags": rec.raw_tags,
            "candidate_families": rec.core_families,
            "selected_for_families": [
                fam for fam, ids in family_to_ids.items() if pid in ids
            ],
        }

        single_rows.append({
            **row_common,
            "scope": "single",
            "primary_family": primary_family,
        })
        multi_rows.append({
            **row_common,
            "scope": "multi" if is_multi else "single",
            "primary_family": primary_family,
            "is_multi_skill_candidate": is_multi,
        })
        if is_multi:
            stats.multi_label_count += 1
        else:
            stats.single_label_count += 1

        if rec.input_output is not None:
            test_rows.append({
                "problem_id": pid,
                "source_index": rec.index,
                "input_output": rec.input_output,
            })

    write_jsonl(single_path, single_rows)
    write_jsonl(multi_path, multi_rows)
    write_jsonl(tests_path, test_rows)
    save_json(stats_path, stats.to_dict())

    _write_profile(
        path=profile_path,
        stats=stats,
        top_n=top_n,
        single_path=single_path,
        multi_path=multi_path,
        tests_path=tests_path,
    )
    LOG.info(
        "Stage A done: scanned=%d selected_unique=%d/%d single=%d multi=%d",
        stats.total_records_scanned, stats.selected_unique, stats.target_unique,
        stats.single_label_count, stats.multi_label_count,
    )
    return stats


def _write_profile(
    *,
    path: Path,
    stats: StageAStats,
    top_n: int,
    single_path: Path,
    multi_path: Path,
    tests_path: Path,
) -> None:
    lines: list[str] = []
    lines.append("# Dataset Profile — Stage A\n")
    lines.append("## Source\n")
    lines.append("- HuggingFace dataset: `BAAI/TACO`, split `train` (pristine).\n")
    lines.append("- No dependency on the parent project's `datasets/` tree.\n\n")
    lines.append("## Parsed TACO fields\n")
    lines.append(
        "| field | handling |\n"
        "| --- | --- |\n"
        "| `question` | kept verbatim as `problem_statement` |\n"
        "| `solutions` | JSON / python-literal decoded → `reference_solutions[].code`, first 5 kept |\n"
        "| `input_output` | JSON decoded → `{inputs[], outputs[], fn_name?}` (for evaluation) |\n"
        "| `skill_types` + `tags` | normalized and mapped to the 8 core families via `taxonomy` |\n"
        "| `difficulty`, `source` | passed through for stratified reporting |\n\n"
    )
    lines.append("## Selection rule\n")
    lines.append(f"- For every core family, take the **first {top_n}** records (in TACO dataset order) that:\n")
    lines.append("  - have at least one reference solution;\n")
    lines.append("  - have a well-formed `input_output`;\n")
    lines.append("  - map to that core family through `skill_types ∪ tags`.\n")
    lines.append("- Those per-family baseline slices are deduplicated into one universe.\n")
    lines.append(
        f"- If deduplication leaves the universe below **{stats.target_unique}** unique problems, "
        "Stage A keeps scanning later family candidates in round-robin order and backfills with unseen problems until the unique target is reached or candidates are exhausted.\n"
    )
    lines.append("- `selected_problems_single.jsonl` and `selected_problems_multi.jsonl` cover the same problem universe.\n")
    lines.append("- The difference is only the view: the single file keeps one `primary_family` per problem, while the multi file also records multi-skill metadata.\n\n")

    lines.append("## Counts\n")
    lines.append(f"- Scanned records: **{stats.total_records_scanned}**\n")
    lines.append(f"- Records with tests: **{stats.records_with_tests}**\n")
    lines.append(f"- Records with ≥1 solution: **{stats.records_with_solutions}**\n")
    lines.append(f"- Records touching any core family: **{stats.records_with_core_family}**\n")
    lines.append(f"- Unique problems selected: **{stats.selected_unique} / {stats.target_unique}**\n")
    lines.append(f"- Unique-universe shortfall: **{stats.unique_shortfall}**\n")
    lines.append(f"- Single-label rows: **{stats.single_label_count}**\n")
    lines.append(f"- Multi-label rows: **{stats.multi_label_count}**\n\n")

    lines.append("### Per-family availability & selection\n\n")
    lines.append("| family | available in TACO | selected after backfill (baseline target = {0}) | shortfall |\n".format(top_n))
    lines.append("| --- | ---: | ---: | ---: |\n")
    for fam in CORE_FAMILIES:
        lines.append(
            f"| {fam} | {stats.per_family_available.get(fam, 0)} | "
            f"{stats.per_family_selected.get(fam, 0)} | {stats.family_shortfall.get(fam, 0)} |\n"
        )

    lines.append("\n## Output files\n")
    lines.append(f"- `{single_path}` — primary-family view (one row per unique selected problem)\n")
    lines.append(f"- `{multi_path}` — multi-skill metadata view (same universe, records all matching families)\n")
    lines.append(f"- `{tests_path}` — sidecar test-cases for Stage F evaluation\n")

    if any(v > 0 for v in stats.family_shortfall.values()):
        lines.append("\n## Caveats\n")
        short = ", ".join(f"{k}({v} short)" for k, v in stats.family_shortfall.items() if v > 0)
        lines.append(
            f"- The following families had fewer than {top_n} qualifying records in TACO train: {short}.\n"
            "  Downstream stages still run on the actually-selected subset — this is noted in the final report.\n"
        )
    if stats.unique_shortfall > 0:
        lines.append("\n## Caveats\n" if not any(v > 0 for v in stats.family_shortfall.values()) else "")
        lines.append(
            f"- Even after backfilling, Stage A could only find {stats.selected_unique} unique qualifying problems "
            f"for a target of {stats.target_unique}.\n"
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(lines), encoding="utf-8")


def load_selected(settings: Settings, *, scope: str = "single") -> list[dict[str, Any]]:
    """Helper for downstream stages."""
    path = settings.stage_dir("stage_a") / f"selected_problems_{scope}.jsonl"
    if not path.exists():
        raise FileNotFoundError(f"Stage A output missing: {path}. Run scripts/run_stage_a.py first.")
    from .io_utils import load_jsonl
    return load_jsonl(path)


def load_problem_skills(settings: Settings) -> dict[str, list[str]]:
    """Convenience: problem_id -> candidate core families (from Stage A)."""
    rows = load_selected(settings, scope="multi")
    return {r["problem_id"]: list(r.get("candidate_families") or []) for r in rows}
