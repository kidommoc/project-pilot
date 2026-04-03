# Phase 2: Implementation

**Goal**: Map Contract to code, execute, and verify each item as you go.  
**Hat**: Developer (with Architect and Tester modes)

---

## Overview

Phase 2 executes the work defined in Phase 1 Contracts:
- Move Contracts from `open/` to `in_progress/` one at a time
- Implement per Contract with thinking-stage separation
- Verify each item, update interface docs
- Archive completed Contracts

---

## Step 1: Implementation Brief (Architect Mode)

**Before any code**, produce Contract → Code mapping:
- Each Contract item → target file(s), function(s), module(s)
- New interfaces → define signatures first (no implementation)
- Execution order → dependencies, parallelization opportunities
- **Test Strategy** per item:
  - Test type (unit/integration/e2e)
  - Key test cases (Given/When/Then → test description)
  - Mock/dependency handling

**Format**: Embed in Contract Tasks section. No separate doc needed.  
**Scale**: Mini-Contract → 5-10 bullets. Full Contract → Implementation Plan section.

⛔ **No code before brief is written.**

---

## Step 2: Test-First Development (Developer Mode)

Execute per Implementation Brief using **red-green-refactor**:

For each Contract item:
1. **Red**: Write test (should fail, validates test)
2. **Green**: Write minimal implementation (test passes)
3. **Refactor**: Optimize code (keep tests passing)

**Record in Contract**:
```markdown
- [ ] Given ... When ... Then ...
  - **Test**: `test_feature_x.py::test_scenario_y()`
```

**Checkpoints**:
- Per-item verification: Test passes immediately after item
- Interface docs: Update on any interface change
- Regression: Fix before continuing
- Subagents: Use for isolated tasks (docs, test scaffolding, parallel modules)

📖 **Task decomposition**: [guides/session-tasks.md](guides/session-tasks.md)

---

## Step 3: Self-Check (Tester Mode)

After all items implemented, switch mindset — **assume you don't know the code**:
- **TDD verification**: Each Contract item has corresponding test
- Walk through each item, verify passes independently
- Run full test suite
- Verify interface docs current
- Any failure → return to Step 2, fix, re-verify

---

## Step 4: Commit

Commit completed Contract in iteration branch:
```bash
git commit --author="Openclaw <claw@openclaw.local>" -m "feature: {contract-name}"
```

**Commit** (on iteration branch):
```bash
git commit --author="Openclaw <claw@openclaw.local>" -m "feature: {contract-name}"
```

---

## Exit Criteria

- [ ] Implementation Brief written
- [ ] All Contract items implemented and individually verified
- [ ] Full test suite passing
- [ ] Interface docs updated (if interfaces changed)
- [ ] Contract status marked "Done"
- [ ] **Committed**: `feature: {contract-name}`

**Claw**: Executes plan, maintains quality, verifies per item, keeps docs current  
**Human**: Available for questions, confirms at Phase end
