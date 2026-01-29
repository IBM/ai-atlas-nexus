# Class: RiskGroup

_A group of AI system related risks that are part of a risk taxonomy._

URI: [nexus:RiskGroup](https://ibm.github.io/ai-atlas-nexus/ontology/RiskGroup)

```mermaid
 classDiagram
    class RiskGroup
    click RiskGroup href "../RiskGroup/"
      RiskConcept <|-- RiskGroup
        click RiskConcept href "../RiskConcept/"
      Group <|-- RiskGroup
        click Group href "../Group/"

      RiskGroup : belongsToDomain





        RiskGroup --> "0..1" Any : belongsToDomain
        click Any href "../Any/"



      RiskGroup : broad_mappings





        RiskGroup --> "*" Any : broad_mappings
        click Any href "../Any/"



      RiskGroup : close_mappings





        RiskGroup --> "*" Any : close_mappings
        click Any href "../Any/"



      RiskGroup : dateCreated

      RiskGroup : dateModified

      RiskGroup : description

      RiskGroup : exact_mappings





        RiskGroup --> "*" Any : exact_mappings
        click Any href "../Any/"



      RiskGroup : hasDocumentation





        RiskGroup --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      RiskGroup : hasPart





        RiskGroup --> "*" Risk : hasPart
        click Risk href "../Risk/"



      RiskGroup : id

      RiskGroup : isDefinedByTaxonomy





        RiskGroup --> "0..1" Taxonomy : isDefinedByTaxonomy
        click Taxonomy href "../Taxonomy/"



      RiskGroup : isDetectedBy





        RiskGroup --> "*" RiskControl : isDetectedBy
        click RiskControl href "../RiskControl/"



      RiskGroup : name

      RiskGroup : narrow_mappings





        RiskGroup --> "*" Any : narrow_mappings
        click Any href "../Any/"



      RiskGroup : related_mappings





        RiskGroup --> "*" Any : related_mappings
        click Any href "../Any/"



      RiskGroup : type

      RiskGroup : url


```

## Inheritance

- [Entity](Entity.md)
  - [Group](Group.md)
    - **RiskGroup** [ [RiskConcept](RiskConcept.md)]

## Slots

| Name                                          | Cardinality and Range                      | Description                                                                      | Inheritance                              |
| --------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------- |
| [isDefinedByTaxonomy](isDefinedByTaxonomy.md) | 0..1 <br/> [Taxonomy](Taxonomy.md)         | A relationship where a concept or a concept group is defined by a taxonomy       | direct                                   |
| [hasPart](hasPart.md)                         | \* <br/> [Risk](Risk.md)                   | A relationship where a riskgroup has a risk                                      | direct                                   |
| [isDetectedBy](isDetectedBy.md)               | \* <br/> [RiskControl](RiskControl.md)     | A relationship where a risk, risk source, consequence, or impact is detected ... | [RiskConcept](RiskConcept.md)            |
| [hasDocumentation](hasDocumentation.md)       | \* <br/> [Documentation](Documentation.md) | Indicates documentation associated with an entity                                | [Group](Group.md), [Concept](Concept.md) |
| [belongsToDomain](belongsToDomain.md)         | 0..1 <br/> [Any](Any.md)                   | A relationship where a group belongs to a domain                                 | [Group](Group.md)                        |
| [type](type.md)                               | 0..1 <br/> [String](String.md)             |                                                                                  | [Group](Group.md), [Concept](Concept.md) |
| [id](id.md)                                   | 1 <br/> [String](String.md)                | A unique identifier to this instance of the model element                        | [Entity](Entity.md)                      |
| [name](name.md)                               | 0..1 <br/> [String](String.md)             | A text name of this instance                                                     | [Entity](Entity.md)                      |
| [description](description.md)                 | 0..1 <br/> [String](String.md)             | The description of an entity                                                     | [Entity](Entity.md)                      |
| [url](url.md)                                 | 0..1 <br/> [Uri](Uri.md)                   | An optional URL associated with this instance                                    | [Entity](Entity.md)                      |
| [dateCreated](dateCreated.md)                 | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was created                                         | [Entity](Entity.md)                      |
| [dateModified](dateModified.md)               | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was most recently modified                          | [Entity](Entity.md)                      |
| [exact_mappings](exact_mappings.md)           | \* <br/> [Any](Any.md)                     | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md)                      |
| [close_mappings](close_mappings.md)           | \* <br/> [Any](Any.md)                     | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md)                      |
| [related_mappings](related_mappings.md)       | \* <br/> [Any](Any.md)                     | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md)                      |
| [narrow_mappings](narrow_mappings.md)         | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                      |
| [broad_mappings](broad_mappings.md)           | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md)                      |

## Usages

| used by         | used in                 | type  | used                      |
| --------------- | ----------------------- | ----- | ------------------------- |
| [Risk](Risk.md) | [isPartOf](isPartOf.md) | range | [RiskGroup](RiskGroup.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | nexus:RiskGroup |
| native       | nexus:RiskGroup |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskGroup
description: A group of AI system related risks that are part of a risk taxonomy.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Group
mixins:
- RiskConcept
slots:
- isDefinedByTaxonomy
- hasPart
slot_usage:
  hasPart:
    name: hasPart
    description: A relationship where a riskgroup has a risk
    range: Risk

````
</details>

### Induced

<details>
```yaml
name: RiskGroup
description: A group of AI system related risks that are part of a risk taxonomy.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Group
mixins:
- RiskConcept
slot_usage:
  hasPart:
    name: hasPart
    description: A relationship where a riskgroup has a risk
    range: Risk
attributes:
  isDefinedByTaxonomy:
    name: isDefinedByTaxonomy
    description: A relationship where a concept or a concept group is defined by a
      taxonomy
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: isDefinedByTaxonomy
    owner: RiskGroup
    domain_of:
    - Concept
    - Control
    - Group
    - Entry
    - Policy
    - RiskGroup
    - Risk
    - RiskControl
    - Action
    - RiskIncident
    - CapabilityGroup
    - StakeholderGroup
    - Stakeholder
    range: Taxonomy
  hasPart:
    name: hasPart
    description: A relationship where a riskgroup has a risk
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: skos:member
    alias: hasPart
    owner: RiskGroup
    domain_of:
    - Group
    - RiskGroup
    - CapabilityGroup
    range: Risk
    multivalued: true
  isDetectedBy:
    name: isDetectedBy
    description: A relationship where a risk, risk source, consequence, or impact
      is detected by a risk control.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    domain: RiskConcept
    alias: isDetectedBy
    owner: RiskGroup
    domain_of:
    - RiskConcept
    inverse: detectsRiskConcept
    range: RiskControl
    multivalued: true
    inlined: false
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: RiskGroup
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
  belongsToDomain:
    name: belongsToDomain
    description: A relationship where a group belongs to a domain
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:isPartOf
    alias: belongsToDomain
    owner: RiskGroup
    domain_of:
    - Group
    - CapabilityGroup
    range: Any
    multivalued: false
    inlined: false
  type:
    name: type
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/common
    ifabsent: string(Group)
    designates_type: true
    alias: type
    owner: RiskGroup
    domain_of:
    - Vocabulary
    - Taxonomy
    - Concept
    - Control
    - Group
    - Entry
    - Policy
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false

````

</details>
