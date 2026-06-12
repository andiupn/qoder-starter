# Qoder 스타터 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <strong>한국어</strong> | <a href="README.es.md">Español</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a> | <a href="README.sv.md">Svenska</a> | <a href="README.ro.md">Română</a>
</div>
<br>

<div align="center">
  <h3><strong>규칙이 없는 AI 에이전트는 혼란스러운 스크립트일 뿐입니다.</strong></h3>
  <p><strong>Qoder Starter는 AI 에이전트 동작을 Cursor, Gemini 및 Claude Code의 원시 코딩 규칙에 맞게 조정하도록 설계된 경량의 AI 우선 규칙 시스템입니다.</strong></p>

  <p>토큰 낭비, AI 환각, 일관되지 않은 코드 스타일로 인한 어려움을 중지하세요. 5가지 기본 규칙 시트로 즉시 코딩 도우미를 강화하세요.</p>
</div>

> 📦 **andiupn**([kuncimu.com](https://kuncimu.com))의 무료 템플릿 · [MIT 라이선스](LICENSE)에 따라 라이선스가 부여됨  
> 주의 도움이 된다면 [커피 사주세요](https://ko-fi.com/andiupn) · 🚀 고급 모노레포, 커스텀 에이전트, 사전 패키지된 메모리가 필요하신가요? [PRO 버전](https://github.com/sponsors/andiupn?frequency=monthly)을 사용해 보세요.

__배지_0__
__배지_1__
__배지_2__
__배지_3__
__배지_4__
__배지_5__

---

## 💡 문제: AI 코드 도우미의 혼돈
AI 비서는 엄청나게 빠릅니다. 그러나 사전 구성된 지침이 없으면 구조화되지 않은 코드를 작성하고, 명명 규칙을 무시하고, 비밀을 유출하고, 저장소 기록을 엉망으로 만드는 불규칙한 git 커밋을 만듭니다.

---

## ⚡ 솔루션: 5가지 기본 AI 규칙

### 1. 📜 코드 및 언어 규칙
언어를 명확하게 유지하고(`bahasa.md`: 채팅용 인도네시아어, 코드용 영어) 표준 형식(`code-conventions.md`: 화살표 함수, TypeScript strict, JSDoc)을 적용합니다.

### 🔒 2. 환각 제로 보안
코드를 작성하기 전에 데이터 유효성 검사(Zod) 및 XSS 방지 규칙(`security.md`)을 적용하여 API 키와 자격 증명을 보호합니다.

### 🧠 3. 역사지식 시스템
AI 에이전트가 세션 검색을 저장하기 위해 `/skills`을 사용하여 저장소 기록에서 학습할 수 있도록 메모리 지침(`memory-usage.md`) 및 Git 규칙(`git-conventions.md`)을 구성합니다.

---

## 📊 LITE 대 PRO: 프리미엄 업그레이드

| 당신이 얻는 것 | 🆓 LITE(스타터) | 💎 PRO(프리미엄) |
|---|:---:|:---:|
| **기본 규칙** | 5 | 14(추가: 오류 처리, 테스트, 스택, a11y 등) |
| **전문 맞춤형 에이전트** | ❌ | 5(`code-reviewer`, `nextjs-specialist` 등) |
| **메모리 항목(일반 시드)** | ❌ | 12(Next.js 구성 수정, Playwright, Redis) |
| **DevOps 및 MCP 구성** | ❌ | ✅ (`mcp.json` 템플릿) |
| **업스트림 업데이트** | GitHub를 통해 | [GitHub 후원자](https://github.com/sponsors/andiupn?frequency=monthly)를 통해 |

👉 **[전체 기능 비교 및 업그레이드 가이드 보기](COMPARISON.md)**

---

## 📂 저장소 청사진

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ 미리보기

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

## 🚀 3단계로 시작하기

### 1. 구성 복사:
`.qoder/`, `.agent/`, `scripts/` 및 `AGENTS.md`을 프로젝트 루트에 복사합니다.

### 2. 환경을 구성합니다.

```bash
cp .env.example .env
```

### 3. 코딩 시작:
커서에서 프로젝트를 열거나 Claude Code를 실행하세요. AI 에이전트가 자동으로 규칙을 읽습니다!

---

## 💖 이 프로젝트를 후원하세요(기부)

이 템플릿으로 코딩 작업 흐름이 가속화된 경우 다음 지원을 고려해보세요.
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **트랙터:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **사웨리아:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 라이선스

이 프로젝트는 **MIT 라이선스**에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.