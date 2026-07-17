# CrewAI and MCP-style tool boundaries

This three-lesson course introduces CrewAI orchestration and then separates tool contracts from agent
roles with a small FastMCP companion server. It is an educational progression, not a production MCP
client implementation.

## What the lessons actually implement

| Lesson | Implementation | MCP status |
|---|---|---|
| [01](lesson_01/) | One CrewAI researcher and one task | No MCP code |
| [02](lesson_02/) | Sequential researcher, writer, and editor with local Python tools | MCP-style concepts only; tools run locally |
| [03](lesson_03/) | CrewAI wrappers plus a separate FastMCP project-data server | Companion server included; the agent uses equivalent local wrappers and does not connect to the server |

The distinction matters: lesson 03 lets readers compare a server contract with in-process tool
wrappers, but `agent.py` does not yet act as an MCP network client.

## Prerequisites

- Python 3.11
- An OpenAI API key
- A separate virtual environment for each lesson

## Installation

From the selected lesson folder:

```bash
uv venv --python 3.11 .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` and use
`Copy-Item .env.example .env`.

## Environment variables

| Variable | Lesson | Required | Purpose |
|---|---:|---|---|
| `OPENAI_API_KEY` | 01-03 | Yes | Authenticates model calls |

## Running

```bash
cd lesson_01
python agent.py
```

```bash
cd lesson_02
python agent.py --topic "AI agents in healthcare"
```

```bash
cd lesson_03
python agent.py
```

To inspect the companion server separately:

```bash
cd lesson_03
python mcp_server.py
```

Running the server does not automatically connect lesson 03's agent to it.

## Architecture

```text
Lesson 01: topic -> researcher -> answer
Lesson 02: topic -> researcher -> writer -> editor -> article
Lesson 03: project question -> local tool wrappers -> CrewAI roles -> status report
                                  |
                                  `-- companion FastMCP server exposes the same project domain
```

## Safety and limitations

- The researcher roles do not include live web search, so claims may be stale or unsupported.
- Generated reports require human review before business use.
- Lesson 03's sample project data is illustrative and contains no live system integration.
- Do not submit confidential data to a model provider without appropriate approval and controls.

## Validation

Repository QA parses all lesson Python files and resolves each requirements file independently on
Python 3.11. Credential-backed model execution is a manual step.

## Contributing

Keep each lesson independently runnable and update this table whenever implementation and stated MCP
capability diverge. Follow the root [contribution guide](../CONTRIBUTING.md).

## License and credits

The course is included under the root [MIT License](../LICENSE) and upstream attribution in
[ATTRIBUTION.md](../ATTRIBUTION.md).
