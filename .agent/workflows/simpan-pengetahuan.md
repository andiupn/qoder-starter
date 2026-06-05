# Simpan Pengetahuan (Knowledge Save Workflow)

> Untuk Qoder AI Agent: Gunakan workflow ini untuk menyimpan pengetahuan dari Chat Session ke memory system.

---

## Langkah 1: Identifikasi Sumber

Baca instruksi user untuk menentukan sumber pengetahuan.

### Opsi A: Dari Chat Session
Jika user bilang "simpan dari chat", "save session", atau tidak menyebutkan folder spesifik.
→ **Lanjut ke Langkah 2A**

### Opsi B: Dari Topik Spesifik
Jika user bilang "simpan pattern ini" atau menunjuk ke solusi tertentu.
→ **Lanjut ke Langkah 2B**

---

## Langkah 2A: Scan Chat Session

Analisis seluruh chat session ini dan identifikasi pengetahuan penting:
1. **Scan:** Cari bug fixes, code patterns, architecture decisions, atau research findings.
2. **Filter:** Abaikan informasi yang sudah ada di `.agent/memory/entries/` (cek dulu dengan `Grep`).
3. **Prioritaskan:** Bug solutions > Code patterns > Architecture decisions > Context info.

## Langkah 2B: Extract dari Topik Spesifik

Ambil knowledge dari bagian percakapan yang ditunjuk user:
1. Identifikasi inti pengetahuan (problem + solution).
2. Tentukan kategori yang tepat.
3. Cek duplikasi di memory entries yang ada.

---

## Langkah 3: Format & Simpan

### Kategori
| Kategori | Kapan Digunakan |
|----------|----------------|
| `gotchas` | Bug unik, error, dan solusinya |
| `patterns` | Pola kode atau logika yang reusable |
| `decisions` | Keputusan arsitektur atau pemilihan library |
| `context` | Informasi lingkungan pengembangan |

### Format Entry
```markdown
# [Judul Deskriptif]
**Category:** [gotchas/patterns/decisions/context]
**Severity:** [CRITICAL / MEDIUM / INFO]
**Tags:** [nextjs, tailwind, typescript, drizzle, mcp]
**Date:** YYYY-MM-DD
**Source:** Chat session

---
## Problem / Context
[Deskripsi masalah atau konteks]

---
## Solution / Pattern
[Solusi atau pola kode dengan contoh jika relevan]
```

### Naming Rules
- **WAJIB:** kebab-case deskriptif (contoh: `nextjs-hydration-fix.md`).
- **DILARANG:** ID acak atau timestamp (contoh: `entry-001.md`, `entry-091413.md`).
- **Max length:** 80 karakter untuk nama file.

### Simpan
Gunakan `Write` tool Qoder untuk menulis file langsung ke kategori yang sesuai:
```
Write(".agent/memory/entries/gotchas/nama-file.md", content)
```

Atau gunakan script:
```bash
python scripts/save-knowledge.py --category gotchas --file content.md
```

---

## Langkah 4: Sync Stats

Setelah menyimpan, jalankan:
```bash
python scripts/sync-agents-stats.py
```

Ini akan update knowledge stats di `AGENTS.md`.

---

## Project Context
- **Memory Root:** `.agent/memory/entries/`
- **Active Categories:** gotchas, patterns, decisions, context.
