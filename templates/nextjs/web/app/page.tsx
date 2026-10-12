import { listPages } from "@/lib/wiki";

export default function Home() {
  const pages = listPages();

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <h1 className="max-w-xs text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50">
          Wiki Next.js viewer
        </h1>
        <p className="max-w-md text-lg leading-8 text-zinc-600 dark:text-zinc-400">
          Static routes generated from a{" "}
          <code className="font-mono text-sm">wiki</code> vault using MDX.
        </p>
        {pages.length === 0 ? (
          <p className="text-zinc-500 dark:text-zinc-400">
            No wiki pages found. Add <code className="font-mono text-sm">.md</code> files
            to the <code className="font-mono text-sm">wiki/</code> directory.
          </p>
        ) : (
          <ul className="mt-8 space-y-2">
            {pages.map((page) => (
              <li key={page.slug}>
                <a
                  href={`/${page.slug}`}
                  className="text-lg font-medium text-blue-600 hover:underline dark:text-blue-400"
                >
                  {page.slug.replace(/_/g, " ")}
                </a>
                {typeof page.frontmatter.description === "string" && (
                  <p className="text-sm text-zinc-500 dark:text-zinc-400">
                    {page.frontmatter.description}
                  </p>
                )}
              </li>
            ))}
          </ul>
        )}
      </main>
    </div>
  );
}
