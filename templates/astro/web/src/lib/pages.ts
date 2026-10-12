import wikiExport from "../../data/wiki-export.json";

export type WikiEntry = {
  name: string;
  slug: string;
};

export function listPages(): WikiEntry[] {
  const rows = Array.isArray(wikiExport) ? wikiExport : [wikiExport];
  return rows.map((row) => {
    const name = String(row.name);
    return { name, slug: name.replace(/\.md$/i, "") };
  });
}

export function findRdf(slug: string) {
  const rows = Array.isArray(wikiExport) ? wikiExport : [wikiExport];
  const row = rows.find((entry) => String(entry.name).replace(/\.md$/i, "") === slug);
  return row?.rdf ?? {};
}
