# Wiki Wikipedia Template

A semantic markdown knowledge base with a **Wikipedia-themed layout**, built with the [Wiki CLI](https://github.com/wazootech/wiki).

## Adding to an existing project

You don't need to start from scratch — add Wikipedia-themed wiki pages to any existing markdown project in a few steps.

### 1. Install the Wiki CLI

```bash
pip install wazootech-wiki
```

### 2. Create a `wiki.yml` config

Place this at your project root:

```yaml
wiki:
  inputs:
    - wiki
  assets:
    - assets
  filename_pattern: "[A-Za-z0-9_()-]+\\.md"

graph:
  context:
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
```

### 3. Copy the build files from this repo

```
cp -r layouts layouts
cp -r assets assets
cp build.py build.py
```

Or copy them manually — you need `build.py`, `layouts/wikipedia.html`, `assets/wikipedia.css`, `assets/wikipedia.js`, and `assets/logo.svg`.

### 4. Add semantic frontmatter to your markdown

In `wiki/Your_Page.md`:

```markdown
---
type: schema:Person
givenName: Your
familyName: Name
---

# Your Name

Your content here.
```

Properties in frontmatter render as a Wikipedia-style infobox. See `wiki/Ethan_Davidson.md` for a full example.

### 5. Build

```bash
python build.py
```

Output goes to `_site/`. Open `_site/wiki/index.html` in a browser.

### 6. (Optional) Add CI checks

Copy `.github/workflows/ci.yml` from this repo to run `wiki check` and `wiki lint` on every push.

## Layout

- `wiki.yml` — Wiki configuration, namespace prefixes, and `fmt` defaults.
- `wiki/` — Contains markdown files with semantic frontmatter.
- `assets/` — Static assets (CSS, JS, logo) for the Wikipedia theme.
- `layouts/` — Token-based layout template for the Wikipedia theme.
- `build.py` — Build script using the Wiki Python library.

## Commands

- **Build** (Wikipedia theme):
  ```bash
  python build.py
  ```
- **Preview** (starts a local dev server):
  ```bash
  wiki serve
  ```
- **Check** (integrity: SHACL, JSON Schema, route safety):
  ```bash
  wiki check
  ```
- **Lint** (conventions: broken links, filename pattern, heading style):
  ```bash
  wiki lint
  ```

The Wikipedia-themed build output goes to `_site/`.

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
