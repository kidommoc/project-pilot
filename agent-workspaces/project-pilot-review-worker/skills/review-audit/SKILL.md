---
name: review_audit
description: "Full iteration audit for CI/CD phase. Validates all contracts were correctly completed and Knowledge is consistent with code."
---

# Review Audit

Comprehensive audit of a completed iteration before release.

## Source → Target

- **Source**: `workspace/meta.md` (symlink → `docs/contracts/meta-*.md`) → follow markdown links to individual contracts + source spec
- **Target**: The codebase changes made during this iteration

## What to Check

### Contract Completion
- Read meta contract, follow each markdown link to verify the contract file exists
- All acceptance criteria are checked off in each contract
- No remaining symlinks in `workspace/contracts/open/` or `workspace/contracts/in_progress/`
- All acceptance criteria are checked off

### Commit History
- Each contract has a single squashed commit with format `impl: <contract-name>`
- WIP commits (`wip: interface/tests/impl - <name>`) are allowed on iteration branch but should be squashed before merge to main
- No rogue commits outside contract scope

### Test Results (Full Regression)
- Run the **full test suite** — not just individual contract tests
- All tests pass, including tests from earlier contracts in this iteration
- No skipped or disabled tests that should be active

### Boundary Compliance
- Files modified match the "touches" declarations across all contracts
- No files modified that appear in any "does NOT touch" list

### Cross-Contract Consistency
- No contract modified files that another contract declared as "does NOT touch"
- No conflicting interface changes between contracts (e.g. contract A changes a signature that contract B depends on)
- Dependency order from 000-meta was respected in commit history

### Spec Coverage
- Every spec requirement is traceable to a completed contract
- No spec requirements were dropped without documentation

### Knowledge Consistency (NEW)
- Run: `git diff -- docs/knowledge/` to check if Knowledge docs were modified during implementation
- If diff is non-empty: report which Knowledge files changed and why. Flag to human for review if changes were made without corresponding Design phase update.
- If diff is empty: note that Knowledge is stable (no divergence between design and implementation)

## Output

Return the audit report as your final output (announce to spawning agent).
Include Knowledge consistency status as a dedicated section.
