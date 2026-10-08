import React from 'react';
import {
  Download,
  Settings,
  Terminal,
  Shield,
  FileCode,
  Layers,
  Sparkles,
  Zap,
  Target,
  Sliders,
  Variable,
  Code2,
  Box,
  Palette,
  Eye,
  Database,
  Coins,
  CreditCard,
  MessageSquare,
  Gamepad2,
  Trophy,
  Swords,
  Timer,
  ShoppingBag,
  Heart,
  Flame,
  Bomb,
  Move,
  Droplet,
  Snowflake,
  ShieldAlert,
  Wand2,
  Package,
  Activity,
  Award,
  BookOpen,
} from 'lucide-react';

export function getSidebarIcon(slug: string, isFolder: boolean = false): React.ReactNode {
  const s = slug.toLowerCase();

  // Folders / Categorías mayores
  if (isFolder) {
    if (s.includes('effects')) return <Sparkles className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('triggers')) return <Target className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('conditions')) return <Sliders className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('enchants')) return <Wand2 className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('customitems')) return <Package className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('economy')) return <Coins className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('chat')) return <MessageSquare className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    if (s.includes('rankups')) return <Award className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
    return <Box className="size-4 text-zinc-400 group-hover:text-zinc-200" />;
  }

  // Common Standard Pages
  if (s === 'instalacion' || s.includes('install')) return <Download className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'config-yml' || s.includes('config')) return <Settings className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'comandos_y_permisos' || s.includes('comando') || s.includes('permiso')) return <Terminal className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'estructura_de_archivos' || s.includes('estructura')) return <Layers className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'requisitos_del_sistema' || s.includes('requisito')) return <Activity className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'messages-yml' || s.includes('message')) return <MessageSquare className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'api' || s.includes('api')) return <Code2 className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'targets-yml' || s.includes('target')) return <Target className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'items-yml' || s.includes('item')) return <Box className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'rarities-yml' || s.includes('raritie')) return <Sparkles className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'filters-and-mutators' || s.includes('filter') || s.includes('mutator')) return <Sliders className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'placeholders' || s.includes('placeholder')) return <Variable className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'base_de_datos' || s.includes('database')) return <Database className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'currencies-yml' || s.includes('currenc')) return <Coins className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'plans-yml' || s.includes('plan')) return <CreditCard className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'games' || s.includes('game')) return <Gamepad2 className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'cosmetics' || s.includes('cosmetic')) return <Palette className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'zonas' || s.includes('zone')) return <Shield className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s === 'menus' || s.includes('menu')) return <Eye className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;

  // Combat / Effects specific
  if (s.includes('damage') || s.includes('attack') || s.includes('sword')) return <Swords className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('heal') || s.includes('health') || s.includes('vampirism')) return <Heart className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('fire') || s.includes('ignite') || s.includes('lava')) return <Flame className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('explosion') || s.includes('blast')) return <Bomb className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('lightning')) return <Zap className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('freeze') || s.includes('ice') || s.includes('snow')) return <Snowflake className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('bleed') || s.includes('poison') || s.includes('potion')) return <Droplet className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('knockback') || s.includes('velocity') || s.includes('launch') || s.includes('pull')) return <Move className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('shield')) return <ShieldAlert className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('time') || s.includes('cooldown')) return <Timer className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
  if (s.includes('shop') || s.includes('auction')) return <ShoppingBag className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;

  return <FileCode className="size-3.5 text-zinc-400 group-hover:text-zinc-200" />;
}
