---
trigger: always_on
---
# Bahasa & Komunikasi

## Komunikasi AI ↔ User
- Selalu gunakan **Bahasa Indonesia** untuk berkomunikasi dengan user dan menjelaskan sesuatu.
- Dokumentasi eksternal (README, laporan, changelog) ditulis dalam Bahasa Indonesia.

## Kode & Teknis
- Nama variabel, fungsi, class, interface, type = **English** (camelCase/PascalCase).
- Komentar inline di dalam kode = **English**.
- Commit message, PR description, branch name = **English** (Conventional Commits format).

## Error Messages
- User-facing error messages = **Bahasa Indonesia**, informatif, tanpa jargon teknis.
  - Contoh: "Gagal menyimpan data. Silakan coba lagi." bukan "Error 500: Internal Server Error".
- Developer-facing logs = **English** untuk kemudahan debugging dan searching.

## Exception
- Jika user beralih ke English di tengah session, agent mengikuti bahasa user.
- Jika user secara eksplisit meminta English, gunakan English untuk session tersebut.
