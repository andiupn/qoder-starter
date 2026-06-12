#Qoder Starter🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <strong>Nederlands</strong>
</div>

<br />

<div align="center">
  <h3><strong>Een AI-agent zonder regels is slechts een chaotisch script.</strong></h3>
  <p><strong>Qoder Starter is een lichtgewicht, op AI gebaseerd regelsysteem dat is ontworpen om het gedrag van AI-agenten af te stemmen op de onberispelijke codeerconventies in Cursor, Gemini en Claude Code.</strong></p>

  <p>Stop met het verspillen van tokens, het lijden aan AI-hallucinaties en het worstelen met inconsistente codestijlen. Geef uw codeerassistent direct toegang tot vijf fundamentele regelbladen.</p>
</div>

> 📦 Gratis sjabloon van **andiupn** ([kuncimu.com](https://kuncimu.com)) · Gelicentieerd onder [MIT-licentie](LICENSE)  
> ☕ Indien nuttig, [koop een kopje koffie](https://ko-fi.com/andiupn) · 🚀 Heeft u geavanceerde monorepos, aangepaste agents en voorverpakt geheugen nodig? Probeer de [PRO-versie](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Het probleem: de chaos van AI-codeassistenten
AI-assistenten zijn ongelooflijk snel. Zonder vooraf geconfigureerde richtlijnen schrijven ze echter ongestructureerde code, negeren ze uw naamgevingsconventies, lekken ze geheimen en maken ze grillige git-commits die de geschiedenis van je repository verpesten.

---

## ⚡ De oplossing: de 5 fundamentele AI-regels

### 1. 📜 Code- en taalconventies
Houdt de taal helder (`bahasa.md`: Indonesisch voor chat, Engels voor code) en dwingt standaardopmaak af (`code-conventions.md`: pijlfuncties, TypeScript strict, JSDoc).

### 🔒 2. Geen hallucinatie-beveiliging
Bewaakt API-sleutels en inloggegevens, dwingt gegevensvalidatie (Zod) en XSS-preventieregels (`security.md`) af voordat code wordt geschreven.

### 🧠 3. Historisch kennissysteem
Configureert geheugenrichtlijnen (`memory-usage.md`) en git-conventies (`git-conventions.md`), zodat de AI-agent leert van de geschiedenis van uw repository, waarbij `/skills` wordt gebruikt om sessieontdekkingen op te slaan.

---

## 📊 LITE versus PRO: de premium-upgrade

| Wat je krijgt | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Fundamentele regels** | 5 | 14 (voegt toe: foutafhandeling, testen, stapelen, a11y, etc.) |
| **Gespecialiseerde douaneagenten** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, enz.) |
| **Geheugeninvoer (Generieke Seed)** | ❌ | 12 (Configuratieoplossingen voor Next.js, Toneelschrijver, Redis) |
| **DevOps- en MCP-configuraties** | ❌ | ✅ (`mcp.json` sjablonen) |
| **Upstream-updates** | Via GitHub | Via [GitHub-sponsors](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Bekijk de volledige functievergelijkings- en upgradehandleiding](COMPARISON.md)**

---

## 📂 Blauwdruk voor opslagplaats

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️Voorbeeld

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

## 🚀 Ga aan de slag in 3 stappen

### 1. Configuraties kopiëren:
Kopieer `.qoder/`, `.agent/`, `scripts/` en `AGENTS.md` naar de hoofdmap van uw project.

### 2. Omgeving configureren:

```bash
cp .env.example .env
```

### 3. Begin met coderen:
Open het project in Cursor of voer Claude Code uit. De AI-agent leest de regels automatisch!

---

## 💖 Steun dit project (donaties)

Als deze sjabloon uw codeerworkflow heeft versneld, kunt u overwegen het volgende te ondersteunen:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licentie

Dit project is gelicentieerd onder de **MIT-licentie**. Zie het bestand [LICENSE](LICENSE) voor meer informatie.