/**
 * Keeps the root package.json (what Bun installs for fmt, lint and type check)
 * in lockstep with each template's package.json (what a scaffolded site builds
 * with): every template dependency must be a root dependency or devDependency
 * at the same version.
 *
 * Usage: `bun scripts/check-template-deps.ts [repoDir]`.
 */
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import process from "node:process";

type Manifest = {
  dependencies?: Record<string, string>;
  devDependencies?: Record<string, string>;
};

const root = resolve(process.argv[2] ?? ".");
const dependencies = (path: string): Record<string, string> => {
  const manifest = JSON.parse(readFileSync(path, "utf8")) as Manifest;
  return { ...manifest.dependencies, ...manifest.devDependencies };
};
const declared = dependencies(join(root, "package.json"));

const problems: string[] = [];
for (const template of readdirSync(join(root, "templates"))) {
  const path = join(root, "templates", template, "package.json");
  if (!existsSync(path)) continue;
  for (const [name, wanted] of Object.entries(dependencies(path))) {
    if (declared[name] === undefined) {
      problems.push(`${template}: "${name}" is not in the root package.json`);
    } else if (declared[name] !== wanted) {
      problems.push(
        `${template}: "${name}" is ${wanted} in the template but ${declared[name]} at the root`,
      );
    }
  }
}

if (problems.length > 0) {
  console.error(problems.join("\n"));
  process.exit(1);
}
console.log("template dependencies match the root package.json");
