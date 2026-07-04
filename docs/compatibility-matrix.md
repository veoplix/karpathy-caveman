# Compatibility Matrix

This matrix describes how Karpathy Caveman maps onto each supported assistant.

| Assistant | Always-on rule entrypoint | Manual trigger | Agent / subagent | Skill path | Copy bundle |
| --- | --- | --- | --- | --- | --- |
| GitHub Copilot in VS Code | `AGENTS.md` or `.github/copilot-instructions.md` | `.github/prompts/karpathy-caveman.prompt.md` | `.github/agents/karpathy-caveman.agent.md` or plugin agent | `.agents/skills/karpathy-caveman/SKILL.md` or plugin skill | `copilot/karpathy-caveman/` |
| Claude Code | `CLAUDE.md` importing `@AGENTS.md` | native skill invocation from `.claude/skills/` in the Claude bundle | `.claude/agents/karpathy-caveman.md` | `.claude/skills/karpathy-caveman/SKILL.md` | `claude/karpathy-caveman/` |
| Codex | `AGENTS.md` | shared Agent Skills format in `.agents/skills/` | `.codex/agents/karpathy-caveman.toml` | `.agents/skills/karpathy-caveman/SKILL.md` | `codex/karpathy-caveman/` |
| Cursor | `AGENTS.md` plus `.cursor/rules/karpathy-caveman.mdc` | shared Agent Skills format in `.agents/skills/` | `.cursor/agents/karpathy-caveman.md` | `.agents/skills/karpathy-caveman/SKILL.md` | `cursor/karpathy-caveman/` |

## Copilot bundle slices

The assistant-root Copilot bundle lives at `copilot/karpathy-caveman/`.

Treat that folder as a **repo-file source bundle**. It collects all Copilot repository-file artifacts in one place, but the `.github/copilot-instructions.md` file inside it is still optional and should only be copied into target repositories when you intentionally want the Copilot-only adapter.

The canonical narrower Copilot slices now live at:

- `copilot/instruction/` → always-on adapter only
- `copilot/prompt/` → prompt only
- `copilot/plugin/karpathy-caveman/` → publishable plugin package only

## Root repository safety choices

The root repository intentionally avoids some otherwise-valid files:

- no root `.claude/skills/karpathy-caveman/`
- no root `.claude/agents/`
- no root `.codex/agents/`
- no root `.github/skills/`
- no root `.github/copilot-instructions.md`

Reason:

- multiple assistants scan overlapping compatibility roots
- duplicate skill or subagent names can lead to duplicate registration or ambiguous selection
- Copilot can already use `AGENTS.md`, so adding a second root always-on instruction file wastes context

## Canonical mirrored content

These files should stay byte-for-byte aligned across their bundle copies:

- `AGENTS.md`
- `.github/copilot-instructions.md` in the instruction and Copilot bundles
- `CLAUDE.md` in the Claude bundle
- `.github/prompts/karpathy-caveman.prompt.md` in the prompt and Copilot bundles
- `.github/agents/karpathy-caveman.agent.md` in the plugin and Copilot bundles
- `.agents/skills/karpathy-caveman/SKILL.md` in the Copilot, plugin, and assistant bundles
- `.cursor/rules/karpathy-caveman.mdc`
- `.cursor/agents/karpathy-caveman.md`

Use `scripts/validate_repo.py` to verify that alignment.