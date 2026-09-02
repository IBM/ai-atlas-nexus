---
type: Service
id: https://w3id.org/ai-atlas-nexus/knowledge/services/ran-extension-cli
title: ran-extension CLI
description: Command-line tool shipped with the ai-atlas-nexus package for installing AI Atlas Nexus extensions.
resource: https://github.com/IBM/ai-atlas-nexus/blob/main/src/ai_atlas_nexus/extension.py
generated:
  by: process:lokf-librarian
  at: "2026-09-02T15:57:00Z"
isPartOf:
  - https://w3id.org/ai-atlas-nexus/knowledge/services/python-library
---

# Overview

**`ran-extension`** is the console script declared in `pyproject.toml` (`[project.scripts]`, target `ai_atlas_nexus.extension:app`, a Typer app). It installs AI Atlas Nexus extensions by name, e.g.:

```
ran-extension install <EXTENSION_NAME>
```

Known extensions are maintained in the separate [ai-atlas-nexus-extensions](https://github.com/ibm/ai-atlas-nexus-extensions) repository, such as `ran-ares-integration` for running ARES robustness evaluations on AI systems derived from use cases.
