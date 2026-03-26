# Interface Contract: {Change Description}

**Status**: draft | approved | completed  
**Date**: YYYY-MM-DD  
**Related Contract**: [link to Mini-Contract or Full Contract]

---

## Purpose

This template is used when a modification involves **module interface changes**. It supplements the main Contract with detailed interface impact analysis.

**When to use**:
- Modifying function signatures (parameters, return types)
- Changing semantic behavior (what a function does)
- Adding/removing callers or dependencies
- Introducing new invariants or constraints

**When NOT needed**:
- Internal implementation changes (no interface impact)
- Bug fixes (behavior unchanged)
- Performance optimizations (interface unchanged)

---

## Modified Interfaces

| Module | Function | Change Type | Description |
|--------|----------|-------------|-------------|
| `file.py` | `function()` | Signature | Added `param` parameter |
| `module.ts` | `interface` | Behavior | Changed return value semantics |

---

## Impact Analysis

### Callers (Who calls these interfaces?)

| Caller Module | Function | Impact | Action Required |
|---------------|----------|--------|-----------------|
| `caller.py` | `func()` | Breaking | Update call site |
| `test.py` | `test_func()` | Non-breaking | Update test assertion |

### Dependencies (What do these interfaces depend on?)

| Dependency | Type | Impact |
|------------|------|--------|
| `STORAGE_ROOT` constant | Internal | Changed value |
| `os.path.join()` | External | None |

---

## Invariants

**New/Modified Invariants**:

1. **Invariant 1**: Semantic constraint (e.g., "function is idempotent")
2. **Invariant 2**: Pre-condition (e.g., "caller must ensure X")
3. **Invariant 3**: Post-condition (e.g., "guaranteed to return Y")

**Unchanged Invariants**:
- List any invariants that remain valid

---

## Interface Docs Update Checklist

- [ ] Read current interface docs (`references/interfaces/{module}.md`)
- [ ] Update function signature
- [ ] Update "Called By" section
- [ ] Update "Depends On" section
- [ ] Update "Invariants" section
- [ ] Add history entry (date + Contract link)
- [ ] Regenerate dependency graph (if structure changed)

---

## Verification

**Interface-Specific Tests**:

```bash
# Run interface contract tests
pytest tests/test_interface_{module}.py

# Verify callers still work
pytest tests/test_callers.py

# Regenerate and validate dependency graph
python scripts/extract-dependencies.py --src . --output .project-graph.json
python scripts/validate-deps.py
```

**Acceptance Criteria**:

- [ ] All callers updated and tested
- [ ] Interface docs reflect current code
- [ ] Dependency graph is valid
- [ ] No breaking changes without migration path

---

## Migration Plan (If Breaking Changes)

**If this change breaks existing callers**:

1. **Deprecation period**: {duration}
2. **Migration guide**: {link or description}
3. **Backward compatibility**: {yes/no, if yes describe}
4. **Removal date**: {planned date for removing old interface}

---

## History

| Date | Change | Contract |
|------|--------|----------|
| YYYY-MM-DD | Initial version | #123 |

---

**Template Version**: 1.0.0 (2026-03-26)  
**Related**: [mini-contract.md](mini-contract.md), [interface-docs.md](../guides/interface-docs.md)
