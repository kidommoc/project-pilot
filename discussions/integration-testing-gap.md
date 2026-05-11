# Integration Testing Gap — Cross-Contract Regression

**Date**: 2026-05-11
**Status**: Open

## Problem

The framework handles per-contract unit testing (Phase B Test RED → Phase C Impl GREEN),
but has no integration/regression testing phase after all contracts in an iteration are implemented.

A real-world case:
- Iteration has 2 contracts: C-1 (argument-parser), C-2 (list-command)
- C-2's implementation may unintentionally break C-1's behavior (semantic regression)
- Interface signatures stay the same, tests stay GREEN, but behavior changes

## Current Coverage

| Phase | What | Regression detection |
|-------|------|---------------------|
| Design | Interface definitions + Knowledge docs | Structural only |
| Plan | Depends On ordering | Dependency graph, not behavior |
| Phase B (Test RED) | Per-contract unit tests | Contract-local only |
| Phase C (Impl GREEN) | Implementation + self-check | Contract-local only |
| Phase D (Intent Review) | Code vs Knowledge docs | Structural verification |
| CI/CD Phase 1 | Lint + test + build | Runs full suite, but no feedback loop |

## The Gap

No explicit **cross-contract integration phase** after all contracts are done.

If integration tests fail at CI/CD stage, the framework can only FAILED and stop.
There's no path to: identify broken contracts → put them back in open/ → re-implement → re-integrate.

## Proposed Directions

1. **Keep as-is (human catch)**: CI/CD finds regression → human decides which contracts to re-do → manually re-opens contracts → L0 lifecycle resumes. Simple, human-accountable.

2. **Add integration phase**: After all contracts done, before CI/CD Release Prep, run full test suite. If FAILED, generate fix-contract list → L0 re-opens affected contracts. Requires state table + CI/CD feedback loop.

## Related

- CI/CD Agent is currently one-directional (lint → test → build → release)
- No mechanism to re-open contracts after they're marked done

## CI/CD Audit Doesn't Run Tests

**Problem**: CI/CD Phase 1 Step 1 (Audit) only runs `git diff` for interface consistency.
It doesn't run `pytest`/`npm test` to catch implementation-level regressions.

**Current coverage**:
- Implement Phase C: Coding Worker runs per-contract tests (contract-local only)
- Phase D (Intent Review): structural validation (code vs Knowledge docs)
- CI/CD Audit: git diff + audit review (structural, no test execution)

**Result**: Full test suite never runs after all contracts merge. Multi-contract regressions
(where C-2 breaks C-1 behavior while keeping all units GREEN) are not caught.

**Status**: Open — pushed to future CI/CD process design.
