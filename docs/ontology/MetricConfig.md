# Class: MetricConfig

_Configuration for evaluation metrics_

URI: [nexus:metricconfig](https://ibm.github.io/ai-atlas-nexus/ontology/metricconfig)

```mermaid
 classDiagram
    class MetricConfig
    click MetricConfig href "../MetricConfig/"
      Entity <|-- MetricConfig
        click Entity href "../Entity/"

      MetricConfig : broad_mappings





        MetricConfig --> "*" Any : broad_mappings
        click Any href "../Any/"



      MetricConfig : close_mappings





        MetricConfig --> "*" Any : close_mappings
        click Any href "../Any/"



      MetricConfig : dateCreated

      MetricConfig : dateModified

      MetricConfig : description

      MetricConfig : exact_mappings





        MetricConfig --> "*" Any : exact_mappings
        click Any href "../Any/"



      MetricConfig : id

      MetricConfig : isCategorizedAs





        MetricConfig --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      MetricConfig : lower_is_better

      MetricConfig : max_score

      MetricConfig : min_score

      MetricConfig : name

      MetricConfig : narrow_mappings





        MetricConfig --> "*" Any : narrow_mappings
        click Any href "../Any/"



      MetricConfig : related_mappings





        MetricConfig --> "*" Any : related_mappings
        click Any href "../Any/"



      MetricConfig : score_type

      MetricConfig : url


```

## Inheritance

- [Entity](Entity.md)
  - **MetricConfig**

## Class Properties

| Property  | Value                                                                            |
| --------- | -------------------------------------------------------------------------------- |
| Class URI | [nexus:metricconfig](https://ibm.github.io/ai-atlas-nexus/ontology/metricconfig) |

## Slots

| Name                                    | Cardinality and Range            | Description                                                                      | Inheritance         |
| --------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------- | ------------------- |
| [lower_is_better](lower_is_better.md)   | 0..1 <br/> [Boolean](Boolean.md) | Whether lower scores are better                                                  | direct              |
| [score_type](score_type.md)             | 0..1 <br/> [String](String.md)   | Type of score (e                                                                 | direct              |
| [min_score](min_score.md)               | 0..1 <br/> [Float](Float.md)     | Minimum possible score                                                           | direct              |
| [max_score](max_score.md)               | 0..1 <br/> [Float](Float.md)     | Maximum possible score                                                           | direct              |
| [id](id.md)                             | 1 <br/> [String](String.md)      | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                         | 0..1 <br/> [String](String.md)   | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)           | 0..1 <br/> [String](String.md)   | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                           | 0..1 <br/> [Uri](Uri.md)         | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)           | 0..1 <br/> [Date](Date.md)       | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)         | 0..1 <br/> [Date](Date.md)       | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)     | \* <br/> [Any](Any.md)           | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)     | \* <br/> [Any](Any.md)           | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md) | \* <br/> [Any](Any.md)           | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)   | \* <br/> [Any](Any.md)           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)     | \* <br/> [Any](Any.md)           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)   | \* <br/> [Any](Any.md)           | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |

## Usages

| used by                                             | used in                               | type  | used                            |
| --------------------------------------------------- | ------------------------------------- | ----- | ------------------------------- |
| [EvaluationResultRecord](EvaluationResultRecord.md) | [hasMetricConfig](hasMetricConfig.md) | range | [MetricConfig](MetricConfig.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:metricconfig |
| native       | nexus:MetricConfig |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MetricConfig
description: Configuration for evaluation metrics
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entity
attributes:
  lower_is_better:
    name: lower_is_better
    description: Whether lower scores are better
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    domain_of:
    - MetricConfig
    range: boolean
  score_type:
    name: score_type
    description: Type of score (e.g., continuous)
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    domain_of:
    - MetricConfig
    range: string
  min_score:
    name: min_score
    description: Minimum possible score
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    domain_of:
    - MetricConfig
    range: float
  max_score:
    name: max_score
    description: Maximum possible score
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    domain_of:
    - MetricConfig
    range: float
class_uri: nexus:metricconfig

````
</details>

### Induced

<details>
```yaml
name: MetricConfig
description: Configuration for evaluation metrics
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
is_a: Entity
attributes:
  lower_is_better:
    name: lower_is_better
    description: Whether lower scores are better
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    alias: lower_is_better
    owner: MetricConfig
    domain_of:
    - MetricConfig
    range: boolean
  score_type:
    name: score_type
    description: Type of score (e.g., continuous)
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    alias: score_type
    owner: MetricConfig
    domain_of:
    - MetricConfig
    range: string
  min_score:
    name: min_score
    description: Minimum possible score
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    alias: min_score
    owner: MetricConfig
    domain_of:
    - MetricConfig
    range: float
  max_score:
    name: max_score
    description: Maximum possible score
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai_eval
    rank: 1000
    alias: max_score
    owner: MetricConfig
    domain_of:
    - MetricConfig
    range: float
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
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
    owner: MetricConfig
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  isCategorizedAs:
    name: isCategorizedAs
    description: A relationship where an entity has been deemed to be categorized
    from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:isCategorizedAs
    alias: isCategorizedAs
    owner: MetricConfig
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
class_uri: nexus:metricconfig

````

</details>
