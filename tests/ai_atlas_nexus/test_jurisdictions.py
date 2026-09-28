"""Jurisdiction enums expanded from the DPV Location vocabulary."""

import pydantic
import pytest
import rdflib
from linkml_runtime.utils.schemaview import SchemaView

from ai_atlas_nexus import AIAtlasNexus
from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    Documentation,
    Jurisdiction,
    SubnationalJurisdiction,
    SupraNationalJurisdiction,
)
from ai_atlas_nexus.ai_risk_ontology.util.expand_jurisdictions import build_schema


_SCHEMA = "src/ai_atlas_nexus/ai_risk_ontology/schema/ai-risk-ontology.yaml"

_LOC_SAMPLE = """
@prefix dpv: <https://w3id.org/dpv#> .
@prefix loc: <https://w3id.org/dpv/loc#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
loc:US a dpv:Country ; skos:prefLabel "United States of America"@en .
loc:US-CA a dpv:Region ; skos:prefLabel "California"@en .
loc:EU a dpv:SupraNationalUnion ; skos:prefLabel "European Union (EU)"@en .
"""


@pytest.mark.parametrize("code", ["US", "IE", "US-CA", "CA-QC", "EU", "EEA", "International"])
def test_valid_jurisdictions(code):
    assert Documentation(id="x", hasJurisdiction=[code]).hasJurisdiction == [code]


@pytest.mark.parametrize("code", ["XX", "us", "dpv-loc:EU", "https://w3id.org/dpv/loc#EU", "California"])
def test_invalid_jurisdictions(code):
    with pytest.raises(pydantic.ValidationError):
        Documentation(id="x", hasJurisdiction=[code])


def test_enum_sizes():
    assert len(Jurisdiction) == 249
    assert len(SubnationalJurisdiction) == 4757
    assert {j.value for j in SupraNationalJurisdiction} == {
        "EEA",
        "EEA30",
        "EEA31",
        "EU",
        "EU27",
        "EU28",
        "International",
    }


def test_enum_values_mean_dpv_loc():
    sv = SchemaView(_SCHEMA)
    for enum_name in ("Jurisdiction", "SupraNationalJurisdiction", "SubnationalJurisdiction"):
        for code, value in sv.get_enum(enum_name).permissible_values.items():
            if code != "International":
                assert value.meaning == f"dpv-loc:{code}", (enum_name, code)


def test_member_names_follow_codes():
    assert SubnationalJurisdiction.US_CA.value == "US-CA"
    assert Jurisdiction.US.value == "US"


def test_build_schema():
    graph = rdflib.Graph().parse(data=_LOC_SAMPLE, format="turtle")
    enums = build_schema(graph)["enums"]
    assert enums["Jurisdiction"]["permissible_values"] == {
        "US": {"meaning": "dpv-loc:US", "description": "United States of America"}
    }
    assert enums["SubnationalJurisdiction"]["permissible_values"] == {
        "US-CA": {"meaning": "dpv-loc:US-CA", "description": "California"}
    }
    assert set(enums["SupraNationalJurisdiction"]["permissible_values"]) == {"EU", "International"}


def test_legal_documents_have_jurisdiction():
    ran = AIAtlasNexus()
    assert ran.get_document(id="eu-gpai-cop-ss-appendix-3-5").hasJurisdiction == ["EU"]
    assert ran.get_document(id="ca-sb-53-22757-12-c-2-c").hasJurisdiction == ["US-CA"]
