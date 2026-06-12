#Qoder Démarreur 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <strong>Français</strong> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>Un agent IA sans règles n'est qu'un script chaotique.</strong></h3>
  <p><strong>Qoder Starter est un système de règles léger, axé sur l'IA, conçu pour aligner les comportements des agents IA avec les conventions de codage vierges dans Cursor, Gemini et Claude Code.</strong></p>

  <p>Arrêtez de gaspiller des jetons, de souffrir d'hallucinations de l'IA et de lutter avec des styles de code incohérents. Alimentez instantanément votre assistant de codage avec 5 feuilles de règles fondamentales.</p>
</div>

> 📦 Modèle gratuit par **andiupn** ([kuncimu.com](https://kuncimu.com)) · Sous licence [Licence MIT](LICENSE)  
> ☕ Si cela est utile, [achetez-moi un café](https://ko-fi.com/andiupn) · 🚀 Besoin de monorepos avancés, d'agents personnalisés et de mémoire préemballée ? Essayez la [version PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Le problème : le chaos des assistants de code IA
Les assistants IA sont incroyablement rapides. Cependant, sans directives préconfigurées, ils écrivent du code non structuré, ignorent vos conventions de dénomination, divulguent des secrets et effectuent des commits git erratiques qui gâchent l'historique de votre référentiel.

---

## ⚡ La solution : les 5 règles fondamentales de l'IA

### 1. 📜 Conventions de code et de langage
Maintient un langage clair (`bahasa.md` : indonésien pour le chat, anglais pour le code) et applique un formatage standard (`code-conventions.md` : fonctions fléchées, TypeScript strict, JSDoc).

### 🔒 2. Sécurité sans hallucination
Protège les clés et les informations d'identification API, en appliquant la validation des données (Zod) et les règles de prévention XSS (`security.md`) avant d'écrire du code.

### 🧠 3. Système de connaissances historiques
Configure les directives de mémoire (`memory-usage.md`) et les conventions git (`git-conventions.md`) afin que l'agent AI apprenne de l'historique de votre référentiel, en utilisant `/skills` pour enregistrer les découvertes de session.

---

## 📊 LITE vs PRO : la mise à niveau Premium

| Ce que vous obtenez | 🆓 LITE (Démarreur) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Règles fondamentales** | 5 | 14 (ajoute : gestion des erreurs, tests, pile, a11y, etc.) |
| **Agents personnalisés spécialisés** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, etc.) |
| **Entrées mémoire (graines génériques)** | ❌ | 12 (correctifs de configuration Next.js, Playwright, Redis) |
| **Configurations DevOps et MCP** | ❌ | ✅ (modèles `mcp.json`) |
| **Mises à jour en amont** | ViaGitHub | Via [Sponsors GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Voir la comparaison complète des fonctionnalités et le guide de mise à niveau](COMPARISON.md)**

---

## 📂 Plan du référentiel

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Aperçu

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

## 🚀 Commencez en 3 étapes

### 1. Copiez les configurations :
Copiez les `.qoder/`, `.agent/`, `scripts/` et `AGENTS.md` à la racine de votre projet.

### 2. Configurez l'environnement :

```bash
cp .env.example .env
```

### 3. Commencez à coder :
Ouvrez le projet dans Cursor ou exécutez Claude Code. L'agent IA lira les règles automatiquement !

---

## 💖 Soutenez ce projet (Dons)

Si ce modèle a accéléré votre flux de travail de codage, envisagez de prendre en charge :
- **Ko-fi :** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon :** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer :** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria :** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licence

Ce projet est sous licence **MIT License**. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.