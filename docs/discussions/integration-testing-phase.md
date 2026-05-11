# Integration Testing Phase

**Date**: 2026-05-11
**Status**: Proposed

## Background

Current flow: Contract 1 (A→B→C→D) → Contract 2 (A→B→C→D) → CI/CD Phase 1 (audit) → CI/CD Phase 2 (release)

Each contract's Phase C (Impl GREEN) runs unit tests locally per contract. But when Contract 2's changes interact with Contract 1's, regressions are only caught if they cause obvious failures.

**There is no dedicated cross-contract integration testing phase.**

## Proposal

Add an integration testing phase between "all contracts done" and "CI/CD Phase 1":

```
C-1 done → C-2 done → Integration Test → CI/CD Phase 1 → Phase 2
                               ↓
                        FAIL → re-open affected contract(s)
```

### What Integration Testing Covers

- Multi-contract end-to-end flows (e.g., C-1 input → pipeline → C-2 output)
- Contract boundary interactions (C-1's output is C-2's input format)
- Full test suite run (all unit + integration tests together)

### Implementation Ideas

- Spawn a dedicated "integration test" worker or reuse CI/CD agent with a new phase
- On failure, report which contracts are likely the source → L0 re-opens them
- Could be gated by human confirmation before proceeding to release

## Open Questions

- Is this a separate agent/phase, or part of CI/CD Phase 1?
- Who owns the integration test setup (test config, fixtures, mocks)?
- How fine-grained should the "re-open contract" logic be? Re-open all or just failed ones?
- Should integration test results be written to a file (like release-plan.md) for traceability?
