import Link from "next/link";
import { IBM_Plex_Sans } from "next/font/google";
import {
  Anvil,
  ArrowRight,
  ArrowUpRight,
  Binary,
  BookOpenText,
  Boxes,
  MessageSquareMore,
  ShieldCheck,
  Zap,
  SquareTerminal,
} from "lucide-react";

const body = IBM_Plex_Sans({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["400", "500", "600", "700"],
});

const pillars = [
  {
    icon: Zap,
    title: "Rendimiento real",
    description:
      "Plugins diseñados para sobrevivir a servidores cargados, con estructuras limpias, persistencia seria y menos ruido innecesario.",
  },
  {
    icon: ShieldCheck,
    title: "Configuración entendible",
    description:
      "Nada de YAML caótico: menús, módulos y lógicas pensadas para modificarse rápido sin perder contexto.",
  },
  {
    icon: BookOpenText,
    title: "Wiki pensada para admins",
    description:
      "Comandos, permisos, placeholders y ejemplos útiles; menos relleno, más respuestas concretas.",
  },
];

const surfaces = [
  {
    eyebrow: "Blueprint 01",
    title:
      "Documentación que se siente como panel de control, no como folleto.",
    text: "Cada sección está planteada para ir de la instalación a la operación diaria con la menor fricción posible. La idea no es impresionar con texto, sino ayudarte a desplegar más rápido.",
    icon: Boxes,
  },
  {
    eyebrow: "Blueprint 02",
    title: "Desarrollo con estándares rigurosos.",
    text: "En ZenForge Studio no hacemos herramientas desechables. Cada línea de código y cada sistema está diseñado para escalar y soportar la presión de una comunidad activa.",
    icon: SquareTerminal,
  },
  {
    eyebrow: "Blueprint 03",
    title: "Soporte, iteración y sistemas que evolucionan.",
    text: "La documentación crece con los plugins. Nuevos módulos, placeholders, GUIs y sistemas se incorporan sin romper la navegación ni la lectura.",
    icon: Anvil,
  },
];

export default function HomePage() {
  return (
    <div
      className={`relative min-h-screen bg-[#050505] text-white ${body.variable} font-sans selection:bg-[#006bb4] selection:text-white`}
    >
      <main className="relative mx-auto flex min-h-screen w-full max-w-6xl flex-col p-6 sm:p-10 lg:p-16 gap-16 md:gap-24">
        
        {/* Simple Header */}
        <header className="flex justify-between items-center pb-6">
          <div className="text-xl font-bold flex items-center gap-2.5 tracking-tight">
            <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-sky-500/10 border border-sky-500/20 text-[#008cff]">
              <Anvil className="h-5 w-5" />
            </div>
            <span>ZenForge</span>
          </div>
          <div className="flex items-center gap-3">
            <a
              href="https://discord.gg/ThVDHfvqxH"
              target="_blank"
              rel="noreferrer"
              aria-label="Discord de la comunidad ZenForge (abre en nueva pestaña)"
              className="text-xs sm:text-sm font-medium border border-white/10 rounded-full px-4 py-2 hover:bg-white/5 hover:border-white/20 transition-colors text-white/80"
            >
              Discord
            </a>
            <Link 
              href="/docs" 
              className="text-xs sm:text-sm font-semibold rounded-full px-5 py-2 bg-gradient-to-r from-[#005c9e] to-[#007cd1] text-white hover:brightness-110 shadow-sm transition-all"
            >
              Documentación
            </Link>
          </div>
        </header>

        {/* HERO SECTION */}
        <section className="flex flex-col items-center text-center gap-8 mt-6">
          <div className="inline-flex items-center gap-2 rounded-full border border-[#006bb4]/40 bg-[#006bb4]/15 px-4 py-1.5 text-xs font-semibold uppercase tracking-wider backdrop-blur-md text-[#7cccff]">
            <ShieldCheck className="h-4 w-4 text-[#38bdf8]" />
            Wiki Oficial & Recursos
          </div>

          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-bold leading-tight tracking-tight max-w-4xl text-white">
            Forjamos la documentación que un servidor <span className="bg-clip-text text-transparent bg-gradient-to-r from-[#38bdf8] via-[#008cff] to-[#006bb4]">serio merece.</span>
          </h1>

          <p className="max-w-2xl text-lg text-white/80 leading-relaxed">
            ZenForge Docs reúne plugins, configuraciones y guías con una
            estructura limpia pensada para administradores que buscan máxima estabilidad
            y eficiencia operativa.
          </p>

          <div className="mt-4 flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
            <Link
              href="/docs"
              className="group flex items-center justify-center gap-3 rounded-full bg-gradient-to-r from-[#005c9e] to-[#007cd1] px-8 py-4 text-base font-semibold text-white transition-all duration-200 hover:scale-[1.03] shadow-[0_0_35px_rgba(0,107,180,0.35)] w-full sm:w-auto"
            >
              Entrar a la Wiki
              <ArrowRight className="h-5 w-5 transition-transform duration-200 group-hover:translate-x-1" />
            </Link>

            <a
              href="https://discord.gg/ThVDHfvqxH"
              target="_blank"
              rel="noreferrer"
              aria-label="Discord de soporte ZenForge (abre en nueva pestaña)"
              className="group flex items-center justify-center gap-3 rounded-full border border-white/15 bg-white/5 px-8 py-4 text-base font-semibold text-white transition-all duration-200 hover:bg-white/10 w-full sm:w-auto"
            >
              Discord de Soporte
              <ArrowUpRight className="h-5 w-5 transition-transform duration-200 group-hover:-translate-y-0.5 group-hover:translate-x-0.5 text-[#38bdf8]" />
            </a>
          </div>
        </section>

        {/* PILLARS GRID */}
        <section className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
          {pillars.map(({ icon: Icon, title, description }) => (
            <article
              key={title}
              className="rounded-2xl border border-white/10 bg-white/[0.03] p-8 backdrop-blur-sm transition-all duration-200 hover:-translate-y-1 hover:bg-white/[0.05] hover:border-[#008cff]/40"
            >
              <div className="bg-[#008cff]/15 w-14 h-14 rounded-xl flex items-center justify-center mb-6 border border-[#008cff]/20">
                <Icon className="h-7 w-7 text-[#38bdf8]" />
              </div>
              <h3 className="text-xl font-bold mb-3 text-white">{title}</h3>
              <p className="text-white/70 leading-relaxed text-sm sm:text-base">
                {description}
              </p>
            </article>
          ))}
        </section>

        {/* DETAILS SECTION */}
        <section className="rounded-[2.5rem] border border-white/10 bg-white/[0.02] p-8 sm:p-12 lg:p-16 flex flex-col lg:flex-row gap-12 items-center backdrop-blur-md mt-4 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-96 h-96 bg-[#006bb4]/15 blur-[100px] rounded-full pointer-events-none"></div>
          
          <div className="lg:w-1/2 relative z-10">
            <div className="text-sm font-semibold uppercase tracking-widest text-[#38bdf8] mb-4">
              ZenForge Studio
            </div>
            <h2 className="text-3xl lg:text-5xl font-bold leading-tight mb-6 text-white">
              Herramientas creadas por administradores, para administradores.
            </h2>
            <p className="text-lg text-white/75 leading-relaxed">
              Sabemos lo frustrante que es lidiar con sistemas a medias. Por eso, en 
              ZenForge Studio nos enfocamos en crear un ecosistema donde la estabilidad, 
              el rendimiento y la facilidad de configuración no sean opcionales, sino 
              nuestra garantía.
            </p>
          </div>
          <div className="lg:w-1/2 grid grid-cols-1 sm:grid-cols-2 gap-4 w-full relative z-10">
             <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-6 backdrop-blur-sm flex flex-col gap-4 group hover:border-[#008cff]/50 transition-colors">
                <Binary className="h-8 w-8 text-[#38bdf8] group-hover:scale-110 transition-transform duration-200" />
                <div>
                   <div className="text-xs font-semibold text-white/60 uppercase tracking-wider mb-1">Núcleo</div>
                   <div className="text-xl font-bold text-white">Plugins</div>
                </div>
             </div>
             <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-6 backdrop-blur-sm flex flex-col gap-4 group hover:border-[#008cff]/50 transition-colors">
                <MessageSquareMore className="h-8 w-8 text-[#38bdf8] group-hover:scale-110 transition-transform duration-200" />
                <div>
                   <div className="text-xs font-semibold text-white/60 uppercase tracking-wider mb-1">Señal</div>
                   <div className="text-xl font-bold text-white">Clara</div>
                </div>
             </div>
          </div>
        </section>

        {/* SURFACES BLOCK */}
        <section className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {surfaces.map(({ eyebrow, title, text, icon: Icon }) => (
            <article
              key={title}
              className="rounded-2xl border border-white/10 bg-white/[0.02] p-8 backdrop-blur-sm hover:border-[#008cff]/30 transition-colors"
            >
              <div className="flex items-center gap-3 mb-6">
                <Icon className="h-6 w-6 text-[#38bdf8]" />
                <span className="text-xs uppercase font-semibold tracking-wider text-sky-400">
                  {eyebrow}
                </span>
              </div>
              <h3 className="text-xl font-bold leading-tight mb-4 text-white">
                {title}
              </h3>
              <p className="text-white/70 leading-relaxed text-sm sm:text-base">{text}</p>
            </article>
          ))}
        </section>

        {/* FOOTER CTA */}
        <section className="flex flex-col items-center justify-center text-center mt-4 mb-12 relative">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-[#006bb4]/20 blur-[120px] rounded-full pointer-events-none"></div>
          
          <h2 className="text-3xl lg:text-5xl font-bold leading-tight mb-8 max-w-3xl relative z-10 text-white">
            Si vas a documentar software serio, hazlo fácil de leer.
          </h2>
          <Link
            href="/docs"
            className="flex items-center justify-center gap-3 rounded-full bg-gradient-to-r from-[#005c9e] to-[#007cd1] px-10 py-4 text-base font-bold text-white transition-all duration-200 hover:scale-[1.03] shadow-[0_0_35px_rgba(0,107,180,0.35)] relative z-10"
          >
            Abrir Documentación
            <ArrowRight className="h-5 w-5" />
          </Link>
        </section>

      </main>
    </div>
  );
}
