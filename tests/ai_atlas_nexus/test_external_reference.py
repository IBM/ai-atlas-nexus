"""
Tests for the `hasExternalReference` slot and the `Documentation.isCategorizedAs`
narrowing added for https://github.com/IBM/ai-atlas-nexus/issues/181.

The modelled shape is:

    Entry/Control --hasExternalReference--> Documentation --isCategorizedAs--> Term

Both edges are `inlined: false`, so they are id references and each document is
declared exactly once in the Container however many records cite it.

`hasExternalReference` is declared on `Entry` and on `Control` rather than on the
root `Entity`: those two cover the catalogued domain concepts (risks, terms,
principles, controls, actions) without giving `License`, `Organization` or
`Dataset` a field they have no use for. The grouping label ("category") is a
catalogued `Term` rather than a free string, so labels are declared in one place
instead of being repeated as text in every record.

The fixture is transcribed from the FINOS AI Governance Framework records that
motivated the issue - risks ri-10 and ri-5, mitigation mi-3. Those two risks
genuinely cite the same BBC report, which the source lists under three different
titles; the fixture collapses it to one Documentation.
"""

# Standard
import os
from pathlib import Path

# Third party
import pytest
from linkml_runtime import SchemaView
from linkml_runtime.loaders import yaml_loader

# Internal
from src.ai_atlas_nexus.ai_risk_ontology.datamodel import ai_risk_ontology as datamodel
from src.ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    Container,
    Documentation,
    Risk,
)
from tests.base import TestCaseBase


SCHEMA_PATH = (
    Path(datamodel.__file__).resolve().parents[1] / "schema" / "ai-risk-ontology.yaml"
)


class TestExternalReference(TestCaseBase):
    """Tests for hasExternalReference and the Documentation.isCategorizedAs narrowing"""

    @classmethod
    def setUpClass(cls):
        cls.schema_view = SchemaView(str(SCHEMA_PATH))
        cls.container = yaml_loader.load_any(
            source=os.path.join(cls.fixtures_dir, "external_reference_data.yaml"),
            target_class=Container,
        )
        cls.entries = {entry.id: entry for entry in cls.container.entries}
        cls.actions = {action.id: action for action in cls.container.actions}
        cls.documents = {doc.id: doc for doc in cls.container.documents}

    def _induced(self, class_name):
        """Map of induced slot name -> slot definition for a class."""
        return {
            slot.name: slot for slot in self.schema_view.class_induced_slots(class_name)
        }

    ###############################################################################################
    #                                    Schema contract                                          #
    ###############################################################################################

    def test_documentation_class_uri_is_preserved(self):
        """issue #181 requires the airo:Documentation designation to survive the change"""
        self.assertEqual(
            self.schema_view.get_class("Documentation").class_uri, "airo:Documentation"
        )

    def test_documentation_aliases_include_external_reference(self):
        """The alias requested by issue #181 makes the pattern discoverable"""
        self.assertIn(
            "ExternalReference", self.schema_view.get_class("Documentation").aliases
        )

    def test_has_external_reference_slot_contract(self):
        """The slot points at Documentation by reference, not by inlining"""
        slot = self.schema_view.get_slot("hasExternalReference")
        self.assertEqual(slot.range, "Documentation")
        self.assertTrue(slot.multivalued)
        self.assertFalse(slot.inlined)
        self.assertEqual(slot.slot_uri, "nexus:hasExternalReference")
        self.assertIn("rdfs:seeAlso", slot.close_mappings)

    def test_has_external_reference_matches_has_documentation_inlining(self):
        """Both point at Documentation by id so references live once and deduplicate"""
        external = self.schema_view.get_slot("hasExternalReference")
        documentation = self.schema_view.get_slot("hasDocumentation")
        self.assertEqual(external.range, documentation.range)
        self.assertEqual(bool(external.inlined), bool(documentation.inlined))

    def test_has_external_reference_is_on_entry_and_control_not_entity(self):
        """Scoped to catalogued concepts, so License/Organization/Documentation do not grow a field"""
        # Entry side (FINOS risks) and Control side (FINOS mitigations).
        for class_name in ("Term", "Risk", "Action", "RiskControl"):
            self.assertIn(
                "hasExternalReference",
                self._induced(class_name),
                f"{class_name} should carry hasExternalReference",
            )
        for class_name in ("Documentation", "License", "Organization", "Dataset"):
            self.assertNotIn(
                "hasExternalReference",
                self._induced(class_name),
                f"{class_name} should not carry hasExternalReference",
            )

    def test_documentation_is_categorized_as_narrowed_to_term(self):
        """The grouping label is a catalogued Term rather than a free string"""
        self.assertEqual(self._induced("Documentation")["isCategorizedAs"].range, "Term")

    def test_is_categorized_as_narrowing_is_scoped_to_documentation(self):
        """Narrowing must not leak onto the schema-level slot or other classes"""
        self.assertEqual(self.schema_view.get_slot("isCategorizedAs").range, "Any")
        self.assertEqual(self._induced("Risk")["isCategorizedAs"].range, "Any")

    ###############################################################################################
    #                                       Test data                                             #
    ###############################################################################################

    def test_all_external_references_resolve_to_declared_documents(self):
        """Every referenced id must resolve to a Documentation declared in the Container"""
        citing = list(self.entries.values()) + list(self.actions.values())
        referenced = {
            reference_id
            for record in citing
            for reference_id in (record.hasExternalReference or [])
        }
        self.assertTrue(referenced, "fixture should exercise hasExternalReference")
        self.assertEqual(referenced - set(self.documents), set())

    def test_finos_risk_carries_its_links(self):
        """FINOS ri-10 "## Links" entries become hasExternalReference on a Risk"""
        risk = self.entries["finos:ri-10"]
        self.assertEqual(risk.name, "Prompt Injection")
        self.assertIn("finos:doc-owasp-llm-top-10", risk.hasExternalReference)
        self.assertEqual(
            self.documents["finos:doc-bbc-dpd-chatbot"].url,
            "https://www.bbc.co.uk/news/technology-68025677",
        )

    def test_finos_mitigation_carries_its_tooling_links(self):
        """FINOS mi-3 is an Action, which reaches the slot through Control rather than Entry"""
        action = self.actions["finos:mi-3"]
        self.assertEqual(action.name, "User/App/Model Firewalling/Filtering")
        self.assertEqual(
            action.hasExternalReference,
            [
                "finos:doc-llm-guard",
                "finos:doc-deberta-prompt-injection",
                "finos:doc-shieldlm",
            ],
        )

    def test_references_are_stored_once_and_cited_by_id(self):
        """inlined: false means citing records hold ids, so a document is stored in one place"""
        document_ids = [document.id for document in self.container.documents]
        self.assertEqual(
            len(document_ids), len(set(document_ids)), "documents must be unique"
        )
        for record in list(self.entries.values()) + list(self.actions.values()):
            for reference in record.hasExternalReference or []:
                self.assertIsInstance(
                    reference, str, "references are ids, not embedded objects"
                )

    def test_shared_reference_is_declared_once_with_one_name(self):
        """The BBC report is cited by ri-10 and ri-5; in FINOS it carries three
        different titles, here it is one Documentation with one canonical name."""
        citing = [
            record.id
            for record in list(self.entries.values()) + list(self.actions.values())
            if "finos:doc-bbc-dpd-chatbot" in (record.hasExternalReference or [])
        ]
        self.assertEqual(sorted(citing), ["finos:ri-10", "finos:ri-5"])
        self.assertEqual(
            [doc.id for doc in self.container.documents].count(
                "finos:doc-bbc-dpd-chatbot"
            ),
            1,
        )

    def test_categories_resolve_to_declared_terms(self):
        """'Tooling' is an id reference to a catalogued Term, not a repeated string"""
        category_ids = self.documents["finos:doc-llm-guard"].isCategorizedAs
        self.assertEqual(category_ids, ["nexus:extref-category-tooling"])
        self.assertEqual(self.entries[category_ids[0]].name, "Tooling")

    def test_category_is_multivalued(self):
        """One reference may carry several grouping labels"""
        category_ids = self.documents["finos:doc-arxiv-jailbreaking-llms"].isCategorizedAs
        self.assertEqual(
            [self.entries[category_id].name for category_id in category_ids],
            ["Links", "Tooling"],
        )

    def test_all_categories_resolve_to_declared_terms(self):
        """No document may point at a category that was never declared"""
        for document in self.container.documents:
            for category_id in document.isCategorizedAs or []:
                self.assertIn(category_id, self.entries)
                self.assertEqual(self.entries[category_id].type, "Term")

    ###############################################################################################
    #                                     Negative cases                                          #
    ###############################################################################################

    def test_documentation_rejects_external_reference_slot(self):
        """hasExternalReference hangs off Entry, so Documentation must reject it"""
        with pytest.raises(ValueError):
            Documentation(id="nexus:doc-x", hasExternalReference=["nexus:doc-y"])

    def test_narrowed_range_rejects_inline_object(self):
        """Documentation takes an id reference; Risk keeps the unnarrowed Any range"""
        with pytest.raises(ValueError):
            Documentation(id="nexus:doc-x", isCategorizedAs=[{"id": "nexus:term-y"}])

        # The same value is still accepted where isCategorizedAs was not narrowed.
        risk = Risk(id="nexus:risk-x", isCategorizedAs=[{"id": "nexus:term-y"}])
        self.assertEqual(risk.isCategorizedAs, [{"id": "nexus:term-y"}])
