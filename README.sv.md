# Qoder Starter 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <strong>Svenska</strong> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>En AI-agent utan regler är bara ett kaotiskt manus.</strong></h3>
  <p><strong>Qoder Starter är ett lätt, AI-first regelsystem utformat för att anpassa AI-agentens beteenden med orörda kodningskonventioner i Cursor, Gemini och Claude Code.</strong></p>

  <p>Sluta slösa bort tokens, lida av AI-hallucinationer och kämpa med inkonsekventa kodstilar. Styr din kodningsassistent med 5 grundläggande regelblad direkt.</p>
</div>

> 📦 Gratis mall av **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licensierad under [MIT License](LICENSE)  
> ☕ Om det är användbart, [köp mig en kaffe](https://ko-fi.com/andiupn) · 🚀 Behöver du avancerade monorepos, anpassade agenter och färdigförpackat minne? Prova [PRO-versionen](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Problemet: kaoset med AI-kodassistenter
AI-assistenter är otroligt snabba. Men utan förkonfigurerade riktlinjer skriver de ostrukturerad kod, ignorerar dina namnkonventioner, läcker hemligheter och gör oberäkneliga git-commits som förstör din förvarshistorik.

---

## ⚡ Lösningen: De 5 grundläggande AI-reglerna

### 1. 📜 Kod- och språkkonventioner
Håller språket tydligt (`bahasa.md`: indonesiska för chatt, engelska för kod) och upprätthåller standardformatering (`code-conventions.md`: pilfunktioner, TypeScript strict, JSDoc).

### 🔒 2. Noll-Hallucinationssäkerhet
Bevakar API-nycklar och autentiseringsuppgifter, upprätthåller datavalidering (Zod) och XSS-förebyggande regler (`security.md`) innan du skriver någon kod.

### 🧠 3. Historiskt kunskapssystem
Konfigurerar minnesriktlinjer (`memory-usage.md`) och git-konventioner (`git-conventions.md`) så att AI-agenten lär sig av din förvarshistorik, med hjälp av `/skills` för att spara sessionsupptäckter.

---

## 📊 LITE vs PRO: Premium-uppgraderingen

| Vad du får | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Grundläggande regler** | 5 | 14 (lägger till: felhantering, testning, stack, a11y, etc.) |
| **Specialiserade kundagenter** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, etc.) |
| **Memory Entries (Generic Seed)** | ❌ | 12 (Next.js config fixar, Playwright, Redis) |
| **DevOps & MCP-konfigurationer** | ❌ | ✅ (`mcp.json` mallar) |
| **Uppströmsuppdateringar** | Via GitHub | Via [GitHub-sponsorer](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Visa fullständig jämförelse av funktioner och uppgraderingsguide](COMPARISON.md)**

---

## 📂 Repository Blueprint

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Förhandsgranskning

<p align="center">
  <img src="assets/screenshots/starter-rules-overview.png" alt="Qoder Starter Rules Overview" width="600"/>
</p>

<p align="center">
  <img src="assets/screenshots/comparison-starter-vs-pro.png" alt="Starter vs PRO Comparison" width="600"/>
</p>

<p align="center">
  <img src="assets/screenshots/starter-validation.png" alt="Qoder Starter Validation" width="600"/>
</p>

---

## 🚀 Kom igång i 3 steg

### 1. Kopiera konfigurationer:
Kopiera `.qoder/`, `.agent/`, `scripts/` och `AGENTS.md` till din projektrot.

### 2. Konfigurera miljö:

```bash
cp .env.example .env
```

### 3. Börja koda:
Öppna projektet i Cursor eller kör Claude Code. AI-agenten läser reglerna automatiskt!

---

## 💖 Stöd detta projekt (donationer)

Om den här mallen har påskyndat ditt kodningsarbetsflöde, överväg att stödja:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licens

Detta projekt är licensierat under **MIT License**. Se filen [LICENSE](LICENSE) för mer information.