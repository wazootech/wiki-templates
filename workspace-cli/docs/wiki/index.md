---
type: wspace:ComposedWorkspace
headline: Workspace CLI Composed Workspace
description: Umbrella Wiki corpus that composes independently-owned sub-wiki git repositories into one queryable semantic dataset.
wspace:compositionScope: Studio-wide knowledge across engineering, data, and product
---

# Workspace CLI Composed Workspace

This template demonstrates **recursive semantic datasets**: an umbrella Wiki corpus that composes independently-owned sub-wikis from separate git repositories into one queryable property graph while preserving named-graph provenance.

## Composition model

- Each sub-wiki lives in its own git repository with its own `wiki.yml`, corpus, shapes, and CI.
- The umbrella declares sub-wikis as `sources` in the `wiki.yml` config and pins them with `wiki install` / `wiki update`.
- Queries run across the union. Per-source `GRAPH` clauses prove provenance.

See [Composed Workspace](Composed_Workspace.md) for the source ledger and [Named Graphs](Named_Graphs.md) for the graph-URI model.

## Quick start

```sh
wiki -c docs/wiki.yml install   # pull pinned sub-wiki sources
wiki -c docs/wiki.yml check --strict
wiki -c docs/wiki.yml lint --strict
wiki -c docs/wiki.yml render --check
```

Start with [Composed Workspace](Composed_Workspace.md) and [Named Graphs](Named_Graphs.md).
