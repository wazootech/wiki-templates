# wiki-nextjs-template

Next.js 16 App Router static site that reads `.md` files from a wiki vault
and renders them as MDX pages.

Registry: [Wiki CLI templates](https://github.com/wazootech/wiki/blob/main/docs/wiki/Wiki_CLI.md#ecosystem-templates).

## Quick start

```bash
pip install wazootech-wiki
bash scripts/check-wiki.sh
cd web && npm install && npm run build
```

Open `web/out/` after `next build`.

## Layout

| Path | Role |
| ---- | ---- |
| `wiki/` | Example vault |
| `wiki.yml` | Wiki CLI config |
| `scripts/check-wiki.sh` | `wiki check` + `wiki lint` |
| `web/` | Next.js 16 App Router SSG app |

## How it works

- `web/lib/wiki.ts` reads `.md` files from `../wiki/` at build time using
  Node.js `fs` and `gray-matter` for frontmatter parsing.
- `web/app/[slug]/page.tsx` uses `generateStaticParams` to statically generate
  one route per vault page, compiling MDX content with `@mdx-js/mdx`.
- `@next/mdx` is configured as the idiomatic MDX plugin in `next.config.ts`.
- `output: "export"` produces a fully static site in `web/out/`.

## Deploy

Deploy `web/out/` to Netlify, Cloudflare Pages, or GitHub Pages. Re-run
`scripts/check-wiki.sh` when the vault changes.

## Related

- [wiki-astro-template](https://github.com/wazootech/wiki-astro-template)
- [Wiki CLI](https://github.com/wazootech/wiki)

## Deployment

### GitHub Pages (preferred)

1. Go to **Settings -> Pages -> Source: GitHub Actions**
2. Push to the default branch — the `.github/workflows/deploy-pages.yml`
   workflow builds the SSG site and deploys automatically
3. Your site appears at `https://{org}.github.io/{repo}/`

### Vercel

1. Import this repo at [vercel.com/new](https://vercel.com/new)
2. Vercel auto-detects the framework — default settings should work
3. Deploy

### Netlify

1. Import this repo at [app.netlify.com/start](https://app.netlify.com/start)
2. **Build command:** `pip install wazootech-wiki && bash scripts/check-wiki.sh && cd web && npm ci && npm run build`
3. **Publish directory:** `web/out`
4. Deploy

### Cloudflare Pages

1. Import this repo in the Cloudflare dashboard
2. **Build command:** `pip install wazootech-wiki && bash scripts/check-wiki.sh && cd web && npm ci && npm run build`
3. **Output directory:** `web/out`
4. Deploy
