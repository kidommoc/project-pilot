# Contract: TDD 强制化

**Opened**: 2026-04-02T15:20

**Priority**: medium
**Type**: Meta (开发方法论)

---

## Goal

在 project-pilot workflow 中强制引入 Test-Driven Development (TDD)，使测试成为开发的前提而非后续补救。

## Context

当前 workflow 对测试的要求是"验收时测试通过"，未强制测试先行。TDD 强制化将改变 Phase 2 Implementation 的执行顺序：先写测试，后写实现。

## Boundary

- **Touches**: 
  - `references/workflow.md` (Phase 2 步骤更新)
  - `references/templates/mini-contract.md` (可选：测试章节)
- **Does NOT touch**: 
  - Phase 1/3/4 流程
  - Contract 状态机
- **Depends on**: 无

## Proposal

### TDD 流程（嵌入 Phase 2）

```
Phase 2: Implementation
├── Step 1: Implementation Brief (Architect Hat)
│   └── 包含：每个 Contract item 的测试策略
├── Step 2: Test-First Development (Developer Hat)
│   ├── 对每个 Contract item:
│   │   ├── 1. 编写测试（红）
│   │   ├── 2. 编写实现（绿）
│   │   └── 3. 重构（可选）
│   └── 记录：测试覆盖的 Contract item
└── Step 3: Self-Check (Tester Hat)
    └── 验证：所有 Contract item 都有对应测试，且通过
```

### Implementation Brief 新增要求

原有内容：
- Each contract item → target file(s), function(s)
- Execution order

新增：
- **Test Strategy**: 每个 Contract item 的测试方案
  - 测试类型（unit/integration/e2e）
  - 关键测试用例（Given/When/Then 转化为测试描述）
  - Mock/依赖处理方式

### Contract items 与测试的映射

每个 Contract item 必须能追溯到至少一个测试用例：

```markdown
## Contract

- [ ] Given ... When ... Then ...
  - **Test**: `test_feature_x.py::test_scenario_y()`
```

### 强制检查点

Phase 2 结束时验证：
- [ ] 每个 Contract item 有对应测试
- [ ] 所有测试通过
- [ ] 测试覆盖率报告（如适用）

## Contract

- [ ] `references/workflow.md` Phase 2 Step 1 更新：Implementation Brief 必须包含 Test Strategy
- [ ] `references/workflow.md` Phase 2 Step 2 更新：改为 "Test-First Development"，明确红-绿-重构循环
- [ ] `references/workflow.md` Phase 2 Step 3 更新：验证每个 Contract item 有对应测试
- [ ] 验证：TDD 流程与现有 Contract 机制兼容

## Tasks

1. 阅读当前 workflow.md Phase 2 结构
2. 修改 Step 1 (Implementation Brief)：增加 Test Strategy 要求
3. 修改 Step 2：改为 "Test-First Development"，描述红-绿-重构流程
4. 修改 Step 3 (Self-Check)：增加"每个 Contract item 有对应测试"检查点
5. Self-review

## Notes

**TDD 不是可选的**，是 Phase 2 的必需步骤。

**测试类型灵活性**：根据项目类型选择 unit/integration/e2e，不要求全覆盖，但每个 Contract item 必须能被测试验证。

**与现有验收标准的衔接**：TDD 的"绿"状态 = 原有的"验收通过"。

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Human confirmed

**Next Session**:
- **Suggested**: Phase 2 Implementation
- **First Task**: 修改 workflow.md Phase 2

**Archive**: Move to `contracts/archived/`.
