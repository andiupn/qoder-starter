---
trigger: always_on
---
# Code Conventions

## Formatting
- **Indentation:** 2 spaces (no tabs).
- **Quotes:** Single quotes untuk string di TypeScript/JavaScript.
- **Semicolons:** Always use semicolons.
- **Trailing comma:** Selalu gunakan trailing comma di objects, arrays, dan function parameters.
- **Max line length:** 100 characters. Wrap jika melebihi.
- **`const` > `let`:** Selalu gunakan `const` kecuali variable memang perlu di-reassign. Jangan gunakan `var`.

## React Components
- **Arrow functions** untuk semua component definitions.
- **JSDoc comments** untuk component dan props (minimal deskripsi + param types).
- **Default export** untuk page-level components. Named export untuk utility components yang di-reuse.
- **Interface** untuk props (bukan type alias). Prefix dengan component name: `UserCardProps`.

### Server Component (Default)
```tsx
import { db } from '@/lib/db'

/**
 * Displays a list of items from the database.
 * Server Component — data fetching happens on the server.
 */
const ItemList = async () => {
  const items = await db.select().from(itemTable).limit(10)

  return (
    <ul className="flex flex-col gap-2">
      {items.map((item) => (
        <li key={item.id} className="rounded-lg border p-4">
          {item.name}
        </li>
      ))}
    </ul>
  )
}

export default ItemList
```

### Client Component (Only when needed)
```tsx
'use client'

import { useState } from 'react'

interface CounterProps {
  /** Initial count value */
  initialCount: number
}

/**
 * An interactive counter button.
 * Client Component — requires useState for interactivity.
 */
const Counter = ({ initialCount }: CounterProps) => {
  const [count, setCount] = useState(initialCount)

  return (
    <button
      className="rounded-lg bg-blue-500 px-4 py-2 text-white"
      onClick={() => setCount((prev) => prev + 1)}
    >
      Count: {count}
    </button>
  )
}

export default Counter
```

## Server vs Client Component
- **Default ke Server Component.** Hanya tambahkan `'use client'` jika komponen membutuhkan:
  - Hooks (`useState`, `useEffect`, `useReducer`, dll)
  - Event handlers (`onClick`, `onChange`, dll)
  - Browser APIs (`window`, `localStorage`, dll)
  - Class components
- **Server Actions** untuk data mutations — jangan buat API route hanya untuk CRUD sederhana.

## Import Ordering
Urutkan imports dengan blank line sebagai separator:
```tsx
// 1. React & Next.js
import { useState } from 'react'
import Link from 'next/link'

// 2. Third-party libraries
import { z } from 'zod'
import { clsx } from 'clsx'

// 3. Internal lib/utils
import { db } from '@/lib/db'
import { formatDate } from '@/lib/utils'

// 4. Components
import { Button } from '@/components/ui/button'
import { UserCard } from '@/components/user-card'

// 5. Types (type-only imports)
import type { Item } from '@/types'

// 6. Styles (jika ada CSS modules)
import styles from './page.module.css'
```

## Naming Conventions
| Element | Convention | Contoh |
|---------|-----------|--------|
| Component files | PascalCase | `UserCard.tsx` |
| Non-component files | kebab-case | `api-helpers.ts`, `date-utils.ts` |
| Variables/functions | camelCase | `getUserName`, `isLoading` |
| Types/Interfaces | PascalCase | `UserProfile`, `ItemData` |
| Constants | UPPER_SNAKE | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| Folders | kebab-case | `user-profile/`, `api-helpers/` |

## TypeScript Strict Mode
- **No `any`** kecuali absolutely necessary — jika terpaksa, tambahkan comment `// eslint-disable-next-line @typescript-eslint/no-explicit-any` dengan alasan.
- **Explicit return types** untuk semua exported functions.
- **Strict null checks** — handle `null` dan `undefined` secara eksplisit.
- Gunakan **type narrowing** (`if`, `in`, `instanceof`) daripada type assertions (`as`).

## CSS Framework
> **Note:** Adjust this section for your CSS framework (Tailwind CSS, UnoCSS, vanilla CSS, etc.)

### Tailwind CSS v4 (Default)
- **Utility-first** — gunakan utility classes, bukan custom CSS.
- **No arbitrary values** (`w-[347px]`) kecuali benar-benar terpaksa.
- **Class ordering:** layout → flex/grid → spacing → sizing → typography → visual → misc.
- Gunakan `clsx` atau `tailwind-merge` untuk conditional classes.
- Di Tailwind v4, `@theme` block menggantikan `tailwind.config.ts` untuk custom values.

```tsx
// Good: logical class ordering
<div className="flex flex-col gap-4 p-6 w-full max-w-lg rounded-xl bg-white shadow-md">

// Bad: random ordering
<div className="bg-white p-6 flex shadow-md rounded-xl w-full gap-4 max-w-lg flex-col">
```
