# Quality Checklists

---

## 🚨 Contract Close Checklist

**See `references/workflow-phase2.md` Step 4 for Phase Sequence verification and Squash**

---

## 🚨 Phase Completion (MUST-1 Enforcement)

**MUST check before declaring Phase complete:**

### Phase 1 Completion (Additional)
- [ ] **000 Meta-Contract archived** (planning complete, child contract list defined)
- [ ] All child Contracts created and in `contracts/open/`
- [ ] iteration branch created: `iteration/v{version}`

### All Contracts Done
- [ ] All Contracts in Phase closed (check `contracts/archived/`)
- [ ] No pending Contracts in `contracts/in_progress/` or `contracts/open/`

### README Update
- [ ] README.md Phase status updated (✅ Completed)
- [ ] README.md next Phase status updated (⏳ Pending)

### User Communication
- [ ] Explicitly asked: "Phase N completed (all Contracts done). Continue to Phase N+1?"
- [ ] ⛔ Stopped and waiting for confirmation, no next phase code executed

**Violation Recovery**: If any of the above is violated, stop immediately and roll back to last valid state.

---

## Pre-Audit (Claw Self-Check — Phase 2 Step 3)

**Contract Verification**:
- [ ] Implementation Brief written before coding started
- [ ] Each contract item individually verified as implemented
- [ ] Full test suite passing

**Code**:
- [ ] No lint/type errors
- [ ] Naming conventions followed
- [ ] No debug statements

**Docs**:
- [ ] Interface docs updated (if interfaces changed)
- [ ] ADR created (if architectural decision)
- [ ] Contract marked "Done"

**Tracking**:
- [ ] ADR created (if applicable)
- [ ] Project board updated

---

## Audit Checklist (Phase 3)

**Contract Audit** (adversarial — verify from Contract perspective, not code perspective):
- [ ] Each contract item checked against actual behavior (not just code reading)
- [ ] Edge case items verified with actual test runs
- [ ] Boundary respected (no changes outside declared scope)

**Quality**:
- [ ] Tests pass
- [ ] No lint errors
- [ ] Docs updated
- [ ] Naming conventions followed

**Audit Summary produced**:
- [ ] Per-item pass/fail status
- [ ] Test results
- [ ] Changes summary
- [ ] Known risks / tech debt

---

## Pre-Release

**Functional**:
- [ ] All tests pass
- [ ] Acceptance criteria met
- [ ] Smoke test passed

**Docs**:
- [ ] CHANGELOG.md updated
- [ ] Interface docs up to date (if interfaces changed)
- [ ] Version bumped (package.json, README, etc.)

**Git**:
- [ ] All changes committed
- [ ] **Iteration branch checked**: `iteration/v{version}` exists and is current
- [ ] **On iteration branch**: All commits pushed (`contract:`, `feature:`, `fix:`)
- [ ] **Cleanup committed**: `chore: cleanup iteration tracking` (README Current Iteration removed)
- [ ] **Release committed**: `release: v{version}`
- [ ] **Merged to main**: `git merge iteration/v{version}`
- [ ] **Tag created**: `v{MAJOR}.{MINOR}.{PATCH}` (on main)

**Release Notes** (if external):
- [ ] Highlights section
- [ ] Breaking changes noted
- [ ] Human approved

---

**Version**: 1.1.1 (2026-03-26) — Contract Close vs Phase Completion separated
