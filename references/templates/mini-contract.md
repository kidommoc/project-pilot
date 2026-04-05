# {Feature / Change Title}

**Opened**: YYYY-MM-DDTHH:MM

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

> **Document-First + Test-Driven**: 严格按 Phase A → B → C 顺序执行。

**Phase A: Interface Definition** ⛔
- [ ] 定义接口，更新 `references/interfaces/{module}.md`
- [ ] Commit: `[A] docs: interface for {contract-name}`

**Phase B: Test First** ⛔
- [ ] 编写测试（应先失败）
- [ ] 验证 Contract items 均有测试覆盖
- [ ] Commit: `[B] test: red tests for {contract-name}`

**Phase C: Implementation** ⛜
- [ ] 编写实现使测试通过
- [ ] Commit: `[C] feat: implement {contract-name}`
- [ ] 运行测试验证全部通过

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

**Archive**: Move to `contracts/archived/`.

---

> **Upgrade path**: If Contract items exceed 8, or changes span multiple modules with architectural impact, upgrade to a full Contract (see [contract.md](contract.md)) + ADR.
