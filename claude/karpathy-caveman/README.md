# Karpathy Caveman for Claude Code

This folder is the Claude Code bundle for the Karpathy Caveman mode.

Use this bundle when you want the full Claude-facing version of the idea: assistant-agnostic always-on rules, a Claude entrypoint, a Claude-native skill, and a Claude-native subagent.

## Files

- `AGENTS.md` → canonical assistant-agnostic rules
- `CLAUDE.md` → Claude always-on entrypoint that imports `@AGENTS.md`
- `.claude/skills/karpathy-caveman/SKILL.md` → Claude-native skill copy
- `.claude/agents/karpathy-caveman.md` → Claude-native subagent that preloads the skill

## What this bundle gives Claude

- the Karpathy-Caveman always-on rules through `AGENTS.md`
- a Claude-specific repository entrypoint through `CLAUDE.md`
- a Claude-native reusable skill
- a Claude-native subagent that is already wired to that skill

## Install into a target repository

Copy these files so the target repository ends up with:

```text
<repo>/
├─ AGENTS.md
├─ CLAUDE.md
└─ .claude/
   ├─ agents/karpathy-caveman.md
   └─ skills/karpathy-caveman/SKILL.md
```

## How the files work together

- `AGENTS.md` contains the canonical shared rules.
- `CLAUDE.md` imports `@AGENTS.md`, so those two files should stay together.
- `.claude/skills/karpathy-caveman/SKILL.md` provides Claude-native skill invocation.
- `.claude/agents/karpathy-caveman.md` gives Claude a ready-to-use subagent that already expects the skill to exist.

## Why this is a bundle instead of a root copy here

The root repository keeps only one canonical root skill at `.agents/skills/karpathy-caveman/SKILL.md` to avoid duplicate skill registration across assistants that scan compatibility roots.

Use this folder when you want a Claude-native copy for another repository.

## How to use this bundle correctly

- Copy the whole bundle if you want the complete Claude setup.
- Do not copy `CLAUDE.md` without `AGENTS.md`, because `CLAUDE.md` imports it.
- Do not copy the Claude subagent without the Claude skill unless you also change the subagent definition.
- If you only want always-on rules and do not need Claude-native skill or subagent behavior, `AGENTS.md` and `CLAUDE.md` may be enough.

## How To Use After Install

- Let `CLAUDE.md` and `AGENTS.md` provide the default repository behavior.
- Invoke the `karpathy-caveman` skill when you want the Claude-native skill surface explicitly.
- Invoke the `karpathy-caveman` subagent when you want a contained implementation, review, refactor, or debugging run with the skill preloaded.

## How To Verify

1. Confirm `AGENTS.md`, `CLAUDE.md`, `.claude/skills/karpathy-caveman/SKILL.md`, and `.claude/agents/karpathy-caveman.md` exist at the exact paths shown above.
2. Ask Claude to summarize the repository rules it sees.
3. Confirm the `karpathy-caveman` skill and subagent are discoverable.
4. Run one small coding task and check for concise reasoning, surgical edits, and explicit verification behavior.

## Limitations

- This bundle primarily affects Claude chat, skill, and subagent workflows.
- It does **not** fully control autocomplete or every Claude behavior outside those surfaces.

## Maintenance

In this source repository, `../../AGENTS.md` and `../../.agents/skills/karpathy-caveman/SKILL.md` remain the canonical shared sources. Keep the Claude-native files aligned with them when the mode changes.

## License

This repository is MIT licensed. See `../../LICENSE`.