# Agent guidelines

## Code health

Family-wide rules live in the [wazootech workspace constitution](https://github.com/wazootech/workspace/blob/main/AGENTS.md#code-health-standards); this repo's specifics:

- **Before pushing**, run what CI runs: `bash scripts/validate-all.sh` (needs the pinned `wazootech-wiki` CLI), then from `templates/wikipedia/`: `deno fmt --check`, `deno lint`, `deno check build.ts`.
- The template Deno job runs without a frozen lockfile because the template ships no `deno.lock` (a scaffolded site generates its own, and adding one would alter the payload). Do not commit a generated one.
- `templates/*/` files, including their `AGENTS.md`, are payloads that must carry their `template-payload` header; code-health tooling checks them but never edits them, and they are excluded from LOC/TODO checks.
- CI uses Deno `v2.9.8`; third-party actions in this repo's own workflows are pinned to full commit SHAs with a version comment.
- `secret-scan.yml` (gitleaks) runs on every PR and push to main. There is no `code-health.yml` because all TS/JS here is payload.
- `.github/CODEOWNERS` assigns review.
