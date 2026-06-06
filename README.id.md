# Qoder Starter 🛰️

<div align="center">
  <a href="README.md">English</a> | <strong>Bahasa Indonesia</strong>
</div>

<br />

<div align="center">
  <h3><strong>AI agent tanpa aturan hanyalah skrip yang kacau.</strong></h3>
  <p><strong>Qoder Starter adalah sistem aturan ringan ramah-AI yang dirancang untuk menyelaraskan perilaku AI agent dengan konvensi kode yang bersih di Cursor, Gemini, dan Claude Code.</strong></p>

  <p>Hentikan pemborosan token, halusinasi AI yang berulang, dan gaya kode yang tidak konsisten. Berikan kekuatan instan pada asisten koding Anda dengan 5 berkas aturan fundamental.</p>
</div>

> 📦 Free template by **andiupn** ([kuncimu.com](https://kuncimu.com)) · Dilisensikan di bawah [MIT License](LICENSE)  
> ☕ Jika bermanfaat, [beli saya kopi](https://ko-fi.com/andiupn) · 🚀 Butuh monorepo canggih, agen khusus, dan memori bawaan? Coba [versi PRO](https://kuncimu.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Masalahnya: Kekacauan Asisten Kode AI Standar
Asisten AI bekerja dengan sangat cepat. Namun tanpa adanya panduan terkonfigurasi, mereka menulis kode yang tidak terstruktur, mengabaikan konvensi penamaan Anda, membocorkan kunci rahasia, dan membuat komit git berantakan yang merusak riwayat repositori.

---

## ⚡ Solusinya: 5 Aturan AI Fundamental

### 1. 📜 Konvensi Kode & Bahasa
Menjaga komunikasi tetap jelas (`bahasa.md`: Bahasa Indonesia untuk obrolan, Bahasa Inggris untuk kode) dan menegakkan format standar (`code-conventions.md`: arrow functions, TypeScript strict, JSDoc).

### 🔒 2. Keamanan Bebas Halusinasi
Menjaga kunci API dan kredensial, menegakkan validasi data (Zod) dan aturan pencegahan XSS (`security.md`) sebelum menulis kode apa pun.

### 🧠 3. Sistem Pengetahuan Historis
Mengonfigurasi panduan memori (`memory-usage.md`) dan konvensi git (`git-conventions.md`) agar AI agent belajar dari riwayat repositori Anda, menggunakan `/skills` untuk menyimpan penemuan sesi.

---

## 📊 LITE vs PRO: Upgrade Premium

| Fitur | 🆓 LITE (Starter) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Rules Fundamental** | 5 | 14 (tambah: error handling, testing, stack, a11y, dll.) |
| **Custom Agent Spesialis** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, dll.) |
| **Entri Memori Bawaan** | ❌ | 12 (perbaikan Next.js, Playwright, Redis) |
| **Konfigurasi DevOps & MCP** | ❌ | ✅ (templat `mcp.json`) |
| **Pembaruan Berkelanjutan** | Via GitHub | Via kuncimu.com |

👉 **[Lihat Perbandingan Fitur Lengkap & Panduan Upgrade](COMPARISON.md)**

---

## 📂 Struktur Repositori

```
your-workspace/
  .qoder/              # Aturan sistem untuk AI agent (bahasa, konvensi, keamanan)
  .agent/              # Konteks memori AI, entri, dan alur kerja
  scripts/             # Alat bantu Python (save-knowledge, sync-stats)
  AGENTS.md            # Instruksi sistem AI master (pintu masuk)
  .env.example         # Templat variabel lingkungan proyek
```

---

## 🚀 Memulai Cepat dalam 3 Langkah

### 1. Salin konfigurasi:
Salin folder `.qoder/`, `.agent/`, `scripts/`, dan file `AGENTS.md` ke direktori proyek Anda.

### 2. Konfigurasi lingkungan:
```bash
cp .env.example .env
```

### 3. Mulai Coding:
Buka proyek di Cursor atau jalankan Claude Code. AI agent akan membaca aturan secara otomatis!

---

## 💖 Dukung Proyek Ini (Donasi)

Jika templat starter ini membantu mempercepat alur kerja pengodean Anda, pertimbangkan untuk memberikan dukungan:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer (Indonesia):** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria (Indonesia):** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat berkas [LICENSE](LICENSE) file untuk informasi lebih lanjut.
