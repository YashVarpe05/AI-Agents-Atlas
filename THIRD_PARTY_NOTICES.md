# Third-party notices and service terms

This file is an operational index, not a replacement for dependency licenses or legal advice.

## Upstream source

The repository originates from `ashishpatel26/500-AI-Agents-Projects` under the MIT license restored
at [LICENSE](LICENSE). See [ATTRIBUTION.md](ATTRIBUTION.md).

## Direct web dependencies

| Dependency | Purpose | Upstream license |
|---|---|---|
| React / React DOM | User interface runtime | MIT |
| Vite | Build tooling | MIT |
| `@vitejs/plugin-react` | React build integration | MIT |
| Lucide React | Icons | ISC |

Transitive versions are recorded in `web/package-lock.json`. Consumers should generate an SBOM or
license report for their release environment.

## Python dependencies

Each local project has an independent `requirements.txt`. The repository does not vendor dependency
source. Package licenses and transitive graphs may change when an installer resolves a manifest;
review the resolved environment before redistribution.

## External services and data

The examples may use OpenAI, Tavily, NewsAPI, GitHub, and Yahoo Finance through `yfinance`. Those
services and data sources are governed by their own terms, privacy policies, rate limits, and usage
rights. The repository's MIT license does not grant rights to provider services or third-party data.

## Bundled legacy images

The downloaded snapshot included three files under `images/` without a complete source/license
record. They are preserved for provenance but are no longer used by the modernized root README or web
catalog. Obtain a rights record before publishing or reusing them outside an archival context.

## External catalog

The preserved upstream catalog links to independently maintained repositories. Linking does not
bundle their code or change their licenses. Some repositories have no detected license or use
non-commercial/custom terms; do not copy their code without permission.
