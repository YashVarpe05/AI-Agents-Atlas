#!/usr/bin/env python3
"""Validate repository structure, metadata, docs, syntax, links, and secret hygiene."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "agents"
REQUIRED_ROOT_FILES = {
    "README.md",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "ARCHITECTURE.md",
    "GETTING_STARTED.md",
    "PROJECT_INDEX.md",
    "CHANGELOG.md",
    "FINAL_REPORT.md",
    "LICENSE",
    "ATTRIBUTION.md",
    "THIRD_PARTY_NOTICES.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
}
REQUIRED_PROJECT_FILES = {
    ".env.example",
    "README.md",
    "agent.py",
    "metadata.yaml",
    "requirements.txt",
}
REQUIRED_METADATA = {
    "title",
    "description",
    "author",
    "language",
    "framework",
    "tags",
    "industry",
    "difficulty",
    "llm",
    "entrypoint",
    "requirements",
    "license",
    "source",
    "provenance",
}
README_SECTIONS = {
    "overview",
    "features",
    "architecture",
    "tech stack",
    "installation",
    "environment variables",
    "running",
    "folder structure",
    "example",
    "screenshots",
    "contributing",
    "license and credits",
    "support",
}
IGNORED_PARTS = {".git", ".venv", "venv", "node_modules", "dist"}
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key": re.compile(r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY"),
}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def parse_metadata(path: Path) -> dict[str, object]:
    """Parse the flat metadata format used by local projects without a YAML dependency."""
    result: dict[str, object] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            result[key.strip()] = [item.strip() for item in value[1:-1].split(",") if item.strip()]
        else:
            result[key.strip()] = value.strip("\"'")
    return result


def iter_files(*suffixes: str):
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in IGNORED_PARTS for part in path.parts):
            continue
        if not suffixes or path.suffix.lower() in suffixes:
            yield path


def markdown_headings(path: Path) -> set[str]:
    headings = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{2,3}\s+(.+?)\s*$", line)
        if match:
            headings.add(re.sub(r"[^a-z0-9 ]", "", match.group(1).lower()).strip())
    return headings


def validate_root(errors: list[str]) -> None:
    missing = sorted(name for name in REQUIRED_ROOT_FILES if not (ROOT / name).is_file())
    if missing:
        errors.append(f"root: missing required files: {', '.join(missing)}")
    if not (ROOT / "web" / "package-lock.json").is_file():
        errors.append("web: package-lock.json is required for reproducible npm installs")


def validate_projects(errors: list[str]) -> int:
    projects = sorted(path for path in AGENTS.iterdir() if path.is_dir())
    seen_titles: set[str] = set()

    for project in projects:
        missing = sorted(name for name in REQUIRED_PROJECT_FILES if not (project / name).is_file())
        if missing:
            errors.append(f"{project.relative_to(ROOT)}: missing {', '.join(missing)}")
            continue

        metadata = parse_metadata(project / "metadata.yaml")
        missing_keys = sorted(REQUIRED_METADATA - metadata.keys())
        if missing_keys:
            errors.append(f"{project.relative_to(ROOT)}: metadata missing {', '.join(missing_keys)}")

        title = str(metadata.get("title", ""))
        if title in seen_titles:
            errors.append(f"{project.relative_to(ROOT)}: duplicate metadata title {title!r}")
        seen_titles.add(title)

        if metadata.get("difficulty") not in {"beginner", "intermediate", "advanced"}:
            errors.append(f"{project.relative_to(ROOT)}: invalid difficulty")
        if metadata.get("language") != "python":
            errors.append(f"{project.relative_to(ROOT)}: local agents must declare language: python")

        entrypoint = project / str(metadata.get("entrypoint", ""))
        requirements = project / str(metadata.get("requirements", ""))
        if not entrypoint.is_file():
            errors.append(f"{project.relative_to(ROOT)}: metadata entrypoint does not exist")
        if not requirements.is_file():
            errors.append(f"{project.relative_to(ROOT)}: metadata requirements file does not exist")

        headings = markdown_headings(project / "README.md")
        missing_sections = sorted(README_SECTIONS - headings)
        if missing_sections:
            errors.append(
                f"{project.relative_to(ROOT)}/README.md: missing sections: "
                + ", ".join(missing_sections)
            )

        screenshot = ROOT / "assets" / "screenshots" / f"{project.name}.svg"
        if not screenshot.is_file():
            errors.append(f"{project.relative_to(ROOT)}: missing screenshot placeholder")

        env_text = (project / ".env.example").read_text(encoding="utf-8")
        if "OPENAI_API_KEY=" not in env_text:
            errors.append(f"{project.relative_to(ROOT)}/.env.example: missing OPENAI_API_KEY")
        for line_number, line in enumerate(env_text.splitlines(), start=1):
            if "=" not in line or line.lstrip().startswith("#"):
                continue
            _, value = line.split("=", 1)
            if value and not any(marker in value.lower() for marker in ("your_", "example", "localhost")):
                errors.append(
                    f"{project.relative_to(ROOT)}/.env.example:{line_number}: value is not an obvious placeholder"
                )

    return len(projects)


def validate_python(errors: list[str]) -> int:
    count = 0
    for path in iter_files(".py"):
        count += 1
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: Python parse failed: {exc}")
    return count


def validate_links(errors: list[str]) -> int:
    count = 0
    for path in iter_files(".md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().strip("<>").split(maxsplit=1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            clean_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean_target:
                continue
            count += 1
            resolved = (path.parent / clean_target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")
    return count


def validate_secret_hygiene(errors: list[str]) -> int:
    scanned = 0
    for path in iter_files():
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".ico", ".lock"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scanned += 1
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: possible {label}")
    return scanned


def validate_generated_artifacts(errors: list[str]) -> None:
    forbidden_names = {
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        ".mypy_cache",
        ".playwright-cli",
        "qa-output",
    }
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        if path.name in forbidden_names or path.suffix.lower() in {".pyc", ".pyo"}:
            errors.append(f"generated artifact present: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_root(errors)
    projects = validate_projects(errors)
    python_files = validate_python(errors)
    links = validate_links(errors)
    text_files = validate_secret_hygiene(errors)
    validate_generated_artifacts(errors)

    if errors:
        print(f"Repository validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        "Repository validation passed: "
        f"{projects} projects, {python_files} Python files, "
        f"{links} local links, {text_files} text files scanned."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
