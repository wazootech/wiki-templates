# Agent guidelines

## Code health

Family-wide rules live in the [wazootech workspace constitution](https://github.com/wazootech/workspace/blob/main/AGENTS.md#code-health-standards); this repo's specifics:

- **Before pushing**, run what CI runs: `bash scripts/validate-all.sh` (needs the pinned `wazootech-wiki` CLI); `bun install --frozen-lockfile` then `bun run ci` (format, lint, type check, and the pin match between `package.json` and each template's `package.json`); and from `templates/wikipedia/`: `bun install` then `bun build.ts --output-dir <tmp>`.
- The template builds on Bun with the engine pinned in its `package.json`. The `template-build` CI job proves that build still works. It runs without a frozen lockfile because the template ships no `bun.lock` (a scaffolded site writes its own, and adding one would alter the payload). Do not commit a generated one.
- `package.json` (repo root, not payload) pins `@wazoo/wiki` and `prismjs` so `bun check` can type check `build.ts`. `scripts/check-template-deps.ts` fails CI when those pins drift from the template's `package.json`, and `scripts/wiki-pins.py` bumps the `@wazoo/wiki` pin with the others.
- `.prettierignore` keeps `bun fmt` to the TypeScript and JSON this repo owns; Markdown, layouts and assets are never reformatted by it.
- `templates/*/` files, including their `AGENTS.md`, are payloads that must carry their `template-payload` header; code-health tooling checks them but never edits them, and they are excluded from LOC/TODO checks.
- CI gates run on Bun (`oven-sh/setup-bun`, `bun-version: "1.x"`, the one toolchain allowed to float). Third-party actions in this repo's own workflows are pinned to full commit SHAs with a version comment.
- `secret-scan.yml` (gitleaks) runs on every PR and push to main. There is no `code-health.yml` because all TS/JS here is payload.
- `.github/CODEOWNERS` assigns review.
