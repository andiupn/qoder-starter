---
trigger: always_on
---

<!--
  Scaffolded by Andi UPN (https://github.com/andiupn)
  Official Website & Support: https://kuncimu.com
  Licensed under MIT License
-->

> 📦 Free Template by **Andi UPN** ([kuncimu.com](https://kuncimu.com)) · Licensed under [MIT License](LICENSE)
# Security Guardrails

## Hard Rules (NEVER Violate)
1. **JANGAN pernah commit `.env`, credentials, atau API keys.** Selalu gunakan environment variables. File `.env*.local` sudah ada di `.gitignore` — pastikan tetap demikian.
2. **JANGAN hardcode secrets** di source code, bahkan untuk testing. Gunakan test fixtures atau mock values.
3. **JANGAN expose API keys** di Client Components. Semua secret harus di Server Components atau Server Actions.

## Input Validation (Zod)
Semua Server Actions **WAJIB** validasi input dengan Zod sebelum memproses data:

```typescript
import { z } from 'zod'

// Define schema terpisah (reusable di client & server)
const createItemSchema = z.object({
  name: z.string().min(1, 'Nama wajib diisi').max(100),
  description: z.string().max(500).optional(),
  quantity: z.number().int().positive('Jumlah harus positif'),
})

export async function createItem(formData: FormData) {
  const rawData = {
    name: formData.get('name'),
    description: formData.get('description') || undefined,
    quantity: Number(formData.get('quantity')),
  }

  const parsed = createItemSchema.safeParse(rawData)
  if (!parsed.success) {
    return { success: false as const, error: parsed.error.issues[0].message }
  }

  // Safe to use parsed.data here
  // ...
}
```

## XSS Prevention
- Gunakan React's built-in escaping (default behavior).
- **`dangerouslySetInnerHTML`** — HANYA gunakan jika benar-benar terpaksa, dan **WAJIB sanitize** dengan DOMPurify:
  ```tsx
  import DOMPurify from 'dompurify'
  <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userContent) }} />
  ```
- Jangan gunakan `eval()`, `Function()`, atau `innerHTML` langsung.

## Authentication
- Gunakan **NextAuth.js (Auth.js v5)** atau middleware-based auth.
- **JANGAN roll your own crypto** — gunakan `bcrypt` atau `argon2` untuk password hashing.
- **JANGAN store passwords** di plaintext atau dengan weak hashing (MD5, SHA1).
- Protect API routes dan Server Actions dengan auth checks.

## CSRF Protection
- Next.js Server Actions sudah include CSRF protection secara default.
- Untuk custom API routes, validasi `Origin` header atau gunakan CSRF tokens.

## Dependency Management
- Cek `npm audit` sebelum install package baru.
- Prefer packages dengan: >1000 weekly downloads, actively maintained, clear license.
- Jangan install package hanya untuk utility trivial yang bisa ditulis sendiri (misal: `is-odd`, `is-even`).
- Review `package-lock.json` changes di PR — perhatikan penambahan dependencies baru.

## Environment Variables
```bash
# .env.local (JANGAN commit)
# Add your environment variables here
# DATABASE_URL="your-database-url"
# API_SECRET="generate-with-openssl-rand-base64-32"

# .env.example (COMMIT ini — tanpa values)
DATABASE_URL=""
API_SECRET=""
```
