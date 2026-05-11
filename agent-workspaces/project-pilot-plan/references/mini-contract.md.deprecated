# {Feature / Change Title}

**Opened**: YYYY-MM-DDTHH:MM
**Meta**: [{meta-name}](../meta-{iteration}.md)
**Source Spec**: [{spec-name}](../../specs/{spec-name}.spec.md)

**Modified Files**:
- `file.py` (description - done)

**Pending**:
- [ ] Task 1
- [ ] Interface docs updated (`docs/interfaces/xxx.md`)

---

## Goal

{One sentence: what problem does this change solve?}

## Context

{Why this is needed. Background, trigger, related ADR links. 2-3 sentences.}

## Boundary

- **Touches**: {affected files/modules, comma-separated}
- **Does NOT touch**: {explicitly excluded scope — prevents scope creep}
- **Depends on**: {preconditions or external deps, "none" if none}

## Contract

> Each item below is an acceptance criterion. On Phase completion, verify each one. All must pass.

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}
- [ ] {Plain testable assertion — strict Gherkin format not required}

## Tasks

> **Document-First + Test-Driven**: Execute in Phase A → B → C order.

**Phase A: Interface Definition** ⛔
- [ ] Define interfaces, update `docs/interfaces/{module}.md`
- [ ] Commit: `wip: interface - {contract-name}`

**Phase B: Test First** ⛔
- [ ] Write tests (should fail first)
- [ ] Verify all Contract items have test coverage
- [ ] Commit: `wip: tests - {contract-name}`

**Phase C: Implementation** ⛜
- [ ] Write implementation to pass tests
- [ ] Commit: `wip: impl - {contract-name}`
- [ ] Run tests to verify all pass

**Phase D: Test Verification** (by Test Worker session)
- [ ] Full test suite passes
- [ ] No regressions

**Phase E: Code Review** ⛜
- [ ] Review Worker validates against contract
- [ ] Review report: PASS

## Notes

{Optional. Open questions, known risks, future extension directions.}

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Interface docs updated (if interfaces changed)
- [ ] Human confirmed

**Archive**: Remove symlink from `workspace/contracts/in_progress/`. Actual file stays in `docs/contracts/`.

---

> **Upgrade**: >8 items, multi-module, or architectural impact → use [contract.md](contract.md) instead.
