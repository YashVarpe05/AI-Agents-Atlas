# Social Media Content Agent

[![Python 3.11](https://img.shields.io/badge/Python-3.11-22d3ee.svg)](../../GETTING_STARTED.md) [![CrewAI](https://img.shields.io/badge/framework-CrewAI-a78bfa.svg)](../../PROJECT_INDEX.md) [![Difficulty: Beginner](https://img.shields.io/badge/difficulty-beginner-fbbf24.svg)](metadata.yaml) [![License: MIT](https://img.shields.io/badge/license-MIT-34d399.svg)](../../LICENSE)

| Field | Value |
|---|---|
| Category | Automation / Marketing |
| Framework | CrewAI |
| Model | `gpt-4o-mini` |
| Difficulty | Beginner |
| Upstream provenance | [Attribution](../../ATTRIBUTION.md) |
Generates platform-optimized social media content (Twitter/X, LinkedIn, Instagram) from any topic.

**Framework**: CrewAI
**LLM**: GPT-4o-mini

## Overview

Generates platform-optimized content for Twitter, LinkedIn, and Instagram.

## Features

- Generates platform-optimized content for Twitter, LinkedIn, and Instagram.
- Uses CrewAI with `gpt-4o-mini`.
- Keeps dependencies and credentials isolated inside this project.
- Metadata tags: `social-media, content, marketing, crewai, copywriting`.

## Architecture

```text
CLI input -> specialist agents and tasks -> sequential CrewAI process -> final output
```

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
python agent.py --topic "The future of remote work"
python agent.py --topic "Product launch announcement" --brand "YourBrand" --platforms "twitter,linkedin"
```

---

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

![Social Media Content Agent screenshot placeholder](../../assets/screenshots/14-social-media-agent.svg)

This is a labeled documentation placeholder, not a claimed live result. Replace it with a redacted screenshot after a credentialed test run.

## Contributing

Follow the root [contribution guide](../../CONTRIBUTING.md). Keep changes scoped, preserve behavior unless fixing a documented defect, and include validation evidence.

## License and credits

This project is included under the repository [MIT License](../../LICENSE). Original upstream authorship and source provenance are preserved in [Attribution](../../ATTRIBUTION.md).

## Support

Use the repository issue tracker. Include the project path, operating system, Python version, command, and redacted error output.
