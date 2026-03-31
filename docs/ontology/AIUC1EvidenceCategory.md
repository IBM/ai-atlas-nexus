# Enum: AIUC1EvidenceCategory

URI: [nexus:AIUC1EvidenceCategory](https://ibm.github.io/ai-atlas-nexus/ontology/AIUC1EvidenceCategory)

## Permissible Values

| Value                    | Meaning | Description              |
| ------------------------ | ------- | ------------------------ |
| TECHNICAL_IMPLEMENTATION | None    | Technical Implementation |
| LEGAL_POLICIES           | None    | Legal Policies           |
| OPERATIONAL_PRACTICES    | None    | Operational Practices    |
| THIRD_PARTY_EVALS        | None    | Third-party Evals        |

## Slots

| Name                                          | Description                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------------------- |
| [hasEvidenceCategory](hasEvidenceCategory.md) | The evidence category, ie Technical Implementation, Operational Practices, et... |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## LinkML Source

<details>
```yaml
name: AIUC1EvidenceCategory
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
permissible_values:
  TECHNICAL_IMPLEMENTATION:
    text: TECHNICAL_IMPLEMENTATION
    description: Technical Implementation
  LEGAL_POLICIES:
    text: LEGAL_POLICIES
    description: Legal Policies
  OPERATIONAL_PRACTICES:
    text: OPERATIONAL_PRACTICES
    description: Operational Practices
  THIRD_PARTY_EVALS:
    text: THIRD_PARTY_EVALS
    description: Third-party Evals

```
</details>
```
