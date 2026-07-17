# Security Policy

> Provenance: restored from the upstream repository. Fork maintainers should replace the reporting
> destination below only when they have an established private security channel.

## Supported Versions

| Version | Supported |
|---|---|
| `main` | Yes |

## Reporting a Vulnerability

**Do not report security vulnerabilities through public GitHub issues.**

For the upstream project, report vulnerabilities responsibly through one of these channels:

1. Email `ashishpatel.ce.2011@gmail.com` with subject `[SECURITY] 500-AI-Agents-Projects`.
2. Use the upstream repository's [private security advisory form](https://github.com/ashishpatel26/500-AI-Agents-Projects/security/advisories/new).

Include a description, reproduction steps, potential impact, and a suggested fix when available.

The upstream policy targets acknowledgement within 48 hours, a status update within 7 days, and a
fix or mitigation within 30 days depending on severity.

## Security Expectations

- Never hardcode or commit API keys. Use the documented environment variables and `.env` files.
- Validate untrusted files, URLs, database queries, and model-generated code before execution.
- Review every tool permission and use least-privilege credentials.
- Treat the examples as educational baselines, not production-hardened services.
- Review resolved dependency advisories before deployment. Some older framework stacks require
  behavior-tested major upgrades that are intentionally outside this compatibility-focused pass.
