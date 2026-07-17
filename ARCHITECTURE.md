# Repository architecture

## Design goals

The repository favors isolated examples, stable upstream comparison, transparent attribution, and
deterministic repository checks. It is a collection, not a single deployable application.

## Boundaries

```text
metadata.yaml + README.md + source files
                 |
                 +--> repository validators --> CI / FINAL_REPORT.md
                 |
                 +--> Vite raw imports -------> searchable React catalog
```

### `agents/`

Each numbered directory is an independent Python project. It owns its dependencies, environment
contract, documentation, and entry point. Agents must not import code from sibling projects.

### `crewai_mcp_course/`

The course is a progressive learning path but lessons remain independently installable. Lesson 03
demonstrates an MCP-style tool boundary; it is not a shared runtime service for the other projects.

### `web/`

The React/Vite application reads repository Markdown, Python, YAML, and image assets with Vite raw
imports. `web/src/content.js` normalizes that source into a browser catalog. The source files remain
canonical; the web app must not maintain a competing manual inventory.

### `scripts/`

Validation scripts use the Python standard library wherever possible. Structural validation is
offline and deterministic. Dependency resolution is a separate networked check using `uv`, keeping
failures attributable and individual projects isolated.

### `docs/` and root documents

Root documents explain how to use and govern the distribution. `docs/upstream-*` preserves the
downloaded long-form catalog and contribution guide for provenance. Generated indexes summarize
local content without replacing original metadata.

## Why projects were not physically regrouped

Category folders such as `rag/` or `multi-agent/` would force broad moves, break stable links, make
upstream diffs noisy, and place multi-category projects into arbitrary single buckets. The repository
instead keeps stable numbered paths and exposes categories through metadata, `PROJECT_INDEX.md`, and
`docs/categories.md`.

## Dependency strategy

- Every Python project resolves independently against Python 3.11.
- Direct requirements stay close to the implementation's framework generation.
- Only unsatisfiable pins are corrected during modernization.
- The web catalog uses `package-lock.json` and `npm ci`.
- Docker is not added to credential-driven single-file examples where it would add maintenance
  without improving reproducibility.

## Trust and security boundaries

- Secrets live only in ignored `.env` files.
- CI never calls paid model providers.
- External catalog URLs are untrusted destinations and are not executed.
- Agent examples can generate incorrect or unsafe output; users must review results before acting.
- Code execution and data-access examples should be run against non-sensitive test data first.
