<!-- template-payload: ships with this template; scaffolds into generated docs sites -->

This file is **template payload**: inside `wazootech/wiki-templates` it marks
shipped content; in every site scaffolded from this template it serves as live
agent instructions. First-party agents editing the template itself should load
the governing skill or reference before changing template internals.

# Agent guidelines

## What this repo is

A Wikipedia-themed static wiki, built from Markdown pages with semantic
frontmatter by the [Wiki CLI](https://github.com/wazootech/wiki). This is a
content/wiki repo: the operating surface is Markdown under `wiki/`, a `wiki.yml`
content/wiki repo: the operating surface is Markdown under `wiki/`, a `wiki.yml` config, and the `build.ts` Bun site builder.

- Preserve template portability and avoid Wazoo-specific content unless the user
  asks to specialize it.
- Keep documentation examples concrete but generic.
- Check for an existing page before creating a new wiki page; update in place
  rather than duplicating.
- Every page needs semantic frontmatter (`type:`, schema properties). Use one
  page per durable entity once it needs lifecycle tracking.
- Add or update a saved query in `queries/` when a recurring question should be
  answered from semantic frontmatter.
- Before finishing, check README links and template file names for consistency.

## Tooling

- Wiki CLI: `wiki` (pip package `wazootech-wiki==0.7.2`). Install with
  `pip install wazootech-wiki==0.7.2`.
- `wiki.yml` at the repo root controls validation severities, link style,
  filename pattern, RDF prefixes, and formatting. Read it before changing
  tooling behavior.
- The Wikipedia theme renders only through `bun build.ts` (not `wiki serve`
  or `wiki build`), because `build.ts` fills the theme's extra layout tokens
  (`infobox`, `toc`, `backlinks`, `categories`, `metadata`).
- Bun is required for the build: `bun install`, then `bun build.ts`. The
  template ships `package.json` and `bunfig.toml`; commit the `bun.lock` your
  first install writes.

## Style guidelines

- ATX `#` headings only (no Setext underlines).
- Title case for H1, sentence case for H2+.
- Standard Markdown links (`[Team](wiki/Team.md)`); no Obsidian-style wikilinks.
- Keep author-facing notes in YAML frontmatter comments (`# ...`), not HTML
  comments in the page body: the renderer escapes raw HTML, so `<!-- ... -->`
  shows up as visible text on the built page.
- No decorative emoji in headings or operating docs.
- Semantic frontmatter required on all wiki pages.
- `wiki fmt` enforces most formatting; run it before committing.

## Verification

After meaningful edits, run:

- `git diff --check`
- `wiki -c wiki.yml fmt --check`
- `wiki -c wiki.yml lint --strict`
- `wiki -c wiki.yml check --strict`
- `wiki -c wiki.yml render --check` (embedded SPARQL blocks still current)
- `bun build.ts --output-dir _site` (confirm no raw `%wiki.*%` tokens in the
  built HTML)
