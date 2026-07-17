#!/usr/bin/env python3
"""Resolve each Python project's requirements independently with uv."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def requirement_files() -> list[Path]:
    paths = list((ROOT / "agents").glob("*/requirements.txt"))
    paths.extend((ROOT / "crewai_mcp_course").glob("lesson_*/requirements.txt"))
    paths.append(ROOT / "templates" / "agent" / "requirements.txt")
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python-version", default="3.11")
    args = parser.parse_args()

    uv = shutil.which("uv")
    if not uv:
        print("uv is required: https://docs.astral.sh/uv/getting-started/installation/", file=sys.stderr)
        return 2

    failures: list[tuple[Path, str]] = []
    files = requirement_files()
    with tempfile.TemporaryDirectory(prefix="agent-dependency-check-") as temp_dir:
        for index, path in enumerate(files):
            output = Path(temp_dir) / f"resolved-{index}.txt"
            process = subprocess.run(
                [
                    uv,
                    "pip",
                    "compile",
                    str(path),
                    "--python-version",
                    args.python_version,
                    "--no-header",
                    "--output-file",
                    str(output),
                    "--quiet",
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            relative = path.relative_to(ROOT)
            if process.returncode:
                failures.append((relative, (process.stderr or process.stdout).strip()))
                print(f"FAIL {relative}")
            else:
                print(f"PASS {relative}")

    if failures:
        print(f"\n{len(failures)} dependency manifest(s) did not resolve:", file=sys.stderr)
        for path, error in failures:
            print(f"\n[{path}]\n{error}", file=sys.stderr)
        return 1

    print(f"\nDependency resolution passed for {len(files)} manifests on Python {args.python_version}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
