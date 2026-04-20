# {Feature Name}

**Opened**: YYYY-MM-DDTHH:MM
**Meta**: [{meta-name}](../meta-{iteration}.md)
**Source Spec**: [{spec-name}](../../specs/{spec-name}.spec.md)

**Author**: Claw
**Approved By**: {Human}

**Modified Files**:
- `file.py` (description - done)

**Pending**:
- [ ] Task 1
- [ ] Interface docs updated (`docs/interfaces/xxx.md`)

---

## Goal

{One sentence: what this feature achieves and why it matters.}

## User Story

As a {role}, I want {capability}, so that {benefit}.

## Context

{Background, problem being solved, trigger. Link to related ADRs if any.}

---

## Boundary

### System Scope

- **Touches**: {modules, files, APIs affected}
- **Does NOT touch**: {explicitly excluded scope}
- **Depends on**: {preconditions, external services, other features}

### Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| {Module/Service} | Internal/External | ✅ Done / 🟡 In Progress / ❌ Blocked |

## Contract

> Each item is an acceptance criterion. Phase completion requires ALL items to pass.
> Use Given/When/Then where it aids clarity; plain assertions are acceptable.

### Core Scenarios (must pass)

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}

### Edge Cases

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}

### Error Handling

- [ ] {Given ... When ... Then ...}

### Non-Functional (if applicable)

- [ ] {Performance: e.g., "Response time < 100ms for ..."}
- [ ] {Security: e.g., "Input X is sanitized before ..."}
- [ ] {Compatibility: e.g., "Works with Node 18+"}

---

## Interface Contract

> **MUST**: If this change modifies module interfaces, document the interface contract below.

**Modified Interfaces**:
- `file.py:function()` → parameter/return type changes

**Callers**:
- List modules that call this interface

**Invariants**:
- Semantic constraints the interface must satisfy

## Technical Approach

{Brief description of implementation strategy. Keep it concise — the Contract above defines WHAT; this section explains HOW.}

### API Changes (if applicable)

```
POST /api/v1/{endpoint}
Request: {schema}
Response: {schema}
```

---

## Tasks

> **Document-First + Test-Driven**: Strictly execute in Phase A → B → C order. No skipping.

### Phase A: Interface Definition ⛔ GATE A
**Entry**: Contract approved  
**Forbidden**: Any implementation code

- [ ] Analyze Contract scenarios and boundary conditions
- [ ] Define interface signatures (inputs, returns, exceptions)
- [ ] Write to `docs/interfaces/{module}.md`
- [ ] Document interface decisions and constraints (trade-offs if any)

**Gate A Complete**:
- [ ] Interface docs committed (commit: `wip: interface - {contract-name}`)

---

### Phase B: Test Development ⛔ GATE B
**Entry**: Gate A complete  
**Forbidden**: Any implementation code

- [ ] Write test framework based on interfaces
- [ ] Implement tests for Contract items (must fail first)

| Contract Item | Test File | Test Function | Status |
|--------------|-----------|---------------|--------|
| Core-1: {Given...When...Then...} | `test_xxx.py` | `test_yyy()` | ⬜ Red |
| Core-2: {Given...When...Then...} | `test_xxx.py` | `test_zzz()` | ⬜ Red |
| Edge-1: {...} | `test_xxx.py` | `test_edge1()` | ⬜ Red |

- [ ] Run tests, confirm Red status (failing)

**Gate B Complete**:
- [ ] Test files committed (commit: `wip: tests - {contract-name}`)
- [ ] All Contract items have corresponding tests
- [ ] Tests show Red (screenshot or log)

---

### Phase C: Implementation ⛔ GATE C
**Entry**: Gate B complete

- [ ] Write minimal implementation to pass tests (Green)
- [ ] Refactor optimization (keep tests passing)
- [ ] Verify interface docs match actual code

**Gate C Complete**:
- [ ] Implementation committed (commit: `wip: impl - {contract-name}`)
- [ ] All tests passing

---

### Phase D: Test Verification (by Test Worker session)
**Entry**: Gate C complete

Test Worker (still running from Phase B) verifies implementation:
- [ ] Full test suite passes (GREEN)
- [ ] No regressions in existing tests
- [ ] Failures diagnosed and fed back to Coding Worker if needed

---

### Phase E: Code Review ⛔ GATE E
**Entry**: Phase D complete (all GREEN)

- [ ] Review Worker validates implementation against contract + interfaces + tests
- [ ] All auto-fixable issues resolved
- [ ] No needs-human issues (or human has resolved them)

**Gate E Complete**:
- [ ] Review report: PASS

---

### Manual Verification (if needed)

- [ ] {Scenario requiring human verification}

---

## Open Questions

| Question | Status | Resolution |
|----------|--------|------------|
| {Question} | Open / Resolved | {Answer} |

---

## Revision History

| Date | Version | Change | Author |
|------|---------|--------|--------|
| YYYY-MM-DD | 1.0 | Initial draft | Claw |

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Interface docs updated (if interfaces changed)
- [ ] Human confirmed

**Archive**: Remove symlink from `workspace/contracts/in_progress/`. Actual file stays in `docs/contracts/`.

---

> **Downgrade**: ≤ 5 items, no dependency graph, single-module scope → use [mini-contract.md](mini-contract.md) instead.
