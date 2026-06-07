# LITE vs PRO Comparison — Qoder Edition

> Bingung memilih versi mana? Berikut perbandingan fitur lengkap antara edisi LITE (Starter) dan PRO (Premium Workspace).

## TL;DR

- **LITE / Starter (Gratis):** Cocok untuk proyek sederhana atau perorangan. Menyertakan 5 rules fundamental untuk AI agent, 1 workflow, 2 skrip, dan lisensi open-source MIT.
- **PRO / Premium (Berbayar $1–$5):** Ditujukan untuk pengembang profesional, freelancer, dan agensi. Menyertakan 14 rules lengkap, 5 agen AI spesialis kustom, 12 entri memori bawaan (gotchas, patterns, decisions), templat konfigurasi MCP, dan lisensi komersial.

---

## Feature Matrix

| Fitur | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Fundamental Rules** | 5 | 10 |
| `bahasa.md` (Language Strategy) | ✅ | ✅ |
| `code-conventions.md` (Formatting/TS) | ✅ | ✅ |
| `git-conventions.md` (Git/Conventional) | ✅ | ✅ |
| `security.md` (Zod/Secrets/MCP) | ✅ | ✅ |
| `memory-usage.md` (AI Memory flow) | ✅ | ✅ |
| `error-handling.md` (API errors/boundaries) | ❌ | ✅ |
| `testing.md` (Vitest/Playwright guide) | ❌ | ✅ |
| `nextjs-stack.md` (Tailwind v4/Drizzle stack) | ❌ | ✅ |
| `mcp-tools.md` (Cross-platform MCP guide) | ❌ | ✅ |
| `qoder-workflow.md` (Expert pipeline mode) | ❌ | ✅ |
| | | |
| **Custom Agent Templates** | 0 | 5 |
| `code-reviewer.md` (QA reviews) | ❌ | ✅ |
| `nextjs-specialist.md` (React 19/Server Actions) | ❌ | ✅ |
| `drizzle-specialist.md` (Migrations/Queries) | ❌ | ✅ |
| `planning-specialist.md` (Architecture/Decomp) | ❌ | ✅ |
| `testing-specialist.md` (Mock strategies) | ❌ | ✅ |
| | | |
| **Workflows Reference** | 1 | 1 |
| `simpan-pengetahuan.md` (Knowledge save) | ✅ | ✅ |
| | | |
| **Memory Entries (Generic Seed)** | 0 | 11 |
| Gotchas (Next.js config conflicts, Node resolution) | ❌ | ✅ (4 gotchas) |
| Patterns (API fetch, Playwright, Redis MCP tools) | ❌ | ✅ (5 patterns) |
| Decisions (Memory naming, baseUrl config) | ❌ | ✅ (2 decisions) |
| | | |
| **DevOps & MCP Config** | ❌ | ✅ |
| `mcp.json` config template | ❌ | ✅ |
| | | |
| **Lisensi & Dukungan** | MIT License | Proprietary Commercial |
| Redistribution allowed | ✅ | ❌ |
| Komersial (proyek klien & internal) | ✅ | ✅ |
| Dukungan Email | Best-effort (Komunitas) | Best-effort (No SLA - Prioritas Tinggi) |
| Pembaruan Berkelanjutan | Via GitHub | Via [GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly) |

---

## When to Choose Which?

### Pilih **LITE (Starter)** jika:
- ✅ Anda baru mulai mempelajari orkestrasi AI Agent rules.
- ✅ Proyek Anda adalah single-project sederhana (1 aplikasi saja).
- ✅ Anda ingin membuat fork komunitas gratis dan open-source.
- ✅ Anda ingin menggunakan rules dasar secara gratis terlebih dahulu.

### Pilih **PRO (Premium)** jika:
- ✅ Anda mengelola banyak proyek aktif untuk klien atau internal (Agensi / Freelancer).
- ✅ Anda membutuhkan state-management pengetahuan (Riset, Rencana, Memory) yang terintegrasi.
- ✅ Anda ingin meningkatkan kecepatan pengerjaan dengan 12 seed memory dan 5 custom agents.
- ✅ Anda ingin mendukung pemeliharaan berkelanjutan dari proyek ini.

---

## Upgrade Path

Jika Anda sudah menggunakan versi LITE dan ingin beralih ke PRO:

1. Dapatkan lisensi resmi versi PRO di **[GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly)**.
2. Unduh berkas repositori `qoder-pro`.
3. Salin folder `.qoder/` dan file `mcp.json` versi PRO ke root project Anda.
4. Nikmati rules dan agents spesialis lengkap!

---

## Hubungi Kami

- **Pertanyaan Umum / Masalah:** Silakan buat Issue di GitHub [github.com/andiupn](https://github.com/andiupn).
- **Pertanyaan Pra-Penjualan PRO:** Hubungi kami melalui email di **andi.upn@gmail.com**.

👉 **[Dapatkan Edisi PRO di GitHub Sponsors](https://github.com/sponsors/andiupn?frequency=monthly)**
