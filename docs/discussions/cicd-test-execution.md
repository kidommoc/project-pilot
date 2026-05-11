# CI/CD: Add Test Execution to Audit

**Date**: 2026-05-11
**Status**: Proposed

## Background

CI/CD Phase 1 Step 1 (Audit) currently only runs `git diff` for interface consistency checks and spawns the Review Worker with `review-audit` skill. It does not execute the actual test suite.

As a result:
- Full test suite never runs after all contracts merge
- Multi-contract regressions (C-2 breaks C-1 behavior while keeping all unit tests GREEN) are not caught
- Only structural/consistency issues are found

## Proposal

Insert a test execution step in CI/CD Phase 1 audit:

```
Current:
  Step 1: Audit → git diff + review-audit → report

Proposed:
  Step 1: Run full test suite → audit → git diff + review-audit → report
```

### Execution Details

- Run `pytest` / `npm test` (or language-specific test command) at the project root
- Capture exit code and output
- Include test result in audit report
- If tests fail → release-plan.md Status: FAIL

### Placement

Two options:
1. **In review-audit skill**: add "run tests" as one of the audit checks
2. **In CI/CD AGENTS.md**: add a standalone test step before spawning Review Worker

Option 2 keeps concerns separated — review-audit stays structural, CI/CD owns the test gate.

## Open Questions

- Is this the right place, or should test execution be its own phase (see integration-testing-phase.md)?
- Who defines the test command — PROJECT.AGENT.md, project-type template, or something else?
- Should test failures auto-create a discussion entry for human review?

## Related

- `docs/discussions/integration-testing-phase.md` — broader integration testing phase proposal
- `discussions/integration-testing-gap.md` — earlier gap analysis (root discussions/)
