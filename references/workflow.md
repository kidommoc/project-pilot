# Development Workflow

**Contract-First, Acceptance-Driven.**

No code without an approved Contract. Success is defined by Contract items passing, not by code being written.

---

## Contract Close vs Phase Completion

**Two different concepts**:

| Concept | When | What |
|---------|------|------|
| **Contract Close** | Each Contract completes | Verify Contract items, update interface docs, record Next Session |
| **Phase Completion** | All Contracts in Phase complete | Verify all Contracts done, update README, ask human to continue |

---

## 🚨 Contract Close Protocol

**When a Contract completes** (all items implemented and verified):

### Step 1: Verify Contract Items

- [ ] All Contract items pass (Given/When/Then)
- [ ] Tests written and passing
- [ ] Edge cases covered

### Step 2: Update Interface Docs (If Interfaces Changed)

- [ ] Update `references/interfaces/{module}.md`
- [ ] Regenerate dependency graph (if structure changed)

### Step 3: Record Next Session

**Fill in the Contract's "Next Session" section**:

```markdown
## Next Session

**Suggested**: {Next Contract topic or Phase N+1}
**First Contract**: {specific task}
**Context**: {ADRs or docs to read}
```

### Step 4: Human Confirmation

> "Contract '{name}' completed. Next: {suggested task}. Continue?"

**⛔ Wait for confirmation** before starting next Contract.

### Step 5: Archive Contract

- Move to `contracts/archived/`

---

## 🚨 Phase Completion Protocol (MUST-1)

**When all Contracts in a Phase are completed**:

### Step 0: Verify All Contracts Done

- [ ] All Contracts in Phase closed (check `contracts/archived/`)
- [ ] No pending Contracts in `contracts/in_progress/` or `contracts/open/`

### Step 1: Ask User

> "Phase N completed (all Contracts done). Continue to Phase N+1?"

**⛔ Wait for confirmation** before starting Phase N+1.

**Note**: README.md phase status is maintained in iteration branches only. Main branch shows only `Current release: v{X.Y.Z}`.

---

## Phase 1: Contract Definition

**Goal**: Define WHAT to build and HOW to verify it.  
**Hat**: Product + Architect

### Branch Model

```
main/master              # 稳定分支，始终保持 Release 终态
iteration/v{version}     # 迭代分支，Phase 1 开始时从 main 创建
```

**main 分支原则**：始终保持 Release 终态，不保留任何"进行中"的 Contract 状态。

### 000 Meta-Contract (Iteration Planning)

**元合约模式**：在完整 workflow 中，Phase 1 从 000 元合约开始。

**文件命名**：`C-{MAJOR.MINOR.PATCH}-000-meta.md`

**生命周期**：
```
从 main 切 iteration 分支
git checkout -b iteration/v{version}
Phase 1 开始: 000 在 iteration 分支创建 → draft/
人类确认后: 000 → open/
开始迭代: 000 → in_progress/  ← iteration 分支第一个 commit: contract: meta v{version}
创建子合约: 000 指导子合约创建，子合约逐个进入 open/ → in_progress/ → archived/
Phase 1 结束: 000 archived + 所有子合约 open
```

**000 的 Contract items**：
- [ ] 定义本次迭代的版本号 `{MAJOR.MINOR.PATCH}`
- [ ] 定义本次迭代要创建的子合约列表（名称、目标）
- [ ] 所有子合约已创建并进入 open/

**Phase 1 中途新增 Contract**：
如需新增子合约，**先修改 000**（追加到子合约列表），人类确认后再创建新子合约。

### Contract Naming Convention

**文件命名**：`C-{MAJOR.MINOR.PATCH}-{No.}-{name}.md`

| 组件 | 含义 | 示例 |
|------|------|------|
| `C` | Contract 前缀 | 固定 |
| `{MAJOR.MINOR.PATCH}` | 迭代版本号 | `1.5.0` |
| `{No.}` | 该迭代内的 Contract 序号，000 保留给元合约 | `000`, `001`, `002` |
| `{name}` | 短横线连接的小写名称 | `branch-management` |

**示例**：
- `C-1.5.0-000-meta.md` — 元合约
- `C-1.5.0-001-branch-version.md` — 子合约

### Contract Selection

| Criteria | Use |
|----------|-----|
| ≤ 8 contract items, single module, no complex deps | **Mini-Contract** ([template](templates/mini-contract.md)) |
| > 8 items, multi-module, architectural impact, dep graph | **Full Contract** ([template](templates/contract.md)) |

### Steps

1. **从 main 创建 iteration 分支**：`git checkout -b iteration/v{version}`
2. **创建 000 元合约**：起草 `C-{version}-000-meta.md`，定义版本号和子合约列表
3. **语义预审查**：Claw 对 000 进行自我审查（见下方「语义预审查机制」）
4. Human 确认 000 规划
5. **000 → in_progress/**，**Commit**: `contract: meta v{version}`（iteration 分支第一个 commit）
6. 按 000 规划创建子合约：`C-{version}-001-{name}.md`，`C-{version}-002-{name}.md`...
7. 每个子合约进入 `draft/` → **语义预审查** → Human 确认 → `open/`
8. **Phase 1 结束**：000 archived + 所有子合约 in `open/`

---

### 语义预审查机制

**时机**：每完成一个 Contract draft 后立即进行（而非等 Phase 1 所有 Contract 完成）。

**目的**：在 Human 审阅前进行语义层面的自检，确保生成的文档与原始意图一致，避免 LLM 生成偏离需求。

**审查维度**：

| 维度 | 检查内容 |
|------|----------|
| **意图一致性** | Contract 是否匹配最初讨论的 idea/purpose？ |
| **需求覆盖度** | 是否遗漏了人类提出的要求？ |
| **逻辑自洽性** | Contract items 之间是否有冲突？Boundary 是否清晰？ |
| **可执行性** | Contract items 是否足够具体，能转化为代码/行动？ |
| **命名一致性** | 术语使用是否一致？是否有歧义？ |

**审查输出格式**：

```markdown
## 预审查报告: {Contract-name}

### ✅ 已覆盖
- {列出已正确实现的需求点}

### ⚠️ 可能遗漏
- {列出可能遗漏或弱化的需求点}

### ❓ 需要澄清
- {列出语义模糊、需要人类确认的点}

### 建议
- {改进建议，可选}
```

**人类决策**：收到预审查报告后，人类选择：
- **确认**：Contract 进入 `open/`
- **修改**：Claw 根据反馈修改，重新预审查
- **忽略**：人类认为报告误报，直接确认

**注意**：预审查不是替代人类审阅，而是帮助人类更快发现问题。

**Claw responsibility**: Propose complete, actionable Contract with testable acceptance criteria  
**Human role**: Audit Contract items (especially edge cases and boundaries), confirm or request changes

### Exit Criteria

- [ ] iteration 分支已创建（`iteration/v{version}`）
- [ ] 000 元合约已 archived（规划完成）
- [ ] 所有子合约已创建并进入 `open/`
- [ ] ADRs created (if architectural decisions involved)

---

## Phase 2: Implementation

**Goal**: Map Contract to code, execute, and verify each item as you go.

Phase 2 enforces **thinking-stage separation** — same Claw, different hats at each step.

### Step 1: Implementation Brief (Architect Hat)

**Before writing any code**, produce a Contract → Code mapping:

- Each contract item → target file(s), function(s), module(s)
- New interfaces → define signatures first (no implementation yet)
- Execution order → which items have dependencies, which can be parallelized (subagent-eligible)
- **Test Strategy** → 每个 Contract item 的测试方案
  - 测试类型（unit/integration/e2e）
  - 关键测试用例（Given/When/Then 转化为测试描述）
  - Mock/依赖处理方式

**Format**: Embed in Contract file (Tasks section) or README. No separate document needed.  
**Scale**: Mini-Contract → 5-10 bullet points. Full Contract → Implementation Plan section.

⛔ **No code before the brief is written.**

### Step 2: Test-First Development (Developer Hat)

执行顺序遵循 Implementation Brief，采用 **红-绿-重构** 循环：

对每个 Contract item：

1. **红**: 编写测试（测试应失败，验证测试有效）
2. **绿**: 编写最小实现使测试通过
3. **重构**: 优化代码（保持测试通过）

**记录要求**: 在 Contract 中标记每个 item 对应的测试用例：

```markdown
- [ ] Given ... When ... Then ...
  - **Test**: `test_feature_x.py::test_scenario_y()`
```

**执行中检查点**:
- **Per-item verification**: 每个 item 完成后立即验证对应测试通过
- **Interface docs update**: 接口变更时立即更新文档
- **Regression check**: 修复回归问题后才能继续
- **Subagents**: 用于独立任务（文档、测试脚手架、并行模块）

📖 **Task decomposition guide**: [guides/session-tasks.md](guides/session-tasks.md)

### Step 3: Self-Check (Tester Hat)

After all items are implemented, switch mindset — **pretend you don't know how the code works**:

- **TDD 验证**: 每个 Contract item 都有对应测试用例
- Walk through each contract item, verify it passes independently
- Run full test suite
- Verify interface docs are up to date
- If any item fails → return to Step 2, fix, re-verify

### Step 4: Commit

Contract 完成后，在 iteration 分支提交（Claw 使用 `--author` 显式标识身份）：

```bash
git commit --author="Openclaw <claw@openclaw.local>" -m "feature: {contract-name}"
```

**Commit 触发点**：

| 时机 | Commit Message |
|------|----------------|
| 000 进入 in_progress | `contract: meta v{version}` ← iteration 分支第一个 commit |
| Phase 1 子合约确认进入 open | `contract: define {contract-name}` |
| Phase 2 Contract 完成 | `feature: {contract-name}` |
| Phase 3 Audit 小问题修复 | `fix: audit feedback - {description}` |
| Phase 3 Audit 大问题 | 新建 Contract → `feature: {new-name}` |
| Phase 4 Release | `release: v{version}` |

### Exit Criteria

- [ ] Implementation Brief written
- [ ] All Contract items implemented and individually verified
- [ ] Full test suite passing
- [ ] Interface docs updated (if interfaces changed)
- [ ] Contract status updated to "Done"
- [ ] **Committed**: `feature: {contract-name}`

**Claw responsibility**: Execute plan, maintain quality, verify per item, keep interface docs current  
**Human role**: Available for questions, confirms at Phase end

---

## Phase 3: Audit

**Goal**: Independent audit against the Contract, then deliver to human.  
**Hat**: Auditor (adversarial to the Phase 2 developer)

The Claw in this phase takes an **opposing stance** to its Phase 2 self. The question is not "did I implement it?" but "does it actually satisfy the Contract?"

### Steps

1. **Contract Audit**: Walk each contract item, verify actual behavior matches the criterion
2. **Code quality check**: Lint, naming conventions, documentation
3. **Produce Audit Summary** for human:
   - Contract items: per-item pass/fail
   - Test results
   - Changes summary (files touched, lines changed)
   - Known risks / tech debt
4. Human reviews (depth at human's discretion: spot / full / delegated)
5. Claw addresses feedback (if any)
6. Human confirms

### Audit Checklist

- [ ] All Contract items verified (each one individually checked against actual behavior)
- [ ] Tests pass
- [ ] No lint errors
- [ ] Docs updated
- [ ] ADRs created (if applicable)
- [ ] Naming conventions followed

### Exit Criteria

- [ ] Audit Summary delivered to human
- [ ] Human confirmation obtained
- [ ] Feedback addressed (if any)

**Claw responsibility**: Audit thoroughly from an adversarial perspective, present clearly  
**Human role**: Validate, confirm, or request changes

---

## Phase 4: Release

**Goal**: Package and ship.  
**Hat**: Release Engineer

**Version History**: CHANGELOG.md is the **single source of truth** for version history. README.md only shows current release.

### Steps

1. **Cleanup README** (iteration branches only)
   - Remove `## Current Iteration` section
   - Commit: `chore: cleanup iteration tracking`
2. Claw updates CHANGELOG.md
3. Claw bumps version (SemVer)
4. **Commit** (Claw identity): 
   ```bash
   git commit --author="Openclaw <claw@openclaw.local>" -m "release: v{version}"
   ```
   （在 iteration 分支）
5. **合并到 main**：
   ```bash
   git checkout main
   git merge iteration/v{version}
   ```
6. Claw creates git tag (`v{version}`)（在 main 分支）
   ```bash
   git tag v{version}
   ```
7. Claw presents release summary to human
8. Human confirms release

### Version Bumping

| Change | Bump | Example |
|--------|------|---------|
| Breaking | MAJOR | 1.0.0 → 2.0.0 |
| Feature | MINOR | 1.2.0 → 1.3.0 |
| Fix | PATCH | 1.2.3 → 1.2.4 |

### Exit Criteria

- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] **Committed**: `release: v{version}`（iteration 分支）
- [ ] **Merged**: iteration branch → main
- [ ] **Git tag created**: `v{version}`（main 分支）
- [ ] Human confirmation obtained

**Claw responsibility**: Package correctly, follow SemVer  
**Human role**: Confirm release or request changes

---

## Templates

| Template | Use Case |
|----------|----------|
| [Mini-Contract](templates/mini-contract.md) | Default for most changes |
| [Full Contract](templates/contract.md) | Multi-module, complex features |
| [ADR](templates/adr.md) | Architectural decisions |
| [Naming Conventions](templates/naming-conventions.md) | Reference |

---

**Version**: 0.7.0 | **See also**: [SKILL.md](../SKILL.md), [checklists.md](checklists.md)
