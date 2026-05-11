---
name: review_meta
description: "Review meta contract against source specs. Validates decomposition strategy, coverage, granularity, and dependency ordering."
---

# Review Meta

Validate that the meta contract correctly decomposes specs into contracts.

## Source → Target

- **Source**: `docs/specs/*.md` + `docs/knowledge/architecture.md` + `docs/knowledge/journey-map.md` + `docs/knowledge/conventions.md`
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

### Architecture Integrity (via architecture.md)
- No single contract spans modules that architecture.md defines as independent
- Contract boundaries respect module ownership per architecture
- Dependency order between contracts is consistent with architecture's module dependency graph

### Journey Coverage (via journey-map.md)
- All key journeys in journey-map are covered by at least one contract
- Critical paths (marked as priority in journey-map) have corresponding contracts

### Convention Compliance (via conventions.md)
- Contract structure follows conventions.md format
- Naming conventions from project conventions are followed in contract names

### Knowledge Ref Accuracy
- If contracts reference Knowledge documents in Boundary Reads, verify those paths exist in `docs/knowledge/`
- Catch stale or renamed Knowledge references early

## Output

Return the review report as your final output (announce to spawning agent).
