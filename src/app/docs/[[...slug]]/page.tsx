import { getPageImage, getPageMarkdownUrl, source } from "@/lib/source";
import {
  DocsBody,
  DocsDescription,
  DocsPage,
  DocsTitle,
} from "fumadocs-ui/layouts/docs/page";
import { notFound } from "next/navigation";
import { getMDXComponents } from "@/components/mdx";
import type { Metadata } from "next";
import { createRelativeLink } from "fumadocs-ui/mdx";
import { gitConfig } from "@/lib/shared";
import { FeedbackWidget } from "@/components/FeedbackWidget";
import { MarkdownCopyButton } from "@/components/MarkdownCopyButton";
import { SidebarSupportCard } from "@/components/SidebarSupportCard";

export default async function Page(props: PageProps<"/docs/[[...slug]]">) {
  const params = await props.params;
  const slug = params.slug ?? [];
  const page = source.getPage(slug);
  if (!page) notFound();

  const pageData = page.data as any;
  const MDX = pageData.body;
  const markdownUrl = getPageMarkdownUrl(page).url;
  const currentSlug = slug.join("/");


  return (
    <DocsPage
      toc={pageData.toc}
      full={pageData.full}
      tableOfContent={{
        footer: (
          <div className="pt-4">
            <SidebarSupportCard />
          </div>
        ),
      }}
    >
      <DocsTitle>{pageData.title}</DocsTitle>
      <DocsDescription className="mb-0">{pageData.description}</DocsDescription>
      <div className="flex flex-row gap-2 items-center border-b pb-6">
        <MarkdownCopyButton markdownUrl={markdownUrl} />
      </div>
      <DocsBody>
        <MDX
          components={getMDXComponents({
            // this allows you to link to other pages with relative file paths
            a: createRelativeLink(source, page),
          })}
        />
      </DocsBody>
      <FeedbackWidget slug={currentSlug} title={pageData.title} />
    </DocsPage>
  );
}

export async function generateStaticParams() {
  return source.generateParams();
}

export async function generateMetadata(
  props: PageProps<"/docs/[[...slug]]">,
): Promise<Metadata> {
  const params = await props.params;
  const page = source.getPage(params.slug ?? []);
  if (!page) notFound();

  const pageData = page.data as any;
  return {
    title: pageData.title,
    description: pageData.description,
    openGraph: {
      images: getPageImage(page).url,
    },
  };
}
