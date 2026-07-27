# wiki-astro-template

Astro static site that consumes **`wiki export`** JSON-LD and pre-renders one route per vault page.

Registry: [Wiki CLI templates](https://github.com/wazootech/wiki/blob/main/docs/wiki/Wiki_CLI.md#ecosystem-templates).

## Quick start

```bash
pip install wazootech-wiki
bash scripts/export-wiki-data.sh
cd web && npm install && npm run build
```

Open `web/dist/` after `astro build`.

## Layout

| Path | Role |
| ---- | ---- |
| `wiki/` | Example vault |
| `wiki.yaml` | Wiki CLI config |
| `scripts/export-wiki-data.sh` | `wiki check` + `wiki export` → `web/data/wiki-export.json` |
| `web/` | Astro SSG app |

## Deploy

Deploy `web/dist/` to Netlify, Cloudflare Pages, or GitHub Pages. Re-run `scripts/export-wiki-data.sh` when the vault changes.

## Related

- [#96](https://github.com/wazootech/wiki/issues/96)
- [Wiki Subcommand export](https://github.com/wazootech/wiki/blob/main/docs/wiki/Wiki_Subcommand_export.md)

## Deployment

### GitHub Pages (preferred)

1. Go to **Settings &rarr; Pages &rarr; Source: GitHub Actions**
2. Push to the default branch &mdash; the \.github/workflows/deploy-pages.yml\ workflow builds the SSG site and deploys automatically
3. Your site appears at \https://{org}.github.io/{repo}/\

### Vercel

1. Import this repo at [vercel.com/new](https://vercel.com/new)
2. Vercel auto-detects the framework &mdash; default settings should work
3. Deploy

### Netlify

1. Import this repo at [app.netlify.com/start](https://app.netlify.com/start)
2. **Build command:** \pip install wazootech-wiki && bash scripts/export-wiki-data.sh && cd web && npm ci && npm run build\
3. **Publish directory:** \web/dist\ (Astro) or \web/out\ (Next.js)
4. Deploy

### Cloudflare Pages

1. Import this repo in the Cloudflare dashboard
2. **Build command:** \pip install wazootech-wiki && bash scripts/export-wiki-data.sh && cd web && npm ci && npm run build\
3. **Output directory:** \web/dist\ (Astro) or \web/out\ (Next.js)
4. Deploy
