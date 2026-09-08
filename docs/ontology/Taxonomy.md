---
search:
  boost: 10.0
---

# Class: Taxonomy

_A hierachical taxonomy of concepts, with their definitions and relationships._

<div data-search-exclude markdown="1">

- **NOTE**: this is an abstract class and should not be instantiated directly

URI: [skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme)

```mermaid
 classDiagram
    class Taxonomy
    click Taxonomy href "../Taxonomy/"
      Entity <|-- Taxonomy
        click Entity href "../Entity/"


      Taxonomy <|-- RiskTaxonomy
        click RiskTaxonomy href "../RiskTaxonomy/"
      Taxonomy <|-- RiskControlGroupTaxonomy
        click RiskControlGroupTaxonomy href "../RiskControlGroupTaxonomy/"
      Taxonomy <|-- CapabilityTaxonomy
        click CapabilityTaxonomy href "../CapabilityTaxonomy/"
      Taxonomy <|-- AiTaskTaxonomy
        click AiTaskTaxonomy href "../AiTaskTaxonomy/"


      Taxonomy : broad_mappings





        Taxonomy --> "*" Any : broad_mappings
        click Any href "../Any/"



      Taxonomy : close_mappings





        Taxonomy --> "*" Any : close_mappings
        click Any href "../Any/"



      Taxonomy : dateCreated

      Taxonomy : dateModified

      Taxonomy : description

      Taxonomy : exact_mappings





        Taxonomy --> "*" Any : exact_mappings
        click Any href "../Any/"



      Taxonomy : hasDocumentation





        Taxonomy --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      Taxonomy : hasLicense





        Taxonomy --> "0..1" License : hasLicense
        click License href "../License/"



      Taxonomy : hasLifecycleStatus





        Taxonomy --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      Taxonomy : id

      Taxonomy : isCategorizedAs





        Taxonomy --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      Taxonomy : name

      Taxonomy : narrow_mappings





        Taxonomy --> "*" Any : narrow_mappings
        click Any href "../Any/"



      Taxonomy : notes

      Taxonomy : related_mappings





        Taxonomy --> "*" Any : related_mappings
        click Any href "../Any/"



      Taxonomy : type

      Taxonomy : url

      Taxonomy : version


```

## Inheritance

- [Entity](Entity.md)
  - **Taxonomy**
    - [RiskTaxonomy](RiskTaxonomy.md)
    - [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md)
    - [CapabilityTaxonomy](CapabilityTaxonomy.md)
    - [AiTaskTaxonomy](AiTaskTaxonomy.md)

## Class Properties

| Property  | Value                                                                   |
| --------- | ----------------------------------------------------------------------- |
| Class URI | [skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme) |
| Mixin     | Yes                                                                     |

## Slots

| Name                                        | Cardinality and Range                            | Description                                                                      | Inheritance         |
| ------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [version](version.md)                       | 0..1 <br/> [String](String.md)                   | The version of the entity embodied by a specified resource                       | direct              |
| [hasDocumentation](hasDocumentation.md)     | \* <br/> [Documentation](Documentation.md)       | Indicates documentation associated with an entity                                | direct              |
| [hasLicense](hasLicense.md)                 | 0..1 <br/> [License](License.md)                 | Indicates licenses associated with a resource                                    | direct              |
| [type](type.md)                             | 0..1 <br/> [String](String.md)                   | The type or class designation of this entity instance                            | direct              |
| [id](id.md)                                 | 1 <br/> [String](String.md)                      | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                             | 0..1 <br/> [String](String.md)                   | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)               | 0..1 <br/> [String](String.md)                   | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                               | 0..1 <br/> [Uri](Uri.md)                         | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)               | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)             | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)     | \* <br/> [Any](Any.md)                           | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)       | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)       | \* <br/> [Any](Any.md)                           | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |
| [hasLifecycleStatus](hasLifecycleStatus.md) | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md) | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md) |
| [notes](notes.md)                           | \* <br/> [String](String.md)                     | Free-text editorial notes, source breadcrumbs, or build-time provenance that ... | [Entity](Entity.md) |

## Mixin Usage

| mixed into | description |
| ---------- | ----------- |

## Usages

| used by                                                           | used in                                       | type  | used                    |
| ----------------------------------------------------------------- | --------------------------------------------- | ----- | ----------------------- |
| [Container](Container.md)                                         | [taxonomies](taxonomies.md)                   | range | [Taxonomy](Taxonomy.md) |
| [Concept](Concept.md)                                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Control](Control.md)                                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Group](Group.md)                                                 | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Entry](Entry.md)                                                 | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Term](Term.md)                                                   | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Principle](Principle.md)                                         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Policy](Policy.md)                                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Rule](Rule.md)                                                   | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AttributeConditionRule](AttributeConditionRule.md)               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Permission](Permission.md)                                       | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Prohibition](Prohibition.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Obligation](Obligation.md)                                       | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Recommendation](Recommendation.md)                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Certification](Certification.md)                                 | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [LocalityOfUse](LocalityOfUse.md)                                 | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [RiskControlGroup](RiskControlGroup.md)                           | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [RiskGroup](RiskGroup.md)                                         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Risk](Risk.md)                                                   | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [RiskConcept](RiskConcept.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [RiskControl](RiskControl.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Action](Action.md)                                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [RiskIncident](RiskIncident.md)                                   | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Impact](Impact.md)                                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [CapabilityConcept](CapabilityConcept.md)                         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [CapabilityDomain](CapabilityDomain.md)                           | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [CapabilityGroup](CapabilityGroup.md)                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Capability](Capability.md)                                       | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AiSystem](AiSystem.md)                                           | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AiAgent](AiAgent.md)                                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AiTask](AiTask.md)                                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AiTaskDomain](AiTaskDomain.md)                                   | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AiTaskGroup](AiTaskGroup.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Purpose](Purpose.md)                                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Domain](Domain.md)                                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AISubject](AISubject.md)                                         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AIOperator](AIOperator.md)                                       | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AIDeveloper](AIDeveloper.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AIDeployer](AIDeployer.md)                                       | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [AIUser](AIUser.md)                                               | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Stakeholder](Stakeholder.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [StakeholderGroup](StakeholderGroup.md)                           | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Adapter](Adapter.md)                                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [ControlActivity](ControlActivity.md)                             | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [ControlActivityPermission](ControlActivityPermission.md)         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [ControlActivityObligation](ControlActivityObligation.md)         | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |
| [Requirement](Requirement.md)                                     | [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | range | [Taxonomy](Taxonomy.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | skos:ConceptScheme |
| native       | nexus:Taxonomy     |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Taxonomy
description: A hierachical taxonomy of concepts, with their definitions and relationships.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
abstract: true
mixin: true
slots:
- version
- hasDocumentation
- hasLicense
attributes:
  type:
    name: type
    description: The type or class designation of this entity instance.
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
class_uri: skos:ConceptScheme

````
</details>

### Induced

<details>
```yaml
name: Taxonomy
description: A hierachical taxonomy of concepts, with their definitions and relationships.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
abstract: true
mixin: true
attributes:
  type:
    name: type
    description: The type or class designation of this entity instance.
    from_schema: https://w3id.org/ai-atlas-nexus/common
    designates_type: true
    owner: Taxonomy
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
  version:
    name: version
    description: The version of the entity embodied by a specified resource.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:version
    owner: Taxonomy
    domain_of:
    - License
    - Vocabulary
    - Taxonomy
    - RiskTaxonomy
    - RiskControlGroupTaxonomy
    - AiTaskTaxonomy
    range: string
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    owner: Taxonomy
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
  hasLicense:
    name: hasLicense
    description: Indicates licenses associated with a resource
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasLicense
    owner: Taxonomy
    domain_of:
    - Dataset
    - Documentation
    - Vocabulary
    - Taxonomy
    - RiskTaxonomy
    - RiskControlGroupTaxonomy
    - BaseAi
    - AiTaskTaxonomy
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    range: License
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: Taxonomy
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
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
    owner: Taxonomy
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: skos:ConceptScheme

````

</details></div>
