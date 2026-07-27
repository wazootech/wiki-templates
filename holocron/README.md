<div align='center'>
    <br/>
    <br/>
    <h3>holocron-template</h3>
    <p>Documentation site template powered by Holocron</p>
    <br/>
    <br/>
</div>

## Quick Start

```bash
bun install     # or: pnpm install / npm install
bun dev         # or: pnpm dev / npm run dev
```

Edit MDX pages in `src/`, configure navigation and theming in `docs.jsonc`.

## Deploy to Vercel

Push to `master` — deploys automatically via the `vercel.json` config.

### One-time setup

1. Push this repo to GitHub
2. Go to [vercel.com/new](https://vercel.com/new) and import the repo
3. Click **Deploy** (build will succeed, but AI chat won't work until step 4)
4. Add `HOLOCRON_KEY` to Vercel environment variables:
   - In the Vercel dashboard, go to your project → **Settings** → **Environment Variables**
   - Create a key `HOLOCRON_KEY` with the API key value from `holocron keys create`
   - Deploy the project again (the key is only needed for AI features, not page rendering)

### Manual (CLI)

```bash
npx vercel -e HOLOCRON_KEY=holo_xxx --prod
```

### Known issue

Spiceflow (Holocron's RSC framework) has a bug where its Vercel handler calls `AbortSignal.any([request.signal, ...])` but Vercel passes `request.signal = undefined`. The post-build script `scripts/patch-vercel-handler.mjs` patches the bundled output. If you upgrade `@holocron.so/vite` and see 500 errors, re-run the patch or check if the upstream fix is no longer needed.

## Project structure

| Path | Purpose |
|------|---------|
| `src/*.md` | MDX pages (shared with wiki CLI) |
| `docs.jsonc` | Holocron nav, colors, theme |
| `wiki.yml` | Wiki CLI config (standalone) |
| `vercel.json` | Vercel build config |
| `scripts/patch-vercel-handler.mjs` | Fixes Spiceflow/Vercel signal bug |
| `.github/workflows/` | CI deploy workflows |

# My Wiki

A semantic markdown knowledge base powered by the Wiki CLI.

## Wiki layout

- `wiki.yml` — Wiki configuration, namespace prefixes, and `fmt` defaults.
- `src/` — Contains markdown files with semantic frontmatter (shared with Holocron).
  - `Person_Shape.md` — SHACL shape for Person documents.
  - `Ethan_Davidson.md` — An example Person document.

## Commands

- **Check** (integrity: SHACL, JSON Schema, route safety, layout frontmatter):
  ```bash
  wiki check
  ```
- **Lint** (conventions: broken links, filename pattern, heading style):
  ```bash
  wiki lint
  ```
- **Preview** (starts a local dev server with auto-reload):
  ```bash
  wiki serve --watch
  ```
- **Build** (compiles to static HTML site):
  ```bash
  wiki build
  ```

---

## First-time setup

```bash
git clone <your-repo-url>
cd <repo>
bun install
```

Edit pages in `src/`, then push to `master` — Vercel auto-deploys.


## Deployment

### GitHub Pages (preferred)

Push to `master` — CI validates the wiki and deploys the Holocron site. Enable **Settings → Pages → Source: GitHub Actions** if not already active.

### Vercel

1. Import this repo at [vercel.com/new](https://vercel.com/new)
2. Vercel auto-detects `vercel.json` — default settings work
3. Add `HOLOCRON_KEY` environment variable for AI features (optional)
4. Deploy

### Netlify / Cloudflare Pages

- **Build command:** `npm ci && npm run build && node scripts/patch-vercel-handler.mjs` (omit the patch script if not on Vercel)
- **Publish directory:** `dist`
