# Agent guidelines

## Code health

Family-wide rules live in the [wazootech workspace constitution](https://github.com/wazootech/workspace/blob/main/AGENTS.md#code-health-standards); this repo's specifics:

- **Before pushing**, run what CI runs: `bash scripts/validate-all.sh` (needs the pinned `wazootech-wiki` CLI); `bun install --frozen-lockfile` then `bun run ci` (format, lint, type check, and the pin match between `package.json` and each template's `deno.json`); and from `templates/wikipedia/`: `deno run -A build.ts --output-dir <tmp>`.
- **Deliberate Deno leftover:** the template still builds on Deno, because `@wazoo/wiki` 0.7.0 calls `Deno.*` internally (`Config.load` reads `Deno.cwd()`), so the shipped `deno.json`, `build.ts` run command and the template's own workflows stay on Deno until the engine runs on Bun (tracked in wazootech/workspace#50; the wiki repo is cut over last). `build.ts` itself uses only `node:` APIs. The `template-build` CI job exists to prove that build still works.
- The `template-build` job runs without a frozen lockfile because the template ships no `deno.lock` (a scaffolded site generates its own, and adding one would alter the payload). Do not commit a generated one.
- `package.json` (repo root, not payload) pins `@wazoo/wiki` and `prismjs` so `bun check` can type check `build.ts`. `scripts/check-template-deps.ts` fails CI when those pins drift from the template's `deno.json`, and `scripts/wiki-pins.py` bumps the `@wazoo/wiki` pin with the others.
- `.prettierignore` keeps `bun fmt` to the TypeScript and JSON this repo owns (as `deno fmt` did); Markdown, layouts and assets are never reformatted by it.
- `templates/*/` files, including their `AGENTS.md`, are payloads that must carry their `template-payload` header; code-health tooling checks them but never edits them, and they are excluded from LOC/TODO checks.
- CI gates run on Bun (`oven-sh/setup-bun`, `bun-version: "1.x"`, the one toolchain allowed to float); the `template-build` job uses Deno `v2.9.8`. Third-party actions in this repo's own workflows are pinned to full commit SHAs with a version comment.
- `secret-scan.yml` (gitleaks) runs on every PR and push to main. There is no `code-health.yml` because all TS/JS here is payload.
- `.github/CODEOWNERS` assigns review.
