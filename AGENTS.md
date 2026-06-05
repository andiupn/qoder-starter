# Qoder Starter — AI Agent Rules
<!--
  Scaffolded by Andi UPN (https://github.com/andiupn)
  Official Website & Support: https://kuncimu.com
  Licensed under MIT License
-->

> 📦 Free Template by **Andi UPN** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)

Template starter untuk AI agent rules system. Cocok untuk project baru yang ingin menggunakan AI agent rules secara sederhana.

## Quick Start

1. **Copy** folder `.qoder/`, `.agent/`, dan `scripts/` ke root project Anda.
2. **Sesuaikan** rules di `.qoder/rules/` sesuai kebutuhan project.
3. **Mulai coding** — AI agent akan otomatis mengikuti rules yang ada.

## Memory Structure
- `.agent/memory/entries/context/` — Project environment and tech stack details.
- `.agent/memory/entries/gotchas/` — Known bugs, limitations, and their solutions.
- `.agent/memory/entries/patterns/` — Reusable code patterns and best practices.
- `.agent/memory/entries/decisions/` — Architecture and technology choices.

## Knowledge Stats
Total Knowledge Entries: 0

| Category | Count |
|----------|-------|
| Gotchas | 0 |
| Patterns | 0 |
| Decisions | 0 |
| Context | 0 |

---

## Instructions for Qoder Agent

### 1. Memory-First
Always check memory directories (via `Glob` and `Grep`) and this `AGENTS.md` before starting new tasks. Leverage historical knowledge to avoid repeating mistakes.

### 2. Learn & Save
If you solve a new complex problem, offer to save the knowledge using the `simpan-pengetahuan` workflow. Run `python scripts/sync-agents-stats.py` after every memory change.

### 3. Consistency
Follow all rules in `.qoder/rules/`. Key rules:
- **Language:** Bahasa Indonesia for communication, English for code (see `bahasa.md`).
- **Code style:** Arrow functions, JSDoc, TypeScript strict (see `code-conventions.md`).
- **Security:** Input validation, no hardcoded secrets (see `security.md`).

---

## Technical Guardrails
- **Indentation:** 2 spaces (see `code-conventions.md`).
- **React:** Server Components by default. `'use client'` only when needed.
- **Validation:** Zod for all Server Action inputs.
- **Testing:** Vitest (unit) + Playwright (E2E).

---

## Rules Reference
All rules are in `.qoder/rules/` with `trigger: always_on`:

| Rule File | Purpose |
|-----------|---------|
| `bahasa.md` | Language: ID for communication, EN for code |
| `code-conventions.md` | Formatting, components, TypeScript, CSS |
| `git-conventions.md` | Conventional Commits, branching |
| `memory-usage.md` | Memory-first workflow, knowledge capture |
| `security.md` | Input validation, XSS, secrets |

---

## Workflows Reference

| Workflow | File | Purpose |
|----------|------|---------|
| Simpan Pengetahuan | `simpan-pengetahuan.md` | Save knowledge from chat sessions to memory |

---

## License
MIT — Free to use, modify, and distribute.
