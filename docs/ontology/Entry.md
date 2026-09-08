---
search:
  boost: 10.0
---

# Class: Entry

_An entry and its definitions._

<div data-search-exclude markdown="1">

- **NOTE**: this is an abstract class and should not be instantiated directly

URI: [nexus:Entry](https://w3id.org/ai-atlas-nexus/Entry)

```mermaid
 classDiagram
    class Entry
    click Entry href "../Entry/"
      Entity <|-- Entry
        click Entity href "../Entity/"


      Entry <|-- Term
        click Term href "../Term/"
      Entry <|-- Principle
        click Principle href "../Principle/"
      Entry <|-- Certification
        click Certification href "../Certification/"
      Entry <|-- LocalityOfUse
        click LocalityOfUse href "../LocalityOfUse/"
      Entry <|-- Risk
        click Risk href "../Risk/"
      Entry <|-- Capability
        click Capability href "../Capability/"
      Entry <|-- AiSystem
        click AiSystem href "../AiSystem/"
      Entry <|-- AiTask
        click AiTask href "../AiTask/"
      Entry <|-- Purpose
        click Purpose href "../Purpose/"
      Entry <|-- Domain
        click Domain href "../Domain/"
      Entry <|-- Adapter
        click Adapter href "../Adapter/"
      Entry <|-- LLMIntrinsic
        click LLMIntrinsic href "../LLMIntrinsic/"


      Entry : broad_mappings





        Entry --> "*" Any : broad_mappings
        click Any href "../Any/"



      Entry : close_mappings





        Entry --> "*" Any : close_mappings
        click Any href "../Any/"



      Entry : dateCreated

      Entry : dateModified

      Entry : description

      Entry : exact_mappings





        Entry --> "*" Any : exact_mappings
        click Any href "../Any/"



      Entry : hasDocumentation





        Entry --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      Entry : hasExternalReference





        Entry --> "*" Documentation : hasExternalReference
        click Documentation href "../Documentation/"



      Entry : hasLifecycleStatus





        Entry --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      Entry : hasRule





        Entry --> "*" Rule : hasRule
        click Rule href "../Rule/"



      Entry : id

      Entry : implementedByAdapter





        Entry --> "*" Any : implementedByAdapter
        click Any href "../Any/"



      Entry : isCategorizedAs





        Entry --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      Entry : isDefinedByTaxonomy





        Entry --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      Entry : isDefinedByVocabulary





        Entry --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      Entry : isPartOf

      Entry : name

      Entry : narrow_mappings





        Entry --> "*" Any : narrow_mappings
        click Any href "../Any/"



      Entry : notes

      Entry : related_mappings





        Entry --> "*" Any : related_mappings
        click Any href "../Any/"



      Entry : requiredByTask





        Entry --> "*" Any : requiredByTask
        click Any href "../Any/"



      Entry : requiresCapability





        Entry --> "*" Any : requiresCapability
        click Any href "../Any/"



      Entry : type

      Entry : url


```

## Inheritance

- [Entity](Entity.md)
  - **Entry**
    - [Term](Term.md)
    - [Principle](Principle.md)
    - [Certification](Certification.md)
    - [LocalityOfUse](LocalityOfUse.md)
    - [Risk](Risk.md) [ [RiskConcept](RiskConcept.md)]
    - [Capability](Capability.md) [ [CapabilityConcept](CapabilityConcept.md)]
    - [AiSystem](AiSystem.md) [ [BaseAi](BaseAi.md)]
    - [AiTask](AiTask.md)
    - [Purpose](Purpose.md)
    - [Domain](Domain.md)
    - [Adapter](Adapter.md) [ [LargeLanguageModel](LargeLanguageModel.md)]
    - [LLMIntrinsic](LLMIntrinsic.md)

## Class Properties

| Property  | Value                                                |
| --------- | ---------------------------------------------------- |
| Class URI | [nexus:Entry](https://w3id.org/ai-atlas-nexus/Entry) |

## Slots

| Name                                              | Cardinality and Range                            | Description                                                                      | Inheritance         |
| ------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)     | 0..1 <br/> [Taxonomy](Taxonomy.md)               | A relationship where a concept or a concept group is defined by a taxonomy       | direct              |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md)           | A relationship where a term or a term group is defined by a vocabulary           | direct              |
| [hasDocumentation](hasDocumentation.md)           | \* <br/> [Documentation](Documentation.md)       | Indicates documentation associated with an entity                                | direct              |
| [hasExternalReference](hasExternalReference.md)   | \* <br/> [Documentation](Documentation.md)       | External references / additional resources related to this entity, such as ar... | direct              |
| [isPartOf](isPartOf.md)                           | 0..1 <br/> [String](String.md)                   | A relationship where an entity is part of another entity                         | direct              |
| [requiredByTask](requiredByTask.md)               | \* <br/> [Any](Any.md)                           | Indicates that this entry is required to perform a specific AI task              | direct              |
| [requiresCapability](requiresCapability.md)       | \* <br/> [Any](Any.md)                           | Indicates that this entry requires a specific capability                         | direct              |
| [implementedByAdapter](implementedByAdapter.md)   | \* <br/> [Any](Any.md)                           | Indicates that this capability is implemented by a specific adapter              | direct              |
| [hasRule](hasRule.md)                             | \* <br/> [Rule](Rule.md)                         | Specifying applicability or inclusion of a rule within specified context         | direct              |
| [type](type.md)                                   | 0..1 <br/> [String](String.md)                   | The entry type or class designation specifying what kind of entry this is        | direct              |
| [id](id.md)                                       | 1 <br/> [String](String.md)                      | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                                   | 0..1 <br/> [String](String.md)                   | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)                     | 0..1 <br/> [String](String.md)                   | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                                     | 0..1 <br/> [Uri](Uri.md)                         | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)                     | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)                   | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)               | \* <br/> [Any](Any.md)                           | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)               | \* <br/> [Any](Any.md)                           | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)           | \* <br/> [Any](Any.md)                           | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)             | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)               | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)             | \* <br/> [Any](Any.md)                           | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |
| [hasLifecycleStatus](hasLifecycleStatus.md)       | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md) | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md) |
| [notes](notes.md)                                 | \* <br/> [String](String.md)                     | Free-text editorial notes, source breadcrumbs, or build-time provenance that ... | [Entity](Entity.md) |

## Usages

| used by                           | used in                             | type   | used              |
| --------------------------------- | ----------------------------------- | ------ | ----------------- |
| [Container](Container.md)         | [entries](entries.md)               | range  | [Entry](Entry.md) |
| [Entry](Entry.md)                 | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Term](Term.md)                   | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Principle](Principle.md)         | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Certification](Certification.md) | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [LocalityOfUse](LocalityOfUse.md) | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Risk](Risk.md)                   | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [AiSystem](AiSystem.md)           | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [AiAgent](AiAgent.md)             | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [AiTask](AiTask.md)               | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Purpose](Purpose.md)             | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Domain](Domain.md)               | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [Adapter](Adapter.md)             | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |
| [LLMIntrinsic](LLMIntrinsic.md)   | [requiredByTask](requiredByTask.md) | domain | [Entry](Entry.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:Entry  |
| native       | nexus:Entry  |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Entry
description: An entry and its definitions.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
abstract: true
slots:
- isDefinedByTaxonomy
- isDefinedByVocabulary
- hasDocumentation
- hasExternalReference
- isPartOf
- requiredByTask
- requiresCapability
- implementedByAdapter
- hasRule
attributes:
  type:
    name: type
    description: The entry type or class designation specifying what kind of entry
      this is.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    designates_type: true
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - Permission
    - Prohibition
    - Obligation
    - Recommendation
    - Certification
    - BenchmarkMetadataCard
    - ControlActivity
    - ControlActivityPermission
    - ControlActivityProhibition
    - ControlActivityObligation
    - ControlActivityRecommendation
    - Requirement
    range: string
class_uri: nexus:Entry

````
</details>

### Induced

<details>
```yaml
name: Entry
description: An entry and its definitions.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
abstract: true
attributes:
  type:
    name: type
    description: The entry type or class designation specifying what kind of entry
      this is.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    designates_type: true
    owner: Entry
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - Permission
    - Prohibition
    - Obligation
    - Recommendation
    - Certification
    - BenchmarkMetadataCard
    - ControlActivity
    - ControlActivityPermission
    - ControlActivityProhibition
    - ControlActivityObligation
    - ControlActivityRecommendation
    - Requirement
    range: string
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: Entry
    domain_of:
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - RiskControlGroup
    - RiskGroup
    - Risk
    - RiskControl
    - Action
    - RiskIncident
    - CapabilityGroup
    - AiTaskDomain
    - AiTaskGroup
    - Stakeholder
    - StakeholderGroup
    - Requirement
    range: Taxonomy
  isDefinedByVocabulary:
    name: isDefinedByVocabulary
    description: A relationship where a term or a term group is defined by a vocabulary
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: Entry
    domain_of:
    - Entry
    - Term
    - Adapter
    - LLMIntrinsic
    range: Vocabulary
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    owner: Entry
    domain_of:
    - Dataset
    - Vocabulary
    - Taxonomy
    - Concept
    - Group
    - Entry
    - Term
    - Principle
    - RiskTaxonomy
    - RiskControlGroupTaxonomy
    - Action
    - BaseAi
    - LargeLanguageModelFamily
    - AiTaskTaxonomy
    - AiEval
    - EveryEvalAIResult
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Documentation
    multivalued: true
    inlined: false
  hasExternalReference:
    name: hasExternalReference
    description: External references / additional resources related to this entity,
      such as articles, tools, or datasets. Distinct from hasDocumentation, which
      documents the entity itself. External references are not necessarily curated
      or vetted, and quality will vary.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    aliases:
    - additional resources
    - external_links
    close_mappings:
    - rdfs:seeAlso
    rank: 1000
    slot_uri: nexus:hasExternalReference
    owner: Entry
    domain_of:
    - Control
    - Entry
    range: Documentation
    multivalued: true
    inlined: false
  isPartOf:
    name: isPartOf
    description: A relationship where an entity is part of another entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: Entry
    domain_of:
    - Entry
    - Risk
    - CapabilityGroup
    - LargeLanguageModel
    - AiTaskGroup
    - Stakeholder
    range: string
  requiredByTask:
    name: requiredByTask
    description: Indicates that this entry is required to perform a specific AI task.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: Entry
    owner: Entry
    domain_of:
    - Entry
    - Capability
    inverse: requiresCapability
    range: Any
    multivalued: true
    inlined: false
  requiresCapability:
    name: requiresCapability
    description: Indicates that this entry requires a specific capability
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: Any
    owner: Entry
    domain_of:
    - Entry
    - LargeLanguageModel
    - AiTask
    - Adapter
    inverse: requiredByTask
    range: Any
    multivalued: true
    inlined: false
  implementedByAdapter:
    name: implementedByAdapter
    description: Indicates that this capability is implemented by a specific adapter.
      This relationship distinguishes the abstract capability (what can be done) from
      the technical implementation mechanism (how it is added/extended via adapters).
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: Any
    owner: Entry
    domain_of:
    - Entry
    - Capability
    inverse: implementsCapability
    range: Any
    multivalued: true
    inlined: false
  hasRule:
    name: hasRule
    description: Specifying applicability or inclusion of a rule within specified
      context.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: dpv:hasRule
    owner: Entry
    domain_of:
    - Entry
    - LLMQuestionPolicy
    - Rule
    - Requirement
    range: Rule
    multivalued: true
    inlined: false
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: Entry
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    owner: Entry
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    owner: Entry
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: Entry
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: Entry
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    owner: Entry
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    owner: Entry
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    owner: Entry
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    owner: Entry
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  narrow_mappings:
    name: narrow_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a narrower concept than
      the originating concept.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    owner: Entry
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  broad_mappings:
    name: broad_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a broader concept than
      the originating concept.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    owner: Entry
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  isCategorizedAs:
    name: isCategorizedAs
    description: A relationship where an entity has been deemed to be categorized
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:isCategorizedAs
    owner: Entry
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  hasLifecycleStatus:
    name: hasLifecycleStatus
    description: The editorial / publication lifecycle state of this entity. Distinct
      from AiLifecyclePhase, which describes an AI system's runtime evolution rather
      than the editorial workflow of a catalogued entry.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    aliases:
    - lifecycle_status
    - doc_status
    rank: 1000
    slot_uri: adms:status
    owner: Entry
    domain_of:
    - Entity
    range: LifecycleStatus
  notes:
    name: notes
    description: Free-text editorial notes, source breadcrumbs, or build-time provenance
      that do not belong in the user-facing description. Opaque to consumers.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:note
    owner: Entry
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: nexus:Entry

````

</details></div>
