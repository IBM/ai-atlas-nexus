---
search:
  boost: 2.0
---

# Enum: ConformanceOutcome

_The outcome of assessing a condition of an evaluation standard._

<div data-search-exclude markdown="1">

URI: [nexus:ConformanceOutcome](https://w3id.org/ai-atlas-nexus/ConformanceOutcome)

## Permissible Values

| Value             | Meaning           | Description                                                                      |
| ----------------- | ----------------- | -------------------------------------------------------------------------------- |
| FULFILLED         | earl:passed       | The condition was fulfilled                                                      |
| NOT_FULFILLED     | earl:failed       | The condition was not fulfilled                                                  |
| ALTERNATIVE_MEANS | None              | The condition was not fulfilled literally, but the same principle was achieve... |
| NOT_APPLICABLE    | earl:inapplicable | The condition does not apply to this engagement                                  |
| NOT_ASSESSED      | earl:untested     | The condition was not assessed                                                   |

## Slots

| Name                                              | Description                         |
| ------------------------------------------------- | ----------------------------------- |
| [hasConformanceOutcome](hasConformanceOutcome.md) | Whether the condition was fulfilled |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: ConformanceOutcome
description: The outcome of assessing a condition of an evaluation standard.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
permissible_values:
  FULFILLED:
    text: FULFILLED
    description: The condition was fulfilled.
    meaning: earl:passed
    close_mappings:
    - dpv:Compliant
  NOT_FULFILLED:
    text: NOT_FULFILLED
    description: The condition was not fulfilled.
    meaning: earl:failed
    close_mappings:
    - dpv:NonCompliant
  ALTERNATIVE_MEANS:
    text: ALTERNATIVE_MEANS
    description: The condition was not fulfilled literally, but the same principle
      was achieved via alternative means.
    related_mappings:
    - earl:passed
    - dpv:PartiallyCompliant
  NOT_APPLICABLE:
    text: NOT_APPLICABLE
    description: The condition does not apply to this engagement.
    meaning: earl:inapplicable
  NOT_ASSESSED:
    text: NOT_ASSESSED
    description: The condition was not assessed.
    meaning: earl:untested
    close_mappings:
    - dpv:ComplianceUnknown

```
</details>

</div>
```
