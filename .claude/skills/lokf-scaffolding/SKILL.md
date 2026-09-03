---
name: lokf-scaffolding
description: 'Scaffold a new `.lokf/` knowledge sidecar into the repository this skill sits inside. Use when: bootstrapping/initializing a LOKF knowledge bundle for a project that does not have one yet; creating the .lokf/ directory with pyproject.toml, justfile, README.md, a knowledge/ bundle skeleton, (optionally) queries.http, and the scheduled librarian wrapper script `.lokf/scripts/knowledge-librarian.sh`; setting up machine-readable, SPARQL-queryable knowledge for a repo; asked to "add a lokf sidecar" or "scaffold lokf". Produces generic templates with <PROJ_NAME>/<PROJ_DESC> placeholders and dummy services; the agent MUST then populate them from the actual host project. Run once to bootstrap, or to repair a missing/broken scaffolding file (tooling or the index.md header) - not for authoring or maintaining concepts, which is the lokf-librarian skill''s job.'
---

# LOKF Scaffolding

Create a fresh **`.lokf/` sidecar** - a machine-readable, SPARQL-queryable [LOKF](https://lokf.nolan-nichols.com/) knowledge bundle - inside whatever repository this skill is invoked from. This skill lays down the directory, tooling, docs, and a small **dummy** bundle skeleton, then hands off to the **lokf-librarian** skill to fill it with real knowledge.

**Why this matters:** plain OKF is *prose + structure*; most hand-rolled OKF sidecars bolt on repo-local *tools*; LOKF is *prose + structure + **meaning** + tools* - the semantic layer is what makes the tooling standard and portable (generated from the LOKF LinkML schema, queryable by any RDF/SPARQL tool), which is why this scaffold ships the generated `lokf` toolkit rather than bespoke scripts.

## Scope - how this differs from lokf-librarian

This is a **one-shot bootstrap** skill; it should **not** overlap with the day-to-day **lokf-librarian** skill:

- **lokf-scaffolding (this skill)** - run **once** to create `.lokf/`, or to **repair** a missing/broken *scaffolding* file (`pyproject.toml`, `justfile`, `README.md`, `queries.http`, `.gitignore`, the `index.md` semantic header, or a Step 5 automation file). It never authors real concepts - only the dummy skeleton.
- **lokf-librarian** - run **often** to scrape the repo and create/maintain/audit the actual concept files and their typed relations.

> Guardrails: if `.lokf/` already exists and is healthy, don't run this skill - use
> **lokf-librarian**. When repairing, only (re)write the scaffolding file that is
> missing or broken; **never overwrite existing concept files** - that is
> lokf-librarian's domain.

## Portability - reusing this skill in another repo

This skill is repo-agnostic; run it in any repository, including an empty one. Assumptions to satisfy when reusing it elsewhere:

- **It pairs with the lokf-librarian skill.** The scaffolded wrapper script resolves
  `lokf-librarian/SKILL.md` from the repo's skill directory - it checks `.claude/skills/`
  (Claude Code) then `.github/skills/` (Copilot-style agents) - so copy **both** `lokf-scaffolding`
  and `lokf-librarian` into whichever of those the new repo uses. Both skills are generic:
  copy them unmodified; the librarian's first run discovers the project's knowledge sources
  and records the map inside the bundle itself (`playbooks/knowledge-sources.md`).
- **Tooling:** validation uses [`uv`](https://docs.astral.sh/uv/) + the `lokf` toolkit
  ([`just`](https://just.systems/) is optional). The files scaffold fine without them;
  only Step 4's validation needs them installed.
- **The host need not be git, GitHub, or Linux.** The scaffold is just files, so any
  directory tree works: a plain local or shared filesystem, or Storage-as-a-Service
  content mounted/synced locally (Drive, Dropbox, an S3/blob mount, ...). Adjust as follows:
  - *No git*: `.gitignore` is inert - keep it (a VCS may arrive later) or drop it; skip
    the "commit" instructions and rely on the platform's own versioning/backup, and
    review changes by whatever mechanism the host offers instead of PRs.
  - *Not GitHub* (other forges, or no forge): Step 5's workflow files are GitHub
    Actions-specific - skip them and schedule `.lokf/scripts/knowledge-librarian.sh`
    (plus `lokf validate` as the gate) with the platform's equivalent: another CI's
    pipeline, cron, or a systemd timer. The wrapper needs only `bash` and the skill file.
  - *Not Linux/POSIX*: run the `justfile` recipes and wrapper from a POSIX shell
    (on Windows: WSL or Git Bash), or bypass them and call `uv run lokf ...` directly -
    `uv` and the toolkit are cross-platform.

## Step 0 - Gather the host project's facts (do this first)

The templates below are generic and use placeholders. **Before writing any file, inspect the repository this skill sits inside and resolve every placeholder from real project sources** - never leave a `<...>` token or a dummy value in the final output. Good sources, in rough priority order:

| Placeholder | Meaning | Where to find it |
|-------------|---------|------------------|
| `<PROJ_NAME>` | Human-readable project name | the project manifest `name` (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `composer.json`, ...), the root `README.md` title, a service-catalog entry, or the repo name |
| `<PROJ_DESC>` | One-sentence project description | the project manifest `description`, the README intro, or a service-catalog entry |
| `<PROJ_SLUG>` | lowercase-hyphenated slug for the Python package name | derive from `<PROJ_NAME>` (e.g. `Acme Platform` -> `acme-platform`) |
| `<BASE_IRI>` | Bundle base IRI - **must end with `/`** | in priority order: (1) a persistent-identifier namespace the project already publishes under (schema/ontology `id` declarations using w3id.org, purl.org, or a project-owned domain) + `/knowledge/`; (2) a stable project URL the project controls (docs `site_url`, GitHub/GitLab Pages, service-catalog entry) + `/knowledge/`; (3) if neither exists, `https://<PROJ_SLUG>.example/knowledge/` and flag it for review. **Never** use the code-host repo URL (e.g. `https://github.com/<org>/<repo>/knowledge/`): that path space belongs to the host's routing, so the minted IDs can never be made to resolve and misattribute naming authority to the host |
| `<OWNER_NAME>` | Owning team/org display name | `CODEOWNERS`, the manifest's authors/owner, a service-catalog entry, or the README |
| `<OWNER_SLUG>` | lowercase-hyphenated slug for the owner | derive from `<OWNER_NAME>` |
| `<TODAY>` | Today's date, `YYYY-MM-DD` | the system clock (used in `log.md`) |

`<BASE_IRI>` is load-bearing: `base_iri` + a concept's path mints its `@id` - a globally unique identifier that happens to look like a URL. It does not need to resolve in a browser today, but it must be stable *and* live in a namespace the project controls so it *can* be made to resolve later (see the lokf-librarian skill's Rule 2 for the full authority test and how to migrate a wrong base). Keep the trailing slash.

If the host is a plain directory tree with none of the sources above (no manifest,
no `CODEOWNERS`, no repo): fall back to the directory name for `<PROJ_NAME>`, any
document in the tree for `<PROJ_DESC>`/`<OWNER_NAME>`, and the `https://<PROJ_SLUG>.example/knowledge/`
fallback for `<BASE_IRI>` - and flag every guessed value for review in the Step 6 handoff.

## Step 1 - Create the directory skeleton

```
.lokf/
|-- .gitignore                # keeps .venv/ and build artifacts out of git
|-- pyproject.toml            # declares the `lokf` toolkit dependency
|-- justfile                  # convenience recipes
|-- README.md                 # human intro
|-- queries.http              # (optional) ready-to-run SPARQL examples
|-- scripts/                  # (optional, Step 5) the knowledge-librarian.sh wrapper
|-- knowledge/                # the bundle - one Markdown file per concept
    |-- index.md              # bundle metadata (base_iri, context, ...) + TOC (reserved)
    |-- log.md                # change history (reserved)
    |-- services/             # start with dummy services; add metrics/policies/... as you grow
        |-- index.md
        |-- example-service-a.md
        |-- example-service-b.md
```

## Step 2 - Write the files (substitute every placeholder from Step 0)

### `.lokf/pyproject.toml`

```toml
# LOKF sidecar for <PROJ_NAME>.
#
# A small Python "sidecar" that lets this repo validate and project its
# knowledge/ bundle with the `lokf` toolkit. It does not affect the app build.
#
#   uv sync             # install lokf into a local .venv
#   just lokf-validate  # validate knowledge/ against the LOKF schema
[project]
name = "<PROJ_SLUG>-knowledge"
version = "0.1.0"
description = "LOKF knowledge-bundle tooling for <PROJ_NAME>."
# Keep in sync with the `lokf` toolkit's own requires-python floor.
requires-python = ">=3.10"
dependencies = [
    "lokf[build]>=0.5.0",
]

[tool.uv]
package = false
```

### `.lokf/.gitignore`

```gitignore
# Python sidecar artifacts (do not commit)
.venv/
__pycache__/
*.pyc
lokf-tables/
```

### `.lokf/justfile`

```just
# LOKF knowledge-bundle recipes for <PROJ_NAME>.
#
# The `lokf` toolkit is a Python sidecar (see pyproject.toml); these recipes
# drive it against the knowledge/ bundle. Run `just --list` to see them.

bundle := "knowledge"

# List available recipes
default:
    @just --list

# Install the lokf sidecar toolkit into a local .venv
lokf-install:
    uv sync

# Assemble and validate the knowledge bundle against the LOKF schema
lokf-validate:
    uv run lokf validate {{ bundle }}

# Project the bundle (or a concept file) to RDF (Turtle) on stdout
lokf-convert FILE=bundle:
    uv run lokf convert --format ttl {{ FILE }}

# Serve the bundle locally: SPARQL endpoint + live graph explorer
lokf-serve:
    uv run lokf serve {{ bundle }}
```

### `.lokf/knowledge/index.md` (bundle root - carries the semantic header)

```markdown
---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: <BASE_IRI>
context: https://w3id.org/lokf/context.jsonld
title: <PROJ_NAME> Knowledge Bundle
description: <PROJ_DESC>
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Organization
  id: <BASE_IRI>org/<OWNER_SLUG>
  name: <OWNER_NAME>
---

# <PROJ_NAME> Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for <PROJ_NAME>. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Example Service A](services/example-service-a.md) - placeholder; replace with a real service.
* [Example Service B](services/example-service-b.md) - placeholder; replace with a real service.
```

### `.lokf/knowledge/services/index.md`

```markdown
# Services

* [Example Service A](example-service-a.md) - placeholder; replace with a real service.
* [Example Service B](example-service-b.md) - placeholder; replace with a real service.
```

### `.lokf/knowledge/services/example-service-a.md` (DUMMY - replace)

```markdown
---
type: Service
id: <BASE_IRI>services/example-service-a
title: Example Service A
description: Placeholder service - replace with a real service of <PROJ_NAME>.
endpoint: https://<PROJ_SLUG>.example/api/example-a
---

# Overview

**Example Service A** is a dummy concept created by scaffolding. Replace its frontmatter and body with a real service, and wire it to other concepts with
typed relations (e.g. `dependsOn`, `about`, `references`).
```

### `.lokf/knowledge/services/example-service-b.md` (DUMMY - replace)

```markdown
---
type: Service
id: <BASE_IRI>services/example-service-b
title: Example Service B
description: Placeholder service - replace with a real service of <PROJ_NAME>.
endpoint: https://<PROJ_SLUG>.example/api/example-b
dependsOn:
  - <BASE_IRI>services/example-service-a
---

# Overview

**Example Service B** is a dummy concept that depends on Example Service A, to show a typed relation. Replace it with a real service.
```

### `.lokf/knowledge/log.md`

```markdown
# Change Log

## <TODAY>
* **Initialization**: Scaffolded the LOKF bundle for <PROJ_NAME> with placeholder
  services. Real concepts to follow.
```

### `.lokf/README.md`

The template is shown inside a **five-backtick** fence so its own triple-backtick
code blocks survive; write the file itself with normal triple-backtick blocks.

`````markdown
# `.lokf/` - <PROJ_NAME>'s machine-readable knowledge base

A small **sidecar** that captures <PROJ_NAME>'s own knowledge - its services, metrics, policies, playbooks, and glossary - as plain Markdown files that are **also a queryable knowledge graph**. It does not touch the app build; it's independent tooling you can run on its own.

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
`````

### `.lokf/queries.http` (optional - include unless the user opts out)

```http
### LOKF SPARQL queries for the <PROJ_NAME> knowledge bundle.
###
### Requires a VS Code "REST Client" extension (humao.rest-client).
### Start the endpoint first (from this directory):
###     just lokf-serve          # or: uv run lokf serve knowledge
### Then click "Send Request" above any query below.
###
### The server presets the LOKF schema prefixes (lokf:, schema:, dcterms:,
### prov:, org:, skos:, rdf:, rdfs:, ...), so no PREFIX lines are needed.

@base = http://127.0.0.1:8000

### 1. Inventory - count concepts by type
POST {{base}}/sparql
Content-Type: application/sparql-query

SELECT ?type (COUNT(?s) AS ?count)
WHERE { ?s a ?type . FILTER(?type != rdf:Statement) }
GROUP BY ?type
ORDER BY DESC(?count)

### 2. All services and their endpoints
POST {{base}}/sparql
Content-Type: application/sparql-query

SELECT ?title ?endpoint
WHERE { ?s a schema:WebAPI ; schema:name ?title .
        OPTIONAL { ?s schema:url ?endpoint } }
ORDER BY ?title

### Bonus: whole graph as Turtle (CONSTRUCT -> text/turtle)
POST {{base}}/sparql
Content-Type: application/sparql-query

CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }
```

## Step 3 - Verify the skeleton

Before finishing, confirm the scaffold is clean - but do **not** author real concepts here (that is lokf-librarian's job):

1. Resolve every placeholder from Step 0 and confirm none survive. Search for the
   placeholder tokens specifically - the finished files legitimately contain other
   angle brackets (`<kind>` in the README, autolink URLs, commented examples), so
   don't grep for a bare `<`:

   ```bash
   grep -rn -e '<PROJ_' -e '<BASE_IRI>' -e '<OWNER_' -e '<TODAY' .lokf/
   ```

   Zero hits means the scaffold is fully resolved.
2. Leave the `services/example-service-*.md` concepts as clearly-marked dummies (or delete them for an empty bundle); do not try to enumerate the project's real services here.

## Step 4 - Validate the skeleton

Confirm the scaffold itself is schema-valid before handing off:

```bash
cd .lokf
just lokf-install     # uv sync
just lokf-validate    # -> the skeleton passes the LOKF schema
```

If `uv` is not installed (or the `lokf` package cannot be fetched), **skip this
step rather than failing**: note the skipped validation in your handoff message,
so it runs in CI (Step 5) or once the tooling is available. Do not record it in
`knowledge/log.md` - the log tracks knowledge changes, not administrative events.

Fix any structural/schema findings, then commit the scaffold. Routine validation
and auditing thereafter belong to lokf-librarian; Step 5 scaffolds the CI gate and
the scheduled loop that run it, and Step 6 hands off.

## Step 5 - (optional) Scaffold the automation

Three files automate validation and the scheduled refresh loop. Scaffolding them
is one-time setup, so it belongs here; how they behave at run time is documented
in **lokf-librarian** step 4 (this step only lays them down). The two workflow files
are **GitHub-specific**: on any other host, scaffold only the wrapper script and
schedule it (plus `lokf validate`) with the platform's own scheduler - see the
Portability section. All are generic - the only project-specific choice is the
runner (`ubuntu-latest` below; swap in a self-hosted runner group and internal-CA
env if your org needs them). The pinned action SHAs carry a version comment; bump
them with your usual update tooling.

### `.github/workflows/knowledge-validate.yaml` - the validation gate

Runs `lokf validate` on every `.lokf/**` PR and weekly.

```yaml
name: Knowledge Bundle Validation

# Validate the LOKF knowledge bundle whenever it (or its tooling) changes, and on
# a weekly schedule.
on:
  pull_request:
    paths:
      - ".lokf/**"
      - ".github/workflows/knowledge-validate.yaml"
  schedule:
    - cron: "0 6 * * 1" # Mondays at 06:00 UTC
  workflow_dispatch:

# Cancel superseded runs on the same ref to save runner time.
concurrency:
  group: knowledge-validate-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    name: Validate the LOKF bundle
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - name: Checkout
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2

      - name: Set up uv
        uses: astral-sh/setup-uv@d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86 # v5
        with:
          python-version: "3.12"

      - name: Install the lokf sidecar
        run: uv sync
        working-directory: .lokf

      - name: Validate the knowledge bundle
        run: uv run lokf validate knowledge
        working-directory: .lokf
```

### `.github/workflows/knowledge-librarian.yaml` - the scheduled loop

Runs the librarian agent weekly, then opens a review PR with whatever changed.

```yaml
name: Knowledge Librarian

# Scheduled LLM "librarian" that keeps the .lokf/ bundle in step with the repo (the
# Karpathy rule): run the agent, validate, and open a review PR with whatever
# changed. It NEVER pushes to the default branch and NEVER auto-merges; no changes
# -> no PR; and it is inert until KNOWLEDGE_LIBRARIAN_CMD is set.
on:
  schedule:
    - cron: "0 5 * * 1" # Mondays at 05:00 UTC
  workflow_dispatch:

permissions:
  contents: write # create/push the librarian branch
  pull-requests: write # open the review PR

concurrency:
  group: knowledge-librarian
  cancel-in-progress: false

jobs:
  librarian:
    name: Refresh the LOKF bundle
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          fetch-depth: 0

      - name: Set up uv
        uses: astral-sh/setup-uv@d4b2f3b6ecc6e67c4457f6d3e41ec42d3d0fcb86 # v5
        with:
          python-version: "3.12"

      - name: Install the lokf sidecar
        id: install-lokf
        continue-on-error: true
        run: uv sync
        working-directory: .lokf

      # Wire this up: point the KNOWLEDGE_LIBRARIAN_CMD repo variable at your agent
      # command (e.g. `bash .lokf/scripts/knowledge-librarian.sh`). Unset = safe no-op.
      # The scaffolded wrapper also reads AGENT_CLI; pass it through here (switch to
      # `secrets.AGENT_CLI` if the command embeds a token).
      - name: Run the librarian agent
        env:
          KNOWLEDGE_LIBRARIAN_CMD: ${{ vars.KNOWLEDGE_LIBRARIAN_CMD }}
          AGENT_CLI: ${{ vars.AGENT_CLI }}
        run: |
          set -euo pipefail
          if [ -z "${KNOWLEDGE_LIBRARIAN_CMD:-}" ]; then
            echo "::notice::KNOWLEDGE_LIBRARIAN_CMD is not set - skipping the agent step."
            exit 0
          fi
          bash -c "${KNOWLEDGE_LIBRARIAN_CMD}"

      - name: Validate the LOKF bundle
        id: validate-lokf
        if: steps.install-lokf.outcome == 'success'
        continue-on-error: true
        run: uv run lokf validate knowledge
        working-directory: .lokf

      - name: Detect changes
        id: diff
        run: |
          set -euo pipefail
          # Scope to the bundle so tool artifacts (e.g. a fresh .lokf/uv.lock from
          # `uv sync`) never trigger a PR by themselves.
          if [ -n "$(git status --porcelain -- .lokf/knowledge)" ]; then
            echo "changed=true" >> "$GITHUB_OUTPUT"
          else
            echo "changed=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Commit and push the librarian branch
        id: push
        if: steps.diff.outputs.changed == 'true'
        run: |
          set -euo pipefail
          branch="knowledge-librarian/$(date -u +%Y-%m-%d)-${GITHUB_RUN_ID}"
          git config user.name  "knowledge-librarian[bot]"
          git config user.email "knowledge-librarian[bot]@users.noreply.github.com"
          git checkout -b "$branch"
          git add -- .lokf/knowledge
          git commit -m "chore(lokf): scheduled librarian refresh of the knowledge bundle" \
                     -m "Automated Karpathy-rule pass. Review required - do not auto-merge."
          git push --set-upstream origin "$branch"
          echo "branch=$branch" >> "$GITHUB_OUTPUT"

      - name: Open the review PR
        if: steps.diff.outputs.changed == 'true'
        uses: actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd # v8
        env:
          BRANCH: ${{ steps.push.outputs.branch }}
          LOKF_OUTCOME: ${{ steps.validate-lokf.outcome }}
        with:
          script: |
            const { BRANCH, LOKF_OUTCOME } = process.env;
            // On `schedule` triggers the event payload is empty, so resolve the
            // default branch via the API rather than context.payload.repository.
            const { data: repo } = await github.rest.repos.get(context.repo);
            const base = repo.default_branch;
            const check = (o) =>
              o === 'success' ? 'pass'
              : o === 'failure' ? 'failed (review the run log)'
              : 'skipped';
            const body = [
              '## Scheduled knowledge-librarian refresh',
              '',
              'Automated Karpathy-rule pass: the librarian agent re-scraped the repo',
              'and reconciled the `.lokf/` bundle. A human maintainer must review and',
              'approve - this PR must not be auto-merged.',
              '',
              `- LOKF validation (\`lokf validate\`): ${check(LOKF_OUTCOME)}`,
              '',
              '### Reviewer checklist',
              '- [ ] Claims trace to a source of truth.',
              '- [ ] `type`/frontmatter and typed relations are correct.',
              '- [ ] Validation findings above are acceptable or addressed.',
            ].join('\n');
            const { data: pr } = await github.rest.pulls.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              head: BRANCH,
              base,
              title: 'chore(lokf): scheduled librarian refresh of the knowledge bundle',
              body,
            });
            console.log(`Opened PR #${pr.number}: ${pr.html_url}`);
```

### `.lokf/scripts/knowledge-librarian.sh` - the agent wrapper

Create it (then `chmod +x`). It is generic - no placeholders - but expects the
**lokf-librarian** skill in the repo's skill directory (it looks in `.claude/skills/`
then `.github/skills/`), so ensure that skill is present too.

```bash
#!/usr/bin/env bash
#
# Wrapper for the scheduled knowledge-librarian loop (Karpathy rule).
#
# `.github/workflows/knowledge-librarian.yaml` invokes whatever the
# `KNOWLEDGE_LIBRARIAN_CMD` repository variable points at. Set that variable to:
#
#     bash .lokf/scripts/knowledge-librarian.sh
#
# ...and set `AGENT_CLI` (repo variable or secret) to the command that runs your
# coding agent non-interactively - e.g. the GitHub Copilot CLI or an internal
# agent runner that accepts a prompt on `-p`/stdin.
#
# CONTRACT (the workflow relies on this):
#   - This script only READS the repo and WRITES files under .lokf/knowledge/
#     (the workflow diffs and commits that path only; tooling files are
#     lokf-scaffolding's domain).
#   - It MUST NOT git commit, push, or open PRs - the workflow owns that.
#   - On success it exits 0 whether or not it changed anything; the workflow
#     diffs the working tree to decide whether to open a PR.
#
# Inputs (env):
#   AGENT_CLI   command that runs the agent given a prompt via -p "<prompt>"
#
set -euo pipefail

# Resolve the repo root from this script's location so it works regardless of cwd.
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

# The lokf-librarian skill may live under either skill-directory convention.
skill=""
for candidate in .claude/skills/lokf-librarian/SKILL.md .github/skills/lokf-librarian/SKILL.md; do
  if [ -f "$candidate" ]; then skill="$candidate"; break; fi
done
[ -n "$skill" ] || {
  echo "knowledge-librarian: lokf-librarian SKILL.md not found in .claude/skills/ or .github/skills/" >&2
  exit 2
}

if [ -z "${AGENT_CLI:-}" ]; then
  cat >&2 <<'EOF'
knowledge-librarian: AGENT_CLI is not set.

Set AGENT_CLI to your non-interactive agent command (e.g. a Copilot CLI or
internal runner). This wrapper hands it a prompt built from the lokf-librarian
skill; the agent is expected to edit files under .lokf/knowledge/ only.
EOF
  exit 2
fi

# Build the prompt. The agent should follow the skill verbatim, edit only the
# .lokf/knowledge/ bundle, and make no VCS operations.
prompt="$(cat <<EOF
You are the repository knowledge librarian. Follow this skill file verbatim:
  - $skill

Task (Karpathy rule - continuous small corrections, not a rewrite):
  1. Follow the skill's Scrape & build procedure: bootstrap discovery if the
     bundle has no real concepts yet, otherwise the steady-state refresh of the
     sources recorded in the bundle (concept provenance and
     .lokf/knowledge/playbooks/knowledge-sources.md).
  2. Reconcile the .lokf/ knowledge bundle with the repository: add missing
     concepts, correct stale facts (refreshing each changed concept's
     `generated` provenance, which supersedes the v0.1 `timestamp`), wire
     typed relations, and prepend dated entries to
     .lokf/knowledge/log.md - but only when the bundle content actually
     changed. If nothing changed, leave the bundle (including log.md)
     untouched; do not log administrative no-op runs.
  3. Only edit files under .lokf/knowledge/. Do NOT run git, open PRs, or touch
     any other path. Cite sources for any claim whose authority is outside the
     repository.
EOF
)"

echo "knowledge-librarian: refreshing the .lokf/ bundle via AGENT_CLI"
# shellcheck disable=SC2086
$AGENT_CLI -p "$prompt"
```

## Step 6 - Hand off to lokf-librarian

Scaffolding ends here. **Hand off to the lokf-librarian skill** to scrape the
repository and create/maintain the real concepts, typed relations, and index/log
entries - that is where all authoring rules live. The librarian's first run is a
**bootstrap discovery** pass: it sweeps the repository for knowledge sources and
records the map as a reviewed concept (`playbooks/knowledge-sources.md`), which
later scheduled runs re-verify instead of re-discovering. In the handoff, tell the user:

- which Step 0 values were **guessed** rather than found (especially a fallback
  `<BASE_IRI>` - it mints every concept's RDF `@id`, so it needs sign-off);
- whether Step 4 validation ran or was skipped (missing `uv`/`lokf`);
- which optional pieces (`queries.http`, Step 5 automation) were scaffolded.
