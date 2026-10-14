# Wiki Wikipedia Template

A semantic markdown knowledge base with a **Wikipedia-themed layout**, built with the [Wiki CLI](https://github.com/wazootech/wiki).

## Adding to an existing project

You don't need to start from scratch — add Wikipedia-themed wiki pages to any existing markdown project in a few steps.

### 1. Install the Wiki CLI

```bash
pip install wazootech-wiki==0.7.0
```

The theme build additionally needs the Deno 2 runtime (`deno --version`); see
<https://deno.com>.

### 2. Create a `wiki.yml` config

Place this at your project root:

```yaml
wiki:
  input:
    - wiki
  assets:
    - assets
  filename_pattern: "[A-Za-z0-9_()-]+\\.md"

graph:
  content_predicate: schema:articleBody
  context:
    "@vocab": https://schema.org/
    schema: https://schema.org/
    wiki: https://your-site.example/
    wazoo: https://schema.wazoo.dev/
    foaf: http://xmlns.com/foaf/0.1/
    sh: http://www.w3.org/ns/shacl#
    xsd: http://www.w3.org/2001/XMLSchema#

site:
  layout: layouts/wikipedia.html
  base_url: /wiki
  url_style: dir

link:
  style: standard

check:
  missing_layout_file: error
  frontmatter_schema: error
  missing_schema_ref: error

lint:
  broken_links: error
  filename_pattern: error
  link_style: error

fmt:
  textWrap: never
  newLineKind: lf
```

### 3. Copy the build files from this repo

```
cp -r layouts .
cp -r assets .
cp build.ts deno.json .
```

You need `build.ts`, `deno.json`, `layouts/wikipedia.html`, `assets/wikipedia.css`, `assets/wikipedia.js`, and `assets/logo.svg`.

### 4. Add semantic frontmatter to your markdown

In `wiki/Your_Page.md`:

```markdown
---
type: schema:Person
schema:givenName: Your
schema:familyName: Name
---

# Your Name

Your content here.
```

Properties in frontmatter render as a Wikipedia-style infobox. See `wiki/Ethan_Davidson.md` for a full example.

### 5. Build

```bash
deno run -A build.ts
```

Output goes to `_site/`. The built pages land under a folder matching your `site.base_url` (e.g. `_site/wiki/index.html` with the config above). Open it in a browser.

### 6. (Optional) Add CI checks

Copy `.github/workflows/ci.yml` from this repo to run `wiki fmt --check`, `wiki check --strict`, `wiki lint --strict`, and `wiki render --check` on every push.

## Layout

- `wiki.yml` — Wiki configuration, namespace prefixes, and `fmt` defaults.
- `wiki/` — Contains markdown files with semantic frontmatter.
- `assets/` — Static assets (CSS, JS, logo) for the Wikipedia theme.
- `layouts/` — Token-based layout template for the Wikipedia theme.
- `build.ts` — Deno build script rendering the theme via `@wazoo/wiki/theme`.
- `deno.json` — Import map and Deno settings for the build.
- `queries/` — Saved SPARQL queries for recurring questions.
- `.gitattributes` — Forces LF line endings so `wiki fmt` results are stable on every platform.

## Commands

- **Build** (Wikipedia theme):
  ```bash
  deno run -A build.ts
  ```
- **Preview** (build locally, then serve the output folder):
  ```bash
  deno run -A build.ts --output-dir _site
  python -m http.server -d _site
  ```
- **Check** (integrity: SHACL, JSON Schema, route safety):
  ```bash
  wiki -c wiki.yml check --strict
  ```
- **Lint** (conventions: broken links, filename pattern, heading style):
  ```bash
  wiki -c wiki.yml lint --strict
  ```
- **Format** (mechanical markdown layout):
  ```bash
  wiki -c wiki.yml fmt
  ```

`wiki serve` uses the Wiki CLI's built-in layout, which only knows the default token set — this theme's extra tokens (infobox, TOC, backlinks, categories, metadata) render via `deno run -A build.ts`. Use the build + static-server preview above for the full theme.

## Deployment

This wiki builds to a static site. Any provider that serves static files works.

### GitHub Pages (preferred)

1. Go to **Settings &rarr; Pages &rarr; Source: GitHub Actions**
2. Push to the default branch &mdash; the `.github/workflows/deploy.yml` workflow builds and deploys automatically
3. Your site appears at `https://{org}.github.io/{repo}/`

### Vercel

1. Import this repo at [vercel.com/new](https://vercel.com/new)
2. **Build command:** `deno run -A build.ts --output-dir .vercel/output`
3. **Output directory:** `.vercel/output`
4. Deploy

### Netlify

1. Import this repo at [app.netlify.com/start](https://app.netlify.com/start)
2. **Build command:** `deno run -A build.ts`
3. **Publish directory:** `_site`
4. Deploy

### Cloudflare Pages

1. Import this repo in the Cloudflare dashboard
2. **Build command:** `deno run -A build.ts`
3. **Output directory:** `_site`
4. Deploy

Every provider above runs the Deno build, so its build image needs the Deno 2
runtime. Make sure your `site.base_url` in `wiki.yml` matches where the site is
served from (`/` for a custom domain or root path).
