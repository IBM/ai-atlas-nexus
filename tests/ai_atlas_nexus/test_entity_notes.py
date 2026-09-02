"""Coverage for the ``notes`` slot on ``Entity`` (common.yaml).

The ``notes`` slot provides a data-level field for free-text editorial notes,
source breadcrumbs, or build-time provenance about an entity. It is distinct from:

* LinkML's metamodel-level ``notes:`` annotation (used in schema comments/permissible values)
* The ``description`` slot (which documents the entity's subject matter)

The slot is declared on the abstract ``Entity`` class so every concrete entity type
(Risk, Term, Organization, Dataset, etc.) inherits it for editorial metadata.

These tests verify:
1. The slot exists and is correctly wired to SKOS
2. The slot is multivalued (an entity may have multiple notes)
3. The slot is inherited by every Entity descendant
4. All required prefixes (particularly SKOS) resolve correctly in the root schema
"""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


# ---------------------------------------------------------------------------
# Schema under test
# ---------------------------------------------------------------------------

_SCHEMA = "src/ai_atlas_nexus/ai_risk_ontology/schema/ai-risk-ontology.yaml"

_SLOT = "notes"
_EXPECTED_SLOT_URI = "http://www.w3.org/2004/02/skos/core#note"


@pytest.fixture(scope="module")
def sv():
    """SchemaView of the merged root schema, with import closure resolved."""
    sv = SchemaView(_SCHEMA)
    sv.all_classes()  # Trigger import merge
    return sv


# ---------------------------------------------------------------------------
# Slot exists and is wired correctly
# ---------------------------------------------------------------------------


class TestNotesSlot:
    """The notes slot exists and connects to SKOS."""

    def test_notes_slot_exists(self, sv):
        slot = sv.get_slot(_SLOT)
        assert slot is not None, f"slot {_SLOT} is missing from {_SCHEMA}"

    def test_notes_slot_uri_maps_to_skos_note(self, sv):
        """The slot_uri expands to the full SKOS note URI."""
        slot = sv.get_slot(_SLOT)
        expanded = sv.get_uri(slot, expand=True)
        assert expanded == _EXPECTED_SLOT_URI, (
            f"notes slot_uri expanded to {expanded}, expected {_EXPECTED_SLOT_URI}"
        )

    def test_notes_slot_is_multivalued(self, sv):
        """An entity may have multiple notes."""
        slot = sv.get_slot(_SLOT)
        assert slot.multivalued, (
            f"{_SLOT} should be multivalued (an entity may have multiple notes)"
        )

    def test_notes_slot_is_optional(self, sv):
        """The slot is not required (existing data has no notes)."""
        slot = sv.get_slot(_SLOT)
        assert not slot.required, f"{_SLOT} is marked required (breaks existing data)"


# ---------------------------------------------------------------------------
# Slot inheritance
# ---------------------------------------------------------------------------


class TestNotesInheritance:
    """The notes slot reaches every Entity descendant."""

    def test_notes_declared_on_entity(self, sv):
        assert _SLOT in sv.class_slots("Entity"), (
            f"{_SLOT} not found in Entity's direct slots"
        )

    def test_notes_inherited_by_every_entity_descendant(self, sv):
        """A new Entity subclass automatically gets the notes slot.

        If a subclass defines slot_usage that drops notes, this test catches it.
        """
        entity_descendants = [
            cls_name
            for cls_name in sv.class_descendants("Entity", reflexive=False)
        ]
        assert entity_descendants, "Entity has no descendants (something is very wrong)"

        missing = [
            cls_name
            for cls_name in entity_descendants
            if _SLOT not in sv.class_slots(cls_name, direct=False)
        ]
        assert not missing, (
            f"Entity descendants missing {_SLOT} via induced slots: {missing}. "
            "Likely cause: a slot_usage in one of these classes drops or shadows it."
        )


# ---------------------------------------------------------------------------
# Prefix resolution
# ---------------------------------------------------------------------------


class TestRootSchemaPrefixes:
    """All prefixes used transitively by the root schema are declared at root level."""

    @pytest.mark.parametrize(
        "prefix,expected_uri",
        [
            ("dpv", "https://w3id.org/dpv#"),
            ("dpv-loc", "https://w3id.org/dpv/loc#"),
            ("dpv-risk", "https://w3id.org/dpv/risk#"),
            ("ai", "https://w3id.org/dpv/ai#"),
            ("tech", "https://w3id.org/dpv/tech#"),
            ("dqv", "https://www.w3.org/TR/vocab-dqv/"),
            ("skos", "http://www.w3.org/2004/02/skos/core#"),
            ("adms", "http://www.w3.org/ns/adms#"),
            ("adms-status", "http://purl.org/adms/status/"),
            ("pso", "http://purl.org/spar/pso/"),
        ],
    )
    def test_prefix_is_declared_and_resolves(self, sv, prefix, expected_uri):
        """Each prefix is declared in the root schema and expands to the expected URI."""
        namespaces = sv.namespaces()
        assert prefix in namespaces, (
            f"prefix {prefix} not found in root schema namespaces. "
            f"Available: {sorted(namespaces.keys())}"
        )
        actual_uri = str(namespaces[prefix])
        assert actual_uri == expected_uri, (
            f"prefix {prefix} expands to {actual_uri}, expected {expected_uri}"
        )
