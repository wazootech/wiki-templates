# Workspace CLI Composed Workspace Template

A semantic Wiki corpus that composes **independently-owned sub-wiki git repositories** into one
umbrella graph with named-graph provenance, following the `workspace-cli` semantic-dataset
conventions (recursive datasets).

This template shows the composition pattern: each sub-wiki stays in its own repo and review loop,
while the umbrella declares them as `sources`, pins them with `wiki install`, and queries the union
with per-source provenance.

## Quick start

```sh
pip install wazootech-wiki
wiki -c docs/wiki.yml check --strict
wiki -c docs/wiki.yml lint --strict
wiki -c docs/wiki.yml render --check
```

## Composition smoke test

`scripts/compose-demo.sh` seeds two temporary sub-wiki repositories, composes them as sources, runs
the four gates, and proves both sub-wikis surface in the union view — no credentials or network
remotes required.

```sh
bash scripts/compose-demo.sh
```

## Repository layout

- `docs/wiki.yml` — umbrella config; uncomment the `sources:` block to compose real sub-wikis.
- `docs/wiki/` — umbrella corpus (workspace, source ledger, named-graph model, decision record).
- `docs/shapes/`, `docs/schemas/` — SHACL shapes and JSON Schemas defining workspace metadata.
- `queries/` — SPARQL examples. `union-headlines.rq` spans all sources; `provenance-graphs.rq`
  names each source graph (needs a Wiki CLI with GRAPH support, newer than the 0.1.21 pin).
- `sample-subwiki/` — a minimal independent sub-wiki to compose,
- `scripts/compose-demo.sh` — credential-free composition smoke test.
- `repos.json` — example `workspace-cli` manifest for the umbrella and its sub-wikis.

## Adding a real sub-wiki

1. Add the repository to `repos.json` and clone it in the workspace.
2. Add a `sources:` entry in `docs/wiki.yml`.
3. Run `wiki -c docs/wiki.yml install` to pin its ref.
4. Run `wiki -c docs/wiki.yml update` when the sub-wiki publishes new content.

See [Named Graphs](docs/wiki/Named_Graphs.md) for the provenance model.