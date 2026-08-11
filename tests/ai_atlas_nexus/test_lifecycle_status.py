"""Coverage for the ``LifecycleStatus`` enum and ``hasLifecycleStatus`` slot (common.yaml).

``hasLifecycleStatus`` carries the editorial / publication state of any catalogued
``Entity``. Its permissible values are aligned to external vocabularies:

* the **ADMS status codelist** at ``http://purl.org/adms/status/`` -- four values
  (UnderDevelopment, Completed, Deprecated, Withdrawn);
* **PSO** (SPAR) at ``http://purl.org/spar/pso/`` for ``REVIEW``, which ADMS has no
  equivalent for;
* the nexus namespace for ``SUPERSEDED``, which neither vocabulary defines.

The alignment is easy to break in a way nothing else catches, because a wrong CURIE
still lints, still generates, and still produces plausible-looking RDF. The critical
trap is that ADMS has *two* namespaces: the vocabulary ``http://www.w3.org/ns/adms#``
(which defines ``adms:status`` and only 4 classes / 13 properties) and the separate
value codelist ``http://purl.org/adms/status/``. Writing ``adms:Completed`` instead of
``adms-status:Completed`` mints a term into a W3C namespace we do not own -- see
``test_no_meaning_lands_in_adms_vocabulary_namespace``.

These tests read the schema itself rather than any generated artifact: at time of
writing the OWL export and the Pydantic datamodel are both stale with respect to this
slot, and the schema is the source of truth regardless.
"""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


# ---------------------------------------------------------------------------
# Schema under test
# ---------------------------------------------------------------------------

_SCHEMA = "src/ai_atlas_nexus/ai_risk_ontology/schema/ai-risk-ontology.yaml"

_ENUM = "LifecycleStatus"
_SLOT = "hasLifecycleStatus"

# Namespaces
_ADMS_VOCAB = "http://www.w3.org/ns/adms#"  # vocabulary: adms:status lives here
_ADMS_CODELIST = "http://purl.org/adms/status/"  # codelist: the values live here
_PSO = "http://purl.org/spar/pso/"

# Expected fully-expanded meaning per permissible value. None => intentionally
# unaligned, minted in the nexus namespace.
#
# Transcribed by hand from the published vocabularies; the tests compare the schema
# against this table, not against ADMS or PSO themselves. Re-check the far end by
# hand when touching alignment.
_EXPECTED_MEANINGS = {
    "DRAFT": _ADMS_CODELIST + "UnderDevelopment",
    "REVIEW": _PSO + "under-review",
    "APPROVED": _ADMS_CODELIST + "Completed",
    "DEPRECATED": _ADMS_CODELIST + "Deprecated",
    "SUPERSEDED": None,
    "WITHDRAWN": _ADMS_CODELIST + "Withdrawn",
}


@pytest.fixture(scope="module")
def sv():
    return SchemaView(_SCHEMA)


@pytest.fixture(scope="module")
def lifecycle_enum(sv):
    enum = sv.get_enum(_ENUM)
    assert enum is not None, f"enum {_ENUM} is missing from {_SCHEMA}"
    return enum


# ---------------------------------------------------------------------------
# Enum shape
# ---------------------------------------------------------------------------


class TestLifecycleStatusEnum:
    """The enum exposes the expected values, in the expected workflow order."""

    def test_permissible_values_are_exactly_as_expected(self, lifecycle_enum):
        assert list(lifecycle_enum.permissible_values) == list(_EXPECTED_MEANINGS), (
            "LifecycleStatus values changed. Adding or removing a value is a breaking "
            "change for consumers -- update _EXPECTED_MEANINGS deliberately."
        )

    def test_every_value_has_a_description(self, lifecycle_enum):
        """Absent, empty and whitespace-only all count as undocumented.

        A blank ``description: |`` block still parses and still generates, so the
        emptiness has to be checked rather than the key's presence.
        """
        undocumented = [
            name
            for name, value in lifecycle_enum.permissible_values.items()
            if not (value.description or "").strip()
        ]
        assert not undocumented, f"permissible values missing a description: {undocumented}"


# ---------------------------------------------------------------------------
# Vocabulary alignment -- the part that silently rots
# ---------------------------------------------------------------------------


class TestLifecycleStatusVocabularyAlignment:
    """Permissible values expand to the URIs recorded in ``_EXPECTED_MEANINGS``.

    Those URIs were copied from ADMS and PSO by hand, and nothing here goes back to
    check them. So these tests won't notice if a term is renamed upstream -- only if
    the schema stops matching what we wrote down: a typo'd CURIE, a moved prefix,
    ``adms:`` where ``adms-status:`` belongs, a lost or duplicated meaning.

    Checking the upstream end stays a manual job. Update ``_EXPECTED_MEANINGS``
    when you do it.
    """

    @pytest.mark.parametrize("value,expected", sorted(_EXPECTED_MEANINGS.items()))
    def test_meaning_expands_to_expected_uri(self, sv, lifecycle_enum, value, expected):
        meaning = lifecycle_enum.permissible_values[value].meaning
        if expected is None:
            assert meaning is None, (
                f"{value} gained meaning {meaning!r}. It is intentionally unaligned: "
                "neither ADMS nor PSO defines a supersession status."
            )
        else:
            assert meaning is not None, f"{value} lost its meaning: CURIE"
            assert sv.expand_curie(meaning) == expected

    def test_no_meaning_lands_in_adms_vocabulary_namespace(self, sv, lifecycle_enum):
        """The ADMS vocabulary namespace holds no status values.

        ``http://www.w3.org/ns/adms#`` defines 4 classes (Asset, AssetDistribution,
        AssetRepository, Identifier) and 13 properties -- and no status concepts. A
        meaning of ``adms:Completed`` therefore points at a term that does not exist,
        and makes gen-owl coin it as an owl:Class in a namespace we do not own.
        Status values belong to the codelist at ``http://purl.org/adms/status/``.
        """
        offenders = {
            name: sv.expand_curie(value.meaning)
            for name, value in lifecycle_enum.permissible_values.items()
            if value.meaning and sv.expand_curie(value.meaning).startswith(_ADMS_VOCAB)
        }
        assert not offenders, (
            f"permissible values point into the ADMS *vocabulary* namespace: {offenders}. "
            f"Status values live in the codelist {_ADMS_CODELIST} -- use the "
            "'adms-status:' prefix, not 'adms:'."
        )

    def test_meanings_are_distinct(self, lifecycle_enum):
        """Two values sharing a meaning URI are indistinguishable in RDF."""
        meanings = [v.meaning for v in lifecycle_enum.permissible_values.values() if v.meaning]
        duplicates = {m for m in meanings if meanings.count(m) > 1}
        assert not duplicates, f"permissible values share a meaning: URI: {duplicates}"

    def test_superseded_is_close_mapped_not_exact(self, sv, lifecycle_enum):
        """SUPERSEDED records its ADMS relationship without claiming equivalence.

        ADMS collapses supersession into Deprecated, which DEPRECATED already claims
        exactly -- so this must stay a close_mapping. Promoting it to meaning: would
        make the two values identical in RDF (guarded by test_meanings_are_distinct).
        """
        superseded = lifecycle_enum.permissible_values["SUPERSEDED"]
        expanded = [sv.expand_curie(m) for m in superseded.close_mappings]
        assert expanded == [_ADMS_CODELIST + "Deprecated"], (
            f"SUPERSEDED close_mappings changed: {expanded}"
        )


# ---------------------------------------------------------------------------
# Slot wiring
# ---------------------------------------------------------------------------


class TestHasLifecycleStatusSlot:
    """The slot is wired to ADMS and reaches every catalogued entity."""

    def test_slot_uri_is_adms_status(self, sv):
        """adms:status *is* a real ADMS property -- unlike the value terms."""
        slot = sv.get_slot(_SLOT)
        assert slot is not None, f"slot {_SLOT} is missing from {_SCHEMA}"
        assert sv.get_uri(slot, expand=True) == _ADMS_VOCAB + "status"

    def test_range_is_the_lifecycle_enum(self, sv):
        assert sv.get_slot(_SLOT).range == _ENUM

    def test_slot_is_optional_and_single_valued(self, sv):
        """The slot was introduced as purely additive; requiring it would break data."""
        slot = sv.get_slot(_SLOT)
        assert not slot.required, f"{_SLOT} became required -- this breaks existing data"
        assert not slot.multivalued, f"{_SLOT} became multivalued -- an entity has one state"

    def test_declared_on_entity(self, sv):
        assert _SLOT in sv.class_slots("Entity")

    def test_inherited_by_every_entity_descendant(self, sv):
        """Declaring on the abstract base is what makes every entry status-able.

        Derived rather than hardcoded: a new subclass is covered the moment it is
        added, and a ``slot_usage`` that drops the slot on one subclass is caught.
        """
        missing = [
            class_name
            for class_name in sv.class_descendants("Entity", reflexive=False)
            if _SLOT not in sv.class_slots(class_name, direct=False)
        ]
        assert not missing, f"classes no longer inherit {_SLOT} from Entity: {missing}"

    def test_enum_range_survives_inheritance_everywhere(self, sv):
        """Inheritance must not erode the range to a bare string."""
        eroded = [
            class_name
            for class_name in sv.class_descendants("Entity", reflexive=False)
            if sv.induced_slot(_SLOT, class_name).range != _ENUM
        ]
        assert not eroded, f"{_SLOT} range is no longer {_ENUM} on: {eroded}"


# ---------------------------------------------------------------------------
# Prefixes
# ---------------------------------------------------------------------------


class TestLifecycleStatusPrefixes:
    """The two ADMS namespaces stay distinct."""

    @pytest.mark.parametrize(
        "prefix,expected",
        [("adms", _ADMS_VOCAB), ("adms-status", _ADMS_CODELIST), ("pso", _PSO)],
    )
    def test_prefix_resolves(self, sv, prefix, expected):
        namespaces = sv.namespaces()
        assert prefix in namespaces, f"prefix {prefix!r} is not declared"
        assert str(namespaces[prefix]) == expected

    def test_adms_and_adms_status_are_not_the_same_namespace(self, sv):
        namespaces = sv.namespaces()
        assert str(namespaces["adms"]) != str(namespaces["adms-status"]), (
            "The ADMS vocabulary and its status codelist are different namespaces; "
            "collapsing them reintroduces the fabricated-term bug."
        )
