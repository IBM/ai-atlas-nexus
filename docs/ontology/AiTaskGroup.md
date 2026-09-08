---
search:
  boost: 10.0
---

# Class: AiTaskGroup

_A group of AI Tasks._

<div data-search-exclude markdown="1">

URI: [nexus:AiTaskGroup](https://w3id.org/ai-atlas-nexus/AiTaskGroup)

```mermaid
 classDiagram
    class AiTaskGroup
    click AiTaskGroup href "../AiTaskGroup/"
      Group <|-- AiTaskGroup
        click Group href "../Group/"

      AiTaskGroup : belongsToDomain





        AiTaskGroup --> "0..1" Any : belongsToDomain
        click Any href "../Any/"



      AiTaskGroup : broad_mappings





        AiTaskGroup --> "*" Any : broad_mappings
        click Any href "../Any/"



      AiTaskGroup : broader

      AiTaskGroup : close_mappings





        AiTaskGroup --> "*" Any : close_mappings
        click Any href "../Any/"



      AiTaskGroup : dateCreated

      AiTaskGroup : dateModified

      AiTaskGroup : description

      AiTaskGroup : exact_mappings





        AiTaskGroup --> "*" Any : exact_mappings
        click Any href "../Any/"



      AiTaskGroup : hasDocumentation





        AiTaskGroup --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      AiTaskGroup : hasLifecycleStatus





        AiTaskGroup --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      AiTaskGroup : hasPart





        AiTaskGroup --> "*" AiTask : hasPart
        click AiTask href "../AiTask/"



      AiTaskGroup : id

      AiTaskGroup : isCategorizedAs





        AiTaskGroup --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      AiTaskGroup : isDefinedByTaxonomy





        AiTaskGroup --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      AiTaskGroup : isPartOf





        AiTaskGroup --> "0..1" AiTaskDomain : isPartOf
        click AiTaskDomain href "../AiTaskDomain/"



      AiTaskGroup : name

      AiTaskGroup : narrow_mappings





        AiTaskGroup --> "*" Any : narrow_mappings
        click Any href "../Any/"



      AiTaskGroup : narrower

      AiTaskGroup : notes

      AiTaskGroup : related_mappings





        AiTaskGroup --> "*" Any : related_mappings
        click Any href "../Any/"



      AiTaskGroup : type

      AiTaskGroup : url


```

## Inheritance

- [Entity](Entity.md)
  - [Group](Group.md)
    - **AiTaskGroup**

## Class Properties

| Property  | Value                                                            |
| --------- | ---------------------------------------------------------------- |
| Class URI | [nexus:AiTaskGroup](https://w3id.org/ai-atlas-nexus/AiTaskGroup) |

## Slots

| Name                                          | Cardinality and Range                            | Description                                                                      | Inheritance         |
| --------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md)               | A relationship where a concept or a concept group is defined by a taxonomy       | direct              |
| [hasPart](hasPart.md)                         | \* <br/> [AiTask](AiTask.md)                     | A relationship where an AI task group has an AI task                             | direct              |
| [isPartOf](isPartOf.md)                       | 0..1 <br/> [AiTaskDomain](AiTaskDomain.md)       | A relationship where an entity is part of another entity                         | direct              |
| [hasDocumentation](hasDocumentation.md)       | \* <br/> [Documentation](Documentation.md)       | Indicates documentation associated with an entity                                | [Group](Group.md)   |
| [belongsToDomain](belongsToDomain.md)         | 0..1 <br/> [Any](Any.md)                         | A relationship where a group belongs to a domain                                 | [Group](Group.md)   |
| [type](type.md)                               | 0..1 <br/> [String](String.md)                   | The type or class designation of this entity instance                            | [Group](Group.md)   |
| [narrower](narrower.md)                       | \* <br/> [String](String.md)                     | Related concepts that are narrower in scope or hierarchy                         | [Group](Group.md)   |
| [broader](broader.md)                         | \* <br/> [String](String.md)                     | Related concepts that are broader in scope or hierarchy                          | [Group](Group.md)   |
| [id](id.md)                                   | 1 <br/> [String](String.md)                      | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                               | 0..1 <br/> [String](String.md)                   | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)                 | 0..1 <br/> [String](String.md)                   | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                                 | 0..1 <br/> [Uri](Uri.md)                         | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)                 | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)               | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)           | \* <br/> [Any](Any.md)                           | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)           | \* <br/> [Any](Any.md)                           | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)       | \* <br/> [Any](Any.md)                           | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)           | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)         | \* <br/> [Any](Any.md)                           | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |
| [hasLifecycleStatus](hasLifecycleStatus.md)   | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md) | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md) |
| [notes](notes.md)                             | \* <br/> [String](String.md)                     | Free-text editorial notes, source breadcrumbs, or build-time provenance that ... | [Entity](Entity.md) |

## Usages

| used by                         | used in               | type  | used                          |
| ------------------------------- | --------------------- | ----- | ----------------------------- |
| [AiTaskDomain](AiTaskDomain.md) | [hasPart](hasPart.md) | range | [AiTaskGroup](AiTaskGroup.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:AiTaskGroup |
| native       | nexus:AiTaskGroup |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AiTaskGroup
description: A group of AI Tasks.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Group
slots:
- isDefinedByTaxonomy
- hasPart
- isPartOf
slot_usage:
  hasPart:
    name: hasPart
    description: A relationship where an AI task group has an AI task.
    range: AiTask
  isPartOf:
    name: isPartOf
    range: AiTaskDomain
class_uri: nexus:AiTaskGroup

````
</details>

### Induced

<details>
```yaml
name: AiTaskGroup
description: A group of AI Tasks.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Group
slot_usage:
  hasPart:
    name: hasPart
    description: A relationship where an AI task group has an AI task.
    range: AiTask
  isPartOf:
    name: isPartOf
    range: AiTaskDomain
attributes:
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: AiTaskGroup
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
  hasPart:
    name: hasPart
    description: A relationship where an AI task group has an AI task.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:member
    owner: AiTaskGroup
    domain_of:
    - Group
    - RiskControlGroup
    - RiskGroup
    - CapabilityGroup
    - AiTaskDomain
    - AiTaskGroup
    range: AiTask
    multivalued: true
  isPartOf:
    name: isPartOf
    description: A relationship where an entity is part of another entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: AiTaskGroup
    domain_of:
    - Entry
    - Risk
    - CapabilityGroup
    - LargeLanguageModel
    - AiTaskGroup
    - Stakeholder
    range: AiTaskDomain
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    owner: AiTaskGroup
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
  belongsToDomain:
    name: belongsToDomain
    description: A relationship where a group belongs to a domain
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: AiTaskGroup
    domain_of:
    - Group
    - CapabilityGroup
    range: Any
    multivalued: false
    inlined: false
  type:
    name: type
    description: The type or class designation of this entity instance.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    ifabsent: string(Group)
    designates_type: true
    owner: AiTaskGroup
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
  narrower:
    name: narrower
    description: Related concepts that are narrower in scope or hierarchy.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    slot_uri: skos:narrower
    owner: AiTaskGroup
    domain_of:
    - Group
    range: string
    multivalued: true
  broader:
    name: broader
    description: Related concepts that are broader in scope or hierarchy.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    slot_uri: skos:narrower
    owner: AiTaskGroup
    domain_of:
    - Group
    range: string
    multivalued: true
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: AiTaskGroup
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
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
    owner: AiTaskGroup
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: nexus:AiTaskGroup

````

</details></div>
