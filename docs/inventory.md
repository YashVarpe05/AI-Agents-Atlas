# Repository inventory

Audit date: 2026-07-18

## Summary

| Item | Count | Audit result |
|---|---:|---|
| Local agent projects | 20 | Complete project skeletons; no duplicate folders detected |
| Course lessons | 3 | Complete lesson files and dependency manifests |
| Web applications | 1 | React/Vite catalog with production build path |
| Python source files | 28 | Syntax parsed successfully across agents, lessons, scripts, and template |
| Project READMEs | 20 | Present; standardized during modernization |
| Project `.env.example` files | 20 | Present; placeholder values only |
| Course `.env.example` files | 3 | Present; placeholder values only |
| Missing root license | 1 | Restored verbatim from upstream MIT license |
| Unsatisfiable requirement manifests | 4 | Corrected without agent logic changes |

## Original structure

The download contained `agents/`, `crewai_mcp_course/`, `images/`, `web/`, `README.md`, and
`CONTRIBUTION.md`. It did not contain Git history, a root license file, CI, a lockfile, repository
validators, or the requested root documentation set.

## Duplicate and incomplete project review

No duplicate local implementations were found. Several projects address related domains, but each
has a distinct entry point and metadata record. Every agent had all five required project files.
README depth varied significantly, so the modernization adds a shared documentation contract while
preserving original examples and commands.

## Dependency findings

Four manifests could not resolve on Python 3.11:

1. `01-web-research-agent` pinned nonexistent `langchain-tavily==0.1.0` and an incompatible
   LangGraph generation.
2. `03-pdf-qa-agent` pinned LlamaIndex OpenAI plugins outside the range required by
   `llama-index==0.11.0`.
3. `13-customer-support-agent` combined `langchain-core==0.3.0` with
   `langgraph==0.2.0`, which requires LangChain Core below 0.3.
4. `19-competitive-analysis-agent` had the same LangGraph conflict.

The corrected manifests resolve independently. Other direct requirements were left unchanged to
avoid untested framework migrations.

## Validation boundaries

Repository QA can verify structure, metadata, syntax, local links, placeholder secrets, dependency
resolution, and the web build. End-to-end provider execution remains manual because it requires
private credentials, external accounts, network access, and may incur cost.

See [../FINAL_REPORT.md](../FINAL_REPORT.md) for the final command results and manual interventions.
