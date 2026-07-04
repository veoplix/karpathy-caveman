# [Karpathy Caveman](https://karpathy-caveman.veoplix.com)

Karpathy Caveman is a cross-assistant customization toolkit that merges:

- **Andrej Karpathy-style engineering discipline**
- **Caveman full-mode communication compression**

into one operating mode that can be delivered to:

1. **GitHub Copilot in VS Code**
2. **Claude Code**
3. **Codex**
4. **Cursor**

The goal is not to invent a different persona per product. The goal is to keep one coherent behavior model and then package it into the discovery formats each assistant actually understands.

## What The Idea Changes

Karpathy Caveman changes four things about coding assistance:

- **Reasoning discipline**
  - think before acting
  - avoid silent guessing
  - prefer the smallest sufficient solution
  - keep scope surgical
  - define and verify completion criteria

- **Communication style**
  - answer first
  - concise high-signal prose
  - no filler or hedging
  - exact technical tokens preserved

- **Safety and clarity behavior**
  - switch to normal technical English when risk, ambiguity, or safety makes compression unsafe
  - prefer explicit tradeoffs over confident bluffing

- **Default tradeoff**
  - bias toward **caution over speed**
  - use judgment for trivial tasks instead of forcing process everywhere

## Canonical Sources

This repository treats these files as the real source of truth:

- `AGENTS.md` → canonical assistant-agnostic always-on rules
- `.agents/skills/karpathy-caveman/SKILL.md` → canonical shared skill

Everything else is either:

- an assistant-specific adapter
- an assistant-native bundle
- a mirrored copy of the canonical source

When the mode itself changes, update those canonical files first and then sync the assistant-specific mirrors.

## Discovery Strategy

Some assistants scan overlapping compatibility roots. If the same skill or subagent is mirrored into every possible root, discovery can become ambiguous or duplicated.

This repository avoids that by:

- keeping exactly one shared root skill in `.agents/skills/`
- keeping assistant bundles under dedicated package folders
- using root direct-use files only where they do not create cross-tool duplicate discovery problems
- omitting a root `.github/copilot-instructions.md` file because Copilot can already use `AGENTS.md` and a second root always-on file wastes context

## Delivery Layers In This Repository

The repository has four delivery layers:

1. **Canonical shared core**
	- `AGENTS.md`
	- `.agents/skills/karpathy-caveman/SKILL.md`

2. **Root direct-use files for this repository itself**
	- `.github/prompts/karpathy-caveman.prompt.md`
	- `.github/agents/karpathy-caveman.agent.md`
	- `.cursor/rules/karpathy-caveman.mdc`
	- `.cursor/agents/karpathy-caveman.md`
	- `CLAUDE.md`

3. **Copyable assistant bundles**
	- `copilot/karpathy-caveman/`
	- `claude/karpathy-caveman/`
	- `codex/karpathy-caveman/`
	- `cursor/karpathy-caveman/`

4. **Copilot-specific slice bundles**
	- `copilot/instruction/`
	- `copilot/prompt/`
	- `copilot/plugin/karpathy-caveman/`

## Root Direct-Use Files In This Repository

| Assistant | Root files in this repo | Bundle or slice to copy |
| --- | --- | --- |
| GitHub Copilot / VS Code | `AGENTS.md`, `.github/prompts/karpathy-caveman.prompt.md`, `.github/agents/karpathy-caveman.agent.md`, `.agents/skills/karpathy-caveman/SKILL.md` | `copilot/karpathy-caveman/` (repo-file source bundle), `copilot/instruction/`, `copilot/prompt/`, `copilot/plugin/karpathy-caveman/` |
| Claude Code | `AGENTS.md`, `CLAUDE.md` | `claude/karpathy-caveman/` |
| Codex | `AGENTS.md`, `.agents/skills/karpathy-caveman/SKILL.md` | `codex/karpathy-caveman/` |
| Cursor | `AGENTS.md`, `.agents/skills/karpathy-caveman/SKILL.md`, `.cursor/rules/karpathy-caveman.mdc`, `.cursor/agents/karpathy-caveman.md` | `cursor/karpathy-caveman/` |

For Copilot, the full `copilot/karpathy-caveman/` folder is a **source bundle** that contains all repo-file artifacts in one place. It is not the same thing as the plugin package, and it is not an instruction to copy every file blindly into every target repository.

## How To Choose The Right Path

### Mixed-assistant repository

Use:

- `AGENTS.md` as the canonical repo rule set
- `.agents/skills/karpathy-caveman/SKILL.md` as the shared portable skill
- the relevant assistant bundle under `copilot/`, `claude/`, `codex/`, or `cursor/`

For Copilot in a mixed-assistant repository, prefer `AGENTS.md` as the always-on source. Add `.github/copilot-instructions.md` only if you specifically want the Copilot-only adapter as well.

### Copilot-only repository

Choose one of these depending on what you actually need:

- `copilot/karpathy-caveman/` when you want one folder containing all Copilot repo-file artifacts as a source bundle
- `copilot/instruction/` when you only want always-on instructions
- `copilot/prompt/` when you only want `/karpathy-caveman`
- `copilot/plugin/karpathy-caveman/` when you want the publishable plugin package

### Claude-only, Codex-only, or Cursor-only repository

Copy the corresponding assistant bundle directory directly.

## Repository Layout

```text
karpathy-caveman/
├─ .agents/skills/karpathy-caveman/SKILL.md
├─ .cursor/
│  ├─ agents/karpathy-caveman.md
│  └─ rules/karpathy-caveman.mdc
├─ .github/
│  ├─ agents/karpathy-caveman.agent.md
│  └─ prompts/karpathy-caveman.prompt.md
├─ AGENTS.md
├─ CLAUDE.md
├─ claude/
│  └─ karpathy-caveman/
├─ copilot/
│  ├─ instruction/
│  ├─ karpathy-caveman/
│  ├─ plugin/
│  │  └─ karpathy-caveman/
│  └─ prompt/
├─ codex/
│  └─ karpathy-caveman/
├─ cursor/
│  └─ karpathy-caveman/
├─ docs/
│  ├─ compatibility-matrix.md
│  └─ rollout-plan.md
└─ scripts/validate_repo.py
```

## How To Verify A Rollout

### In this repository

Run:

```text
python scripts/validate_repo.py
```

That validator checks:

- required files
- forbidden duplicate root paths
- frontmatter structure
- mirror drift
- JSON and TOML parseability
- relative Markdown links

### In a target repository

Verify three things:

1. **Exact file placement**
	- files must land at the paths documented by the chosen bundle or slice

2. **Assistant discovery**
	- ask the assistant to summarize active repo rules
	- confirm prompts, agents, rules, or skills appear where the target product exposes them

3. **Behavior on a small task**
	- test one coding request and check for concise reasoning, surgical edits, explicit assumptions, and verification-minded behavior

## Important Limitations

### 1) This mainly shapes chat, agent, instruction, skill, and rule workflows

These files do **not** fully control inline ghost-text autocomplete.

### 2) Copilot repo files and Copilot plugin packaging are separate delivery mechanisms

`copilot/karpathy-caveman/` is a repo-file source bundle.

`copilot/plugin/karpathy-caveman/` is a plugin package.

Use the plugin when you want installable Copilot plugin distribution. Use the repo-file bundle or slices when you want files copied into a repository.

### 3) The default mode is Caveman full-mode, not ultra

The communication style stays terse and high-signal without becoming cryptic.

### 4) The merged mode still prefers caution over speed

That bias is inherited from the Karpathy principles. For trivial tasks, use judgment.

## Maintenance Model

1. Edit `AGENTS.md` and `.agents/skills/karpathy-caveman/SKILL.md` first.
2. Keep assistant-specific adapters and mirrored files aligned with them.
3. Re-run `scripts/validate_repo.py`.
4. Update the bundle READMEs and the compatibility docs whenever delivery guidance changes.
5. Avoid introducing overlapping discovery roots unless a platform explicitly requires them.

## More Detail

See:

- `copilot/karpathy-caveman/README.md`
- `copilot/instruction/README.md`
- `copilot/prompt/README.md`
- `copilot/plugin/karpathy-caveman/README.md`
- `claude/karpathy-caveman/README.md`
- `codex/karpathy-caveman/README.md`
- `cursor/karpathy-caveman/README.md`
- `docs/compatibility-matrix.md`
- `docs/rollout-plan.md`

## License

This repository is MIT licensed. See `LICENSE`.

## Source Inspirations And Attribution

This repository is inspired by:

- `multica-ai/andrej-karpathy-skills`
- `JuliusBrussee/caveman`

Conceptual inheritance:

- Karpathy source → reasoning discipline, simplicity, surgical scope, verification
- Caveman source → communication compression, exact technical fidelity, clarity override

If you copy upstream wording directly into released artifacts, preserve their MIT notices where required.
