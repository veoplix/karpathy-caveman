# Karpathy Caveman for GitHub Copilot

This folder is the **repo-file source bundle** for GitHub Copilot in VS Code.

Use it when you want one place that contains every Copilot repository-file artifact for Karpathy Caveman, without having to assemble the instruction, prompt, and agent pieces manually.

## What This Bundle Changes

This bundle brings the Karpathy-Caveman operating model into Copilot repository files:

- **Reasoning and editing**
   - think before coding
   - avoid silent assumptions
   - prefer the smallest sufficient solution
   - keep edits surgical
   - verify outcomes explicitly

- **Communication**
   - answer first
   - concise high-signal phrasing
   - preserve exact technical tokens

- **Safety behavior**
   - switch to normal technical English when risk or ambiguity makes compressed wording unsafe

## Files

- `AGENTS.md` → canonical assistant-agnostic always-on rules
- `.agents/skills/karpathy-caveman/SKILL.md` → shared portable skill copy
- `.github/copilot-instructions.md` → optional Copilot-specific always-on adapter
- `.github/prompts/karpathy-caveman.prompt.md` → Copilot slash-command prompt
- `.github/agents/karpathy-caveman.agent.md` → Copilot-native agent file

## When To Use This Bundle

Use this bundle when:

- you want one folder that contains the full Copilot repository-file set
- you are preparing a Copilot rollout for a repository and want the files collected in one place
- you want both the shared core and the Copilot-native entrypoints available as source material

Do **not** read this bundle as an instruction to copy every file blindly into every target repository.

## When To Use A Narrower Copilot Slice Instead

Use the narrower slices when you only need one delivery primitive:

- `../instruction/` → always-on instruction slice only
- `../prompt/` → prompt slice only
- `../plugin/karpathy-caveman/` → plugin package only

## How To Install Correctly

Choose the target shape first.

### Mixed-assistant repository

Copy:

```text
<repo>/
├─ AGENTS.md
├─ .agents/
│  └─ skills/karpathy-caveman/SKILL.md
└─ .github/
    ├─ agents/karpathy-caveman.agent.md
    └─ prompts/karpathy-caveman.prompt.md
```

Add `.github/copilot-instructions.md` only if you intentionally want the Copilot-only adapter in addition to `AGENTS.md`.

### Copilot-only repository

Copy the pieces you actually want:

```text
<repo>/
└─ .github/
   ├─ agents/karpathy-caveman.agent.md
   ├─ prompts/karpathy-caveman.prompt.md
   └─ copilot-instructions.md
```

Add `AGENTS.md` as well if you want the shared canonical rules file present in that Copilot-only repository, or if the repository may later be shared with other assistants.

## How To Use After Install

- **Always-on behavior**: use `AGENTS.md` when you want the shared canonical rules, or `.github/copilot-instructions.md` when you specifically want the Copilot-only adapter.
- **Manual trigger**: use `/karpathy-caveman` if you copied `.github/prompts/karpathy-caveman.prompt.md`.
- **Native agent**: choose the `Karpathy Caveman` agent if you copied `.github/agents/karpathy-caveman.agent.md`.
- **Portable skill copy**: keep `.agents/skills/karpathy-caveman/SKILL.md` when you want the shared skill format available in a mixed-assistant repository.

## How To Verify

1. Confirm the copied files landed at the exact paths shown above.
2. Ask Copilot to summarize the repository rules it sees.
3. Confirm the prompt and agent appear in the UI if you copied them.
4. Run one small coding task and check for concise reasoning, surgical edits, and explicit verification behavior.

## Limitations

- This bundle mainly affects Copilot chat, agent, instruction, and prompt workflows.
- It does **not** fully control inline ghost-text autocomplete.
- The publishable plugin package is separate and lives at `../plugin/karpathy-caveman/`.

## Updating

1. Edit `../../AGENTS.md` and `../../.agents/skills/karpathy-caveman/SKILL.md` first when the mode changes.
2. Keep this source bundle aligned with those canonical files.
3. Re-run `../../scripts/validate_repo.py` in the source repository before publishing or copying updates.

## License

This repository is MIT licensed. See `../../LICENSE`.