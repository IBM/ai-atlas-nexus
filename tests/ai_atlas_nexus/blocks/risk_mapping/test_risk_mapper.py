"""Tests for RiskMapper semantic mapping."""

from unittest.mock import patch

import pytest

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from ai_atlas_nexus.blocks.risk_mapping import RiskMapper
from ai_atlas_nexus.metadata_base import MappingMethod


def _risk(rid, name, description, taxonomy):
    return Risk(
        id=rid, name=name, description=description, isDefinedByTaxonomy=taxonomy
    )


def _make_mapper():
    return RiskMapper(
        new_risks=[],
        existing_risks=[],
        inference_engine=None,
        new_prefix="test",
        mapping_method=MappingMethod.SEMANTIC,
    )


class TestBucketSemanticScore:
    """_bucket_semantic_score buckets a 0-1 float into a SKOS predicate."""

    def test_exact_match(self):
        assert _make_mapper()._bucket_semantic_score(0.98) == "skos:exactMatch"

    def test_close_match(self):
        assert _make_mapper()._bucket_semantic_score(0.85) == "skos:closeMatch"

    def test_related_match(self):
        assert _make_mapper()._bucket_semantic_score(0.60) == "skos:relatedMatch"

    def test_no_match(self):
        assert _make_mapper()._bucket_semantic_score(0.20) is None

    def test_monotonic_ordering(self):
        """Higher similarity never yields a weaker relationship."""
        rank = {
            None: 0,
            "skos:relatedMatch": 1,
            "skos:closeMatch": 2,
            "skos:exactMatch": 3,
        }
        mapper = _make_mapper()
        scores = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
        ranks = [rank[mapper._bucket_semantic_score(s)] for s in scores]
        assert ranks == sorted(ranks)


class TestGenerateSemanticBelowThreshold:
    """A below-threshold match is skipped and logged, not emitted as a mapping."""

    @patch("ai_atlas_nexus.blocks.risk_mapping.risk_mapper.Embeddings")
    def test_below_threshold_emits_no_mapping(self, mock_embeddings, caplog):
        # force the top match to score below the related-match threshold
        mock_embeddings.return_value.search.return_value = [(0, 0.10)]
        existing = [_risk("atlas-a", "Alpha", "Alpha description", "tax-existing")]
        new = [_risk("new-x", "Xray", "Unrelated description", "tax-new")]

        with caplog.at_level("INFO"):
            mappings = _make_mapper().generate(
                new_risks=new,
                existing_risks=existing,
                inference_engine=None,
                new_prefix="tax-new",
                mapping_method=MappingMethod.SEMANTIC,
            )

        assert mappings == []
        assert "No match found for new-x" in caplog.text


@pytest.mark.slow
class TestGenerateSemantic:
    """generate() with SEMANTIC uses the similarity score, not the list index."""

    def test_similarity_score_is_a_float_not_an_index(self):
        existing = [
            _risk(
                "atlas-a", "Alpha risk", "A risk about alpha behaviour", "tax-existing"
            ),
            _risk(
                "atlas-b", "Beta risk", "A risk about beta behaviour", "tax-existing"
            ),
        ]
        # near-verbatim copy of the second existing risk -> high similarity
        new = [_risk("new-b", "Beta risk", "A risk about beta behaviour", "tax-new")]

        mapper = _make_mapper()
        mappings = mapper.generate(
            new_risks=new,
            existing_risks=existing,
            inference_engine=None,
            new_prefix="tax-new",
            mapping_method=MappingMethod.SEMANTIC,
        )

        assert len(mappings) == 1
        m = mappings[0]
        # matched the right existing risk
        assert m.object_id == "tax-existing:atlas-b"
        # similarity_score is a real 0-1 similarity, not the row index
        assert isinstance(m.similarity_score, float)
        assert 0.0 < m.similarity_score <= 1.0
        # a near-identical risk should be a strong match
        assert m.predicate_id in ("skos:exactMatch", "skos:closeMatch")
