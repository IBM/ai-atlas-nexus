"""Evaluate proposed cross-taxonomy mappings against curated ground truth.

The risk mapper produces suggested mappings between taxonomies. This utility
scores those suggestions against a set of curated (human-reviewed) mappings so
we can establish a baseline and re-run the same measurement after changes.
"""

from pathlib import Path

from sssom_schema import Mapping


# Curated mapping files ship in the package data directory.
_MAPPINGS_DIR = Path(__file__).resolve().parents[2] / "data" / "mappings"


def load_curated_mappings(
    filename: str,
    justification: str = "semapv:ManualMappingCuration",
    risk_ids: set[str] | None = None,
) -> list[Mapping]:
    """Load curated mappings from a shipped SSSOM/TSV file, for use as ground truth.

    Args:
        filename: str
            Name of a mapping file in the package's data/mappings directory.
        justification: str
            Keep only mappings with this mapping_justification. Defaults to
            manual curation so the mapper is not scored against machine-generated
            mappings, which would be circular.
        risk_ids: set[str], optional
            If given, keep only mappings where both subject and object are risk
            ids in this set. Excludes non-risk targets, e.g. classification
            factors or requirements, that some curated files also mix in.

    Returns:
        list[Mapping]: the curated mappings, with noMatch rows removed.
    """
    from sssom.parsers import parse_sssom_table

    path = _MAPPINGS_DIR / filename
    mapping_set = parse_sssom_table(file_path=str(path)).to_mapping_set()
    mappings = [
        m
        for m in mapping_set.mappings
        if m.mapping_justification == justification and m.predicate_id != "noMatch"
    ]
    if risk_ids is not None:
        mappings = [
            m
            for m in mappings
            if str(m.subject_id).split(":")[-1] in risk_ids
            and str(m.object_id).split(":")[-1] in risk_ids
        ]
    return mappings


def _pair_key(mapping: Mapping) -> tuple:
    """Return a direction-agnostic key for a mapping.

    Ids are stored as CURIEs (e.g. ``ibm-risk-atlas:atlas-x``). We compare on
    the local part after the prefix, and sort the two ids so that a mapping and
    its reverse are treated as the same pair.
    """
    subject = str(mapping.subject_id).split(":")[-1]
    obj = str(mapping.object_id).split(":")[-1]
    return tuple(sorted((subject, obj)))


def evaluate_mappings(predicted: list[Mapping], ground_truth: list[Mapping]) -> dict:
    """Score predicted mappings against curated ground-truth mappings.

    Matching is on the risk pair only (direction-agnostic) and ignores the
    predicate, which keeps this focused on retrieval and coverage.

    Args:
        predicted: list[Mapping]
            Mappings produced by the risk mapper.
        ground_truth: list[Mapping]
            Curated mappings to score against.

    Returns:
        dict: retrieval metrics (precision, recall, F1 on risk pairs, with
        counts) and coverage (the fraction of ground-truth source risks for
        which at least one curated mapping was recovered). A metric is
        ``None`` when it is not applicable, e.g. precision when nothing was
        predicted, which is different from a real ``0.0`` (something was
        predicted and none of it was correct).
    """
    predicted_pairs = {_pair_key(m) for m in predicted}
    ground_truth_pairs = {_pair_key(m) for m in ground_truth}
    matched_pairs = predicted_pairs & ground_truth_pairs

    n_predicted = len(predicted_pairs)
    n_ground_truth = len(ground_truth_pairs)
    n_matched = len(matched_pairs)

    precision = n_matched / n_predicted if n_predicted else None
    recall = n_matched / n_ground_truth if n_ground_truth else None
    if precision is None or recall is None:
        f1 = None
    else:
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0

    # Coverage: for how many curated source risks did we recover at least one of
    # their curated mappings? This is more informative than pair recall when a
    # source risk has several curated targets but the mapper returns one match.
    pairs_by_source: dict = {}
    for mapping in ground_truth:
        source = str(mapping.subject_id).split(":")[-1]
        pairs_by_source.setdefault(source, set()).add(_pair_key(mapping))

    covered = sum(1 for pairs in pairs_by_source.values() if pairs & predicted_pairs)
    n_sources = len(pairs_by_source)
    source_coverage = covered / n_sources if n_sources else None

    return {
        "retrieval": {
            "precision": round(precision, 4) if precision is not None else None,
            "recall": round(recall, 4) if recall is not None else None,
            "f1": round(f1, 4) if f1 is not None else None,
            "n_predicted_pairs": n_predicted,
            "n_ground_truth_pairs": n_ground_truth,
            "n_matched_pairs": n_matched,
        },
        "coverage": {
            "source_risk_coverage": round(source_coverage, 4) if source_coverage is not None else None,
            "n_source_risks": n_sources,
            "n_source_risks_covered": covered,
        },
    }
