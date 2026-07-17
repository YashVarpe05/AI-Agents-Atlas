# Contributing

Thank you for improving the AI Agents Atlas. Contributions should remain small, runnable,
attribution-safe, and easy to review.

## Before opening a change

1. Search [PROJECT_INDEX.md](PROJECT_INDEX.md) for an existing implementation.
2. Open an issue for substantial additions or repository-wide structural changes.
3. Confirm that you may redistribute every file you plan to add.
4. Never commit API keys, `.env` files, generated environments, model outputs containing private
   data, or copied third-party code without its required license and notices.

## Add a local agent

Copy [`templates/agent/`](templates/agent/) into `agents/NN-project-slug/` and complete every file:

```text
NN-project-slug/
|-- .env.example
|-- README.md
|-- agent.py
|-- metadata.yaml
`-- requirements.txt
```

An agent contribution must:

- run on Python 3.11 in an isolated virtual environment;
- expose a useful `--help` command when it accepts CLI input;
- list direct dependencies in `requirements.txt` using compatible pins or bounded ranges;
- document every required environment variable with placeholder values;
- avoid network calls at import time;
- avoid destructive tools and unsafe code execution by default;
- include original attribution and licensing when derived from another project;
- include a clearly labeled screenshot placeholder or real, non-sensitive screenshot;
- pass `python scripts/validate_repository.py` and `python scripts/check_dependencies.py`.

## Documentation contract

Each project README must include overview, features, architecture, tech stack, installation,
environment variables, running instructions, folder structure, an example, screenshots,
contributing guidance, license/credits, and support information. Use
[`templates/agent/README.md`](templates/agent/README.md) as the source of truth.

## Web catalog changes

The React catalog reads project and course files at build time. After metadata or README changes:

```bash
npm --prefix web ci
npm --prefix web run build
```

Do not hard-code a second project catalog in the web application. Metadata and repository docs are
the canonical sources.

## Pull request checklist

- [ ] The change has one clear purpose.
- [ ] Agent functionality is unchanged unless the PR explains a setup or correctness fix.
- [ ] Required attribution and license notices are preserved.
- [ ] No secret or personal data is included.
- [ ] README commands were tested from a clean environment.
- [ ] Repository validation passes.
- [ ] Web build passes when catalog content changes.
- [ ] Generated artifacts and virtual environments are excluded.

## Commit style

Use concise conventional commits where practical, for example:

- `feat(agent): add invoice extraction example`
- `fix(deps): resolve LangGraph compatibility`
- `docs: clarify local model setup`
- `chore(ci): validate project metadata`

## License

By contributing, you agree that your contribution may be distributed under this repository's MIT
license unless a clearly identified nested project requires compatible, separately documented terms.
Do not submit material you do not have permission to redistribute.
