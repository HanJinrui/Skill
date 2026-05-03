"""Stage D — synthesize the algorithm-skill knowledge base.

We build one skill per canonical skill-id:

  * Single-skill ids: each of the 8 core families (when at least one
    "consistent" example exists with exactly that family set).
  * Multi-skill ids: any observed frozenset of ≥2 core families that has
    ≥ `min_multi_examples` consistent solutions.

For every skill-id we pack up to `max_examples_per_skill` consistent
(problem, solution) pairs and ask GLM to produce a transferable skill card
that conforms to `prompts/skill_generation.yaml`. The returned JSON is
post-processed (skill_id pinned, families sanitized) and written to
`skills_single.jsonl` / `skills_multi.jsonl` / `skills_merged.jsonl`.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import re
import time
from typing import Any, Iterable

import yaml

from .cache import DiskCache
from .io_utils import append_jsonl, load_jsonl, read_jsonl, save_json, write_jsonl
from .llm.base import ChatLLM, LLMError
from .logging_utils import get_logger
from .settings import Settings
from .stage_a_filter import load_selected
from .stage_c_solution_label import load_consistent
from .subtype_taxonomy import all_subtypes, get_subtype
from .taxonomy import CORE_FAMILY_SET, skill_id_for_multi, skill_id_for_single

LOG = get_logger(__name__)

MIN_SINGLE_EXAMPLES = 3
MIN_MULTI_EXAMPLES = 2
MAX_EXAMPLES_PER_SKILL = 6
MAX_STATEMENT_CHARS = 900
MAX_CODE_CHARS = 1000
STAGE_D_V2_VERSION = "stage_d_v2@v1"
V2_MAX_EXAMPLES_PER_SKILL = 5
V2_MAX_STATEMENT_CHARS = 700
V2_MAX_CODE_CHARS = 900

_STOPWORDS = {
    "the", "and", "for", "with", "that", "from", "this", "into", "when", "then",
    "using", "maintains", "maintain", "current", "window", "array", "string", "code",
    "solution", "algorithm", "problem", "through", "there", "their", "where", "which",
    "while", "move", "moves", "left", "right", "find", "minimum", "maximum", "valid",
    "track", "tracking", "count", "counts", "each", "over", "after", "before", "once",
    "pointer", "pointers", "value", "values", "result", "results",
}

_FAMILY_HINTS: dict[str, dict[str, Any]] = {
    "amortized_analysis": {
        "applicable_when": [
            "The problem asks for linear or near-linear scanning over a sequence.",
            "A valid answer can be maintained by expanding and shrinking a moving frontier.",
            "Each element should enter and leave an active structure only a constant number of times.",
        ],
        "problem_signals": [
            "subarray or substring constraints",
            "two pointers or sliding interval behavior",
            "need to maintain a valid window while scanning",
            "linear-time target despite nested-looking logic",
        ],
        "template_strategy": [
            "Identify the invariant that makes the current window or frontier valid.",
            "Advance the right boundary to include new information.",
            "While the invariant is violated or already satisfied too strongly, move the left boundary to restore the desired state.",
            "Update the answer after each valid state transition.",
        ],
        "common_pitfalls": [
            "Forgetting to remove stale elements when the left boundary moves.",
            "Breaking the window invariant before recording the answer.",
            "Using an O(n) cleanup inside each step and losing the amortized bound.",
        ],
        "complexity_pattern": "Typically O(n) or O(n log n) with each index updated only a constant number of times.",
        "related_skills": ["data_structures", "range_queries"],
    },
    "bit_manipulation": {
        "applicable_when": [
            "State or transitions are naturally described by binary choices or masks.",
            "The task depends on checking, setting, or combining flags efficiently.",
            "Constraints make compact integer-state representation attractive.",
        ],
        "problem_signals": [
            "mask or subset reasoning",
            "binary representation matters",
            "xor, and, or, shifts, parity",
            "small-state encoding inside integers",
        ],
        "template_strategy": [
            "Choose a bit-level encoding for the relevant state.",
            "Use shifts and masks to extract or update the needed components.",
            "Iterate over bits or subsets in the order implied by the transition.",
            "Convert the final bit-encoded state back into the required answer.",
        ],
        "common_pitfalls": [
            "Mixing 0-based and 1-based bit positions.",
            "Overflowing intermediate masks or forgetting to cast consistently.",
            "Using bit tricks where a clearer invariant is still required.",
        ],
        "complexity_pattern": "Often O(n * word_size), O(2^k * poly(k)), or O(log V) per bitwise transition.",
        "related_skills": ["complete_search", "dynamic_programming"],
    },
    "complete_search": {
        "applicable_when": [
            "The search space is small enough to enumerate directly or with pruning.",
            "The answer can be validated incrementally during exploration.",
            "There is a natural branching process over states, choices, or placements.",
        ],
        "problem_signals": [
            "small constraints such as n <= 20 or manageable branching depth",
            "explicit enumeration of subsets, permutations, or assignments",
            "backtracking with feasibility checks",
            "need to try all valid constructions",
        ],
        "template_strategy": [
            "Define the search state and the next decision to branch on.",
            "Apply pruning rules as early as possible.",
            "Enumerate all remaining valid transitions recursively or iteratively.",
            "Record the best feasible answer or all accepted constructions.",
        ],
        "common_pitfalls": [
            "Failing to prune symmetric or impossible branches early.",
            "Mutating shared state without proper rollback.",
            "Assuming exhaustive search is viable when the true branching factor is too large.",
        ],
        "complexity_pattern": "Usually exponential or factorial in the worst case, improved by pruning and ordering heuristics.",
        "related_skills": ["dynamic_programming", "bit_manipulation"],
    },
    "data_structures": {
        "applicable_when": [
            "The task repeatedly updates and queries a dynamic set of values.",
            "You need fast access to the current minimum, maximum, order, or frequency information.",
            "The core difficulty is maintaining state efficiently across operations.",
        ],
        "problem_signals": [
            "online updates and queries",
            "need to keep ordered or aggregated information",
            "heap, deque, stack, queue, hash map, union-find, or balanced structure patterns",
            "stale elements must be inserted and removed carefully",
        ],
        "template_strategy": [
            "Choose the structure whose supported operations match the problem's update/query pattern.",
            "Define exactly what each stored item represents.",
            "Maintain the structure after every operation, removing stale entries when necessary.",
            "Read the answer directly from the maintained state.",
        ],
        "common_pitfalls": [
            "Using the right structure with the wrong invariant.",
            "Leaving stale entries inside heaps or deques without cleanup.",
            "Paying O(n) rebuilding cost after each update.",
        ],
        "complexity_pattern": "Usually O(log n) or amortized O(1) per update/query depending on the maintained structure.",
        "related_skills": ["range_queries", "amortized_analysis"],
    },
    "dynamic_programming": {
        "applicable_when": [
            "The problem decomposes into overlapping subproblems with reusable state.",
            "A state transition can be written from smaller or simpler states.",
            "Optimal value, count, or feasibility depends on previous choices.",
        ],
        "problem_signals": [
            "minimize, maximize, count ways, or feasibility over prefixes or states",
            "small dimensions or compressible state space",
            "transition from previous index, mask, or resource usage",
            "recurrence naturally appears from the problem structure",
        ],
        "template_strategy": [
            "Define the DP state so it captures exactly the information needed for future transitions.",
            "Initialize base states carefully.",
            "Write the transition and iterate in an order that respects dependencies.",
            "Extract the final answer from the terminal states.",
        ],
        "common_pitfalls": [
            "Defining an incomplete state that cannot support correct transitions.",
            "Updating in the wrong order and reusing overwritten values.",
            "Ignoring memory compression opportunities when only the previous layer is needed.",
        ],
        "complexity_pattern": "Often O(number_of_states * transitions_per_state), with memory optimization possible when dependencies are local.",
        "related_skills": ["complete_search", "bit_manipulation"],
    },
    "greedy_algorithms": {
        "applicable_when": [
            "A locally optimal choice can be justified to extend to a global optimum.",
            "Ordering or exchange arguments explain why one decision is always safe.",
            "The structure of the answer can be built incrementally without revisiting earlier choices.",
        ],
        "problem_signals": [
            "sort then choose or pair elements",
            "need a canonical local choice",
            "exchange argument or monotone preference",
            "construct an optimal answer step by step",
        ],
        "template_strategy": [
            "Identify the safe local decision and the invariant it preserves.",
            "Sort or prioritize items if the greedy rule depends on order.",
            "Apply the decision repeatedly while maintaining feasibility.",
            "Prove correctness with an exchange or stay-ahead argument.",
        ],
        "common_pitfalls": [
            "Assuming a greedy rule works without a proof invariant.",
            "Choosing the right ordering but updating the maintained state incorrectly.",
            "Overlooking counterexamples where local choices block future feasibility.",
        ],
        "complexity_pattern": "Frequently O(n log n) after sorting, or O(n) with a direct greedy scan.",
        "related_skills": ["sorting", "amortized_analysis"],
    },
    "range_queries": {
        "applicable_when": [
            "The task involves repeated interval queries, prefix aggregates, or point/range updates.",
            "Preprocessing can make many queries significantly faster.",
            "The answer depends on combining values over contiguous ranges.",
        ],
        "problem_signals": [
            "many queries over intervals",
            "prefix sum, fenwick tree, segment tree, difference array",
            "point update plus range query or range update plus point query",
            "offline or online interval aggregation",
        ],
        "template_strategy": [
            "Choose the aggregation operation and determine whether it is associative or prefix-friendly.",
            "Build the preprocessing structure that matches the update/query pattern.",
            "Translate each query or update into structure operations.",
            "Return answers from the maintained aggregates.",
        ],
        "common_pitfalls": [
            "Using an interval structure when simple prefix preprocessing is enough.",
            "Mixing inclusive and exclusive boundaries.",
            "Forgetting lazy propagation or difference reconstruction details when updates are ranged.",
        ],
        "complexity_pattern": "Commonly O(1) per query after prefix preprocessing or O(log n) per operation with trees/Fenwick structures.",
        "related_skills": ["data_structures", "amortized_analysis"],
    },
    "sorting": {
        "applicable_when": [
            "Reordering items reveals structure that is hidden in the raw input order.",
            "The solution depends on processing elements by value, key, or dominance order.",
            "Once ordered, the remaining step becomes greedy, scanning, or simple aggregation.",
        ],
        "problem_signals": [
            "sort by one or more keys",
            "pairing or grouping after ordering",
            "coordinate compression or ranking",
            "offline processing in sorted order",
        ],
        "template_strategy": [
            "Choose the ordering key that exposes the needed structure.",
            "Sort the items and inspect how adjacent or monotone relationships simplify the task.",
            "Run the post-sort logic such as greedy pairing, scanning, or aggregation.",
            "Map the result back to the original format if needed.",
        ],
        "common_pitfalls": [
            "Sorting by the wrong key or forgetting tie-breaking rules.",
            "Assuming sorting alone solves the problem without the second phase.",
            "Losing original indices when the output needs them later.",
        ],
        "complexity_pattern": "Usually O(n log n) dominated by sorting, followed by a linear or logarithmic post-processing pass.",
        "related_skills": ["greedy_algorithms", "data_structures"],
    },
}


def _load_prompt(settings: Settings) -> dict[str, Any]:
    with open(settings.prompts_dir / "skill_generation.yaml", "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _group_consistent(rows: Iterable[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group consistent/partial rows by their detected skill-id."""
    by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        detected = [s for s in (row.get("detected_multi_skills") or []) if s in CORE_FAMILY_SET]
        if not detected:
            continue
        if len(detected) == 1:
            sid = skill_id_for_single(detected[0])
            by_id[sid].append({**row, "_scope": "single", "_families": detected})
        else:
            sid = skill_id_for_multi(detected)
            by_id[sid].append({**row, "_scope": "multi", "_families": sorted(set(detected))})
    return by_id


def _render_examples(
    rows: list[dict[str, Any]],
    problems_by_id: dict[str, dict[str, Any]],
    max_items: int,
) -> str:
    blocks: list[str] = []
    for row in rows[:max_items]:
        prob = problems_by_id.get(row["problem_id"], {})
        statement = (prob.get("problem_statement") or "")[:MAX_STATEMENT_CHARS]
        code = (row.get("solution_code") or "")[:MAX_CODE_CHARS]
        summary = row.get("core_mechanism_summary") or ""
        blocks.append(
            f"--- problem_id: {row['problem_id']}\n"
            f"    difficulty: {prob.get('difficulty')}\n"
            f"    solution_mechanism: {summary}\n"
            f"    problem_excerpt: |\n      {statement}\n"
            f"    solution_excerpt: |\n      ```python\n      {code}\n      ```\n"
        )
    return "\n".join(blocks)


def _unique_keep_order(items: Iterable[str], *, limit: int | None = None) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        text = str(item or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
        if limit is not None and len(out) >= limit:
            break
    return out


def _extract_keywords(examples: list[dict[str, Any]], problems_by_id: dict[str, dict[str, Any]], *, limit: int = 8) -> list[str]:
    text_parts: list[str] = []
    for row in examples[:MAX_EXAMPLES_PER_SKILL]:
        text_parts.append(row.get("core_mechanism_summary") or "")
        prob = problems_by_id.get(row["problem_id"], {})
        text_parts.append((prob.get("problem_statement") or "")[:500])
    counts: dict[str, int] = {}
    for token in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", " ".join(text_parts).lower()):
        if token in _STOPWORDS:
            continue
        counts[token] = counts.get(token, 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [token.replace("_", " ") for token, _ in ranked[:limit]]


def _family_hint(family: str) -> dict[str, Any]:
    return _FAMILY_HINTS.get(family, {})


def _build_fallback_payload(
    *,
    skill_id: str,
    families: list[str],
    scope: str,
    examples: list[dict[str, Any]],
    problems_by_id: dict[str, dict[str, Any]],
    error_message: str,
) -> dict[str, Any]:
    keywords = _extract_keywords(examples, problems_by_id, limit=8)
    family_templates = [_family_hint(f) for f in families]

    applicable_when: list[str] = []
    problem_signals: list[str] = []
    template_strategy: list[str] = []
    common_pitfalls: list[str] = []
    related_skills: list[str] = []
    complexity_bits: list[str] = []
    for tpl in family_templates:
        applicable_when.extend(tpl.get("applicable_when") or [])
        problem_signals.extend(tpl.get("problem_signals") or [])
        template_strategy.extend(tpl.get("template_strategy") or [])
        common_pitfalls.extend(tpl.get("common_pitfalls") or [])
        related_skills.extend(tpl.get("related_skills") or [])
        if tpl.get("complexity_pattern"):
            complexity_bits.append(str(tpl["complexity_pattern"]))

    if keywords:
        problem_signals.extend([f"observed keyword: {kw}" for kw in keywords[:4]])

    family_phrase = ", ".join(f.replace("_", " ") for f in families)
    if scope == "single":
        core_idea = (
            f"This fallback skill card summarizes the recurring {family_phrase} mechanism observed in the "
            f"consistent Stage C solutions. It captures reusable cues, implementation steps, and retrieval terms "
            f"even though GLM was unavailable during Stage D."
        )
    else:
        core_idea = (
            f"This fallback skill card captures a multi-skill pattern combining {family_phrase}. "
            f"The retrieved examples indicate that these families need to be coordinated rather than applied in isolation."
        )

    retrieval_parts = [
        f"Skill {skill_id.replace('__', ' + ').replace('_', ' ')}.",
        f"Families: {family_phrase}.",
    ]
    if keywords:
        retrieval_parts.append("Observed mechanism keywords: " + ", ".join(keywords[:6]) + ".")
    retrieval_parts.append(core_idea)
    retrieval_text = " ".join(retrieval_parts)

    return {
        "skill_id": skill_id,
        "skill_name": skill_id.replace("__", " + ").replace("_", " ").title(),
        "scope": scope,
        "families": families,
        "applicable_when": _unique_keep_order(applicable_when, limit=6),
        "problem_signals": _unique_keep_order(problem_signals, limit=8),
        "core_idea": core_idea,
        "template_strategy": _unique_keep_order(template_strategy, limit=8),
        "common_pitfalls": _unique_keep_order(common_pitfalls, limit=6),
        "complexity_pattern": " / ".join(_unique_keep_order(complexity_bits, limit=2)),
        "representative_examples": [
            {
                "problem_id": e["problem_id"],
                "reason": (e.get("core_mechanism_summary") or "Representative consistent example.")[:200],
            }
            for e in examples[:MAX_EXAMPLES_PER_SKILL]
        ],
        "related_skills": _unique_keep_order(
            [r for r in related_skills if r not in families],
            limit=6,
        ),
        "retrieval_text": retrieval_text[:900],
        "generation_source": "heuristic_fallback",
        "generation_note": error_message[:300],
    }


def _is_rate_limited_error(exc: LLMError) -> bool:
    msg = str(exc).lower()
    return "rate-limited" in msg or "too many requests" in msg or "达到速率限制" in msg or "code': '1302" in msg


def _load_existing_skill_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    out: set[str] = set()
    for row in load_jsonl(path):
        skill_id = row.get("skill_id")
        if isinstance(skill_id, str) and skill_id:
            out.add(skill_id)
    return out


def run_stage_d(settings: Settings, glm: ChatLLM) -> dict[str, Path]:
    prompt_cfg = _load_prompt(settings)
    prompt_version = prompt_cfg["version"]
    recommended = prompt_cfg.get("recommended_params", {}) or {}
    temperature = float(recommended.get("temperature", settings.glm.temperature))
    max_tokens = int(recommended.get("max_tokens", 3000))

    problems_by_id = {r["problem_id"]: r for r in load_selected(settings, scope="multi")}
    consistent_rows = load_consistent(settings)
    if not consistent_rows:
        raise RuntimeError("No consistent Stage C rows. Run Stages B/C first.")

    # Stage C may also include 'partial' — we prefer strict 'consistent' when available
    strict = [r for r in consistent_rows if r.get("consistency_type") == "consistent"]
    pool = strict if strict else consistent_rows
    grouped = _group_consistent(pool)
    stage_d_cfg = settings.config.get("stage_d", {}) if isinstance(settings.config, dict) else {}
    allow_heuristic_fallback = bool(stage_d_cfg.get("allow_heuristic_fallback", False))
    eligible_items: list[tuple[str, list[dict[str, Any]]]] = []
    for skill_id, examples in grouped.items():
        scope = examples[0]["_scope"]
        threshold = MIN_SINGLE_EXAMPLES if scope == "single" else MIN_MULTI_EXAMPLES
        if len(examples) >= threshold:
            eligible_items.append((skill_id, examples))
    LOG.info(
        "Stage D: %d grouped skill ids, %d eligible for synthesis (heuristic_fallback=%s)",
        len(grouped),
        len(eligible_items),
        allow_heuristic_fallback,
    )

    cache = DiskCache(settings.cache_dir / "glm" / "skill_generation")
    out_dir = settings.stage_dir("stage_d")
    single_path = out_dir / "skills_single.jsonl"
    multi_path = out_dir / "skills_multi.jsonl"
    merged_path = out_dir / "skills_merged.jsonl"

    if not single_path.exists():
        write_jsonl(single_path, [])
    if not multi_path.exists():
        write_jsonl(multi_path, [])
    if not merged_path.exists():
        write_jsonl(merged_path, [])

    persisted_single_ids = _load_existing_skill_ids(single_path)
    persisted_multi_ids = _load_existing_skill_ids(multi_path)
    persisted_merged_ids = _load_existing_skill_ids(merged_path)
    LOG.info(
        "Stage D resume state: single=%d multi=%d merged=%d",
        len(persisted_single_ids),
        len(persisted_multi_ids),
        len(persisted_merged_ids),
    )

    llm_rate_limited = False
    total_eligible = len(eligible_items)
    for progress_idx, (skill_id, examples) in enumerate(eligible_items, start=1):
        scope = examples[0]["_scope"]
        families = examples[0]["_families"]
        threshold = MIN_SINGLE_EXAMPLES if scope == "single" else MIN_MULTI_EXAMPLES
        if len(examples) < threshold:
            LOG.info("Skip skill_id=%s (only %d examples < %d)", skill_id, len(examples), threshold)
            continue

        LOG.info(
            "[%d/%d] Synthesizing skill_id=%s scope=%s examples=%d",
            progress_idx,
            total_eligible,
            skill_id,
            scope,
            len(examples),
        )
        if scope == "single" and skill_id in persisted_single_ids and skill_id in persisted_merged_ids:
            LOG.info("[%d/%d] Resume skip for skill_id=%s; already persisted", progress_idx, total_eligible, skill_id)
            continue
        if scope == "multi" and skill_id in persisted_multi_ids and skill_id in persisted_merged_ids:
            LOG.info("[%d/%d] Resume skip for skill_id=%s; already persisted", progress_idx, total_eligible, skill_id)
            continue
        cache_key = DiskCache.make_key({
            "v": prompt_version,
            "provider": getattr(glm, "provider", "unknown"),
            "model": getattr(glm, "model", "unknown"),
            "skill_id": skill_id,
            "problem_ids": sorted({e["problem_id"] for e in examples})[:MAX_EXAMPLES_PER_SKILL],
        })
        cached = cache.get("skill_generation", cache_key)
        if cached is not None:
            cached_payload = cached.get("payload") or {}
            cached_source = str(cached_payload.get("generation_source") or "glm")
            if cached_source == "heuristic_fallback" and not allow_heuristic_fallback:
                LOG.info("Ignore cached heuristic fallback for skill_id=%s and retry GLM", skill_id)
                cached = None
        if cached is not None:
            LOG.info("Use cached Stage D payload for skill_id=%s", skill_id)
            payload = cached.get("payload") or {}
        else:
            if allow_heuristic_fallback and llm_rate_limited:
                payload = _build_fallback_payload(
                    skill_id=skill_id,
                    families=families,
                    scope=scope,
                    examples=examples[:MAX_EXAMPLES_PER_SKILL],
                    problems_by_id=problems_by_id,
                    error_message="Skipped GLM call because the provider had already rate-limited this Stage D run.",
                )
                LOG.warning(
                    "[%d/%d] Use heuristic fallback for skill_id=%s because GLM is currently rate-limited",
                    progress_idx,
                    total_eligible,
                    skill_id,
                )
            else:
                examples_block = _render_examples(examples, problems_by_id, MAX_EXAMPLES_PER_SKILL)
                user = prompt_cfg["user_template"].format(
                    scope=scope,
                    families=families,
                    skill_id=skill_id,
                    examples_block=examples_block,
                )
                try:
                    payload = glm.chat_json(
                        system=prompt_cfg["system"],
                        user=user,
                        temperature=temperature,
                        max_tokens=max_tokens,
                    )
                except LLMError as exc:
                    if _is_rate_limited_error(exc):
                        llm_rate_limited = True
                    LOG.error("[%d/%d] GLM failed synthesizing skill %s: %s", progress_idx, total_eligible, skill_id, exc)
                    if not allow_heuristic_fallback:
                        continue
                    payload = _build_fallback_payload(
                        skill_id=skill_id,
                        families=families,
                        scope=scope,
                        examples=examples[:MAX_EXAMPLES_PER_SKILL],
                        problems_by_id=problems_by_id,
                        error_message=str(exc),
                    )
                    LOG.warning(
                        "[%d/%d] Falling back to heuristic Stage D synthesis for skill_id=%s",
                        progress_idx,
                        total_eligible,
                        skill_id,
                    )
            cache.set("skill_generation", cache_key, {"payload": payload})

        skill_record = _normalize_skill_record(
            payload=payload,
            skill_id=skill_id,
            families=families,
            scope=scope,
            examples=examples[:MAX_EXAMPLES_PER_SKILL],
            generation_provider=getattr(glm, "provider", "unknown"),
            generation_model=getattr(glm, "model", "unknown"),
        )
        if scope == "single" and skill_id not in persisted_single_ids:
            append_jsonl(single_path, skill_record)
            persisted_single_ids.add(skill_id)
        if scope == "multi" and skill_id not in persisted_multi_ids:
            append_jsonl(multi_path, skill_record)
            persisted_multi_ids.add(skill_id)
        if skill_id not in persisted_merged_ids:
            append_jsonl(merged_path, skill_record)
            persisted_merged_ids.add(skill_id)
        LOG.info("[%d/%d] Finished skill_id=%s", progress_idx, total_eligible, skill_id)

    LOG.info(
        "Stage D done — single=%d multi=%d",
        len(persisted_single_ids),
        len(persisted_multi_ids),
    )
    return {"single": single_path, "multi": multi_path, "merged": merged_path}


def _normalize_skill_record(
    *,
    payload: dict[str, Any],
    skill_id: str,
    families: list[str],
    scope: str,
    examples: list[dict[str, Any]],
    generation_provider: str,
    generation_model: str,
) -> dict[str, Any]:
    representative = payload.get("representative_examples") or []
    if not representative:
        representative = [
            {"problem_id": e["problem_id"], "reason": e.get("core_mechanism_summary", "")[:200]}
            for e in examples
        ]
    return {
        "skill_id": skill_id,
        "skill_name": payload.get("skill_name") or skill_id.replace("_", " ").title(),
        "scope": scope,
        "families": families,
        "applicable_when": list(payload.get("applicable_when") or []),
        "problem_signals": list(payload.get("problem_signals") or []),
        "core_idea": payload.get("core_idea") or "",
        "template_strategy": list(payload.get("template_strategy") or []),
        "common_pitfalls": list(payload.get("common_pitfalls") or []),
        "complexity_pattern": payload.get("complexity_pattern") or "",
        "representative_examples": representative,
        "related_skills": list(payload.get("related_skills") or []),
        "retrieval_text": payload.get("retrieval_text") or "",
        "num_source_examples": len(examples),
        "generation_source": payload.get("generation_source") or "glm",
        "generation_note": payload.get("generation_note") or "",
        "generation_provider": generation_provider,
        "generation_model": generation_model,
    }


def run_stage_d_v2(
    settings: Settings,
    *,
    writer: str = "rule-only",
    llm: ChatLLM | None = None,
    resume: bool = False,
    log_every: int = 5,
    limit_skills: int = 0,
    examples: int = 5,
    writer_retries: int = 2,
    writer_backoff_seconds: float = 8.0,
    writer_max_tokens: int = 1800,
    writer_examples: int = 2,
    writer_statement_chars: int = 360,
    writer_code_chars: int = 240,
) -> dict[str, Path]:
    """Build hierarchical skills from Stage C verified subtype outputs.

    V2 is evidence-first: deterministic aggregation creates a complete draft,
    and an optional DeepSeek writer rewrites that draft into the same schema.
    """
    writer = writer.strip().lower()
    if writer not in {"rule-only", "deepseek"}:
        raise ValueError("writer must be one of: rule-only, deepseek")
    if writer == "deepseek" and llm is None:
        raise RuntimeError("Stage D v2 writer=deepseek requires a ChatLLM client.")

    out_dir = settings.stage_dir("stage_d_v2")
    subtype_path = out_dir / "subtype_skills.jsonl"
    family_path = out_dir / "family_skills.jsonl"
    router_path = out_dir / "router_skills.jsonl"
    bundle_path = out_dir / "bundles_or_compositions.jsonl"
    merged_path = out_dir / "skills_merged_v2.jsonl"
    evidence_path = out_dir / "skill_evidence_packets.jsonl"
    summary_path = out_dir / "summary.json"

    output_paths = (subtype_path, family_path, router_path, bundle_path, merged_path, evidence_path)
    if not resume:
        for path in output_paths + (summary_path,):
            if path.exists():
                path.unlink()
    for path in output_paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

    primary_rows = _load_stage_c_primary_rows(settings)
    if not primary_rows:
        raise RuntimeError("Stage D v2 requires Stage C primary rows. Run Stage C verified subtype first.")
    router_rows = load_jsonl(settings.stage_dir("stage_c0") / "router_dataset.jsonl")
    multi_rows = load_jsonl(settings.stage_dir("stage_c0") / "multi_skill_composition_dataset.jsonl")

    subtype_drafts = _build_subtype_skill_drafts(primary_rows)
    family_drafts = _build_family_skill_drafts(subtype_drafts, primary_rows)
    router_drafts = _build_router_skill_drafts(router_rows, primary_rows, subtype_drafts)
    bundle_drafts = _build_bundle_skill_drafts(multi_rows, primary_rows)
    drafts_by_level: list[tuple[str, Path, list[dict[str, Any]]]] = [
        ("subtype", subtype_path, subtype_drafts),
        ("family", family_path, family_drafts),
        ("router", router_path, router_drafts),
        ("bundle", bundle_path, bundle_drafts),
    ]

    total_drafts = sum(len(items) for _, _, items in drafts_by_level)
    if limit_skills:
        remaining = int(limit_skills)
        limited: list[tuple[str, Path, list[dict[str, Any]]]] = []
        for level, path, items in drafts_by_level:
            take = max(0, min(remaining, len(items)))
            limited.append((level, path, items[:take]))
            remaining -= take
        drafts_by_level = limited
        total_drafts = sum(len(items) for _, _, items in drafts_by_level)

    persisted = {
        "subtype": _load_existing_skill_ids(subtype_path),
        "family": _load_existing_skill_ids(family_path),
        "router": _load_existing_skill_ids(router_path),
        "bundle": _load_existing_skill_ids(bundle_path),
        "merged": _load_existing_skill_ids(merged_path),
    }
    prompt_cfg = _load_prompt(settings)
    cache = DiskCache(settings.cache_dir / "deepseek" / "skill_generation_v2")
    model = getattr(llm, "model", "rule-only") if llm is not None else "rule-only"
    provider = getattr(llm, "provider", "rule-only") if llm is not None else "rule-only"
    summary: dict[str, Any] = {
        "schema_version": STAGE_D_V2_VERSION,
        "writer": writer,
        "provider": provider,
        "model": model,
        "resume": bool(resume),
        "limit_skills": int(limit_skills or 0),
        "writer_retries": int(writer_retries),
        "writer_backoff_seconds": float(writer_backoff_seconds),
        "writer_max_tokens": int(writer_max_tokens),
        "writer_examples": int(writer_examples),
        "writer_statement_chars": int(writer_statement_chars),
        "writer_code_chars": int(writer_code_chars),
        "source_primary_rows": len(primary_rows),
        "source_router_rows": len(router_rows),
        "source_multi_rows": len(multi_rows),
        "planned_skills": total_drafts,
        "written": {"subtype": 0, "family": 0, "router": 0, "bundle": 0, "merged": 0},
        "skipped_existing": 0,
        "generation_source_counts": {},
        "outputs": {},
        "examples": {"subtype": [], "bundle": []},
    }
    LOG.info(
        "Stage D v2: writer=%s model=%s primary_rows=%d subtype=%d family=%d router=%d bundle=%d resume=%s",
        writer,
        model,
        len(primary_rows),
        len(subtype_drafts),
        len(family_drafts),
        len(router_drafts),
        len(bundle_drafts),
        resume,
    )

    processed = 0
    for level, level_path, drafts in drafts_by_level:
        for draft in drafts:
            skill_id = str(draft.get("skill_id") or "")
            if not skill_id:
                continue
            if skill_id in persisted[level] and skill_id in persisted["merged"]:
                summary["skipped_existing"] += 1
                continue
            evidence_packet = _skill_evidence_packet(draft)
            skill = _write_skill_with_optional_deepseek(
                draft,
                writer=writer,
                llm=llm,
                prompt_cfg=prompt_cfg,
                cache=cache,
                provider=provider,
                model=model,
                writer_retries=writer_retries,
                writer_backoff_seconds=writer_backoff_seconds,
                writer_max_tokens=writer_max_tokens,
                writer_examples=writer_examples,
                writer_statement_chars=writer_statement_chars,
                writer_code_chars=writer_code_chars,
            )
            append_jsonl(level_path, skill)
            append_jsonl(merged_path, _flatten_skill_for_retriever(skill))
            append_jsonl(evidence_path, evidence_packet)
            persisted[level].add(skill_id)
            persisted["merged"].add(skill_id)
            summary["written"][level] += 1
            summary["written"]["merged"] += 1
            _bump(summary["generation_source_counts"], skill.get("generation_source") or "unknown")
            if level == "subtype" and len(summary["examples"]["subtype"]) < examples:
                summary["examples"]["subtype"].append(_skill_brief(skill))
            if level == "bundle" and len(summary["examples"]["bundle"]) < examples:
                summary["examples"]["bundle"].append(_skill_brief(skill))
            processed += 1
            if log_every and processed % log_every == 0:
                LOG.info("Stage D v2 progress: written=%d/%d last=%s", processed, total_drafts, skill_id)

    summary["outputs"] = {
        "subtype_skills": str(subtype_path),
        "family_skills": str(family_path),
        "router_skills": str(router_path),
        "bundles_or_compositions": str(bundle_path),
        "skills_merged_v2": str(merged_path),
        "skill_evidence_packets": str(evidence_path),
    }
    summary["counts"] = {
        "subtype": _count_jsonl(subtype_path),
        "family": _count_jsonl(family_path),
        "router": _count_jsonl(router_path),
        "bundle": _count_jsonl(bundle_path),
        "merged": _count_jsonl(merged_path),
    }
    save_json(summary_path, summary)
    LOG.info("Stage D v2 done: %s", summary["counts"])
    return {
        "subtype": subtype_path,
        "family": family_path,
        "router": router_path,
        "bundle": bundle_path,
        "merged": merged_path,
        "evidence": evidence_path,
        "summary": summary_path,
    }


def _load_stage_c_primary_rows(settings: Settings) -> list[dict[str, Any]]:
    stage_c = settings.stage_dir("stage_c")
    labeled_path = stage_c / "solution_labeled.jsonl"
    if not labeled_path.exists():
        raise FileNotFoundError(f"Stage C labeled output missing: {labeled_path}")
    rows: list[dict[str, Any]] = []
    order: list[str] = []
    by_key: dict[str, dict[str, Any]] = {}
    for row in read_jsonl(labeled_path):
        if not row.get("is_primary_solution"):
            continue
        key = _solution_key(row)
        order.append(key)
        by_key[key] = row
    for overlay_name in ("primary_solutions_deepseek.jsonl", "primary_solutions_merged.jsonl"):
        path = stage_c / overlay_name
        if not path.exists():
            continue
        for row in read_jsonl(path):
            key = _solution_key(row)
            if key in by_key:
                by_key[key] = {**by_key[key], **row}
    for key in order:
        if key in by_key:
            row = by_key[key]
            if row.get("hard_filter_pass", True) is False and row.get("filter_flags"):
                row = dict(row)
                row["stage_d_quality_penalty"] = 0.12
            rows.append(row)
    return rows


def _solution_key(row: dict[str, Any]) -> str:
    return f"{row.get('problem_id')}::{row.get('solution_id')}"


def _build_subtype_skill_drafts(primary_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in primary_rows:
        if row.get("stage_c0_clean_split") != "single_clean":
            continue
        subtype = str(row.get("primary_subtype") or "")
        if subtype:
            grouped[subtype].append(row)

    drafts: list[dict[str, Any]] = []
    for subtype, rows in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        family = _majority([str(r.get("detected_single_skill") or "") for r in rows]) or _family_for_subtype(subtype)
        definition = get_subtype(subtype)
        examples = _rank_examples(rows)[:V2_MAX_EXAMPLES_PER_SKILL]
        trigger_signals = _subtype_trigger_signals(subtype, family, rows)
        draft = _base_skill_record(
            skill_id=f"subtype__{family}__{subtype}",
            skill_level="subtype",
            family=family,
            subtype=subtype,
            skill_name=f"{subtype.replace('_', ' ')}",
            description=(definition.description if definition else f"{subtype} algorithm pattern"),
            trigger_signals=trigger_signals,
            non_triggers=_default_non_triggers(family, subtype=subtype),
            failure_modes=_default_failure_modes(family, subtype=subtype),
            pattern_abstraction=_pattern_abstraction_for(subtype, family, rows),
            transfer_strategy=_transfer_strategy_for(subtype, family),
            representative_examples=_representative_examples(examples),
            related_skills=_related_skills_for(family, subtype=subtype),
            source_rows=rows,
        )
        draft["num_source_examples"] = len(rows)
        draft["taxonomy_definition"] = definition.to_dict() if definition else {}
        drafts.append(draft)
    return drafts


def _build_family_skill_drafts(
    subtype_drafts: list[dict[str, Any]],
    primary_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    subtype_by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    rows_by_family: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for draft in subtype_drafts:
        subtype_by_family[str(draft["family"])].append(draft)
    for row in primary_rows:
        family = str(row.get("detected_single_skill") or "")
        if family in CORE_FAMILY_SET:
            rows_by_family[family].append(row)

    drafts: list[dict[str, Any]] = []
    for family in sorted(CORE_FAMILY_SET):
        subtypes = sorted(subtype_by_family.get(family, []), key=lambda d: -int(d.get("num_source_examples") or 0))
        rows = rows_by_family.get(family, [])
        hint = _family_hint(family)
        examples = _rank_examples(rows)[:V2_MAX_EXAMPLES_PER_SKILL]
        draft = _base_skill_record(
            skill_id=f"family__{family}",
            skill_level="family",
            family=family,
            subtype="",
            skill_name=family.replace("_", " "),
            description=f"family router and execution guide for {family.replace('_', ' ')}",
            trigger_signals=_unique_keep_order((hint.get("problem_signals") or []) + _top_problem_terms(rows), limit=10),
            non_triggers=_default_non_triggers(family),
            failure_modes=_default_failure_modes(family),
            pattern_abstraction={
                "core_recognition": "Select this family when the problem statement asks for the recurring mechanism listed in trigger_signals.",
                "state_templates": [d["subtype"] for d in subtypes[:8]],
                "transition_templates": [s.get("description", "") for s in subtypes[:5]],
                "base_case_rules": ["First decide the subtype before committing to implementation details."],
                "iteration_order_rules": ["Route from problem goal and constraints to family, then to subtype."],
            },
            transfer_strategy={
                "steps": _unique_keep_order((hint.get("template_strategy") or []) + [
                    "Choose the closest subtype from subtype_registry.",
                    "Use representative_examples only as pattern evidence, not as templates to copy verbatim.",
                ], limit=8),
                "subtype_selection_rules": [
                    f"Prefer {s['subtype']} when signals include: {', '.join(s.get('trigger_signals', [])[:3])}."
                    for s in subtypes[:8]
                ],
            },
            representative_examples=_representative_examples(examples),
            related_skills=_unique_keep_order(hint.get("related_skills") or [], limit=6),
            source_rows=rows,
        )
        draft["subtype_registry"] = [
            {
                "subtype": s["subtype"],
                "skill_id": s["skill_id"],
                "num_source_examples": s.get("num_source_examples", 0),
                "trigger_summary": s.get("trigger_signals", [])[:4],
            }
            for s in subtypes
        ]
        drafts.append(draft)
    return drafts


def _build_router_skill_drafts(
    router_rows: list[dict[str, Any]],
    primary_rows: list[dict[str, Any]],
    subtype_drafts: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    family_counts: Counter[str] = Counter()
    tag_counter: Counter[str] = Counter()
    for row in router_rows:
        families = row.get("candidate_families") or []
        for family in families:
            if family in CORE_FAMILY_SET:
                family_counts[family] += 1
        for tag in (row.get("original_skill_types") or []) + (row.get("original_tags") or []):
            tag_counter[str(tag).lower()] += 1
    examples = _rank_examples(primary_rows)[:V2_MAX_EXAMPLES_PER_SKILL]
    supported = [
        {
            "family": family,
            "skill_id": f"family__{family}",
            "observed_router_rows": family_counts.get(family, 0),
            "top_subtypes": [d["subtype"] for d in subtype_drafts if d["family"] == family][:8],
        }
        for family in sorted(CORE_FAMILY_SET)
    ]
    draft = _base_skill_record(
        skill_id="router__algorithm_family",
        skill_level="router",
        family="",
        subtype="",
        skill_name="algorithm family router",
        description="route a problem statement into family and subtype candidates before retrieval",
        trigger_signals=[
            "Use when no subtype has been selected yet.",
            "Read problem goal, constraints, operations, and original weak tags as routing evidence.",
            "Prefer single-family routing only when one family dominates; otherwise preserve multi-family candidates.",
            "Never use this router to decide solution correctness.",
        ],
        non_triggers=[
            "Do not use as a replacement for subtype execution guidance.",
            "Do not collapse clearly multi-skill problems into a pure subtype.",
            "Do not trust original TACO tags without statement and mechanism evidence.",
        ],
        failure_modes=[
            "Overrouting to dynamic programming whenever the statement says maximize or count.",
            "Missing data-structure requirements hidden behind online updates.",
            "Treating a composition problem as a single pure subtype.",
        ],
        pattern_abstraction={
            "core_recognition": "Family routing maps problem-level signals into candidate algorithm families and then hands off to family/subtype skills.",
            "state_templates": ["problem_goal", "constraints", "operations", "input_shape", "weak_tags"],
            "transition_templates": ["candidate_families -> family skills -> subtype skills"],
            "base_case_rules": ["If no strong signal exists, return multiple candidate families instead of forcing one."],
            "iteration_order_rules": ["Route family first, then subtype, then composition bundle when multiple families remain plausible."],
        },
        transfer_strategy={
            "steps": [
                "Extract goal verbs such as count, minimize, query, update, construct, or enumerate.",
                "Extract constraints and input shape to separate exhaustive, dynamic, online, and sorting patterns.",
                "Map weak tags into candidate families but downweight them when statement signals disagree.",
                "If two or more families remain necessary, emit a bundle candidate rather than a pure subtype.",
            ],
            "family_selection_rules": [
                f"{item['family']}: observed in {item['observed_router_rows']} router rows"
                for item in supported
            ],
        },
        representative_examples=_representative_examples(examples),
        related_skills=[f"family__{family}" for family in sorted(CORE_FAMILY_SET)],
        source_rows=primary_rows,
    )
    draft["supported_families"] = supported
    draft["top_original_tags"] = tag_counter.most_common(20)
    return [draft]


def _build_bundle_skill_drafts(
    multi_rows: list[dict[str, Any]],
    primary_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in multi_rows:
        families = tuple(sorted(f for f in (row.get("family_set") or row.get("candidate_families") or []) if f in CORE_FAMILY_SET))
        if len(families) >= 2:
            grouped[families].append(row)

    primary_by_set: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in primary_rows:
        if row.get("stage_c0_clean_split") != "multi_clean":
            continue
        families = tuple(sorted(f for f in (row.get("problem_skills") or row.get("detected_multi_skills") or []) if f in CORE_FAMILY_SET))
        if len(families) >= 2:
            primary_by_set[families].append(row)

    drafts: list[dict[str, Any]] = []
    for families, rows in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        primary_rows_for_set = primary_by_set.get(families, [])
        examples = _representative_examples(_rank_examples(primary_rows_for_set)[:V2_MAX_EXAMPLES_PER_SKILL])
        subtype_counts = Counter(str(r.get("primary_subtype") or "") for r in primary_rows_for_set if r.get("primary_subtype"))
        skill_id = "bundle__" + "__".join(families)
        draft = _base_skill_record(
            skill_id=skill_id,
            skill_level="bundle",
            family=families[0],
            subtype="",
            skill_name=" + ".join(f.replace("_", " ") for f in families),
            description="composition metadata for problems that require coordinated algorithm families",
            trigger_signals=_bundle_trigger_signals(families, rows, primary_rows_for_set),
            non_triggers=[
                "Do not use this bundle when one subtype explains both the statement and solution mechanism.",
                "Do not treat the bundle as a new pure subtype.",
                "Do not combine families unless each has a concrete role in the algorithm.",
            ],
            failure_modes=[
                "Applying only the primary family and ignoring the auxiliary invariant.",
                "Using the right families but in the wrong order.",
                "Retrieving unrelated family cards without a composition plan.",
            ],
            pattern_abstraction={
                "core_recognition": "A bundle captures how multiple families cooperate in one solution.",
                "state_templates": list(families),
                "transition_templates": [
                    f"Use {families[0]} as the primary family and add auxiliary families when their trigger role appears."
                ],
                "base_case_rules": ["First solve the pure-family subproblem before layering the auxiliary structure."],
                "iteration_order_rules": ["Identify primary family, auxiliary family, then data/control flow between them."],
            },
            transfer_strategy={
                "steps": [
                    "Name the role of each family in the bundle.",
                    "Decide which family owns the main state or loop.",
                    "Attach auxiliary families only where they maintain a required invariant.",
                    "Check whether a pure subtype skill would be sufficient before using the bundle.",
                ],
                "component_families": list(families),
            },
            representative_examples=examples,
            related_skills=[f"family__{family}" for family in families],
            source_rows=primary_rows_for_set or rows,
        )
        draft["families"] = list(families)
        draft["family_set"] = list(families)
        draft["component_families"] = list(families)
        draft["observed_multi_rows"] = len(rows)
        draft["observed_primary_rows"] = len(primary_rows_for_set)
        draft["observed_primary_subtypes"] = [
            {"subtype": subtype, "count": count}
            for subtype, count in subtype_counts.most_common(12)
        ]
        drafts.append(draft)
    return drafts


def _base_skill_record(
    *,
    skill_id: str,
    skill_level: str,
    family: str,
    subtype: str,
    skill_name: str,
    description: str,
    trigger_signals: list[str],
    non_triggers: list[str],
    failure_modes: list[str],
    pattern_abstraction: dict[str, Any],
    transfer_strategy: dict[str, Any],
    representative_examples: list[dict[str, Any]],
    related_skills: list[str],
    source_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    retrieval_text = _build_retrieval_text(
        skill_id=skill_id,
        skill_level=skill_level,
        family=family,
        subtype=subtype,
        description=description,
        trigger_signals=trigger_signals,
        transfer_strategy=transfer_strategy,
    )
    return {
        "schema_version": STAGE_D_V2_VERSION,
        "skill_id": skill_id,
        "skill_level": skill_level,
        "skill_name": skill_name,
        "description": description,
        "family": family,
        "families": [family] if family else [],
        "subtype": subtype,
        "trigger_signals": _unique_keep_order(trigger_signals, limit=10),
        "non_triggers": _unique_keep_order(non_triggers, limit=8),
        "failure_modes": _unique_keep_order(failure_modes, limit=8),
        "pattern_abstraction": pattern_abstraction,
        "transfer_strategy": transfer_strategy,
        "representative_examples": representative_examples,
        "related_skills": _unique_keep_order(related_skills, limit=12),
        "retrieval_text": retrieval_text,
        "num_source_examples": len(source_rows),
        "source_problem_ids": _unique_keep_order([str(r.get("problem_id")) for r in source_rows], limit=50),
        "generation_source": "rule_fallback",
        "generation_model": "deterministic",
    }


def _write_skill_with_optional_deepseek(
    draft: dict[str, Any],
    *,
    writer: str,
    llm: ChatLLM | None,
    prompt_cfg: dict[str, Any],
    cache: DiskCache,
    provider: str,
    model: str,
    writer_retries: int,
    writer_backoff_seconds: float,
    writer_max_tokens: int,
    writer_examples: int,
    writer_statement_chars: int,
    writer_code_chars: int,
) -> dict[str, Any]:
    if writer != "deepseek" or llm is None:
        return {**draft, "generation_source": "rule_fallback", "generation_model": "deterministic"}
    prompt_version = str(prompt_cfg.get("hierarchical_version") or "skill_generation_hierarchy@v2")
    cache_key = DiskCache.make_key({
        "v": prompt_version,
        "skill_id": draft.get("skill_id"),
        "writer": writer,
        "model": model,
        "writer_max_tokens": writer_max_tokens,
        "writer_examples": writer_examples,
        "writer_statement_chars": writer_statement_chars,
        "writer_code_chars": writer_code_chars,
        "draft": draft,
    })
    cached = cache.get("skill_generation_v2", cache_key)
    cached_payload = cached.get("payload") if cached is not None else None
    if isinstance(cached_payload, dict) and cached_payload:
        payload = cached_payload
    else:
        payload: dict[str, Any] = {}
        last_error: Exception | None = None
        attempts = max(1, int(writer_retries) + 1)
        user_prompt = (prompt_cfg.get("hierarchical_user_template") or "").format(
            skill_level=draft.get("skill_level"),
            skill_id=draft.get("skill_id"),
            draft_json=json.dumps(
                _trim_skill_for_prompt(
                    draft,
                    max_examples=writer_examples,
                    statement_chars=writer_statement_chars,
                    code_chars=writer_code_chars,
                ),
                ensure_ascii=False,
                indent=2,
            ),
        )
        for attempt in range(1, attempts + 1):
            if attempt > 1:
                delay = max(0.0, float(writer_backoff_seconds)) * (attempt - 1)
                if delay:
                    time.sleep(delay)
                LOG.info(
                    "Stage D v2 DeepSeek retry %d/%d for %s",
                    attempt,
                    attempts,
                    draft.get("skill_id"),
                )
            try:
                payload = llm.chat_json(
                    system=prompt_cfg.get("hierarchical_system") or prompt_cfg.get("system") or "",
                    user=user_prompt,
                    temperature=float((prompt_cfg.get("hierarchical_recommended_params") or {}).get("temperature", 0.2)),
                    max_tokens=int(writer_max_tokens or (prompt_cfg.get("hierarchical_recommended_params") or {}).get("max_tokens", 1800)),
                )
                break
            except (LLMError, KeyError) as exc:
                last_error = exc
                LOG.warning(
                    "Stage D v2 DeepSeek attempt %d/%d failed for %s: %s",
                    attempt,
                    attempts,
                    draft.get("skill_id"),
                    exc,
                )
        if payload:
            cache.set("skill_generation_v2", cache_key, {"payload": payload})
        else:
            LOG.warning(
                "Stage D v2 DeepSeek failed for %s after %d attempt(s): %s; using rule fallback",
                draft.get("skill_id"),
                attempts,
                last_error or "empty payload",
            )
    merged = _normalize_v2_skill_payload(payload, draft)
    merged["generation_source"] = "deepseek" if payload else "rule_fallback"
    merged["generation_provider"] = provider
    merged["generation_model"] = model if payload else "deterministic"
    return merged


def _normalize_v2_skill_payload(payload: dict[str, Any], draft: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or not payload:
        return {**draft, "generation_source": "rule_fallback"}
    out = dict(draft)
    for key in (
        "skill_name",
        "description",
        "trigger_signals",
        "non_triggers",
        "failure_modes",
        "pattern_abstraction",
        "transfer_strategy",
        "representative_examples",
        "related_skills",
        "retrieval_text",
    ):
        if key in payload and payload[key]:
            out[key] = payload[key]
    out["skill_id"] = draft["skill_id"]
    out["skill_level"] = draft["skill_level"]
    out["family"] = draft.get("family", "")
    out["families"] = draft.get("families", [draft.get("family", "")] if draft.get("family") else [])
    out["subtype"] = draft.get("subtype", "")
    out["schema_version"] = STAGE_D_V2_VERSION
    return out


def _flatten_skill_for_retriever(skill: dict[str, Any]) -> dict[str, Any]:
    level = skill.get("skill_level")
    families = skill.get("families") or ([skill.get("family")] if skill.get("family") else [])
    return {
        **skill,
        "scope": "multi" if level == "bundle" else "single",
        "families": families,
        "applicable_when": skill.get("trigger_signals") or [],
        "problem_signals": skill.get("trigger_signals") or [],
        "core_idea": _core_idea_from_pattern(skill.get("pattern_abstraction")),
        "template_strategy": _strategy_steps(skill.get("transfer_strategy")),
        "common_pitfalls": skill.get("failure_modes") or [],
        "complexity_pattern": _complexity_from_pattern(skill.get("pattern_abstraction")),
        "retrieval_text": skill.get("retrieval_text") or _build_retrieval_text(
            skill_id=skill.get("skill_id", ""),
            skill_level=level or "",
            family=skill.get("family", ""),
            subtype=skill.get("subtype", ""),
            description=skill.get("description", ""),
            trigger_signals=skill.get("trigger_signals") or [],
            transfer_strategy=skill.get("transfer_strategy") or {},
        ),
        "compat_note": "Flattened Stage D v2 compatibility export; hierarchy files are the source of truth.",
    }


def _skill_evidence_packet(draft: dict[str, Any]) -> dict[str, Any]:
    return {
        "skill_id": draft.get("skill_id"),
        "skill_level": draft.get("skill_level"),
        "family": draft.get("family"),
        "families": draft.get("families"),
        "subtype": draft.get("subtype"),
        "num_source_examples": draft.get("num_source_examples"),
        "source_problem_ids": draft.get("source_problem_ids"),
        "representative_examples": draft.get("representative_examples"),
        "trigger_signals": draft.get("trigger_signals"),
    }


def _trim_skill_for_prompt(
    draft: dict[str, Any],
    *,
    max_examples: int = 2,
    statement_chars: int = 360,
    code_chars: int = 240,
) -> dict[str, Any]:
    keep_keys = (
        "schema_version",
        "skill_id",
        "skill_level",
        "skill_name",
        "description",
        "family",
        "families",
        "family_set",
        "component_families",
        "subtype",
        "trigger_signals",
        "non_triggers",
        "failure_modes",
        "pattern_abstraction",
        "transfer_strategy",
        "related_skills",
        "num_source_examples",
        "observed_multi_rows",
        "observed_primary_rows",
        "observed_primary_subtypes",
        "supported_families",
        "subtype_registry",
    )
    trimmed = {key: draft.get(key) for key in keep_keys if key in draft}
    slim_examples: list[dict[str, Any]] = []
    for example in (draft.get("representative_examples") or [])[: max(0, int(max_examples))]:
        slim_examples.append(
            {
                "problem_id": example.get("problem_id"),
                "solution_id": example.get("solution_id"),
                "family": example.get("family"),
                "subtype": example.get("subtype"),
                "reason": _short_text(example.get("reason"), 180),
                "problem_excerpt": _short_text(example.get("problem_excerpt"), statement_chars),
                "solution_excerpt": _short_text(example.get("solution_excerpt"), code_chars),
                "confidence": example.get("confidence"),
                "tests": example.get("tests"),
            }
        )
    trimmed["representative_examples"] = slim_examples
    trimmed["source_problem_ids"] = (draft.get("source_problem_ids") or [])[:12]
    trimmed["retrieval_text"] = _short_text(draft.get("retrieval_text"), 800)
    return trimmed


def _skill_brief(skill: dict[str, Any]) -> dict[str, Any]:
    return {
        "skill_id": skill.get("skill_id"),
        "skill_level": skill.get("skill_level"),
        "family": skill.get("family"),
        "subtype": skill.get("subtype"),
        "generation_source": skill.get("generation_source"),
        "examples": len(skill.get("representative_examples") or []),
    }


def _short_text(value: Any, limit: int) -> str:
    text = str(value or "")
    limit = max(0, int(limit))
    if limit and len(text) > limit:
        return text[:limit].rstrip() + "..."
    return text


def _rank_examples(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda r: (
            -int(bool(r.get("hard_filter_pass", True))),
            -float(r.get("subtype_confidence") or 0.0),
            -(float(r.get("primary_solution_score") or 0.0) - float(r.get("stage_d_quality_penalty") or 0.0)),
            -int(r.get("total_tests") or 0),
            str(r.get("problem_id") or ""),
        ),
    )


def _representative_examples(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    examples: list[dict[str, Any]] = []
    for row in rows:
        examples.append(
            {
                "problem_id": row.get("problem_id"),
                "solution_id": row.get("solution_id"),
                "family": row.get("detected_single_skill"),
                "subtype": row.get("primary_subtype"),
                "reason": (row.get("subtype_rationale") or row.get("core_mechanism_summary") or "verified primary solution")[:260],
                "problem_excerpt": (row.get("problem_statement") or "")[:V2_MAX_STATEMENT_CHARS],
                "solution_excerpt": (row.get("solution_code") or "")[:V2_MAX_CODE_CHARS],
                "confidence": row.get("subtype_confidence"),
                "tests": row.get("total_tests"),
            }
        )
    return examples


def _family_for_subtype(subtype: str) -> str:
    definition = get_subtype(subtype)
    return definition.family if definition else ""


def _subtype_trigger_signals(subtype: str, family: str, rows: list[dict[str, Any]]) -> list[str]:
    definition = get_subtype(subtype)
    signals: list[str] = []
    if definition:
        signals.extend(definition.problem_tag_seeds)
        signals.extend(definition.aliases)
        signals.extend(definition.solution_mechanism_seeds[:4])
    signals.extend(_top_problem_terms(rows, limit=6))
    signals.append(f"Stage C primary subtype is {subtype} under {family}.")
    return _unique_keep_order(signals, limit=10)


def _top_problem_terms(rows: list[dict[str, Any]], *, limit: int = 8) -> list[str]:
    text_parts: list[str] = []
    for row in rows[:20]:
        text_parts.append(" ".join(row.get("original_skill_types") or []))
        text_parts.append(" ".join(row.get("original_tags") or []))
        text_parts.append((row.get("problem_statement") or "")[:500])
        text_parts.append(" ".join(row.get("ast_hints") or []))
    counts: Counter[str] = Counter()
    for token in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", " ".join(text_parts).lower()):
        if token not in _STOPWORDS:
            counts[token.replace("_", " ")] += 1
    return [token for token, _ in counts.most_common(limit)]


def _default_non_triggers(family: str, *, subtype: str = "") -> list[str]:
    related = _family_hint(family).get("related_skills") or []
    items = [
        "Do not use when the problem statement only shares surface keywords but the state transition is different.",
        "Do not use when constraints make a simpler direct formula sufficient.",
        "Do not use when another family owns the main invariant.",
    ]
    for other in related[:3]:
        items.append(f"Prefer {other} when its trigger is the actual maintained invariant.")
    if subtype:
        items.append(f"Do not force {subtype} when another subtype in {family} has stronger code and statement evidence.")
    return items


def _default_failure_modes(family: str, *, subtype: str = "") -> list[str]:
    hint = _family_hint(family)
    items = list(hint.get("common_pitfalls") or [])
    if subtype:
        items.append(f"Copying an example of {subtype} without matching its state and transition assumptions.")
    items.append("Ignoring edge cases in initialization, empty inputs, or boundary indices.")
    return _unique_keep_order(items, limit=8)


def _pattern_abstraction_for(subtype: str, family: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    definition = get_subtype(subtype)
    family_template = _family_hint(family)
    code_tokens = Counter()
    for row in rows[:30]:
        for token in row.get("ast_hints") or []:
            code_tokens[token] += 1
        for token in (row.get("ast_features") or {}).keys():
            if (row.get("ast_features") or {}).get(token):
                code_tokens[token] += 1
    return {
        "core_recognition": definition.description if definition else f"Recognize {subtype} as a reusable {family} mechanism.",
        "state_templates": _unique_keep_order(
            list(definition.solution_mechanism_seeds if definition else [])[:4]
            + [token for token, _ in code_tokens.most_common(4)],
            limit=6,
        ),
        "transition_templates": _unique_keep_order((family_template.get("template_strategy") or [])[:4], limit=6),
        "base_case_rules": [
            "Define the smallest valid state before applying the recurrence or maintained invariant.",
            "Handle empty, singleton, and boundary inputs explicitly.",
        ],
        "iteration_order_rules": [
            "Choose an order that respects data dependencies.",
            "Update maintained structures only after preserving the invariant used by future steps.",
        ],
        "complexity_pattern": family_template.get("complexity_pattern") or "",
    }


def _transfer_strategy_for(subtype: str, family: str) -> dict[str, Any]:
    hint = _family_hint(family)
    definition = get_subtype(subtype)
    steps = list(hint.get("template_strategy") or [])
    if definition:
        steps.insert(0, f"Confirm the mechanism is {definition.description}")
    steps.extend(
        [
            "Map problem variables into the state/invariant names before coding.",
            "Write the transition or maintained operation in terms of the invariant, not the sample narrative.",
            "Check complexity against the largest constraints before finalizing.",
        ]
    )
    return {
        "steps": _unique_keep_order(steps, limit=8),
        "implementation_skeleton": [
            "parse inputs and normalize indexing",
            "initialize state/invariant",
            "iterate in dependency order",
            "apply transition/update",
            "extract answer from final state",
        ],
        "complexity_check": hint.get("complexity_pattern") or "",
    }


def _related_skills_for(family: str, *, subtype: str = "") -> list[str]:
    related = [f"family__{item}" for item in (_family_hint(family).get("related_skills") or [])]
    if subtype:
        definition = get_subtype(subtype)
        if definition:
            related.extend(f"subtype__{definition.family}__{other.subtype_id}" for other in all_subtypes_for_family(definition.family) if other.subtype_id != subtype)
    return _unique_keep_order(related, limit=12)


def all_subtypes_for_family(family: str) -> list[Any]:
    return [item for item in (get_subtype(s["subtype_id"]) for s in all_subtypes()) if item and item.family == family]


def _bundle_trigger_signals(
    families: tuple[str, ...],
    rows: list[dict[str, Any]],
    primary_rows: list[dict[str, Any]],
) -> list[str]:
    signals = [f"Problem-level family set includes {', '.join(families)}."]
    signals.extend(_top_problem_terms(primary_rows, limit=6))
    if not primary_rows:
        for row in rows[:20]:
            for tag in (row.get("original_skill_types") or []) + (row.get("original_tags") or []):
                signals.append(str(tag))
    signals.append("Multiple families appear necessary; use this as composition metadata rather than a pure subtype.")
    return _unique_keep_order(signals, limit=10)


def _build_retrieval_text(
    *,
    skill_id: str,
    skill_level: str,
    family: str,
    subtype: str,
    description: str,
    trigger_signals: list[str],
    transfer_strategy: dict[str, Any],
) -> str:
    steps = _strategy_steps(transfer_strategy)
    parts = [
        f"{skill_level} skill {skill_id}.",
        f"family {family}." if family else "",
        f"subtype {subtype}." if subtype else "",
        description,
        "triggers: " + "; ".join(trigger_signals[:6]),
        "strategy: " + "; ".join(steps[:6]),
    ]
    return " ".join(p for p in parts if p).strip()[:1600]


def _strategy_steps(strategy: Any) -> list[str]:
    if isinstance(strategy, dict):
        for key in ("steps", "implementation_skeleton", "family_selection_rules", "subtype_selection_rules"):
            if isinstance(strategy.get(key), list):
                return [str(item) for item in strategy[key]]
    if isinstance(strategy, list):
        return [str(item) for item in strategy]
    if strategy:
        return [str(strategy)]
    return []


def _core_idea_from_pattern(pattern: Any) -> str:
    if isinstance(pattern, dict):
        return str(pattern.get("core_recognition") or "")
    return str(pattern or "")


def _complexity_from_pattern(pattern: Any) -> str:
    if isinstance(pattern, dict):
        return str(pattern.get("complexity_pattern") or "")
    return ""


def _majority(values: list[str]) -> str:
    values = [v for v in values if v]
    return Counter(values).most_common(1)[0][0] if values else ""


def _count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    with open(path, "r", encoding="utf-8") as fh:
        return sum(1 for line in fh if line.strip())


def _bump(counter: dict[str, int], key: str) -> None:
    counter[key] = int(counter.get(key, 0)) + 1


def load_skills(settings: Settings) -> list[dict[str, Any]]:
    path = settings.stage_dir("stage_d") / "skills_merged.jsonl"
    if not path.exists():
        return []
    return load_jsonl(path)
