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

from collections import defaultdict
from pathlib import Path
import re
from typing import Any, Iterable

import yaml

from .cache import DiskCache
from .io_utils import append_jsonl, load_jsonl, write_jsonl
from .llm.base import ChatLLM, LLMError
from .logging_utils import get_logger
from .settings import Settings
from .stage_a_filter import load_selected
from .stage_c_solution_label import load_consistent
from .taxonomy import CORE_FAMILY_SET, skill_id_for_multi, skill_id_for_single

LOG = get_logger(__name__)

MIN_SINGLE_EXAMPLES = 3
MIN_MULTI_EXAMPLES = 2
MAX_EXAMPLES_PER_SKILL = 6
MAX_STATEMENT_CHARS = 900
MAX_CODE_CHARS = 1000

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


def load_skills(settings: Settings) -> list[dict[str, Any]]:
    path = settings.stage_dir("stage_d") / "skills_merged.jsonl"
    if not path.exists():
        return []
    return load_jsonl(path)
