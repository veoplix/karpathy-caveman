# Karpathy Caveman Plugin

A VS Code GitHub Copilot agent plugin that packages:

- a **custom agent**: `Karpathy Caveman`
- a **skill**: `karpathy-caveman`

This is the canonical Copilot **plugin slice** inside the larger `karpathy-caveman` repository.

For the full Copilot repo-file source bundle, use `../../karpathy-caveman/`.

## What This Plugin Changes

The plugin packages the same Karpathy-Caveman operating model into Copilot plugin payloads:

- think before coding
- avoid silent assumptions
- prefer the smallest sufficient solution
- keep changes surgical
- answer first in concise high-signal prose
- preserve exact technical tokens
- switch to normal technical English when safety or ambiguity requires it

## When To Use This Slice

Use this slice when:

- you want a publishable Copilot plugin package
- you want a packaged agent + skill rollout rather than repository files
- you want the agent picker and plugin skill behavior without managing prompt or instruction files in the same package

If you also want repo-wide always-on rules in the target repository, combine the plugin with `AGENTS.md` or the instruction slice.

## Why This Plugin Only Bundles The Agent And Skill

The larger repository also contains:

- a Copilot repo-file source bundle
- a standalone slash-command prompt slice
- a standalone always-on instruction slice
- Claude, Codex, and Cursor bundles

Those stay outside the plugin package intentionally.

Reason:

- official plugin documentation and plugin repositories center plugin payloads around `plugin.json`, `agents/`, `skills/`, optional hooks, and optional MCP
- prompt files are a separate VS Code primitive
- repository instruction files are a separate rollout mechanism from plugin distribution

## Plugin Package Layout

```text
karpathy-caveman/
├─ .github/plugin/plugin.json
├─ agents/karpathy-caveman.agent.md
├─ skills/karpathy-caveman/SKILL.md
└─ README.md
```

The files in this package mirror the canonical root assets:

- `agents/karpathy-caveman.agent.md` mirrors `../../../.github/agents/karpathy-caveman.agent.md`
- `skills/karpathy-caveman/SKILL.md` mirrors `../../../.agents/skills/karpathy-caveman/SKILL.md`

## How To Use After Installation

### Option 1: select the custom agent

Open Copilot Chat and select the **Karpathy Caveman** agent from the agent picker.

Use this when you want a persistent persona for the whole chat/session.

### Option 2: let the skill load when relevant

The `karpathy-caveman` skill is designed to activate for tasks that benefit from terse, surgical, minimal, verifiable engineering behavior.

Use this when the task naturally fits the mode.

## How To Verify

1. Confirm the plugin package contains `.github/plugin/plugin.json`, `agents/`, and `skills/`.
2. Install or publish it through your Copilot plugin workflow.
3. Confirm the `Karpathy Caveman` agent appears in the agent picker.
4. Run one small coding task and confirm concise, verification-minded behavior.

## What This Plugin Does Not Do By Itself

* It does **not** create repo-wide always-on instructions.
* It does **not** fully control inline autocomplete behavior.
* It does **not** bundle the separate `/karpathy-caveman` prompt file.

For those, use the sibling Copilot slices:

* `../../prompt/`
* `../../instruction/`

## Installation And Publishing Notes

This package is structured in the same broad style used by official/community Copilot plugin collections:

* plugin payload under a plugin package directory
* nested `.github/plugin/plugin.json`
* plugin-local `agents/`
* plugin-local `skills/`

For team rollout, publish or list the package from:

* `copilot/plugin/karpathy-caveman/`

through your chosen agent-plugin marketplace path.

## Updating

1. Edit the root canonical agent and skill sources first.
2. Keep this plugin slice aligned with those sources.
3. Re-run `../../../scripts/validate_repo.py` before publishing.

## Sources And Inspiration

This plugin is inspired by:

* `multica-ai/andrej-karpathy-skills`
* `JuliusBrussee/caveman`

## License

This repository is MIT licensed. See `../../../LICENSE`.

If you copy upstream wording directly, preserve their MIT notices where required.