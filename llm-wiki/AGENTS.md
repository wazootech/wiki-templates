# Agent instructions (LLM Wiki vault)

This repository follows the [LLM Wiki](https://github.com/wazootech/wiki/blob/main/docs/wiki/LLM_Wiki.md) pattern.

## Before editing vault pages

1. `wiki check --strict` — integrity (SHACL, JSON Schema, routes)
2. `wiki lint --strict` — conventions (links, filenames, headings)

## After editing markdown

1. `wiki fmt` on changed files under `wiki/`
2. If pages contain `<!-- sparql:start -->` blocks: `wiki render`

## Link hygiene

- Use Markdown links to wiki pages (`Page_Name.md`) when `link.style` is `markdown`.
- Run `wiki link` to suggest missing links; `wiki link --apply` only with user approval.

## Do not

- Commit `_site/` build output
- Vendor agent skill bundles unless explicitly requested
