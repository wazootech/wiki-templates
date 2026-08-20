---
type: wspace:ComposedWorkspace
headline: Named Graphs
description: How composed sub-wiki sources appear as named graphs and how queries prove provenance.
wspace:compositionScope: Provenance and graph-addressing model for composed sub-wikis
---

# Named Graphs

Composed sub-wikis are loaded into named graphs so a query result can always name its origin repository. The umbrella corpus and installed sources live under distinct graph URIs.

## Graph URIs

| graph                                                                 | contents                      |
| --------------------------------------------------------------------- | ----------------------------- |
| `https://wazootech.github.io/wiki-templates/workspace-cli/docs/wiki/` | umbrella corpus (root)        |
| `https://github.com/acme/alpha-brain`                                 | `alpha-brain` sub-wiki corpus |
| `https://github.com/acme/beta-brain`                                  | `beta-brain` sub-wiki corpus  |

## Union queries

Querying without a `GRAPH` clause spans every loaded corpus (umbrella plus all installed sources), so the dashboard in [Composed Workspace](Composed_Workspace.md) is a union view by default.

## Provenance queries

Restrict to a single source by its graph URI:

```sparql
PREFIX schema: <https://schema.org/>

SELECT ?name WHERE {
  GRAPH <https://github.com/acme/alpha-brain> {
    ?doc schema:headline ?name .
  }
}
```

Ready-made examples live in the `queries/` directory and are exercised by `scripts/compose-demo.sh`.

Start with [Composed Workspace](Composed_Workspace.md).
