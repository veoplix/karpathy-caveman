from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "CLAUDE.md",
    ROOT / "index.html",
    ROOT / ".github" / "prompts" / "karpathy-caveman.prompt.md",
    ROOT / ".github" / "agents" / "karpathy-caveman.agent.md",
    ROOT / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
    ROOT / ".cursor" / "rules" / "karpathy-caveman.mdc",
    ROOT / ".cursor" / "agents" / "karpathy-caveman.md",
    ROOT / "README.md",
    ROOT / "docs" / "compatibility-matrix.md",
    ROOT / "docs" / "rollout-plan.md",
    ROOT / "copilot" / "instruction" / "AGENTS.md",
    ROOT / "copilot" / "instruction" / ".github" / "copilot-instructions.md",
    ROOT / "copilot" / "instruction" / "README.md",
    ROOT / "copilot" / "karpathy-caveman" / "AGENTS.md",
    ROOT / "copilot" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
    ROOT / "copilot" / "karpathy-caveman" / ".github" / "copilot-instructions.md",
    ROOT / "copilot" / "karpathy-caveman" / ".github" / "prompts" / "karpathy-caveman.prompt.md",
    ROOT / "copilot" / "karpathy-caveman" / ".github" / "agents" / "karpathy-caveman.agent.md",
    ROOT / "copilot" / "karpathy-caveman" / "README.md",
    ROOT / "copilot" / "prompt" / "karpathy-caveman.prompt.md",
    ROOT / "copilot" / "prompt" / "README.md",
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / "README.md",
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / "agents" / "karpathy-caveman.agent.md",
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / "skills" / "karpathy-caveman" / "SKILL.md",
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / ".github" / "plugin" / "plugin.json",
    ROOT / "claude" / "karpathy-caveman" / "AGENTS.md",
    ROOT / "claude" / "karpathy-caveman" / "CLAUDE.md",
    ROOT / "claude" / "karpathy-caveman" / ".claude" / "skills" / "karpathy-caveman" / "SKILL.md",
    ROOT / "claude" / "karpathy-caveman" / ".claude" / "agents" / "karpathy-caveman.md",
    ROOT / "claude" / "karpathy-caveman" / "README.md",
    ROOT / "codex" / "karpathy-caveman" / "AGENTS.md",
    ROOT / "codex" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
    ROOT / "codex" / "karpathy-caveman" / ".codex" / "agents" / "karpathy-caveman.toml",
    ROOT / "codex" / "karpathy-caveman" / "README.md",
    ROOT / "cursor" / "karpathy-caveman" / "AGENTS.md",
    ROOT / "cursor" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
    ROOT / "cursor" / "karpathy-caveman" / ".cursor" / "rules" / "karpathy-caveman.mdc",
    ROOT / "cursor" / "karpathy-caveman" / ".cursor" / "agents" / "karpathy-caveman.md",
    ROOT / "cursor" / "karpathy-caveman" / "README.md",
]

FORBIDDEN_ROOT_PATHS = [
    ROOT / ".github" / "copilot-instructions.md",
    ROOT / ".github" / "skills",
    ROOT / ".claude" / "skills",
    ROOT / ".claude" / "agents",
    ROOT / ".codex" / "agents",
]

FRONTMATTER_RULES = {
    ROOT / ".github" / "prompts" / "karpathy-caveman.prompt.md": {"description", "name"},
    ROOT / ".github" / "agents" / "karpathy-caveman.agent.md": {"name", "description"},
    ROOT / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md": {"name", "description"},
    ROOT / ".cursor" / "rules" / "karpathy-caveman.mdc": {"description", "alwaysApply"},
    ROOT / ".cursor" / "agents" / "karpathy-caveman.md": {"name", "description"},
    ROOT / "copilot" / "prompt" / "karpathy-caveman.prompt.md": {"description", "name"},
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / "agents" / "karpathy-caveman.agent.md": {"name", "description"},
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / "skills" / "karpathy-caveman" / "SKILL.md": {"name", "description"},
    ROOT / "copilot" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md": {"name", "description"},
    ROOT / "copilot" / "karpathy-caveman" / ".github" / "prompts" / "karpathy-caveman.prompt.md": {"description", "name"},
    ROOT / "copilot" / "karpathy-caveman" / ".github" / "agents" / "karpathy-caveman.agent.md": {"name", "description"},
    ROOT / "claude" / "karpathy-caveman" / ".claude" / "skills" / "karpathy-caveman" / "SKILL.md": {"name", "description"},
    ROOT / "claude" / "karpathy-caveman" / ".claude" / "agents" / "karpathy-caveman.md": {"name", "description"},
    ROOT / "codex" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md": {"name", "description"},
    ROOT / "cursor" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md": {"name", "description"},
    ROOT / "cursor" / "karpathy-caveman" / ".cursor" / "rules" / "karpathy-caveman.mdc": {"description", "alwaysApply"},
    ROOT / "cursor" / "karpathy-caveman" / ".cursor" / "agents" / "karpathy-caveman.md": {"name", "description"},
}

SINGLE_HEADING_RULES = {
    ROOT / "README.md": "# Karpathy Caveman",
    ROOT / "AGENTS.md": "# AGENTS.md",
    ROOT / "CLAUDE.md": "# CLAUDE.md",
    ROOT / ".github" / "agents" / "karpathy-caveman.agent.md": "# Karpathy Caveman Agent",
    ROOT / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md": "# Karpathy Caveman",
    ROOT / ".cursor" / "rules" / "karpathy-caveman.mdc": "# Karpathy Caveman Cursor Rule",
    ROOT / "copilot" / "instruction" / "README.md": "# Karpathy Caveman Always-On Instructions",
    ROOT / "copilot" / "karpathy-caveman" / "README.md": "# Karpathy Caveman for GitHub Copilot",
    ROOT / "copilot" / "prompt" / "README.md": "# Karpathy Caveman Prompt",
    ROOT / "copilot" / "plugin" / "karpathy-caveman" / "README.md": "# Karpathy Caveman Plugin",
    ROOT / "claude" / "karpathy-caveman" / "README.md": "# Karpathy Caveman for Claude Code",
    ROOT / "codex" / "karpathy-caveman" / "README.md": "# Karpathy Caveman for Codex",
    ROOT / "cursor" / "karpathy-caveman" / "README.md": "# Karpathy Caveman for Cursor",
    ROOT / "docs" / "compatibility-matrix.md": "# Compatibility Matrix",
    ROOT / "docs" / "rollout-plan.md": "# Rollout Plan",
}

MIRROR_GROUPS = [
    [
        ROOT / "AGENTS.md",
        ROOT / "copilot" / "instruction" / "AGENTS.md",
        ROOT / "copilot" / "karpathy-caveman" / "AGENTS.md",
        ROOT / "claude" / "karpathy-caveman" / "AGENTS.md",
        ROOT / "codex" / "karpathy-caveman" / "AGENTS.md",
        ROOT / "cursor" / "karpathy-caveman" / "AGENTS.md",
    ],
    [ROOT / "CLAUDE.md", ROOT / "claude" / "karpathy-caveman" / "CLAUDE.md"],
    [
        ROOT / "copilot" / "prompt" / "karpathy-caveman.prompt.md",
        ROOT / ".github" / "prompts" / "karpathy-caveman.prompt.md",
        ROOT / "copilot" / "karpathy-caveman" / ".github" / "prompts" / "karpathy-caveman.prompt.md",
    ],
    [
        ROOT / "copilot" / "plugin" / "karpathy-caveman" / "agents" / "karpathy-caveman.agent.md",
        ROOT / ".github" / "agents" / "karpathy-caveman.agent.md",
        ROOT / "copilot" / "karpathy-caveman" / ".github" / "agents" / "karpathy-caveman.agent.md",
    ],
    [
        ROOT / "copilot" / "instruction" / ".github" / "copilot-instructions.md",
        ROOT / "copilot" / "karpathy-caveman" / ".github" / "copilot-instructions.md",
    ],
    [
        ROOT / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
        ROOT / "copilot" / "plugin" / "karpathy-caveman" / "skills" / "karpathy-caveman" / "SKILL.md",
        ROOT / "copilot" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
        ROOT / "claude" / "karpathy-caveman" / ".claude" / "skills" / "karpathy-caveman" / "SKILL.md",
        ROOT / "codex" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
        ROOT / "cursor" / "karpathy-caveman" / ".agents" / "skills" / "karpathy-caveman" / "SKILL.md",
    ],
    [ROOT / ".cursor" / "rules" / "karpathy-caveman.mdc", ROOT / "cursor" / "karpathy-caveman" / ".cursor" / "rules" / "karpathy-caveman.mdc"],
    [ROOT / ".cursor" / "agents" / "karpathy-caveman.md", ROOT / "cursor" / "karpathy-caveman" / ".cursor" / "agents" / "karpathy-caveman.md"],
]

MARKDOWN_FILES = [path for path in REQUIRED_FILES if path.suffix in {".md", ".mdc"}]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HTML_FILES = [ROOT / "index.html"]
HTML_HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    closing_delimiter = "\n---\n"
    closing_count = text.count(closing_delimiter)
    if closing_count != 1:
        raise ValueError(
            f"expected exactly one closing frontmatter delimiter, found {closing_count}"
        )
    end = text.find(closing_delimiter, 4)
    raw = text[4:end]
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - "):
            if current_key is not None:
                data[current_key] = data.get(current_key, "") + line.strip()
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip()
    return data


def ensure_exists(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")


def ensure_forbidden_absent(errors: list[str]) -> None:
    for path in FORBIDDEN_ROOT_PATHS:
        if path.exists():
            errors.append(f"forbidden root path present: {path.relative_to(ROOT)}")


def validate_json(errors: list[str]) -> None:
    path = ROOT / "copilot" / "plugin" / "karpathy-caveman" / ".github" / "plugin" / "plugin.json"
    try:
        data = json.loads(read_text(path))
    except Exception as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return
    for key in ["name", "description", "version", "license", "agents", "skills"]:
        if key not in data:
            errors.append(f"plugin manifest missing key `{key}`: {path.relative_to(ROOT)}")


def validate_toml(errors: list[str]) -> None:
    path = ROOT / "codex" / "karpathy-caveman" / ".codex" / "agents" / "karpathy-caveman.toml"
    if tomllib is None:
        errors.append("tomllib unavailable; use Python 3.11+ to validate Codex agent TOML")
        return
    try:
        data = tomllib.loads(read_text(path))
    except Exception as exc:
        errors.append(f"invalid TOML in {path.relative_to(ROOT)}: {exc}")
        return
    for key in ["name", "description", "developer_instructions"]:
        if key not in data:
            errors.append(f"Codex agent TOML missing key `{key}`: {path.relative_to(ROOT)}")


def validate_frontmatter(errors: list[str]) -> None:
    for path, required_keys in FRONTMATTER_RULES.items():
        try:
            data = parse_frontmatter(read_text(path))
        except Exception as exc:
            errors.append(f"invalid frontmatter in {path.relative_to(ROOT)}: {exc}")
            continue
        for key in required_keys:
            if key not in data:
                errors.append(f"frontmatter missing `{key}` in {path.relative_to(ROOT)}")


def validate_single_headings(errors: list[str]) -> None:
    for path, heading in SINGLE_HEADING_RULES.items():
        count = sum(1 for line in read_text(path).splitlines() if line == heading)
        if count != 1:
            errors.append(
                f"expected heading `{heading}` exactly once in {path.relative_to(ROOT)}; found {count}"
            )


def validate_mirrors(errors: list[str]) -> None:
    for group in MIRROR_GROUPS:
        baseline = read_text(group[0])
        for path in group[1:]:
            if read_text(path) != baseline:
                errors.append(
                    "mirror drift: "
                    + ", ".join(str(item.relative_to(ROOT)) for item in group)
                )
                break


def validate_links(errors: list[str]) -> None:
    for path in MARKDOWN_FILES:
        text = read_text(path)
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            target_path = (path.parent / relative).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not target_path.exists():
                errors.append(f"broken relative link in {path.relative_to(ROOT)}: {target}")


def validate_html(errors: list[str]) -> None:
    for path in HTML_FILES:
        text = read_text(path)
        if "<title>" not in text or "</title>" not in text:
            errors.append(f"missing HTML title in {path.relative_to(ROOT)}")
        for match in HTML_HREF_RE.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "data:", "#")):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            target_path = (path.parent / relative).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"HTML link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not target_path.exists():
                errors.append(f"broken relative HTML link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    errors: list[str] = []
    ensure_exists(errors)
    ensure_forbidden_absent(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    validate_json(errors)
    validate_toml(errors)
    validate_frontmatter(errors)
    validate_single_headings(errors)
    validate_mirrors(errors)
    validate_links(errors)
    validate_html(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())