# Wiki Templates

Starter templates for [Wiki CLI](https://github.com/wazootech/wiki) — vault scaffolds, publish integrations, and framework starters.

Each directory under `templates/` is a self-contained template you can clone and customize. See the individual READMEs for setup instructions.

## Templates

| Template | Description | Stack |
|----------|-------------|-------|
| [generic](templates/generic/) | Minimal Wiki CLI starter — equivalent to `wiki init` output with GitHub Pages deploy | Python, Jinja2 |
| [quartz](templates/quartz/) | Quartz publish integration for wiki vaults | TypeScript, Quartz |
| [llm-wiki](templates/llm-wiki/) | LLM Wiki pattern starter — agent gardening, SHACL shapes, SPARQL indexes | Python, Jinja2 |
| [yasgui](templates/yasgui/) | YASGUI SPARQL explorer for browsing wiki graph data | HTML, shell |
| [wikipedia](templates/wikipedia/) | Wikipedia-themed static site builder using Wiki CLI + Deno theme API | Deno, TypeScript |
| [mintlify](templates/mintlify/) | Mintlify docs site from a Wiki CLI vault | TypeScript, Mintlify |
| [holocron](templates/holocron/) | Holocron docs site from a Wiki CLI vault | TypeScript, Vite |
| [astro](templates/astro/) | Astro SSG consuming wiki export JSON-LD | TypeScript, Astro |
| [nextjs](templates/nextjs/) | Next.js App Router SSG consuming wiki export JSON-LD | TypeScript, Next.js |
| [camunda](templates/camunda/) | Camunda BPMN/DMN governance knowledge base | Markdown, SHACL, JSON Schema |
| [cocoindex](templates/cocoindex/) | CocoIndex incremental memory sidecar with pgvector | Python, Docker, pgvector |
| [workspace-cli](templates/workspace-cli/) | Composed workspace of independently-owned sub-wiki repos with named-graph provenance | Markdown, SHACL, bash |

## Quick start

```bash
# Clone a template
git clone https://github.com/wazootech/wiki-templates.git
cd wiki-templates/templates/<template>

# Follow the template's README for setup
cat README.md
```

## Creating a new template

Each template should contain at minimum:

- `wiki.yml` — Wiki CLI configuration
- `wiki/` — Sample markdown pages with semantic frontmatter
- `README.md` — Setup instructions and template description
- `.github/workflows/` — CI for the four wiki gates and optional deploy

Templates must pass all four wiki gates: `wiki fmt --check`, `wiki lint --strict`,
`wiki check --strict`, and `wiki render --check`. Each template's own
`.github/workflows/ci.yml` mirrors those four steps with an explicit `-c <config>`
and a pinned Wiki CLI; [`templates/generic/.github/workflows/ci.yml`](templates/generic/.github/workflows/ci.yml)
is the canonical copy to diff yours against. The repository CI auto-discovers
template configs (`wiki.yml`, `docs/wiki.yml`, or `sample/wiki.yml` per template)
and runs all gates across every template, so run the same loop locally before
opening a PR:

```bash
bash scripts/validate-all.sh
```

See `templates/generic/` for the minimal structure.

## Keeping pins current

Every template pins the Wiki CLI it is built against: `wazootech-wiki==<version>`
in its workflows and prose, `jsr:@wazoo/wiki@<version>` in its `deno.json`.
`scripts/wiki-pins.py` is the single place that knows where those pins live:

```bash
python scripts/wiki-pins.py scan         # read-only report: pins, published versions, drift
python scripts/wiki-pins.py check        # exit 1 when a pin is behind the published latest
python scripts/wiki-pins.py sync         # rewrite the pins that are behind
python scripts/wiki-pins.py assert-diff  # fail unless the diff only changes version substrings
```

`.github/workflows/pin-bumps.yml` runs `sync` weekly, and on demand; `assert-diff`
proves the result changes nothing but version substrings; then the job opens or
updates a single `pin-bumps` PR and stops. It never pushes to `main`, and it
closes the PR when nothing is behind any more. The job needs a `PIN_BUMP_TOKEN`
secret — a fine-grained PAT or GitHub App token with `contents: write` and
`pull_requests: write` — because a PR opened with the default `GITHUB_TOKEN`
does not trigger CI on itself.

## Why a monorepo?

Templates live in subdirectories of this repo rather than as separate `wazootech/wiki-<name>-template` repos. The tradeoffs:

- **Discoverability** — all templates are visible in one place; users can browse and compare without knowing repo names in advance.
- **Shared CI** — a single workflow runs `wiki fmt/lint/check/render` across every template, so a upstream Wiki CLI change that breaks a template is caught in one PR.
- **Atomic cross-template changes** — updates to shared conventions (lint rules, SHACL patterns, deploy workflows) land in one commit.
- **Lower maintenance overhead** — one repo to configure, one issue tracker, one set of branch protections.

The cost is that `wiki init --template` must shallow-clone the entire monorepo to copy one subdirectory. In practice this is fast (`--depth 1`) and a single network round-trip. If this ever becomes a concern, the GitHub Contents API could fetch individual template files without a full clone.

The original individual repos were consolidated to reduce clutter in the [wazootech](https://github.com/wazootech) organization.
