# Karpathy Caveman Always-On Instructions

This folder is the canonical Copilot **instruction slice**.

Use it when you want repository-wide Copilot defaults without taking the prompt slice or the plugin slice.

## What This Slice Contains

- `.github/copilot-instructions.md` → Copilot-specific always-on adapter
- `AGENTS.md` → shared canonical always-on rules file

The mode encoded here emphasizes:

- think before coding
- prefer the smallest sufficient solution
- keep edits surgical
- answer first and stay concise
- switch to normal technical English when clarity matters more than compression

## Canonical Source

The canonical rule set lives at `../../AGENTS.md`.

For the full Copilot repo-file source bundle, use `../karpathy-caveman/`.

## When To Use This Slice

Use this slice when:

- you want always-on Copilot behavior
- you do not need a prompt or plugin package in the same bundle
- you want a clear separation between always-on rules and other Copilot delivery primitives

## How To Copy It Correctly

### Copilot-only repository

Copy:

```text
<repo>/
└─ .github/
   └─ copilot-instructions.md
```

That is enough if the target repository is only meant for Copilot and you want the Copilot-specific adapter.

### Mixed-assistant repository

Copy:

```text
<repo>/
└─ AGENTS.md
```

Add `.github/copilot-instructions.md` only if you explicitly want the Copilot-only adapter alongside the shared canonical rules.

For assistants that can already use `AGENTS.md`, prefer keeping `AGENTS.md` as the single always-on source to avoid duplicated instruction context.

## How To Verify

1. Confirm the target repository contains `AGENTS.md` and/or `.github/copilot-instructions.md` at the exact paths you intended.
2. Ask Copilot to summarize the repository rules it sees.
3. Run one short coding task and check for concise planning, surgical edits, and explicit verification behavior.

## When To Use Something Else

- Choose `../prompt/` when you want an explicit `/karpathy-caveman` trigger.
- Choose `../plugin/karpathy-caveman/` when you want a packaged Copilot agent + skill rollout.
- Choose `../karpathy-caveman/` when you want one source bundle containing all Copilot repository-file artifacts.

## Limitations

Like other instruction files, this slice primarily affects Copilot chat and agent workflows. It does **not** fully control inline ghost-text autocomplete.

## Updating

1. Edit `../../AGENTS.md` first when the canonical rule set changes.
2. Keep `.github/copilot-instructions.md` semantically aligned with it.
3. Re-run `../../scripts/validate_repo.py` before publishing or copying updates.

## License

This repository is MIT licensed. See `../../LICENSE`.