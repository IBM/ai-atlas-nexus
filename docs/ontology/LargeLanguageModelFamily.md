# Class: LargeLanguageModelFamily

_A large language model family is a set of models that are provided by the same AI systems provider and are built around the same architecture, but differ e.g. in the number of parameters. Examples are Meta's Llama2 family or the IBM granite models._

URI: [nexus:LargeLanguageModelFamily](https://ibm.github.io/ai-atlas-nexus/ontology/LargeLanguageModelFamily)

```mermaid
 classDiagram
    class LargeLanguageModelFamily
    click LargeLanguageModelFamily href "../LargeLanguageModelFamily/"
      Entity <|-- LargeLanguageModelFamily
        click Entity href "../Entity/"

      LargeLanguageModelFamily : broad_mappings





        LargeLanguageModelFamily --> "*" Any : broad_mappings
        click Any href "../Any/"



      LargeLanguageModelFamily : close_mappings





        LargeLanguageModelFamily --> "*" Any : close_mappings
        click Any href "../Any/"



      LargeLanguageModelFamily : dateCreated

      LargeLanguageModelFamily : dateModified

      LargeLanguageModelFamily : description

      LargeLanguageModelFamily : exact_mappings





        LargeLanguageModelFamily --> "*" Any : exact_mappings
        click Any href "../Any/"



      LargeLanguageModelFamily : hasDocumentation





        LargeLanguageModelFamily --> "*" Documentation : hasDocumentation
        click Documentation href "../Documentation/"



      LargeLanguageModelFamily : id

      LargeLanguageModelFamily : name

      LargeLanguageModelFamily : narrow_mappings





        LargeLanguageModelFamily --> "*" Any : narrow_mappings
        click Any href "../Any/"



      LargeLanguageModelFamily : related_mappings





        LargeLanguageModelFamily --> "*" Any : related_mappings
        click Any href "../Any/"



      LargeLanguageModelFamily : url


```

## Inheritance

- [Entity](Entity.md)
  - **LargeLanguageModelFamily**

## Slots

| Name                                    | Cardinality and Range                      | Description                                                                      | Inheritance         |
| --------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [hasDocumentation](hasDocumentation.md) | \* <br/> [Documentation](Documentation.md) | Indicates documentation associated with an entity                                | direct              |
| [id](id.md)                             | 1 <br/> [String](String.md)                | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                         | 0..1 <br/> [String](String.md)             | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)           | 0..1 <br/> [String](String.md)             | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                           | 0..1 <br/> [Uri](Uri.md)                   | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)           | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)         | 0..1 <br/> [Date](Date.md)                 | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)     | \* <br/> [Any](Any.md)                     | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)     | \* <br/> [Any](Any.md)                     | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md) | \* <br/> [Any](Any.md)                     | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)   | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)     | \* <br/> [Any](Any.md)                     | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |

## Usages

| used by                                     | used in                               | type  | used                                                    |
| ------------------------------------------- | ------------------------------------- | ----- | ------------------------------------------------------- |
| [Container](Container.md)                   | [aimodelfamilies](aimodelfamilies.md) | range | [LargeLanguageModelFamily](LargeLanguageModelFamily.md) |
| [LargeLanguageModel](LargeLanguageModel.md) | [isPartOf](isPartOf.md)               | range | [LargeLanguageModelFamily](LargeLanguageModelFamily.md) |
| [Adapter](Adapter.md)                       | [isPartOf](isPartOf.md)               | range | [LargeLanguageModelFamily](LargeLanguageModelFamily.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                   |
| ------------ | ------------------------------ |
| self         | nexus:LargeLanguageModelFamily |
| native       | nexus:LargeLanguageModelFamily |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LargeLanguageModelFamily
description: A large language model family is a set of models that are provided by
  the same AI systems provider and are built around the same architecture, but differ
  e.g. in the number of parameters. Examples are Meta's Llama2 family or the IBM granite
  models.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entity
slots:
- hasDocumentation

````
</details>

### Induced

<details>
```yaml
name: LargeLanguageModelFamily
description: A large language model family is a set of models that are provided by
  the same AI systems provider and are built around the same architecture, but differ
  e.g. in the number of parameters. Examples are Meta's Llama2 family or the IBM granite
  models.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entity
attributes:
  hasDocumentation:
    name: hasDocumentation
    description: Indicates documentation associated with an entity.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: airo:hasDocumentation
    alias: hasDocumentation
    owner: LargeLanguageModelFamily
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
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
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
    owner: LargeLanguageModelFamily
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false

````

</details>
