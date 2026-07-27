import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = join(fileURLToPath(import.meta.url), '..', '..', 'dist', 'rsc', 'assets');
const files = readdirSync(dir).filter(f => f.startsWith('holocron-stable-') && f.endsWith('.js'));
let patched = false;

for (const file of files) {
  const fp = join(dir, file);
  const content = readFileSync(fp, 'utf-8');
  const original = `AbortSignal.any([request.signal, abort.signal])`;
  const replacement = `AbortSignal.any([request.signal, abort.signal].filter(Boolean))`;
  if (content.includes(original)) {
    writeFileSync(fp, content.replaceAll(original, replacement));
    patched = true;
    console.log(`✓ Patched ${file}`);
  }
}

if (!patched) {
  console.error('✗ Pattern not found — nothing patched');
  process.exit(1);
}
