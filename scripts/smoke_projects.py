#!/usr/bin/env python3
"""Smoke project imports and agent CLI startup without provider requests."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_uv(requirements: Path, cwd: Path, command: list[str], timeout: int) -> tuple[bool, str]:
    process = subprocess.run(
        [
            "uv",
            "run",
            "--no-project",
            "--isolated",
            "--python",
            "3.11",
            "--with-requirements",
            str(requirements),
            *command,
        ],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    output = "\n".join(part.strip() for part in (process.stdout, process.stderr) if part.strip())
    return process.returncode == 0, output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=int, default=240, help="Seconds allowed per project")
    args = parser.parse_args()

    if not shutil.which("uv"):
        print("uv is required for isolated smoke environments", file=sys.stderr)
        return 2

    checks: list[tuple[str, Path, Path, list[str]]] = []
    for project in sorted((ROOT / "agents").glob("[0-9][0-9]-*")):
        checks.append(
            (
                str(project.relative_to(ROOT)),
                project / "requirements.txt",
                project,
                ["python", "agent.py", "--help"],
            )
        )

    for lesson in sorted((ROOT / "crewai_mcp_course").glob("lesson_*")):
        for source in sorted(lesson.glob("*.py")):
            smoke_code = f"import runpy; runpy.run_path({source.name!r}, run_name='repository_smoke')"
            if source.name == "mcp_server.py":
                smoke_code += "; server = runpy.run_path('mcp_server.py')['create_mcp_server'](); assert server.settings.port == 8000"
            checks.append(
                (
                    str(source.relative_to(ROOT)),
                    lesson / "requirements.txt",
                    lesson,
                    [
                        "python",
                        "-c",
                        smoke_code,
                    ],
                )
            )

    failures: list[tuple[str, str]] = []
    for label, requirements, cwd, command in checks:
        try:
            passed, output = run_uv(requirements, cwd, command, args.timeout)
        except subprocess.TimeoutExpired:
            passed, output = False, f"timed out after {args.timeout} seconds"
        print(f"{'PASS' if passed else 'FAIL'} {label}")
        if not passed:
            failures.append((label, output))

    if failures:
        print(f"\n{len(failures)} smoke check(s) failed:", file=sys.stderr)
        for label, output in failures:
            print(f"\n[{label}]\n{output}", file=sys.stderr)
        return 1

    print(f"\nCredential-free smoke checks passed for {len(checks)} entry points.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
