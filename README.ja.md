#Qoderスターター🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <strong>日本語</strong> | <a href="README.ko.md">한국어</a> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a>
</div>

<br />

<div align="center">
  <h3><strong>ルールのない AI エージェントは、単なる混沌としたスクリプトです。</strong></h3>
  <p><strong>Qoder Starter は、AI エージェントの動作を Cursor、Gemini、および Claude Code の純粋なコーディング規約に合わせるように設計された軽量の AI ファースト ルール システムです。</strong></p>

  <p>トークンの無駄遣い、AI の幻覚に悩まされること、一貫性のないコード スタイルに悩むことはもうやめましょう。 5 つの基本ルール シートを使用してコーディング アシスタントを瞬時に強化します。</p>
</div>

> 📦 **andiupn** による無料テンプレート ([kuncimu.com](https://kuncimu.com)) · [MIT ライセンス](LICENSE) に基づいてライセンスされています  
> ☕ 役に立ったら、[コーヒーを買ってきてください](https://ko-fi.com/andiupn) · 🚀 高度なモノリポジトリ、カスタム エージェント、および事前にパッケージ化されたメモリが必要ですか? [PRO バージョン](https://github.com/sponsors/andiupn?frequency=monthly) をお試しください

__バッジ_0__
__バッジ_1__
__バッジ_2__
__バッジ_3__
__バッジ_4__
__バッジ_5__

---

## 💡 問題: AI コードアシスタントの混乱
AI アシスタントは信じられないほど高速です。ただし、事前に設定されたガイドラインがなければ、構造化されていないコードを記述し、命名規則を無視し、機密情報を漏洩し、リポジトリの履歴を台無しにする不安定な git コミットを行います。

---

## ⚡ 解決策: AI の 5 つの基本ルール

### 1. 📜 コードと言語の規約
言語を明確に保ち (`bahasa.md`: チャットはインドネシア語、コードは英語)、標準書式設定を強制します (`code-conventions.md`: アロー関数、TypeScript strict、JSDoc)。

### 🔒 2. 幻覚ゼロのセキュリティ
API キーと認証情報を保護し、コードを記述する前にデータ検証 (Zod) と XSS 防止ルール (`security.md`) を適用します。

### 🧠 3. 歴史知識システム
AI エージェントがリポジトリ履歴から学習し、`/skills` を使用してセッション ディスカバリを保存できるように、メモリ ガイドライン (`memory-usage.md`) と git 規則 (`git-conventions.md`) を構成します。

---

## 📊 LITE vs PRO: プレミアムアップグレード

|得られるもの | 🆓 LITE (スターター) | 💎 プロ (プレミアム) |
|---|:---:|:---:|
| **基本的なルール** | 5 | 14 (追加: エラー処理、テスト、スタック、a11y など) |
| **専門のカスタム エージェント** | ❌ | 5 (`code-reviewer`、`nextjs-specialist` など) |
| **メモリ エントリ (汎用シード)** | ❌ | 12 (Next.js 構成修正、Playwright、Redis) |
| **DevOps と MCP 構成** | ❌ | ✅ (`mcp.json` テンプレート) |
| **アップストリームのアップデート** | GitHub経由 | [GitHub スポンサー](https://github.com/sponsors/andiupn?frequency=monthly) 経由 |

👉 **[全機能の比較とアップグレード ガイドを表示](COMPARISON.md)**

---

## 📂 リポジトリ ブループリント

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ プレビュー

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

## 🚀 3 ステップで始めましょう

### 1. 構成をコピーします。
`.qoder/`、`.agent/`、`scripts/`、および `AGENTS.md` をプロジェクト ルートにコピーします。

### 2. 環境を構成します。

```bash
cp .env.example .env
```

### 3. コーディングを開始します。
カーソルでプロジェクトを開くか、クロード コードを実行します。 AI エージェントがルールを自動的に読み取ります。

---

## 💖 このプロジェクトをサポートする (寄付)

このテンプレートによりコーディング ワークフローが高速化された場合は、以下のサポートを検討してください。
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **サウェリア:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 ライセンス

このプロジェクトは **MIT ライセンス** に基づいてライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。