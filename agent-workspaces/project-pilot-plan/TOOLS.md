# Plan Agent — Tools Notes

## Contract Writing

Plan Agent writes contracts directly (no separate Contract Worker).
Each contract file goes to `docs/contracts/feature/` or `docs/contracts/fix/`.
File names MUST match the markdown link targets in the meta contract table.

## Traceability Chain

All references use markdown relative links:
- **Meta → Spec**: `[spec-name](../specs/xxx.spec.md)`
- **Meta → Contract**: `[contract-name](./feature/xxx.md)`
- **Contract → Meta**: `[meta-name](../meta-xxx.md)`
- **Contract → Spec**: `[spec-name](../../specs/xxx.spec.md)`

## Key Directories

- **Input**: `workspace/current-spec.md` (symlink → `docs/specs/`)
- **Output**: `docs/contracts/meta-*.md` + `docs/contracts/{feature,fix}/`
- **State**: `workspace/meta.md` (symlink → meta contract) + `workspace/contracts/open/` (symlinks → individual contracts)
