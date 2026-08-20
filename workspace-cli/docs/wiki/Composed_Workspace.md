---
type: wspace:ComposedWorkspace
headline: Composed Workspace
description: Ledger of sub-wiki sources composed into the umbrella corpus by wiki.yml sources blocks.
wspace:compositionScope: Source registry and ownership for composed sub-wikis
---

# Composed Workspace

The umbrella corpus composes sub-wiki repositories declared as `sources` in the `wiki.yml` config (under `docs/`). Each entry declares the owning repository, ref, and corpus path, and is pinned through `wiki install`.

## Source ledger

| sub-wiki                      | repo                                  | ref    | corpus path |
| ----------------------------- | ------------------------------------- | ------ | ----------- |
| [Alpha Brain](Alpha_Brain.md) | `https://github.com/acme/alpha-brain` | `main` | `wiki`      |
| [Beta Brain](Beta_Brain.md)   | `https://github.com/acme/beta-brain`  | `main` | `wiki`      |

## Declared sub-wikis

<!-- sparql:start -->

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX wspace: <https://wazootech.github.io/wiki-templates/workspace-cli/ns/wspace#>

SELECT ?source ?repo WHERE {
  ?doc rdf:type wspace:SubwikiSource .
  ?doc schema:headline ?source .
  ?doc wspace:sourceRepo ?repo .
}
ORDER BY ?source
```

| source | repo |
| --- | --- |
| Alpha Brain | https://github.com/acme/alpha-brain |
| Beta Brain | https://github.com/acme/beta-brain |

<!-- sparql:end -->

## Ownership model

- Umbrella corpus and shapes: platform/workspace team, reviewed in this repository.
- Sub-wiki corpora: owning teams, reviewed in each sub-wiki repository.
- Ownership is declared in `docs/shapes/Subwiki_Source_Shape.md` and enforced by `wiki check`.

End with [Named Graphs](Named_Graphs.md).
