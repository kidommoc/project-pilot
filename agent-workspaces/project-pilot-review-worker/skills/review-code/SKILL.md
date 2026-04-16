---
name: review_code
description: "Review implementation code against contract, interfaces, and tests. Triggered during Implement Agent step C/E review."
---

# Review Code

Validate that implementation correctly fulfills the contract and passes tests.

## Source → Target

- **Source**: `workspace/contracts/in_progress/<contract>.md` (symlink → `docs/contracts/`) + interface docs (`docs/interfaces/`) + test files (Phase B)
- **Target**: Implementation code produced by Coding Worker

## What to Check

### MISS Detection
- All interfaces defined in step A are implemented
- All acceptance criteria from the contract are addressed in code
- Error handling paths from the contract are implemented

### EXTRA Detection
- No code for features outside the contract boundary
- No new public APIs not defined in the interface docs
- No dependencies on modules listed in "does NOT touch"

### ERROR Detection
- Implementation matches interface signatures exactly
- Logic matches the behavior described in the contract
- Code doesn't violate constraints listed in the contract (performance, security, etc.)
- Boundary compliance: only files in "touches" are modified

## Code Quality (secondary, report but don't FAIL for these alone)
- Obvious bugs or logic errors
- Unreachable code
- Missing error handling for common failure modes

## Output

Write review report to the location specified in the task.
