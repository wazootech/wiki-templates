<!-- template-payload: ships with this template; scaffolds into generated docs sites -->

This file is **template payload**: inside `wazootech/wiki-templates` it marks
shipped content; in every site scaffolded from this template it serves as live
agent instructions. First-party agents editing the template itself should load
the governing skill or reference before changing template internals.

# Agent guidelines

## What this repo is

This repository is a Next.js wiki template. It reads `.md` files from a
`wiki/` vault directory and renders them as a static site using Next.js App
Router, MDX, and `getStaticProps`-style static generation via
`generateStaticParams`.

## How to work here

- Preserve template clarity: avoid project-specific assumptions unless the user
  asks to specialize the template.
- Keep setup instructions explicit for future users.
- The `wiki/` directory is the example vault. The `web/` directory is the
  Next.js application that consumes it.
- Before finishing, check for unintentional generated files or template-local
  secrets.
