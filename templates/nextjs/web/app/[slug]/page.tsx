import { notFound } from "next/navigation";
import Link from "next/link";
import { evaluate } from "@mdx-js/mdx";
import * as runtime from "react/jsx-runtime";
import React from "react";
import type { Metadata } from "next";
import { getPage, listPages } from "@/lib/wiki";

export function generateStaticParams() {
  return listPages().map((page) => ({ slug: page.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const page = getPage(slug);
  if (!page) return {};
  return {
    title: String(page.frontmatter.headline ?? page.frontmatter.name ?? slug),
    description: String(page.frontmatter.description ?? ""),
  };
}

export default async function WikiPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const page = getPage(slug);
  if (!page) notFound();

  const { default: MDXContent } = await evaluate(page.content, {
    ...runtime,
    remarkRehypeOptions: {},
  });

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <article className="flex min-h-screen w-full max-w-3xl flex-col py-32 px-16 bg-white dark:bg-black">
        <p className="mb-4 text-sm text-zinc-500 dark:text-zinc-400">
          <Link href="/" className="hover:underline">
            &larr; Index
          </Link>
        </p>
        <h1 className="max-w-xs text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50">
          {String(
            page.frontmatter.headline ?? page.frontmatter.name ?? slug
          ).replace(/_/g, " ")}
        </h1>
        <p className="mb-8 text-sm text-zinc-500 dark:text-zinc-400">
          Source: <code className="font-mono">{page.filename}</code>
        </p>
        <div className="prose prose-zinc dark:prose-invert max-w-none">
          <MDXContent />
        </div>
      </article>
    </div>
  );
}
