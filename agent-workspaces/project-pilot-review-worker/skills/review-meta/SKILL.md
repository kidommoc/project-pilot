---
name: review_meta
description: "Review meta contract against source specs. Validates decomposition strategy, coverage, granularity, and dependency ordering."
---

# Review Meta

Validate that the meta contract correctly decomposes specs into contracts.

## Source → Target

- **Source**: `docs/specs/*.spec.md`
- **Target**: Meta contract (produced by Plan Agent)

## What to Check

### MISS Detection
- Every requirement in the specs is assigned to at least one contract
- Cross-module dependencies mentioned in specs are captured in the dependency column
- Risks or open questions from specs are noted

### EXTRA Detection
- No contracts for work not traceable to any spec
- No invented scope beyond what specs describe

### ERROR Detection
- Dependency order is logically correct (no cycles, no missing edges)
- Execution order is consistent with the dependency declarations
- Priority assignments match the relative importance implied by specs

### Granularity Check
- No contract is trivially small (single file change with no logic)
- No contract is too large (spans multiple unrelated modules or >1 day of work)
- Each contract is a coherent unit — one squashed commit should make sense

### Coverage Check
- Union of all contracts covers 100% of spec requirements
- No overlaps — no two contracts claim the same scope
- No orphans — every contract maps to at least one spec

## Output

Write review report to the location specified in the task.
