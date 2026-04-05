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

## Step 2: Phase-Gated Development

**Document-First + Test-Driven**: Strictly execute in Phase A → B → C order. No skipping.

### Phase A: Interface Definition ⛔ GATE A
**Entry**: Contract approved  
**Forbidden**: Any implementation code

- Analyze Contract scenarios and boundary conditions
- Define interface signatures (inputs, returns, exceptions)
- Update `references/interfaces/{module}.md`
- **Commit**: `[A] docs: interface for {contract-name}`

**⛔ Check**: Gate A incomplete, Phase B forbidden

---

### Phase B: Test Development ⛔ GATE B
**Entry**: Gate A commit complete  
**Forbidden**: Any implementation code

- Write test framework based on interfaces
- Implement tests for Contract items (must fail first - Red)
- Run tests, confirm Red status (screenshot or log)
- **Commit**: `[B] test: red tests for {contract-name}`

**⛔ Check**: Gate B incomplete, Phase C forbidden

---

### Phase C: Implementation ⛔ GATE C
**Entry**: Gate B commit complete

- Write minimal implementation to pass tests (Green)
- Refactor optimization (keep tests passing)
- Verify interface docs match actual code
- **Commit**: `[C] feat: implement {contract-name}`

---

**Subagents**: Use for isolated tasks (docs, test scaffolding, parallel modules)

📖 **Task decomposition**: [guides/session-tasks.md](guides/session-tasks.md)

---

## Step 3: Self-Check (Tester Mode)

After Phase C, switch mindset — **assume you don't know the code**:
- Walk through each Contract item, verify passes independently
- Run full test suite
- Verify interface docs current
- Any failure → return to Phase C, fix, re-verify

---

## Step 4: Contract Close Verification

**Timing**: After all Contract items implemented, before archiving

### 4.1 Phase Sequence Verification

Verify last 3 commits follow `[A] → [B] → [C]` order:

```bash
git log -3 --format=%s
```

**Pass Criteria**:
- [ ] Commit-3: `[A] docs: interface for {contract}` — Interface docs
- [ ] Commit-2: `[B] test: red tests for {contract}` — Tests first
- [ ] Commit-1: `[C] feat: implement {contract}` — Implementation
- [ ] All tests currently passing (Green)

### 4.2 Result Handling

**✅ Verified → Squash**:
```bash
git reset --soft HEAD~3
git commit -m "feat: {contract-name}"
```

**❌ Failed → Rollback**:
```bash
git reset --hard HEAD~3
```
**Action**: Return to Phase A, re-execute A → B → C

### 4.3 Close Contract
- [ ] Squashed commit created
- [ ] Human final confirmation
- [ ] Move to `contracts/archived/`

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

## Transition Actions (P2→P3)

Execute these steps **immediately after** all Contracts are archived:

1. **Verify**: `contracts/open/` and `contracts/in_progress/` are empty
2. **Update README**: Change `Phase: 2` → `Phase: 3`
3. **Commit**: `docs: phase 2 → 3`

```bash
git add -A
git commit --author="Openclaw <claw@openclaw.local>" -m "docs: phase 2 → 3"
```

**Human confirmation**: Required before commit.

---

## Exit Criteria

- [ ] Implementation Brief written
- [ ] All Contract items implemented and individually verified
- [ ] Full test suite passing
- [ ] Interface docs updated (if interfaces changed)
- [ ] All Contracts archived
- [ ] README updated to Phase 3
- [ ] Transition commit created

**Claw**: Executes plan, maintains quality, verifies per item, keeps docs current  
**Human**: Available for questions, confirms at Phase end
