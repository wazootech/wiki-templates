import { readFileSync, existsSync, cpSync, mkdirSync, writeFileSync } from 'node:fs';
import { spawn } from 'node:child_process';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');

const PORT = process.env.PORT || '4173';
const BASE = (process.env.BASE || '').replace(/\/+$/, '');
const OUT_DIR = join(root, 'out');
const CLIENT_DIR = join(root, 'dist', 'client');
const RSC_SERVER = join(root, 'dist', 'rsc', 'index.js');

// Read docs.jsonc to find known page slugs
const configRaw = readFileSync(join(root, 'docs.jsonc'), 'utf-8');
const config = JSON.parse(configRaw);
const slugs = [];

function extractPages(nav) {
  if (!nav) return;
  if (Array.isArray(nav.tabs)) {
    for (const tab of nav.tabs) {
      if (tab.pages) {
        for (const page of tab.pages) {
          if (typeof page === 'string') slugs.push(page);
          else if (page.pages) extractPages({ tabs: [{ pages: page.pages }] });
        }
      }
      if (tab.groups) {
        for (const group of tab.groups) {
          if (group.pages) {
            for (const page of group.pages) {
              if (typeof page === 'string') slugs.push(page);
            }
          }
        }
      }
    }
  }
  if (nav.groups) extractPages({ tabs: [{ groups: nav.groups }] });
}

extractPages(config.navigation);
console.log(`Found pages: ${slugs.join(', ') || '(none besides root)'}`);

const prefix = BASE || '';

async function fetchPage(path) {
  const url = `${prefix}${path}`;
  try {
    const res = await fetch(`http://localhost:${PORT}${url}`, {
      headers: { 'Accept': 'text/html,application/xhtml+xml' },
      redirect: 'follow',
    });
    if (res.ok) {
      return { html: await res.text(), status: res.status, url };
    }
    return { html: null, status: res.status, url };
  } catch (err) {
    return { html: null, status: 0, url, error: err.message };
  }
}

// Start the RSC production server
console.log(`Starting server on port ${PORT}...`);
const server = spawn('node', [RSC_SERVER], {
  env: { ...process.env, PORT },
  stdio: ['ignore', 'pipe', 'pipe'],
  cwd: root,
});

let started = false;

server.stdout.on('data', (data) => {
  const text = data.toString();
  for (const line of text.split('\n').filter(Boolean)) {
    console.log('[server]', line.trim());
    if (line.includes('Listening')) started = true;
  }
});

server.stderr.on('data', (data) => {
  const text = data.toString();
  for (const line of text.split('\n').filter(Boolean)) {
    console.log('[server:err]', line.trim());
    if (line.includes('Listening')) started = true;
  }
});

let attempts = 0;
while (!started && attempts < 60) {
  await new Promise((r) => setTimeout(r, 1000));
  attempts++;
  try {
    const res = await fetch(`http://localhost:${PORT}${prefix}/`);
    if (res.ok || res.status === 404) started = true;
  } catch {}
}
if (!started) {
  console.error('Server failed to start');
  server.kill();
  process.exit(1);
}

console.log('Server ready. Crawling pages...');

mkdirSync(OUT_DIR, { recursive: true });

const paths = ['/', ...slugs.map((s) => `/${s}`)];
const results = [];

for (const path of paths) {
  const result = await fetchPage(path);
  results.push({ path, ...result });
  if (result.html) {
    console.log(`✓ ${result.url} (${result.status})`);
  } else if (result.error) {
    console.log(`✗ ${result.url} → ${result.error}`);
  } else {
    console.log(`  ${result.url} → ${result.status} (will use root HTML as fallback)`);
  }
}

const rootResult = results.find((r) => r.path === '/');
const rootHtml = rootResult?.html;
if (!rootHtml) {
  console.error('Failed to fetch root page');
  server.kill();
  process.exit(1);
}

for (const { path, html, status } of results) {
  const content = html || rootHtml;
  if (!html) {
    console.log(`  ${path} using root HTML as SPA fallback`);
  }

  if (path === '/') {
    writeFileSync(join(OUT_DIR, 'index.html'), content);
  } else {
    const slug = path.replace(/^\//, '');
    const dir = join(OUT_DIR, slug);
    mkdirSync(dir, { recursive: true });
    writeFileSync(join(dir, 'index.html'), content);
  }
}

if (existsSync(CLIENT_DIR)) {
  cpSync(CLIENT_DIR, OUT_DIR, { recursive: true, force: true });
  console.log(`✓ Copied client assets`);
} else {
  console.warn(`⚠ dist/client not found at ${CLIENT_DIR}`);
}

writeFileSync(join(OUT_DIR, '404.html'), rootHtml);
console.log('✓ Created 404.html for SPA fallback');

server.kill('SIGTERM');
console.log('Export complete.');
