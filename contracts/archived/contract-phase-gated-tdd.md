# Contract: Phase-Gated Document-First Test-Driven Workflow

**Opened**: 2026-04-06T00:00 | **Priority**: medium

## Goal

在 project-pilot 的 Phase 2 Implementation 中强制引入严格的 document-first + test-driven 三阶段门控流程（A:接口定义 → B:测试先行 → C:实现）。

## Problem Statement

当前 workflow 对测试的要求是"验收时通过"，未强制要求：
1. 接口文档必须先于实现完成
2. 测试必须先于实现编写并验证失败（Red）

这导致可能出现"先写代码后补测试"的违规情况，无法保证 document-first 和 test-driven 原则被严格遵守。

## Proposal

### Phase-Gated 结构

每个需要代码实现的 Contract 必须按顺序执行：

**Phase A: Interface Definition**
- 准入：Contract 已批准
- 禁止：任何实现代码
- 输出：`references/interfaces/{module}.md` + commit `[A] docs: interface...`

**Phase B: Test Development**
- 准入：Phase A commit 完成
- 禁止：任何实现代码
- 输出：测试文件（必须先失败 Red）+ commit `[B] test: red tests...`

**Phase C: Implementation**
- 准入：Phase B commit 完成
- 输出：实现代码（使测试 Green）+ commit `[C] feat: implement...`

### 验证与 Squash

Contract Close 前验证最近 3 个 commit 符合 `[A] → [B] → [C]` 顺序：
- ✅ 通过：`git reset --soft HEAD~3 && git commit -m "feat: {name}"`
- ❌ 失败：`git reset --hard HEAD~3` 重做

### 模板更新

- `contract.md`: Tasks 改为三阶段结构，Phase B 包含 Contract items → tests 映射表
- `mini-contract.md`: 简化三阶段结构，无映射表
- `workflow-phase2.md`: 改为 Phase-Gated Development，新增 Step 4 Verification
- `checklists.md`: 删除重复内容（验证已嵌入 workflow）

## Acceptance Criteria

- [x] `workflow-phase2.md` Step 2 改为 Phase A/B/C 三阶段结构，明确门控规则
- [x] `workflow-phase2.md` 新增 Step 4: Contract Close Verification，包含 commit 顺序验证和 squash/rollback 指令
- [x] `templates/contract.md` Tasks 部分改为三阶段，Phase B 包含 items→tests 映射表
- [x] `templates/mini-contract.md` Tasks 部分改为简化三阶段，无映射表
- [x] `checklists.md` 删除 Contract Close 重复检查项（因已嵌入 workflow）
- [x] 所有变更符合 lightweight-workflow 的"一个 Contract = 一个 commit"原则

## Implementation Plan

1. 阅读并理解当前 `workflow-phase2.md`、`templates/contract.md`、`templates/mini-contract.md`、`checklists.md` 内容
2. 修改 `workflow-phase2.md`: Step 2 改为 Phase-Gated，新增 Step 4 Verification
3. 修改 `templates/contract.md`: Tasks 改为三阶段 + 映射表
4. 修改 `templates/mini-contract.md`: Tasks 改为简化三阶段
5. 修改 `checklists.md`: 删除重复 Contract Close 检查项
6. 自审：验证所有 Acceptance Criteria 满足

## Boundary

- **Touches**:
  - `references/workflow-phase2.md`
  - `references/templates/contract.md`
  - `references/templates/mini-contract.md`
  - `references/checklists.md`
- **Does NOT touch**:
  - `contracts/` 目录下现有 Contract 文件
  - `SKILL.md`（不新增 MUST 约束，通过模板强制执行）
  - `README.md`（lightweight-workflow 由 Claw 自动更新）
  - `CHANGELOG.md`（发布时自动更新）
  - `references/workflow-phase1.md`、`workflow-phase3.md`、`workflow-phase4.md`
- **Depends on**: 无

## Notes

**Commit 标记规范**：
- `[A] docs: interface for {contract-name}`
- `[B] test: red tests for {contract-name}`
- `[C] feat: implement {contract-name}`

**验证命令**：
```bash
git log -3 --format=%s | grep -E "^\[(A|B|C)\]"
```

**纯文档修改的 Contract 豁免**：此流程仅适用于需要写代码实现的 Contract。
