from __future__ import annotations

import re
import sys
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Literal, Optional, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer,
)


metamodel_version = "None"
version = "0.5.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_curi_maps': ['semweb_context'],
     'default_prefix': 'nexus',
     'default_range': 'string',
     'description': 'An ontology describing AI systems and their risks',
     'id': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology',
     'imports': ['linkml:types',
                 'common',
                 'ai_risk',
                 'ai_capability',
                 'ai_system',
                 'ai_eval',
                 'ai_intrinsic',
                 'ai_csiro_rai'],
     'license': 'https://www.apache.org/licenses/LICENSE-2.0.html',
     'name': 'ai-risk-ontology',
     'prefixes': {'airo': {'prefix_prefix': 'airo',
                           'prefix_reference': 'https://w3id.org/airo#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nexus': {'prefix_prefix': 'nexus',
                            'prefix_reference': 'https://ibm.github.io/ai-atlas-nexus/ontology/'}},
     'settings': {'strict': {'setting_key': 'strict', 'setting_value': 'False'}},
     'source_file': 'src/ai_atlas_nexus/ai_risk_ontology/schema/ai-risk-ontology.yaml'} )

class AdapterType(str, Enum):
    LORA = "LORA"
    """
    Low-rank adapters, or LoRAs, are a fast way to give generalist large language models targeted knowledge and skills so they can do things like summarize IT manuals or rate the accuracy of their own answers. LoRA reduces the number of trainable parameters by learning pairs of rank-decompostion matrices while freezing the original weights. This vastly reduces the storage requirement for large language models adapted to specific tasks and enables efficient task-switching during deployment all without introducing inference latency. LoRA also outperforms several other adaptation methods including adapter, prefix-tuning, and fine-tuning. See arXiv:2106.09685
    """
    ALORA = "ALORA"
    """
    Activated LoRA (aLoRA) is a low rank adapter architecture that allows for reusing existing base model KV cache for more efficient inference, unlike standard LoRA models. As a result, aLoRA models can be quickly invoked as-needed for specialized tasks during (long) flows where the base model is primarily used, avoiding potentially expensive prefill costs in terms of latency, throughput, and GPU memory. See arXiv:2504.12397 for further details.
    """
    X_LORA = "X-LORA"
    """
    Mixture of LoRA Experts (X-LoRA) is a mixture of experts method for LoRA which works by using dense or sparse gating to dynamically activate LoRA experts.
    """


class EuAiRiskCategory(str, Enum):
    EXCLUDED = "EXCLUDED"
    """
    Excluded
    """
    PROHIBITED = "PROHIBITED"
    """
    Prohibited
    """
    HIGH_RISK_EXCEPTION = "HIGH_RISK_EXCEPTION"
    """
    High-Risk Exception
    """
    HIGH_RISK = "HIGH_RISK"
    """
    High Risk
    """
    LIMITED_OR_LOW_RISK = "LIMITED_OR_LOW_RISK"
    """
    Limited or Low Risk
    """


class AiSystemType(str, Enum):
    GPAI = "GPAI"
    """
    General-purpose AI (GPAI)
    """
    GPAI_OS = "GPAI_OS"
    """
    General-purpose AI (GPAI) models released under free and open-source licences
    """
    PROHIBITED = "PROHIBITED"
    """
    Prohibited AI system due to unacceptable risk category (e.g. social scoring systems and manipulative AI).
    """
    SCIENTIFIC_RD = "SCIENTIFIC_RD"
    """
    AI used for scientific research and development
    """
    MILITARY_SECURITY = "MILITARY_SECURITY"
    """
    AI used for military, defense and security purposes.
    """
    HIGH_RISK = "HIGH_RISK"
    """
    AI systems pursuant to Article 6(1)(2) Classification Rules for High-Risk AI Systems
    """



class Entity(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Organization(Entity):
    """
    Any organizational entity such as a corporation, educational institution, consortium, government, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Organization',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    grants_license: Optional[str] = Field(default=None, description="""A relationship from a granting entity such as an Organization to a License instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class License(Entity):
    """
    The general notion of a license which defines terms and grants permissions to users of AI systems, datasets and software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:License',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'Vocabulary', 'Taxonomy', 'RiskTaxonomy'],
         'slot_uri': 'schema:version'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Dataset(Entity):
    """
    A body of structured information describing some topic(s) of interest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Dataset',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    provider: Optional[str] = Field(default=None, description="""A relationship to the Organization instance that provides this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:provider'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Documentation(Entity):
    """
    Documented information about a concept or other topic(s) of interest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Documentation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    author: Optional[str] = Field(default=None, description="""The author or authors of the documentation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Documentation', 'RiskIncident']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Fact(ConfiguredBaseModel):
    """
    A fact about something, for example the result of a measurement. In addition to the value, evidence is provided.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Statement',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    value: str = Field(default=..., description="""Some numeric or string value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Fact']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Fact']} })


class Vocabulary(Entity):
    """
    A collection of terms, with their definitions and relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'Vocabulary', 'Taxonomy', 'RiskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["Vocabulary"] = Field(default="Vocabulary", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Taxonomy(Entity):
    """
    A hierachical taxonomy of concepts, with their definitions and relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'Vocabulary', 'Taxonomy', 'RiskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["Taxonomy"] = Field(default="Taxonomy", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Concept(Entity):
    """
    A concept
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'skos:Concept',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["Concept"] = Field(default="Concept", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Control(Entity):
    """
    A measure that maintains and/or modifies
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nexus:Control',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["Control"] = Field(default="Control", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Group(Entity):
    """
    Labelled groups of concepts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'skos:Collection',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasPart: Optional[list[str]] = Field(default=[], description="""A relationship where an entity has another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'RiskGroup', 'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'CapabilityGroup'], 'slot_uri': 'schema:isPartOf'} })
    type: Literal["Group"] = Field(default="Group", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy'],
         'ifabsent': 'string(Group)'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Entry(Entity):
    """
    An entry and its definitions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nexus:Entry',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["Entry"] = Field(default="Entry", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Term(Entry):
    """
    A term and its definitions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasParentDefinition: Optional[list[str]] = Field(default=[], description="""Indicates parent terms associated with a term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Term'], 'slot_uri': 'nexus:hasParentDefinition'} })
    hasSubDefinition: Optional[list[str]] = Field(default=[], description="""Indicates child terms associated with a term""", json_schema_extra = { "linkml_meta": {'domain_of': ['Term'], 'slot_uri': 'nexus:hasSubDefinition'} })
    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["Term"] = Field(default="Term", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Principle(Entry):
    """
    A representation of values or norms that must be taken into consideration when conducting activities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Principle',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["Principle"] = Field(default="Principle", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Policy(Entity):
    """
    A guidance document outlining any of: procedures, plans, principles, decisions, intent, or protocols.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Policy',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["Policy"] = Field(default="Policy", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class LLMQuestionPolicy(Policy):
    """
    The policy guides how the language model should answer a diverse set of sensitive questions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasRule: Optional[list[str]] = Field(default=[], description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LLMQuestionPolicy'], 'slot_uri': 'dpv:hasRule'} })
    hasReasonDenial: Optional[str] = Field(default=None, description="""Reason for denial""", json_schema_extra = { "linkml_meta": {'domain_of': ['LLMQuestionPolicy'], 'slot_uri': 'nexus:hasReasonDenial'} })
    hasShortReplyType: Optional[str] = Field(default=None, description="""Short reply type""", json_schema_extra = { "linkml_meta": {'domain_of': ['LLMQuestionPolicy'], 'slot_uri': 'nexus:hasShortReplyType'} })
    hasException: Optional[str] = Field(default=None, description="""Exception type""", json_schema_extra = { "linkml_meta": {'domain_of': ['LLMQuestionPolicy'], 'slot_uri': 'nexus:hasException'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["LLMQuestionPolicy"] = Field(default="LLMQuestionPolicy", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Rule(Entity):
    """
    A rule describing a process or control that directs or determines if and how an activity should be conducted.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Rule',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Permission(Rule):
    """
    A rule describing a permission to perform an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Permission',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Prohibition(Rule):
    """
    A rule describing a prohibition to perform an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Prohibition',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Obligation(Rule):
    """
    A rule describing an obligation for performing an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Obligation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class RiskTaxonomy(Taxonomy):
    """
    A taxonomy of AI system related risks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'Vocabulary', 'Taxonomy', 'RiskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["RiskTaxonomy"] = Field(default="RiskTaxonomy", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class RiskConcept(Concept):
    """
    An umbrella term for referring to risk, risk source, consequence and impact.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:RiskConcept',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixin': True})

    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["RiskConcept"] = Field(default="RiskConcept", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class RiskGroup(RiskConcept, Group):
    """
    A group of AI system related risks that are part of a risk taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept'],
         'slot_usage': {'hasPart': {'description': 'A relationship where a riskgroup '
                                                   'has a risk',
                                    'name': 'hasPart',
                                    'range': 'Risk'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[list[str]] = Field(default=[], description="""A relationship where a riskgroup has a risk""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'RiskGroup', 'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'CapabilityGroup'], 'slot_uri': 'schema:isPartOf'} })
    type: Literal["RiskGroup"] = Field(default="RiskGroup", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy'],
         'ifabsent': 'string(Group)'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Risk(RiskConcept, Entry):
    """
    The state of uncertainty associated with an AI system, that has the potential to cause harms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Risk',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept'],
         'slot_usage': {'isPartOf': {'description': 'A relationship where a risk is '
                                                    'part of a risk group',
                                     'name': 'isPartOf',
                                     'range': 'RiskGroup'}}})

    hasRelatedAction: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to an action""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a risk is part of a risk group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    detectsRiskConcept: Optional[list[str]] = Field(default=[], description="""The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskControl',
         'domain_of': ['Risk', 'RiskControl'],
         'exact_mappings': ['airo:detectsRiskConcept'],
         'inverse': 'isDetectedBy'} })
    tag: Optional[str] = Field(default=None, description="""A shost version of the name""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    risk_type: Optional[str] = Field(default=None, description="""Annotation whether an AI risk occurs at input or output or is non-technical.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    phase: Optional[str] = Field(default=None, description="""Annotation whether an AI risk shows specifically during the training-tuning or inference phase.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    descriptor: Optional[list[str]] = Field(default=[], description="""Annotates whether an AI risk is a traditional risk, specific to or amplified by AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    concern: Optional[str] = Field(default=None, description="""Some explanation about the concern related to an AI risk""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk']} })
    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["Risk"] = Field(default="Risk", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class RiskControl(RiskConcept, Control):
    """
    A measure that maintains and/or modifies risk (and risk concepts)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:RiskControl',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixin': True,
         'mixins': ['RiskConcept']})

    detectsRiskConcept: Optional[list[str]] = Field(default=[], description="""The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskControl',
         'domain_of': ['Risk', 'RiskControl'],
         'exact_mappings': ['airo:detectsRiskConcept'],
         'inverse': 'isDetectedBy'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    type: Literal["RiskControl"] = Field(default="RiskControl", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })


class Action(RiskControl):
    """
    Action to remediate a risk
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasAiActorTask: Optional[list[str]] = Field(default=[], description="""Pertinent AI Actor Tasks for each subcategory. Not every AI Actor Task listed will apply to every suggested action in the subcategory (i.e., some apply to AI development and others apply to AI deployment).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Action']} })
    detectsRiskConcept: Optional[list[str]] = Field(default=[], description="""The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskControl',
         'domain_of': ['Risk', 'RiskControl'],
         'exact_mappings': ['airo:detectsRiskConcept'],
         'inverse': 'isDetectedBy'} })
    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    type: Literal["Action"] = Field(default="Action", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class RiskIncident(RiskConcept, Entity):
    """
    An event occuring or occured which is a realised or materialised risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'https://w3id.org/dpv/risk#Incident',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept']})

    refersToRisk: Optional[list[str]] = Field(default=[], description="""Indicates the incident (subject) is a materialisation of the indicated risk (object)""", json_schema_extra = { "linkml_meta": {'domain': 'RiskIncident',
         'domain_of': ['RiskIncident'],
         'exact_mappings': ['dpv:refersToRisk']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasStatus: Optional[str] = Field(default=None, description="""Indicates the status of specified concept""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept', 'domain_of': ['RiskIncident']} })
    hasSeverity: Optional[str] = Field(default=None, description="""Indicates the severity associated with a concept""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept', 'domain_of': ['RiskIncident']} })
    hasLikelihood: Optional[str] = Field(default=None, description="""The likelihood or probability or chance of something taking place or occuring""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept', 'domain_of': ['RiskIncident']} })
    hasImpactOn: Optional[str] = Field(default=None, description="""Indicates impact(s) possible or arising as consequences from specified concept""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dpv:hasConsequenceOn'],
         'domain': 'RiskConcept',
         'domain_of': ['RiskIncident']} })
    hasConsequence: Optional[str] = Field(default=None, description="""Indicates consequence(s) possible or arising from specified concept""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept', 'domain_of': ['RiskIncident']} })
    hasImpact: Optional[str] = Field(default=None, description="""Indicates impact(s) possible or arising as consequences from specified concept""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['dpv:hasConsequence'],
         'domain': 'RiskConcept',
         'domain_of': ['RiskIncident']} })
    hasVariant: Optional[str] = Field(default=None, description="""Indicates an incident that shares the same causative factors, produces similar harms, and involves the same intelligent systems as a known AI incident.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskIncident', 'domain_of': ['RiskIncident']} })
    author: Optional[str] = Field(default=None, description="""The author or authors of the incident report""", json_schema_extra = { "linkml_meta": {'domain_of': ['Documentation', 'RiskIncident']} })
    source_uri: Optional[str] = Field(default=None, description="""The uri of the incident""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskIncident']} })
    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["RiskIncident"] = Field(default="RiskIncident", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })


class Impact(RiskConcept, Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Impact',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept']})

    isDetectedBy: Optional[list[str]] = Field(default=[], description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["Impact"] = Field(default="Impact", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })


class IncidentStatus(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentStatus',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class IncidentConcludedclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentConcludedclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class IncidentHaltedclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentHaltedclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class IncidentMitigatedclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentMitigatedclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class IncidentNearMissclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentNearMissclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class IncidentOngoingclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentOngoingclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Severity(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Severity',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Likelihood(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Likelihood',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Consequence(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Consequence',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class BaseAi(Entity):
    """
    Any type of AI, be it a LLM, RL agent, SVM, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasModelCard: Optional[list[str]] = Field(default=[], description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[list[str]] = Field(default=[], description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI model has been provided by an AI model provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi'], 'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiSystem(BaseAi):
    """
    A compound AI System composed of one or more AI capablities. ChatGPT is an example of an AI system which deploys multiple GPT AI models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AISystem',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'slot_usage': {'isComposedOf': {'description': 'Relationship indicating the '
                                                        'AI components from which a '
                                                        'complete AI system is '
                                                        'composed.',
                                         'name': 'isComposedOf',
                                         'range': 'BaseAi'}}})

    hasEuAiSystemType: Optional[AiSystemType] = Field(default=None, description="""The type of system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem']} })
    hasEuRiskCategory: Optional[EuAiRiskCategory] = Field(default=None, description="""The risk category of an AI system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem']} })
    hasCapability: Optional[list[str]] = Field(default=[], description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasModelCard: Optional[list[str]] = Field(default=[], description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[list[str]] = Field(default=[], description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI model has been provided by an AI model provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi'], 'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiAgent(AiSystem):
    """
    An artificial intelligence (AI) agent refers to a system or program that is capable of autonomously performing tasks on behalf of a user or another system by designing its workflow and utilizing available tools.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'mixin': True,
         'slot_usage': {'isProvidedBy': {'description': 'A relationship indicating the '
                                                        'AI agent has been provided by '
                                                        'an AI systems provider.',
                                         'name': 'isProvidedBy'}}})

    hasEuAiSystemType: Optional[AiSystemType] = Field(default=None, description="""The type of system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem']} })
    hasEuRiskCategory: Optional[EuAiRiskCategory] = Field(default=None, description="""The risk category of an AI system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem']} })
    hasCapability: Optional[list[str]] = Field(default=[], description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasModelCard: Optional[list[str]] = Field(default=[], description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[list[str]] = Field(default=[], description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI agent has been provided by an AI systems provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi'], 'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiModel(BaseAi):
    """
    A base AI Model class. No assumption about the type (SVM, LLM, etc.). Subclassed by model types (see LargeLanguageModel).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'mixin': True})

    hasEvaluation: Optional[list[str]] = Field(default=[], description="""A relationship indicating that an entity has an AI evaluation result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'], 'slot_uri': 'dqv:hasQualityMeasurement'} })
    architecture: Optional[str] = Field(default=None, description="""A description of the architecture of an AI such as 'Decoder-only'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    gpu_hours: Optional[int] = Field(default=None, description="""GPU consumption in terms of hours""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    power_consumption_w: Optional[int] = Field(default=None, description="""power consumption in Watts""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    carbon_emitted: Optional[float] = Field(default=None, description="""The number of tons of carbon dioxide equivalent that are emitted during training""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'],
         'unit': {'descriptive_name': 'tons of CO2 equivalent', 'symbol': 't CO2-eq'}} })
    hasRiskControl: Optional[list[str]] = Field(default=[], description="""Indicates the control measures associated with a system or component to modify risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'], 'slot_uri': 'airo:hasRiskControl'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasModelCard: Optional[list[str]] = Field(default=[], description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[list[str]] = Field(default=[], description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI model has been provided by an AI model provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi'], 'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class LargeLanguageModel(AiModel):
    """
    A large language model (LLM) is an AI model which supports a range of language-related tasks such as generation, summarization, classification, among others. A LLM is implemented as an artificial neural networks using a transformer architecture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['LLM'],
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'mixin': True,
         'slot_usage': {'isPartOf': {'description': 'Annotation that a Large Language '
                                                    'model is part of a family of '
                                                    'models',
                                     'name': 'isPartOf',
                                     'range': 'LargeLanguageModelFamily'}}})

    numParameters: Optional[int] = Field(default=None, description="""A property indicating the number of parameters in a LLM.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    numTrainingTokens: Optional[int] = Field(default=None, description="""The number of tokens a AI model was trained on.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    contextWindowSize: Optional[int] = Field(default=None, description="""The total length, in bytes, of an AI model's context window.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    hasInputModality: Optional[list[str]] = Field(default=[], description="""A relationship indicating the input modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    hasOutputModality: Optional[list[str]] = Field(default=[], description="""A relationship indicating the output modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    hasTrainingData: Optional[list[str]] = Field(default=[], description="""A relationship indicating the datasets an AI model was trained on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel'], 'slot_uri': 'airo:hasTrainingData'} })
    fine_tuning: Optional[str] = Field(default=None, description="""A description of the fine-tuning mechanism(s) applied to a model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    supported_languages: Optional[list[str]] = Field(default=[], description="""A list of languages, expressed as ISO two letter codes. For example, 'jp, fr, en, de'""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    isPartOf: Optional[str] = Field(default=None, description="""Annotation that a Large Language model is part of a family of models""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    hasEvaluation: Optional[list[str]] = Field(default=[], description="""A relationship indicating that an entity has an AI evaluation result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'], 'slot_uri': 'dqv:hasQualityMeasurement'} })
    architecture: Optional[str] = Field(default=None, description="""A description of the architecture of an AI such as 'Decoder-only'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    gpu_hours: Optional[int] = Field(default=None, description="""GPU consumption in terms of hours""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    power_consumption_w: Optional[int] = Field(default=None, description="""power consumption in Watts""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    carbon_emitted: Optional[float] = Field(default=None, description="""The number of tons of carbon dioxide equivalent that are emitted during training""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'],
         'unit': {'descriptive_name': 'tons of CO2 equivalent', 'symbol': 't CO2-eq'}} })
    hasRiskControl: Optional[list[str]] = Field(default=[], description="""Indicates the control measures associated with a system or component to modify risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'], 'slot_uri': 'airo:hasRiskControl'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasModelCard: Optional[list[str]] = Field(default=[], description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[list[str]] = Field(default=[], description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI model has been provided by an AI model provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi'], 'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class LargeLanguageModelFamily(Entity):
    """
    A large language model family is a set of models that are provided by the same AI systems provider and are built around the same architecture, but differ e.g. in the number of parameters. Examples are Meta's Llama2 family or the IBM granite models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiTask(Entry):
    """
    A task, such as summarization and classification, performed by an AI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AiCapability',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["AiTask"] = Field(default="AiTask", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiLifecyclePhase(Entity):
    """
    A Phase of AI lifecycle which indicates evolution of the system from conception through retirement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'airo:AILifecyclePhase',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class DataPreprocessing(AiLifecyclePhase):
    """
    Data transformations, such as PI filtering, performed to ensure high quality of AI model training data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiModelValidation(AiLifecyclePhase):
    """
    AI model validation steps that have been performed after the model training to ensure high AI model quality.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiProvider(Organization):
    """
    A provider under the AI Act is defined by Article 3(3) as a natural or legal person or body that develops an AI system or general-purpose AI model or has an AI system or general-purpose AI model developed; and places that system or model on the market, or puts that system into service, under the provider's own name or trademark, whether for payment or free for charge.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIProvider',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    grants_license: Optional[str] = Field(default=None, description="""A relationship from a granting entity such as an Organization to a License instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Modality(Entity):
    """
    A modality supported by an Ai component. Examples include text, image, video.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Modality',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Input(Entity):
    """
    Input for which the system or component generates output.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Input',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class CapabilityTaxonomy(Taxonomy):
    """
    A taxonomy of AI capabilities describing the abilities of AI systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['License', 'Vocabulary', 'Taxonomy', 'RiskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["CapabilityTaxonomy"] = Field(default="CapabilityTaxonomy", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class CapabilityConcept(Concept):
    """
    An umbrella term for referring to capability domains, groups, and individual capabilities..
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:CapabilityConcept',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["CapabilityConcept"] = Field(default="CapabilityConcept", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class CapabilityDomain(CapabilityConcept, Group):
    """
    A high-level domain of AI capabilities (e.g., Language, Reasoning, Knowledge)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:CapabilityDomain',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability',
         'mixins': ['CapabilityConcept'],
         'slot_usage': {'hasPart': {'description': 'A relationship where a capability '
                                                   'domain has capability groups',
                                    'name': 'hasPart',
                                    'range': 'CapabilityGroup'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasPart: Optional[list[str]] = Field(default=[], description="""A relationship where a capability domain has capability groups""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'RiskGroup', 'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'CapabilityGroup'], 'slot_uri': 'schema:isPartOf'} })
    type: Literal["CapabilityDomain"] = Field(default="CapabilityDomain", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy'],
         'ifabsent': 'string(Group)'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class CapabilityGroup(CapabilityConcept, Group):
    """
    A group of AI capabilities that are part of a capability taxonomy, organized under a domain
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability',
         'mixins': ['CapabilityConcept'],
         'slot_usage': {'belongsToDomain': {'description': 'A relationship where a '
                                                           'capability group belongs '
                                                           'to a capability domain',
                                            'name': 'belongsToDomain',
                                            'range': 'CapabilityDomain'},
                        'hasPart': {'description': 'A relationship where a capability '
                                                   'group has capabilities',
                                    'name': 'hasPart',
                                    'range': 'Capability'},
                        'isPartOf': {'description': 'A relationship where a capability '
                                                    'group belongs to a capability '
                                                    'domain',
                                     'name': 'isPartOf',
                                     'range': 'CapabilityDomain'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a capability group belongs to a capability domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[list[str]] = Field(default=[], description="""A relationship where a capability group has capabilities""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'RiskGroup', 'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[str] = Field(default=None, description="""A relationship where a capability group belongs to a capability domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'CapabilityGroup'], 'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["CapabilityGroup"] = Field(default="CapabilityGroup", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy'],
         'ifabsent': 'string(Group)'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Capability(CapabilityConcept, Entry):
    """
    A specific AI capability or ability, such as reading comprehension, logical reasoning, or code generation. Aligned with the W3C DPV AI extension dpv-ai:Capability, representing what an AI technology is capable of achieving or providing. Capabilities are distinct from: (1) the intended purpose for which the technology is designed, (2) the actual tasks performed in a specific deployment context, and (3) the technical implementation mechanisms (intrinsics, adapters) that enable the capability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['tech:Capability'],
         'class_uri': 'ai:Capability',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability',
         'mixins': ['CapabilityConcept'],
         'slot_usage': {'implementedByAdapter': {'description': 'Indicates that this '
                                                                'capability is '
                                                                'implemented by a '
                                                                'specific adapter. '
                                                                'This relationship '
                                                                'distinguishes the '
                                                                'abstract capability '
                                                                '(what can be done) '
                                                                'from the technical '
                                                                'implementation '
                                                                'mechanism (how it is '
                                                                'added/extended via '
                                                                'adapters).',
                                                 'domain': 'Capability',
                                                 'name': 'implementedByAdapter',
                                                 'range': 'Adapter'},
                        'isPartOf': {'description': 'A relationship where a capability '
                                                    'is part of a capability group',
                                     'name': 'isPartOf',
                                     'range': 'CapabilityGroup'},
                        'requiredByTask': {'description': 'Indicates that this '
                                                          'capability is required to '
                                                          'perform a specific AI task. '
                                                          'This links abstract '
                                                          'capabilities (technical '
                                                          'abilities) to concrete '
                                                          'tasks (application-level '
                                                          'operations). An AI system '
                                                          'with this capability can '
                                                          'perform tasks that require '
                                                          'it.',
                                           'name': 'requiredByTask',
                                           'range': 'AiTask'}}})

    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is required to perform a specific AI task. This links abstract capabilities (technical abilities) to concrete tasks (application-level operations). An AI system with this capability can perform tasks that require it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'domain': 'Capability',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a capability is part of a capability group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    type: Literal["Capability"] = Field(default="Capability", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiEval(Entity):
    """
    An AI Evaluation, e.g. a metric, benchmark, unitxt card evaluation, a question or a combination of such entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dqv:Metric',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval',
         'slot_usage': {'isComposedOf': {'description': 'A relationship indicating '
                                                        'that an AI evaluation maybe '
                                                        'composed of other AI '
                                                        "evaluations (e.g. it's an "
                                                        'overall average of other '
                                                        'scores).',
                                         'name': 'isComposedOf',
                                         'range': 'AiEval'}}})

    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasDataset: Optional[list[str]] = Field(default=[], description="""A relationship to datasets that are used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval']} })
    hasTasks: Optional[list[str]] = Field(default=[], description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval', 'BenchmarkMetadataCard']} })
    hasImplementation: Optional[list[str]] = Field(default=[], description="""A relationship to a implementation defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasUnitxtCard: Optional[list[str]] = Field(default=[], description="""A relationship to a Unitxt card defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    bestValue: Optional[str] = Field(default=None, description="""Annotation of the best possible result of the evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval']} })
    hasBenchmarkMetadata: Optional[list[str]] = Field(default=[], description="""A relationship to a Benchmark Metadata Card which contains metadata about the benchmark.""", json_schema_extra = { "linkml_meta": {'domain': 'AiEval', 'domain_of': ['AiEval'], 'inverse': 'describesAiEval'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiEvalResult(Fact, Entity):
    """
    The result of an evaluation for a specific AI model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dqv:QualityMeasurement',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval',
         'mixins': ['Fact']})

    isResultOf: Optional[str] = Field(default=None, description="""A relationship indicating that an entity is the result of an AI evaluation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEvalResult'], 'slot_uri': 'dqv:isMeasurementOf'} })
    value: str = Field(default=..., description="""Some numeric or string value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Fact']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Fact']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class BenchmarkMetadataCard(Entity):
    """
    Benchmark metadata cards offer a standardized way to document LLM benchmarks clearly and transparently. Inspired by Model Cards and Datasheets, Benchmark metadata cards help researchers and practitioners understand exactly what benchmarks test, how they relate to real-world risks, and how to interpret their results responsibly.  This is an implementation of the design set out in 'BenchmarkCards: Large Language Model and Risk Reporting' (https://doi.org/10.48550/arXiv.2410.12974)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:benchmarkmetadatacard',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    describesAiEval: Optional[list[str]] = Field(default=[], description="""A relationship where a BenchmarkMetadataCard describes and AI evaluation (benchmark).""", json_schema_extra = { "linkml_meta": {'domain': 'BenchmarkMetadataCard',
         'domain_of': ['BenchmarkMetadataCard'],
         'inverse': 'hasBenchmarkMetadata'} })
    hasDataType: Optional[list[str]] = Field(default=[], description="""The type of data used in the benchmark (e.g., text, images, or multi-modal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasDomains: Optional[list[str]] = Field(default=[], description="""The specific domains or areas where the benchmark is applied (e.g., natural language processing,computer vision).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasLanguages: Optional[list[str]] = Field(default=[], description="""The languages included in the dataset used by the benchmark (e.g., English, multilingual).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasSimilarBenchmarks: Optional[list[str]] = Field(default=[], description="""Benchmarks that are closely related in terms of goals or data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasResources: Optional[list[str]] = Field(default=[], description="""Links to relevant resources, such as repositories or papers related to the benchmark.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasGoal: Optional[str] = Field(default=None, description="""The specific goal or primary use case the benchmark is designed for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasAudience: Optional[str] = Field(default=None, description="""The intended audience, such as researchers, developers, policymakers, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasTasks: Optional[list[str]] = Field(default=[], description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval', 'BenchmarkMetadataCard']} })
    hasLimitations: Optional[list[str]] = Field(default=[], description="""Limitations in evaluating or addressing risks, such as gaps in demographic coverage or specific domains.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasOutOfScopeUses: Optional[list[str]] = Field(default=[], description="""Use cases where the benchmark is not designed to be applied and could give misleading results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasDataSource: Optional[list[str]] = Field(default=[], description="""The origin or source of the data used in the benchmark (e.g., curated datasets, user submissions).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasDataSize: Optional[str] = Field(default=None, description="""The size of the dataset, including the number of data points or examples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasDataFormat: Optional[str] = Field(default=None, description="""The structure and modality of the data (e.g., sentence pairs, question-answer format, tabular data).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasAnnotation: Optional[str] = Field(default=None, description="""The process used to annotate or label the dataset, including who or what performed the annotations (e.g., human annotators, automated processes).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasMethods: Optional[list[str]] = Field(default=[], description="""The evaluation techniques applied within the benchmark.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasMetrics: Optional[list[str]] = Field(default=[], description="""The specific performance metrics used to assess models (e.g., accuracy, F1 score, precision, recall).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasCalculation: Optional[list[str]] = Field(default=[], description="""The way metrics are computed based on model outputs and the benchmark data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasInterpretation: Optional[list[str]] = Field(default=[], description="""How users should interpret the scores or results from the metrics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasBaselineResults: Optional[str] = Field(default=None, description="""The results of well-known or widely used models to give context to new performance scores.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasValidation: Optional[list[str]] = Field(default=[], description="""Measures taken to ensure that the benchmark provides valid and reliable evaluations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasDemographicAnalysis: Optional[str] = Field(default=None, description="""How the benchmark evaluates performance across different demographic groups (e.g., gender, race).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasConsiderationPrivacyAndAnonymity: Optional[str] = Field(default=None, description="""How any personal or sensitive data is handled and whether any anonymization techniques are applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasConsiderationConsentProcedures: Optional[str] = Field(default=None, description="""Information on how consent was obtained (if applicable), especially for datasets involving personal data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasConsiderationComplianceWithRegulations: Optional[str] = Field(default=None, description="""Compliance with relevant legal or ethical regulations (if applicable).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    name: Optional[str] = Field(default=None, description="""The official name of the benchmark.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard']} })
    overview: Optional[str] = Field(default=None, description="""A brief description of the benchmark's main goals and scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BenchmarkMetadataCard']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Question(AiEval):
    """
    An evaluation where a question has to be answered
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    text: str = Field(default=..., description="""The question itself""", json_schema_extra = { "linkml_meta": {'domain_of': ['Question']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasDataset: Optional[list[str]] = Field(default=[], description="""A relationship to datasets that are used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval']} })
    hasTasks: Optional[list[str]] = Field(default=[], description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval', 'BenchmarkMetadataCard']} })
    hasImplementation: Optional[list[str]] = Field(default=[], description="""A relationship to a implementation defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasUnitxtCard: Optional[list[str]] = Field(default=[], description="""A relationship to a Unitxt card defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    bestValue: Optional[str] = Field(default=None, description="""Annotation of the best possible result of the evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval']} })
    hasBenchmarkMetadata: Optional[list[str]] = Field(default=[], description="""A relationship to a Benchmark Metadata Card which contains metadata about the benchmark.""", json_schema_extra = { "linkml_meta": {'domain': 'AiEval', 'domain_of': ['AiEval'], 'inverse': 'describesAiEval'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Questionnaire(AiEval):
    """
    A questionnaire groups questions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval',
         'slot_usage': {'composed_of': {'name': 'composed_of', 'range': 'Question'}}})

    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasDataset: Optional[list[str]] = Field(default=[], description="""A relationship to datasets that are used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval']} })
    hasTasks: Optional[list[str]] = Field(default=[], description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval', 'BenchmarkMetadataCard']} })
    hasImplementation: Optional[list[str]] = Field(default=[], description="""A relationship to a implementation defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasUnitxtCard: Optional[list[str]] = Field(default=[], description="""A relationship to a Unitxt card defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    bestValue: Optional[str] = Field(default=None, description="""Annotation of the best possible result of the evaluation""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiEval']} })
    hasBenchmarkMetadata: Optional[list[str]] = Field(default=[], description="""A relationship to a Benchmark Metadata Card which contains metadata about the benchmark.""", json_schema_extra = { "linkml_meta": {'domain': 'AiEval', 'domain_of': ['AiEval'], 'inverse': 'describesAiEval'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Adapter(LargeLanguageModel, Entry):
    """
    Adapter-based methods add extra trainable parameters after the attention and fully-connected layers of a frozen pretrained model to reduce memory-usage and speed up training. The adapters are typically small but demonstrate comparable performance to a fully finetuned model and enable training larger models with fewer resources. (https://huggingface.co/docs/peft/en/conceptual_guides/adapter)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_intrinsic',
         'mixins': ['LargeLanguageModel']})

    hasAdapterType: Optional[AdapterType] = Field(default=None, description="""The Adapter type, for example: LORA, ALORA, X-LORA""", json_schema_extra = { "linkml_meta": {'domain_of': ['Adapter']} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'BaseAi',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    adaptsModel: Optional[str] = Field(default=None, description="""The LargeLanguageModel being adapted""", json_schema_extra = { "linkml_meta": {'domain_of': ['Adapter']} })
    implementsCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this intrinsic implements a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'LLMIntrinsic',
         'domain_of': ['Adapter'],
         'inverse': 'implementedByIntrinsic'} })
    hasCapability: Optional[list[str]] = Field(default=[], description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    numParameters: Optional[int] = Field(default=None, description="""A property indicating the number of parameters in a LLM.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    numTrainingTokens: Optional[int] = Field(default=None, description="""The number of tokens a AI model was trained on.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    contextWindowSize: Optional[int] = Field(default=None, description="""The total length, in bytes, of an AI model's context window.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    hasInputModality: Optional[list[str]] = Field(default=[], description="""A relationship indicating the input modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    hasOutputModality: Optional[list[str]] = Field(default=[], description="""A relationship indicating the output modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    hasTrainingData: Optional[list[str]] = Field(default=[], description="""A relationship indicating the datasets an AI model was trained on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel'], 'slot_uri': 'airo:hasTrainingData'} })
    fine_tuning: Optional[str] = Field(default=None, description="""A description of the fine-tuning mechanism(s) applied to a model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    supported_languages: Optional[list[str]] = Field(default=[], description="""A list of languages, expressed as ISO two letter codes. For example, 'jp, fr, en, de'""", json_schema_extra = { "linkml_meta": {'domain_of': ['LargeLanguageModel']} })
    isPartOf: Optional[str] = Field(default=None, description="""Annotation that a Large Language model is part of a family of models""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["Adapter"] = Field(default="Adapter", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })
    hasEvaluation: Optional[list[str]] = Field(default=[], description="""A relationship indicating that an entity has an AI evaluation result.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'], 'slot_uri': 'dqv:hasQualityMeasurement'} })
    architecture: Optional[str] = Field(default=None, description="""A description of the architecture of an AI such as 'Decoder-only'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    gpu_hours: Optional[int] = Field(default=None, description="""GPU consumption in terms of hours""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    power_consumption_w: Optional[int] = Field(default=None, description="""power consumption in Watts""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel']} })
    carbon_emitted: Optional[float] = Field(default=None, description="""The number of tons of carbon dioxide equivalent that are emitted during training""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'],
         'unit': {'descriptive_name': 'tons of CO2 equivalent', 'symbol': 't CO2-eq'}} })
    hasRiskControl: Optional[list[str]] = Field(default=[], description="""Indicates the control measures associated with a system or component to modify risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiModel'], 'slot_uri': 'airo:hasRiskControl'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    hasModelCard: Optional[list[str]] = Field(default=[], description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    performsTask: Optional[list[str]] = Field(default=[], description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI model has been provided by an AI model provider.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BaseAi'], 'slot_uri': 'airo:isProvidedBy'} })


class LLMIntrinsic(Entry):
    """
    A capability that can be invoked through a well-defined API that is reasonably stable and independent of how the LLM intrinsic itself is implemented.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ai:Capability',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_intrinsic'})

    hasRelatedRisk: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasRelatedTerm: Optional[list[str]] = Field(default=[], description="""A relationship where an entity relates to a term""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['LLMIntrinsic']} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasAdapter: Optional[list[str]] = Field(default=[], description="""The Adapter for the intrinsic""", json_schema_extra = { "linkml_meta": {'domain': 'LLMIntrinsic', 'domain_of': ['LLMIntrinsic']} })
    hasCapability: Optional[list[str]] = Field(default=[], description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[list[str]] = Field(default=[], description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry', 'Capability'], 'inverse': 'requiresCapability'} })
    requiresCapability: Optional[list[str]] = Field(default=[], description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[list[str]] = Field(default=[], description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).
""", json_schema_extra = { "linkml_meta": {'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    type: Literal["LLMIntrinsic"] = Field(default="LLMIntrinsic", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class AiOffice(Organization):
    """
    The EU AI Office (https://digital-strategy.ec.europa.eu/en/policies/ai-office)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Organization',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/eu_ai_act'})

    grants_license: Optional[str] = Field(default=None, description="""A relationship from a granting entity such as an Organization to a License instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class StakeholderGroup(Group):
    """
    An AI system stakeholder grouping.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_csiro_rai'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[list[str]] = Field(default=[], description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasPart: Optional[list[str]] = Field(default=[], description="""A relationship where an entity has another entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'RiskGroup', 'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Group', 'CapabilityGroup'], 'slot_uri': 'schema:isPartOf'} })
    type: Literal["StakeholderGroup"] = Field(default="StakeholderGroup", json_schema_extra = { "linkml_meta": {'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy'],
         'ifabsent': 'string(Group)'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Stakeholder(Entity):
    """
    An AI system stakeholder for Responsible AI governance (e.g., AI governors, users, consumers).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_csiro_rai',
         'slot_usage': {'isPartOf': {'description': 'A relationship where a '
                                                    'stakeholder is part of a '
                                                    'stakeholder group',
                                     'name': 'isPartOf',
                                     'range': 'StakeholderGroup'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'CapabilityGroup',
                       'StakeholderGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'CapabilityGroup',
                       'Stakeholder'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity', 'BenchmarkMetadataCard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[list[Any]] = Field(default=[], description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[list[Any]] = Field(default=[], description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Entity'], 'slot_uri': 'skos:broadMatch'} })


class Container(ConfiguredBaseModel):
    """
    An umbrella object that holds the ontology class instances
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology',
         'tree_root': True})

    organizations: Optional[list[Organization]] = Field(default=[], description="""A list of organizations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    licenses: Optional[list[License]] = Field(default=[], description="""A list of licenses""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    modalities: Optional[list[Modality]] = Field(default=[], description="""A list of AI modalities""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aitasks: Optional[list[AiTask]] = Field(default=[], description="""A list of AI tasks""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    documents: Optional[list[Documentation]] = Field(default=[], description="""A list of documents""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    datasets: Optional[list[Dataset]] = Field(default=[], description="""A list of data sets""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    llmintrinsics: Optional[list[LLMIntrinsic]] = Field(default=[], description="""A list of LLMIntrinsics""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    adapters: Optional[list[Adapter]] = Field(default=[], description="""A list of Adapters""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    taxonomies: Optional[list[Union[Taxonomy,RiskTaxonomy,CapabilityTaxonomy]]] = Field(default=[], description="""A list of taxonomies""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    concepts: Optional[list[Union[Concept,RiskConcept,CapabilityConcept,CapabilityDomain,CapabilityGroup,Capability,RiskGroup,Risk,RiskControl,RiskIncident,Impact,Action]]] = Field(default=[], description="""A list of concepts""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    entries: Optional[list[Union[Entry,Term,Principle,Risk,AiTask,Capability,Adapter,LLMIntrinsic]]] = Field(default=[], description="""A list of entries""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    groups: Optional[list[Union[Group,RiskGroup,CapabilityDomain,CapabilityGroup,StakeholderGroup]]] = Field(default=[], description="""A list of groups""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    vocabularies: Optional[list[Vocabulary]] = Field(default=[], description="""A list of vocabularies""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    controls: Optional[list[Union[Control,RiskControl,Action]]] = Field(default=[], description="""A list of AI controls""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    riskincidents: Optional[list[RiskIncident]] = Field(default=[], description="""A list of AI risk incidents""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    stakeholdergroups: Optional[list[StakeholderGroup]] = Field(default=[], description="""A list of AI stakeholder groups""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    stakeholders: Optional[list[Stakeholder]] = Field(default=[], description="""A list of stakeholders""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    actions: Optional[list[Action]] = Field(default=[], description="""A list of risk related actions""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    evaluations: Optional[list[AiEval]] = Field(default=[], description="""A list of AI evaluation methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aievalresults: Optional[list[AiEvalResult]] = Field(default=[], description="""A list of AI evaluation results""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    benchmarkmetadatacards: Optional[list[BenchmarkMetadataCard]] = Field(default=[], description="""A list of AI evaluation benchmark metadata cards""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aimodelfamilies: Optional[list[LargeLanguageModelFamily]] = Field(default=[], description="""A list of AI model families""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    aimodels: Optional[list[LargeLanguageModel]] = Field(default=[], description="""A list of AI models""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    policies: Optional[list[Union[Policy,LLMQuestionPolicy]]] = Field(default=[], description="""A list of policies""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    rules: Optional[list[Rule]] = Field(default=[], description="""A list of rules""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    prohibitions: Optional[list[Prohibition]] = Field(default=[], description="""A list of prohibitions""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    permissions: Optional[list[Permission]] = Field(default=[], description="""A list of Permissions""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })
    obligations: Optional[list[Obligation]] = Field(default=[], description="""A list of Obligations""", json_schema_extra = { "linkml_meta": {'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Entity.model_rebuild()
Organization.model_rebuild()
License.model_rebuild()
Dataset.model_rebuild()
Documentation.model_rebuild()
Fact.model_rebuild()
Vocabulary.model_rebuild()
Taxonomy.model_rebuild()
Concept.model_rebuild()
Control.model_rebuild()
Group.model_rebuild()
Entry.model_rebuild()
Term.model_rebuild()
Principle.model_rebuild()
Policy.model_rebuild()
LLMQuestionPolicy.model_rebuild()
Rule.model_rebuild()
Permission.model_rebuild()
Prohibition.model_rebuild()
Obligation.model_rebuild()
RiskTaxonomy.model_rebuild()
RiskConcept.model_rebuild()
RiskGroup.model_rebuild()
Risk.model_rebuild()
RiskControl.model_rebuild()
Action.model_rebuild()
RiskIncident.model_rebuild()
Impact.model_rebuild()
IncidentStatus.model_rebuild()
IncidentConcludedclass.model_rebuild()
IncidentHaltedclass.model_rebuild()
IncidentMitigatedclass.model_rebuild()
IncidentNearMissclass.model_rebuild()
IncidentOngoingclass.model_rebuild()
Severity.model_rebuild()
Likelihood.model_rebuild()
Consequence.model_rebuild()
BaseAi.model_rebuild()
AiSystem.model_rebuild()
AiAgent.model_rebuild()
AiModel.model_rebuild()
LargeLanguageModel.model_rebuild()
LargeLanguageModelFamily.model_rebuild()
AiTask.model_rebuild()
AiLifecyclePhase.model_rebuild()
DataPreprocessing.model_rebuild()
AiModelValidation.model_rebuild()
AiProvider.model_rebuild()
Modality.model_rebuild()
Input.model_rebuild()
CapabilityTaxonomy.model_rebuild()
CapabilityConcept.model_rebuild()
CapabilityDomain.model_rebuild()
CapabilityGroup.model_rebuild()
Capability.model_rebuild()
AiEval.model_rebuild()
AiEvalResult.model_rebuild()
BenchmarkMetadataCard.model_rebuild()
Question.model_rebuild()
Questionnaire.model_rebuild()
Adapter.model_rebuild()
LLMIntrinsic.model_rebuild()
AiOffice.model_rebuild()
StakeholderGroup.model_rebuild()
Stakeholder.model_rebuild()
Container.model_rebuild()
