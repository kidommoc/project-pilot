# Quality Checklists

---

## Pre-Review (Claw Self-Check)

**Code**:
- [ ] Tests pass
- [ ] No lint/type errors
- [ ] Naming conventions followed
- [ ] No debug statements

**Docs**:
- [ ] README/API docs updated
- [ ] Spec marked "Implemented"
- [ ] Session log written

**Tracking**:
- [ ] ADR created (if applicable)
- [ ] Project board updated

---

## Pre-Release

**Functional**:
- [ ] All tests pass
- [ ] Acceptance criteria met
- [ ] Smoke test passed

**Docs**:
- [ ] CHANGELOG.md updated
- [ ] Version bumped (package.json, README, etc.)

**Git**:
- [ ] All changes committed
- [ ] Tag created: `v{MAJOR}.{MINOR}.{PATCH}`

**Release Notes** (if external):
- [ ] Highlights section
- [ ] Breaking changes noted
- [ ] Human approved

---

## Spec Review (Human)

- [ ] Goal clear and testable
- [ ] Requirements complete
- [ ] Technical approach sound
- [ ] Effort estimate reasonable

**Approval**: [ ] As-is [ ] Minor changes [ ] Major revision

---

## Code Review (Human)

- [ ] Implements all requirements
- [ ] No obvious bugs
- [ ] Tests cover key scenarios
- [ ] Code readable

**Approval**: [ ] Merge [ ] Minor fixes [ ] Major revision

---

## Session End

- [ ] Work committed (descriptive messages)
- [ ] Project board updated
- [ ] Session log written
- [ ] Next priorities noted

---

## Project Health (Weekly)

**Progress**: [ ] On track [ ] Tasks stuck [ ] Blockers

**Quality**: [ ] Tests ok [ ] Docs current [ ] Debt managed

**Retrospective**:
- Went well: ...
- Improve: ...
- Actions: [ ] ...

---

**Version**: 0.4.0
