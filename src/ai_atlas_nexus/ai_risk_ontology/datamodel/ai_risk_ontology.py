from __future__ import annotations

import re
import sys
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator


metamodel_version = "None"
version = "0.5.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
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
                 'ai_aiuc'],
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
    # Low-rank adapters, or LoRAs, are a fast way to give generalist large language models targeted knowledge and skills so they can do things like summarize IT manuals or rate the accuracy of their own answers. LoRA reduces the number of trainable parameters by learning pairs of rank-decompostion matrices while freezing the original weights. This vastly reduces the storage requirement for large language models adapted to specific tasks and enables efficient task-switching during deployment all without introducing inference latency. LoRA also outperforms several other adaptation methods including adapter, prefix-tuning, and fine-tuning. See arXiv:2106.09685
    LORA = "LORA"
    # Activated LoRA (aLoRA) is a low rank adapter architecture that allows for reusing existing base model KV cache for more efficient inference, unlike standard LoRA models. As a result, aLoRA models can be quickly invoked as-needed for specialized tasks during (long) flows where the base model is primarily used, avoiding potentially expensive prefill costs in terms of latency, throughput, and GPU memory. See arXiv:2504.12397 for further details.
    ALORA = "ALORA"
    # Mixture of LoRA Experts (X-LoRA) is a mixture of experts method for LoRA which works by using dense or sparse gating to dynamically activate LoRA experts.
    X_LORA = "X-LORA"


class EuAiRiskCategory(str, Enum):
    # Excluded
    EXCLUDED = "EXCLUDED"
    # Prohibited
    PROHIBITED = "PROHIBITED"
    # High-Risk Exception
    HIGH_RISK_EXCEPTION = "HIGH_RISK_EXCEPTION"
    # High Risk
    HIGH_RISK = "HIGH_RISK"
    # Limited or Low Risk
    LIMITED_OR_LOW_RISK = "LIMITED_OR_LOW_RISK"


class AiSystemType(str, Enum):
    # General-purpose AI (GPAI)
    GPAI = "GPAI"
    # General-purpose AI (GPAI) models released under free and open-source licences
    GPAI_OS = "GPAI_OS"
    # Prohibited AI system due to unacceptable risk category (e.g. social scoring systems and manipulative AI).
    PROHIBITED = "PROHIBITED"
    # AI used for scientific research and development
    SCIENTIFIC_RD = "SCIENTIFIC_RD"
    # AI used for military, defense and security purposes.
    MILITARY_SECURITY = "MILITARY_SECURITY"
    # AI systems pursuant to Article 6(1)(2) Classification Rules for High-Risk AI Systems
    HIGH_RISK = "HIGH_RISK"


class AIUC1ApplicationCategory(str, Enum):
    # Mandatory
    MANDATORY = "MANDATORY"
    # Optional
    OPTIONAL = "OPTIONAL"


class AIUC1ControlApplicationCategory(str, Enum):
    # Core Control
    CORE = "CORE"
    # Supplemental Control
    SUPPLEMENTAL = "SUPPLEMENTAL"


class AIUC1EvidenceCategory(str, Enum):
    # Technical Implementation
    TECHNICAL_IMPLEMENTATION = "TECHNICAL_IMPLEMENTATION"
    # Legal Policies
    LEGAL_POLICIES = "LEGAL_POLICIES"
    # Operational Practices
    OPERATIONAL_PRACTICES = "OPERATIONAL_PRACTICES"
    # Third-party Evals
    THIRD_PARTY_EVALS = "THIRD_PARTY_EVALS"


class AIUC1Frequency(str, Enum):
    # Every 3 months
    MONTHS_3 = "MONTHS_3"
    # Every 6 months
    MONTHS_6 = "MONTHS_6"
    # Every 12 months
    MONTHS_12 = "MONTHS_12"


class AIUC1RequirementType(str, Enum):
    # Detective
    DETECTIVE = "DETECTIVE"
    # Preventative
    PREVENTATIVE = "PREVENTATIVE"



class Entity(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Organization(Entity):
    """
    Any organizational entity such as a corporation, educational institution, consortium, government, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Organization',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    grants_license: Optional[str] = Field(default=None, description="""A relationship from a granting entity such as an Organization to a License instance.""", json_schema_extra = { "linkml_meta": {'alias': 'grants_license', 'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class License(Entity):
    """
    The general notion of a license which defines terms and grants permissions to users of AI systems, datasets and software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:License',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Dataset(Entity):
    """
    A body of structured information describing some topic(s) of interest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Dataset',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    provider: Optional[str] = Field(default=None, description="""A relationship to the Organization instance that provides this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'provider', 'domain_of': ['Dataset'], 'slot_uri': 'schema:provider'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Documentation(Entity):
    """
    Documented information about a concept or other topic(s) of interest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Documentation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    author: Optional[str] = Field(default=None, description="""The author or authors of the documentation""", json_schema_extra = { "linkml_meta": {'alias': 'author', 'domain_of': ['Documentation', 'RiskIncident']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Fact(ConfiguredBaseModel):
    """
    A fact about something, for example the result of a measurement. In addition to the value, evidence is provided.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Statement',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    value: str = Field(default=..., description="""Some numeric or string value""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['Fact']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence', 'domain_of': ['Fact']} })


class Vocabulary(Entity):
    """
    A collection of terms, with their definitions and relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["Vocabulary"] = Field(default="Vocabulary", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Taxonomy(Entity):
    """
    A hierachical taxonomy of concepts, with their definitions and relationships.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["Taxonomy"] = Field(default="Taxonomy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Concept(Entity):
    """
    A concept
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'skos:Concept',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["Concept"] = Field(default="Concept", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Control(Entity):
    """
    A measure that maintains and/or modifies
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nexus:Control',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isApplicableinLocality: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has is applicable in these localities.""", json_schema_extra = { "linkml_meta": {'alias': 'isApplicableinLocality',
         'domain_of': ['Control', 'Policy'],
         'slot_uri': 'nexus:isApplicableinLocality'} })
    type: Literal["Control"] = Field(default="Control", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Group(Entity):
    """
    Labelled groups of concepts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'skos:Collection',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has another entity""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["Group"] = Field(default="Group", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Entry(Entity):
    """
    An entry and its definitions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nexus:Entry',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Entry"] = Field(default="Entry", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Term(Entry):
    """
    A term and its definitions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasParentDefinition: Optional[List[str]] = Field(default=None, description="""Indicates parent terms associated with a term""", json_schema_extra = { "linkml_meta": {'alias': 'hasParentDefinition',
         'domain_of': ['Term'],
         'slot_uri': 'nexus:hasParentDefinition'} })
    hasSubDefinition: Optional[List[str]] = Field(default=None, description="""Indicates child terms associated with a term""", json_schema_extra = { "linkml_meta": {'alias': 'hasSubDefinition',
         'domain_of': ['Term'],
         'slot_uri': 'nexus:hasSubDefinition'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Term"] = Field(default="Term", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Principle(Entry):
    """
    A representation of values or norms that must be taken into consideration when conducting activities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Principle',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Principle"] = Field(default="Principle", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Policy(Entity):
    """
    A guidance document outlining any of: procedures, plans, principles, decisions, intent, or protocols.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Policy',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isApplicableinLocality: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has is applicable in these localities.""", json_schema_extra = { "linkml_meta": {'alias': 'isApplicableinLocality',
         'domain_of': ['Control', 'Policy'],
         'slot_uri': 'nexus:isApplicableinLocality'} })
    type: Literal["Policy"] = Field(default="Policy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class LLMQuestionPolicy(Policy):
    """
    The policy guides how the language model should answer a diverse set of sensitive questions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    hasReasonDenial: Optional[str] = Field(default=None, description="""Reason for denial""", json_schema_extra = { "linkml_meta": {'alias': 'hasReasonDenial',
         'domain_of': ['LLMQuestionPolicy'],
         'slot_uri': 'nexus:hasReasonDenial'} })
    hasShortReplyType: Optional[str] = Field(default=None, description="""Short reply type""", json_schema_extra = { "linkml_meta": {'alias': 'hasShortReplyType',
         'domain_of': ['LLMQuestionPolicy'],
         'slot_uri': 'nexus:hasShortReplyType'} })
    hasException: Optional[str] = Field(default=None, description="""Exception type""", json_schema_extra = { "linkml_meta": {'alias': 'hasException',
         'domain_of': ['LLMQuestionPolicy'],
         'slot_uri': 'nexus:hasException'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isApplicableinLocality: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has is applicable in these localities.""", json_schema_extra = { "linkml_meta": {'alias': 'isApplicableinLocality',
         'domain_of': ['Control', 'Policy'],
         'slot_uri': 'nexus:isApplicableinLocality'} })
    type: Literal["LLMQuestionPolicy"] = Field(default="LLMQuestionPolicy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Rule(Entity):
    """
    A rule describing a process or control that directs or determines if and how an activity should be conducted.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Rule',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Rule"] = Field(default="Rule", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AttributeConditionRule(Rule):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    preconditions: Optional[AnonymousClassExpression] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'preconditions', 'domain_of': ['AttributeConditionRule']} })
    postconditions: Optional[AnonymousClassExpression] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'postconditions', 'domain_of': ['AttributeConditionRule']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["AttributeConditionRule"] = Field(default="AttributeConditionRule", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AnonymousClassExpression(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    slot_conditions: Optional[List[SlotCondition]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'slot_conditions', 'domain_of': ['AnonymousClassExpression']} })


class SlotCondition(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    slot_name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'slot_name', 'domain_of': ['SlotCondition']} })
    equals_string: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'equals_string', 'domain_of': ['SlotCondition']} })


class Permission(Rule):
    """
    A rule describing a permission to perform an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Permission',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    type: Literal["Permission"] = Field(default="Permission", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Prohibition(Rule):
    """
    A rule describing a prohibition to perform an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Prohibition',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    type: Literal["Prohibition"] = Field(default="Prohibition", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Obligation(Rule):
    """
    A rule describing an obligation for performing an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Obligation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    type: Literal["Obligation"] = Field(default="Obligation", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Recommendation(Rule):
    """
    A rule describing a recommendation for performing an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Recommendation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    type: Literal["Recommendation"] = Field(default="Recommendation", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Certification(Entry):
    """
    Certification mechanisms, seals, and marks for the purpose of demonstrating compliance
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dpv:Certification',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/common'})

    type: Literal["Certification"] = Field(default="Certification", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class RiskTaxonomy(Taxonomy):
    """
    A taxonomy of AI system related risks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["RiskTaxonomy"] = Field(default="RiskTaxonomy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class RiskControlGroupTaxonomy(Taxonomy):
    """
    A taxonomy of AI system related risk controls groups
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["RiskControlGroupTaxonomy"] = Field(default="RiskControlGroupTaxonomy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class RiskConcept(Concept):
    """
    An umbrella term for referring to risk, risk source, consequence and impact.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:RiskConcept',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixin': True})

    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["RiskConcept"] = Field(default="RiskConcept", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class RiskControlGroup(RiskConcept, Group):
    """
    A group of AI system related risk controls.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept'],
         'slot_usage': {'hasPart': {'description': 'A relationship where a '
                                                   'riskcontrolgroup has a risk '
                                                   'control',
                                    'name': 'hasPart',
                                    'range': 'RiskControl'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where a riskcontrolgroup has a risk control""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["RiskControlGroup"] = Field(default="RiskControlGroup", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where a riskgroup has a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["RiskGroup"] = Field(default="RiskGroup", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    hasRelatedAction: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to an action""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedAction', 'domain_of': ['Risk']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a risk is part of a risk group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    detectsRiskConcept: Optional[List[str]] = Field(default=None, description="""The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'alias': 'detectsRiskConcept',
         'domain': 'RiskControl',
         'domain_of': ['Risk', 'RiskControl'],
         'exact_mappings': ['airo:detectsRiskConcept'],
         'inverse': 'isDetectedBy'} })
    tag: Optional[str] = Field(default=None, description="""A shost version of the name""", json_schema_extra = { "linkml_meta": {'alias': 'tag', 'domain_of': ['Risk']} })
    risk_type: Optional[str] = Field(default=None, description="""Annotation whether an AI risk occurs at input or output or is non-technical.""", json_schema_extra = { "linkml_meta": {'alias': 'risk_type', 'domain_of': ['Risk']} })
    phase: Optional[str] = Field(default=None, description="""Annotation whether an AI risk shows specifically during the training-tuning or inference phase.""", json_schema_extra = { "linkml_meta": {'alias': 'phase', 'domain_of': ['Risk']} })
    descriptor: Optional[List[str]] = Field(default=None, description="""Annotates whether an AI risk is a traditional risk, specific to or amplified by AI.""", json_schema_extra = { "linkml_meta": {'alias': 'descriptor', 'domain_of': ['Risk']} })
    concern: Optional[str] = Field(default=None, description="""Some explanation about the concern related to an AI risk""", json_schema_extra = { "linkml_meta": {'alias': 'concern', 'domain_of': ['Risk']} })
    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Risk"] = Field(default="Risk", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class RiskControl(RiskConcept, Control):
    """
    A measure that maintains and/or modifies risk (and risk concepts)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:RiskControl',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixin': True,
         'mixins': ['RiskConcept']})

    detectsRiskConcept: Optional[List[str]] = Field(default=None, description="""The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'alias': 'detectsRiskConcept',
         'domain': 'RiskControl',
         'domain_of': ['Risk', 'RiskControl'],
         'exact_mappings': ['airo:detectsRiskConcept'],
         'inverse': 'isDetectedBy'} })
    mitigatesRiskConcept: Optional[List[str]] = Field(default=None, description="""Indicates the control used for mitigating risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'alias': 'mitigatesRiskConcept',
         'domain': 'RiskControl',
         'domain_of': ['RiskControl'],
         'exact_mappings': ['airo:mitigatesRiskConcept'],
         'inverse': 'isMitigatedBy'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    isApplicableinLocality: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has is applicable in these localities.""", json_schema_extra = { "linkml_meta": {'alias': 'isApplicableinLocality',
         'domain_of': ['Control', 'Policy'],
         'slot_uri': 'nexus:isApplicableinLocality'} })
    type: Literal["RiskControl"] = Field(default="RiskControl", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })


class Action(RiskControl):
    """
    Action to remediate a risk
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasAiActorTask: Optional[List[str]] = Field(default=None, description="""Pertinent AI Actor Tasks for each subcategory. Not every AI Actor Task listed will apply to every suggested action in the subcategory (i.e., some apply to AI development and others apply to AI deployment).""", json_schema_extra = { "linkml_meta": {'alias': 'hasAiActorTask', 'domain_of': ['Action']} })
    detectsRiskConcept: Optional[List[str]] = Field(default=None, description="""The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'alias': 'detectsRiskConcept',
         'domain': 'RiskControl',
         'domain_of': ['Risk', 'RiskControl'],
         'exact_mappings': ['airo:detectsRiskConcept'],
         'inverse': 'isDetectedBy'} })
    mitigatesRiskConcept: Optional[List[str]] = Field(default=None, description="""Indicates the control used for mitigating risks, risk sources, consequences, and impacts.""", json_schema_extra = { "linkml_meta": {'alias': 'mitigatesRiskConcept',
         'domain': 'RiskControl',
         'domain_of': ['RiskControl'],
         'exact_mappings': ['airo:mitigatesRiskConcept'],
         'inverse': 'isMitigatedBy'} })
    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    isApplicableinLocality: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has is applicable in these localities.""", json_schema_extra = { "linkml_meta": {'alias': 'isApplicableinLocality',
         'domain_of': ['Control', 'Policy'],
         'slot_uri': 'nexus:isApplicableinLocality'} })
    type: Literal["Action"] = Field(default="Action", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class RiskIncident(RiskConcept, Entity):
    """
    An event occuring or occured which is a realised or materialised risk.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'https://w3id.org/dpv/risk#Incident',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept']})

    refersToRisk: Optional[List[str]] = Field(default=None, description="""Indicates the incident (subject) is a materialisation of the indicated risk (object)""", json_schema_extra = { "linkml_meta": {'alias': 'refersToRisk',
         'domain': 'RiskIncident',
         'domain_of': ['RiskIncident'],
         'exact_mappings': ['dpv:refersToRisk']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasStatus: Optional[str] = Field(default=None, description="""Indicates the status of specified concept""", json_schema_extra = { "linkml_meta": {'alias': 'hasStatus', 'domain': 'RiskConcept', 'domain_of': ['RiskIncident']} })
    hasSeverity: Optional[str] = Field(default=None, description="""Indicates the severity associated with a concept""", json_schema_extra = { "linkml_meta": {'alias': 'hasSeverity', 'domain': 'RiskConcept', 'domain_of': ['RiskIncident']} })
    hasLikelihood: Optional[str] = Field(default=None, description="""The likelihood or probability or chance of something taking place or occuring""", json_schema_extra = { "linkml_meta": {'alias': 'hasLikelihood',
         'domain': 'RiskConcept',
         'domain_of': ['RiskIncident']} })
    hasImpactOn: Optional[str] = Field(default=None, description="""Indicates impact(s) possible or arising as consequences from specified concept""", json_schema_extra = { "linkml_meta": {'alias': 'hasImpactOn',
         'broad_mappings': ['dpv:hasConsequenceOn'],
         'domain': 'RiskConcept',
         'domain_of': ['RiskIncident']} })
    hasConsequence: Optional[str] = Field(default=None, description="""Indicates consequence(s) possible or arising from specified concept""", json_schema_extra = { "linkml_meta": {'alias': 'hasConsequence',
         'domain': 'RiskConcept',
         'domain_of': ['RiskIncident']} })
    hasImpact: Optional[str] = Field(default=None, description="""Indicates impact(s) possible or arising as consequences from specified concept""", json_schema_extra = { "linkml_meta": {'alias': 'hasImpact',
         'broad_mappings': ['dpv:hasConsequence'],
         'domain': 'RiskConcept',
         'domain_of': ['RiskIncident']} })
    hasVariant: Optional[str] = Field(default=None, description="""Indicates an incident that shares the same causative factors, produces similar harms, and involves the same intelligent systems as a known AI incident.""", json_schema_extra = { "linkml_meta": {'alias': 'hasVariant', 'domain': 'RiskIncident', 'domain_of': ['RiskIncident']} })
    author: Optional[str] = Field(default=None, description="""The author or authors of the incident report""", json_schema_extra = { "linkml_meta": {'alias': 'author', 'domain_of': ['Documentation', 'RiskIncident']} })
    source_uri: Optional[str] = Field(default=None, description="""The uri of the incident""", json_schema_extra = { "linkml_meta": {'alias': 'source_uri', 'domain_of': ['RiskIncident']} })
    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["RiskIncident"] = Field(default="RiskIncident", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })


class Impact(RiskConcept, Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Impact',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk',
         'mixins': ['RiskConcept']})

    isDetectedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is detected by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isDetectedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'detectsRiskConcept'} })
    isMitigatedBy: Optional[List[str]] = Field(default=None, description="""A relationship where a risk, risk source, consequence, or impact is mitigated by a risk control.""", json_schema_extra = { "linkml_meta": {'alias': 'isMitigatedBy',
         'domain': 'RiskConcept',
         'domain_of': ['RiskConcept'],
         'inverse': 'mitigatesRiskConcept'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["Impact"] = Field(default="Impact", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })


class IncidentStatus(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentStatus',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class IncidentConcludedclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentConcludedclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class IncidentHaltedclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentHaltedclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class IncidentMitigatedclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentMitigatedclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class IncidentNearMissclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentNearMissclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class IncidentOngoingclass(IncidentStatus):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:IncidentOngoingclass',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Severity(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Severity',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Likelihood(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Likelihood',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Consequence(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dpv:Consequence',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_risk'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class BaseAi(Entity):
    """
    Any type of AI, be it a LLM, RL agent, SVM, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'producer', 'domain_of': ['BaseAi']} })
    hasModelCard: Optional[List[str]] = Field(default=None, description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelCard', 'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[List[str]] = Field(default=None, description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'alias': 'performsTask', 'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""Indicates provider of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isProvidedBy',
         'domain_of': ['BaseAi'],
         'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiSystem(BaseAi, Entry):
    """
    A compound AI System composed of one or more AI capablities. ChatGPT is an example of an AI system which deploys multiple GPT AI models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AISystem',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'mixin': True,
         'mixins': ['BaseAi'],
         'slot_usage': {'isComposedOf': {'description': 'Relationship indicating the '
                                                        'AI components from which a '
                                                        'complete AI system is '
                                                        'composed.',
                                         'name': 'isComposedOf',
                                         'range': 'BaseAi'}}})

    isComposedOf: Optional[List[str]] = Field(default=None, description="""Relationship indicating the AI components from which a complete AI system is composed.""", json_schema_extra = { "linkml_meta": {'alias': 'isComposedOf', 'domain_of': ['AiSystem']} })
    hasEuAiSystemType: Optional[AiSystemType] = Field(default=None, description="""The type of system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEuAiSystemType', 'domain_of': ['AiSystem']} })
    hasEuRiskCategory: Optional[EuAiRiskCategory] = Field(default=None, description="""The risk category of an AI system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEuRiskCategory', 'domain_of': ['AiSystem']} })
    hasCapability: Optional[List[str]] = Field(default=None, description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'alias': 'hasCapability',
         'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    isAppliedWithinDomain: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isAppliedWithinDomain',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:isAppliedWithinDomain'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    hasPurpose: Optional[List[str]] = Field(default=None, description="""Indicates the purpose of an entity, e.g. AI system, components.""", json_schema_extra = { "linkml_meta": {'alias': 'hasPurpose',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasPurpose'} })
    hasStakeholder: Optional[str] = Field(default=None, description="""Indicates stakeholders of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'hasStakeholder',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasStakeholder'} })
    isDeployedBy: Optional[str] = Field(default=None, description="""Indicates the deployer of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isDeployedBy',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:isDeployedBy'} })
    isDevelopedBy: Optional[str] = Field(default=None, description="""Indicates the developer of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isDevelopedBy',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:isDevelopedBy'} })
    hasAISubject: Optional[List[str]] = Field(default=None, description="""Indicates the subjects of an AI system""", json_schema_extra = { "linkml_meta": {'alias': 'hasAISubject',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasAISubject'} })
    hasAIUser: Optional[List[str]] = Field(default=None, description="""Indicate the end-user of an AI system.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAIUser',
         'domain': 'AiSystem',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasAiUser'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'producer', 'domain_of': ['BaseAi']} })
    hasModelCard: Optional[List[str]] = Field(default=None, description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelCard', 'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[List[str]] = Field(default=None, description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'alias': 'performsTask', 'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""Indicates provider of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isProvidedBy',
         'domain_of': ['BaseAi'],
         'slot_uri': 'airo:isProvidedBy'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["AiSystem"] = Field(default="AiSystem", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    isComposedOf: Optional[List[str]] = Field(default=None, description="""Relationship indicating the AI components from which a complete AI system is composed.""", json_schema_extra = { "linkml_meta": {'alias': 'isComposedOf', 'domain_of': ['AiSystem']} })
    hasEuAiSystemType: Optional[AiSystemType] = Field(default=None, description="""The type of system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEuAiSystemType', 'domain_of': ['AiSystem']} })
    hasEuRiskCategory: Optional[EuAiRiskCategory] = Field(default=None, description="""The risk category of an AI system as defined by the EU AI Act.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEuRiskCategory', 'domain_of': ['AiSystem']} })
    hasCapability: Optional[List[str]] = Field(default=None, description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'alias': 'hasCapability',
         'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    isAppliedWithinDomain: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isAppliedWithinDomain',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:isAppliedWithinDomain'} })
    isUsedWithinLocality: Optional[List[str]] = Field(default=None, description="""Specifies the domain an AI system is used within.""", json_schema_extra = { "linkml_meta": {'alias': 'isUsedWithinLocality',
         'domain_of': ['RiskConcept', 'AiSystem'],
         'slot_uri': 'airo:isUsedWithinLocality'} })
    hasPurpose: Optional[List[str]] = Field(default=None, description="""Indicates the purpose of an entity, e.g. AI system, components.""", json_schema_extra = { "linkml_meta": {'alias': 'hasPurpose',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasPurpose'} })
    hasStakeholder: Optional[str] = Field(default=None, description="""Indicates stakeholders of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'hasStakeholder',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasStakeholder'} })
    isDeployedBy: Optional[str] = Field(default=None, description="""Indicates the deployer of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isDeployedBy',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:isDeployedBy'} })
    isDevelopedBy: Optional[str] = Field(default=None, description="""Indicates the developer of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isDevelopedBy',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:isDevelopedBy'} })
    hasAISubject: Optional[List[str]] = Field(default=None, description="""Indicates the subjects of an AI system""", json_schema_extra = { "linkml_meta": {'alias': 'hasAISubject',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasAISubject'} })
    hasAIUser: Optional[List[str]] = Field(default=None, description="""Indicate the end-user of an AI system.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAIUser',
         'domain': 'AiSystem',
         'domain_of': ['AiSystem'],
         'slot_uri': 'airo:hasAiUser'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'producer', 'domain_of': ['BaseAi']} })
    hasModelCard: Optional[List[str]] = Field(default=None, description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelCard', 'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[List[str]] = Field(default=None, description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'alias': 'performsTask', 'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""A relationship indicating the AI agent has been provided by an AI systems provider.""", json_schema_extra = { "linkml_meta": {'alias': 'isProvidedBy',
         'domain_of': ['BaseAi'],
         'slot_uri': 'airo:isProvidedBy'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["AiAgent"] = Field(default="AiAgent", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class LargeLanguageModelFamily(Entity):
    """
    A large language model family is a set of models that are provided by the same AI systems provider and are built around the same architecture, but differ e.g. in the number of parameters. Examples are Meta's Llama2 family or the IBM granite models.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiTask(Entry):
    """
    A task, such as summarization and classification, performed by an AI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AiCapability',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["AiTask"] = Field(default="AiTask", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiTaskTaxonomy(Taxonomy):
    """
    A taxonomy of AI Tasks
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["AiTaskTaxonomy"] = Field(default="AiTaskTaxonomy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiTaskDomain(Group):
    """
    A grouping of AI Tasks by domain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:AiTaskDomain',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'slot_usage': {'hasPart': {'description': 'A relationship where an AI Task '
                                                   'domain has a group.',
                                    'name': 'hasPart',
                                    'range': 'AiTaskGroup'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where an AI Task domain has a group.""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["AiTaskDomain"] = Field(default="AiTaskDomain", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiTaskGroup(Group):
    """
    A group of AI Tasks.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:AiTaskGroup',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'slot_usage': {'hasPart': {'description': 'A relationship where an AI task '
                                                   'group has an AI task.',
                                    'name': 'hasPart',
                                    'range': 'AiTask'},
                        'isPartOf': {'name': 'isPartOf', 'range': 'AiTaskDomain'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where an AI task group has an AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["AiTaskGroup"] = Field(default="AiTaskGroup", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiLifecyclePhase(Entity):
    """
    A Phase of AI lifecycle which indicates evolution of the system from conception through retirement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'airo:AILifecyclePhase',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class DataPreprocessing(AiLifecyclePhase):
    """
    Data transformations, such as PI filtering, performed to ensure high quality of AI model training data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiModelValidation(AiLifecyclePhase):
    """
    AI model validation steps that have been performed after the model training to ensure high AI model quality.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiProvider(Organization):
    """
    A provider under the AI Act is defined by Article 3(3) as a natural or legal person or body that develops an AI system or general-purpose AI model or has an AI system or general-purpose AI model developed; and places that ystem or model on the market, or puts that system into service, under the provider's own name or trademark, whether for payment or free for charge.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIProvider',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    grants_license: Optional[str] = Field(default=None, description="""A relationship from a granting entity such as an Organization to a License instance.""", json_schema_extra = { "linkml_meta": {'alias': 'grants_license', 'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Modality(Entity):
    """
    A modality supported by an Ai component. Examples include text, image, video.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Modality',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Input(Entity):
    """
    Input for which the system or component generates output.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Input',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Purpose(Entry):
    """
    The end goal for which an entity is used or an action is taken.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Purpose',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Purpose"] = Field(default="Purpose", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Domain(Entry):
    """
    An area, sector, or industry that is associated with economic activities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Domain',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Domain"] = Field(default="Domain", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class LocalityOfUse(Entry):
    """
    The area, e.g. facility or institution, in which an entity is used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:LocalityOfUse',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["LocalityOfUse"] = Field(default="LocalityOfUse", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AIComponent(Entity):
    """
    Component (element) of an AI system
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIComponent',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiModel(AIComponent, BaseAi):
    """
    A base AI Model class. No assumption about the type (SVM, LLM, etc.). Subclassed by model types (see LargeLanguageModel).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'mixin': True,
         'mixins': ['AIComponent']})

    hasEvaluation: Optional[List[str]] = Field(default=None, description="""A relationship indicating that an entity has an AI evaluation result.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvaluation',
         'domain_of': ['AiModel'],
         'slot_uri': 'dqv:hasQualityMeasurement'} })
    architecture: Optional[str] = Field(default=None, description="""A description of the architecture of an AI such as 'Decoder-only'.""", json_schema_extra = { "linkml_meta": {'alias': 'architecture', 'domain_of': ['AiModel']} })
    gpu_hours: Optional[int] = Field(default=None, description="""GPU consumption in terms of hours""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'gpu_hours', 'domain_of': ['AiModel']} })
    power_consumption_w: Optional[int] = Field(default=None, description="""power consumption in Watts""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'power_consumption_w', 'domain_of': ['AiModel']} })
    carbon_emitted: Optional[float] = Field(default=None, description="""The number of tons of carbon dioxide equivalent that are emitted during training""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'carbon_emitted',
         'domain_of': ['AiModel'],
         'unit': {'descriptive_name': 'tons of CO2 equivalent', 'symbol': 't CO2-eq'}} })
    hasRiskControl: Optional[List[str]] = Field(default=None, description="""Indicates the control measures associated with a system or component to modify risks.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRiskControl',
         'domain_of': ['AiModel'],
         'slot_uri': 'airo:hasRiskControl'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'producer', 'domain_of': ['BaseAi']} })
    hasModelCard: Optional[List[str]] = Field(default=None, description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelCard', 'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[List[str]] = Field(default=None, description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'alias': 'performsTask', 'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""Indicates provider of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isProvidedBy',
         'domain_of': ['BaseAi'],
         'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    numParameters: Optional[int] = Field(default=None, description="""A property indicating the number of parameters in a LLM.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'numParameters', 'domain_of': ['LargeLanguageModel']} })
    numTrainingTokens: Optional[int] = Field(default=None, description="""The number of tokens a AI model was trained on.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'numTrainingTokens', 'domain_of': ['LargeLanguageModel']} })
    contextWindowSize: Optional[int] = Field(default=None, description="""The total length, in bytes, of an AI model's context window.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'contextWindowSize', 'domain_of': ['LargeLanguageModel']} })
    hasInputModality: Optional[List[str]] = Field(default=None, description="""A relationship indicating the input modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'alias': 'hasInputModality', 'domain_of': ['LargeLanguageModel']} })
    hasOutputModality: Optional[List[str]] = Field(default=None, description="""A relationship indicating the output modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'alias': 'hasOutputModality', 'domain_of': ['LargeLanguageModel']} })
    hasTrainingData: Optional[List[str]] = Field(default=None, description="""A relationship indicating the datasets an AI model was trained on.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTrainingData',
         'domain_of': ['LargeLanguageModel'],
         'slot_uri': 'airo:hasTrainingData'} })
    fine_tuning: Optional[str] = Field(default=None, description="""A description of the fine-tuning mechanism(s) applied to a model.""", json_schema_extra = { "linkml_meta": {'alias': 'fine_tuning', 'domain_of': ['LargeLanguageModel']} })
    supported_languages: Optional[List[str]] = Field(default=None, description="""A list of languages, expressed as ISO two letter codes. For example, 'jp, fr, en, de'""", json_schema_extra = { "linkml_meta": {'alias': 'supported_languages', 'domain_of': ['LargeLanguageModel']} })
    isPartOf: Optional[str] = Field(default=None, description="""Annotation that a Large Language model is part of a family of models""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    hasEvaluation: Optional[List[str]] = Field(default=None, description="""A relationship indicating that an entity has an AI evaluation result.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvaluation',
         'domain_of': ['AiModel'],
         'slot_uri': 'dqv:hasQualityMeasurement'} })
    architecture: Optional[str] = Field(default=None, description="""A description of the architecture of an AI such as 'Decoder-only'.""", json_schema_extra = { "linkml_meta": {'alias': 'architecture', 'domain_of': ['AiModel']} })
    gpu_hours: Optional[int] = Field(default=None, description="""GPU consumption in terms of hours""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'gpu_hours', 'domain_of': ['AiModel']} })
    power_consumption_w: Optional[int] = Field(default=None, description="""power consumption in Watts""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'power_consumption_w', 'domain_of': ['AiModel']} })
    carbon_emitted: Optional[float] = Field(default=None, description="""The number of tons of carbon dioxide equivalent that are emitted during training""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'carbon_emitted',
         'domain_of': ['AiModel'],
         'unit': {'descriptive_name': 'tons of CO2 equivalent', 'symbol': 't CO2-eq'}} })
    hasRiskControl: Optional[List[str]] = Field(default=None, description="""Indicates the control measures associated with a system or component to modify risks.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRiskControl',
         'domain_of': ['AiModel'],
         'slot_uri': 'airo:hasRiskControl'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'producer', 'domain_of': ['BaseAi']} })
    hasModelCard: Optional[List[str]] = Field(default=None, description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelCard', 'domain_of': ['BaseAi']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    performsTask: Optional[List[str]] = Field(default=None, description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'alias': 'performsTask', 'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""Indicates provider of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isProvidedBy',
         'domain_of': ['BaseAi'],
         'slot_uri': 'airo:isProvidedBy'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Stakeholder(Entity):
    """
    Represents any individual, group or organization that can affect, be affected by or perceive itself to be affected by a decision or activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:Stakeholder',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system',
         'slot_usage': {'isPartOf': {'description': 'A relationship where a '
                                                    'stakeholder is part of a '
                                                    'stakeholder group',
                                     'name': 'isPartOf',
                                     'range': 'StakeholderGroup'}}})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AISubject(Stakeholder):
    """
    An entity that is subject to or impacted by the use of AI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AISubject',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AIOperator(Stakeholder):
    """
    Refers to a provider, product manufacturer, deployer, authorised representative, importer or distributor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIOperator',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AIDeveloper(Stakeholder):
    """
    An organisation or entity that is concerned with the development of AI services and products.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIDeveloper',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AIDeployer(AIOperator):
    """
    Any natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIDeployer',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AIUser(Stakeholder):
    """
    Individual or group that interacts with a system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'airo:AIUser',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a stakeholder is part of a stakeholder group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class StakeholderGroup(Group):
    """
    An AI system stakeholder grouping.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_system'})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where an entity has another entity""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["StakeholderGroup"] = Field(default="StakeholderGroup", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class CapabilityTaxonomy(Taxonomy):
    """
    A taxonomy of AI capabilities describing the abilities of AI systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability'})

    version: Optional[str] = Field(default=None, description="""The version of the entity embodied by a specified resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version',
         'domain_of': ['License',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'AiTaskTaxonomy'],
         'slot_uri': 'schema:version'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    type: Literal["CapabilityTaxonomy"] = Field(default="CapabilityTaxonomy", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class CapabilityConcept(Concept):
    """
    An umbrella term for referring to capability domains, groups, and individual capabilities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:CapabilityConcept',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_capability',
         'mixin': True})

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["CapabilityConcept"] = Field(default="CapabilityConcept", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where a capability domain has capability groups""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[Any] = Field(default=None, description="""A relationship where a group belongs to a domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    type: Literal["CapabilityDomain"] = Field(default="CapabilityDomain", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a capability group belongs to a capability domain""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    hasPart: Optional[List[str]] = Field(default=None, description="""A relationship where a capability group has capabilities""", json_schema_extra = { "linkml_meta": {'alias': 'hasPart',
         'domain_of': ['Group',
                       'RiskControlGroup',
                       'RiskGroup',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'CapabilityGroup'],
         'slot_uri': 'skos:member'} })
    belongsToDomain: Optional[str] = Field(default=None, description="""A relationship where a capability group belongs to a capability domain""", json_schema_extra = { "linkml_meta": {'alias': 'belongsToDomain',
         'domain_of': ['Group', 'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    type: Literal["CapabilityGroup"] = Field(default="CapabilityGroup", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement'],
         'ifabsent': 'string(Group)'} })
    narrower: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'narrower', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    broader: Optional[List[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'broader', 'domain_of': ['Group'], 'slot_uri': 'skos:narrower'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Capability(CapabilityConcept, Entry):
    """
    A specific AI capability or ability, such as reading comprehension, logical reasoning, or code generation. Aligned with the W3C DPV AI extension dpv-ai:Capability, representing what an AI technology is capable of achieving or providing.
    Capabilities are distinct from: (1) the intended purpose for which the technology is designed, (2) the actual tasks performed in a specific deployment context, and (3) the technical implementation mechanisms (intrinsics, adapters) that enable the capability.
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

    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is required to perform a specific AI task. This links abstract capabilities (technical abilities) to concrete tasks (application-level operations). An AI system with this capability can perform tasks that require it.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Capability',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where a capability is part of a capability group""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Capability"] = Field(default="Capability", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


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

    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasDataset: Optional[List[str]] = Field(default=None, description="""A relationship to datasets that are used.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataset', 'domain_of': ['AiEval']} })
    hasTasks: Optional[List[str]] = Field(default=None, description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTasks',
         'domain_of': ['AiEval', 'EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasImplementation: Optional[List[str]] = Field(default=None, description="""A relationship to a implementation defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasImplementation',
         'domain_of': ['AiEval'],
         'slot_uri': 'schema:url'} })
    hasUnitxtCard: Optional[List[str]] = Field(default=None, description="""A relationship to a Unitxt card defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasUnitxtCard', 'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    bestValue: Optional[str] = Field(default=None, description="""Annotation of the best possible result of the evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'bestValue', 'domain_of': ['AiEval']} })
    hasBenchmarkMetadata: Optional[List[str]] = Field(default=None, description="""A relationship to a Benchmark Metadata Card which contains metadata about the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasBenchmarkMetadata',
         'domain': 'AiEval',
         'domain_of': ['AiEval'],
         'inverse': 'describesAiEval'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiEvalResult(Fact, Entity):
    """
    The result of an evaluation for a specific AI model.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dqv:QualityMeasurement',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval',
         'mixins': ['Fact']})

    isResultOf: Optional[str] = Field(default=None, description="""A relationship indicating that an entity is the result of an AI evaluation.""", json_schema_extra = { "linkml_meta": {'alias': 'isResultOf',
         'domain_of': ['AiEvalResult'],
         'slot_uri': 'dqv:isMeasurementOf'} })
    value: str = Field(default=..., description="""Some numeric or string value""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['Fact']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence', 'domain_of': ['Fact']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class SourceMetadata(Entity):
    """
    Metadata about the source of an evaluation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:sourcemetadata',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    source_name: Optional[str] = Field(default=None, description="""Name of the evaluation source""", json_schema_extra = { "linkml_meta": {'alias': 'source_name', 'domain_of': ['SourceMetadata']} })
    source_type: Optional[str] = Field(default=None, description="""Type of source (e.g., evaluation_run)""", json_schema_extra = { "linkml_meta": {'alias': 'source_type', 'domain_of': ['SourceMetadata', 'SourceData']} })
    source_organization_name: Optional[str] = Field(default=None, description="""Organization that provided the evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'source_organization_name', 'domain_of': ['SourceMetadata']} })
    source_organization_url: Optional[str] = Field(default=None, description="""URL of the source organization""", json_schema_extra = { "linkml_meta": {'alias': 'source_organization_url', 'domain_of': ['SourceMetadata']} })
    evaluator_relationship: Optional[str] = Field(default=None, description="""Relationship of evaluator (e.g., first_party, third_party)""", json_schema_extra = { "linkml_meta": {'alias': 'evaluator_relationship', 'domain_of': ['SourceMetadata']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ModelInfo(Entity):
    """
    Information about the AI model being evaluated
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:modelinfo',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    model_name: Optional[str] = Field(default=None, description="""Name of the AI model""", json_schema_extra = { "linkml_meta": {'alias': 'model_name', 'domain_of': ['ModelInfo']} })
    model_id: Optional[str] = Field(default=None, description="""Identifier of the AI model""", json_schema_extra = { "linkml_meta": {'alias': 'model_id', 'domain_of': ['ModelInfo']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class SourceData(Entity):
    """
    Information about the data source used in evaluation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:sourcedata',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    dataset_name: Optional[str] = Field(default=None, description="""Name of the dataset""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_name', 'domain_of': ['SourceData']} })
    source_type: Optional[str] = Field(default=None, description="""Type of data source (e.g., hf_dataset)""", json_schema_extra = { "linkml_meta": {'alias': 'source_type', 'domain_of': ['SourceMetadata', 'SourceData']} })
    hf_repo: Optional[str] = Field(default=None, description="""HuggingFace repository""", json_schema_extra = { "linkml_meta": {'alias': 'hf_repo', 'domain_of': ['SourceData']} })
    hf_split: Optional[str] = Field(default=None, description="""HuggingFace dataset split""", json_schema_extra = { "linkml_meta": {'alias': 'hf_split', 'domain_of': ['SourceData']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class MetricConfig(Entity):
    """
    Configuration for evaluation metrics
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:metricconfig',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    lower_is_better: Optional[bool] = Field(default=None, description="""Whether lower scores are better""", json_schema_extra = { "linkml_meta": {'alias': 'lower_is_better', 'domain_of': ['MetricConfig']} })
    score_type: Optional[str] = Field(default=None, description="""Type of score (e.g., continuous)""", json_schema_extra = { "linkml_meta": {'alias': 'score_type', 'domain_of': ['MetricConfig']} })
    min_score: Optional[float] = Field(default=None, description="""Minimum possible score""", json_schema_extra = { "linkml_meta": {'alias': 'min_score', 'domain_of': ['MetricConfig']} })
    max_score: Optional[float] = Field(default=None, description="""Maximum possible score""", json_schema_extra = { "linkml_meta": {'alias': 'max_score', 'domain_of': ['MetricConfig']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ScoreDetails(Entity):
    """
    Details about evaluation scores
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:scoredetails',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    score: Optional[float] = Field(default=None, description="""The evaluation score""", json_schema_extra = { "linkml_meta": {'alias': 'score', 'domain_of': ['ScoreDetails']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class EvaluationResultRecord(Entity):
    """
    A single evaluation result record
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:evaluationresultrecord',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    hasSourceData: Optional[SourceData] = Field(default=None, description="""Source data information""", json_schema_extra = { "linkml_meta": {'alias': 'hasSourceData',
         'domain': 'EvaluationResultRecord',
         'domain_of': ['EvaluationResultRecord']} })
    hasMetricConfig: Optional[MetricConfig] = Field(default=None, description="""Metric configuration""", json_schema_extra = { "linkml_meta": {'alias': 'hasMetricConfig',
         'domain': 'EvaluationResultRecord',
         'domain_of': ['EvaluationResultRecord']} })
    hasScoreDetails: Optional[ScoreDetails] = Field(default=None, description="""Score details""", json_schema_extra = { "linkml_meta": {'alias': 'hasScoreDetails',
         'domain': 'EvaluationResultRecord',
         'domain_of': ['EvaluationResultRecord']} })
    evaluation_name: Optional[str] = Field(default=None, description="""Name of the evaluation benchmark""", json_schema_extra = { "linkml_meta": {'alias': 'evaluation_name', 'domain_of': ['EvaluationResultRecord']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class EveryEvalAIResult(AiEvalResult):
    """
    An evaluation result from the Every Eval Ever dataset, capturing evaluation metadata and results from the EEE_datastore.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:everyevalairesult',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    hasSourceMetadata: Optional[SourceMetadata] = Field(default=None, description="""Source metadata for the evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasSourceMetadata',
         'domain': 'EveryEvalAIResult',
         'domain_of': ['EveryEvalAIResult']} })
    hasModelInfo: Optional[ModelInfo] = Field(default=None, description="""Model information for the evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelInfo',
         'domain': 'EveryEvalAIResult',
         'domain_of': ['EveryEvalAIResult']} })
    hasEvaluationResults: Optional[Dict[str, EvaluationResultRecord]] = Field(default=None, description="""Array of evaluation results""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvaluationResults',
         'domain': 'EveryEvalAIResult',
         'domain_of': ['EveryEvalAIResult']} })
    hasDataType: Optional[List[str]] = Field(default=None, description="""The type of data used in the benchmark (e.g., text, images, or multi-modal)""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataType',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDomains: Optional[List[str]] = Field(default=None, description="""The specific domains or areas where the benchmark is applied (e.g., natural language processing, computer vision).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDomains',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasLanguages: Optional[List[str]] = Field(default=None, description="""The languages included in the dataset used by the benchmark (e.g., English, multilingual).""", json_schema_extra = { "linkml_meta": {'alias': 'hasLanguages',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasTasks: Optional[List[str]] = Field(default=None, description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTasks',
         'domain_of': ['AiEval', 'EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDataSource: Optional[List[str]] = Field(default=None, description="""The origin or source of the data used in the benchmark (e.g., curated datasets, user submissions).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataSource',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDataSize: Optional[str] = Field(default=None, description="""The size of the dataset, including the number of data points or examples.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataSize',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDataFormat: Optional[List[str]] = Field(default=None, description="""The structure and modality of the data (e.g., sentence pairs, question-answer format, tabular data).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataFormat',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasMethods: Optional[List[str]] = Field(default=None, description="""The evaluation techniques applied within the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasMethods',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasMetrics: Optional[List[str]] = Field(default=None, description="""The specific performance metrics used to assess models (e.g., accuracy, F1 score, precision, recall).""", json_schema_extra = { "linkml_meta": {'alias': 'hasMetrics',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasLimitations: Optional[List[str]] = Field(default=None, description="""Limitations in evaluating or addressing risks, such as gaps in demographic coverage or specific domains.""", json_schema_extra = { "linkml_meta": {'alias': 'hasLimitations',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasGoal: Optional[str] = Field(default=None, description="""The specific goal or primary use case the benchmark is designed for.""", json_schema_extra = { "linkml_meta": {'alias': 'hasGoal',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasAudience: Optional[List[str]] = Field(default=None, description="""The intended audience, such as researchers, developers, policymakers, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAudience',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasResources: Optional[List[str]] = Field(default=None, description="""Links to relevant resources, such as repositories or papers related to the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasResources',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    schema_version: Optional[str] = Field(default=None, description="""Version of the evaluation schema""", json_schema_extra = { "linkml_meta": {'alias': 'schema_version', 'domain_of': ['EveryEvalAIResult']} })
    evaluation_id: Optional[str] = Field(default=None, description="""Unique identifier for this evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'evaluation_id', 'domain_of': ['EveryEvalAIResult']} })
    evaluation_timestamp: Optional[datetime ] = Field(default=None, description="""ISO 8601 timestamp when evaluation was performed""", json_schema_extra = { "linkml_meta": {'alias': 'evaluation_timestamp', 'domain_of': ['EveryEvalAIResult']} })
    retrieved_timestamp: Optional[str] = Field(default=None, description="""Unix timestamp when the data was retrieved""", json_schema_extra = { "linkml_meta": {'alias': 'retrieved_timestamp', 'domain_of': ['EveryEvalAIResult']} })
    isResultOf: Optional[str] = Field(default=None, description="""A relationship indicating that an entity is the result of an AI evaluation.""", json_schema_extra = { "linkml_meta": {'alias': 'isResultOf',
         'domain_of': ['AiEvalResult'],
         'slot_uri': 'dqv:isMeasurementOf'} })
    value: str = Field(default=..., description="""Some numeric or string value""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['Fact']} })
    evidence: Optional[str] = Field(default=None, description="""Evidence provides a source (typical a chunk, paragraph or link) describing where some value was found or how it was generated.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence', 'domain_of': ['Fact']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class BenchmarkMetadataCard(Entity):
    """
    Benchmark metadata cards offer a standardized way to document LLM benchmarks clearly and transparently. Inspired by Model Cards and Datasheets, Benchmark metadata cards help researchers and practitioners understand exactly what benchmarks test, how they relate to real-world risks, and how to interpret their results responsibly. This is an implementation of the design set out in BenchmarkCards: Large Language Model and Risk Reporting (https://doi.org/10.48550/arXiv.2410.12974)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:benchmarkmetadatacard',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    describesAiEval: Optional[List[str]] = Field(default=None, description="""A relationship where a BenchmarkMetadataCard describes an AI evaluation (benchmark).""", json_schema_extra = { "linkml_meta": {'alias': 'describesAiEval',
         'domain': 'BenchmarkMetadataCard',
         'domain_of': ['BenchmarkMetadataCard'],
         'inverse': 'hasBenchmarkMetadata'} })
    hasDataType: Optional[List[str]] = Field(default=None, description="""The type of data used in the benchmark (e.g., text, images, or multi-modal)""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataType',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDomains: Optional[List[str]] = Field(default=None, description="""The specific domains or areas where the benchmark is applied (e.g., natural language processing, computer vision).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDomains',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasLanguages: Optional[List[str]] = Field(default=None, description="""The languages included in the dataset used by the benchmark (e.g., English, multilingual).""", json_schema_extra = { "linkml_meta": {'alias': 'hasLanguages',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasSimilarBenchmarks: Optional[List[str]] = Field(default=None, description="""Benchmarks that are closely related in terms of goals or data type.""", json_schema_extra = { "linkml_meta": {'alias': 'hasSimilarBenchmarks', 'domain_of': ['BenchmarkMetadataCard']} })
    hasResources: Optional[List[str]] = Field(default=None, description="""Links to relevant resources, such as repositories or papers related to the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasResources',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasGoal: Optional[str] = Field(default=None, description="""The specific goal or primary use case the benchmark is designed for.""", json_schema_extra = { "linkml_meta": {'alias': 'hasGoal',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasAudience: Optional[List[str]] = Field(default=None, description="""The intended audience, such as researchers, developers, policymakers, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAudience',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasTasks: Optional[List[str]] = Field(default=None, description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTasks',
         'domain_of': ['AiEval', 'EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasLimitations: Optional[List[str]] = Field(default=None, description="""Limitations in evaluating or addressing risks, such as gaps in demographic coverage or specific domains.""", json_schema_extra = { "linkml_meta": {'alias': 'hasLimitations',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasOutOfScopeUses: Optional[List[str]] = Field(default=None, description="""Use cases where the benchmark is not designed to be applied and could give misleading results.""", json_schema_extra = { "linkml_meta": {'alias': 'hasOutOfScopeUses', 'domain_of': ['BenchmarkMetadataCard']} })
    hasDataSource: Optional[List[str]] = Field(default=None, description="""The origin or source of the data used in the benchmark (e.g., curated datasets, user submissions).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataSource',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDataSize: Optional[str] = Field(default=None, description="""The size of the dataset, including the number of data points or examples.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataSize',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasDataFormat: Optional[List[str]] = Field(default=None, description="""The structure and modality of the data (e.g., sentence pairs, question-answer format, tabular data).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataFormat',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasAnnotation: Optional[List[str]] = Field(default=None, description="""The process used to annotate or label the dataset, including who or what performed the annotations (e.g., human annotators, automated processes).""", json_schema_extra = { "linkml_meta": {'alias': 'hasAnnotation', 'domain_of': ['BenchmarkMetadataCard']} })
    hasMethods: Optional[List[str]] = Field(default=None, description="""The evaluation techniques applied within the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasMethods',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasMetrics: Optional[List[str]] = Field(default=None, description="""The specific performance metrics used to assess models (e.g., accuracy, F1 score, precision, recall).""", json_schema_extra = { "linkml_meta": {'alias': 'hasMetrics',
         'domain_of': ['EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasCalculation: Optional[List[str]] = Field(default=None, description="""The way metrics are computed based on model outputs and the benchmark data.""", json_schema_extra = { "linkml_meta": {'alias': 'hasCalculation', 'domain_of': ['BenchmarkMetadataCard']} })
    hasInterpretation: Optional[List[str]] = Field(default=None, description="""How users should interpret the scores or results from the metrics.""", json_schema_extra = { "linkml_meta": {'alias': 'hasInterpretation', 'domain_of': ['BenchmarkMetadataCard']} })
    hasBaselineResults: Optional[List[str]] = Field(default=None, description="""The results of well-known or widely used models to give context to new performance scores.""", json_schema_extra = { "linkml_meta": {'alias': 'hasBaselineResults', 'domain_of': ['BenchmarkMetadataCard']} })
    hasValidation: Optional[List[str]] = Field(default=None, description="""Measures taken to ensure that the benchmark provides valid and reliable evaluations.""", json_schema_extra = { "linkml_meta": {'alias': 'hasValidation', 'domain_of': ['BenchmarkMetadataCard']} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasDemographicAnalysis: Optional[List[str]] = Field(default=None, description="""How the benchmark evaluates performance across different demographic groups (e.g., gender, race).""", json_schema_extra = { "linkml_meta": {'alias': 'hasDemographicAnalysis', 'domain_of': ['BenchmarkMetadataCard']} })
    hasConsiderationPrivacyAndAnonymity: Optional[List[str]] = Field(default=None, description="""How any personal or sensitive data is handled and whether any anonymization techniques are applied.""", json_schema_extra = { "linkml_meta": {'alias': 'hasConsiderationPrivacyAndAnonymity',
         'domain_of': ['BenchmarkMetadataCard']} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasConsiderationConsentProcedures: Optional[List[str]] = Field(default=None, description="""Information on how consent was obtained (if applicable), especially for datasets involving personal data.""", json_schema_extra = { "linkml_meta": {'alias': 'hasConsiderationConsentProcedures',
         'domain_of': ['BenchmarkMetadataCard']} })
    hasConsiderationComplianceWithRegulations: Optional[List[str]] = Field(default=None, description="""Compliance with relevant legal or ethical regulations (if applicable).""", json_schema_extra = { "linkml_meta": {'alias': 'hasConsiderationComplianceWithRegulations',
         'domain_of': ['BenchmarkMetadataCard']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    name: Optional[str] = Field(default=None, description="""The official name of the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Entity', 'BenchmarkMetadataCard']} })
    overview: Optional[str] = Field(default=None, description="""A brief description of the benchmark's main goals and scope.""", json_schema_extra = { "linkml_meta": {'alias': 'overview', 'domain_of': ['BenchmarkMetadataCard']} })
    type: Literal["BenchmarkMetadataCard"] = Field(default="BenchmarkMetadataCard", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Question(AiEval):
    """
    An evaluation where a question has to be answered
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval'})

    text: str = Field(default=..., description="""The question itself""", json_schema_extra = { "linkml_meta": {'alias': 'text', 'domain_of': ['Question']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasDataset: Optional[List[str]] = Field(default=None, description="""A relationship to datasets that are used.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataset', 'domain_of': ['AiEval']} })
    hasTasks: Optional[List[str]] = Field(default=None, description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTasks',
         'domain_of': ['AiEval', 'EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasImplementation: Optional[List[str]] = Field(default=None, description="""A relationship to a implementation defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasImplementation',
         'domain_of': ['AiEval'],
         'slot_uri': 'schema:url'} })
    hasUnitxtCard: Optional[List[str]] = Field(default=None, description="""A relationship to a Unitxt card defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasUnitxtCard', 'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    bestValue: Optional[str] = Field(default=None, description="""Annotation of the best possible result of the evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'bestValue', 'domain_of': ['AiEval']} })
    hasBenchmarkMetadata: Optional[List[str]] = Field(default=None, description="""A relationship to a Benchmark Metadata Card which contains metadata about the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasBenchmarkMetadata',
         'domain': 'AiEval',
         'domain_of': ['AiEval'],
         'inverse': 'describesAiEval'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Questionnaire(AiEval):
    """
    A questionnaire groups questions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval',
         'slot_usage': {'composed_of': {'name': 'composed_of', 'range': 'Question'}}})

    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasDataset: Optional[List[str]] = Field(default=None, description="""A relationship to datasets that are used.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDataset', 'domain_of': ['AiEval']} })
    hasTasks: Optional[List[str]] = Field(default=None, description="""The tasks or evaluations the benchmark is intended to assess.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTasks',
         'domain_of': ['AiEval', 'EveryEvalAIResult', 'BenchmarkMetadataCard']} })
    hasImplementation: Optional[List[str]] = Field(default=None, description="""A relationship to a implementation defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasImplementation',
         'domain_of': ['AiEval'],
         'slot_uri': 'schema:url'} })
    hasUnitxtCard: Optional[List[str]] = Field(default=None, description="""A relationship to a Unitxt card defining the risk evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'hasUnitxtCard', 'domain_of': ['AiEval'], 'slot_uri': 'schema:url'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    bestValue: Optional[str] = Field(default=None, description="""Annotation of the best possible result of the evaluation""", json_schema_extra = { "linkml_meta": {'alias': 'bestValue', 'domain_of': ['AiEval']} })
    hasBenchmarkMetadata: Optional[List[str]] = Field(default=None, description="""A relationship to a Benchmark Metadata Card which contains metadata about the benchmark.""", json_schema_extra = { "linkml_meta": {'alias': 'hasBenchmarkMetadata',
         'domain': 'AiEval',
         'domain_of': ['AiEval'],
         'inverse': 'describesAiEval'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Adapter(LargeLanguageModel, Entry):
    """
    Adapter-based methods add extra trainable parameters after the attention and fully-connected layers of a frozen pretrained model to reduce memory-usage and speed up training. The adapters are typically small but demonstrate comparable performance to a fully finetuned model and enable training larger models with fewer resources. (https://huggingface.co/docs/peft/en/conceptual_guides/adapter)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_intrinsic',
         'mixins': ['LargeLanguageModel']})

    hasAdapterType: Optional[List[AdapterType]] = Field(default=None, description="""The Adapter type, for example: LORA, ALORA, X-LORA""", json_schema_extra = { "linkml_meta": {'alias': 'hasAdapterType', 'domain_of': ['Adapter']} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    hasLicense: Optional[str] = Field(default=None, description="""Indicates licenses associated with a resource""", json_schema_extra = { "linkml_meta": {'alias': 'hasLicense',
         'domain_of': ['Dataset',
                       'Documentation',
                       'Vocabulary',
                       'Taxonomy',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'BaseAi',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'BenchmarkMetadataCard',
                       'Adapter'],
         'slot_uri': 'airo:hasLicense'} })
    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    adaptsModel: Optional[List[str]] = Field(default=None, description="""The LargeLanguageModel being adapted""", json_schema_extra = { "linkml_meta": {'alias': 'adaptsModel', 'domain_of': ['Adapter']} })
    implementsCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entity implements a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'implementsCapability',
         'domain': 'Any',
         'domain_of': ['Adapter'],
         'inverse': 'implementedByAdapter'} })
    hasCapability: Optional[List[str]] = Field(default=None, description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'alias': 'hasCapability',
         'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    numParameters: Optional[int] = Field(default=None, description="""A property indicating the number of parameters in a LLM.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'numParameters', 'domain_of': ['LargeLanguageModel']} })
    numTrainingTokens: Optional[int] = Field(default=None, description="""The number of tokens a AI model was trained on.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'numTrainingTokens', 'domain_of': ['LargeLanguageModel']} })
    contextWindowSize: Optional[int] = Field(default=None, description="""The total length, in bytes, of an AI model's context window.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'contextWindowSize', 'domain_of': ['LargeLanguageModel']} })
    hasInputModality: Optional[List[str]] = Field(default=None, description="""A relationship indicating the input modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'alias': 'hasInputModality', 'domain_of': ['LargeLanguageModel']} })
    hasOutputModality: Optional[List[str]] = Field(default=None, description="""A relationship indicating the output modalities supported by an AI component. Examples include text, image, video.""", json_schema_extra = { "linkml_meta": {'alias': 'hasOutputModality', 'domain_of': ['LargeLanguageModel']} })
    hasTrainingData: Optional[List[str]] = Field(default=None, description="""A relationship indicating the datasets an AI model was trained on.""", json_schema_extra = { "linkml_meta": {'alias': 'hasTrainingData',
         'domain_of': ['LargeLanguageModel'],
         'slot_uri': 'airo:hasTrainingData'} })
    fine_tuning: Optional[str] = Field(default=None, description="""A description of the fine-tuning mechanism(s) applied to a model.""", json_schema_extra = { "linkml_meta": {'alias': 'fine_tuning', 'domain_of': ['LargeLanguageModel']} })
    supported_languages: Optional[List[str]] = Field(default=None, description="""A list of languages, expressed as ISO two letter codes. For example, 'jp, fr, en, de'""", json_schema_extra = { "linkml_meta": {'alias': 'supported_languages', 'domain_of': ['LargeLanguageModel']} })
    isPartOf: Optional[str] = Field(default=None, description="""Annotation that a Large Language model is part of a family of models""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Adapter"] = Field(default="Adapter", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })
    hasEvaluation: Optional[List[str]] = Field(default=None, description="""A relationship indicating that an entity has an AI evaluation result.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvaluation',
         'domain_of': ['AiModel'],
         'slot_uri': 'dqv:hasQualityMeasurement'} })
    architecture: Optional[str] = Field(default=None, description="""A description of the architecture of an AI such as 'Decoder-only'.""", json_schema_extra = { "linkml_meta": {'alias': 'architecture', 'domain_of': ['AiModel']} })
    gpu_hours: Optional[int] = Field(default=None, description="""GPU consumption in terms of hours""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'gpu_hours', 'domain_of': ['AiModel']} })
    power_consumption_w: Optional[int] = Field(default=None, description="""power consumption in Watts""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'power_consumption_w', 'domain_of': ['AiModel']} })
    carbon_emitted: Optional[float] = Field(default=None, description="""The number of tons of carbon dioxide equivalent that are emitted during training""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'carbon_emitted',
         'domain_of': ['AiModel'],
         'unit': {'descriptive_name': 'tons of CO2 equivalent', 'symbol': 't CO2-eq'}} })
    hasRiskControl: Optional[List[str]] = Field(default=None, description="""Indicates the control measures associated with a system or component to modify risks.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRiskControl',
         'domain_of': ['AiModel'],
         'slot_uri': 'airo:hasRiskControl'} })
    producer: Optional[str] = Field(default=None, description="""A relationship to the Organization instance which produces this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'producer', 'domain_of': ['BaseAi']} })
    hasModelCard: Optional[List[str]] = Field(default=None, description="""A relationship to model card references.""", json_schema_extra = { "linkml_meta": {'alias': 'hasModelCard', 'domain_of': ['BaseAi']} })
    performsTask: Optional[List[str]] = Field(default=None, description="""relationship indicating the AI tasks an AI model can perform.""", json_schema_extra = { "linkml_meta": {'alias': 'performsTask', 'domain_of': ['BaseAi']} })
    isProvidedBy: Optional[str] = Field(default=None, description="""Indicates provider of an AI system or component.""", json_schema_extra = { "linkml_meta": {'alias': 'isProvidedBy',
         'domain_of': ['BaseAi'],
         'slot_uri': 'airo:isProvidedBy'} })


class LLMIntrinsic(Entry):
    """
    A capability that can be invoked through a well-defined API that is reasonably stable and independent of how the LLM intrinsic itself is implemented.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'ai:Capability',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_intrinsic'})

    hasRelatedRisk: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a risk""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedRisk',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['Term',
                       'LLMQuestionPolicy',
                       'Action',
                       'AiSystem',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic']} })
    hasRelatedTerm: Optional[List[str]] = Field(default=None, description="""A relationship where an entity relates to a term""", json_schema_extra = { "linkml_meta": {'alias': 'hasRelatedTerm',
         'any_of': [{'range': 'RiskConcept'}, {'range': 'Term'}],
         'domain': 'Any',
         'domain_of': ['LLMIntrinsic']} })
    hasDocumentation: Optional[List[str]] = Field(default=None, description="""Indicates documentation associated with an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'hasDocumentation',
         'domain_of': ['Dataset',
                       'Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Group',
                       'Entry',
                       'Term',
                       'Principle',
                       'RiskTaxonomy',
                       'RiskControlGroupTaxonomy',
                       'Action',
                       'BaseAi',
                       'LargeLanguageModelFamily',
                       'AiTaskTaxonomy',
                       'AiEval',
                       'EveryEvalAIResult',
                       'BenchmarkMetadataCard',
                       'Adapter',
                       'LLMIntrinsic'],
         'slot_uri': 'airo:hasDocumentation'} })
    isDefinedByVocabulary: Optional[str] = Field(default=None, description="""A relationship where a term or a term group is defined by a vocabulary""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByVocabulary',
         'domain_of': ['Entry', 'Term', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'schema:isPartOf'} })
    hasAdapter: Optional[List[str]] = Field(default=None, description="""The Adapter for the intrinsic""", json_schema_extra = { "linkml_meta": {'alias': 'hasAdapter', 'domain': 'LLMIntrinsic', 'domain_of': ['LLMIntrinsic']} })
    hasCapability: Optional[List[str]] = Field(default=None, description="""Indicates the technical capabilities this entry possesses.
""", json_schema_extra = { "linkml_meta": {'alias': 'hasCapability',
         'domain_of': ['AiSystem', 'Adapter', 'LLMIntrinsic'],
         'slot_uri': 'tech:hasCapability'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    isPartOf: Optional[str] = Field(default=None, description="""A relationship where an entity is part of another entity""", json_schema_extra = { "linkml_meta": {'alias': 'isPartOf',
         'domain_of': ['Entry',
                       'Risk',
                       'LargeLanguageModel',
                       'AiTaskGroup',
                       'Stakeholder',
                       'CapabilityGroup'],
         'slot_uri': 'schema:isPartOf'} })
    requiredByTask: Optional[List[str]] = Field(default=None, description="""Indicates that this entry is required to perform a specific AI task.""", json_schema_extra = { "linkml_meta": {'alias': 'requiredByTask',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'requiresCapability'} })
    requiresCapability: Optional[List[str]] = Field(default=None, description="""Indicates that this entry requires a specific capability""", json_schema_extra = { "linkml_meta": {'alias': 'requiresCapability',
         'domain': 'Any',
         'domain_of': ['Entry', 'LargeLanguageModel', 'AiTask', 'Adapter'],
         'inverse': 'requiredByTask'} })
    implementedByAdapter: Optional[List[str]] = Field(default=None, description="""Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters).""", json_schema_extra = { "linkml_meta": {'alias': 'implementedByAdapter',
         'domain': 'Any',
         'domain_of': ['Entry', 'Capability'],
         'inverse': 'implementsCapability'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["LLMIntrinsic"] = Field(default="LLMIntrinsic", description="""The entry type.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class AiOffice(Organization):
    """
    The EU AI Office (https://digital-strategy.ec.europa.eu/en/policies/ai-office)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Organization',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/eu_ai_act'})

    grants_license: Optional[str] = Field(default=None, description="""A relationship from a granting entity such as an Organization to a License instance.""", json_schema_extra = { "linkml_meta": {'alias': 'grants_license', 'domain_of': ['Organization']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ControlActivity(Rule):
    """
    An obligation, permission, or prohibition for AI system assurance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_aiuc',
         'mixin': True})

    hasControlApplication: Optional[AIUC1ControlApplicationCategory] = Field(default=None, description="""Which of the AIUC-1 ControlApplicationCategory this control activity (rule) belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasControlApplication',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasControlApplication'} })
    hasEvidenceCategory: Optional[List[AIUC1EvidenceCategory]] = Field(default=None, description="""The evidence category, ie Technical Implementation, Operational Practices, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceCategory',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasEvidenceCategory'} })
    hasTypicalLocation: Optional[List[str]] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalLocation',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalLocation'} })
    appliesToCapability: Optional[List[str]] = Field(default=None, description="""This evidence only applies to AI systems with this capability""", json_schema_extra = { "linkml_meta": {'alias': 'appliesToCapability',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:appliesToCapability'} })
    hasRequirement: Optional[str] = Field(default=None, description="""This requirement this rule belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirement',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasRequirement'} })
    hasRequirementType: Optional[AIUC1RequirementType] = Field(default=None, description="""The requirement type of whether this is preventive, detective, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirementType',
         'domain': 'Any',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:hasRequirementType'} })
    hasTypicalEvidence: Optional[str] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalEvidence',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalEvidence'} })
    type: Literal["ControlActivity"] = Field(default="ControlActivity", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ControlActivityPermission(ControlActivity, Permission):
    """
    A control activity (rule) describing a permission to perform an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:ControlActivityPermission',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_aiuc',
         'mixins': ['ControlActivity']})

    type: Literal["ControlActivityPermission"] = Field(default="ControlActivityPermission", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    hasControlApplication: Optional[AIUC1ControlApplicationCategory] = Field(default=None, description="""Which of the AIUC-1 ControlApplicationCategory this control activity (rule) belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasControlApplication',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasControlApplication'} })
    hasEvidenceCategory: Optional[List[AIUC1EvidenceCategory]] = Field(default=None, description="""The evidence category, ie Technical Implementation, Operational Practices, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceCategory',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasEvidenceCategory'} })
    hasTypicalLocation: Optional[List[str]] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalLocation',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalLocation'} })
    appliesToCapability: Optional[List[str]] = Field(default=None, description="""This evidence only applies to AI systems with this capability""", json_schema_extra = { "linkml_meta": {'alias': 'appliesToCapability',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:appliesToCapability'} })
    hasRequirement: Optional[str] = Field(default=None, description="""This requirement this rule belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirement',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasRequirement'} })
    hasRequirementType: Optional[AIUC1RequirementType] = Field(default=None, description="""The requirement type of whether this is preventive, detective, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirementType',
         'domain': 'Any',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:hasRequirementType'} })
    hasTypicalEvidence: Optional[str] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalEvidence',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalEvidence'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ControlActivityProhibition(ControlActivity, Prohibition):
    """
    A control activity (rule) describing a prohibition to perform an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:ControlActivityProhibition',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_aiuc',
         'mixins': ['ControlActivity']})

    type: Literal["ControlActivityProhibition"] = Field(default="ControlActivityProhibition", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    hasControlApplication: Optional[AIUC1ControlApplicationCategory] = Field(default=None, description="""Which of the AIUC-1 ControlApplicationCategory this control activity (rule) belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasControlApplication',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasControlApplication'} })
    hasEvidenceCategory: Optional[List[AIUC1EvidenceCategory]] = Field(default=None, description="""The evidence category, ie Technical Implementation, Operational Practices, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceCategory',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasEvidenceCategory'} })
    hasTypicalLocation: Optional[List[str]] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalLocation',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalLocation'} })
    appliesToCapability: Optional[List[str]] = Field(default=None, description="""This evidence only applies to AI systems with this capability""", json_schema_extra = { "linkml_meta": {'alias': 'appliesToCapability',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:appliesToCapability'} })
    hasRequirement: Optional[str] = Field(default=None, description="""This requirement this rule belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirement',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasRequirement'} })
    hasRequirementType: Optional[AIUC1RequirementType] = Field(default=None, description="""The requirement type of whether this is preventive, detective, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirementType',
         'domain': 'Any',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:hasRequirementType'} })
    hasTypicalEvidence: Optional[str] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalEvidence',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalEvidence'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ControlActivityObligation(ControlActivity, Obligation):
    """
    A control activity (rule) describing an obligation for performing an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:ControlActivityObligation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_aiuc',
         'mixins': ['ControlActivity']})

    type: Literal["ControlActivityObligation"] = Field(default="ControlActivityObligation", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    hasControlApplication: Optional[AIUC1ControlApplicationCategory] = Field(default=None, description="""Which of the AIUC-1 ControlApplicationCategory this control activity (rule) belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasControlApplication',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasControlApplication'} })
    hasEvidenceCategory: Optional[List[AIUC1EvidenceCategory]] = Field(default=None, description="""The evidence category, ie Technical Implementation, Operational Practices, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceCategory',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasEvidenceCategory'} })
    hasTypicalLocation: Optional[List[str]] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalLocation',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalLocation'} })
    appliesToCapability: Optional[List[str]] = Field(default=None, description="""This evidence only applies to AI systems with this capability""", json_schema_extra = { "linkml_meta": {'alias': 'appliesToCapability',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:appliesToCapability'} })
    hasRequirement: Optional[str] = Field(default=None, description="""This requirement this rule belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirement',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasRequirement'} })
    hasRequirementType: Optional[AIUC1RequirementType] = Field(default=None, description="""The requirement type of whether this is preventive, detective, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirementType',
         'domain': 'Any',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:hasRequirementType'} })
    hasTypicalEvidence: Optional[str] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalEvidence',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalEvidence'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class ControlActivityRecommendation(ControlActivity, Recommendation):
    """
    A control activity (rule) describing a recommendation for performing an activity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nexus:ControlActivityRecommendation',
         'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_aiuc',
         'mixins': ['ControlActivity']})

    type: Literal["ControlActivityRecommendation"] = Field(default="ControlActivityRecommendation", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    hasControlApplication: Optional[AIUC1ControlApplicationCategory] = Field(default=None, description="""Which of the AIUC-1 ControlApplicationCategory this control activity (rule) belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasControlApplication',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasControlApplication'} })
    hasEvidenceCategory: Optional[List[AIUC1EvidenceCategory]] = Field(default=None, description="""The evidence category, ie Technical Implementation, Operational Practices, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceCategory',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasEvidenceCategory'} })
    hasTypicalLocation: Optional[List[str]] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalLocation',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalLocation'} })
    appliesToCapability: Optional[List[str]] = Field(default=None, description="""This evidence only applies to AI systems with this capability""", json_schema_extra = { "linkml_meta": {'alias': 'appliesToCapability',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:appliesToCapability'} })
    hasRequirement: Optional[str] = Field(default=None, description="""This requirement this rule belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirement',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasRequirement'} })
    hasRequirementType: Optional[AIUC1RequirementType] = Field(default=None, description="""The requirement type of whether this is preventive, detective, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirementType',
         'domain': 'Any',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:hasRequirementType'} })
    hasTypicalEvidence: Optional[str] = Field(default=None, description="""The evidence is usually found here""", json_schema_extra = { "linkml_meta": {'alias': 'hasTypicalEvidence',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity'],
         'slot_uri': 'nexus:hasTypicalEvidence'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Specifying applicability or inclusion of a rule within specified context.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Requirement(Rule):
    """
    A requirement representing a combination of obligation, permission, or prohibition for AI system assurance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai_aiuc',
         'slot_usage': {'hasRule': {'description': 'Relationship indicating the '
                                                   'control activities (rules) of '
                                                   'which the requirement is composed.',
                                    'inlined': False,
                                    'name': 'hasRule'}}})

    hasApplication: Optional[List[AIUC1ApplicationCategory]] = Field(default=None, description="""The application category, Optional or Mandatory.""", json_schema_extra = { "linkml_meta": {'alias': 'hasApplication',
         'domain': 'Requirement',
         'domain_of': ['Requirement'],
         'slot_uri': 'nexus:hasApplication'} })
    hasFrequency: Optional[AIUC1Frequency] = Field(default=None, description="""The frequency""", json_schema_extra = { "linkml_meta": {'alias': 'hasFrequency',
         'domain': 'Requirement',
         'domain_of': ['Requirement'],
         'slot_uri': 'nexus:hasFrequency'} })
    hasKeywords: Optional[List[str]] = Field(default=None, description="""A collection of keywords""", json_schema_extra = { "linkml_meta": {'alias': 'hasKeywords',
         'domain': 'Requirement',
         'domain_of': ['Requirement'],
         'slot_uri': 'nexus:hasKeywords'} })
    hasPrinciple: Optional[List[str]] = Field(default=None, description="""Which of the AIUC-1 principles this requirement belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'hasPrinciple',
         'domain': 'Requirement',
         'domain_of': ['Requirement'],
         'slot_uri': 'dpv:isPartOf'} })
    appliesToCapability: Optional[List[str]] = Field(default=None, description="""This evidence only applies to AI systems with this capability""", json_schema_extra = { "linkml_meta": {'alias': 'appliesToCapability',
         'domain': 'ControlActivity',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:appliesToCapability'} })
    hasRequirementType: Optional[AIUC1RequirementType] = Field(default=None, description="""The requirement type of whether this is preventive, detective, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRequirementType',
         'domain': 'Any',
         'domain_of': ['ControlActivity', 'Requirement'],
         'slot_uri': 'nexus:hasRequirementType'} })
    isDefinedByTaxonomy: Optional[str] = Field(default=None, description="""A relationship where a concept or a concept group is defined by a taxonomy""", json_schema_extra = { "linkml_meta": {'alias': 'isDefinedByTaxonomy',
         'domain_of': ['Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'RiskControlGroup',
                       'RiskGroup',
                       'Risk',
                       'RiskControl',
                       'Action',
                       'RiskIncident',
                       'AiTaskDomain',
                       'AiTaskGroup',
                       'Stakeholder',
                       'StakeholderGroup',
                       'CapabilityGroup',
                       'Requirement'],
         'slot_uri': 'schema:isPartOf'} })
    hasRule: Optional[List[str]] = Field(default=None, description="""Relationship indicating the control activities (rules) of which the requirement is composed.""", json_schema_extra = { "linkml_meta": {'alias': 'hasRule',
         'domain_of': ['Entry', 'LLMQuestionPolicy', 'Rule', 'Requirement'],
         'slot_uri': 'dpv:hasRule'} })
    type: Literal["Requirement"] = Field(default="Requirement", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'designates_type': True,
         'domain_of': ['Vocabulary',
                       'Taxonomy',
                       'Concept',
                       'Control',
                       'Group',
                       'Entry',
                       'Policy',
                       'Rule',
                       'Permission',
                       'Prohibition',
                       'Obligation',
                       'Recommendation',
                       'Certification',
                       'BenchmarkMetadataCard',
                       'ControlActivity',
                       'ControlActivityPermission',
                       'ControlActivityProhibition',
                       'ControlActivityObligation',
                       'ControlActivityRecommendation',
                       'Requirement']} })
    id: str = Field(default=..., description="""A unique identifier to this instance of the model element. Example identifiers include UUID, URI, URN, etc.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Entity'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A text name of this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Entity', 'BenchmarkMetadataCard'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""The description of an entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:description'} })
    url: Optional[str] = Field(default=None, description="""An optional URL associated with this instance.""", json_schema_extra = { "linkml_meta": {'alias': 'url', 'domain_of': ['Entity'], 'slot_uri': 'schema:url'} })
    dateCreated: Optional[date] = Field(default=None, description="""The date on which the entity was created.""", json_schema_extra = { "linkml_meta": {'alias': 'dateCreated',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateCreated'} })
    dateModified: Optional[date] = Field(default=None, description="""The date on which the entity was most recently modified.""", json_schema_extra = { "linkml_meta": {'alias': 'dateModified',
         'domain_of': ['Entity'],
         'slot_uri': 'schema:dateModified'} })
    exact_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications""", json_schema_extra = { "linkml_meta": {'alias': 'exact_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:exactMatch'} })
    close_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications.""", json_schema_extra = { "linkml_meta": {'alias': 'close_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:closeMatch'} })
    related_mappings: Optional[List[Any]] = Field(default=None, description="""The property skos:relatedMatch is used to state an associative mapping link between two concepts.""", json_schema_extra = { "linkml_meta": {'alias': 'related_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:relatedMatch'} })
    narrow_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'narrow_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:narrowMatch'} })
    broad_mappings: Optional[List[Any]] = Field(default=None, description="""The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a broader concept than the originating concept.""", json_schema_extra = { "linkml_meta": {'alias': 'broad_mappings',
         'domain_of': ['Entity'],
         'slot_uri': 'skos:broadMatch'} })
    isCategorizedAs: Optional[List[Any]] = Field(default=None, description="""A relationship where an entity has been deemed to be categorized""", json_schema_extra = { "linkml_meta": {'alias': 'isCategorizedAs',
         'domain_of': ['Entity'],
         'slot_uri': 'nexus:isCategorizedAs'} })


class Container(ConfiguredBaseModel):
    """
    An umbrella object that holds the ontology class instances
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology',
         'tree_root': True})

    organizations: Optional[List[Organization]] = Field(default=None, description="""A list of organizations""", json_schema_extra = { "linkml_meta": {'alias': 'organizations', 'domain_of': ['Container']} })
    licenses: Optional[List[License]] = Field(default=None, description="""A list of licenses""", json_schema_extra = { "linkml_meta": {'alias': 'licenses', 'domain_of': ['Container']} })
    modalities: Optional[List[Modality]] = Field(default=None, description="""A list of AI modalities""", json_schema_extra = { "linkml_meta": {'alias': 'modalities', 'domain_of': ['Container']} })
    aitasks: Optional[List[AiTask]] = Field(default=None, description="""A list of AI tasks""", json_schema_extra = { "linkml_meta": {'alias': 'aitasks', 'domain_of': ['Container']} })
    documents: Optional[List[Documentation]] = Field(default=None, description="""A list of documents""", json_schema_extra = { "linkml_meta": {'alias': 'documents', 'domain_of': ['Container']} })
    datasets: Optional[List[Dataset]] = Field(default=None, description="""A list of data sets""", json_schema_extra = { "linkml_meta": {'alias': 'datasets', 'domain_of': ['Container']} })
    llmintrinsics: Optional[List[LLMIntrinsic]] = Field(default=None, description="""A list of LLMIntrinsics""", json_schema_extra = { "linkml_meta": {'alias': 'llmintrinsics', 'domain_of': ['Container']} })
    adapters: Optional[List[Adapter]] = Field(default=None, description="""A list of Adapters""", json_schema_extra = { "linkml_meta": {'alias': 'adapters', 'domain_of': ['Container']} })
    taxonomies: Optional[List[Union[Taxonomy,RiskTaxonomy,RiskControlGroupTaxonomy,AiTaskTaxonomy,CapabilityTaxonomy]]] = Field(default=None, description="""A list of taxonomies""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomies', 'domain_of': ['Container']} })
    concepts: Optional[List[Union[Concept,RiskConcept,CapabilityConcept,CapabilityDomain,CapabilityGroup,Capability,RiskControlGroup,RiskGroup,Risk,RiskControl,RiskIncident,Impact,Action]]] = Field(default=None, description="""A list of concepts""", json_schema_extra = { "linkml_meta": {'alias': 'concepts', 'domain_of': ['Container']} })
    entries: Optional[List[Union[Entry,Term,Principle,Certification,Risk,AiSystem,AiTask,Purpose,Domain,LocalityOfUse,Capability,Adapter,LLMIntrinsic,AiAgent]]] = Field(default=None, description="""A list of entries""", json_schema_extra = { "linkml_meta": {'alias': 'entries', 'domain_of': ['Container']} })
    groups: Optional[List[Union[Group,RiskControlGroup,RiskGroup,AiTaskDomain,AiTaskGroup,StakeholderGroup,CapabilityDomain,CapabilityGroup]]] = Field(default=None, description="""A list of groups""", json_schema_extra = { "linkml_meta": {'alias': 'groups', 'domain_of': ['Container']} })
    vocabularies: Optional[List[Vocabulary]] = Field(default=None, description="""A list of vocabularies""", json_schema_extra = { "linkml_meta": {'alias': 'vocabularies', 'domain_of': ['Container']} })
    controls: Optional[List[Union[Control,RiskControl,Action]]] = Field(default=None, description="""A list of AI controls""", json_schema_extra = { "linkml_meta": {'alias': 'controls', 'domain_of': ['Container']} })
    riskincidents: Optional[List[RiskIncident]] = Field(default=None, description="""A list of AI risk incidents""", json_schema_extra = { "linkml_meta": {'alias': 'riskincidents', 'domain_of': ['Container']} })
    stakeholdergroups: Optional[List[StakeholderGroup]] = Field(default=None, description="""A list of AI stakeholder groups""", json_schema_extra = { "linkml_meta": {'alias': 'stakeholdergroups', 'domain_of': ['Container']} })
    stakeholders: Optional[List[Stakeholder]] = Field(default=None, description="""A list of stakeholders""", json_schema_extra = { "linkml_meta": {'alias': 'stakeholders', 'domain_of': ['Container']} })
    actions: Optional[List[Action]] = Field(default=None, description="""A list of risk related actions""", json_schema_extra = { "linkml_meta": {'alias': 'actions', 'domain_of': ['Container']} })
    evaluations: Optional[List[AiEval]] = Field(default=None, description="""A list of AI evaluation methods""", json_schema_extra = { "linkml_meta": {'alias': 'evaluations', 'domain_of': ['Container']} })
    aievalresults: Optional[List[AiEvalResult]] = Field(default=None, description="""A list of AI evaluation results""", json_schema_extra = { "linkml_meta": {'alias': 'aievalresults', 'domain_of': ['Container']} })
    benchmarkmetadatacards: Optional[List[BenchmarkMetadataCard]] = Field(default=None, description="""A list of AI evaluation benchmark metadata cards""", json_schema_extra = { "linkml_meta": {'alias': 'benchmarkmetadatacards', 'domain_of': ['Container']} })
    aimodelfamilies: Optional[List[LargeLanguageModelFamily]] = Field(default=None, description="""A list of AI model families""", json_schema_extra = { "linkml_meta": {'alias': 'aimodelfamilies', 'domain_of': ['Container']} })
    aimodels: Optional[List[LargeLanguageModel]] = Field(default=None, description="""A list of AI models""", json_schema_extra = { "linkml_meta": {'alias': 'aimodels', 'domain_of': ['Container']} })
    policies: Optional[List[Union[Policy,LLMQuestionPolicy]]] = Field(default=None, description="""A list of policies""", json_schema_extra = { "linkml_meta": {'alias': 'policies', 'domain_of': ['Container']} })
    rules: Optional[List[Union[Rule,AttributeConditionRule,Permission,Prohibition,Obligation,Recommendation,ControlActivity,Requirement,ControlActivityPermission,ControlActivityProhibition,ControlActivityObligation,ControlActivityRecommendation]]] = Field(default=None, description="""A list of rules""", json_schema_extra = { "linkml_meta": {'alias': 'rules', 'domain_of': ['Container']} })
    prohibitions: Optional[List[Union[Prohibition,ControlActivityProhibition]]] = Field(default=None, description="""A list of prohibitions""", json_schema_extra = { "linkml_meta": {'alias': 'prohibitions', 'domain_of': ['Container']} })
    permissions: Optional[List[Union[Permission,ControlActivityPermission]]] = Field(default=None, description="""A list of Permissions""", json_schema_extra = { "linkml_meta": {'alias': 'permissions', 'domain_of': ['Container']} })
    obligations: Optional[List[Union[Obligation,ControlActivityObligation]]] = Field(default=None, description="""A list of Obligations""", json_schema_extra = { "linkml_meta": {'alias': 'obligations', 'domain_of': ['Container']} })


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
AttributeConditionRule.model_rebuild()
AnonymousClassExpression.model_rebuild()
SlotCondition.model_rebuild()
Permission.model_rebuild()
Prohibition.model_rebuild()
Obligation.model_rebuild()
Recommendation.model_rebuild()
Certification.model_rebuild()
RiskTaxonomy.model_rebuild()
RiskControlGroupTaxonomy.model_rebuild()
RiskConcept.model_rebuild()
RiskControlGroup.model_rebuild()
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
LargeLanguageModelFamily.model_rebuild()
AiTask.model_rebuild()
AiTaskTaxonomy.model_rebuild()
AiTaskDomain.model_rebuild()
AiTaskGroup.model_rebuild()
AiLifecyclePhase.model_rebuild()
DataPreprocessing.model_rebuild()
AiModelValidation.model_rebuild()
AiProvider.model_rebuild()
Modality.model_rebuild()
Input.model_rebuild()
Purpose.model_rebuild()
Domain.model_rebuild()
LocalityOfUse.model_rebuild()
AIComponent.model_rebuild()
AiModel.model_rebuild()
LargeLanguageModel.model_rebuild()
Stakeholder.model_rebuild()
AISubject.model_rebuild()
AIOperator.model_rebuild()
AIDeveloper.model_rebuild()
AIDeployer.model_rebuild()
AIUser.model_rebuild()
StakeholderGroup.model_rebuild()
CapabilityTaxonomy.model_rebuild()
CapabilityConcept.model_rebuild()
CapabilityDomain.model_rebuild()
CapabilityGroup.model_rebuild()
Capability.model_rebuild()
AiEval.model_rebuild()
AiEvalResult.model_rebuild()
SourceMetadata.model_rebuild()
ModelInfo.model_rebuild()
SourceData.model_rebuild()
MetricConfig.model_rebuild()
ScoreDetails.model_rebuild()
EvaluationResultRecord.model_rebuild()
EveryEvalAIResult.model_rebuild()
BenchmarkMetadataCard.model_rebuild()
Question.model_rebuild()
Questionnaire.model_rebuild()
Adapter.model_rebuild()
LLMIntrinsic.model_rebuild()
AiOffice.model_rebuild()
ControlActivity.model_rebuild()
ControlActivityPermission.model_rebuild()
ControlActivityProhibition.model_rebuild()
ControlActivityObligation.model_rebuild()
ControlActivityRecommendation.model_rebuild()
Requirement.model_rebuild()
Container.model_rebuild()
