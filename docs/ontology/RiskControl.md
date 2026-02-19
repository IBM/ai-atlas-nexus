# Class: RiskControl

_A measure that maintains and/or modifies risk (and risk concepts)_

URI: [airo:RiskControl](https://w3id.org/airo#RiskControl)

```mermaid
 classDiagram
    class RiskControl
    click RiskControl href "../RiskControl/"
      RiskConcept <|-- RiskControl
        click RiskConcept href "../RiskConcept/"
      Control <|-- RiskControl
        click Control href "../Control/"


      RiskControl <|-- Action
        click Action href "../Action/"


      RiskControl : broad_mappings





        RiskControl --> "*" Any : broad_mappings
        click Any href "../Any/"



      RiskControl : close_mappings





        RiskControl --> "*" Any : close_mappings
        click Any href "../Any/"



      RiskControl : dateCreated

      RiskControl : dateModified

      RiskControl : description

      RiskControl : detectsRiskConcept





        RiskControl --> "*" RiskConcept : detectsRiskConcept
        click RiskConcept href "../RiskConcept/"



      RiskControl : exact_mappings





        RiskControl --> "*" Any : exact_mappings
        click Any href "../Any/"



      RiskControl : hasDocumentation





        RiskControl --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      RiskControl : id

      RiskControl : isDefinedByTaxonomy





        RiskControl --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      RiskControl : isDetectedBy





        RiskControl --> "*" RiskControl : isDetectedBy
        click RiskControl href "../RiskControl/"



      RiskControl : name

      RiskControl : narrow_mappings





        RiskControl --> "*" Any : narrow_mappings
        click Any href "../Any/"



      RiskControl : related_mappings





        RiskControl --> "*" Any : related_mappings
        click Any href "../Any/"



      RiskControl : type

      RiskControl : url


```

## Inheritance

- [Entity](Entity.md)
  - [Control](Control.md)
    - **RiskControl** [ [RiskConcept](RiskConcept.md)]
      - [Action](Action.md)

## Slots

| Name                                          | Cardinality and Range                      | Description                                                                      | Inheritance                                  |
| --------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- | -------------------------------------------- |
| [detectsRiskConcept](detectsRiskConcept.md)   | \* <br/> [RiskConcept](RiskConcept.md)     | The property airo:detectsRiskConcept indicates the control used for detecting... | direct                                       |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md)         | A relationship where a concept or a concept group is defined by a taxonomy       | direct                                       |
| [isDetectedBy](isDetectedBy.md)               | \* <br/> [RiskControl](RiskControl.md)     | A relationship where a risk, risk source, consequence, or impact is detected ... | [RiskConcept](RiskConcept.md)                |
| [type](type.md)                               | 0..1 <br/> [String](String.md)             |                                                                                  | [Control](Control.md), [Concept](Concept.md) |
| [id](id.md)                                   | 1 <br/> [String](String.md)                | A unique identifier to this instance of the model element                        | [Entity](Entity.md)                          |
| [name](name.md)                               | 0..1 <br/> [String](String.md)             | A text name of this instance                                                     | [Entity](Entity.md)                          |
| [description](description.md)                 | 0..1 <br/> [String](String.md)             | The description of an entity                                                     | [Entity](Entity.md)                          |
| [url](url.md)                                 | 0..1 <br/> [Uri](Uri.md)                   | An optional URL associated with this instance                                    | [Entity](Entity.md)                          |
| [dateCreated](dateCreated.md)                 | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was created                                         | [Entity](Entity.md)                          |
| [dateModified](dateModified.md)               | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was most recently modified                          | [Entity](Entity.md)                          |
| [exact_mappings](exact_mappings.md)           | \* <br/> [Any](Any.md)                     | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)                          |
| [close_mappings](close_mappings.md)           | \* <br/> [Any](Any.md)                     | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)                          |
| [related_mappings](related_mappings.md)       | \* <br/> [Any](Any.md)                     | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)                          |
| [narrow_mappings](narrow_mappings.md)         | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                          |
| [broad_mappings](broad_mappings.md)           | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                          |
| [hasDocumentation](hasDocumentation.md)       | \* <br/> [Documentation](Documentation.md) | Indicates documentation associated with an entity                                | [Concept](Concept.md)                        |

## Mixin Usage

| mixed into | description |
| ---------- | ----------- |

## Usages

| used by                                     | used in                                     | type   | used                          |
| ------------------------------------------- | ------------------------------------------- | ------ | ----------------------------- |
| [RiskGroup](RiskGroup.md)                   | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [Risk](Risk.md)                             | [detectsRiskConcept](detectsRiskConcept.md) | domain | [RiskControl](RiskControl.md) |
| [Risk](Risk.md)                             | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [RiskConcept](RiskConcept.md)               | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [RiskControl](RiskControl.md)               | [detectsRiskConcept](detectsRiskConcept.md) | domain | [RiskControl](RiskControl.md) |
| [RiskControl](RiskControl.md)               | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [Action](Action.md)                         | [detectsRiskConcept](detectsRiskConcept.md) | domain | [RiskControl](RiskControl.md) |
| [Action](Action.md)                         | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [RiskIncident](RiskIncident.md)             | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [Impact](Impact.md)                         | [isDetectedBy](isDetectedBy.md)             | range  | [RiskControl](RiskControl.md) |
| [AiModel](AiModel.md)                       | [hasRiskControl](hasRiskControl.md)         | range  | [RiskControl](RiskControl.md) |
| [LargeLanguageModel](LargeLanguageModel.md) | [hasRiskControl](hasRiskControl.md)         | range  | [RiskControl](RiskControl.md) |
| [Adapter](Adapter.md)                       | [hasRiskControl](hasRiskControl.md)         | range  | [RiskControl](RiskControl.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | airo:RiskControl  |
| native       | nexus:RiskControl |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskControl
description: A measure that maintains and/or modifies risk (and risk concepts)
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Control
mixin: true
mixins:
- RiskConcept
slots:
- detectsRiskConcept
- isDefinedByTaxonomy
class_uri: airo:RiskControl

````
</details>

### Induced

<details>
```yaml
name: RiskControl
description: A measure that maintains and/or modifies risk (and risk concepts)
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Control
mixin: true
mixins:
- RiskConcept
attributes:
  detectsRiskConcept:
    name: detectsRiskConcept
    description: The property airo:detectsRiskConcept indicates the control used for
      detecting risks, risk sources, consequences, and impacts.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    exact_mappings:
    - airo:detectsRiskConcept
    rank: 1000
    domain: RiskControl
    alias: detectsRiskConcept
    owner: RiskControl
    domain_of:
    - Risk
    - RiskControl
    inverse: isDetectedBy
    range: RiskConcept
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
    owner: RiskControl
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
  isDetectedBy:
    name: isDetectedBy
    description: A relationship where a risk, risk source, consequence, or impact
      is detected by a risk control.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    alias: isDetectedBy
    owner: RiskControl
    domain_of:
    - RiskConcept
    inverse: detectsRiskConcept
    range: RiskControl
    multivalued: true
    inlined: false
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    designates_type: true
    alias: type
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
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
    owner: RiskControl
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: RiskControl
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
class_uri: airo:RiskControl

````

</details>
