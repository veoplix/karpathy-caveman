# Rollout Plan

This is the implementation and adoption plan for using Karpathy Caveman across GitHub Copilot, Claude Code, Codex, and Cursor.

## Phase 1: Choose the repository posture

Pick one of these deployment shapes before copying files:

1. Copilot-only repository
2. Claude-only repository
3. Codex-only repository
4. Cursor-only repository
5. Mixed-assistant repository

## Phase 2: Install the shared core

For any repository that can use the shared core directly:

1. Copy `AGENTS.md`.
2. Copy `.agents/skills/karpathy-caveman/SKILL.md`.
3. Treat those as the canonical files.

## Phase 3: Add assistant-specific adapters

### GitHub Copilot / VS Code

1. Use `copilot/karpathy-caveman/` as the source bundle when you want one folder containing all Copilot repository-file artifacts.
2. In mixed-assistant repositories, prefer `AGENTS.md` as the always-on source and copy `.github/copilot-instructions.md` only when you specifically want the Copilot-only adapter.
3. Use `copilot/instruction/` if you only want the always-on instruction slice.
4. Use `copilot/prompt/` if you only want `/karpathy-caveman`.
5. Use `copilot/plugin/karpathy-caveman/` for packaged team rollout.

### Claude Code

1. Copy the `claude/karpathy-caveman/` bundle.
2. Keep `CLAUDE.md` importing `@AGENTS.md`.
3. Keep the native `.claude/skills/` and `.claude/agents/` files together.

### Codex

1. Copy the `codex/karpathy-caveman/` bundle.
2. Keep `AGENTS.md` as the always-on rules file.
3. Keep `.codex/agents/karpathy-caveman.toml` for the native Codex role.

### Cursor

1. Copy the `cursor/karpathy-caveman/` bundle.
2. Keep `AGENTS.md` and `.agents/skills/`.
3. Keep the Cursor-native `.cursor/rules/` and `.cursor/agents/` files.

## Phase 4: Validate the bundle set

1. Run `python scripts/validate_repo.py` in this repository before publishing or copying updates.
2. Fix any reported drift between mirrored files.
3. Fix missing links, invalid frontmatter, or manifest parse failures.

## Phase 5: Publish or copy to target repositories

1. Publish or distribute the Copilot plugin from `copilot/plugin/karpathy-caveman/` if your team uses plugin rollout.
2. Copy the assistant-specific bundles into target repositories. For Copilot, prefer `copilot/karpathy-caveman/` when you want the full bundle.
3. Avoid mixing duplicate root discovery paths unless you have a platform-specific reason.

## Phase 6: Ongoing maintenance

1. Edit canonical files first: `AGENTS.md` and `.agents/skills/karpathy-caveman/SKILL.md`.
2. Mirror those edits into bundle copies.
3. Re-run the validator.
4. Keep the compatibility matrix current whenever assistant discovery behavior changes.