# External link audit

Audit date: 2026-07-18

The preserved upstream catalog contains 109 unique external examples across 28 parent repositories.
At audit time, 74 deep links returned HTTP 200 and 35 returned HTTP 404.

## Broken-link groups

- 17 Agno example paths under the former `cookbook/examples/agents/` layout returned 404. The
  current [Agno cookbook](https://github.com/agno-agi/agno/tree/main/cookbook) is reachable, but a
  one-to-one replacement for each historical file was not established.
- 18 LangGraph tutorial paths under the former `docs/docs/tutorials/` layout returned 404. The
  current [LangGraph examples](https://github.com/langchain-ai/langgraph/tree/main/examples) and
  [documentation source](https://github.com/langchain-ai/langgraph/tree/main/docs) are reachable,
  but tutorial filenames have changed.
- The linked game repository redirects from the historical owner to `onjas-6`.

## Decision

The source catalog is kept as an explicitly labeled upstream snapshot rather than silently replacing
specific examples with broad repository home pages. The active root README and project index do not
present these 35 links as validated. A maintainer should map each title to a current equivalent before
promoting it into an active catalog.

## License review

External repositories use a mix of MIT, Apache-2.0, CC-BY-4.0, dual, custom non-commercial,
Unlicense, and undetected licenses. Treat links as references only and verify the destination before
copying any material.
