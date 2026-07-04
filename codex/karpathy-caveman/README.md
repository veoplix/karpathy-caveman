# Karpathy Caveman for Codex

This folder is the Codex bundle for the Karpathy Caveman mode.

Use this bundle when you want the full Codex-facing version of the idea: assistant-agnostic always-on rules, the shared portable skill, and a Codex-native role file.

## Files

- `AGENTS.md` → canonical always-on rules
- `.agents/skills/karpathy-caveman/SKILL.md` → shared portable skill copy
- `.codex/agents/karpathy-caveman.toml` → Codex-native agent role file

## What this bundle gives Codex

- `AGENTS.md` for the canonical always-on rules
- `.agents/skills/karpathy-caveman/SKILL.md` for the shared portable task-mode definition
- `.codex/agents/karpathy-caveman.toml` for a Codex-native role with the same behavioral contract baked into `developer_instructions`

## Install into a target repository

Copy these files so the target repository ends up with:

```text
<repo>/
├─ AGENTS.md
├─ .agents/
│  └─ skills/karpathy-caveman/SKILL.md
└─ .codex/
   └─ agents/karpathy-caveman.toml
```

## How the files work together

- `AGENTS.md` defines the core Karpathy-Caveman operating model.
- `.agents/skills/karpathy-caveman/SKILL.md` carries the portable skill definition.
- `.codex/agents/karpathy-caveman.toml` gives Codex a native role that restates the same intent in Codex-native configuration.

## Notes

`AGENTS.md` provides the always-on rules.

The skill gives Codex the portable Karpathy Caveman operating mode in the shared Agent Skills format.

The `.codex/agents/` role file gives Codex a native agent type with the same behavior baked into `developer_instructions`.

## How to use this bundle correctly

- Copy all three files if you want the complete Codex setup.
- If you keep only `AGENTS.md`, you still get the always-on rules but lose the portable skill and native role.
- If you keep the skill but omit `.codex/agents/karpathy-caveman.toml`, you keep the shared mode but lose the Codex-native role entrypoint.

## How To Use After Install

- Use `AGENTS.md` as the default repository rule set.
- Use the shared `karpathy-caveman` skill when the Codex host exposes the shared Agent Skills surface.
- Use the `karpathy-caveman` role from `.codex/agents/karpathy-caveman.toml` when you want the Codex-native role entrypoint.

Exact role and skill selection UX depends on the Codex host, but this bundle keeps both surfaces available.

## How To Verify

1. Confirm `AGENTS.md`, `.agents/skills/karpathy-caveman/SKILL.md`, and `.codex/agents/karpathy-caveman.toml` exist at the exact paths shown above.
2. Ask Codex to summarize the repository rules or role instructions it sees.
3. Confirm the `karpathy-caveman` skill or native role is discoverable in your Codex host.
4. Run one small coding task and check for concise reasoning, minimal diffs, and explicit verification behavior.

## Limitations

- This bundle documents Codex-native configuration and portable skill use, but it does **not** guarantee control over every Codex surface outside those mechanisms.
- As with the other assistants, inline suggestion behavior is broader than these repository files.

## Maintenance

In this source repository, `../../AGENTS.md` and `../../.agents/skills/karpathy-caveman/SKILL.md` remain the canonical shared sources. Keep the Codex role aligned with them when the mode changes.

## License

This repository is MIT licensed. See `../../LICENSE`.