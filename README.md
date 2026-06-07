# Qoder Starter 🛰️

<div align="center">
  <strong>English</strong> | <a href="README.id.md">Bahasa Indonesia</a>
</div>

<br />

<div align="center">
  <h3><strong>An AI agent without rules is just a chaotic script.</strong></h3>
  <p><strong>Qoder Starter is a lightweight, AI-first rules system designed to align AI agent behaviors with pristine coding conventions in Cursor, Gemini, and Claude Code.</strong></p>

  <p>Stop wasting tokens, suffering from AI hallucinations, and struggling with inconsistent code styles. Power your coding assistant with 5 fundamental rule sheets instantly.</p>
</div>

> 📦 Free template by **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)  
> ☕ If useful, [buy me a coffee](https://ko-fi.com/andiupn) · 🚀 Need advanced monorepos, custom agents, and pre-packaged memory? Try the [PRO version](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 The Problem: The Chaos of AI Code Assistants
AI assistants are incredibly fast. However, without pre-configured guidelines, they write unstructured code, ignore your naming conventions, leak secrets, and make erratic git commits that mess up your repository history.

---

## ⚡ The Solution: The 5 Fundamental AI Rules

### 1. 📜 Code & Language Conventions
Keeps language clear (`bahasa.md`: Indonesian for chat, English for code) and enforces standard formatting (`code-conventions.md`: arrow functions, TypeScript strict, JSDoc).

### 🔒 2. Zero-Hallucination Security
Guards API keys and credentials, enforcing data validation (Zod) and XSS prevention rules (`security.md`) before writing any code.

### 🧠 3. Historical Knowledge System
Configures memory guidelines (`memory-usage.md`) and git conventions (`git-conventions.md`) so the AI agent learns from your repository history, using `/skills` to save session discoveries.

---

## 📊 LITE vs PRO: The Premium Upgrade

| What You Get | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Fundamental Rules** | 5 | 14 (adds: error handling, testing, stack, a11y, etc.) |
| **Specialized Custom Agents** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, etc.) |
| **Memory Entries (Generic Seed)** | ❌ | 12 (Next.js config fixes, Playwright, Redis) |
| **DevOps & MCP Configurations** | ❌ | ✅ (`mcp.json` templates) |
| **Upstream Updates** | Via GitHub | Via [GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[View Full Feature Comparison & Upgrade Guide](COMPARISON.md)**

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

## 🖼️ Preview

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

## 🚀 Get Started in 3 Steps

### 1. Copy configurations:
Copy the `.qoder/`, `.agent/`, `scripts/`, and `AGENTS.md` to your project root.

### 2. Configure environment:
```bash
cp .env.example .env
```

### 3. Start Coding:
Open the project in Cursor or run Claude Code. The AI agent will read the rules automatically!

---

## 💖 Support This Project (Donations)

If this template has accelerated your coding workflow, consider supporting:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.
