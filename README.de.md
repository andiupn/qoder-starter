# Qoder-Starter 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <strong>Deutsch</strong> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>Ein KI-Agent ohne Regeln ist nur ein chaotisches Skript.</strong></h3>
  <p><strong>Qoder Starter ist ein leichtes, AI-first-Regelsystem, das entwickelt wurde, um das Verhalten von KI-Agenten an makellose Codierungskonventionen in Cursor, Gemini und Claude Code anzupassen.</strong></p>

  <p>Verschwenden Sie keine Token mehr, leiden Sie nicht mehr unter KI-Halluzinationen und kämpfen Sie nicht mehr mit inkonsistenten Codestilen. Stärken Sie Ihren Codierungsassistenten sofort mit 5 grundlegenden Regelblättern.</p>
</div>

> 📦 Kostenlose Vorlage von **andiupn** ([kuncimu.com](https://kuncimu.com)) · Lizenziert unter [MIT-Lizenz](LICENSE)  
> ☕ Wenn es sinnvoll ist, [kaufen Sie mir einen Kaffee](https://ko-fi.com/andiupn) · 🚀 Benötigen Sie erweiterte Monorepos, benutzerdefinierte Agenten und vorgefertigten Speicher? Probieren Sie die [PRO-Version](https://github.com/sponsors/andiupn?frequency=monthly) aus.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Das Problem: Das Chaos der KI-Code-Assistenten
KI-Assistenten sind unglaublich schnell. Ohne vorkonfigurierte Richtlinien schreiben sie jedoch unstrukturierten Code, ignorieren Ihre Namenskonventionen, geben Geheimnisse preis und führen unregelmäßige Git-Commits durch, die Ihren Repository-Verlauf durcheinander bringen.

---

## ⚡ Die Lösung: Die 5 grundlegenden KI-Regeln

### 1. 📜 Code- und Sprachkonventionen
Hält die Sprache klar (`bahasa.md`: Indonesisch für Chat, Englisch für Code) und erzwingt die Standardformatierung (`code-conventions.md`: Pfeilfunktionen, TypeScript strikt, JSDoc).

### 🔒 2. Sicherheit ohne Halluzination
Schützt API-Schlüssel und Anmeldeinformationen und erzwingt die Datenvalidierung (Zod) und XSS-Verhinderungsregeln (`security.md`), bevor Code geschrieben wird.

### 🧠 3. Historisches Wissenssystem
Konfiguriert Speicherrichtlinien (`memory-usage.md`) und Git-Konventionen (`git-conventions.md`), damit der KI-Agent aus Ihrem Repository-Verlauf lernt und `/skills` zum Speichern von Sitzungserkennungen verwendet.

---

## 📊 LITE vs. PRO: Das Premium-Upgrade

| Was Sie bekommen | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Grundregeln** | 5 | 14 (fügt hinzu: Fehlerbehandlung, Tests, Stack, a11y usw.) |
| **Spezialisierte kundenspezifische Agenten** | ❌ | 5 (`code-reviewer`, `nextjs-specialist` usw.) |
| **Speichereinträge (generischer Seed)** | ❌ | 12 (Next.js-Konfigurationskorrekturen, Playwright, Redis) |
| **DevOps- und MCP-Konfigurationen** | ❌ | ✅ (`mcp.json` Vorlagen) |
| **Upstream-Updates** | Über GitHub | Über [GitHub-Sponsoren](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Vollständigen Funktionsvergleich und Upgrade-Leitfaden anzeigen](COMPARISON.md)**

---

## 📂 Repository-Blaupause

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Vorschau

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

## 🚀 Beginnen Sie in 3 Schritten

### 1. Konfigurationen kopieren:
Kopieren Sie `.qoder/`, `.agent/`, `scripts/` und `AGENTS.md` in Ihr Projektstammverzeichnis.

### 2. Umgebung konfigurieren:

```bash
cp .env.example .env
```

### 3. Beginnen Sie mit dem Codieren:
Öffnen Sie das Projekt in Cursor oder führen Sie Claude Code aus. Der KI-Agent liest die Regeln automatisch!

---

## 💖 Unterstützen Sie dieses Projekt (Spenden)

Wenn diese Vorlage Ihren Codierungsworkflow beschleunigt hat, sollten Sie Folgendes unterstützen:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Lizenz

Dieses Projekt ist unter der **MIT-Lizenz** lizenziert. Weitere Informationen finden Sie in der Datei [LICENSE](LICENSE).