# Wiki Templates

Starter templates for [Wiki CLI](https://github.com/wazootech/wiki).

## Templates

| Template | Description | Stack |
|----------|-------------|-------|
| [wikipedia](templates/wikipedia/) | Wikipedia-themed static site builder on the Wiki CLI theme API | Deno, TypeScript |

## Quick start

```bash
# Clone the template
git clone https://github.com/wazootech/wiki-templates.git
cd wiki-templates/templates/wikipedia

# Or scaffold it into an existing vault
wiki init --template wikipedia

# Build the site
deno task build
```

`templates/wikipedia/README.md` covers installation, assets, and deployment.

## Keeping pins current

Every template pins the Wiki CLI it is built against: `wazootech-wiki==<version>`
in its workflows and prose, `jsr:@wazoo/wiki@<version>` in its `deno.json`.
`scripts/wiki-pins.py` is the single place that knows where those pins live:

```bash
python scripts/wiki-pins.py scan         # read-only report: pins, published versions, drift
python scripts/wiki-pins.py check        # exit 1 when a pin is behind the published latest
python scripts/wiki-pins.py sync         # rewrite the pins that are behind
python scripts/wiki-pins.py assert-diff  # fail unless the diff only changes version substrings
```

`.github/workflows/pin-bumps.yml` runs `sync` weekly, and on demand; `assert-diff`
proves the result changes nothing but version substrings; then the job opens or
updates a single `pin-bumps` PR and stops. It never pushes to `main`, and it
closes the PR when nothing is behind any more. The job needs a `PIN_BUMP_TOKEN`
secret — a fine-grained PAT or GitHub App token with `contents: write` and
`pull_requests: write` — because a PR opened with the default `GITHUB_TOKEN`
does not trigger CI on itself.

## Validation

Every template must pass the four wiki gates:

```bash
bash scripts/validate-all.sh
```

The script auto-discovers each template's config (`wiki.yml`, `docs/wiki.yml`,
`sample/wiki.yml`, or `sample-subwiki/wiki.yml`) and runs `fmt --check`,
`lint --strict`, `check --strict`, and `render --check`.
`templates/wikipedia/.github/workflows/ci.yml` mirrors those gates with a pinned
Wiki CLI.

## Why this is a separate repository

The template lives outside [`wazootech/wiki`](https://github.com/wazootech/wiki)
because it owns a publish surface — layout, assets, and build script — not the
engine. This repository's CI never runs the template's workflows; they are
payload for the scaffolded site.

`wiki init --template` shallow-clones this repository (`--depth 1`) to copy the
one subdirectory, which is a single network round-trip.

## Retired templates

This repository held twelve templates; eleven were retired on 2026-10-14
([#64](https://github.com/wazootech/wiki-templates/issues/64)): `astro`,
`camunda`, `cocoindex`, `generic`, `holocron`, `llm-wiki`, `mintlify`, `nextjs`,
`quartz`, `workspace-cli`, `yasgui`. Their history remains in this repository.
