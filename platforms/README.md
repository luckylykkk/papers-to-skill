# Platform Adapters

`papers-to-skill` is packaged as a plain `SKILL.md` directory plus optional platform manifests.

## Canonical Skill Path

```text
skills/papers-to-skill/
+-- SKILL.md
+-- references/
+-- scripts/
```

Platforms that understand `SKILL.md` folders can load this directory directly.

## npm Installer

```bash
npm install -g github:luckylykkk/papers-to-skill
papers-to-skill paths
papers-to-skill install codex
papers-to-skill install hermes
papers-to-skill install openclaw --dest <openclaw-skills-dir>/papers-to-skill
```

Use `papers-to-skill install skill-dir --dest <agent-skills-dir>/papers-to-skill` for any runtime that accepts a copied skill directory.

## Claude Code

The repository is also a Claude Code plugin:

```bash
claude plugin validate .
```

A local marketplace manifest is provided at `marketplace/.claude-plugin/marketplace.json`:

```bash
claude plugin marketplace add ./marketplace
claude plugin install papers-to-skill@papers-to-skill-marketplace
```

If the plugin is later accepted into a public marketplace, installation becomes:

```bash
claude plugin install papers-to-skill
```

## Hermes

Hermes-compatible installs copy the canonical skill directory into a research skill folder:

```bash
papers-to-skill install hermes
```

This maps to:

```text
~/.hermes/skills/research/papers-to-skill
```

## OpenClaw

OpenClaw-compatible installs should point to the platform's skill directory:

```bash
OPENCLAW_SKILLS_DIR=<openclaw-skills-dir> papers-to-skill install openclaw
```

or:

```bash
papers-to-skill install openclaw --dest <openclaw-skills-dir>/papers-to-skill
```

## 中文说明

`papers-to-skill` 同时提供标准 `SKILL.md` 目录、Claude Code 插件清单、npm 安装器和平台适配 manifest。只要目标平台支持加载 `SKILL.md` 目录，就可以直接使用 `skills/papers-to-skill/`。

常用安装方式：

```bash
npm install -g github:luckylykkk/papers-to-skill
papers-to-skill install codex
papers-to-skill install hermes
papers-to-skill install openclaw --dest <openclaw-skills-dir>/papers-to-skill
```

Claude Code 本地 marketplace 安装：

```bash
claude plugin marketplace add ./marketplace
claude plugin install papers-to-skill@papers-to-skill-marketplace
```
