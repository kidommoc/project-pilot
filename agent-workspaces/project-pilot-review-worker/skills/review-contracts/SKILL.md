---
name: review_contracts
description: "Review individual contracts against source specs and meta. Triggered after Contract Workers draft contracts."
---

# Review Contracts

Validate that each contract correctly and completely represents its assigned scope.

## Source → Target

- **Source**: `docs/specs/*.md` + meta contract (scope assignment)
- **Target**: `docs/contracts/{feature,fix}/*.md`

## What to Check

### MISS Detection
- Every requirement assigned to this contract (per meta) has a corresponding acceptance criterion
- Constraints from the spec are reflected in the contract boundary
- Dependencies on other contracts are declared

### EXTRA Detection
- Every acceptance criterion traces back to the spec
- No features or behaviors were invented by the Contract Worker
- No scope claimed that belongs to a different contract (per meta assignment)

### ERROR Detection
- Contract boundary (touches / does-not-touch) is accurate per spec
- Acceptance criteria match the behavior described in the spec
- Priority matches meta assignment

## Output

Write review report to the location specified in the task.
