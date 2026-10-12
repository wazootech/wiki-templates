<!-- template-payload: ships with this template; scaffolds into generated docs sites -->

This file is **template payload**: inside `wazootech/wiki-templates` it marks
shipped content; in every site scaffolded from this template it serves as live
agent instructions. First-party agents editing the template itself should load
the governing skill or reference before changing template internals.

# AGENTS.md — Workspace CLI Composed Workspace

Guidance for agents working in this composed workspace template.

## Scope

This is a **composition** template, not a monorepo. It demonstrates how an umbrella Wiki corpus
composes independently-owned sub-wiki repositories as source graphs.

## Repositories in scope

- `sample-subwiki/` — the canonical example of an independent sub-wiki. Treat it as owned by its own
  team; umbrella edits must not change its content.
- Umbrella corpus under `docs/` — platform/workspace team owned; cross-cutting schemas live here.

## Navigation rules

- Commit in the repo that owns the change. A sub-wiki content fix belongs in the sub-wiki repo, not
  here.
- Cross-team schema changes belong in the umbrella `docs/shapes/` / `docs/schemas/` and get reviewed
  here.
- Before composing, read `docs/wiki/Composed_Workspace.md` and `docs/wiki/Named_Graphs.md`.

## Verification

Run from this template directory:

```sh
wiki -c docs/wiki.yml fmt --check
wiki -c docs/wiki.yml lint --strict -v
wiki -c docs/wiki.yml check --strict -v
wiki -c docs/wiki.yml render --check -v
bash scripts/compose-demo.sh      # composition smoke test (sources + gates)
```

The monorepo validates `docs/wiki.yml`, so keep the umbrella config self-contained: it must pass the
four gates without any declared source installed. Uninstall sources before committing config changes.

## Secrets

Do not commit API keys or `.env` files. The compose demo is intentionally credential-free and must
stay that way.