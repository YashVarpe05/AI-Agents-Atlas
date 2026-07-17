## Summary

Describe the problem and the smallest change that solves it.

## Scope

- Project or repository area:
- Behavior change: yes / no
- Upstream or third-party source, if any:

## Validation

- [ ] `python scripts/validate_repository.py`
- [ ] `python scripts/check_dependencies.py` when Python manifests changed
- [ ] `npm --prefix web ci && npm --prefix web run build` when catalog content changed
- [ ] Credential-backed behavior tested manually when applicable

## Safety and provenance

- [ ] No secrets, personal data, generated environments, or paid-provider outputs were committed.
- [ ] Original copyright, license, source, and attribution are preserved.
- [ ] External code is not copied without redistribution permission.
- [ ] Documentation distinguishes validated local code from external links.
