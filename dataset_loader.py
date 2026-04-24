from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json

from schema import canonicalize_family_name, validate_json_payload


@dataclass(frozen=True)
class Sample:
    sample_id: str
    family_name: str
    subtype_name: str
    problem_path: Path
    solution_path: Path
    problem: str
    reference_code: str
    metadata: dict[str, object]

    def to_prompt_dict(self) -> dict[str, object]:
        payload: dict[str, object] = {
            "sample_id": self.sample_id,
            "family_name": self.family_name,
            "subtype_name": self.subtype_name,
            "problem_statement": self.problem,
            "reference_solution": self.reference_code,
        }
        prompt_metadata = {
            key: self.metadata[key]
            for key in (
                "source_dataset",
                "source_id",
                "difficulty",
                "skill_types",
                "tags",
                "family_assignment",
                "subtype_assignment",
            )
            if key in self.metadata
        }
        if prompt_metadata:
            payload["metadata"] = prompt_metadata
        return payload


@dataclass(frozen=True)
class SubtypeCluster:
    family_name: str
    subtype_name: str
    samples: list[Sample]

    @property
    def sample_count(self) -> int:
        return len(self.samples)

    def to_metadata(self, dataset_name: str) -> dict[str, object]:
        tag_hints = sorted(
            {
                str(tag)
                for sample in self.samples
                for tag in sample.metadata.get("tags", [])
                if isinstance(tag, str) and tag
            }
        )
        skill_type_hints = sorted(
            {
                str(skill_type)
                for sample in self.samples
                for skill_type in sample.metadata.get("skill_types", [])
                if isinstance(skill_type, str) and skill_type
            }
        )
        difficulty_distribution: dict[str, int] = {}
        for sample in self.samples:
            difficulty = sample.metadata.get("difficulty")
            if isinstance(difficulty, str) and difficulty:
                difficulty_distribution[difficulty] = difficulty_distribution.get(difficulty, 0) + 1

        metadata = {
            "algorithm_family_hint": self.family_name,
            "subtype_hint": self.subtype_name,
            "dataset_name": dataset_name,
            "sample_count": self.sample_count,
            "known_neighbors": [],
            "notes": [
                "directory labels are trusted as v1 supervision",
                "future versions may replace labels with automatic clustering",
            ],
        }
        if skill_type_hints:
            metadata["skill_type_hints"] = skill_type_hints
        if tag_hints:
            metadata["tag_hints"] = tag_hints
        if difficulty_distribution:
            metadata["difficulty_distribution"] = difficulty_distribution
        return metadata


@dataclass(frozen=True)
class DatasetManifest:
    dataset_name: str
    raw_payload: dict
    clusters: list[SubtypeCluster]


def load_dataset_manifest(datasets_dir: Path, schema_path: Path) -> DatasetManifest:
    if not datasets_dir.exists():
        raise FileNotFoundError(f"datasets directory not found: {datasets_dir}")

    clusters_by_key: dict[tuple[str, str], list[Sample]] = {}
    payload_by_key: dict[tuple[str, str], list[dict[str, object]]] = {}

    for family_dir in sorted(path for path in datasets_dir.iterdir() if path.is_dir()):
        family_name = canonicalize_family_name(family_dir.name)
        for subtype_dir in sorted(path for path in family_dir.iterdir() if path.is_dir()):
            cluster_key = (family_name, subtype_dir.name)
            samples = clusters_by_key.setdefault(cluster_key, [])
            samples_payload = payload_by_key.setdefault(cluster_key, [])
            for sample_dir in sorted(path for path in subtype_dir.iterdir() if path.is_dir()):
                problem_path = sample_dir / "problem.md"
                solution_path = sample_dir / "solution.py"
                metadata_path = sample_dir / "metadata.json"
                if not problem_path.exists() or not solution_path.exists():
                    raise ValueError(
                        f"sample '{sample_dir}' must contain both problem.md and solution.py"
                    )
                problem = problem_path.read_text(encoding="utf-8").strip()
                reference_code = solution_path.read_text(encoding="utf-8").strip()
                if not problem or not reference_code:
                    raise ValueError(f"sample '{sample_dir}' contains an empty problem or solution file")
                metadata: dict[str, object] = {}
                if metadata_path.exists():
                    try:
                        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"sample '{sample_dir}' metadata.json is invalid JSON: {exc}") from exc
                    if not isinstance(metadata, dict):
                        raise ValueError(f"sample '{sample_dir}' metadata.json must contain a JSON object")

                sample = Sample(
                    sample_id=sample_dir.name,
                    family_name=family_name,
                    subtype_name=subtype_dir.name,
                    problem_path=problem_path,
                    solution_path=solution_path,
                    problem=problem,
                    reference_code=reference_code,
                    metadata=metadata,
                )
                samples.append(sample)
                sample_payload = {
                    "sample_id": sample.sample_id,
                    "problem_path": str(problem_path.relative_to(datasets_dir)).replace("\\", "/"),
                    "solution_path": str(solution_path.relative_to(datasets_dir)).replace("\\", "/"),
                    "problem_statement": sample.problem,
                    "reference_solution": sample.reference_code,
                }
                if metadata:
                    sample_payload["metadata"] = metadata
                samples_payload.append(sample_payload)

    clusters = [
        SubtypeCluster(
            family_name=family_name,
            subtype_name=subtype_name,
            samples=samples,
        )
        for (family_name, subtype_name), samples in sorted(clusters_by_key.items())
    ]

    family_names = sorted({family_name for family_name, _ in clusters_by_key})
    families_payload: list[dict[str, object]] = []
    for family_name in family_names:
        subtypes_payload = []
        for subtype_name in sorted(
            subtype_name for current_family, subtype_name in clusters_by_key if current_family == family_name
        ):
            samples_payload = payload_by_key[(family_name, subtype_name)]
            subtypes_payload.append(
                {
                    "subtype_name": subtype_name,
                    "sample_count": len(samples_payload),
                    "samples": samples_payload,
                }
            )
        families_payload.append(
            {
                "family_name": family_name,
                "subtypes": subtypes_payload,
            }
        )

    payload = {
        "dataset_name": datasets_dir.name,
        "families": families_payload,
    }
    validate_json_payload(payload, schema_path, "dataset manifest")
    return DatasetManifest(
        dataset_name=datasets_dir.name,
        raw_payload=payload,
        clusters=clusters,
    )


def get_cluster(manifest: DatasetManifest, family_name: str, subtype_name: str) -> SubtypeCluster:
    family_name = canonicalize_family_name(family_name)
    for cluster in manifest.clusters:
        if cluster.family_name == family_name and cluster.subtype_name == subtype_name:
            return cluster
    raise ValueError(f"dataset cluster not found for family='{family_name}', subtype='{subtype_name}'")


def list_clusters(
    manifest: DatasetManifest,
    family_name: str | None = None,
) -> list[SubtypeCluster]:
    clusters = manifest.clusters
    if family_name is not None:
        family_name = canonicalize_family_name(family_name)
        clusters = [cluster for cluster in clusters if cluster.family_name == family_name]
    return clusters
