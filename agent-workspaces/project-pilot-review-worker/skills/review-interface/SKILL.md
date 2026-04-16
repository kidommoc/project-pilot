---
name: review_interface
description: "Review interface definitions (code + docs) against the contract. Triggered during Implement Agent Phase A review."
---

# Review Interface

Validate that interface definitions correctly represent the contract's requirements.

## Source → Target

- **Source**: `workspace/contracts/in_progress/<contract>.md` (symlink → `docs/contracts/`) (scope and acceptance criteria)
- **Target**: Interface code (if applicable) + interface documentation produced by Interface Worker

## What to Check

### MISS Detection
- Every module/component in the contract scope has interface definitions
- All public APIs, types, and data structures are defined
- Error cases and edge cases from contract acceptance criteria are covered
- Interface documentation exists and matches the interface code

### EXTRA Detection
- No interfaces for modules outside the contract boundary
- No invented API methods or types not implied by the contract

### ERROR Detection
- Interface signatures match the contract's described behavior
- Dependency topology is correct (calls/called-by relationships)
- Interface code and interface documentation are consistent with each other

## Output

Write review report to the location specified in the task.
