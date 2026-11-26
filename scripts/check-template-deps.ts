/**
 * Keeps the root package.json (what Bun installs for fmt, lint and type check)
 * in lockstep with each template's deno.json (what a scaffolded site builds
 * with): every `jsr:` or `npm:` import in a template's deno.json must be a
 * package.json dependency or devDependency at the same version, with each
 * `jsr:` import spelled as `npm:@jsr/<scope>__<name>@<version>`. Subpath import
 * keys such as `@wazoo/wiki/theme` are covered by their package entry.
 *
 * Usage: `bun scripts/check-template-deps.ts [repoDir]`.
 */
import { readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import process from "node:process";

type Manifest = {
  imports?: Record<string, string>;
  devDependencies?: Record<string, string>;
};

const root = resolve(process.argv[2] ?? ".");
const readJson = (path: string): Manifest =>
  JSON.parse(readFileSync(path, "utf8")) as Manifest;
const declared = readJson(join(root, "package.json")).devDependencies ?? {};

function expected(spec: string): string {
  const jsr = /^jsr:@([^/]+)\/([^@/]+)@([^/]+)(?:\/.*)?$/.exec(spec);
  if (jsr) return `npm:@jsr/${jsr[1]}__${jsr[2]}@${jsr[3]}`;
  return /^npm:[^@]+@(.+)$/.exec(spec)?.[1] ?? spec;
}

const problems: string[] = [];
for (const template of readdirSync(join(root, "templates"))) {
  const path = join(root, "templates", template, "deno.json");
  let imports: Record<string, string>;
  try {
    imports = readJson(path).imports ?? {};
  } catch {
    continue;
  }
  for (const [alias, spec] of Object.entries(imports)) {
    // Subpath keys (`@wazoo/wiki/theme`) ride on their package's entry.
    if (alias.includes("/") && !alias.startsWith("@")) continue;
    if (alias.startsWith("@") && alias.split("/").length > 2) continue;
    const want = expected(spec);
    if (declared[alias] === undefined) {
      problems.push(`${template}: "${alias}" is not in package.json`);
    } else if (declared[alias] !== want) {
      problems.push(
        `${template}: "${alias}" is ${spec} in deno.json but ${declared[alias]} in package.json`,
      );
    }
  }
}

if (problems.length > 0) {
  console.error(problems.join("\n"));
  process.exit(1);
}
console.log("template imports match package.json");
