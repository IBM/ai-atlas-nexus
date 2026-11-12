# Importing the schema into your own LinkML project

This document describes how to import the AI Atlas Nexus LinkML schema modules directly into your own project using persistent identifiers.

1. [Overview](#overview)
2. [Importing a module](#importing-a-module)
3. [Available modules](#available-modules)

## Overview

Every module of the AI Atlas Nexus schema is published as plain LinkML YAML, resolvable through a
persistent [w3id.org](https://w3id.org) identifier:

```
https://w3id.org/ai-atlas-nexus/schema/<module>
```

This redirects to the schema file hosted on GitHub Pages
(`https://ibm.github.io/ai-atlas-nexus/schema/<module>.yaml`). This means the LinkML tooling
(`gen-pydantic`, `gen-doc`, `linkml-lint`, `SchemaView`, ...) can use `imports:` for it like any other schema, without you having to copy or track our source files yourself.

## Importing a module

Declare a prefix for the namespace, then reference modules by name in `imports:`:

```yaml
prefixes:
  ai-atlas-nexus-schemas: https://w3id.org/ai-atlas-nexus/schema/

imports:
  - linkml:types
  - ai-atlas-nexus-schemas:common
  - ai-atlas-nexus-schemas:ai_risk
```

LinkML expands the CURIE and appends `.yaml` when resolving an import, so
`ai-atlas-nexus-schemas:common` fetches
`https://w3id.org/ai-atlas-nexus/schema/common.yaml`. Modules that import each other internally
(for example `ai_risk` imports `common`) keep resolving correctly, since every module is published
at a sibling path.

## Available modules

| Module             | Description                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `common`           | A core schema supporting the AI Risk Model ontology                                       |
| `ai_risk`          | Vocabulary describing AI risks as used by IBM Risk Atlas                                  |
| `ai_capability`    | Vocabulary describing AI capabilities as used by IBM Risk Atlas                           |
| `ai_system`        | An ontology describing AI systems                                                         |
| `ai_eval`          | Defines vocabulary relating to AI model evaluation                                        |
| `ai_intrinsic`     | An ontology describing AI Intrinsics and representing LoRA (Low-Rank Adaptation) adapters |
| `ai_aiuc`          | AIUC-1 classes as used by AI Atlas Nexus                                                  |
| `eu_ai_act`        | Vocabulary pertaining to the EU AI Act                                                    |
| `energy`           | Defines vocabularies relating to energy consumption                                       |
| `ai-risk-ontology` | The top-level schema that imports all of the above                                        |

See [the ontology reference](../ontology/index.md) for the full class and slot documentation.
