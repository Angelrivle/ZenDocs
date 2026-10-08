import { source } from '@/lib/source';
import { DocsLayout } from 'fumadocs-ui/layouts/docs';
import { baseOptions } from '@/lib/layout.shared';
import React from 'react';

export default function Layout({ children }: LayoutProps<'/docs'>) {
  const shared = baseOptions();

  return (
    <DocsLayout
      tree={source.getPageTree()}
      {...shared}
      nav={{
        ...shared.nav,
        enabled: true,
      }}
    >
      {children}
    </DocsLayout>
  );
}
