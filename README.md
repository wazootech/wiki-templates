# Wiki Templates

Starter templates for [Wiki CLI](https://github.com/wazootech/wiki) — vault scaffolds, publish integrations, and framework starters.

Each subdirectory is a self-contained template you can clone and customize. See the individual READMEs for setup instructions.

## Templates

| Template | Description | Stack |
|----------|-------------|-------|
| [generic](generic/) | Minimal Wiki CLI starter — equivalent to `wiki init` output with GitHub Pages deploy | Python, Jinja2 |
| [quartz](quartz/) | Quartz publish integration for wiki vaults | TypeScript, Quartz |
| [llm-wiki](llm-wiki/) | LLM Wiki pattern starter — agent gardening, SHACL shapes, SPARQL indexes | Python, Jinja2 |
| [yasgui](yasgui/) | YASGUI SPARQL explorer for browsing wiki graph data | HTML, shell |
| [wikipedia](wikipedia/) | Wikipedia-themed static site builder using Wiki Python API | Python, Jinja2 |
| [mintlify](mintlify/) | Mintlify docs site from a Wiki CLI vault | TypeScript, Mintlify |
| [holocron](holocron/) | Holocron docs site from a Wiki CLI vault | TypeScript, Vite |
| [astro](astro/) | Astro SSG consuming wiki export JSON-LD | TypeScript, Astro |
| [nextjs](nextjs/) | Next.js App Router SSG consuming wiki export JSON-LD | TypeScript, Next.js |
| [camunda](camunda/) | Camunda BPMN/DMN governance knowledge base | Markdown, SHACL, JSON Schema |
| [cocoindex](cocoindex/) | CocoIndex incremental memory sidecar with pgvector | Python, Docker, pgvector |

## Quick start

```bash
# Clone a template
git clone https://github.com/wazootech/wiki-templates.git
cd wiki-templates/<template>

# Follow the template's README for setup
cat README.md
```

## Creating a new template

Each template should contain at minimum:

- `wiki.yml` — Wiki CLI configuration
- `wiki/` — Sample markdown pages with semantic frontmatter
- `README.md` — Setup instructions and template description
- `.github/workflows/` — CI for wiki check/lint and optional deploy

Templates with a `wiki.yml` must pass `wiki check --strict` and
`wiki lint --strict`. The repository CI enforces this across all templates, so
run both commands locally for your template before opening a PR.

See `generic/` for the minimal structure.

## History

These templates were consolidated from 11 individual repos into this monorepo to reduce clutter in the [wazootech](https://github.com/wazootech) organization. The original repos are archived with redirect notices.
