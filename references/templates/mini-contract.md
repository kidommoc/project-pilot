# {Feature / Change Title}

**Opened**: YYYY-MM-DDTHH:MM
**Status**: draft | in_progress | completed | pending-confirmation
**Modified Files**:
- `file.py` (description - done)

**Pending**:
- [ ] Task 1
- [ ] Interface docs updated (`references/interfaces/xxx.md`)

---

## Goal

{One sentence: what problem does this change solve?}

## Context

{Why this is needed. Background, trigger, related ADR links. 2-3 sentences.}

## Boundary

- **Touches**: {affected files/modules, comma-separated}
- **Does NOT touch**: {explicitly excluded scope — prevents scope creep}
- **Depends on**: {preconditions or external deps, "none" if none}

## Impact Analysis

**Run before starting implementation**:

```bash
# Find files impacted by changes
python scripts/extract-doc-deps.py --src . --output .doc-graph.json
python scripts/query-doc-deps.py --graph .doc-graph.json --impact {modified_file.md}
```

**Referenced by**:
- {List files that reference the modified files}

**Requires update**:
- [ ] project-types/*.md (if project-init.md or SKILL.md changed)
- [ ] Templates (if core workflow changed)
- [ ] Guides (if referenced)

## Interface Contract

> **MUST**: If this change modifies module interfaces, document the interface contract below.

**Modified Interfaces**:
- `file.py:function()` → parameter/return type changes

**Callers**:
- List modules that call this interface

**Invariants**:
- Semantic constraints the interface must satisfy

## Contract

> Each item below is an acceptance criterion. On Phase completion, verify each one. All must pass.

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}
- [ ] {Plain testable assertion — strict Gherkin format not required}

## Tasks

1. {Concrete step}
2. {Concrete step}
3. Verify: run `{test command}` → all contract items pass

## Notes

{Optional. Open questions, known risks, future extension directions.}

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Interface docs updated (if interfaces changed)
- [ ] Human confirmed

**Next Session** (for reference):
- **Suggested**: {Phase N+1 or specific task}
- **First Contract**: {suggested topic}
- **Context**: {ADRs or docs to read}

**Archive**: Move to `contracts/archive/`, mark Status as `completed`.

---

> **Upgrade path**: If Contract items exceed 8, or changes span multiple modules with architectural impact, upgrade to a full Contract (see [contract.md](contract.md)) + ADR.
