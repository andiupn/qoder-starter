#Qoder 入门🛰️

<div align="center">
  <strong>英语</strong> | <a href="README.id.md">印度尼西亚语</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">法语（加拿大）</a> | <a href="README.de.md">德语</a> | <a href="README.fr.md">法语</a> | <a href="README.pt-br.md">葡萄牙语（巴西）</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">波兰斯基</a>
</div>

<br />

<div align="center">
  <h3><strong>没有规则的人工智能代理只是一个混乱的脚本。</strong></h3>
  <p><strong>Qoder Starter 是一个轻量级的 AI 优先规则系统，旨在使 AI 代理行为与 Cursor、Gemini 和 Claude Code 中的原始编码约定保持一致。</strong></p>

  <p>停止浪费代币、遭受人工智能幻觉以及与不一致的代码风格作斗争。立即为您的编码助手提供 5 个基本规则表。</p>
</div>

> 📦 **andiupn** 提供的免费模板 ([kuncimu.com](https://kuncimu.com)) · 根据 [MIT 许可证](LICENSE) 获得许可  
> ☕ 如果有用，[请我喝杯咖啡](https://ko-fi.com/andiupn) · 🚀 需要高级 monorepos、自定义代理和预打包内存？尝试[专业版](https://github.com/sponsors/andiupn?frequency=monthly)

__徽章_0__
__徽章_1__
__徽章_2__
__徽章_3__
__徽章_4__
__徽章_5__

---

## 💡 问题：AI 代码助手的混乱
人工智能助手的速度快得令人难以置信。然而，如果没有预先配置的指导方针，他们会编写非结构化代码，忽略您的命名约定，泄漏秘密，并进行不稳定的 git 提交，从而弄乱您的存储库历史记录。

---

## ⚡ 解决方案：5 个基本人工智能规则

### 1.📜 代码和语言约定
保持语言清晰（`bahasa.md`：印度尼西亚语用于聊天，英语用于代码）并强制执行标准格式（`code-conventions.md`：箭头函数、TypeScript strict、JSDoc）。

### 🔒 2. 零幻觉安全
在编写任何代码之前保护 API 密钥和凭据，强制执行数据验证 (Zod) 和 XSS 预防规则 (`security.md`)。

### 🧠 3.历史知识体系
配置内存准则 (`memory-usage.md`) 和 git 约定 (`git-conventions.md`)，以便 AI 代理从存储库历史记录中学习，使用 `/skills` 保存会话发现。

---

## 📊 LITE 与 PRO：高级升级

|你得到什么 | 🆓 LITE（入门版）| 💎 PRO（高级）|
|---|:---:|:---:|
| **基本规则** | 5 | 14（添加：错误处理、测试、堆栈、a11y 等）|
| **专业定制代理** | ❌ | 5（`code-reviewer`、`nextjs-specialist` 等）|
| **内存条目（通用种子）** | ❌ | 12（Next.js 配置修复、Playwright、Redis）|
| **DevOps 和 MCP 配置** | ❌ | ✅（`mcp.json` 模板）|
| **上游更新** |通过 GitHub |通过 [GitHub 赞助商](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[查看完整功能比较和升级指南](COMPARISON.md)**

---

## 📂 存储库蓝图

__代码_块_0__

---

## 🖼️ 预览

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

## 🚀 3 步入门

### 1.复制配置：
将 `.qoder/`、`.agent/`、`scripts/` 和 `AGENTS.md` 复制到项目根目录。

### 2.配置环境：

__代码_块_1__

### 3.开始编码：
在 Cursor 中打开项目或运行 Claude Code。 AI代理会自动读取规则！

---

## 💖 支持这个项目（捐款）

如果此模板加速了您的编码工作流程，请考虑支持：
- **Ko-fi：** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon：** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer：** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria：** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 许可证

该项目根据 **MIT 许可证** 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。