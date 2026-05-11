---
name: review_contracts
description: "Review individual contracts against source specs and meta. Validates anchor refs, task breakdown, and boundary accuracy."
---

# Review Contracts

Validate that each contract correctly and completely represents its assigned scope.

## Source → Target

- **Source**: `docs/specs/*.md` + meta contract (scope assignment) + `docs/knowledge/architecture.md` + `docs/knowledge/conventions.md`
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

### Anchor Ref Accuracy
- Boundary Reads anchor paths (e.g. `docs/knowledge/interfaces/*.md`) are correct and files exist
- Anchor references point to valid Knowledge documents (not stale/renamed files)
- No orphaned anchors pointing to nonexistent locations

### Architecture Compliance (via architecture.md)
- Contract's touches/does-not-touch respects module boundaries defined in architecture
- Modules listed in touches belong to the same subsystem (per architecture.md module index)

### Domain Model Consistency (via domain-models/*.md, if referenced)
- Types, entities, and concepts referenced in contract use correct naming per domain-models
- Contract doesn't introduce conflicting terminology

### Convention Compliance (via conventions.md)
- Contract format follows conventions.md requirements
- Wording and style matches project conventions

### Task Reasonableness
- Tasks in the contract are coherent units — each task should produce one meaningful change
- Task ordering is logical (no task that depends on a later task)
- No task is trivially small or implausibly large for a single coding session

## Output

Return the review report as your final output (announce to spawning agent).
