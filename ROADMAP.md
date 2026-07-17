# Roadmap

The roadmap is intentionally maintenance-focused. It does not promise ownership or support for
externally linked projects.

## Completed in the modernization baseline

- Restore the exact upstream MIT license and document provenance.
- Inventory and classify every local project.
- Correct unsatisfiable dependency manifests without rewriting agent logic.
- Add repository validation, dependency resolution checks, CI, and a locked web build.
- Standardize project documentation and screenshot placeholders.
- Add repository-owned SVG brand assets and an accessible dark/light banner.

## Near term

- Add credential-free smoke tests for agents that expose pure parsing or formatting functions.
- Capture real, redacted screenshots after maintainers run projects with test accounts.
- Verify external catalog links on a scheduled, rate-limited basis.
- Test the reference projects on Linux and macOS in addition to Windows and CI Linux.

## Later, with maintainer approval

- Upgrade framework generations one project at a time with behavior tests.
- Add local-model alternatives where the project can support them without duplicated logic.
- Publish the web catalog through an owned GitHub Pages repository.
- Add signed release artifacts and a documented versioning policy.

## Explicitly out of scope

- Mirroring third-party repositories into this collection.
- Claiming that external catalog entries are locally validated.
- Force-upgrading all projects to one framework version.
- Adding Docker, orchestration, or shared abstractions to simple one-file examples without evidence.
