# Class: AiTask

_A task, such as summarization and classification, performed by an AI._

URI: [airo:AiCapability](https://w3id.org/airo#AiCapability)

```mermaid
 classDiagram
    class AiTask
    click AiTask href "../AiTask/"
      Entry <|-- AiTask
        click Entry href "../Entry/"

      AiTask : broad_mappings





        AiTask --> "*" Any : broad_mappings
        click Any href "../Any/"



      AiTask : close_mappings





        AiTask --> "*" Any : close_mappings
        click Any href "../Any/"



      AiTask : dateCreated

      AiTask : dateModified

      AiTask : description

      AiTask : exact_mappings





        AiTask --> "*" Any : exact_mappings
        click Any href "../Any/"



      AiTask : hasDocumentation





        AiTask --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      AiTask : id

      AiTask : implementedByAdapter





        AiTask --> "*" Adapter : implementedByAdapter
        click Adapter href "../Adapter/"



      AiTask : isDefinedByTaxonomy





        AiTask --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      AiTask : isDefinedByVocabulary





        AiTask --> "0..1" Vocabulary : isDefinedByVocabulary
        click Vocabulary href "../Vocabulary/"



      AiTask : isPartOf

      AiTask : name

      AiTask : narrow_mappings





        AiTask --> "*" Any : narrow_mappings
        click Any href "../Any/"



      AiTask : related_mappings





        AiTask --> "*" Any : related_mappings
        click Any href "../Any/"



      AiTask : requiredByTask





        AiTask --> "*" AiTask : requiredByTask
        click AiTask href "../AiTask/"



      AiTask : requiresCapability





        AiTask --> "*" Capability : requiresCapability
        click Capability href "../Capability/"



      AiTask : type

      AiTask : url


```

## Inheritance

- [Entity](Entity.md)
  - [Entry](Entry.md)
    - **AiTask**

## Slots

| Name                                              | Cardinality and Range                      | Description                                                                      | Inheritance         |
| ------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [requiresCapability](requiresCapability.md)       | \* <br/> [Capability](Capability.md)       | Indicates that this entry requires a specific capability                         | direct              |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md)     | 0..1 <br/> [Taxonomy](Taxonomy.md)         | A relationship where a concept or a concept group is defined by a taxonomy       | [Entry](Entry.md)   |
| [isDefinedByVocabulary](isDefinedByVocabulary.md) | 0..1 <br/> [Vocabulary](Vocabulary.md)     | A relationship where a term or a term group is defined by a vocabulary           | [Entry](Entry.md)   |
| [hasDocumentation](hasDocumentation.md)           | \* <br/> [Documentation](Documentation.md) | Indicates documentation associated with an entity                                | [Entry](Entry.md)   |
| [isPartOf](isPartOf.md)                           | 0..1 <br/> [String](String.md)             | A relationship where an entity is part of another entity                         | [Entry](Entry.md)   |
| [requiredByTask](requiredByTask.md)               | \* <br/> [AiTask](AiTask.md)               | Indicates that this entry is required to perform a specific AI task              | [Entry](Entry.md)   |
| [implementedByAdapter](implementedByAdapter.md)   | \* <br/> [Adapter](Adapter.md)             | Indicates that this capability is implemented by a specific adapter              | [Entry](Entry.md)   |
| [type](type.md)                                   | 0..1 <br/> [String](String.md)             |                                                                                  | [Entry](Entry.md)   |
| [id](id.md)                                       | 1 <br/> [String](String.md)                | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                                   | 0..1 <br/> [String](String.md)             | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)                     | 0..1 <br/> [String](String.md)             | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                                     | 0..1 <br/> [Uri](Uri.md)                   | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)                     | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)                   | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)               | \* <br/> [Any](Any.md)                     | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)               | \* <br/> [Any](Any.md)                     | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)           | \* <br/> [Any](Any.md)                     | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)             | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)               | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |

## Usages

| used by                                                           | used in                                       | type  | used                |
| ----------------------------------------------------------------- | --------------------------------------------- | ----- | ------------------- |
| [Container](Container.md)                                         | [aitasks](aitasks.md)                         | range | [AiTask](AiTask.md) |
| [Entry](Entry.md)                                                 | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Term](Term.md)                                                   | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Principle](Principle.md)                                         | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Certification](Certification.md)                                 | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Risk](Risk.md)                                                   | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [BaseAi](BaseAi.md)                                               | [performsTask](performsTask.md)               | range | [AiTask](AiTask.md) |
| [AiSystem](AiSystem.md)                                           | [performsTask](performsTask.md)               | range | [AiTask](AiTask.md) |
| [AiAgent](AiAgent.md)                                             | [performsTask](performsTask.md)               | range | [AiTask](AiTask.md) |
| [AiModel](AiModel.md)                                             | [performsTask](performsTask.md)               | range | [AiTask](AiTask.md) |
| [LargeLanguageModel](LargeLanguageModel.md)                       | [performsTask](performsTask.md)               | range | [AiTask](AiTask.md) |
| [AiTask](AiTask.md)                                               | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Capability](Capability.md)                                       | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Adapter](Adapter.md)                                             | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [Adapter](Adapter.md)                                             | [performsTask](performsTask.md)               | range | [AiTask](AiTask.md) |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | [requiredByTask](requiredByTask.md)           | range | [AiTask](AiTask.md) |
| [ControlActivity](ControlActivity.md)                             | [appliesToCapability](appliesToCapability.md) | range | [AiTask](AiTask.md) |
| [ControlActivityPermission](ControlActivityPermission.md)         | [appliesToCapability](appliesToCapability.md) | range | [AiTask](AiTask.md) |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | [appliesToCapability](appliesToCapability.md) | range | [AiTask](AiTask.md) |
| [ControlActivityObligation](ControlActivityObligation.md)         | [appliesToCapability](appliesToCapability.md) | range | [AiTask](AiTask.md) |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | [appliesToCapability](appliesToCapability.md) | range | [AiTask](AiTask.md) |
| [Requirement](Requirement.md)                                     | [appliesToCapability](appliesToCapability.md) | range | [AiTask](AiTask.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | airo:AiCapability |
| native       | nexus:AiTask      |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AiTask
description: A task, such as summarization and classification, performed by an AI.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entry
slots:
- requiresCapability
class_uri: airo:AiCapability

````
</details>

### Induced

<details>
```yaml
name: AiTask
description: A task, such as summarization and classification, performed by an AI.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entry
attributes:
  requiresCapability:
    name: requiresCapability
    description: Indicates that this entry requires a specific capability
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: requiresCapability
    owner: AiTask
    domain_of:
    - Entry
    - LargeLanguageModel
    - AiTask
    - Adapter
    inverse: requiredByTask
    range: Capability
    multivalued: true
    inlined: false
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: AiTask
    domain_of:
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - Rule
    - RiskGroup
    - Risk
    - RiskControl
    - Action
    - RiskIncident
    - CapabilityGroup
    - StakeholderGroup
    - Stakeholder
    - Requirement
    range: Taxonomy
  isDefinedByVocabulary:
    name: isDefinedByVocabulary
    description: A relationship where a term or a term group is defined by a vocabulary
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByVocabulary
    owner: AiTask
    domain_of:
    - Entry
    - Term
    - Adapter
    - LLMIntrinsic
    range: Vocabulary
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: AiTask
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
    - Action
    - BaseAi
    - LargeLanguageModelFamily
    - AiEval
    - BenchmarkMetadataCard
    - Adapter
    - LLMIntrinsic
    range: Documentation
    multivalued: true
    inlined: false
  isPartOf:
    name: isPartOf
    description: A relationship where an entity is part of another entity
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isPartOf
    owner: AiTask
    domain_of:
    - Entry
    - Risk
    - LargeLanguageModel
    - CapabilityGroup
    - Stakeholder
    range: string
  requiredByTask:
    name: requiredByTask
    description: Indicates that this entry is required to perform a specific AI task.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    alias: requiredByTask
    owner: AiTask
    domain_of:
    - Entry
    - Capability
    inverse: requiresCapability
    range: AiTask
    multivalued: true
    inlined: false
  implementedByAdapter:
    name: implementedByAdapter
    description: 'Indicates that this capability is implemented by a specific adapter.
      This relationship distinguishes the abstract capability (what can be done) from
      the technical implementation mechanism (how it is added/extended via adapters).

      '
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: Any
    alias: implementedByAdapter
    owner: AiTask
    domain_of:
    - Entry
    - Capability
    inverse: implementsCapability
    range: Adapter
    multivalued: true
    inlined: false
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: AiTask
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
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: AiTask
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: AiTask
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: AiTask
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    alias: url
    owner: AiTask
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    alias: dateCreated
    owner: AiTask
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    alias: dateModified
    owner: AiTask
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    alias: exact_mappings
    owner: AiTask
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    alias: close_mappings
    owner: AiTask
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    alias: related_mappings
    owner: AiTask
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
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    alias: narrow_mappings
    owner: AiTask
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
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    alias: broad_mappings
    owner: AiTask
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
class_uri: airo:AiCapability

````

</details>
