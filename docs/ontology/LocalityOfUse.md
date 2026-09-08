---
search:
  boost: 10.0
---

# Class: LocalityOfUse

_The area, e.g. facility or institution, in which an entity is used._

<div data-search-exclude markdown="1">

URI: [airo:LocalityOfUse](https://w3id.org/airo#LocalityOfUse)

```mermaid
 classDiagram
    class LocalityOfUse
    click LocalityOfUse href "../LocalityOfUse/"
      Entry <|-- LocalityOfUse
        click Entry href "../Entry/"

      LocalityOfUse : broad_mappings





        LocalityOfUse --> "*" Any : broad_mappings
        click Any href "../Any/"



      LocalityOfUse : close_mappings





        LocalityOfUse --> "*" Any : close_mappings
        click Any href "../Any/"



      LocalityOfUse : dateCreated

      LocalityOfUse : dateModified

      LocalityOfUse : description

      LocalityOfUse : exact_mappings





        LocalityOfUse --> "*" Any : exact_mappings
        click Any href "../Any/"



      LocalityOfUse : hasDocumentation





        LocalityOfUse --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      LocalityOfUse : hasExternalReference





        LocalityOfUse --> "*" Documentation : hasExternalReference
        click Documentation href "../Documentation/"



      LocalityOfUse : hasLifecycleStatus





        LocalityOfUse --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      LocalityOfUse : hasRule





        LocalityOfUse --> "*" Rule : hasRule
        click Rule href "../Rule/"



      LocalityOfUse : id

      LocalityOfUse : implementedByAdapter





        LocalityOfUse --> "*" Any : implementedByAdapter
        click Any href "../Any/"



      LocalityOfUse : isCategorizedAs





        LocalityOfUse --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      LocalityOfUse : isDefinedByTaxonomy





        LocalityOfUse --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      LocalityOfUse : isDefinedByVocabulary





        LocalityOfUse --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      LocalityOfUse : isPartOf

      LocalityOfUse : name

      LocalityOfUse : narrow_mappings





        LocalityOfUse --> "*" Any : narrow_mappings
        click Any href "../Any/"



      LocalityOfUse : notes

      LocalityOfUse : related_mappings





        LocalityOfUse --> "*" Any : related_mappings
        click Any href "../Any/"



      LocalityOfUse : requiredByTask





        LocalityOfUse --> "*" Any : requiredByTask
        click Any href "../Any/"



      LocalityOfUse : requiresCapability





        LocalityOfUse --> "*" Any : requiresCapability
        click Any href "../Any/"



      LocalityOfUse : type

      LocalityOfUse : url


```

## Inheritance

- [Entity](Entity.md)
  - [Entry](Entry.md)
    - **LocalityOfUse**

## Class Properties

| Property  | Value                                                     |
| --------- | --------------------------------------------------------- |
| Class URI | [airo:LocalityOfUse](https://w3id.org/airo#LocalityOfUse) |

## Slots

| Name                                              | Cardinality and Range                            | Description                                                                      | Inheritance         |
| ------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)     | 0..1 <br/> [Taxonomy](Taxonomy.md)               | A relationship where a concept or a concept group is defined by a taxonomy       | [Entry](Entry.md)   |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md)           | A relationship where a term or a term group is defined by a vocabulary           | [Entry](Entry.md)   |
| [hasDocumentation](hasDocumentation.md)           | \* <br/> [Documentation](Documentation.md)       | Indicates documentation associated with an entity                                | [Entry](Entry.md)   |
| [hasExternalReference](hasExternalReference.md)   | \* <br/> [Documentation](Documentation.md)       | External references / additional resources related to this entity, such as ar... | [Entry](Entry.md)   |
| [isPartOf](isPartOf.md)                           | 0..1 <br/> [String](String.md)                   | A relationship where an entity is part of another entity                         | [Entry](Entry.md)   |
| [requiredByTask](requiredByTask.md)               | \* <br/> [Any](Any.md)                           | Indicates that this entry is required to perform a specific AI task              | [Entry](Entry.md)   |
| [requiresCapability](requiresCapability.md)       | \* <br/> [Any](Any.md)                           | Indicates that this entry requires a specific capability                         | [Entry](Entry.md)   |
| [implementedByAdapter](implementedByAdapter.md)   | \* <br/> [Any](Any.md)                           | Indicates that this capability is implemented by a specific adapter              | [Entry](Entry.md)   |
| [hasRule](hasRule.md)                             | \* <br/> [Rule](Rule.md)                         | Specifying applicability or inclusion of a rule within specified context         | [Entry](Entry.md)   |
| [type](type.md)                                   | 0..1 <br/> [String](String.md)                   | The entry type or class designation specifying what kind of entry this is        | [Entry](Entry.md)   |
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

| used by                                   | used in                                             | type  | used                              |
| ----------------------------------------- | --------------------------------------------------- | ----- | --------------------------------- |
| [Control](Control.md)                     | [isApplicableinLocality](isApplicableinLocality.md) | range | [LocalityOfUse](LocalityOfUse.md) |
| [Policy](Policy.md)                       | [isApplicableinLocality](isApplicableinLocality.md) | range | [LocalityOfUse](LocalityOfUse.md) |
| [LLMQuestionPolicy](LLMQuestionPolicy.md) | [isApplicableinLocality](isApplicableinLocality.md) | range | [LocalityOfUse](LocalityOfUse.md) |
| [RiskControlGroup](RiskControlGroup.md)   | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [RiskGroup](RiskGroup.md)                 | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [Risk](Risk.md)                           | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [RiskConcept](RiskConcept.md)             | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [RiskControl](RiskControl.md)             | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [RiskControl](RiskControl.md)             | [isApplicableinLocality](isApplicableinLocality.md) | range | [LocalityOfUse](LocalityOfUse.md) |
| [Action](Action.md)                       | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [Action](Action.md)                       | [isApplicableinLocality](isApplicableinLocality.md) | range | [LocalityOfUse](LocalityOfUse.md) |
| [RiskIncident](RiskIncident.md)           | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [Impact](Impact.md)                       | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [AiSystem](AiSystem.md)                   | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |
| [AiAgent](AiAgent.md)                     | [isUsedWithinLocality](isUsedWithinLocality.md)     | range | [LocalityOfUse](LocalityOfUse.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | airo:LocalityOfUse  |
| native       | nexus:LocalityOfUse |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LocalityOfUse
description: The area, e.g. facility or institution, in which an entity is used.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entry
class_uri: airo:LocalityOfUse

````
</details>

### Induced

<details>
```yaml
name: LocalityOfUse
description: The area, e.g. facility or institution, in which an entity is used.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entry
attributes:
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: LocalityOfUse
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
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
    owner: LocalityOfUse
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: airo:LocalityOfUse

````

</details></div>
