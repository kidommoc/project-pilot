---
name: review_interface
description: "Review interface code against Knowledge interface docs. Triggered during Implement Agent Phase A review."
---

# Review Interface

Validate that interface code correctly matches the Knowledge interface docs.

## Source → Target

- **Source**: Existing Knowledge interface docs at `{project_root}/docs/knowledge/interfaces/`
- **Target**: Interface code produced by Interface Worker

## What to Check

### MISS Detection
- Every interface defined in Knowledge docs has corresponding code
- All function/method signatures from Knowledge docs are implemented
- All types and data structures from Knowledge docs are represented in code

### EXTRA Detection
- No interfaces for modules outside the contract boundary
- No invented API methods or types not implied by the Knowledge docs

### ERROR Detection
- Code signatures match Knowledge interface docs exactly
  - Function names match
  - Parameter names and types match
  - Return types match
  - Error types match
- Import/export topology is correct (no circular deps)

## Output

Return the review report as your final output (announce to spawning agent).
