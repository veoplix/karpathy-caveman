# Karpathy Caveman Prompt

This folder is the canonical Copilot **prompt slice**.

It contains the standalone Copilot / VS Code prompt file:

- `karpathy-caveman.prompt.md`

It provides the explicit slash command:

```text
/karpathy-caveman
```

## What This Slice Does

This slice gives you a manual Copilot entrypoint into the Karpathy-Caveman mode.

Use it when you want:

- a one-shot trigger for the current thread
- a manual override without changing the whole repository setup
- a stable slash command that maps to the Karpathy-Caveman rules

It is **not** the canonical source of the mode. The canonical sources remain:

- `../../AGENTS.md`
- `../../.agents/skills/karpathy-caveman/SKILL.md`

The root direct-use copy for this repository lives at `../../.github/prompts/karpathy-caveman.prompt.md`.

## When To Use This Slice

Use this slice when:

- you want a prompt file only
- you do not need the instruction slice or plugin package in the same bundle
- you want users to opt into the mode explicitly instead of loading it always-on

For the full Copilot repo-file source bundle, use `../karpathy-caveman/`.

## How To Install In VS Code

### Workspace scope

Place the file at:

```text
.github/prompts/karpathy-caveman.prompt.md
```

### User profile scope

Create it from `Chat: New Prompt File` or the Agent Customizations editor and store it in the user profile.

## How To Use After Install

1. Open Copilot Chat.
2. Run `/karpathy-caveman`.
3. Continue the thread under the mode unless you explicitly switch away.

This works well either on its own or alongside `AGENTS.md` when you want both always-on defaults and a manual reinforcement command.

## How To Verify

1. Confirm the prompt file exists at `.github/prompts/karpathy-caveman.prompt.md`.
2. Check that `/karpathy-caveman` appears in Copilot Chat.
3. Run the prompt once and confirm the assistant adopts concise, surgical, verification-minded behavior.

## Why This Remains Separate From The Plugin

Prompt files are a separate VS Code customization primitive from plugin-packaged agents and skills.

The plugin package intentionally focuses on:

- the custom agent
- the skill

That keeps the prompt slice installable on its own and avoids mixing distinct delivery mechanisms.

## Relationship To The Other Copilot Folders

- `../instruction/` → Copilot always-on rules slice
- `../plugin/karpathy-caveman/` → Copilot agent + skill slice
- `../karpathy-caveman/` → full Copilot repo-file source bundle
- `../../docs/compatibility-matrix.md` → cross-assistant mapping

## Limitations

This slice is manual, not always-on. It does not replace repository instruction files when you need persistent defaults.

## Updating

1. Edit `../../.github/prompts/karpathy-caveman.prompt.md` if the prompt behavior changes.
2. Keep this slice aligned with the root direct-use copy.
3. Re-run `../../scripts/validate_repo.py` before publishing or copying updates.

## License

This repository is MIT licensed. See `../../LICENSE`.