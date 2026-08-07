"""Evaluate proposed cross-taxonomy mappings against curated ground truth.

The risk mapper produces suggested mappings between taxonomies. This utility
scores those suggestions against a set of curated (human-reviewed) mappings so
we can establish a baseline and re-run the same measurement after changes.
"""

from sssom_schema import Mapping


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
        which at least one curated mapping was recovered).
    """
    predicted_pairs = {_pair_key(m) for m in predicted}
    ground_truth_pairs = {_pair_key(m) for m in ground_truth}
    matched_pairs = predicted_pairs & ground_truth_pairs

    n_predicted = len(predicted_pairs)
    n_ground_truth = len(ground_truth_pairs)
    n_matched = len(matched_pairs)

    precision = n_matched / n_predicted if n_predicted else 0.0
    recall = n_matched / n_ground_truth if n_ground_truth else 0.0
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
    source_coverage = covered / n_sources if n_sources else 0.0

    return {
        "retrieval": {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "n_predicted_pairs": n_predicted,
            "n_ground_truth_pairs": n_ground_truth,
            "n_matched_pairs": n_matched,
        },
        "coverage": {
            "source_risk_coverage": round(source_coverage, 4),
            "n_source_risks": n_sources,
            "n_source_risks_covered": covered,
        },
    }
