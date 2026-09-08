---
search:
  boost: 10.0
---

# Class: Group

_Labelled groups of concepts._

<div data-search-exclude markdown="1">

- **NOTE**: this is an abstract class and should not be instantiated directly

URI: [skos:Collection](http://www.w3.org/2004/02/skos/core#Collection)

```mermaid
 classDiagram
    class Group
    click Group href "../Group/"
      Entity <|-- Group
        click Entity href "../Entity/"


      Group <|-- RiskControlGroup
        click RiskControlGroup href "../RiskControlGroup/"
      Group <|-- RiskGroup
        click RiskGroup href "../RiskGroup/"
      Group <|-- CapabilityDomain
        click CapabilityDomain href "../CapabilityDomain/"
      Group <|-- CapabilityGroup
        click CapabilityGroup href "../CapabilityGroup/"
      Group <|-- AiTaskDomain
        click AiTaskDomain href "../AiTaskDomain/"
      Group <|-- AiTaskGroup
        click AiTaskGroup href "../AiTaskGroup/"
      Group <|-- StakeholderGroup
        click StakeholderGroup href "../StakeholderGroup/"


      Group : belongsToDomain





        Group --> "0..1" Any : belongsToDomain
        click Any href "../Any/"



      Group : broad_mappings





        Group --> "*" Any : broad_mappings
        click Any href "../Any/"



      Group : broader

      Group : close_mappings





        Group --> "*" Any : close_mappings
        click Any href "../Any/"



      Group : dateCreated

      Group : dateModified

      Group : description

      Group : exact_mappings





        Group --> "*" Any : exact_mappings
        click Any href "../Any/"



      Group : hasDocumentation





        Group --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      Group : hasLifecycleStatus





        Group --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      Group : hasPart

      Group : id

      Group : isCategorizedAs





        Group --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      Group : isDefinedByTaxonomy





        Group --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      Group : name

      Group : narrow_mappings





        Group --> "*" Any : narrow_mappings
        click Any href "../Any/"



      Group : narrower

      Group : notes

      Group : related_mappings





        Group --> "*" Any : related_mappings
        click Any href "../Any/"



      Group : type

      Group : url


```

## Inheritance

- [Entity](Entity.md)
  - **Group**
    - [RiskControlGroup](RiskControlGroup.md) [ [RiskConcept](RiskConcept.md)]
    - [RiskGroup](RiskGroup.md) [ [RiskConcept](RiskConcept.md)]
    - [CapabilityDomain](CapabilityDomain.md) [ [CapabilityConcept](CapabilityConcept.md)]
    - [CapabilityGroup](CapabilityGroup.md) [ [CapabilityConcept](CapabilityConcept.md)]
    - [AiTaskDomain](AiTaskDomain.md)
    - [AiTaskGroup](AiTaskGroup.md)
    - [StakeholderGroup](StakeholderGroup.md)

## Class Properties

| Property  | Value                                                             |
| --------- | ----------------------------------------------------------------- |
| Class URI | [skos:Collection](http://www.w3.org/2004/02/skos/core#Collection) |
| Mixin     | Yes                                                               |

## Slots

| Name                                          | Cardinality and Range                            | Description                                                                      | Inheritance         |
| --------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md)               | A relationship where a concept or a concept group is defined by a taxonomy       | direct              |
| [hasDocumentation](hasDocumentation.md)       | \* <br/> [Documentation](Documentation.md)       | Indicates documentation associated with an entity                                | direct              |
| [hasPart](hasPart.md)                         | \* <br/> [String](String.md)                     | A relationship where an entity has another entity                                | direct              |
| [belongsToDomain](belongsToDomain.md)         | 0..1 <br/> [Any](Any.md)                         | A relationship where a group belongs to a domain                                 | direct              |
| [type](type.md)                               | 0..1 <br/> [String](String.md)                   | The type or class designation of this entity instance                            | direct              |
| [narrower](narrower.md)                       | \* <br/> [String](String.md)                     | Related concepts that are narrower in scope or hierarchy                         | direct              |
| [broader](broader.md)                         | \* <br/> [String](String.md)                     | Related concepts that are broader in scope or hierarchy                          | direct              |
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

## Mixin Usage

| mixed into | description |
| ---------- | ----------- |

## Usages

| used by                   | used in             | type  | used              |
| ------------------------- | ------------------- | ----- | ----------------- |
| [Container](Container.md) | [groups](groups.md) | range | [Group](Group.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | skos:Collection |
| native       | nexus:Group     |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Group
description: Labelled groups of concepts.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
abstract: true
mixin: true
slots:
- isDefinedByTaxonomy
- hasDocumentation
- hasPart
- belongsToDomain
attributes:
  type:
    name: type
    description: The type or class designation of this entity instance.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    ifabsent: string(Group)
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
  narrower:
    name: narrower
    description: Related concepts that are narrower in scope or hierarchy.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    slot_uri: skos:narrower
    domain_of:
    - Group
    multivalued: true
  broader:
    name: broader
    description: Related concepts that are broader in scope or hierarchy.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    rank: 1000
    slot_uri: skos:narrower
    domain_of:
    - Group
    multivalued: true
class_uri: skos:Collection

````
</details>

### Induced

<details>
```yaml
name: Group
description: Labelled groups of concepts.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
abstract: true
mixin: true
attributes:
  type:
    name: type
    description: The type or class designation of this entity instance.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    ifabsent: string(Group)
    designates_type: true
    owner: Group
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
    owner: Group
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
    owner: Group
    domain_of:
    - Group
    range: string
    multivalued: true
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: Group
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
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    owner: Group
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
  hasPart:
    name: hasPart
    description: A relationship where an entity has another entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:member
    owner: Group
    domain_of:
    - Group
    - RiskControlGroup
    - RiskGroup
    - CapabilityGroup
    - AiTaskDomain
    - AiTaskGroup
    range: string
    multivalued: true
  belongsToDomain:
    name: belongsToDomain
    description: A relationship where a group belongs to a domain
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    owner: Group
    domain_of:
    - Group
    - CapabilityGroup
    range: Any
    multivalued: false
    inlined: false
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: Group
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
    owner: Group
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
    owner: Group
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: Group
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
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
    owner: Group
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: skos:Collection

````

</details></div>
