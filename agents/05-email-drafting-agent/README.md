# Email Drafting Agent

[![Python 3.11](https://img.shields.io/badge/Python-3.11-22d3ee.svg)](../../GETTING_STARTED.md) [![CrewAI](https://img.shields.io/badge/framework-CrewAI-a78bfa.svg)](../../PROJECT_INDEX.md) [![Difficulty: Beginner](https://img.shields.io/badge/difficulty-beginner-fbbf24.svg)](metadata.yaml) [![License: MIT](https://img.shields.io/badge/license-MIT-34d399.svg)](../../LICENSE)

| Field | Value |
|---|---|
| Category | Automation / Multi-Agent Systems |
| Framework | CrewAI |
| Model | `gpt-4o-mini` |
| Difficulty | Beginner |
| Original author | `ashishpatel26` |
A CrewAI two-agent system that drafts professional emails. An analyst agent extracts requirements, then a writer agent produces the final email.

**Framework**: CrewAI
**LLM**: GPT-4o-mini

## Overview

Two-agent CrewAI system that drafts professional emails from context.

## Features

- Two-agent CrewAI system that drafts professional emails from context.
- Uses CrewAI with `gpt-4o-mini`.
- Keeps dependencies and credentials isolated inside this project.
- Metadata tags: `email, communication, crewai, productivity`.

## Architecture

```
Context → [Analyst Agent] → Email Brief → [Writer Agent] → Final Email
```

---

## Tech stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Agent framework | CrewAI |
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

Copy `.env.example` to `.env`, replace placeholders locally, and never commit the resulting file.

## Running
```bash
# Default example
python agent.py

# Custom email
python agent.py \
  --context "Apologize for the delayed delivery of the software project" \
  --tone "apologetic but confident" \
  --recipient "the client project manager"
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

## Screenshots

![Email Drafting Agent screenshot placeholder](../../assets/screenshots/05-email-drafting-agent.svg)

This is a labeled documentation placeholder, not a claimed live result. Replace it with a redacted screenshot after a credentialed test run.

## Contributing

Follow the root [contribution guide](../../CONTRIBUTING.md). Keep changes scoped, preserve behavior unless fixing a documented defect, and include validation evidence.

## License and credits

This project is included under the repository [MIT License](../../LICENSE). Original author metadata credits `ashishpatel26`; see [Attribution](../../ATTRIBUTION.md).

## Support

Use the repository issue tracker. Include the project path, operating system, Python version, command, and redacted error output.
