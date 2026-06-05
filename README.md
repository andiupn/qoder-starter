# Qoder Starter

Template AI agent rules yang ringan dan mudah digunakan untuk project baru.

## Apa Ini?

Qoder Starter adalah **subset dari Qoder Pro** yang berisi 5 rules fundamental untuk AI agent. Cocok untuk developer yang ingin menggunakan AI agent rules secara sederhana tanpa setup yang kompleks.

## Yang Termasuk

| Komponen | Jumlah | Deskripsi |
|----------|--------|-----------|
| Rules | 5 | Bahasa, code conventions, git, security, memory |
| Workflows | 1 | Simpan pengetahuan (knowledge save) |
| Scripts | 2 | Sync stats + save knowledge |
| Memory entries | 0 | Struktur kosong, siap diisi |

### Rules yang Termasuk

1. **bahasa.md** — Konvensi bahasa (ID untuk komunikasi, EN untuk kode)
2. **code-conventions.md** — Format kode, naming, TypeScript, React components
3. **git-conventions.md** — Conventional Commits, branching strategy
4. **security.md** — Input validation (Zod), XSS prevention, secrets management
5. **memory-usage.md** — Sistem memory dan knowledge management

## Quick Setup

### Opsi 1: Copy Manual
```bash
# Copy folder-file ini ke root project Anda
cp -r .qoder/ /path/to/your-project/
cp -r .agent/ /path/to/your-project/
cp -r scripts/ /path/to/your-project/
cp AGENTS.md /path/to/your-project/
```

### Opsi 2: Clone sebagai Template
```bash
# Clone repo ini
git clone https://github.com/yourusername/qoder-starter.git my-project
cd my-project
# Mulai develop!
```

## Kustomisasi

### Menambah Rule Baru
Buat file `.md` baru di `.qoder/rules/` dengan format:
```markdown
---
trigger: always_on
---
# Nama Rule

## Deskripsi
...
```

### Mengisi Memory
Tambahkan file `.md` ke kategori yang sesuai di `.agent/memory/entries/`:
- `gotchas/` — Bug unik dan solusinya
- `patterns/` — Pola kode reusable
- `decisions/` — Keputusan arsitektur
- `context/` — Informasi lingkungan

Setelah menambah memory, jalankan:
```bash
python scripts/sync-agents-stats.py
```

### Mengubah `project-context.json`
Edit `.agent/context/project-context.json` untuk menambahkan info project Anda (stack, struktur, dll).

## Upgrade ke Pro

Ingin rules yang lebih lengkap? Upgrade ke **Qoder Pro** yang mencakup:
- 10 rules (error handling, testing, MCP tools, Next.js stack, dll)
- 5 custom AI agent templates (code reviewer, Next.js specialist, dll)
- 13 generic memory entries (gotchas & patterns yang umum digunakan)
- Project setup skill
- MCP configuration template

## Lisensi

MIT — Bebas digunakan, dimodifikasi, dan didistribusikan.
