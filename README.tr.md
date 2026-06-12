# Qoder Başlangıç 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <strong>Türkçe</strong> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a>
</div>

<br />

<div align="center">
  <h3><strong>Kuralları olmayan bir AI aracısı yalnızca kaotik bir komut dosyasıdır.</strong></h3>
  <p><strong>Qoder Starter, AI aracısı davranışlarını Cursor, Gemini ve Claude Code'daki orijinal kodlama kurallarıyla uyumlu hale getirmek için tasarlanmış hafif, AI öncelikli bir kural sistemidir.</strong></p>

  <p>Jeton israfına, yapay zeka halüsinasyonlarına maruz kalmaya ve tutarsız kod stilleriyle uğraşmaya son verin. Kodlama asistanınızı 5 temel kural sayfasıyla anında güçlendirin.</p>
</div>

> 📦 **andiupn** ([kuncimu.com](https://kuncimu.com)) tarafından hazırlanan ücretsiz şablon · [MIT Lisansı](LICENSE) kapsamında lisanslıdır  
> ☕ Yararlıysa, [bana bir kahve al](https://ko-fi.com/andiupn) · 🚀 Gelişmiş monorepolara, özel aracılara ve önceden paketlenmiş belleğe mi ihtiyacınız var? [PRO sürümünü] deneyin(https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Sorun: Yapay Zeka Kod Asistanlarının Kaosu
Yapay zeka asistanları inanılmaz derecede hızlıdır. Ancak önceden yapılandırılmış yönergeler olmadan yapılandırılmamış kod yazarlar, adlandırma kurallarınızı göz ardı ederler, sırları sızdırırlar ve depo geçmişinizi bozan düzensiz git taahhütleri yaparlar.

---

## ⚡ Çözüm: 5 Temel Yapay Zeka Kuralı

### 1. 📜 Kod ve Dil Kuralları
Dili anlaşılır tutar (`bahasa.md`: Sohbet için Endonezce, kod için İngilizce) ve standart biçimlendirmeyi uygular (`code-conventions.md`: ok işlevleri, TypeScript katı, JSDoc).

### 🔒 2. Sıfır Halüsinasyon Güvenliği
Herhangi bir kod yazmadan önce veri doğrulamayı (Zod) ve XSS önleme kurallarını (`security.md`) zorunlu kılarak API anahtarlarını ve kimlik bilgilerini korur.

### 🧠 3. Tarihsel Bilgi Sistemi
Bellek yönergelerini (`memory-usage.md`) ve git kurallarını (`git-conventions.md`) yapılandırarak AI aracısının oturum keşiflerini kaydetmek için `/skills` kullanarak depo geçmişinizden öğrenmesini sağlar.

---

## 📊 LITE ve PRO: Premium Yükseltmesi

| Ne Alırsınız | 🆓 LITE (Başlangıç) | 💎 PRO (Premium) |
|---|:---:|:---:|
| **Temel Kurallar** | 5 | 14 (ekler: hata işleme, test etme, yığın, a11y, vb.) |
| **Uzman Özel Temsilciler** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, vb.) |
| **Bellek Girişleri (Genel Çekirdek)** | ❌ | 12 (Next.js yapılandırma düzeltmeleri, Oyun Yazarı, Redis) |
| **DevOps ve MCP Yapılandırmaları** | ❌ | ✅ (`mcp.json` şablonları) |
| **Yukarı Akış Güncellemeleri** | GitHub aracılığıyla | [GitHub Sponsorları](https://github.com/sponsors/andiupn?frequency=monthly) aracılığıyla |

👉 **[Tam Özellik Karşılaştırma ve Yükseltme Kılavuzunu Görüntüleyin](COMPARISON.md)**

---

## 📂 Depo Planı

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Önizleme

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

## 🚀 3 Adımda Başlayın

### 1. Yapılandırmaları kopyalayın:
`.qoder/`, `.agent/`, `scripts/` ve `AGENTS.md` proje kökünüze kopyalayın.

### 2. Ortamı yapılandırın:

```bash
cp .env.example .env
```

### 3. Kodlamaya Başlayın:
Projeyi İmleç'te açın veya Claude Code'u çalıştırın. Yapay zeka temsilcisi kuralları otomatik olarak okuyacaktır!

---

## 💖 Bu Projeyi Destekleyin (Bağışlar)

Bu şablon kodlama iş akışınızı hızlandırdıysa aşağıdakileri desteklemeyi düşünün:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Lisans

Bu proje **MIT Lisansı** kapsamında lisanslanmıştır. Daha fazla bilgi için [LİSANS](LICENSE) dosyasına bakın.