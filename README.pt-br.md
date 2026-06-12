# Qoder Starter 🛰️

<div align="center">
  <strong>Inglês</strong> | <a href="README.id.md">Bahasa Indonésia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Alemão</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a>
</div>

<br />

<div align="center">
  <h3><strong>Um agente de IA sem regras é apenas um script caótico.</strong></h3>
  <p><strong>Qoder Starter é um sistema de regras leve e baseado em IA, projetado para alinhar os comportamentos dos agentes de IA com convenções de codificação originais em Cursor, Gemini e Claude Code.</strong></p>

  <p>Pare de desperdiçar tokens, sofrer de alucinações de IA e lutar com estilos de código inconsistentes. Capacite seu assistente de codificação com 5 folhas de regras fundamentais instantaneamente.</p>
</div>

> 📦 Modelo gratuito de **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licenciado sob [Licença MIT](LICENSE)  
> ☕ Se for útil, [me compre um café](https://ko-fi.com/andiupn) · 🚀 Precisa de monorepos avançados, agentes personalizados e memória pré-empacotada? Experimente a [versão PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
__EMBAIXO_1__
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
__EMBAIXO_3__
__EMBAIXO_4__
__EMBLEMA_5__

---

## 💡 O problema: o caos dos assistentes de código de IA
Os assistentes de IA são incrivelmente rápidos. No entanto, sem diretrizes pré-configuradas, eles escrevem código não estruturado, ignoram suas convenções de nomenclatura, vazam segredos e fazem commits git erráticos que bagunçam o histórico do seu repositório.

---

## ⚡ A solução: as 5 regras fundamentais de IA

### 1. 📜 Convenções de código e linguagem
Mantém a linguagem clara (`bahasa.md`: indonésio para bate-papo, inglês para código) e impõe formatação padrão (`code-conventions.md`: funções de seta, TypeScript estrito, JSDoc).

### 🔒 2. Segurança sem alucinações
Protege chaves e credenciais de API, aplicando validação de dados (Zod) e regras de prevenção XSS (`security.md`) antes de escrever qualquer código.

### 🧠 3. Sistema de Conhecimento Histórico
Configura diretrizes de memória (`memory-usage.md`) e convenções git (`git-conventions.md`) para que o agente de IA aprenda com o histórico do seu repositório, usando `/skills` para salvar descobertas de sessão.

---

## 📊 LITE vs PRO: a atualização premium

| O que você ganha | 🆓 LITE (iniciante) | 💎 PRO (Prêmio) |
|---|:---:|:---:|
| **Regras Fundamentais** | 5 | 14 (adiciona: tratamento de erros, testes, pilha, a11y, etc.) |
| **Agentes Personalizados Especializados** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, etc.) |
| **Entradas de memória (semente genérica)** | ❌ | 12 (correções de configuração Next.js, Playwright, Redis) |
| **Configurações de DevOps e MCP** | ❌ | ✅ (`mcp.json` modelos) |
| **Atualizações upstream** | Através do GitHub | Através de [patrocinadores do GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Ver comparação completa de recursos e guia de atualização](COMPARISON.md)**

---

## 📂 Projeto do Repositório

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Visualização

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

## 🚀 Comece em 3 etapas

### 1. Copiar configurações:
Copie `.qoder/`, `.agent/`, `scripts/` e `AGENTS.md` para a raiz do seu projeto.

### 2. Configurar ambiente:

```bash
cp .env.example .env
```

### 3. Comece a codificar:
Abra o projeto no Cursor ou execute o Claude Code. O agente AI lerá as regras automaticamente!

---

## 💖 Apoie este projeto (doações)

Se este modelo acelerou seu fluxo de trabalho de codificação, considere apoiar:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.