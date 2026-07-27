# LLM Wiki template

Opinionated [LLM Wiki](https://github.com/wazootech/wiki/blob/main/docs/wiki/LLM_Wiki.md) starter — agent gardening, SHACL shapes, and SPARQL-backed indexes. Distinct from the generic [`wiki-template`](https://github.com/wazootech/wiki-template).

Registry: [Wiki CLI templates](https://github.com/wazootech/wiki/blob/main/docs/wiki/Wiki_CLI.md#ecosystem-templates).

## Quick start

```bash
pip install wazootech-wiki
wiki check --strict
wiki serve --watch
```

Read [wiki/LLM_Wiki_Guide.md](wiki/LLM_Wiki_Guide.md) for agent workflows (`check`, `lint`, `fmt`, `render`, `link`).

## Agent hygiene

- Run `wiki check --strict` before commit; `wiki lint --strict` for conventions.
- Run `wiki fmt` on edited markdown.
- Use `wiki render` to refresh embedded SPARQL tables.
- See [AGENTS.md](AGENTS.md) for coding-agent instructions.

## Layout

- `wiki.yaml` — `graph.content_predicate: schema:articleBody`, standard prefixes
- `wiki/Person_Shape.md`, `wiki/Concept_Shape.md` — SHACL shapes
- `wiki/LLM_Wiki_Guide.md` — gardening and agent DX
- `wiki/Ethan_Davidson.md` — example person page

## Deploy

Enable GitHub Pages (GitHub Actions). The [deploy-pages workflow](.github/workflows/deploy-pages.yml) runs `wiki build`.

## Related

- [Wiki CLI](https://github.com/wazootech/wiki)
- [LLM Wiki pattern](https://github.com/wazootech/wiki/blob/main/docs/wiki/LLM_Wiki.md)

## Deployment

This wiki builds to a static site. Any provider that serves static files works.

### GitHub Pages (preferred)

1. Go to **Settings &rarr; Pages &rarr; Source: GitHub Actions**
2. Push to the default branch &mdash; the \.github/workflows/deploy-pages.yml\ workflow builds and deploys automatically
3. Your site appears at \https://{org}.github.io/{repo}/\

### Vercel

1. Import this repo at [vercel.com/new](https://vercel.com/new)
2. **Build command:** \pip install wazootech-wiki && wiki build --output-dir .vercel/output --site-base-url /\
3. **Output directory:** \.vercel/output\
4. Deploy

### Netlify

1. Import this repo at [app.netlify.com/start](https://app.netlify.com/start)
2. **Build command:** \pip install wazootech-wiki && wiki build --output-dir _site --site-base-url /\
3. **Publish directory:** \_site\
4. Deploy

### Cloudflare Pages

1. Import this repo in the Cloudflare dashboard
2. **Build command:** \pip install wazootech-wiki && wiki build --output-dir _site --site-base-url /\
3. **Output directory:** \_site\
4. Deploy
