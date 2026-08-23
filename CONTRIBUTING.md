# Contributing to wiki-templates

This monorepo collects wiki templates: each subdirectory is a standalone
starting point for a docs site powered by Wiki CLI. Proposals for new
integrations and templates are tracked here — this guide is the quality bar
they must meet.

## Filing a proposal

Template proposals are tracked in `wazootech/wiki-templates`, not in
`wazootech/wiki`. Prefer the GitHub issue form:
[`.github/ISSUE_TEMPLATE/integration-template.yml`](.github/ISSUE_TEMPLATE/integration-template.yml).

Before filing, review existing open proposals to avoid duplicate scope:

```bash
gh search issues --repo wazootech/wiki-templates --label template --state open
```

If filing via `gh issue create`, preserve the form's structure and apply the
`template` label:

```bash
gh issue create --repo wazootech/wiki-templates --label template --body-file proposal.md
```

The [template program umbrella issue](https://github.com/wazootech/wiki-templates/issues/4)
tracks the ranked backlog; reference its bucket when relevant.

## The boundary rule

Every integration proposal must make the boundary explicit:

- **Wiki CLI owns the semantic Markdown source layer**: `wiki.yml`, documents,
  frontmatter, SHACL, JSON Schema, lint, fmt, SPARQL, RDF/JSON-LD export,
  render, build, and serve.
- **The integration owns a distinct role**: runtime memory, retrieval,
  publishing surface, agent workflow, issue-tracker bridge, domain model, or
  downstream application.
- Derived indexes, generated memories, PR comments, vector stores, and external
  runtimes are **not** the canonical Wiki corpus unless explicitly promoted into
  Wiki pages and validated.

## Classifying the integration

Place every proposal in one category:

1. Agent workflow / coding agent
2. Runtime memory / retrieval
3. Static site / publishing surface
4. Issue tracker / work management
5. Domain-specific knowledgebase
6. Ontology / linked data
7. RAG / GraphRAG / search

## Proposal sections

Drafts (by hand or via the issue form) use these sections:

1. Goal
2. Why this matters
3. Boundary between Wiki CLI and the integration
4. Recommended architecture
5. Template subdirectory
6. Template contents
7. Wiki corpus examples
8. Validation and CI
9. README positioning
10. Non-goals
11. Acceptance criteria
12. Open questions
13. Related issues and references

## Quality bar

A good proposal:

- states the proposed template as a **subdirectory of this monorepo**, e.g.
  `wazootech/wiki-templates/<integration>/` — templates are monorepo
  subdirectories, not standalone `wazootech/wiki-*-template` repos;
- explains what Wiki CLI owns and what the integration owns;
- includes deterministic validation commands;
- avoids requiring private credentials in CI;
- includes provenance and citation expectations;
- names related template issues;
- cites primary external documentation;
- explains whether the template is standalone or should fold into an existing
  template.

## Default validation block

Templates validate with the standard gate:

```bash
wiki -c wiki.yml fmt --check
wiki -c wiki.yml lint --strict
wiki -c wiki.yml check --strict
wiki -c wiki.yml render --check
```

Use `docs/wiki.yml` instead of `wiki.yml` when the template follows this
repository's dogfooding layout.
