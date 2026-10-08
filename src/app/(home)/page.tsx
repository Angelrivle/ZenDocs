"use client";

import Link from "next/link";
import { useState } from "react";
import {
  BookOpen,
  Wrench,
  Package,
  Layers,
  ChevronDown,
  ArrowRight,
  Sun,
  Moon,
  ExternalLink,
  ChevronRight,
  Flame,
  Terminal,
  Activity,
  Sliders,
  Sparkles,
  Zap,
} from "lucide-react";
import {
  DiscordIcon,
  GithubIcon,
  SpigotIcon,
  BuiltByBitIcon,
} from "@/components/BrandIcons";

// Custom Heads Data matching the 8 showcase heads in sapphi.dev
const showcaseHeads = [
  {
    name: "Creeper",
    texture: "https://textures.minecraft.net/texture/f4254838c33ea227ffca223dddaabfe0b0215f70da649e944477f44370ca6952",
  },
  {
    name: "Pumpkin",
    texture: "https://textures.minecraft.net/texture/3f11c78a59db2c024f7d11e43bf60d8c2c3531d641764b1cc426b133525edae5",
  },
  {
    name: "Cake",
    texture: "https://textures.minecraft.net/texture/8f8d233d72c2c7e8010d939093598437ade515c475434e375796ddfadadf2448",
  },
  {
    name: "Chest",
    texture: "https://textures.minecraft.net/texture/8a75619deabcf4fe8603909ac79d2b6d6f31cdb84603f8bae07ef0e24891def3",
  },
  {
    name: "Ender Dragon",
    texture: "https://textures.minecraft.net/texture/7e4d35a2f6bd739605fa4eaa6e15d038009f3f20b1a204628016058736e7b95e",
  },
  {
    name: "Present",
    texture: "https://textures.minecraft.net/texture/94c3f595ae2ad5d7e931e4719cf6405832698b9e443adef8875d24fbeda7bfc4",
  },
  {
    name: "Earth",
    texture: "https://textures.minecraft.net/texture/f151cffdaf303673531a7651b36637cad912ba485643158e548d59b2ead5011",
  },
  {
    name: "Bee",
    texture: "https://textures.minecraft.net/texture/a0170da2428188b9b27a95d689b691d5fd77d7a666d113a9d2d4e642e474a935",
  },
];

export default function HomePage() {
  const [theme, setTheme] = useState<"dark" | "light">("dark");

  const toggleTheme = () => {
    const next = theme === "dark" ? "light" : "dark";
    setTheme(next);
    if (next === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  };

  return (
    <div className="min-h-screen bg-[#09090b] text-[#f4f4f5] selection:bg-[#00bcff] selection:text-white flex flex-col font-sans">
      
      {/* ========================================================= */}
      {/* 1. TOP NAVBAR (Identical to sapphi.dev)                   */}
      {/* ========================================================= */}
      <header className="sticky top-0 z-50 w-full border-b border-border/60 bg-[#09090b]/80 backdrop-blur-md">
        <nav className="mx-auto flex h-14 max-w-7xl items-center justify-between px-4 sm:px-6">
          
          {/* Left Brand + Nav links */}
          <div className="flex items-center gap-6">
            <Link href="/" className="flex items-center gap-2 outline-none group">
              <div className="flex size-7 items-center justify-center rounded-lg bg-zinc-800 text-white font-black text-sm group-hover:scale-105 transition-transform">
                <span className="font-mono">Z</span>
              </div>
            </Link>

            <div className="hidden md:flex items-center gap-1 text-sm font-normal text-muted-foreground">
              <Link
                href="/docs"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-md hover:text-foreground hover:bg-muted/50 transition-colors"
              >
                <BookOpen className="size-4" />
                <span>Docs</span>
                <ChevronDown className="size-3.5 opacity-60" />
              </Link>
              <Link
                href="/docs/zencustomitems"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-md hover:text-foreground hover:bg-muted/50 transition-colors"
              >
                <Wrench className="size-4" />
                <span>Tools</span>
                <ChevronDown className="size-3.5 opacity-60" />
              </Link>
              <Link
                href="/docs/zenenchants"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-md hover:text-foreground hover:bg-muted/50 transition-colors"
              >
                <Package className="size-4" />
                <span>Resources</span>
              </Link>
              <Link
                href="/docs/zeneconomy"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-md hover:text-foreground hover:bg-muted/50 transition-colors"
              >
                <Layers className="size-4" />
                <span>ZenItems</span>
              </Link>
            </div>
          </div>

          {/* Right Links (BuiltByBit, Spigot, Discord, GitHub, Theme Toggle) */}
          <div className="flex items-center gap-1.5">
            <a
              href="https://builtbybit.com/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="BuiltByBit"
              className="p-2 rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
            >
              <BuiltByBitIcon className="size-4" />
            </a>
            <a
              href="https://www.spigotmc.org/"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="SpigotMC"
              className="p-2 rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
            >
              <SpigotIcon className="size-4" />
            </a>
            <a
              href="https://discord.gg/ThVDHfvqxH"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Discord"
              className="p-2 rounded-lg text-muted-foreground hover:text-[#5865F2] hover:bg-muted/50 transition-colors"
            >
              <DiscordIcon className="size-4" />
            </a>
            <a
              href="https://github.com/ZenForge-Studios"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
              className="p-2 rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
            >
              <GithubIcon className="size-4" />
            </a>

            <div className="h-4 w-px bg-border/60 mx-1" />

            {/* Theme Toggle Pill */}
            <button
              onClick={toggleTheme}
              className="flex items-center gap-1 rounded-full border border-border bg-secondary/40 p-1 text-muted-foreground hover:text-foreground transition-all"
              aria-label="Toggle theme"
            >
              <span className={`p-1 rounded-full ${theme === "light" ? "bg-background text-foreground shadow-xs" : ""}`}>
                <Sun className="size-3.5" />
              </span>
              <span className={`p-1 rounded-full ${theme === "dark" ? "bg-background text-foreground shadow-xs" : ""}`}>
                <Moon className="size-3.5" />
              </span>
            </button>
          </div>
        </nav>
      </header>

      {/* ========================================================= */}
      {/* 2. HERO SECTION (Sapphire replica)                       */}
      {/* ========================================================= */}
      <section className="relative isolate w-full overflow-hidden border-b border-border/40">
        {/* Background Minecraft Scene with Dark Overlay */}
        <div className="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-950/20 via-[#09090b] to-[#09090b]">
          <div className="absolute inset-0 bg-[#09090b]/80 backdrop-blur-xs" />
        </div>

        <div className="mx-auto flex max-w-7xl flex-col items-center gap-6 px-4 py-20 text-center md:px-6 md:py-28">
          
          {/* Organization Tag */}
          <div className="flex items-center gap-2">
            <div className="flex size-6 items-center justify-center rounded-md bg-zinc-800 text-white font-mono text-xs font-bold">
              Z
            </div>
            <span className="font-medium text-muted-foreground text-sm tracking-wide">
              ZenForge Development
            </span>
          </div>

          {/* Heading */}
          <h1 className="max-w-4xl font-semibold text-4xl text-foreground tracking-[-0.03em] sm:text-5xl lg:text-6xl text-balance">
            Custom Minecraft plugins and high-quality configurations
          </h1>

          {/* Subtitle */}
          <p className="max-w-xl text-balance text-lg text-muted-foreground leading-relaxed">
            Plugins, documentation, and free web tools for Minecraft servers.
          </p>

          {/* Action Buttons */}
          <div className="mt-2 flex flex-wrap items-center justify-center gap-3">
            <Link
              href="/docs"
              className="inline-flex items-center gap-2 rounded-lg bg-[#008cff] hover:bg-[#007ad4] text-white px-4 py-2 text-sm font-medium transition-all shadow-sm"
            >
              <BookOpen className="size-4" />
              <span>Read the docs</span>
            </Link>

            <Link
              href="/docs/zencustomitems"
              className="inline-flex items-center gap-2 rounded-lg border border-border bg-background hover:bg-muted text-foreground px-4 py-2 text-sm font-medium transition-all"
            >
              <Wrench className="size-4 text-muted-foreground" />
              <span>Browse tools</span>
            </Link>
          </div>
        </div>
      </section>

      {/* ========================================================= */}
      {/* 3. MAIN CONTENT CONTAINER                                */}
      {/* ========================================================= */}
      <main className="mx-auto flex w-full max-w-7xl flex-col gap-20 px-4 py-16 md:px-6">

        {/* --------------------------------------------------------- */}
        {/* SECTION: PLUGINS (Cards with preview banners)             */}
        {/* --------------------------------------------------------- */}
        <section className="flex flex-col gap-5">
          <div className="flex items-baseline justify-between gap-4">
            <h2 className="font-semibold text-foreground text-xl tracking-[-0.02em]">
              Plugins
            </h2>
            <Link
              href="/docs"
              className="group inline-flex shrink-0 items-center gap-1 text-muted-foreground text-sm hover:text-foreground transition-colors"
            >
              <span>All plugins</span>
              <ChevronRight className="size-4 transition-transform group-hover:translate-x-0.5" />
            </Link>
          </div>

          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
            
            {/* Card 1: ZenCustomItems (SDlore counterpart) */}
            <Link
              href="/docs/zencustomitems"
              className="group flex flex-col overflow-hidden rounded-xl border border-border/60 bg-card hover:border-border hover:bg-accent/30 transition-all duration-300 hover:-translate-y-0.5"
            >
              <div className="relative aspect-video w-full overflow-hidden bg-gradient-to-br from-amber-500/20 via-zinc-900 to-black p-6 flex flex-col justify-between">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-amber-400 bg-amber-400/10 border border-amber-400/20 px-2 py-0.5 rounded">
                    PLUGIN
                  </span>
                  <div className="size-6 rounded-full bg-black/40 flex items-center justify-center text-xs font-mono text-zinc-400">
                    Z
                  </div>
                </div>
                <div>
                  <h4 className="text-2xl font-black tracking-tight text-white">
                    ZenCustomItems
                  </h4>
                  <p className="text-xs text-zinc-400 font-mono mt-0.5">
                    Items, triggers & mastery system
                  </p>
                </div>
              </div>

              <div className="flex flex-1 flex-col gap-1.5 p-4">
                <div className="flex items-center justify-between gap-2">
                  <h3 className="font-semibold text-base text-foreground">
                    ZenCustomItems
                  </h3>
                  <ChevronRight className="size-4 text-muted-foreground transition-transform group-hover:translate-x-0.5" />
                </div>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  Create and manage custom items with textures, conditions and triggers.
                </p>
              </div>
            </Link>

            {/* Card 2: ZenEnchants (SDStats counterpart) */}
            <Link
              href="/docs/zenenchants"
              className="group flex flex-col overflow-hidden rounded-xl border border-border/60 bg-card hover:border-border hover:bg-accent/30 transition-all duration-300 hover:-translate-y-0.5"
            >
              <div className="relative aspect-video w-full overflow-hidden bg-gradient-to-br from-emerald-500/20 via-zinc-900 to-black p-6 flex flex-col justify-between">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-400/10 border border-emerald-400/20 px-2 py-0.5 rounded">
                    ENCHANTS
                  </span>
                  <div className="size-6 rounded-full bg-black/40 flex items-center justify-center text-xs font-mono text-zinc-400">
                    Z
                  </div>
                </div>
                <div>
                  <h4 className="text-2xl font-black tracking-tight text-white">
                    ZenEnchants
                  </h4>
                  <p className="text-xs text-zinc-400 font-mono mt-0.5">
                    185+ custom modular effects
                  </p>
                </div>
              </div>

              <div className="flex flex-1 flex-col gap-1.5 p-4">
                <div className="flex items-center justify-between gap-2">
                  <h3 className="font-semibold text-base text-foreground">
                    ZenEnchants
                  </h3>
                  <ChevronRight className="size-4 text-muted-foreground transition-transform group-hover:translate-x-0.5" />
                </div>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  High-performance custom enchantments engine with zero server lag.
                </p>
              </div>
            </Link>

            {/* Card 3: ZenEconomy (SDLootboxes counterpart) */}
            <Link
              href="/docs/zeneconomy"
              className="group flex flex-col overflow-hidden rounded-xl border border-border/60 bg-card hover:border-border hover:bg-accent/30 transition-all duration-300 hover:-translate-y-0.5"
            >
              <div className="relative aspect-video w-full overflow-hidden bg-gradient-to-br from-indigo-500/20 via-zinc-900 to-black p-6 flex flex-col justify-between">
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-400 bg-indigo-400/10 border border-indigo-400/20 px-2 py-0.5 rounded">
                    ECONOMY
                  </span>
                  <div className="size-6 rounded-full bg-black/40 flex items-center justify-center text-xs font-mono text-zinc-400">
                    Z
                  </div>
                </div>
                <div>
                  <h4 className="text-2xl font-black tracking-tight text-white">
                    ZenEconomy
                  </h4>
                  <p className="text-xs text-zinc-400 font-mono mt-0.5">
                    Multi-currency & real-time transactions
                  </p>
                </div>
              </div>

              <div className="flex flex-1 flex-col gap-1.5 p-4">
                <div className="flex items-center justify-between gap-2">
                  <h3 className="font-semibold text-base text-foreground">
                    ZenEconomy
                  </h3>
                  <ChevronRight className="size-4 text-muted-foreground transition-transform group-hover:translate-x-0.5" />
                </div>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  Modern Vault-backed economy with dynamic currencies and MySQL caching.
                </p>
              </div>
            </Link>

          </div>
        </section>

        {/* --------------------------------------------------------- */}
        {/* SECTION: FREE TOOLS FOR YOUR SERVER                       */}
        {/* --------------------------------------------------------- */}
        <section className="flex flex-col gap-8">
          <div className="flex flex-col items-center gap-3 text-center">
            <h2 className="font-semibold text-3xl text-foreground tracking-[-0.03em] sm:text-4xl">
              Free tools for your server
            </h2>
            <p className="max-w-xl text-muted-foreground leading-relaxed">
              Build holograms, tune startup flags, color your text and check how your server looks in the multiplayer list, right from the browser.
            </p>
          </div>

          <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
            
            {/* BIG CARD: Hologram Builders */}
            <article className="group relative flex flex-col gap-4 overflow-hidden rounded-xl border border-border/60 bg-card p-3 transition-colors hover:border-border md:col-span-2 lg:row-span-2">
              <div className="relative isolate flex min-h-64 flex-1 items-center justify-center overflow-hidden rounded-lg px-4 py-8 ring-1 ring-foreground/10 bg-[#0d1117] transition-transform duration-300 group-hover:-translate-y-0.5">
                {/* Simulated Floating Hologram */}
                <div className="grid bg-black/50 backdrop-blur-md px-6 py-4 rounded-lg border border-white/10 text-center font-mono text-sm sm:text-base leading-snug">
                  <span className="font-bold text-[#00bcff] tracking-wider">ZENFORGE DEVELOPMENT</span>
                  <span className="text-zinc-400 text-xs">Plugins • Configs • Tools</span>
                  <span className="text-white mt-2">Welcome, <span className="text-cyan-300">%player_name%</span></span>
                  <span className="text-yellow-300 text-xs mt-1">Right-click to open the menu</span>
                </div>
              </div>

              <div className="flex flex-col gap-4 px-1 pb-1 sm:flex-row sm:items-end sm:justify-between">
                <div className="flex flex-col gap-1">
                  <h3 className="font-medium text-foreground">Hologram Builders</h3>
                  <p className="max-w-md text-muted-foreground text-sm leading-relaxed">
                    Write the lines, see them float in the world as you type, then export the file or the commands for FancyHolograms or DecentHolograms.
                  </p>
                </div>
                <div className="flex shrink-0 gap-2">
                  <Link
                    href="/docs"
                    className="inline-flex items-center gap-1.5 rounded-lg border border-border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted transition-colors"
                  >
                    <span>FancyHolograms</span>
                    <ChevronRight className="size-3.5" />
                  </Link>
                  <Link
                    href="/docs"
                    className="inline-flex items-center gap-1.5 rounded-lg border border-border bg-background px-3 py-1.5 text-xs font-medium hover:bg-muted transition-colors"
                  >
                    <span>DecentHolograms</span>
                    <ChevronRight className="size-3.5" />
                  </Link>
                </div>
              </div>
            </article>

            {/* CARD 2: Startup Flags */}
            <Link
              href="/docs"
              className="group relative flex flex-col gap-4 overflow-hidden rounded-xl border border-border/60 bg-card p-3 transition-colors hover:border-border"
            >
              <div className="relative isolate flex min-h-40 flex-1 items-center justify-center overflow-hidden rounded-lg px-4 py-6 ring-1 ring-foreground/10 bg-muted/60">
                <div className="flex w-full flex-col gap-3 font-mono text-xs">
                  <div className="flex justify-between text-muted-foreground text-[11px]">
                    <span>Allocated memory</span>
                    <span className="text-foreground font-semibold">8 GB</span>
                  </div>
                  {/* Memory bar */}
                  <div className="flex h-2.5 gap-1">
                    <span className="h-full flex-1 rounded-xs bg-[#008cff]" />
                    <span className="h-full flex-1 rounded-xs bg-[#008cff]" />
                    <span className="h-full flex-1 rounded-xs bg-[#008cff]" />
                    <span className="h-full flex-1 rounded-xs bg-foreground/15" />
                    <span className="h-full flex-1 rounded-xs bg-foreground/15" />
                    <span className="h-full flex-1 rounded-xs bg-foreground/15" />
                  </div>
                  <div className="rounded bg-background/80 p-2 text-[10px] text-zinc-400 border border-white/5 truncate">
                    java -Xms8192M -Xmx8192M -XX:+UseG1GC
                  </div>
                </div>
              </div>
              <div className="flex flex-col gap-1 px-1 pb-1">
                <h3 className="flex items-center gap-1 font-medium text-foreground">
                  Startup Flags
                  <ChevronRight className="size-3.5 text-muted-foreground" />
                </h3>
                <p className="text-muted-foreground text-xs leading-relaxed">
                  Aikar&apos;s flags sized to your RAM, as a start script for Paper or Purpur.
                </p>
              </div>
            </Link>

            {/* CARD 3: Server Status */}
            <Link
              href="/docs"
              className="group relative flex flex-col gap-4 overflow-hidden rounded-xl border border-border/60 bg-card p-3 transition-colors hover:border-border"
            >
              <div className="relative isolate flex min-h-40 flex-1 items-center justify-center overflow-hidden rounded-lg px-4 py-6 ring-1 ring-foreground/10 bg-[#151619]">
                <div className="flex w-full gap-2 rounded bg-black/90 p-2 text-left font-mono text-xs ring-1 ring-white/10">
                  <div className="size-9 bg-emerald-700 rounded-xs flex items-center justify-center font-bold text-white shrink-0">
                    MC
                  </div>
                  <div className="flex flex-col min-w-0 flex-1">
                    <div className="flex justify-between items-center text-[11px]">
                      <span className="font-semibold text-white truncate">ZenForge Server</span>
                      <span className="text-emerald-400 text-[10px]">128/500</span>
                    </div>
                    <span className="text-zinc-400 text-[10px] truncate">
                      Minecraft plugins and configs
                    </span>
                  </div>
                </div>
              </div>
              <div className="flex flex-col gap-1 px-1 pb-1">
                <h3 className="flex items-center gap-1 font-medium text-foreground">
                  Server Status
                  <ChevronRight className="size-3.5 text-muted-foreground" />
                </h3>
                <p className="text-muted-foreground text-xs leading-relaxed">
                  Ping any Java server and see its icon, MOTD and online players.
                </p>
              </div>
            </Link>

            {/* CARD 4: RGB Gradients */}
            <Link
              href="/docs"
              className="group relative flex flex-col gap-4 overflow-hidden rounded-xl border border-border/60 bg-card p-3 transition-colors hover:border-border"
            >
              <div className="relative isolate flex min-h-40 flex-1 items-center justify-center overflow-hidden rounded-lg px-4 py-6 ring-1 ring-foreground/10 bg-[#100818]">
                <div className="flex flex-col items-center gap-2">
                  <span className="font-mono text-3xl font-black bg-gradient-to-r from-cyan-400 to-indigo-500 bg-clip-text text-transparent">
                    ZenForge
                  </span>
                  <code className="text-[10px] text-zinc-400 font-mono">
                    &lt;gradient:#00bcff:#6366f1&gt;ZenForge&lt;/gradient&gt;
                  </code>
                </div>
              </div>
              <div className="flex flex-col gap-1 px-1 pb-1">
                <h3 className="flex items-center gap-1 font-medium text-foreground">
                  RGB Gradients
                  <ChevronRight className="size-3.5 text-muted-foreground" />
                </h3>
                <p className="text-muted-foreground text-xs leading-relaxed">
                  Per-character RGB text for chat, lore and signs, in MiniMessage.
                </p>
              </div>
            </Link>

            {/* CARD 5: Sounds Explorer */}
            <Link
              href="/docs"
              className="group relative flex flex-col gap-4 overflow-hidden rounded-xl border border-border/60 bg-card p-3 transition-colors hover:border-border"
            >
              <div className="relative isolate flex min-h-40 flex-1 items-center justify-center overflow-hidden rounded-lg px-4 py-6 ring-1 ring-foreground/10 bg-muted/60">
                <div className="flex w-full items-center gap-3">
                  <div className="size-9 rounded-full bg-[#008cff] text-white flex items-center justify-center shrink-0">
                    ▶
                  </div>
                  <div className="flex flex-col min-w-0 flex-1 gap-1">
                    <div className="h-6 flex items-center gap-0.5">
                      {[40, 60, 20, 80, 50, 90, 70, 30, 85, 45, 65, 35, 75].map((h, i) => (
                        <span
                          key={i}
                          style={{ height: `${h}%` }}
                          className="w-1 bg-[#008cff] rounded-xs"
                        />
                      ))}
                    </div>
                    <span className="font-mono text-[10px] text-muted-foreground truncate">
                      entity.ender_dragon.growl
                    </span>
                  </div>
                </div>
              </div>
              <div className="flex flex-col gap-1 px-1 pb-1">
                <h3 className="flex items-center gap-1 font-medium text-foreground">
                  Sounds Explorer
                  <ChevronRight className="size-3.5 text-muted-foreground" />
                </h3>
                <p className="text-muted-foreground text-xs leading-relaxed">
                  Play every Minecraft sound and copy its id or /playsound command.
                </p>
              </div>
            </Link>

            {/* CARD 6: More tools */}
            <div className="group relative flex flex-col justify-between overflow-hidden rounded-xl border border-border/60 bg-card p-4">
              <h3 className="font-medium text-foreground text-sm">More tools</h3>
              <ul className="flex flex-col gap-2 my-2">
                <li className="flex items-center gap-2.5 text-xs text-muted-foreground hover:text-foreground">
                  <div className="size-7 rounded bg-muted/80 flex items-center justify-center">
                    <Activity className="size-3.5" />
                  </div>
                  <div>
                    <p className="font-medium text-foreground">World Size Calculator</p>
                    <p className="text-[10px]">Chunks, disk and pregen time</p>
                  </div>
                </li>
                <li className="flex items-center gap-2.5 text-xs text-muted-foreground hover:text-foreground">
                  <div className="size-7 rounded bg-muted/80 flex items-center justify-center">
                    <Sliders className="size-3.5" />
                  </div>
                  <div>
                    <p className="font-medium text-foreground">Server Icon Maker</p>
                    <p className="text-[10px]">Any image or head as server-icon.png</p>
                  </div>
                </li>
              </ul>
              <Link
                href="/docs"
                className="flex items-center justify-between text-xs font-medium text-foreground pt-2 border-t border-border/40 hover:text-[#008cff]"
              >
                <span>All tools</span>
                <ChevronRight className="size-3.5" />
              </Link>
            </div>

          </div>
        </section>

        {/* --------------------------------------------------------- */}
        {/* SECTION: MINECRAFT HEADS (Replica)                       */}
        {/* --------------------------------------------------------- */}
        <section className="relative isolate grid items-center gap-8 overflow-hidden rounded-xl border border-border/60 bg-card p-6 md:grid-cols-[minmax(0,1fr)_auto] md:gap-12 md:p-10">
          <div className="flex flex-col items-start gap-4">
            <h2 className="font-semibold text-2xl text-foreground tracking-[-0.02em]">
              Minecraft Heads
            </h2>
            <p className="max-w-md text-muted-foreground leading-relaxed text-sm">
              More than 86,000 custom heads, searchable by name. Rotate any of them in 3D and copy a ready-made /give command for 1.8 through 1.21, or turn a player&apos;s skin into a head.
            </p>
            <div className="flex flex-wrap gap-3">
              <Link
                href="/docs"
                className="inline-flex items-center gap-2 rounded-lg bg-[#008cff] hover:bg-[#007ad4] text-white px-3.5 py-1.5 text-xs font-medium transition-all"
              >
                <span>Browse heads</span>
              </Link>
              <Link
                href="/docs"
                className="inline-flex items-center gap-1.5 rounded-lg border border-border px-3.5 py-1.5 text-xs font-medium text-muted-foreground hover:text-foreground hover:bg-muted transition-all"
              >
                <span>Try a player&apos;s head</span>
                <ChevronRight className="size-3" />
              </Link>
            </div>
          </div>

          {/* Grid of 8 Minecraft Heads with isometric 3D styling */}
          <div className="grid grid-cols-4 gap-2.5 sm:gap-3 justify-self-center">
            {showcaseHeads.map((head) => (
              <div
                key={head.name}
                title={head.name}
                className="group relative flex size-16 sm:size-18 items-center justify-center rounded-xl bg-background/50 border border-border/60 hover:bg-background/80 hover:-translate-y-1 transition-all duration-200 cursor-pointer"
              >
                <div
                  className="size-10 sm:size-12 [image-rendering:pixelated] rounded shadow-sm group-hover:scale-110 transition-transform"
                  style={{
                    backgroundImage: `url("${head.texture}")`,
                    backgroundSize: "800% auto",
                    backgroundPosition: "-100% -100%",
                  }}
                />
              </div>
            ))}
          </div>
        </section>

        {/* --------------------------------------------------------- */}
        {/* SECTION: STUCK ON SOMETHING? (Support Card on right)      */}
        {/* --------------------------------------------------------- */}
        <section className="relative isolate grid items-center gap-8 overflow-hidden rounded-xl border border-border/60 bg-card p-6 md:grid-cols-[minmax(0,1fr)_auto] md:gap-12 md:p-10">
          <div className="flex flex-col items-start gap-4">
            <h2 className="font-semibold text-2xl text-foreground tracking-[-0.02em]">
              Stuck on something?
            </h2>
            <p className="max-w-md text-muted-foreground leading-relaxed text-sm">
              Bring setup questions, config issues or bug reports straight to the team on Discord. If your server is crashing, run its latest.log through our guides: it often names the fix.
            </p>
            <div className="flex flex-wrap gap-2.5">
              <a
                href="https://discord.gg/ThVDHfvqxH"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 rounded-lg bg-[#008cff] hover:bg-[#007ad4] text-white px-3.5 py-1.5 text-xs font-medium transition-all"
              >
                <DiscordIcon className="size-3.5 fill-current" />
                <span>Ask on Discord</span>
              </a>
              <Link
                href="/docs"
                className="inline-flex items-center gap-2 rounded-lg border border-border bg-background hover:bg-muted px-3.5 py-1.5 text-xs font-medium text-foreground transition-all"
              >
                <span>Read the docs</span>
              </Link>
            </div>
          </div>

          {/* Right Discord Invitation Box (Replica) */}
          <div className="w-full max-w-xs justify-self-center overflow-hidden rounded-xl bg-muted/40 shadow-lg ring-1 ring-border/60">
            <p className="px-4 py-2.5 font-medium text-muted-foreground text-xs">
              You&apos;re invited to join
            </p>
            <div className="mx-1.5 mb-1.5 flex flex-col gap-4 rounded-lg bg-card p-4 ring-1 ring-border/60">
              <div className="flex items-center gap-3">
                <div className="size-12 rounded-xl bg-zinc-800 flex items-center justify-center font-mono font-black text-white text-xl">
                  Z
                </div>
                <div className="flex min-w-0 flex-col gap-0.5">
                  <p className="truncate font-semibold text-sm">ZenForge Development</p>
                  <p className="flex items-center gap-3 text-muted-foreground text-[11px]">
                    <span className="flex items-center gap-1.5">
                      <span className="size-2 rounded-full bg-emerald-500" />
                      Online
                    </span>
                    <span className="text-muted-foreground/60">Discord Community</span>
                  </p>
                </div>
              </div>
              <a
                href="https://discord.gg/ThVDHfvqxH"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center justify-center gap-2 rounded-lg bg-[#008cff] hover:bg-[#007ad4] text-white py-2 text-xs font-medium transition-all w-full"
              >
                <DiscordIcon className="size-3.5 fill-current" />
                <span>Join the server</span>
              </a>
            </div>
          </div>
        </section>

      </main>

      {/* ========================================================= */}
      {/* 4. FOOTER (Identical multi-column replica from image 5)   */}
      {/* ========================================================= */}
      <footer className="border-t border-border/40 bg-background">
        <div className="mx-auto max-w-7xl px-4 py-12 md:px-6">
          <div className="grid grid-cols-2 gap-8 md:grid-cols-5">
            
            {/* Brand column */}
            <div className="col-span-2 flex flex-col gap-3">
              <Link href="/" className="flex items-center gap-2 font-semibold text-base text-foreground">
                <div className="size-6 rounded bg-zinc-800 text-white font-mono flex items-center justify-center text-xs">
                  Z
                </div>
                <span>ZenForge</span>
              </Link>
              <p className="max-w-64 text-sm text-muted-foreground leading-relaxed">
                Plugins, tools and resources for Minecraft servers.
              </p>
            </div>

            {/* Products column */}
            <div className="flex flex-col gap-2.5 text-sm">
              <h4 className="font-medium text-foreground">Products</h4>
              <Link href="/docs/zencustomitems" className="text-muted-foreground hover:text-foreground transition-colors">ZenCustomItems</Link>
              <Link href="/docs/zenenchants" className="text-muted-foreground hover:text-foreground transition-colors">ZenEnchants</Link>
              <Link href="/docs/zeneconomy" className="text-muted-foreground hover:text-foreground transition-colors">ZenEconomy</Link>
              <Link href="/docs" className="text-muted-foreground hover:text-foreground transition-colors">All Plugins</Link>
            </div>

            {/* Documentation column */}
            <div className="flex flex-col gap-2.5 text-sm">
              <h4 className="font-medium text-foreground">Documentation</h4>
              <Link href="/docs" className="text-muted-foreground hover:text-foreground transition-colors">Docs</Link>
              <Link href="/docs" className="text-muted-foreground hover:text-foreground transition-colors">Plugins</Link>
              <Link href="/docs" className="text-muted-foreground hover:text-foreground transition-colors">Changelog</Link>
            </div>

            {/* Community column */}
            <div className="flex flex-col gap-2.5 text-sm">
              <h4 className="font-medium text-foreground">Community</h4>
              <a href="https://discord.gg/ThVDHfvqxH" target="_blank" rel="noreferrer" className="flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors">
                <DiscordIcon className="size-3.5 fill-current text-[#5865F2]" />
                <span>Discord</span>
              </a>
              <a href="https://builtbybit.com/" target="_blank" rel="noreferrer" className="flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors">
                <BuiltByBitIcon className="size-3.5" />
                <span>BuiltByBit</span>
              </a>
              <a href="https://github.com/ZenForge-Studios" target="_blank" rel="noreferrer" className="flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors">
                <GithubIcon className="size-3.5" />
                <span>GitHub</span>
              </a>
            </div>

          </div>

          {/* Subfooter */}
          <div className="mt-12 pt-6 border-t border-border/40 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-muted-foreground">
            <p>© {new Date().getFullYear()} ZenForge Development. Not affiliated with Mojang or Microsoft.</p>
            <div className="flex items-center gap-4">
              <Link href="/docs" className="hover:text-foreground">Privacy</Link>
              <Link href="/docs" className="hover:text-foreground">Terms</Link>
            </div>
          </div>
        </div>
      </footer>

    </div>
  );
}
