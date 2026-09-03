# `.lokf/` - AI Atlas Nexus's machine-readable knowledge base

A small **sidecar** that captures AI Atlas Nexus's own knowledge - its services, metrics, policies, playbooks, and glossary - as plain Markdown files that are **also a queryable knowledge graph**. It does not touch the app build; it's independent tooling you can run on its own.

## The 60-second version

- **OKF (Open Knowledge Format)** is a folder of Markdown files, one *concept* per file, each with a little YAML frontmatter block (`type`, `title`, `description`, ...). Just files you can read on GitHub or in any editor.
- **LOKF (Linked OKF)** gives every field a precise meaning (schema.org, DCAT, PROV-O), so the same Markdown turns into RDF and is queryable with SPARQL. [`lokf`](https://lokf.nolan-nichols.com/) is the toolkit that does the turning.

You write normal Markdown; you get a validated, queryable graph for free.

## What's in here

```
.lokf/
|-- knowledge/            # the bundle - one Markdown file per concept
|   |-- index.md          # bundle metadata + table of contents (reserved)
|   |-- log.md            # change history (reserved)
|   |-- services/         # concepts (grow into metrics/ policies/ playbooks/ glossary/ ...)
|-- pyproject.toml        # declares the `lokf` toolkit as a dependency
|-- justfile              # convenience commands (below)
```

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) - the Python package runner.
- [`just`](https://just.systems/) - optional, for the shortcut recipes.

## Use it

```bash
cd .lokf
just lokf-install    # one-time: install the toolkit (uv sync)
just lokf-validate   # check every concept against the LOKF schema
just lokf-serve      # local SPARQL endpoint + interactive graph explorer
just lokf-convert    # print the whole bundle as RDF (Turtle)
```

Without `just`:

```bash
cd .lokf
uv sync
uv run lokf validate knowledge
uv run lokf serve knowledge
uv run lokf convert knowledge --format ttl
```

## Add or edit a concept

1. Create a Markdown file under `knowledge/<kind>/` (e.g. `services/`, `metrics/`).
2. Start with frontmatter. OKF requires only `type`; this bundle also sets `id`, `title`, and `description` on every concept.
3. Link concepts with typed-relation keys whose values are target `id`s - e.g. `dependsOn:`, `about:`, `references:`, `measures:`. Run `uv run lokf vocab` to list available relations.
4. Add the concept to the table of contents in `knowledge/index.md`.
5. Run `just lokf-validate` before committing.

## Learn more

- LOKF toolkit & docs: <https://lokf.nolan-nichols.com/>
- OKF spec: <https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>
