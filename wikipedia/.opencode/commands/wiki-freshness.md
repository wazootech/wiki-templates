---
description: Check which wiki pages are stale or need updating
---
Scan all wiki/ pages and identify:
- Pages older than 30 days that likely need freshness checks
- Pages with incomplete frontmatter
- Pages referencing repos or services that may have changed
- Orphaned pages not linked from any index
Use `git log --format="%ai" -- wiki/` to check last-modified dates.
Report findings with specific page names and recommended actions.
