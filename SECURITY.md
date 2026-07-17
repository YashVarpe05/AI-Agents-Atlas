# Security Policy

> This active policy is adapted from the upstream repository. Exact policy provenance is recorded
> in [Attribution](ATTRIBUTION.md).

## Supported Versions

| Version | Supported |
|---|---|
| `main` | Yes |

## Reporting a Vulnerability

**Do not report security vulnerabilities through public GitHub issues.**

Report vulnerabilities through the repository's
[private security advisory form](https://github.com/YashVarpe05/AI-Agents-Atlas/security/advisories/new).
If that form is unavailable, request a private maintainer contact without posting exploit details
in a public issue.

Include a description, reproduction steps, potential impact, and a suggested fix when available.

Response timing depends on severity and maintainer availability. Confirmed reports will be handled
privately until a fix or mitigation is ready.

## Security Expectations

- Never hardcode or commit API keys. Use the documented environment variables and `.env` files.
- Validate untrusted files, URLs, database queries, and model-generated code before execution.
- Review every tool permission and use least-privilege credentials.
- Treat the examples as educational baselines, not production-hardened services.
- Review resolved dependency advisories before deployment. Some older framework stacks require
  behavior-tested major upgrades that are intentionally outside this compatibility-focused pass.
