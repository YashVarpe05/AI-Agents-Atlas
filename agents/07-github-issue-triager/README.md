# GitHub Issue Triager

[![Python 3.11](https://img.shields.io/badge/Python-3.11-22d3ee.svg)](../../GETTING_STARTED.md) [![LangChain](https://img.shields.io/badge/framework-LangChain-a78bfa.svg)](../../PROJECT_INDEX.md) [![Difficulty: Intermediate](https://img.shields.io/badge/difficulty-intermediate-fbbf24.svg)](metadata.yaml) [![License: MIT](https://img.shields.io/badge/license-MIT-34d399.svg)](../../LICENSE)

| Field | Value |
|---|---|
| Category | Developer Tools / Automation |
| Framework | LangChain |
| Model | `gpt-4o-mini` |
| Difficulty | Intermediate |
| Upstream provenance | [Attribution](../../ATTRIBUTION.md) |
Automatically triages GitHub issues: assigns severity, category, labels, and routing recommendations.

**Framework**: LangChain
**LLM**: GPT-4o-mini

## Overview

Automatically triages GitHub issues with severity, category, and routing recommendations.

## Features

- Automatically triages GitHub issues with severity, category, and routing recommendations.
- Uses LangChain with `gpt-4o-mini`.
- Keeps dependencies and credentials isolated inside this project.
- Metadata tags: `github, devops, triage, issue-management, automation`.

## Architecture

```text
CLI or file input -> prompt/tool pipeline -> language model -> structured output
```

## Tech stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Agent framework | LangChain |
| Model | `gpt-4o-mini` |
| Configuration | `python-dotenv` and `.env` |

## Installation
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Environment variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Authenticates OpenAI model and embedding requests |
| `GITHUB_TOKEN` | No | Raises GitHub API limits for repository requests; optional |

Copy `.env.example` to `.env`, replace placeholders locally, and never commit the resulting file.

## Running
```bash
# From a GitHub URL
python agent.py --issue-url https://github.com/owner/repo/issues/123

# From title + body text
python agent.py --title "App crashes on login" --body "Steps: 1. Open app 2. Click login 3. App crashes"
```

## Folder structure

```text
.
|-- .env.example       Credential contract with placeholders
|-- README.md          Setup, usage, and project notes
|-- agent.py           Command-line entry point
|-- metadata.yaml      Catalog metadata and attribution
`-- requirements.txt   Direct Python dependencies
```

## Example

Verify the command surface without making a provider request:

```bash
python agent.py --help
```

Then use the documented command in **Running** with non-sensitive test input.

## Output

```
🔴 Severity: CRITICAL (Priority: 9/10)
📁 Category: bug
👤 Assignee: backend team
🏷️  Labels: bug, critical, authentication
📝 Summary: Authentication crash affecting all users on login
```

---

## Screenshots

![GitHub Issue Triager screenshot placeholder](../../assets/screenshots/07-github-issue-triager.svg)

This is a labeled documentation placeholder, not a claimed live result. Replace it with a redacted screenshot after a credentialed test run.

## Contributing

Follow the root [contribution guide](../../CONTRIBUTING.md). Keep changes scoped, preserve behavior unless fixing a documented defect, and include validation evidence.

## License and credits

This project is included under the repository [MIT License](../../LICENSE). Original upstream authorship and source provenance are preserved in [Attribution](../../ATTRIBUTION.md).

## Support

Use the repository issue tracker. Include the project path, operating system, Python version, command, and redacted error output.
