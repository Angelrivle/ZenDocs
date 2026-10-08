import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';
import { appName } from './shared';
import { DiscordIcon, GithubIcon, SpigotIcon, BuiltByBitIcon } from '@/components/BrandIcons';
import { Layers } from 'lucide-react';
import React from 'react';

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: (
        <div className="flex items-center gap-2.5 select-none group">
          <div className="flex size-7 items-center justify-center rounded-md bg-zinc-800 text-white dark:bg-zinc-800 dark:text-white transition-all">
            <Layers className="size-4 text-white" />
          </div>
          <div className="flex items-baseline gap-1.5 font-bold tracking-tight">
            <span className="text-foreground text-sm font-semibold">ZenForge</span>
            <span className="text-xs text-muted-foreground font-normal">Docs</span>
          </div>
        </div>
      ),
    },
    links: [
      {
        type: 'main',
        text: 'Docs',
        url: '/docs',
      },
      {
        type: 'icon',
        label: 'BuiltByBit',
        url: 'https://builtbybit.com/',
        external: true,
        text: 'BuiltByBit',
        icon: <BuiltByBitIcon className="size-4 text-muted-foreground hover:text-foreground transition-colors" />,
      },
      {
        type: 'icon',
        label: 'SpigotMC',
        url: 'https://www.spigotmc.org/',
        external: true,
        text: 'SpigotMC',
        icon: <SpigotIcon className="size-4 text-muted-foreground hover:text-foreground transition-colors" />,
      },
      {
        type: 'icon',
        label: 'Discord',
        url: 'https://discord.gg/ThVDHfvqxH',
        external: true,
        text: 'Discord',
        icon: <DiscordIcon className="size-4 text-muted-foreground hover:text-foreground transition-colors" />,
      },
      {
        type: 'icon',
        label: 'GitHub',
        url: 'https://github.com/ZenForge-Studios',
        external: true,
        text: 'GitHub',
        icon: <GithubIcon className="size-4 text-muted-foreground hover:text-foreground transition-colors" />,
      },
    ],
  };
}
