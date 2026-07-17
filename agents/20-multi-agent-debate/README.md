# Multi-Agent Debate System

[![Python 3.11](https://img.shields.io/badge/Python-3.11-22d3ee.svg)](../../GETTING_STARTED.md) [![LangChain](https://img.shields.io/badge/framework-LangChain-a78bfa.svg)](../../PROJECT_INDEX.md) [![Difficulty: Advanced](https://img.shields.io/badge/difficulty-advanced-fbbf24.svg)](metadata.yaml) [![License: MIT](https://img.shields.io/badge/license-MIT-34d399.svg)](../../LICENSE)

| Field | Value |
|---|---|
| Category | Multi-Agent Systems / Research Agents |
| Framework | LangChain |
| Model | `gpt-4o` |
| Difficulty | Advanced |
| Original author | `ashishpatel26` |
Two AI agents debate any topic from opposing sides, with an impartial AI judge declaring a winner.

**Framework**: LangChain (multi-agent)
**LLM**: GPT-4o-mini (debaters) + GPT-4o (judge)

## Overview

Two AI agents debate any topic with an AI judge scoring the outcome.

## Features

- Two AI agents debate any topic with an AI judge scoring the outcome.
- Uses LangChain with `gpt-4o`.
- Keeps dependencies and credentials isolated inside this project.
- Metadata tags: `multi-agent, debate, reasoning, research, argumentation`.

## Architecture

```
Topic → [PRO Agent] ↔ [CON Agent] (N rounds) → [Judge Agent] → Verdict
```

The judge scores each side and provides a balanced synthesis conclusion.

---

## Tech stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Agent framework | LangChain |
| Model | `gpt-4o` |
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
python agent.py --topic "AI will eliminate more jobs than it creates"
python agent.py --topic "Remote work is better than office work" --rounds 3
python agent.py --topic "Cryptocurrency will replace fiat currency" --rounds 2
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

![Multi-Agent Debate System screenshot placeholder](../../assets/screenshots/20-multi-agent-debate.svg)

This is a labeled documentation placeholder, not a claimed live result. Replace it with a redacted screenshot after a credentialed test run.

## Contributing

Follow the root [contribution guide](../../CONTRIBUTING.md). Keep changes scoped, preserve behavior unless fixing a documented defect, and include validation evidence.

## License and credits

This project is included under the repository [MIT License](../../LICENSE). Original author metadata credits `ashishpatel26`; see [Attribution](../../ATTRIBUTION.md).

## Support

Use the repository issue tracker. Include the project path, operating system, Python version, command, and redacted error output.
