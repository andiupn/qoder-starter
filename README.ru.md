#Кодер Стартер 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <strong>Русский</strong> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>ИИ-агент без правил — это просто хаотичный сценарий.</strong></h3>
  <p><strong>Qoder Starter — это легкая система правил, ориентированная на искусственный интеллект, предназначенная для согласования поведения агентов искусственного интеллекта с первоначальными соглашениями о кодировании в Cursor, Gemini и Claude Code.</strong></p>

  <p>Хватит тратить токены, страдать от галлюцинаций ИИ и бороться с противоречивыми стилями кода. Моментально включите в своего помощника по кодированию 5 основных правил.</p>
</div>

> 📦 Бесплатный шаблон от **andiupn** ([kuncimu.com](https://kuncimu.com)) · Лицензия [MIT License](LICENSE)  
> ☕ Если полезно, [купи мне кофе](https://ko-fi.com/andiupn) · 🚀 Нужны расширенные монорепозитории, специальные агенты и предварительно упакованная память? Попробуйте [PRO-версию](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
__ЗНАК_3__
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Проблема: хаос помощников по кодированию с помощью искусственного интеллекта
Помощники с искусственным интеллектом невероятно быстры. Однако без предварительно настроенных рекомендаций они пишут неструктурированный код, игнорируют ваши соглашения об именах, сливают секреты и делают ошибочные git-коммиты, которые портят историю вашего репозитория.

---

## ⚡ Решение: 5 фундаментальных правил ИИ

### 1. 📜 Соглашения о коде и языке
Сохраняет ясность языка (`bahasa.md`: индонезийский для чата, английский для кода) и обеспечивает стандартное форматирование (`code-conventions.md`: функции стрелок, строгий TypeScript, JSDoc).

### 🔒 2. Безопасность без галлюцинаций
Защищает ключи и учетные данные API, обеспечивая проверку данных (Zod) и правила предотвращения XSS (`security.md`) перед написанием любого кода.

### 🧠 3. Система исторических знаний
Настраивает рекомендации по использованию памяти (`memory-usage.md`) и соглашения git (`git-conventions.md`), чтобы ИИ-агент учился на основе истории вашего репозитория, используя `/skills` для сохранения обнаруженных сеансов.

---

## 📊 LITE против PRO: Премиум-обновление

| Что вы получаете | 🆓 ЛАЙТ (Стартер) | 💎 ПРО (Премиум) |
|---|:---:|:---:|
| **Основные правила** | 5 | 14 (добавлены: обработка ошибок, тестирование, стек, a11y и т. д.) |
| **Специализированные агенты** | ❌ | 5 (`code-reviewer`, `nextjs-specialist` и т. д.) |
| **Записи памяти (общее начальное значение)** | ❌ | 12 (исправления конфигурации Next.js, Playwright, Redis) |
| **Конфигурации DevOps и MCP** | ❌ | ✅ (шаблоны `mcp.json`) |
| **Обновления основной разработки** | Через GitHub | Через [спонсоров GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Посмотреть полное руководство по сравнению функций и обновлению](COMPARISON.md)**

---

## 📂 Схема репозитория

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Предварительный просмотр

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

## 🚀 Начните за 3 шага

### 1. Скопируйте конфигурации:
Скопируйте `.qoder/`, `.agent/`, `scripts/` и `AGENTS.md` в корень вашего проекта.

### 2. Настройте среду:

```bash
cp .env.example .env
```

### 3. Начните кодирование:
Откройте проект в Cursor или запустите Claude Code. ИИ-агент прочитает правила автоматически!

---

## 💖 Поддержите этот проект (пожертвования)

Если этот шаблон ускорил ваш рабочий процесс кодирования, рассмотрите возможность поддержки:
- **Ко-фи:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Саверия:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Лицензия

Этот проект распространяется по лицензии **MIT License**. Дополнительную информацию см. в файле [ЛИЦЕНЗИЯ](LICENSE).