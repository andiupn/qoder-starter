---
trigger: always_on
---

<!--
  Scaffolded by Andi UPN (https://github.com/andiupn)
  Official Website & Support: https://kuncimu.com
  Licensed under MIT License
-->

> 📦 Free Template by **Andi UPN** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)
# Memory Usage & Knowledge Management

## Memory-First Workflow
Sebelum memulai tugas baru:
1. **Baca `AGENTS.md`** — entry point yang berisi stats, instruksi, dan workflow references.
2. **Scan memory entries** — gunakan `Glob` untuk melihat file yang ada:
   ```
   .agent/memory/entries/**/*.md
   ```
3. **Search relevant entries** — gunakan `Grep` untuk cari topik spesifik:
   ```
   Grep pattern: "keyword" di path .agent/memory/entries/
   ```
4. **Read entries** — gunakan `Read` untuk baca file yang relevan.

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `.agent/memory/entries/` | Knowledge entries (gotchas, patterns, decisions, context) |
| `.agent/workflows/` | Reusable agent workflows (e.g., `simpan-pengetahuan.md`) |

## Kategori Aktif (4 kategori)

| Kategori | Purpose | Contoh |
|----------|---------|--------|
| `gotchas` | Bug unik, gotchas, dan solusinya | Next.js hydration mismatch, Tailwind v4 PostCSS |
| `patterns` | Pola kode dan best practices reusable | Query patterns, Server Action validation |
| `decisions` | Keputusan arsitektur dan pemilihan tech | Tech stack choice, naming conventions |
| `context` | Informasi lingkungan dan setup proyek | Tech stack versions, MCP capabilities |

## Qoder Tools untuk Memory Access

| Task | Tool | Example |
|------|------|---------|
| Cari file memory | `Glob` | `Glob(".agent/memory/entries/**/*.md")` |
| Cari konten spesifik | `Grep` | `Grep("drizzle", ".agent/memory/entries/")` |
| Baca file | `Read` | `Read(".agent/memory/entries/gotchas/typescript-node-types.md")` |
| Tulis entry baru | `Write` | `Write(".agent/memory/entries/patterns/new-pattern.md", content)` |

## Knowledge Capture Rules
- **Setelah solve bug/pattern baru:** Tawarkan user untuk menyimpan ke memory.
- **Ekstraksi Maksimal:** Tangkap solusi bug, pola kode baru, atau hasil riset teknologi.
- **Naming:** WAJIB kebab-case deskriptif. DILARANG pakai ID acak atau timestamp.
  - Good: `nextjs-hydration-fix.md`, `drizzle-query-optimization.md`
  - Bad: `entry-001.md`, `entry-091413.md`
- **Frontmatter wajib ada:**
  ```markdown
  # Judul Deskriptif
  **Category:** gotchas|patterns|decisions|context
  **Severity:** CRITICAL | MEDIUM | INFO
  **Tags:** [nextjs, tailwind, typescript]
  **Date:** YYYY-MM-DD
  **Source:** Chat session | Research | Documentation

  ---
  ## Problem / Context
  [Deskripsi masalah atau konteks]

  ---
  ## Solution / Pattern
  [Solusi atau pola kode]
  ```
- **Severity format:** Use plain text only (`CRITICAL`, `MEDIUM`, `INFO`). Do NOT use emoji markers (e.g., ~~🚨 CRITICAL~~).

## Quality Standards for Memory Entries
- **Minimum content:** Every entry must have Problem/Context + Solution/Pattern sections with meaningful content.
- **No one-liners:** Single-sentence entries should be expanded with code examples, context, or links.
- **No duplicates:** Check existing entries before creating new ones. Merge related entries when appropriate.
- **Code examples:** Include working code snippets whenever possible (especially for `patterns` and `gotchas`).

## Auto-Sync
Setelah setiap perubahan memory (tambah, hapus, rename), **otomatis jalankan**:
```bash
python scripts/sync-agents-stats.py
```
Ini akan update statistik di `AGENTS.md`.

## Encoding
Semua file markdown menggunakan encoding **UTF-8**.
