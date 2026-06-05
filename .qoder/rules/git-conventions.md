---
trigger: always_on
---
# Git Conventions

## Commit Message Format
Gunakan **Conventional Commits** — format standar internasional:

```
<type>(<scope>): <description>

[optional body]
```

| Type | Kapan Digunakan |
|------|----------------|
| `feat` | Fitur baru |
| `fix` | Bug fix |
| `docs` | Dokumentasi saja |
| `refactor` | Code change tanpa fitur/fix baru |
| `test` | Menambah atau memperbaiki test |
| `chore` | Maintenance (deps, config, scripts) |
| `perf` | Performance improvement |
| `style` | Formatting, whitespace (no logic change) |

**Contoh:**
```
feat(auth): add login page component
fix(hydration): resolve mismatch in UserCard server/client render
docs: update README with setup instructions
refactor(db): simplify schema definitions
test(actions): add validation tests for createItem
chore(deps): upgrade next.js to latest
```

**Bahasa commit message: English** (standar internasional).

## Branching Strategy
| Branch | Purpose |
|--------|---------|
| `main` | Production-ready, stable |
| `dev` | Development, integration |
| `feat/nama-fitur` | New feature |
| `fix/nama-bug` | Bug fix |
| `refactor/nama-refactor` | Refactoring |
| `chore/nama-chore` | Maintenance tasks |

Branch name: lowercase, kebab-case, descriptive.

## Pull Request Requirements
- **Deskripsi:** What changed + why (bukan hanya what).
- **Screenshot:** Wajib jika ada perubahan UI.
- **Link issue:** Jika PR terkait issue tertentu.
- **Self-review:** Baca diff sendiri sebelum submit PR.

## Pre-Commit Checklist
- [ ] `npm run lint` passes
- [ ] `npm run build` succeeds
- [ ] No uncommitted `.env` files
- [ ] No `console.log` yang tidak perlu di production code
- [ ] Tests pass (jika ada)

## Jangan Commit
File-file berikut sudah ada di `.gitignore` — pastikan tetap demikian:
- `node_modules/`
- `.env*.local`
- `*.tsbuildinfo`
- `.next/`
- `.DS_Store`
- `coverage/`
- `out/`

## Merge Strategy
- Prefer **squash merge** untuk feature branches (clean history).
- Use **regular merge** untuk long-lived branches (dev → main).
- JANGAN force push ke `main` atau `dev`.
