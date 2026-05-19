"""Tests for OxigraphExplorer — pyoxigraph-backed RDF graph explorer."""

import pytest

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.blocks.atlas_explorer import (
    AtlasExplorer,
    OxigraphExplorer,
    StarGraph,
    StarGraphComparison,
)


@pytest.fixture
def nexus():
    """Load AIAtlasNexus ontology."""
    return AIAtlasNexus()


@pytest.fixture
def ox_explorer(nexus):
    """Create OxigraphExplorer instance."""
    return OxigraphExplorer(nexus._ontology)


@pytest.fixture
def atlas_explorer(nexus):
    """Create AtlasExplorer instance for comparison."""
    return AtlasExplorer(nexus._ontology)


class TestOxigraphExplorerBasics:
    """Test basic OxigraphExplorer functionality."""

    def test_initialization(self, nexus):
        """Test that OxigraphExplorer initializes correctly."""
        ox = OxigraphExplorer(nexus._ontology)
        assert ox is not None
        assert ox._data is not None
        assert len(ox._id_cache) > 0
        assert len(ox._collection_map) > 0

    def test_get_all_classes(self, ox_explorer):
        """Test get_all_classes returns a list of available classes."""
        classes = ox_explorer.get_all_classes()
        assert isinstance(classes, list)
        assert len(classes) > 0
        # Check for known classes
        assert "entries" in classes or "risks" in classes
        assert "actions" in classes

    def test_get_all_by_collection_key(self, ox_explorer):
        """Test get_all with collection key."""
        risks = ox_explorer.get_all("entries")
        assert isinstance(risks, list)
        assert len(risks) > 0
        # All items should be Risk objects
        assert all(hasattr(item, "id") for item in risks)

    def test_get_all_risks_count(self, ox_explorer, nexus):
        """Test that risk count matches library."""
        ox_risks = ox_explorer.get_all("entries")
        lib_risks = nexus.get_all_risks()
        assert len(ox_risks) == len(lib_risks)

    def test_get_all_actions_count(self, ox_explorer):
        """Test getting all actions."""
        actions = ox_explorer.get_all("actions")
        assert isinstance(actions, list)
        assert len(actions) > 0

    def test_get_by_id(self, ox_explorer, nexus):
        """Test get_by_id retrieval."""
        # Get a known risk
        lib_risks = nexus.get_all_risks()
        test_id = lib_risks[0].id

        # Retrieve via OxigraphExplorer
        retrieved = ox_explorer.get_by_id(None, test_id)
        assert retrieved is not None
        assert retrieved.id == test_id

    def test_get_by_id_nonexistent(self, ox_explorer):
        """Test get_by_id with nonexistent ID."""
        result = ox_explorer.get_by_id(None, "nonexistent-id-12345")
        assert result is None

    def test_get_by_id_multiple_calls(self, ox_explorer, nexus):
        """Test multiple get_by_id calls for same ID."""
        lib_risks = nexus.get_all_risks()
        test_id = lib_risks[0].id

        first = ox_explorer.get_by_id(None, test_id)
        second = ox_explorer.get_by_id(None, test_id)

        assert first is not None
        assert second is not None
        assert first.id == second.id


class TestOxigraphExplorerClassNameResolution:
    """Test _check_subclasses logic for flexible class name resolution."""

    def test_collection_key_entries(self, ox_explorer):
        """Test querying by collection key 'entries'."""
        results = ox_explorer.get_all("entries")
        assert len(results) > 0
        assert all(type(item).__name__ == "Risk" for item in results)

    def test_singular_class_name_risk(self, ox_explorer):
        """Test querying by singular class name 'Risk'."""
        results = ox_explorer.get_all("Risk")
        assert len(results) > 0
        assert all(type(item).__name__ == "Risk" for item in results)

    def test_plural_class_name_risks(self, ox_explorer):
        """Test querying by plural class name 'Risks'."""
        results = ox_explorer.get_all("Risks")
        assert len(results) > 0
        assert all(type(item).__name__ == "Risk" for item in results)

    def test_class_names_consistent(self, ox_explorer):
        """Test that collection key and class names return same results."""
        by_key = ox_explorer.get_all("entries")
        by_singular = ox_explorer.get_all("Risk")
        by_plural = ox_explorer.get_all("Risks")

        assert len(by_key) == len(by_singular) == len(by_plural)

    def test_collection_key_actions(self, ox_explorer):
        """Test querying actions by collection key."""
        results = ox_explorer.get_all("actions")
        assert len(results) > 0
        assert all(type(item).__name__ == "Action" for item in results)

    def test_singular_class_name_action(self, ox_explorer):
        """Test querying by singular class name 'Action'."""
        results = ox_explorer.get_all("Action")
        assert len(results) > 0
        assert all(type(item).__name__ == "Action" for item in results)

    def test_plural_class_name_actions(self, ox_explorer):
        """Test querying by plural class name 'Actions'."""
        results = ox_explorer.get_all("Actions")
        assert len(results) > 0
        assert all(type(item).__name__ == "Action" for item in results)

    def test_action_class_names_consistent(self, ox_explorer):
        """Test that collection key and class names for actions return same results."""
        by_key = ox_explorer.get_all("actions")
        by_singular = ox_explorer.get_all("Action")
        by_plural = ox_explorer.get_all("Actions")

        assert len(by_key) == len(by_singular) == len(by_plural)


class TestOxigraphExplorerFiltering:
    """Test filtering and attribute-based queries."""

    def test_filter_by_taxonomy(self, ox_explorer):
        """Test filtering by taxonomy."""
        filtered = ox_explorer.get_all("entries", taxonomy="ibm-risk-atlas")
        assert len(filtered) > 0
        assert all(
            item.isDefinedByTaxonomy == "ibm-risk-atlas" for item in filtered
        )

    def test_get_by_attribute(self, ox_explorer):
        """Test get_by_attribute."""
        # Get actions from NIST taxonomy
        nist_actions = ox_explorer.get_by_attribute(
            "actions", "isDefinedByTaxonomy", "nist-ai-rmf"
        )
        if nist_actions:  # NIST actions may or may not exist
            assert all(
                item.isDefinedByTaxonomy == "nist-ai-rmf" for item in nist_actions
            )

    def test_filter_instances(self, ox_explorer):
        """Test filter_instances with multiple criteria."""
        filtered = ox_explorer.filter_instances("entries", {})
        assert len(filtered) > 0

    def test_filter_instances_with_criteria(self, ox_explorer):
        """Test filter_instances with filtering criteria."""
        # Get all risks with IBM Risk Atlas taxonomy
        filtered = ox_explorer.filter_instances(
            "entries", {"isDefinedByTaxonomy": "ibm-risk-atlas"}
        )
        assert len(filtered) > 0
        assert all(
            item.isDefinedByTaxonomy == "ibm-risk-atlas" for item in filtered
        )

    def test_query_method(self, ox_explorer):
        """Test query method with keyword arguments."""
        results = ox_explorer.query("actions")
        assert len(results) > 0


class TestOxigraphExplorerSPARQL:
    """Test SPARQL query functionality."""

    def test_sparql_query_basic(self, ox_explorer):
        """Test basic SPARQL query."""
        sparql = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX nexus: <https://ibm.github.io/ai-atlas-nexus/ontology/>

        SELECT ?s WHERE {
            ?s rdf:type nexus:Risk .
        }
        LIMIT 5
        """
        results = ox_explorer.sparql_query(sparql)
        assert isinstance(results, list)
        assert len(results) > 0
        assert all("?s" in r or "error" in r for r in results)

    def test_sparql_query_relationships(self, ox_explorer):
        """Test SPARQL query for relationships."""
        sparql = """
        PREFIX nexus: <https://ibm.github.io/ai-atlas-nexus/ontology/>

        SELECT ?action ?risk WHERE {
            ?action nexus:hasRelatedRisk ?risk .
        }
        LIMIT 5
        """
        results = ox_explorer.sparql_query(sparql)
        assert isinstance(results, list)
        # May be empty or have results depending on data
        assert isinstance(results, list)

    def test_sparql_query_returns_dicts(self, ox_explorer):
        """Test that SPARQL query results are dictionaries."""
        sparql = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX nexus: <https://ibm.github.io/ai-atlas-nexus/ontology/>

        SELECT ?s WHERE {
            ?s rdf:type nexus:Risk .
        }
        LIMIT 1
        """
        results = ox_explorer.sparql_query(sparql)
        if results and "error" not in results[0]:
            assert all(isinstance(r, dict) for r in results)


class TestOxigraphExplorerCaching:
    """Test caching behavior."""

    def test_cache_built_on_init(self, ox_explorer):
        """Test that cache is built during initialization."""
        assert len(ox_explorer._id_cache) > 0
        assert len(ox_explorer._combined_cache) >= 0  # May be empty initially

    def test_clear_cache(self, ox_explorer):
        """Test clearing cache."""
        # Trigger some queries to populate cache
        ox_explorer.get_all("entries")
        assert len(ox_explorer._combined_cache) > 0

        # Clear cache
        ox_explorer.clear_cache()
        # combined_cache should be cleared but id_cache should remain
        assert len(ox_explorer._combined_cache) == 0
        assert len(ox_explorer._id_cache) > 0

    def test_cache_consistency(self, ox_explorer):
        """Test that queries return consistent results."""
        first = ox_explorer.get_all("entries")
        second = ox_explorer.get_all("entries")
        assert len(first) == len(second)
        assert [r.id for r in first] == [r.id for r in second]


class TestOxigraphExplorerComparison:
    """Compare OxigraphExplorer with AtlasExplorer."""

    def test_get_by_id_consistency(self, ox_explorer, atlas_explorer, nexus):
        """Test that get_by_id returns same results."""
        lib_risks = nexus.get_all_risks()
        test_id = lib_risks[0].id

        ox_result = ox_explorer.get_by_id(None, test_id)
        atlas_result = atlas_explorer.get_by_id(None, test_id)

        assert ox_result is not None
        assert atlas_result is not None
        assert ox_result.id == atlas_result.id

    def test_taxonomy_filter_consistency(self, ox_explorer, atlas_explorer):
        """Test that taxonomy filtering is consistent."""
        ox_filtered = ox_explorer.get_all(
            "entries", taxonomy="ibm-risk-atlas"
        )
        atlas_filtered = atlas_explorer.get_all(
            "entries", taxonomy="ibm-risk-atlas"
        )

        assert len(ox_filtered) == len(atlas_filtered)

    def test_get_all_risks_matches_library(self, ox_explorer, nexus):
        """Test that OxigraphExplorer results match library method."""
        ox_risks = ox_explorer.get_all("entries")
        lib_risks = nexus.get_all_risks()

        # Should have same count
        assert len(ox_risks) == len(lib_risks)

        # All items should be present in both results (order may differ)
        ox_ids = {r.id for r in ox_risks}
        lib_ids = {r.id for r in lib_risks}
        assert ox_ids == lib_ids


class TestOxigraphExplorerUtilities:
    """Test utility methods."""

    def test_filter_ids_by_type(self, ox_explorer):
        """Test filter_ids_by_type method."""
        all_ids = list(ox_explorer._id_cache.keys())[:10]
        if all_ids:
            filtered = ox_explorer.filter_ids_by_type(all_ids, ["Documentation"])
            assert isinstance(filtered, list)
            assert len(filtered) <= len(all_ids)

    def test_arrange_ids_by_type(self, ox_explorer):
        """Test arrange_ids_by_type method."""
        all_ids = list(ox_explorer._id_cache.keys())[:20]
        if all_ids:
            arranged = ox_explorer.arrange_ids_by_type(all_ids)
            assert isinstance(arranged, dict)
            # Should be grouped by type
            for type_name, ids in arranged.items():
                assert isinstance(ids, list)

    def test_get_attribute(self, ox_explorer, nexus):
        """Test get_attribute method."""
        lib_risks = nexus.get_all_risks()
        test_id = lib_risks[0].id

        name = ox_explorer.get_attribute(None, test_id, "name")
        assert name is not None


class TestOxigraphExplorerEdgeCases:
    """Test edge cases and error handling."""

    def test_get_all_with_none_class(self, ox_explorer):
        """Test get_all with None class name."""
        results = ox_explorer.get_all(None)
        assert isinstance(results, list)
        # Should return all instances across all classes
        assert len(results) > 0

    def test_empty_filter(self, ox_explorer):
        """Test filter_instances with empty filters."""
        results = ox_explorer.filter_instances("entries", {})
        assert isinstance(results, list)
        assert len(results) > 0

    def test_nonexistent_collection(self, ox_explorer):
        """Test get_all with nonexistent collection."""
        results = ox_explorer.get_all("nonexistent-class-xyz")
        assert isinstance(results, list)
        assert len(results) == 0

    def test_case_insensitive_class_name(self, ox_explorer):
        """Test that class name resolution is case-insensitive."""
        results_lower = ox_explorer.get_all("risk")
        results_upper = ox_explorer.get_all("RISK")
        results_title = ox_explorer.get_all("Risk")

        assert len(results_lower) == len(results_upper) == len(results_title)


class TestOxigraphExplorerPydanticCompat:
    """Test Pydantic object compatibility."""

    def test_returns_pydantic_objects(self, ox_explorer):
        """Test that queries return Pydantic objects."""
        risks = ox_explorer.get_all("entries")
        if risks:
            first = risks[0]
            # Check for Pydantic v2 attributes
            assert hasattr(first, "model_fields") or hasattr(
                first, "__pydantic_model__"
            )

    def test_pydantic_objects_have_id(self, ox_explorer):
        """Test that returned objects have id attribute."""
        risks = ox_explorer.get_all("entries")
        assert all(hasattr(item, "id") for item in risks)

    def test_pydantic_object_attribute_access(self, ox_explorer):
        """Test accessing attributes on returned Pydantic objects."""
        risks = ox_explorer.get_all("entries")
        if risks:
            first = risks[0]
            # Should be able to access attributes
            assert hasattr(first, "id")
            assert hasattr(first, "name") or hasattr(first, "isDefinedByTaxonomy")


class TestOxigraphExplorerSimilarity:
    """Test object_similarity and object_equivalence methods."""

    def test_object_similarity_identical_objects(self, ox_explorer):
        """Identical objects should have 100% similarity."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk = risks[0]
        scores = {}
        similarity = ox_explorer.object_similarity(risk, risk, 0.8, scores)

        assert pytest.approx(similarity, abs=0.01) == 100.0
        assert "_final_score" in scores
        assert pytest.approx(scores["_final_score"], abs=0.01) == 100.0

    def test_object_equivalence_identical_objects(self, ox_explorer):
        """Identical objects should be equivalent."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk = risks[0]
        scores = {}
        equivalent = ox_explorer.object_equivalence(risk, risk, 0.8, scores)

        assert equivalent is True

    def test_object_similarity_different_objects(self, ox_explorer):
        """Different objects should have lower similarity."""
        risks = ox_explorer.get_all("entries")
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        risk1, risk2 = risks[0], risks[1]
        scores = {}
        similarity = ox_explorer.object_similarity(risk1, risk2, 0.8, scores)

        assert isinstance(similarity, float)
        assert 0.0 <= similarity <= 100.0
        assert "_final_score" in scores

    def test_object_equivalence_threshold_gating(self, ox_explorer):
        """Threshold should gate equivalence result."""
        risks = ox_explorer.get_all("entries")
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        risk1, risk2 = risks[0], risks[1]
        scores = {}
        similarity = ox_explorer.object_similarity(risk1, risk2, 0.5, scores)

        threshold_low = 0.0
        threshold_high = 100.0

        equiv_low = ox_explorer.object_equivalence(risk1, risk2, threshold_low, {})
        equiv_high = ox_explorer.object_equivalence(risk1, risk2, threshold_high, {})

        if similarity >= threshold_low:
            assert equiv_low is True
        if similarity < threshold_high:
            assert equiv_high is False

    def test_property_scores_populated(self, ox_explorer):
        """property_scores dict should be populated with field scores."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk = risks[0]
        scores = {}
        ox_explorer.object_similarity(risk, risk, 0.8, scores)

        assert len(scores) > 0
        assert "_sum_of_weights" in scores
        assert "_final_score" in scores

        for field, field_scores in scores.items():
            if not field.startswith("_"):
                assert "score" in field_scores
                assert "weight" in field_scores
                assert "contributing_score" in field_scores

    def test_weight_dict_exclusion(self, ox_explorer):
        """weight_dict with 0 weight should exclude field."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk = risks[0]
        scores = {}

        weight_dict = {"id": 0}
        ox_explorer.object_similarity(risk, risk, 0.8, scores, weight_dict=weight_dict)

        assert "id" not in scores

    def test_weight_dict_custom_weights(self, ox_explorer):
        """Custom weights should affect similarity calculation."""
        risks = ox_explorer.get_all("entries")
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        risk1, risk2 = risks[0], risks[1]

        scores1 = {}
        sim1 = ox_explorer.object_similarity(risk1, risk2, 0.5, scores1)

        scores2 = {}
        weight_dict = {"name": 10.0, "description": 0.1}
        sim2 = ox_explorer.object_similarity(risk1, risk2, 0.5, scores2, weight_dict=weight_dict)

        assert isinstance(sim1, float)
        assert isinstance(sim2, float)

    def test_object_similarity_with_none_values(self, ox_explorer):
        """Objects with None values should still compute similarity."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk1 = risks[0]
        risk2 = risks[0]

        scores = {}
        similarity = ox_explorer.object_similarity(risk1, risk2, 0.5, scores)

        assert pytest.approx(similarity, abs=0.01) == 100.0

    def test_object_similarity_depth_zero(self, ox_explorer):
        """max_depth=0 should not recurse into references."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk = risks[0]
        scores = {}
        similarity = ox_explorer.object_similarity(risk, risk, 0.5, scores, max_depth=0)

        assert similarity == 100.0

    def test_object_equivalence_returns_bool(self, ox_explorer):
        """object_equivalence should always return bool."""
        risks = ox_explorer.get_all("entries")
        if not risks:
            pytest.skip("No risks found")

        risk = risks[0]
        result = ox_explorer.object_equivalence(risk, risk, 0.5, {})

        assert isinstance(result, bool)
        assert result is True

    def test_object_similarity_actions(self, ox_explorer):
        """Test similarity with Action objects."""
        actions = ox_explorer.get_all("actions")
        if not actions:
            pytest.skip("No actions found")

        action = actions[0]
        scores = {}
        similarity = ox_explorer.object_similarity(action, action, 0.5, scores)

        assert similarity > 50.0


class TestStarGraph:
    """Test star graph extraction functionality."""

    def test_get_star_graph_known_id(self, ox_explorer, nexus):
        """Test get_star_graph returns a StarGraph with correct structure."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        star_graph = ox_explorer.get_star_graph(test_id)

        assert isinstance(star_graph, StarGraph)
        assert star_graph.center_id == test_id
        assert star_graph.center is not None
        assert isinstance(star_graph.neighbors, dict)

    def test_get_star_graph_unknown_id(self, ox_explorer):
        """Test get_star_graph raises ValueError for unknown ID."""
        with pytest.raises(ValueError, match="not found in id cache"):
            ox_explorer.get_star_graph("nonexistent-id-xyz-12345")

    def test_star_graph_neighbor_ids_property(self, ox_explorer, nexus):
        """Test neighbor_ids property returns set of IDs."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        star_graph = ox_explorer.get_star_graph(test_id)

        neighbor_ids = star_graph.neighbor_ids
        assert isinstance(neighbor_ids, set)
        # All neighbor IDs should exist in _id_cache
        for nid in neighbor_ids:
            assert nid in ox_explorer._id_cache

    def test_star_graph_skips_literal_fields(self, ox_explorer, nexus):
        """Test that literal fields are not in neighbors."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        star_graph = ox_explorer.get_star_graph(test_id)

        # Literal fields should not be in neighbors
        literal_fields = {"name", "description", "tag", "url", "concern"}
        for field in literal_fields:
            assert field not in star_graph.neighbors

    def test_get_star_graph_actions(self, ox_explorer):
        """Test get_star_graph works for Action entities."""
        actions = ox_explorer.get_all("actions")
        if not actions:
            pytest.skip("No actions found")

        action_id = actions[0].id
        star_graph = ox_explorer.get_star_graph(action_id)

        assert star_graph.center_id == action_id
        assert star_graph.center is not None
        assert isinstance(star_graph.neighbors, dict)

    def test_star_graph_with_no_neighbors(self, ox_explorer):
        """Test star graph for entity with no references."""
        # Try to find an entity with no neighbors
        for entity_id, entity in ox_explorer._id_cache.items():
            star_graph = ox_explorer.get_star_graph(entity_id)
            # Even with no neighbors, should return valid StarGraph
            assert star_graph.center_id == entity_id
            assert isinstance(star_graph.neighbors, dict)
            if not star_graph.neighbors:
                break

    def test_get_star_graph_default_depth_unchanged(self, ox_explorer, nexus):
        """Test that default max_depth=1 behavior is unchanged."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        graph_default = ox_explorer.get_star_graph(test_id)
        graph_explicit_1 = ox_explorer.get_star_graph(test_id, max_depth=1)

        assert graph_default.center_id == graph_explicit_1.center_id
        assert graph_default.neighbor_ids == graph_explicit_1.neighbor_ids
        assert graph_default.neighbors == graph_explicit_1.neighbors

    def test_get_star_graph_depth_2_expands_neighbors(self, ox_explorer, nexus):
        """Test that depth=2 includes all depth=1 neighbors and potentially more."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        graph_1 = ox_explorer.get_star_graph(test_id, max_depth=1)
        graph_2 = ox_explorer.get_star_graph(test_id, max_depth=2)

        # depth=2 should have at least as many neighbors as depth=1
        assert len(graph_2.neighbor_ids) >= len(graph_1.neighbor_ids)
        # depth=1 neighbors should be subset of depth=2 neighbors
        assert graph_1.neighbor_ids.issubset(graph_2.neighbor_ids)

    def test_get_star_graph_no_cycles(self, ox_explorer, nexus):
        """Test that visited set prevents center entity from appearing as neighbor."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        graph = ox_explorer.get_star_graph(test_id, max_depth=2)

        # Center entity should never be in neighbors (no self-loops)
        assert test_id not in graph.neighbor_ids

    def test_get_star_graph_depth_0_returns_only_center(self, ox_explorer, nexus):
        """Test that max_depth=0 returns only center with no neighbors."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        graph = ox_explorer.get_star_graph(test_id, max_depth=0)

        assert graph.center_id == test_id
        assert len(graph.neighbors) == 0
        assert graph.neighbor_ids == set()


class TestStarGraphComparison:
    """Test star graph comparison functionality."""

    def test_compare_same_id(self, ox_explorer, nexus):
        """Test comparing identical entities - Jaccard should be 1.0."""
        risks = nexus.get_all_risks()
        if not risks:
            pytest.skip("No risks found")

        test_id = risks[0].id
        comparison = ox_explorer.compare_star_graphs(test_id, test_id)

        assert isinstance(comparison, StarGraphComparison)
        assert comparison.jaccard_similarity == 1.0
        assert comparison.unique_to_a == set()
        assert comparison.unique_to_b == set()
        # All neighbors should be shared
        assert len(comparison.shared_neighbor_ids) == len(comparison.graph_a.neighbor_ids)

    def test_compare_different_ids(self, ox_explorer, nexus):
        """Test comparing two different entities."""
        risks = nexus.get_all_risks()
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        id_a, id_b = risks[0].id, risks[1].id
        comparison = ox_explorer.compare_star_graphs(id_a, id_b)

        assert isinstance(comparison, StarGraphComparison)
        assert 0.0 <= comparison.jaccard_similarity <= 1.0
        assert isinstance(comparison.shared_neighbor_ids, set)
        assert isinstance(comparison.unique_to_a, set)
        assert isinstance(comparison.unique_to_b, set)
        assert isinstance(comparison.per_field, dict)

    def test_compare_structure(self, ox_explorer, nexus):
        """Test that comparison has correct structure."""
        risks = nexus.get_all_risks()
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        id_a, id_b = risks[0].id, risks[1].id
        comparison = ox_explorer.compare_star_graphs(id_a, id_b)

        # Check star graphs
        assert comparison.graph_a.center_id == id_a
        assert comparison.graph_b.center_id == id_b

        # Check set sizes are correct
        union = comparison.shared_neighbor_ids | comparison.unique_to_a | comparison.unique_to_b
        assert union == comparison.graph_a.neighbor_ids | comparison.graph_b.neighbor_ids

    def test_per_field_breakdown(self, ox_explorer, nexus):
        """Test per_field breakdown in comparison."""
        risks = nexus.get_all_risks()
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        id_a, id_b = risks[0].id, risks[1].id
        comparison = ox_explorer.compare_star_graphs(id_a, id_b)

        # Each field in per_field should have shared/unique_to_a/unique_to_b
        for field, breakdown in comparison.per_field.items():
            assert isinstance(breakdown, dict)
            assert "shared" in breakdown
            assert "unique_to_a" in breakdown
            assert "unique_to_b" in breakdown
            assert isinstance(breakdown["shared"], set)
            assert isinstance(breakdown["unique_to_a"], set)
            assert isinstance(breakdown["unique_to_b"], set)

    def test_compare_cross_entity_types(self, ox_explorer):
        """Test comparing different entity types (Risk vs Action)."""
        risks = ox_explorer.get_all("entries")
        actions = ox_explorer.get_all("actions")

        if not risks or not actions:
            pytest.skip("Need both risks and actions")

        risk_id = risks[0].id
        action_id = actions[0].id

        comparison = ox_explorer.compare_star_graphs(risk_id, action_id)

        assert isinstance(comparison, StarGraphComparison)
        assert 0.0 <= comparison.jaccard_similarity <= 1.0

    def test_compare_star_graphs_max_depth(self, ox_explorer, nexus):
        """Test comparing star graphs with max_depth=2."""
        risks = nexus.get_all_risks()
        if len(risks) < 2:
            pytest.skip("Need at least 2 risks")

        id_a, id_b = risks[0].id, risks[1].id

        # Compare with depth=1 and depth=2
        cmp_1 = ox_explorer.compare_star_graphs(id_a, id_b, max_depth=1)
        cmp_2 = ox_explorer.compare_star_graphs(id_a, id_b, max_depth=2)

        # depth=2 comparison should have valid structure
        assert isinstance(cmp_2, StarGraphComparison)
        assert 0.0 <= cmp_2.jaccard_similarity <= 1.0

        # depth=2 neighbor sets should be >= depth=1
        assert len(cmp_2.graph_a.neighbor_ids) >= len(cmp_1.graph_a.neighbor_ids)
        assert len(cmp_2.graph_b.neighbor_ids) >= len(cmp_1.graph_b.neighbor_ids)
