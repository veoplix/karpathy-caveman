# Karpathy Caveman for Cursor

This folder is the Cursor bundle for the Karpathy Caveman mode.

Use this bundle when you want the full Cursor-facing version of the idea: assistant-agnostic rules, the shared skill, an always-apply Cursor rule, and a Cursor-native subagent.

## Files

- `AGENTS.md` → canonical always-on rules
- `.agents/skills/karpathy-caveman/SKILL.md` → shared portable skill copy
- `.cursor/rules/karpathy-caveman.mdc` → Cursor always-apply rule
- `.cursor/agents/karpathy-caveman.md` → Cursor-native subagent

## What this bundle gives Cursor

- `AGENTS.md` for the canonical always-on rules
- `.agents/skills/karpathy-caveman/SKILL.md` for the portable task-mode definition
- `.cursor/rules/karpathy-caveman.mdc` for passive always-apply Cursor defaults
- `.cursor/agents/karpathy-caveman.md` for an explicit Cursor-native subagent

## Install into a target repository

Copy these files so the target repository ends up with:

```text
<repo>/
├─ AGENTS.md
├─ .agents/
│  └─ skills/karpathy-caveman/SKILL.md
└─ .cursor/
   ├─ agents/karpathy-caveman.md
   └─ rules/karpathy-caveman.mdc
```

## How the files work together

- `AGENTS.md` carries the core Karpathy-Caveman rules.
- `.agents/skills/karpathy-caveman/SKILL.md` keeps the shared portable mode available.
- `.cursor/rules/karpathy-caveman.mdc` applies Cursor-specific defaults automatically.
- `.cursor/agents/karpathy-caveman.md` gives you an explicit Cursor-native subagent when you want one.

## Notes

The root repository keeps the Cursor rule and Cursor subagent at the root because they do not collide with the shared `.agents/skills/` path.

This bundle exists so another repository can copy the same layout directly.

## How to use this bundle correctly

- Copy all four files if you want the complete Cursor experience.
- If you only want passive Cursor defaults, `AGENTS.md` plus `.cursor/rules/karpathy-caveman.mdc` may be enough.
- If you want the explicit Cursor-native subagent too, keep `.cursor/agents/karpathy-caveman.md` alongside the rule and the shared skill.

## How To Use After Install

- Let `AGENTS.md` and `.cursor/rules/karpathy-caveman.mdc` provide the default repository behavior.
- Use the shared `karpathy-caveman` skill when the Cursor workflow exposes the shared Agent Skills surface.
- Invoke the `karpathy-caveman` subagent from `.cursor/agents/karpathy-caveman.md` when you want an explicit Cursor-native agent run.

## How To Verify

1. Confirm `AGENTS.md`, `.agents/skills/karpathy-caveman/SKILL.md`, `.cursor/rules/karpathy-caveman.mdc`, and `.cursor/agents/karpathy-caveman.md` exist at the exact paths shown above.
2. Ask Cursor to summarize the repository rules it sees.
3. Confirm the always-apply rule and the `karpathy-caveman` subagent are discoverable.
4. Run one small coding task and check for concise reasoning, surgical edits, and explicit verification behavior.

## Limitations

- This bundle primarily affects Cursor rule, skill, and subagent workflows.
- It does **not** fully control inline autocomplete or every Cursor behavior outside those surfaces.

## Maintenance

In this source repository, `../../AGENTS.md`, `../../.agents/skills/karpathy-caveman/SKILL.md`, `../../.cursor/rules/karpathy-caveman.mdc`, and `../../.cursor/agents/karpathy-caveman.md` remain the canonical sources.

## License

This repository is MIT licensed. See `../../LICENSE`.