# Qoder Starter 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <strong>Română</strong>
</div>

<br />

<div align="center">
  <h3><strong>Un agent AI fără reguli este doar un script haotic.</strong></h3>
  <p><strong>Qoder Starter este un sistem de reguli ușor, bazat pe AI, conceput pentru a alinia comportamentele agenților AI cu convențiile de codare impecabile din Cursor, Gemini și Claude Code.</strong></p>

  <p>Nu mai risipiți jetoane, nu suferiți de halucinații AI și nu vă luptați cu stiluri de cod inconsecvente. Alimentați-vă asistentul de codificare cu 5 foi de reguli fundamentale instantaneu.</p>
</div>

> 📦 Șablon gratuit de la **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licențiat sub [Licență MIT](LICENSE)  
> ☕ Dacă este util, [cumpără-mi o cafea](https://ko-fi.com/andiupn) · 🚀 Ai nevoie de monorepos avansate, agenți personalizați și memorie preambalată? Încercați [versiunea PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Problema: haosul asistenților de cod AI
Asistenții AI sunt incredibil de rapizi. Cu toate acestea, fără linii directoare preconfigurate, ei scriu cod nestructurat, ignoră convențiile de numire, scurg secrete și fac comiteri git neregulate care îți distrug istoricul depozitului.

---

## ⚡ Soluția: cele 5 reguli fundamentale ale AI

### 1. 📜 Convenții de cod și limbă
Menține limba clară (`bahasa.md`: indoneziană pentru chat, engleză pentru cod) și impune formatarea standard (`code-conventions.md`: funcții săgeți, TypeScript strict, JSDoc).

### 🔒 2. Securitate Zero-Halucinații
Protejează cheile și acreditările API, impunând validarea datelor (Zod) și regulile de prevenire XSS (`security.md`) înainte de a scrie orice cod.

### 🧠 3. Sistemul de cunoștințe istorice
Configurați regulile de memorie (`memory-usage.md`) și convențiile git (`git-conventions.md`), astfel încât agentul AI să învețe din istoricul depozitului dvs., folosind `/skills` pentru a salva descoperirile sesiunii.

---

## 📊 LITE vs PRO: Upgrade Premium

| Ce primești | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Reguli fundamentale** | 5 | 14 (adaugă: tratarea erorilor, testare, stivă, a11y etc.) |
| **Agenți specialiști în vamă** | ❌ | 5 (`code-reviewer`, `nextjs-specialist` etc.) |
| **Intrari de memorie (Seed generic)** | ❌ | 12 (remedieri de configurare Next.js, Dramaturg, Redis) |
| **Configurații DevOps și MCP** | ❌ | ✅ (`mcp.json` șabloane) |
| **Actualizări în amonte** | Prin GitHub | Prin [Sponsori GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Vedeți Ghidul complet de comparare și actualizare a funcțiilor](COMPARISON.md)**

---

## 📂 Planul de depozit

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Previzualizare

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

## 🚀 Începeți în 3 pași

### 1. Copiați configurațiile:
Copiați `.qoder/`, `.agent/`, `scripts/` și `AGENTS.md` în rădăcina proiectului.

### 2. Configurați mediul:

```bash
cp .env.example .env
```

### 3. Începeți codarea:
Deschideți proiectul în Cursor sau rulați Claude Code. Agentul AI va citi regulile automat!

---

## 💖 Sprijină acest proiect (donații)

Dacă acest șablon a accelerat fluxul de lucru de codare, luați în considerare sprijinul:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licență

Acest proiect este licențiat sub **Licența MIT**. Consultați fișierul [LICENSE](LICENSE) pentru mai multe informații.