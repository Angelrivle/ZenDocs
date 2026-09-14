"use client";

import { useState } from "react";
import { Check, Copy } from "lucide-react";
import { buttonVariants } from "fumadocs-ui/components/ui/button";
import { useCopyButton } from "fumadocs-ui/utils/use-copy-button";

type MarkdownCopyButtonProps = {
  markdownUrl: string;
  className?: string;
  children?: React.ReactNode;
};

const cache = new Map<string, Promise<string>>();

export function MarkdownCopyButton({
  markdownUrl,
  className,
  children,
}: MarkdownCopyButtonProps) {
  const [isLoading, setLoading] = useState(false);
  const [checked, onClick] = useCopyButton(async () => {
    const cached = cache.get(markdownUrl);
    if (cached) {
      await navigator.clipboard.writeText(await cached);
      return;
    }
    setLoading(true);
    try {
      const promise = fetch(markdownUrl).then((res) => res.text());
      cache.set(markdownUrl, promise);
      await navigator.clipboard.write([
        new ClipboardItem({ "text/plain": promise }),
      ]);
    } finally {
      setLoading(false);
    }
  });

  const mergedClassName = `${buttonVariants({
    color: "secondary",
    size: "sm",
    className: "gap-2 [&_svg]:size-3.5 [&_svg]:text-fd-muted-foreground",
  })}${className ? ` ${className}` : ""}`;

  return (
    <button disabled={isLoading} onClick={onClick} className={mergedClassName}>
      {checked ? <Check /> : <Copy />}
      <span>{children ?? "Copiar Markdown"}</span>
    </button>
  );
}
