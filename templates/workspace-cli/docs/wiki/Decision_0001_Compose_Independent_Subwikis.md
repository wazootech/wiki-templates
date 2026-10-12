---
type: wspace:WorkspaceDecision
headline: Compose independent sub-wikis as sourced datasets
description: ADR-0001 records the decision to compose independent sub-wiki repositories instead of maintaining a single monolithic corpus.
wspace:status: accepted
wspace:decisionOwner: Platform Workspace Team
wspace:decisionDate: '2026-01-15'
---

# Compose independent sub-wikis as sourced datasets

## Context

Each team maintained its own wiki, but queries needed a unified view. Flattening every corpus into one repository created cross-team coupling and stale ownership.

## Decision

Keep each sub-wiki in its own git repository and compose them as `sources` from the umbrella `wiki.yml` config. `wiki install` pins refs, `wiki update` refreshes them, and named graphs preserve provenance.

## Consequences

- Cross-team schemas live in the umbrella `docs/shapes/` directory.
- Provenance is explicit; a result can name its source graph.
- Sub-wikis can be on a different release cadence than the umbrella.

See [Composed Workspace](Composed_Workspace.md).
