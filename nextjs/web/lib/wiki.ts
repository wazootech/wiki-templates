import fs from "node:fs";
import path from "node:path";
import { extract } from "@wazoo/linked-markdown";

const WIKI_DIR = path.resolve(process.cwd(), "../wiki");

export interface WikiPage {
  slug: string;
  filename: string;
  frontmatter: Record<string, unknown>;
  content: string;
}

function readMarkdownFiles(): string[] {
  if (!fs.existsSync(WIKI_DIR)) return [];
  return fs
    .readdirSync(WIKI_DIR)
    .filter((file) => file.endsWith(".md"))
    .sort();
}

export function listPages(): Omit<WikiPage, "content">[] {
  return readMarkdownFiles().map((file) => {
    const raw = fs.readFileSync(path.join(WIKI_DIR, file), "utf-8");
    const { attrs } = extract<Record<string, unknown>>(raw);
    const slug = file.replace(/\.md$/i, "");
    return { slug, filename: file, frontmatter: attrs };
  });
}

export function getPage(slug: string): WikiPage | null {
  const filePath = path.join(WIKI_DIR, `${slug}.md`);
  if (!fs.existsSync(filePath)) return null;
  const raw = fs.readFileSync(filePath, "utf-8");
  const { attrs, body } = extract<Record<string, unknown>>(raw);
  return { slug, filename: `${slug}.md`, frontmatter: attrs, content: body };
}
