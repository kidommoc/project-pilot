# {Feature Name}

**Opened**: YYYY-MM-DDTHH:MM

**Author**: Claw
**Approved By**: {Human}

**Modified Files**:
- `file.py` (description - done)

**Pending**:
- [ ] Task 1
- [ ] Interface docs updated (`references/interfaces/xxx.md`)

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

---

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

> **Document-First + Test-Driven**: 严格按 Phase A → B → C 顺序执行，不可跳过。

### Phase A: Interface Definition ⛔ GATE A
**准入**: Contract 已批准  
**禁止**: 任何实现代码

- [ ] 分析 Contract 场景和边界条件
- [ ] 定义接口签名（输入参数、返回值、异常类型）
- [ ] 写入 `references/interfaces/{module}.md`
- [ ] 记录接口决策和约束（如有 trade-off）

**Gate A 完成**:
- [ ] 接口文档已提交（commit 标记 `[A] docs: interface for {contract-name}`）

---

### Phase B: Test Development ⛔ GATE B
**准入**: Gate A 已完成  
**禁止**: 任何实现代码

- [ ] 根据接口编写测试框架
- [ ] 实现 Contract items 的测试（必须先失败）

| Contract Item | 测试文件 | 测试函数 | 状态 |
|--------------|---------|---------|------|
| Core-1: {Given...When...Then...} | `test_xxx.py` | `test_yyy()` | ⬜ Red |
| Core-2: {Given...When...Then...} | `test_xxx.py` | `test_zzz()` | ⬜ Red |
| Edge-1: {...} | `test_xxx.py` | `test_edge1()` | ⬜ Red |

- [ ] 运行测试，确认 Red 状态（失败）

**Gate B 完成**:
- [ ] 测试文件已提交（commit 标记 `[B] test: red tests for {contract-name}`）
- [ ] 所有 Contract items 有对应测试
- [ ] 测试显示 Red（截图或日志记录）

---

### Phase C: Implementation ⛔ GATE C
**准入**: Gate B 已完成

- [ ] 编写最小实现使测试通过（Green）
- [ ] 重构优化（保持测试通过）
- [ ] 验证接口文档与实际代码一致

**Gate C 完成**:
- [ ] 实现代码已提交（commit 标记 `[C] feat: implement {contract-name}`）
- [ ] 所有测试通过

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

**Next Session** (for reference):
- **Suggested**: {Phase N+1 or specific task}
- **First Contract**: {suggested topic}
- **Context**: {ADRs or docs to read}

**Archive**: Move to `contracts/archived/`.

---

> **Downgrade path**: If this Contract has ≤ 5 items, no dependency graph, and single-module scope, consider using a Mini-Contract instead (see [mini-contract.md](mini-contract.md)).
