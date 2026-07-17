# Getting started

## Prerequisites

- Git
- Python 3.11
- Node.js 20 or newer for `web/`
- npm 10 or newer
- `uv` (recommended for creating the validated Python 3.11 environment and checking dependencies)
- API credentials required by the project you choose

Python 3.11 is the validated baseline. Newer Python versions may not be supported by the older
framework releases used in some educational examples.

## Run a Python agent

Choose one folder from [PROJECT_INDEX.md](PROJECT_INDEX.md), then create an isolated environment.

### macOS or Linux

```bash
cd agents/10-meeting-notes-agent
uv venv --python 3.11 .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
python agent.py --help
```

### Windows PowerShell

```powershell
Set-Location agents/10-meeting-notes-agent
uv venv --python 3.11 .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python agent.py --help
```

Open `.env`, replace only the documented placeholders, and never commit the file.

## Run the CrewAI/MCP course

Start with the course overview at [`crewai_mcp_course/README.md`](crewai_mcp_course/README.md).
Lessons are independent, so create a fresh virtual environment for each lesson.

```bash
cd crewai_mcp_course/lesson_01
uv venv --python 3.11 .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python agent.py
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1` instead.

## Run the web catalog

```bash
cd web
npm ci
npm run dev
```

Vite prints the local URL. Use `npm run build` for a production bundle and `npm run preview` to
serve that bundle locally.

## Validate a clean checkout

```bash
python scripts/validate_repository.py
python scripts/check_dependencies.py
npm --prefix web ci
npm --prefix web run build
```

Dependency validation resolves each project independently on Python 3.11. It does not install or
execute agents and therefore does not require provider credentials.

## Common problems

### Missing API key

Copy the selected project's `.env.example` to `.env` and set the named variable. Do not add unrelated
keys globally.

### Package does not support your Python version

Use Python 3.11. The collection intentionally keeps framework versions close to the examples they
were written against instead of force-upgrading every project to one global stack.

### Provider request fails

Check account credits, model access, region availability, rate limits, and the exact environment
variable name. Provider calls are outside repository QA because they require private credentials and
may incur charges.

### Web catalog is stale

Stop the Vite server, remove `web/node_modules/.vite` if present, run `npm ci`, and restart it. The
catalog imports repository content during the Vite build.
