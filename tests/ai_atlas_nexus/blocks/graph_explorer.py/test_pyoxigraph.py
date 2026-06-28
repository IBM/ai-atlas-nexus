"""Tests for PyoxigraphExplorer — pyoxigraph-backed RDF graph explorer."""

import pytest

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.blocks.graph_explorer import AtlasExplorer, PyoxigraphExplorer


@pytest.fixture
def nexus():
    """Load AIAtlasNexus ontology."""
    return AIAtlasNexus()


@pytest.fixture
def ox_explorer(nexus):
    """Create PyoxigraphExplorer instance."""
    return PyoxigraphExplorer(nexus._ontology)


@pytest.fixture
def atlas_explorer(nexus):
    """Create AtlasExplorer instance for comparison."""
    return AtlasExplorer(nexus._ontology)


class TestPyoxigraphExplorerBasics:
    """Test basic PyoxigraphExplorer functionality."""

    def test_initialization(self, nexus):
        """Test that PyoxigraphExplorer initializes correctly."""
        ox = PyoxigraphExplorer(nexus._ontology)
        assert ox is not None
        assert ox._data is not None

    def test_get_all_classes(self, ox_explorer):
        """Test get_all_classes returns a list of available classes."""
        classes = ox_explorer.get_all_classes()
        assert isinstance(classes, list)
        assert len(classes) > 0
        # Check for known classes
        assert "Entry" in classes or "Risk" in classes
        assert "Action" in classes

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

        # Retrieve via PyoxigraphExplorer
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


class TestPyoxigraphExplorerClassNameResolution:
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


class TestPyoxigraphExplorerFiltering:
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
                item.isDefinedByTaxonomy == "nist-ai-rmf"
                for item in nist_actions
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


class TestPyoxigraphExplorerSPARQL:
    """Test SPARQL query functionality."""

    def test_sparql_query_basic(self, ox_explorer):
        """Test basic SPARQL query."""
        sparql = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX nexus: <https://w3id.org/ai-atlas-nexus/>

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
        PREFIX nexus: <https://w3id.org/ai-atlas-nexus/>

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
        PREFIX nexus: <https://w3id.org/ai-atlas-nexus/>

        SELECT ?s WHERE {
            ?s rdf:type nexus:Risk .
        }
        LIMIT 1
        """
        results = ox_explorer.sparql_query(sparql)
        if results and "error" not in results[0]:
            assert all(isinstance(r, dict) for r in results)


class TestPyoxigraphExplorerComparison:
    """Compare PyoxigraphExplorer with AtlasExplorer."""

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
        ox_filtered = ox_explorer.get_all("entries", taxonomy="ibm-risk-atlas")
        atlas_filtered = atlas_explorer.get_all(
            "entries", taxonomy="ibm-risk-atlas"
        )

        assert len(ox_filtered) == len(atlas_filtered)

    def test_get_all_risks_matches_library(self, ox_explorer, nexus):
        """Test that PyoxigraphExplorer results match library method."""
        ox_risks = ox_explorer.get_all("entries")
        lib_risks = nexus.get_all_risks()

        # Should have same count
        assert len(ox_risks) == len(lib_risks)

        # All items should be present in both results (order may differ)
        ox_ids = {r.id for r in ox_risks}
        lib_ids = {r.id for r in lib_risks}
        assert ox_ids == lib_ids


class TestPyoxigraphExplorerUtilities:
    """Test utility methods."""

    def test_filter_ids_by_type(self, ox_explorer):
        """Test filter_ids_by_type method."""
        all_ids = ox_explorer.query("entries")[:900]
        if all_ids:
            filtered = ox_explorer.filter_ids_by_type(
                all_ids, ["Documentation"]
            )
            assert isinstance(filtered, list)
            assert len(filtered) <= len(all_ids)

    def test_arrange_ids_by_type(self, ox_explorer):
        """Test arrange_ids_by_type method."""
        all_ids = ox_explorer.query("entries")[:900]
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


class TestPyoxigraphExplorerEdgeCases:
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


class TestPyoxigraphExplorerPydanticCompat:
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
            assert hasattr(first, "name") or hasattr(
                first, "isDefinedByTaxonomy"
            )
