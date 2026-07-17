# Repository scripts

- `validate_repository.py` performs offline structure, metadata, README, syntax, local-link, secret,
  and generated-artifact checks.
- `check_dependencies.py` asks `uv` to resolve every Python requirements file independently on the
  selected Python version. It does not install or execute project code.
- `smoke_projects.py` launches every agent's `--help` path and imports course entry points in isolated
  Python 3.11 environments without making provider requests.

These scripts are cross-platform and write no persistent output into the repository.
