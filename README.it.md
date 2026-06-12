#Qoder Antipasto 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <strong>Italiano</strong> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  __HTML_43<strong>Un agente AI senza regole è solo uno script caotico.</strong></h3>
  <p><strong>Qoder Starter è un sistema di regole leggero, incentrato sull'intelligenza artificiale, progettato per allineare i comportamenti degli agenti IA con le convenzioni di codifica incontaminate in Cursor, Gemini e Claude Code.</strong></p>

  <p>Smetti di sprecare token, di soffrire di allucinazioni dell'intelligenza artificiale e di lottare con stili di codice incoerenti. Potenzia istantaneamente il tuo assistente di codifica con 5 fogli di regole fondamentali.</p>
</div>

> 📦 Modello gratuito di **andiupn** ([kuncimu.com](https://kuncimu.com)) · Concesso in licenza con [licenza MIT](LICENSE)  
> ☕ Se utile, [offrimi un caffè](https://ko-fi.com/andiupn) · 🚀 Hai bisogno di monorepos avanzati, agenti personalizzati e memoria preconfezionata? Prova la [versione PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Il problema: il caos degli assistenti di codice AI
Gli assistenti IA sono incredibilmente veloci. Tuttavia, senza linee guida preconfigurate, scrivono codice non strutturato, ignorano le convenzioni di denominazione, trapelano segreti ed effettuano commit git irregolari che rovinano la cronologia del repository.

---

## ⚡ La soluzione: le 5 regole fondamentali dell'IA

### 1. 📜 Convenzioni sul codice e sulla lingua
Mantiene la lingua chiara (`bahasa.md`: indonesiano per la chat, inglese per il codice) e applica la formattazione standard (`code-conventions.md`: funzioni freccia, TypeScript strict, JSDoc).

### 🔒 2. Sicurezza senza allucinazioni
Protegge le chiavi e le credenziali API, applicando la convalida dei dati (Zod) e le regole di prevenzione XSS (`security.md`) prima di scrivere qualsiasi codice.

### 🧠 3. Sistema della conoscenza storica
Configura le linee guida sulla memoria (`memory-usage.md`) e le convenzioni git (`git-conventions.md`) in modo che l'agente AI apprenda dalla cronologia del repository, utilizzando `/skills` per salvare le scoperte della sessione.

---

## 📊 LITE vs PRO: l'aggiornamento Premium

| Cosa ottieni | 🆓 LITE (Starter) | 💎PRO (Premium) |
|---|:---:|:---:|
| **Regole Fondamentali** | 5| 14 (aggiunge: gestione degli errori, testing, stack, a11y, ecc.) |
| **Agenti personalizzati specializzati** | ❌| 5 (`code-reviewer`, `nextjs-specialist`, ecc.) |
| **Voci di memoria (seme generico)** | ❌| 12 (correzioni di configurazione Next.js, Drammaturgo, Redis) |
| **Configurazioni DevOps e MCP** | ❌| ✅ (`mcp.json` modelli) |
| **Aggiornamenti a monte** | Tramite GitHub | Tramite [Sponsor GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Visualizza la guida completa al confronto delle funzionalità e all'aggiornamento](COMPARISON.md)**

---

## 📂 Progetto del repository

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Anteprima

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

## 🚀 Inizia in 3 passaggi

### 1. Copia configurazioni:
Copia `.qoder/`, `.agent/`, `scripts/` e `AGENTS.md` nella radice del progetto.

### 2. Configura l'ambiente:

```bash
cp .env.example .env
```

### 3. Inizia a scrivere codice:
Apri il progetto nel cursore o esegui Claude Code. L'agente AI leggerà le regole automaticamente!

---

## 💖 Sostieni questo progetto (donazioni)

Se questo modello ha accelerato il flusso di lavoro di codifica, valuta la possibilità di supportare:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licenza

Questo progetto è concesso in licenza con la **Licenza MIT**. Per ulteriori informazioni, consulta il file [LICENZA](LICENSE).