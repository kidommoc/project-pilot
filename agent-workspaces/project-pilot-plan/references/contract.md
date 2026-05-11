# {Contract Name}

**Opened**: {date}
**Source Spec**: `docs/specs/{date}-{name}.md` (Section: {section})
**Type**: `feature/` | `fix/`

## Goal

{One sentence: what does this contract achieve?}

## Boundary

- **Touches**: {modules affected}
- **Does NOT touch**: {explicitly excluded}
- **Depends on**: {preconditions}
- **Reads**:
  - `docs/knowledge/interfaces/{name}.md` — signatures to implement
  - `docs/knowledge/modules/{name}.md` — constraints to respect
  - `docs/specs/{date}-{name}.md` — design intent (section) {omit for fix/}

## Contract (Acceptance Criteria)

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}
- [ ] {Edge case}

## Tasks

### Phase A: Interface Code ⛔
- [ ] Write interface code matching `docs/knowledge/interfaces/`
- [ ] Review Worker PASS (review-interface)

### Phase B: Test (RED) ⛔
- [ ] Write tests per interfaces in `docs/knowledge/interfaces/`
- [ ] Run tests, confirm RED
- [ ] If fix: write test that reproduces the bug, confirm RED
- [ ] Review Worker PASS (review-tests)

### Phase C: Impl (GREEN) ⛔
- [ ] Implement to pass all tests
- [ ] Run tests, confirm GREEN (self-check loop: if fail → fix → run again)

### Phase D: Intent Review ⛔
- [ ] Review Worker PASS (review-code: intent + code quality)
- [ ] If fail → back to Phase C, Coding Worker re-spawned with review report
