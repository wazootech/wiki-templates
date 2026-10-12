---
type: TechArticle
headline: Alpha Sub-wiki Home
description: Landing page of sample-subwiki, an independent corpus used to exercise composition.
---

# Alpha Sub-wiki Home

This is the corpus of an **independent sub-wiki**. It owns its own `wiki.yml`, pages, and review loop. An umbrella workspace can declare it as a git source in a `wiki.yml` `sources:` block; `wiki install` then loads its pages into a named graph reachable from union queries.

The compose demo seeds two copies of this corpus as separate git repositories and asserts that both surface in the composed umbrella graph.
