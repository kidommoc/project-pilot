# Fix: {Bug Title}

**Opened**: YYYY-MM-DDTHH:MM

## Bug

{What's broken. Observable symptoms, error messages, or incorrect behavior.}

## Expected

{What should happen instead.}

## Reproduce (optional)

{Steps to trigger the bug, if known.}

## Boundary

- **Touches**: {affected files/modules}
- **Does NOT touch**: {explicitly excluded scope}

## Contract

- [ ] {Given ... When ... Then ... (verifies the fix)}
- [ ] {Given ... When ... Then ... (verifies no regression)}

## Tasks

**Phase B: Test First** ⛔
- [ ] Write failing test that reproduces the bug
- [ ] Commit: `[B] test: red test for {fix-name}`

**Phase C: Fix** ⛔
- [ ] Implement fix, test passes
- [ ] Commit: `[C] fix: {fix-name}`

**Phase D: Test Verification**
- [ ] Full test suite passes
- [ ] No regressions

**Phase E: Code Review** ⛔
- [ ] Review Worker validates against contract
- [ ] Review report: PASS

## Close Contract

- [ ] All Contract items pass
- [ ] Human confirmed

**Archive**: Remove symlink from `workspace/contracts/in_progress/`. Actual file stays in `docs/contracts/` (Git history is the archive).
