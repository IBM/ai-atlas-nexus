"""Tests for evaluate_mappings (mapping-quality metrics)."""

from sssom_schema import Mapping

from ai_atlas_nexus.blocks.risk_mapping import evaluate_mappings, load_curated_mappings


def _m(subject, obj, predicate="skos:relatedMatch"):
    return Mapping(
        subject_id=subject,
        predicate_id=predicate,
        object_id=obj,
        mapping_justification="semapv:ManualMappingCuration",
    )


class TestRetrieval:

    def test_perfect_match(self):
        gt = [_m("ibm:a", "mit:x"), _m("ibm:b", "mit:y")]
        pred = [_m("ibm:a", "mit:x"), _m("ibm:b", "mit:y")]
        r = evaluate_mappings(pred, gt)["retrieval"]
        assert r["precision"] == 1.0
        assert r["recall"] == 1.0
        assert r["f1"] == 1.0
        assert r["n_matched_pairs"] == 2

    def test_partial_overlap(self):
        gt = [_m("ibm:a", "mit:x"), _m("ibm:b", "mit:y")]
        pred = [_m("ibm:a", "mit:x"), _m("ibm:c", "mit:z")]  # 1 right, 1 wrong
        r = evaluate_mappings(pred, gt)["retrieval"]
        assert r["precision"] == 0.5  # 1 of 2 predicted correct
        assert r["recall"] == 0.5  # 1 of 2 ground truth found
        assert r["f1"] == 0.5

    def test_direction_agnostic(self):
        # ground truth ibm->mit, prediction mit->ibm: same pair
        gt = [_m("ibm-risk-atlas:a", "mit-ai-risk-repository:x")]
        pred = [_m("mit-ai-risk-repository:x", "ibm-risk-atlas:a")]
        r = evaluate_mappings(pred, gt)["retrieval"]
        assert r["n_matched_pairs"] == 1
        assert r["recall"] == 1.0

    def test_curie_prefixes_ignored(self):
        # same local ids, different prefixes still match
        gt = [_m("ibmairisk:atlas-x", "nistai:nist-y")]
        pred = [_m("ibm-risk-atlas:atlas-x", "nist-ai-rmf:nist-y")]
        assert evaluate_mappings(pred, gt)["retrieval"]["n_matched_pairs"] == 1

    def test_duplicate_predictions_counted_once(self):
        gt = [_m("ibm:a", "mit:x")]
        pred = [_m("ibm:a", "mit:x"), _m("ibm:a", "mit:x")]
        r = evaluate_mappings(pred, gt)["retrieval"]
        assert r["n_predicted_pairs"] == 1
        assert r["precision"] == 1.0

    def test_empty_predicted(self):
        # nothing predicted -> precision is not applicable, not a real 0.0
        gt = [_m("ibm:a", "mit:x")]
        r = evaluate_mappings([], gt)["retrieval"]
        assert r["precision"] is None
        assert r["recall"] == 0.0
        assert r["f1"] is None

    def test_empty_ground_truth_does_not_divide_by_zero(self):
        # no ground truth -> recall is not applicable, not a real 0.0
        pred = [_m("ibm:a", "mit:x")]
        r = evaluate_mappings(pred, [])["retrieval"]
        assert r["recall"] is None
        assert r["precision"] == 0.0
        assert r["f1"] is None


class TestCoverage:

    def test_source_covered_when_one_of_several_targets_found(self):
        # source "a" has 3 curated targets; mapper finds only 1 -> a is covered
        gt = [_m("ibm:a", "mit:x"), _m("ibm:a", "mit:y"), _m("ibm:a", "mit:z")]
        pred = [_m("ibm:a", "mit:y")]
        result = evaluate_mappings(pred, gt)
        assert result["coverage"]["source_risk_coverage"] == 1.0
        assert result["coverage"]["n_source_risks"] == 1
        assert result["coverage"]["n_source_risks_covered"] == 1
        # but pair recall reflects the many-to-many gap
        assert result["retrieval"]["recall"] == round(1 / 3, 4)

    def test_partial_source_coverage(self):
        gt = [_m("ibm:a", "mit:x"), _m("ibm:b", "mit:y")]
        pred = [_m("ibm:a", "mit:x")]  # covers a, not b
        cov = evaluate_mappings(pred, gt)["coverage"]
        assert cov["n_source_risks"] == 2
        assert cov["n_source_risks_covered"] == 1
        assert cov["source_risk_coverage"] == 0.5

    def test_no_ground_truth(self):
        # no ground-truth sources -> coverage is not applicable, not a real 0.0
        cov = evaluate_mappings([_m("ibm:a", "mit:x")], [])["coverage"]
        assert cov["source_risk_coverage"] is None
        assert cov["n_source_risks"] == 0


class TestLoadCuratedMappings:
    """Loading curated ground truth from the shipped SSSOM files."""

    def test_loads_ibm_mit_manual_pairs(self):
        # exact row count isn't asserted, the file can grow as more mappings
        # are curated; what must hold is that every row is manual and complete
        mappings = load_curated_mappings("mit-ai-risk-repository_ibm-risk-atlas.tsv")
        assert mappings
        assert all(
            m.mapping_justification == "semapv:ManualMappingCuration" for m in mappings
        )
        assert all(m.subject_id and m.object_id for m in mappings)

    def test_default_keeps_only_manual_curation(self):
        # this file mixes ManualMappingCuration with SemanticSimilarityThresholdMatching,
        # so this proves the filter both keeps manual rows and drops non-manual ones
        mappings = load_curated_mappings("aiuc1_to_ibm_from_tsv_data.tsv")
        assert mappings
        assert all(
            m.mapping_justification == "semapv:ManualMappingCuration" for m in mappings
        )

    def test_drops_no_match_rows(self):
        mappings = load_curated_mappings("ibm2owasp.tsv")
        assert mappings  # file has manual rows
        assert all(m.predicate_id != "noMatch" for m in mappings)

    def test_risk_ids_filters_out_non_risk_targets(self):
        # this subject also maps to MIT causal factors (not risks), which
        # must be dropped when risk_ids only lists the real risk on both sides
        risk_ids = {"atlas-attribute-inference-attack", "mit-ai-risk-subdomain-2.2"}
        mappings = load_curated_mappings(
            "mit-ai-risk-repository_ibm-risk-atlas.tsv", risk_ids=risk_ids
        )
        assert mappings
        assert all(
            str(m.subject_id).split(":")[-1] in risk_ids
            and str(m.object_id).split(":")[-1] in risk_ids
            for m in mappings
        )
