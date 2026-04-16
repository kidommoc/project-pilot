---
name: review_tests
description: "Review test cases against the contract. Triggered during Implement Agent step B review."
---

# Review Tests

Validate that test cases correctly cover the contract's acceptance criteria.

## Source → Target

- **Source**: `workspace/contracts/in_progress/<contract>.md` (symlink → `docs/contracts/`) (acceptance criteria) + interface docs (`docs/interfaces/`)
- **Target**: Test files produced by Test Worker

## What to Check

### MISS Detection
- Every acceptance criterion has at least one corresponding test
- Edge cases mentioned in the contract are tested
- Error/failure paths are tested

### EXTRA Detection
- No tests for behavior outside the contract scope
- No tests that assume implementation details not in the interface

### ERROR Detection
- Test assertions match the expected behavior described in the contract
- Test setup uses correct interfaces (matches step A output)
- Tests are actually runnable (no syntax errors, correct imports)

## Mapping Table

If the contract includes a criteria-to-test mapping table, verify it:
- Every criterion row has at least one test
- Referenced test names/files actually exist
- No mapping points to a nonexistent test

## Output

Write review report to the location specified in the task.
