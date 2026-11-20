---

search:
boost: 1.0
---# Type: Time

_A time object represents a (local) time of day, independent of any particular day_

<div data-search-exclude markdown="1">

URI: [xsd:time](http://www.w3.org/2001/XMLSchema#time)

## Type Properties

| Property       | Value                                             |
| -------------- | ------------------------------------------------- |
| Base           | `XSDTime`                                         |
| Type URI       | [xsd:time](http://www.w3.org/2001/XMLSchema#time) |
| Representation | `str`                                             |

## Notes

- URI is dateTime because OWL reasoners do not work with straight date or time
- If you are authoring schemas in LinkML YAML, the type is referenced with the lower case "time".

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | xsd:time     |
| native       | nexus:Time   |
| exact        | schema:Time  |

</div>
