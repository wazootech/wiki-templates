import fs from "node:fs";
import path from "node:path";

const dataPath = path.join(process.cwd(), "data", "wiki-export.json");
if (!fs.existsSync(dataPath)) {
  console.error("Missing web/data/wiki-export.json — run scripts/export-wiki-data.sh");
  process.exit(1);
}
