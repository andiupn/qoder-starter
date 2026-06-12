# Qoder Starter 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <strong>Українська</strong> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>

<br />

<div align="center">
  <h3><strong>Агент ШІ без правил — це просто хаотичний сценарій.</strong></h3>
  <p><strong>Qoder Starter — це легка система правил на основі штучного інтелекту, розроблена для узгодження поведінки агентів штучного інтелекту з незмінними умовами кодування в Cursor, Gemini та Claude Code.</strong></p>

  <p>Припиніть витрачати токени, страждати від галюцинацій ШІ та боротися з непослідовними стилями коду. Миттєво наповніть свого помічника кодування 5 основними правилами.</p>
</div>

> 📦 Безкоштовний шаблон від **andiupn** ([kuncimu.com](https://kuncimu.com)) · Ліцензовано відповідно до [ліцензії MIT](LICENSE)  
> ☕ Якщо це корисно, [пригости мене кавою](https://ko-fi.com/andiupn) · 🚀 Потрібні розширені монорепозиторії, користувацькі агенти та готова пам’ять? Спробуйте [PRO версію](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Проблема: хаос помічників коду AI
ШІ-помічники неймовірно швидкі. Однак без попередньо налаштованих інструкцій вони пишуть неструктурований код, ігнорують ваші угоди про іменування, витікають секрети та роблять помилкові git-коміти, які псують історію вашого сховища.

---

## ⚡ Рішення: 5 фундаментальних правил ШІ

### 1. 📜 Код і мова
Зберігає чіткість мови (`bahasa.md`: індонезійська для чату, англійська для коду) і забезпечує стандартне форматування (`code-conventions.md`: функції стрілок, TypeScript strict, JSDoc).

### 🔒 2. Безпека без галюцинацій
Охороняє ключі та облікові дані API, примусову перевірку даних (Zod) і правила запобігання XSS (`security.md`) перед написанням будь-якого коду.

### 🧠 3. Система історичних знань
Налаштовує вказівки щодо пам’яті (`memory-usage.md`) та угоди git (`git-conventions.md`), щоб агент штучного інтелекту навчався з історії вашого сховища, використовуючи `/skills` для збереження відкриттів сеансів.

---

## 📊 LITE vs PRO: преміум-оновлення

| Що ви отримуєте | 🆓 LITE (початковий) | 💎 PRO (Преміум) |
|---|:---:|:---:|
| **Основні правила** | 5 | 14 (додає: обробку помилок, тестування, стек, a11y тощо) |
| **Спеціалізовані митні агенти** | ❌ | 5 (`code-reviewer`, `nextjs-specialist` тощо) |
| **Записи пам’яті (загальне початкове значення)** | ❌ | 12 (виправлення конфігурації Next.js, Playwright, Redis) |
| **Конфігурації DevOps і MCP** | ❌ | ✅ (`mcp.json` шаблони) |
| **Оновлення вгору** | Через GitHub | Через [Спонсорів GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Переглянути повний посібник із порівняння функцій і оновлення](COMPARISON.md)**

---

## 📂 Проект сховища

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Попередній перегляд

<p align="center">
  <img src="assets/screenshots/starter-rules-overview.png" alt="Qoder Starter Rules Overview" width="600"/>
</p>

<p align="center">
  <img src="assets/screenshots/comparison-starter-vs-pro.png" alt="Starter vs PRO Comparison" width="600"/>
</p>

<p align="center">
  <img src="assets/screenshots/starter-validation.png" alt="Qoder Starter Validation" width="600"/>
</p>

---

## 🚀 Розпочніть у 3 кроки

### 1. Скопіюйте конфігурації:
Скопіюйте `.qoder/`, `.agent/`, `scripts/` та `AGENTS.md` до кореня вашого проекту.

### 2. Налаштувати середовище:

```bash
cp .env.example .env
```

### 3. Почніть кодування:
Відкрийте проект у Cursor або запустіть Claude Code. Агент ШІ автоматично прочитає правила!

---

## 💖 Підтримайте цей проект (пожертви)

Якщо цей шаблон прискорив ваш робочий процес кодування, подумайте про підтримку:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Ліцензія

Цей проект ліцензований згідно з **ліцензією MIT**. Додаткову інформацію див. у файлі [LICENSE](LICENSE).