# Job Application Agent

[![Python 3.11](https://img.shields.io/badge/Python-3.11-22d3ee.svg)](../../GETTING_STARTED.md) [![CrewAI](https://img.shields.io/badge/framework-CrewAI-a78bfa.svg)](../../PROJECT_INDEX.md) [![Difficulty: Intermediate](https://img.shields.io/badge/difficulty-intermediate-fbbf24.svg)](metadata.yaml) [![License: MIT](https://img.shields.io/badge/license-MIT-34d399.svg)](../../LICENSE)

| Field | Value |
|---|---|
| Category | Workflows / Multi-Agent Systems |
| Framework | CrewAI |
| Model | `gpt-4o-mini` |
| Difficulty | Intermediate |
| Original author | `ashishpatel26` |
CrewAI agent that generates a complete job application package: cover letter, tailored resume bullets, interview questions, and salary range.

**Framework**: CrewAI
**LLM**: GPT-4o-mini

## Overview

Generates cover letter, interview prep, and salary range from job description + candidate profile.

## Features

- Generates cover letter, interview prep, and salary range from job description + candidate profile.
- Uses CrewAI with `gpt-4o-mini`.
- Keeps dependencies and credentials isolated inside this project.
- Metadata tags: `hr, job-search, cover-letter, interview-prep, recruitment`.

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
# Uses built-in sample
python agent.py

# Your own job + profile
python agent.py \
  --job-desc "$(cat job_posting.txt)" \
  --candidate "$(cat my_profile.txt)"
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

## Output includes

- Tailored cover letter (250-300 words)
- Top 5 resume bullets to highlight
- 10 interview questions with answer frameworks
- Salary negotiation range

---

## Screenshots

![Job Application Agent screenshot placeholder](../../assets/screenshots/18-job-application-agent.svg)

This is a labeled documentation placeholder, not a claimed live result. Replace it with a redacted screenshot after a credentialed test run.

## Responsible use

Candidate profiles and job materials contain personal data. Review every generated claim, salary
estimate, and interview recommendation; never submit fabricated experience or use the output as an
autonomous employment decision.

## Contributing

Follow the root [contribution guide](../../CONTRIBUTING.md). Keep changes scoped, preserve behavior unless fixing a documented defect, and include validation evidence.

## License and credits

This project is included under the repository [MIT License](../../LICENSE). Original author metadata credits `ashishpatel26`; see [Attribution](../../ATTRIBUTION.md).

## Support

Use the repository issue tracker. Include the project path, operating system, Python version, command, and redacted error output.
