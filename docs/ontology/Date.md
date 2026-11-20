---

search:
boost: 1.0
---# Type: Date

_a date (year, month and day) in an idealized calendar_

<div data-search-exclude markdown="1">

URI: [xsd:date](http://www.w3.org/2001/XMLSchema#date)

## Type Properties

| Property       | Value                                             |
| -------------- | ------------------------------------------------- |
| Base           | `XSDDate`                                         |
| Type URI       | [xsd:date](http://www.w3.org/2001/XMLSchema#date) |
| Representation | `str`                                             |

## Notes

- URI is dateTime because OWL reasoners don't work with straight date or time
- If you are authoring schemas in LinkML YAML, the type is referenced with the lower case "date".

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | xsd:date     |
| native       | nexus:Date   |
| exact        | schema:Date  |

</div>
