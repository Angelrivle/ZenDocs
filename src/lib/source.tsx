import React from "react";
import { docs } from "collections/server";
import { loader } from "fumadocs-core/source";
import { lucideIconsPlugin } from "fumadocs-core/source/lucide-icons";
import { docsContentRoute, docsImageRoute, docsRoute } from "./shared";

// See https://fumadocs.dev/docs/headless/source-api for more info
export const source = loader({
  baseUrl: docsRoute,
  source: docs.toFumadocsSource(),
  plugins: [lucideIconsPlugin()],
});

import { getSidebarIcon } from "@/components/SidebarIconMap";

// Recursive function to post-process the page tree and inject icons and badges
function injectIconsAndBadges(nodes: any[]) {
  for (const node of nodes) {
    if (node.type === "folder") {
      const folderKey = node.$id || node.name || "";
      if (!node.icon) {
        node.icon = getSidebarIcon(folderKey, true);
      }
      if (typeof node.name === "string") {
        if (node.name.includes("(Soon)")) {
          const cleanName = node.name.replace("(Soon)", "").trim();
          node.name = (
            <span className="flex items-center justify-between w-full pr-1.5 gap-2">
              <span>{cleanName}</span>
              <span className="inline-flex items-center text-[10px] font-bold px-1.5 py-0.5 rounded border border-blue-500/40 bg-blue-500/10 text-cyan-400 leading-none tracking-wide select-none">
                Soon
              </span>
            </span>
          );
        } else if (node.name.includes("(New)")) {
          const cleanName = node.name.replace("(New)", "").trim();
          node.name = (
            <span className="flex items-center justify-between w-full pr-1.5 gap-2">
              <span>{cleanName}</span>
              <span className="inline-flex items-center text-[10px] font-medium px-1.5 py-0.5 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-400 leading-none select-none">
                New
              </span>
            </span>
          );
        }
      }
      if (node.children) {
        injectIconsAndBadges(node.children);
      }
    } else if (node.type === "page") {
      const pageSlug = node.url ? node.url.split("/").pop() || "" : "";
      if (!node.icon) {
        node.icon = getSidebarIcon(pageSlug, false);
      }
      if (typeof node.name === "string") {
        if (node.name.includes("(Soon)")) {
          const cleanName = node.name.replace("(Soon)", "").trim();
          node.name = (
            <span className="flex items-center justify-between w-full pr-1.5 gap-2">
              <span>{cleanName}</span>
              <span className="inline-flex items-center text-[10px] font-bold px-1.5 py-0.5 rounded border border-blue-500/40 bg-blue-500/10 text-cyan-400 leading-none tracking-wide select-none">
                Soon
              </span>
            </span>
          );
        } else if (node.name.includes("(New)")) {
          const cleanName = node.name.replace("(New)", "").trim();
          node.name = (
            <span className="flex items-center justify-between w-full pr-1.5 gap-2">
              <span>{cleanName}</span>
              <span className="inline-flex items-center text-[10px] font-medium px-1.5 py-0.5 rounded border border-emerald-500/30 bg-emerald-500/10 text-emerald-400 leading-none select-none">
                New
              </span>
            </span>
          );
        }
      }
    }
  }
}

// Perform post-processing immediately on loader tree children
if (source.pageTree && source.pageTree.children) {
  injectIconsAndBadges(source.pageTree.children);
}

export function getPageImage(page: (typeof source)["$inferPage"]) {
  const segments = [...page.slugs, "image.png"];

  return {
    segments,
    url: `${docsImageRoute}/${segments.join("/")}`,
  };
}

export function getPageMarkdownUrl(page: (typeof source)["$inferPage"]) {
  const segments = [...page.slugs, "content.md"];

  return {
    segments,
    url: `${docsContentRoute}/${segments.join("/")}`,
  };
}

export async function getLLMText(page: (typeof source)["$inferPage"]) {
  const processed = await page.data.getText("processed");

  return `# ${page.data.title} (${page.url})

${processed}`;
}
