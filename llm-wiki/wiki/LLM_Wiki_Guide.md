---
type: TechArticle
headline: LLM Wiki guide
description: How agents and humans garden this LLM Wiki vault.
---

# LLM Wiki guide

This vault follows the [LLM Wiki](https://github.com/wazootech/wiki/blob/main/docs/wiki/LLM_Wiki.md) pattern: Obsidian (or any editor) is the IDE, the LLM is the programmer, the wiki is the codebase.

## Daily loop

```bash
wiki check --strict
wiki lint --strict
wiki serve --watch
```

After editing pages:

```bash
wiki fmt wiki/
wiki render   # when SPARQL blocks change
```

## Gardening rules

- Prefer Wikipedia-style filenames (`Concept_Name.md`).
- Use ATX headings; title-case H1 aligned with `headline` frontmatter.
- Link to existing pages with Markdown links (`Other_Page.md`).
- Add or extend SHACL shapes under `wiki/*_Shape.md` before introducing new document types.

## Embedded indexes

Add SPARQL result blocks to maintain dynamic tables (see [Style Guide](https://github.com/wazootech/wiki/blob/main/docs/wiki/Style_Guide.md)):

```markdown
<!-- sparql:start -->
```sparql
SELECT ?page WHERE { ?page a schema:Person }
```
<!-- sparql:end -->
```

Run `wiki render` to refresh stale tables.

## Related

- [Ethan_Davidson.md](Ethan_Davidson.md) — example person
- [Person_Shape.md](Person_Shape.md) — person SHACL shape
- [Concept_Shape.md](Concept_Shape.md) — concept/article shape
