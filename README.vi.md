#Qoder Khởi Đầu 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <strong>Tiếng Việt</strong> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>Một tác nhân AI không có quy tắc chỉ là một kịch bản hỗn loạn.</strong></h3>
  <p><strong>Qoder Starter là một hệ thống quy tắc nhẹ, ưu tiên AI được thiết kế để điều chỉnh các hành vi của tác nhân AI với các quy ước mã hóa nguyên sơ trong Mã con trỏ, Gemini và Claude.</strong></p>

  <p>Hãy ngừng lãng phí mã thông báo, mắc chứng ảo giác về AI và đấu tranh với các kiểu mã không nhất quán. Hỗ trợ ngay lập tức trợ lý mã hóa của bạn với 5 bảng quy tắc cơ bản.</p>
</div>

> 📦 Mẫu miễn phí của **andiupn** ([kuncimu.com](https://kuncimu.com)) · Được cấp phép theo [Giấy phép MIT](LICENSE)  
> ☕ Nếu hữu ích, [mua cho tôi một ly cà phê](https://ko-fi.com/andiupn) · 🚀 Bạn cần monorepos nâng cao, tác nhân tùy chỉnh và bộ nhớ đóng gói sẵn? Hãy thử [phiên bản PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 Vấn đề: Sự hỗn loạn của Trợ lý mã AI
Trợ lý AI cực kỳ nhanh. Tuy nhiên, nếu không có các hướng dẫn được định cấu hình trước, chúng sẽ viết mã không có cấu trúc, bỏ qua các quy ước đặt tên của bạn, rò rỉ bí mật và thực hiện các cam kết git thất thường làm xáo trộn lịch sử kho lưu trữ của bạn.

---

## ⚡ Giải pháp: 5 quy tắc AI cơ bản

### 1. 📜 Quy ước về mã và ngôn ngữ
Giữ ngôn ngữ rõ ràng (`bahasa.md`: Tiếng Indonesia cho trò chuyện, tiếng Anh cho mã) và thực thi định dạng chuẩn (`code-conventions.md`: hàm mũi tên, TypeScript strict, JSDoc).

### 🔒 2. Bảo mật không gây ảo giác
Bảo vệ khóa API và thông tin xác thực, thực thi xác thực dữ liệu (Zod) và các quy tắc ngăn chặn XSS (`security.md`) trước khi viết bất kỳ mã nào.

### 🧠 3. Hệ thống kiến thức lịch sử
Định cấu hình các nguyên tắc bộ nhớ (`memory-usage.md`) và quy ước git (`git-conventions.md`) để tác nhân AI học hỏi từ lịch sử kho lưu trữ của bạn, sử dụng `/skills` để lưu các khám phá phiên.

---

## 📊 LITE vs PRO: Bản nâng cấp cao cấp

| Những gì bạn nhận được | 🆓 LITE (Người mới bắt đầu) | 💎 PRO (Cao cấp) |
|---|:---:|:---:|
| **Quy tắc cơ bản** | 5 | 14 (bổ sung: xử lý lỗi, kiểm tra, ngăn xếp, a11y, v.v.) |
| **Đại lý tùy chỉnh chuyên biệt** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, v.v.) |
| **Mục nhập bộ nhớ (Hạt giống chung)** | ❌ | 12 (Sửa cấu hình Next.js, Nhà viết kịch, Redis) |
| **Cấu hình DevOps & MCP** | ❌ | ✅ (`mcp.json` mẫu) |
| **Cập nhật ngược dòng** | Qua GitHub | Thông qua [Nhà tài trợ GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Xem hướng dẫn nâng cấp và so sánh đầy đủ tính năng](COMPARISON.md)**

---

## 📂 Bản thiết kế kho lưu trữ

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Xem trước

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

## 🚀 Bắt đầu sau 3 bước

### 1. Sao chép cấu hình:
Sao chép `.qoder/`, `.agent/`, `scripts/` và `AGENTS.md` vào thư mục gốc dự án của bạn.

### 2. Cấu hình môi trường:

```bash
cp .env.example .env
```

### 3. Bắt đầu viết mã:
Mở dự án bằng Cursor hoặc chạy Claude Code. Tác nhân AI sẽ tự động đọc các quy tắc!

---

## 💖 Hỗ trợ dự án này (Quyên góp)

Nếu mẫu này đã tăng tốc quy trình viết mã của bạn, hãy xem xét hỗ trợ:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Giấy phép

Dự án này được cấp phép theo **Giấy phép MIT**. Xem tệp [LICENSE](LICENSE) để biết thêm thông tin.