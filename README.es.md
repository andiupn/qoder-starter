#Qoder Iniciador 🛰️

<div align="center">
  <a href="README.md">English</a> | <a href="README.id.md">Bahasa Indonesia</a> | <a href="README.zh.md">简体中文</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.fr-ca.md">Français (CA)</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.pt-br.md">Português (BR)</a> | <a href="README.vi.md">Tiếng Việt</a> | <a href="README.pl.md">Polski</a> | <a href="README.ja.md">日本語</a> | <a href="README.ko.md">한국어</a> | <strong>Español</strong> | <a href="README.tr.md">Türkçe</a> | <a href="README.it.md">Italiano</a> | <a href="README.ru.md">Русский</a> | <a href="README.uk.md">Українська</a> | <a href="README.nl.md">Nederlands</a>
</div>

<br />

<div align="center">
  <h3><strong>Un agente de IA sin reglas es solo un guión caótico.</strong></h3>
  <p><strong>Qoder Starter es un sistema de reglas liviano, centrado en la IA, diseñado para alinear los comportamientos de los agentes de IA con convenciones de codificación impecables en Cursor, Gemini y Claude Code.</strong></p>

  <p>Deja de desperdiciar tokens, sufrir alucinaciones de IA y luchar con estilos de código inconsistentes. Potencia tu asistente de codificación con 5 hojas de reglas fundamentales al instante.</p>
</div>

> 📦 Plantilla gratuita de **andiupn** ([kuncimu.com](https://kuncimu.com)) · Licenciado bajo [Licencia MIT](LICENSE)  
> ☕ Si es útil, [cómprame un café](https://ko-fi.com/andiupn) · 🚀 ¿Necesitas monorepos avanzados, agentes personalizados y memoria preempaquetada? Pruebe la [versión PRO](https://github.com/sponsors/andiupn?frequency=monthly)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/andiupn/qoder-starter)](https://github.com/andiupn/qoder-starter/releases)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-Support-ff5f5f?logo=ko-fi)](https://ko-fi.com/andiupn)
[![Patreon](https://img.shields.io/badge/Patreon-Support-f96854?logo=patreon)](https://patreon.com/AndiUpn)
[![Trakteer](https://img.shields.io/badge/Trakteer-Support-red?logo=trakteer)](https://trakteer.id/andi_upn/gift)
[![Saweria](https://img.shields.io/badge/Saweria-Support-yellow?logo=saweria)](https://saweria.co/andiupn)

---

## 💡 El problema: el caos de los asistentes de código de IA
Los asistentes de IA son increíblemente rápidos. Sin embargo, sin pautas preconfiguradas, escriben código no estructurado, ignoran sus convenciones de nomenclatura, filtran secretos y realizan confirmaciones de git erráticas que arruinan el historial de su repositorio.

---

## ⚡ La solución: las 5 reglas fundamentales de la IA

### 1. 📜 Convenciones de código y lenguaje
Mantiene el lenguaje claro (`bahasa.md`: indonesio para chat, inglés para código) y aplica el formato estándar (`code-conventions.md`: funciones de flecha, TypeScript estricto, JSDoc).

### 🔒 2. Seguridad sin alucinaciones
Protege las claves y credenciales de API, aplicando la validación de datos (Zod) y las reglas de prevención XSS (`security.md`) antes de escribir cualquier código.

### 🧠 3. Sistema de conocimiento histórico
Configura pautas de memoria (`memory-usage.md`) y convenciones de git (`git-conventions.md`) para que el agente de IA aprenda del historial de su repositorio y utilice `/skills` para guardar los descubrimientos de sesiones.

---

## 📊 LITE vs PRO: La actualización Premium

| Lo que obtienes | 🆓 LITE (Iniciador) | 💎PRO (Premium) |
|---|:---:|:---:|
| **Reglas Fundamentales** | 5 | 14 (agrega: manejo de errores, pruebas, pila, a11y, etc.) |
| **Agentes Aduaneros Especializados** | ❌ | 5 (`code-reviewer`, `nextjs-specialist`, etc.) |
| **Entradas de Memoria (Semilla Genérica)** | ❌ | 12 (correcciones de configuración de Next.js, Playwright, Redis) |
| **Configuraciones de DevOps y MCP** | ❌ | ✅ (`mcp.json` plantillas) |
| **Actualizaciones ascendentes** | Vía GitHub | A través de [Patrocinadores de GitHub](https://github.com/sponsors/andiupn?frequency=monthly) |

👉 **[Ver comparación completa de funciones y guía de actualización](COMPARISON.md)**

---

## 📂 Plano de repositorio

```
your-workspace/
  .qoder/              # System rules for AI agents (bahasa, conventions, security)
  .agent/              # AI memory context, entries, and workflows
  scripts/             # Python tools (save-knowledge, sync-stats)
  AGENTS.md            # The master AI system instructions (entry point)
  .env.example         # Template for environment variables
```

---

## 🖼️ Vista previa

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

## 🚀 Comience en 3 pasos

### 1. Copiar configuraciones:
Copie `.qoder/`, `.agent/`, `scripts/` y `AGENTS.md` a la raíz de su proyecto.

### 2. Configurar el entorno:

```bash
cp .env.example .env
```

### 3. Comience a codificar:
Abra el proyecto en Cursor o ejecute Claude Code. ¡El agente de IA leerá las reglas automáticamente!

---

## 💖 Apoye este proyecto (Donaciones)

Si esta plantilla ha acelerado su flujo de trabajo de codificación, considere admitir:
- **Ko-fi:** [ko-fi.com/andiupn](https://ko-fi.com/andiupn)
- **Patreon:** [patreon.com/AndiUpn](https://patreon.com/AndiUpn)
- **Trakteer:** [trakteer.id/andi_upn/gift](https://trakteer.id/andi_upn/gift)
- **Saweria:** [saweria.co/andiupn](https://saweria.co/andiupn)

---

## 📄 Licencia

Este proyecto tiene la licencia **Licencia MIT**. Consulte el archivo [LICENCIA](LICENSE) para obtener más información.