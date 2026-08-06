"""Coverage for the ``regenerate_owl_schema`` Makefile flags.

The OWL export needs two non-default ``gen-owl`` flags::

    --no-use-native-uris                external slot_uri / class_uri values become the
                                        RDF subject instead of the nexus: native name
    --default-permissible-value-type    enum permissible values are typed skos:Concept
      http://...skos/core#Concept       instead of owl:Class

Without them the published ontology asserts no relationship to AIRO, DPV, schema.org
or DCMI, and types SKOS concepts as OWL classes.

Coverage is deliberately two-layered:

1. **Makefile declares the flags** -- catches a flag being dropped from the build
   configuration, even before anyone regenerates.
2. **The committed artifact obeys them** -- catches the published deliverable drifting
   from the build configuration. This is the file consumers actually download, so it is
   the layer that matters most.

Note both layers read real files on disk. Constructing ``OwlSchemaGenerator`` in-process
with the flags passed as Python kwargs would be tautological: it would assert that
gen-owl honours its own arguments (an upstream concern) while passing regardless of what
the Makefile says.
"""

import re
from pathlib import Path

import pytest
import rdflib

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).resolve().parents[2]
_MAKEFILE = _REPO_ROOT / "Makefile"
_OWL_TTL = _REPO_ROOT / "graph_export" / "owl" / "ai-risk-ontology_schema.ttl"

# ---------------------------------------------------------------------------
# URIs asserted below
# ---------------------------------------------------------------------------

_SKOS = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
_AIRO = rdflib.Namespace("https://w3id.org/airo#")
_NEXUS = rdflib.Namespace("https://w3id.org/ai-atlas-nexus/")

# common.yaml: slot broad_mappings has  slot_uri: skos:broadMatch
_EXTERNAL_SLOT_URI = _SKOS.broadMatch
_NATIVE_SLOT_URI = _NEXUS.broad_mappings

# common.yaml: class License has  class_uri: airo:License
_EXTERNAL_CLASS_URI = _AIRO.License
_NATIVE_CLASS_URI = _NEXUS.License

# eu_ai_act.yaml: EuAiRiskCategory.EXCLUDED has no meaning:, so gen-owl mints a nexus: URI
_MINTED_PERMISSIBLE_VALUE = _NEXUS["EuAiRiskCategory#EXCLUDED"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_recipe(target: str) -> str:
    """Return the recipe body (tab-indented lines) of a Makefile target.

    Scoped to the target so a flag mentioned in an unrelated recipe -- or in the
    ``help`` target's echo lines -- cannot satisfy the assertions.
    """
    recipe, capturing = [], False
    for line in _MAKEFILE.read_text().splitlines():
        if re.match(rf"^{re.escape(target)}\s*:", line):
            capturing = True
            continue
        if capturing:
            if line.startswith("\t"):
                recipe.append(line)
            elif line.strip():  # next target begins
                break
    assert recipe, f"Makefile target {target!r} not found or has an empty recipe"
    return "\n".join(recipe)


@pytest.fixture(scope="module")
def owl_recipe():
    """The ``regenerate_owl_schema`` recipe body."""
    return _make_recipe("regenerate_owl_schema")


@pytest.fixture(scope="module")
def owl_graph():
    """The committed OWL artifact, parsed."""
    assert _OWL_TTL.is_file(), (
        f"{_OWL_TTL} is missing. It is a committed artifact -- regenerate it with "
        "`make regenerate_owl_schema`."
    )
    graph = rdflib.Graph()
    graph.parse(_OWL_TTL, format="ttl")
    return graph


# ---------------------------------------------------------------------------
# Layer 1 -- the build configuration declares the flags
# ---------------------------------------------------------------------------


class TestMakefileDeclaresOwlFlags:
    """The gen-owl invocation carries both non-default flags."""

    def test_declares_no_use_native_uris(self, owl_recipe):
        assert "--no-use-native-uris" in owl_recipe, (
            "regenerate_owl_schema must pass --no-use-native-uris, otherwise gen-owl "
            "emits nexus: native names and every external slot_uri / class_uri "
            "alignment is silently dropped from the published ontology."
        )

    def test_declares_skos_concept_permissible_value_type(self, owl_recipe):
        assert "--default-permissible-value-type" in owl_recipe, (
            "regenerate_owl_schema must pass --default-permissible-value-type."
        )
        assert "http://www.w3.org/2004/02/skos/core#Concept" in owl_recipe, (
            "--default-permissible-value-type must be skos:Concept; gen-owl otherwise "
            "defaults to owl:Class, typing SKOS concepts as OWL classes."
        )


# ---------------------------------------------------------------------------
# Layer 2 -- the published artifact reflects the flags
# ---------------------------------------------------------------------------


class TestOwlArtifactHonoursFlags:
    """The committed .ttl carries the alignments the flags are there to preserve."""

    def test_external_slot_uri_is_the_property_uri(self, owl_graph):
        """--no-use-native-uris, slot half.

        broad_mappings declares slot_uri: skos:broadMatch, so skos:broadMatch -- not
        nexus:broad_mappings -- must be the property in the exported ontology.
        """
        subjects = set(owl_graph.subjects())
        assert _EXTERNAL_SLOT_URI in subjects, (
            f"{_EXTERNAL_SLOT_URI} is absent from the OWL export. The artifact was "
            "generated without --no-use-native-uris; regenerate with "
            "`make regenerate_owl_schema`."
        )
        assert _NATIVE_SLOT_URI not in subjects, (
            f"{_NATIVE_SLOT_URI} appears in the OWL export, so the native slot URI "
            "shadowed the declared slot_uri."
        )

    def test_external_class_uri_is_the_class_uri(self, owl_graph):
        """--no-use-native-uris, class half.

        License declares class_uri: airo:License, so airo:License -- not nexus:License
        -- must be the OWL class.
        """
        subjects = set(owl_graph.subjects())
        assert _EXTERNAL_CLASS_URI in subjects, (
            f"{_EXTERNAL_CLASS_URI} is absent from the OWL export. The artifact was "
            "generated without --no-use-native-uris; regenerate with "
            "`make regenerate_owl_schema`."
        )
        assert _NATIVE_CLASS_URI not in subjects, (
            f"{_NATIVE_CLASS_URI} appears in the OWL export, so the native class URI "
            "shadowed the declared class_uri."
        )

    def test_permissible_values_typed_as_skos_concept(self, owl_graph):
        """--default-permissible-value-type.

        A permissible value is an individual, not a class. gen-owl's default types it
        owl:Class, which is wrong for a SKOS codelist -- adms:status, for instance,
        declares rdfs:range skos:Concept.
        """
        types = set(owl_graph.objects(_MINTED_PERMISSIBLE_VALUE, rdflib.RDF.type))
        found = types or "no rdf:type"
        assert _SKOS.Concept in types, (
            f"{_MINTED_PERMISSIBLE_VALUE} is not typed skos:Concept (got: {found}). "
            "The artifact was generated without --default-permissible-value-type; "
            "regenerate with `make regenerate_owl_schema`."
        )
        assert rdflib.OWL.Class not in types, (
            f"{_MINTED_PERMISSIBLE_VALUE} is typed owl:Class; a permissible value is an "
            "individual, not a class."
        )
