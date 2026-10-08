import React from 'react';
import { DiscordIcon } from './BrandIcons';

interface SidebarSupportCardProps {
  className?: string;
}

export function SidebarSupportCard({ className = '' }: SidebarSupportCardProps) {
  return (
    <div
      className={`rounded-xl border border-sky-500/20 bg-sky-950/20 p-3.5 backdrop-blur-md shadow-lg shadow-black/20 flex flex-col gap-2.5 my-3 ${className}`}
    >
      <div className="flex flex-col gap-1">
        <span className="text-[10px] font-bold uppercase tracking-wider text-sky-400">
          Soporte Oficial
        </span>
        <h4 className="text-xs font-semibold text-white/95 leading-snug">
          ¿Tienes dudas o necesitas ayuda?
        </h4>
        <p className="text-[11px] text-white/60 leading-relaxed">
          Preguntas sobre configuración, guías o soporte técnico directo con nuestro equipo.
        </p>
      </div>

      <a
        href="https://discord.gg/ThVDHfvqxH"
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center justify-center gap-2 rounded-lg bg-[#5865F2] hover:bg-[#4752c4] text-white px-3 py-1.5 text-xs font-medium transition-all duration-150 shadow-sm hover:shadow-md cursor-pointer active:scale-[0.98]"
      >
        <DiscordIcon className="size-3.5 fill-current" />
        <span>Preguntar en Discord</span>
      </a>
    </div>
  );
}
