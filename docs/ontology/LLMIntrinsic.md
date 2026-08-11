---
search:
  boost: 10.0
---

# Class: LLMIntrinsic

_A capability that can be invoked through a well-defined API that is reasonably stable and independent of how the LLM intrinsic itself is implemented._

<div data-search-exclude markdown="1">

URI: [ai:Capability](https://w3id.org/dpv/ai#Capability)

```mermaid
 classDiagram
    class LLMIntrinsic
    click LLMIntrinsic href "../LLMIntrinsic/"
      Entry <|-- LLMIntrinsic
        click Entry href "../Entry/"

      LLMIntrinsic : broad_mappings





        LLMIntrinsic --> "*" Any : broad_mappings
        click Any href "../Any/"



      LLMIntrinsic : close_mappings





        LLMIntrinsic --> "*" Any : close_mappings
        click Any href "../Any/"



      LLMIntrinsic : dateCreated

      LLMIntrinsic : dateModified

      LLMIntrinsic : description

      LLMIntrinsic : exact_mappings





        LLMIntrinsic --> "*" Any : exact_mappings
        click Any href "../Any/"



      LLMIntrinsic : hasAdapter





        LLMIntrinsic --> "*" Adapter : hasAdapter
        click Adapter href "../Adapter/"



      LLMIntrinsic : hasCapability





        LLMIntrinsic --> "*" Capability : hasCapability
        click Capability href "../Capability/"



      LLMIntrinsic : hasDocumentation





        LLMIntrinsic --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      LLMIntrinsic : hasExternalReference





        LLMIntrinsic --> "*" Documentation : hasExternalReference
        click Documentation href "../Documentation/"



      LLMIntrinsic : hasLifecycleStatus





        LLMIntrinsic --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      LLMIntrinsic : hasRelatedRisk





        LLMIntrinsic --> "*" RiskConcept : hasRelatedRisk
        click RiskConcept href "../RiskConcept/"



      LLMIntrinsic : hasRelatedTerm





        LLMIntrinsic --> "*" Term : hasRelatedTerm
        click Term href "../Term/"



      LLMIntrinsic : hasRule





        LLMIntrinsic --> "*" Rule : hasRule
        click Rule href "../Rule/"



      LLMIntrinsic : id

      LLMIntrinsic : implementedByAdapter





        LLMIntrinsic --> "*" Any : implementedByAdapter
        click Any href "../Any/"



      LLMIntrinsic : implementsCapability





        LLMIntrinsic --> "*" Capability : implementsCapability
        click Capability href "../Capability/"



      LLMIntrinsic : isCategorizedAs





        LLMIntrinsic --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      LLMIntrinsic : isDefinedByTaxonomy





        LLMIntrinsic --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      LLMIntrinsic : isDefinedByVocabulary





        LLMIntrinsic --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      LLMIntrinsic : isPartOf

      LLMIntrinsic : name

      LLMIntrinsic : narrow_mappings





        LLMIntrinsic --> "*" Any : narrow_mappings
        click Any href "../Any/"



      LLMIntrinsic : related_mappings





        LLMIntrinsic --> "*" Any : related_mappings
        click Any href "../Any/"



      LLMIntrinsic : requiredByTask





        LLMIntrinsic --> "*" Any : requiredByTask
        click Any href "../Any/"



      LLMIntrinsic : requiresCapability





        LLMIntrinsic --> "*" Any : requiresCapability
        click Any href "../Any/"



      LLMIntrinsic : type

      LLMIntrinsic : url


```

## Inheritance

- [Entity](Entity.md)
  - [Entry](Entry.md)
    - **LLMIntrinsic**

## Class Properties

| Property  | Value                                               |
| --------- | --------------------------------------------------- |
| Class URI | [ai:Capability](https://w3id.org/dpv/ai#Capability) |

## Slots

| Name                                              | Cardinality and Range                                                     | Description                                                                      | Inheritance         |
| ------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------- |
| [hasRelatedRisk](hasRelatedRisk.md)               | \* <br/> [RiskConcept](RiskConcept.md)                                    | A relationship where an entity relates to a risk                                 | direct              |
| [hasRelatedTerm](hasRelatedTerm.md)               | \* <br/> [RiskConcept](RiskConcept.md)&nbsp;or&nbsp;<br />[Term](Term.md) | A relationship where an entity relates to a term                                 | direct              |
| [hasDocumentation](hasDocumentation.md)           | \* <br/> [Documentation](Documentation.md)                                | Indicates documentation associated with an entity                                | direct              |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md)                                    | A relationship where a term or a term group is defined by a vocabulary           | direct              |
| [hasAdapter](hasAdapter.md)                       | \* <br/> [Adapter](Adapter.md)                                            | The Adapter for the intrinsic                                                    | direct              |
| [hasCapability](hasCapability.md)                 | \* <br/> [Capability](Capability.md)                                      | Indicates the technical capabilities this entry possesses                        | direct              |
| [implementsCapability](implementsCapability.md)   | \* <br/> [Capability](Capability.md)                                      | Indicates that this entity implements a specific capability                      | direct              |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)     | 0..1 <br/> [Taxonomy](Taxonomy.md)                                        | A relationship where a concept or a concept group is defined by a taxonomy       | [Entry](Entry.md)   |
| [hasExternalReference](hasExternalReference.md)   | \* <br/> [Documentation](Documentation.md)                                | External references / additional resources related to this entity, such as ar... | [Entry](Entry.md)   |
| [isPartOf](isPartOf.md)                           | 0..1 <br/> [String](String.md)                                            | A relationship where an entity is part of another entity                         | [Entry](Entry.md)   |
| [requiredByTask](requiredByTask.md)               | \* <br/> [Any](Any.md)                                                    | Indicates that this entry is required to perform a specific AI task              | [Entry](Entry.md)   |
| [requiresCapability](requiresCapability.md)       | \* <br/> [Any](Any.md)                                                    | Indicates that this entry requires a specific capability                         | [Entry](Entry.md)   |
| [implementedByAdapter](implementedByAdapter.md)   | \* <br/> [Any](Any.md)                                                    | Indicates that this capability is implemented by a specific adapter              | [Entry](Entry.md)   |
| [hasRule](hasRule.md)                             | \* <br/> [Rule](Rule.md)                                                  | Specifying applicability or inclusion of a rule within specified context         | [Entry](Entry.md)   |
| [type](type.md)                                   | 0..1 <br/> [String](String.md)                                            | The entry type or class designation specifying what kind of entry this is        | [Entry](Entry.md)   |
| [id](id.md)                                       | 1 <br/> [String](String.md)                                               | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                                   | 0..1 <br/> [String](String.md)                                            | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)                     | 0..1 <br/> [String](String.md)                                            | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                                     | 0..1 <br/> [Uri](Uri.md)                                                  | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)                     | 0..1 <br/> [Date](Date.md)                                                | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)                   | 0..1 <br/> [Date](Date.md)                                                | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)               | \* <br/> [Any](Any.md)                                                    | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)               | \* <br/> [Any](Any.md)                                                    | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)           | \* <br/> [Any](Any.md)                                                    | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)             | \* <br/> [Any](Any.md)                                                    | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)               | \* <br/> [Any](Any.md)                                                    | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)             | \* <br/> [Any](Any.md)                                                    | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |
| [hasLifecycleStatus](hasLifecycleStatus.md)       | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md)                          | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md) |

## Usages

| used by                         | used in                                         | type   | used                            |
| ------------------------------- | ----------------------------------------------- | ------ | ------------------------------- |
| [Container](Container.md)       | [llmintrinsics](llmintrinsics.md)               | range  | [LLMIntrinsic](LLMIntrinsic.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [hasRelatedRisk](hasRelatedRisk.md)             | domain | [LLMIntrinsic](LLMIntrinsic.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [hasAdapter](hasAdapter.md)                     | domain | [LLMIntrinsic](LLMIntrinsic.md) |
| [LLMIntrinsic](LLMIntrinsic.md) | [implementsCapability](implementsCapability.md) | domain | [LLMIntrinsic](LLMIntrinsic.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | ai:Capability      |
| native       | nexus:LLMIntrinsic |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LLMIntrinsic
description: A capability that can be invoked through a well-defined API that is reasonably
  stable and independent of how the LLM intrinsic itself is implemented.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entry
slots:
- hasRelatedRisk
- hasRelatedTerm
- hasDocumentation
- isDefinedByVocabulary
- hasAdapter
- hasCapability
- implementsCapability
slot_usage:
  implementsCapability:
    name: implementsCapability
    domain: LLMIntrinsic
    inverse: implementedByIntrinsic
    range: Capability
  hasRelatedRisk:
    name: hasRelatedRisk
    domain: LLMIntrinsic
    range: RiskConcept
class_uri: ai:Capability

````
</details>

### Induced

<details>
```yaml
name: LLMIntrinsic
description: A capability that can be invoked through a well-defined API that is reasonably
  stable and independent of how the LLM intrinsic itself is implemented.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entry
slot_usage:
  implementsCapability:
    name: implementsCapability
    domain: LLMIntrinsic
    inverse: implementedByIntrinsic
    range: Capability
  hasRelatedRisk:
    name: hasRelatedRisk
    domain: LLMIntrinsic
    range: RiskConcept
attributes:
  hasRelatedRisk:
    name: hasRelatedRisk
    description: A relationship where an entity relates to a risk
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: LLMIntrinsic
    alias: hasRelatedRisk
    owner: LLMIntrinsic
    domain_of:
    - Term
    - LLMQuestionPolicy
    - Action
    - AiSystem
    - AiEval
    - EveryEvalAIResult
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: RiskConcept
    multivalued: true
    inlined: false
  hasRelatedTerm:
    name: hasRelatedTerm
    description: A relationship where an entity relates to a term
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: hasRelatedTerm
    owner: LLMIntrinsic
    domain_of:
    - LLMIntrinsic
    range: Term
    multivalued: true
    inlined: false
    any_of:
    - range: RiskConcept
    - range: Term
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: LLMIntrinsic
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
  isDefinedByVocabulary:
    name: isDefinedByVocabulary
    description: A relationship where a term or a term group is defined by a vocabulary
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByVocabulary
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - Term
    - Adapter
    - LLMIntrinsic
    range: Vocabulary
  hasAdapter:
    name: hasAdapter
    description: The Adapter for the intrinsic
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: LLMIntrinsic
    alias: hasAdapter
    owner: LLMIntrinsic
    domain_of:
    - LLMIntrinsic
    range: Adapter
    multivalued: true
    inlined: false
  hasCapability:
    name: hasCapability
    description: 'Indicates the technical capabilities this entry possesses.

      '
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: tech:hasCapability
    alias: hasCapability
    owner: LLMIntrinsic
    domain_of:
    - AiSystem
    - Adapter
    - LLMIntrinsic
    range: Capability
    multivalued: true
    inlined: false
  implementsCapability:
    name: implementsCapability
    description: Indicates that this entity implements a specific capability
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    domain: LLMIntrinsic
    alias: implementsCapability
    owner: LLMIntrinsic
    domain_of:
    - Adapter
    - LLMIntrinsic
    inverse: implementedByIntrinsic
    range: Capability
    multivalued: true
    inlined: false
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: LLMIntrinsic
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
    alias: hasExternalReference
    owner: LLMIntrinsic
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
    alias: isPartOf
    owner: LLMIntrinsic
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
    alias: requiredByTask
    owner: LLMIntrinsic
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
    alias: requiresCapability
    owner: LLMIntrinsic
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
    alias: implementedByAdapter
    owner: LLMIntrinsic
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
    alias: hasRule
    owner: LLMIntrinsic
    domain_of:
    - Entry
    - LLMQuestionPolicy
    - Rule
    - Requirement
    range: Rule
    multivalued: true
    inlined: false
  type:
    name: type
    description: The entry type or class designation specifying what kind of entry
      this is.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    designates_type: true
    alias: type
    owner: LLMIntrinsic
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
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: LLMIntrinsic
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
    alias: name
    owner: LLMIntrinsic
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
    alias: description
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    alias: url
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    alias: dateCreated
    owner: LLMIntrinsic
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
    alias: dateModified
    owner: LLMIntrinsic
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
    alias: exact_mappings
    owner: LLMIntrinsic
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
    alias: close_mappings
    owner: LLMIntrinsic
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
    alias: related_mappings
    owner: LLMIntrinsic
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
    alias: narrow_mappings
    owner: LLMIntrinsic
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
    alias: broad_mappings
    owner: LLMIntrinsic
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
    alias: isCategorizedAs
    owner: LLMIntrinsic
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
    alias: hasLifecycleStatus
    owner: LLMIntrinsic
    domain_of:
    - Entity
    range: LifecycleStatus
class_uri: ai:Capability

````

</details></div>
