# Contributing to wiki-templates

This repository holds one template,
[`templates/wikipedia/`](templates/wikipedia/): a Wikipedia-themed static site
builder that consumes the Wiki CLI artifact contract — the `wiki` command, the
`@wazoo/wiki` Deno API, and `@wazoo/wiki/theme`.

New templates are not being added here. The other eleven were retired on
2026-10-14 ([#64](https://github.com/wazootech/wiki-templates/issues/64)), and
this template may fold into [`wazootech/wiki`](https://github.com/wazootech/wiki)
once the engine can render the theme itself (wazootech/wiki#407 and
wazootech/wiki#409). Proposals for new integrations belong in that repository's
issue tracker.

## The boundary rule

- **Wiki CLI owns the semantic Markdown source layer**: `wiki.yml`, documents,
  frontmatter, SHACL, JSON Schema, lint, fmt, SPARQL, RDF/JSON-LD export,
  render, build, and serve.
- **The template owns a distinct role**: the publishing surface — layout,
  assets, and the build script that turns exported pages into HTML.

Derived indexes, generated memories, PR comments, vector stores, and external
runtimes are **not** the canonical Wiki corpus unless explicitly promoted into
Wiki pages and validated.

## Changing the template

- **Keep the engine contract intact.** `build.ts` substitutes the layout tokens
  the template computes itself; a change to the token set, the exported API, or
  the build output layout is an engine change and belongs in `wazootech/wiki`
  first.
- **Follow the template's own guide.** `templates/wikipedia/AGENTS.md` covers
  its style, build, and version-pin rules.
- **Template workflows are payload.** This repository's CI never executes
  `templates/*/.github/workflows/*`; they run in a scaffolded site.

## Validation

Templates validate with the standard gate:

```bash
bash scripts/validate-all.sh
```

which runs, per template config:

```bash
wiki -c wiki.yml fmt --check
wiki -c wiki.yml lint --strict
wiki -c wiki.yml check --strict
wiki -c wiki.yml render --check
```

Use `docs/wiki.yml` instead of `wiki.yml` when a template follows this
repository's dogfooding layout.

Pinned Wiki CLI versions are not edited by hand; see
[Keeping pins current](README.md#keeping-pins-current).
