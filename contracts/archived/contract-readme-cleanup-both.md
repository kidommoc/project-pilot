# Contract: 统一简化 README 中的版本记录和 Phase 追踪

**Opened**: 2026-04-02T15:47

**Priority**: high
**Type**: Meta (A 和 B 方法统一优化)

---

## Goal

统一简化 project-pilot 的两种工作流（A 完整版 和 B lightweight 版）：
- 移除 README 中的**版本变更历史**（移到 CHANGELOG）
- **简化** README 中的 Phase 追踪（保留极简状态，移除详细列表）
- **发布前清理**：Release commit 前移除 Current Iteration 区块

## Context

当前 A 和 B 都要求 Claw 在 README 中维护：
- Phase 状态 + **详细的 Contract 列表**（易 drift）
- **版本变更历史**（与 CHANGELOG 重复）

这导致：
1. README 频繁变动，产生不必要的 commit 噪音
2. 版本历史在 README 和 CHANGELOG 中重复
3. 详细 Contract 列表与 contracts/ 目录冗余

但完全移除 Phase 追踪会导致零背景 agent 无法快速判断"现在该做什么"。

## Boundary

- **Touches**: 
  - `SKILL.md` (MUST-1, State Transparency 章节)
  - `references/workflow.md` (Phase Completion Protocol, Phase 4)
  - `contracts/lightweight-workflow.md` (Phase 2, Release Checklist, README Scope)
  - `README.md` (简化 Phase 章节，移除 Version 章节)
- **Does NOT touch**: 
  - Contract 状态机
  - 目录结构
- **Depends on**: 无

## Proposal

### 统一原则

| 文档 | 新职责 |
|------|--------|
| **README.md** | 项目概述、**极简 Phase 状态（仅迭代中）**、Quick Start、相关链接 |
| **CHANGELOG.md** | 版本历史（唯一来源） |
| **contracts/** | Contract 级别状态（目录结构即状态） |
| **main 分支** | 仅显示 `Current release: v{X.Y.Z}` |
| **iteration 分支** | 显示完整的 Current Iteration 区块 |

### 极简状态格式

**main 分支（始终）**：
```markdown
# Project-Pilot

Current release: v1.5.0
```

**iteration 分支（迭代期间）**：
```markdown
# Project-Pilot

Current release: v1.5.0

## Current Iteration

- **Version**: v1.6.0
- **Phase**: 2 (Implementation)
- **000**: C-1.6.0-000-meta.md
- **Status**: 2 open, 1 in_progress, 3 archived
```

### 生命周期管理

| 时机 | 动作 | 分支 |
|------|------|------|
| 迭代开始（000 → in_progress）| 添加 Current Iteration 区块 | iteration/* |
| 迭代进行中 | 更新 Current Iteration 状态 | iteration/* |
| **Release commit 前** | **移除 Current Iteration 区块** | iteration/* |
| 合并到 main | main 仅显示 Current release | main |

### A 方法（完整 4-Phase）修改

**SKILL.md MUST-1** — 移除 README 更新步骤（状态在 iteration 分支维护，无需在 main 更新）：
```
原: 0. Test → 1. Update interface docs → 2. Update README.md phase status → 3. Ask user
新: 0. Test → 1. Update interface docs → 2. Ask user
```

**workflow.md Phase 4 Release** — 增加清理步骤：
```
原: CHANGELOG updated, version bumped, git tag created
新: 
  1. Cleanup README (移除 Current Iteration 区块)
  2. Commit: "chore: cleanup iteration tracking"
  3. CHANGELOG updated
  4. version bumped  
  5. git tag created
```

### B 方法（lightweight）修改

**lightweight-workflow.md Phase 2** — 更新：
```
原: Claw auto-updates: README + CHANGELOG + Bump Version
新: 
  1. Claw auto-updates: CHANGELOG + Bump Version
  2. README: 添加/更新 Current Iteration（迭代中）
  3. Release commit 前: 移除 Current Iteration
```

**lightweight-workflow.md Release Checklist** — 增加清理项：
```
- [ ] Cleanup README (移除 Current Iteration)
- [ ] Commit: "chore: cleanup iteration tracking"
- [ ] Update CHANGELOG.md
- [ ] Update version
- [ ] Git commit + optional tag
```

**lightweight-workflow.md README Scope** — 更新：
```
原: Include: Phase name, Contract list, Version
新: Include: 项目概述、Quick Start
    Exclude: 详细 Phase 追踪（迭代中在 iteration 分支）、版本历史
```

### README.md 清理

**main 分支目标状态**：
```markdown
# Project-Pilot

Current release: v1.5.0

[其余项目概述内容...]
```

**移除**：
- `## Current Phase` 及其所有详细子章节
- `## Version` 及其所有版本历史子章节

**迭代期间（iteration 分支）临时添加**：
- `## Current Iteration` 极简区块

## Contract

- [x] `SKILL.md` MUST-1: 移除 "Update README.md phase status" 步骤
- [x] `references/workflow.md` Phase Completion Protocol: 移除 Update README.md 步骤
- [x] `references/workflow.md` Phase 4: 增加 "Cleanup README" 步骤（移除 Current Iteration）
- [x] `references/workflow.md` Phase 4: 明确 CHANGELOG 是唯一版本记录
- [x] `contracts/lightweight-workflow.md` Phase 2: 更新 README 管理（迭代中添加，发布前移除）
- [x] `contracts/lightweight-workflow.md` Release Checklist: 增加 "Cleanup README" 项
- [x] `contracts/lightweight-workflow.md` README Scope: 更新为 main 仅显示 release
- [x] `README.md`: 简化为仅显示 `Current release: v{X.Y.Z}`
- [x] 验证：A 和 B 的 README 职责一致，main 始终干净

## Tasks

1. 读取并标记修改点：SKILL.md, workflow.md, lightweight-workflow.md, README.md
2. 修改 SKILL.md：
   - MUST-1 移除 README 更新步骤
3. 修改 workflow.md：
   - Phase Completion Protocol 移除 Update README
   - Phase 4 增加 Cleanup README 步骤
   - Phase 4 明确 CHANGELOG 唯一版本记录
4. 修改 lightweight-workflow.md：
   - Phase 2 README 管理改为"迭代中添加，发布前移除"
   - Release Checklist 增加 Cleanup 项
   - README Scope 更新
5. 修改 README.md：
   - 简化为仅显示 `Current release: v{X.Y.Z}`
   - 移除详细 Phase 和 Version 章节
6. Self-review：确保 A 和 B 的 README 职责一致

## Notes

**为什么 main 只显示 release？**
- main 始终反映 Release 终态，没有"进行中"的临时信息
- iteration 分支是"工作区"，Current Iteration 在那里维护
- Release commit 前清理 = 明确标记"迭代结束，准备归档"

**为什么 Release 前专门 cleanup commit？**
- 清晰的语义："清理迭代追踪，准备发布"
- 方便回滚：如果发布有问题，cleanup commit 可单独 revert

**CHANGELOG 是唯一版本记录**
- README 不再重复版本历史
- 所有版本变更详情在 CHANGELOG.md

---

## Close Contract

**Completed**: 2026-04-02T16:25

**Verification**:
- [x] All Contract items pass
- [ ] Human confirmed

**Summary**:
- SKILL.md: MUST-1 移除 README 更新步骤，添加 iteration branch 说明
- workflow.md: Phase Completion Protocol 移除 Update README，Phase 4 增加 Cleanup + CHANGELOG 唯一版本说明
- lightweight-workflow.md: Phase 2 README 管理更新，Release Checklist 增加 Cleanup，README Scope 更新
- README.md: 简化为仅 `Current release: v{X.Y.Z}`，移除 Phase/Version 详细章节
- CHANGELOG.md: 添加 v1.5.0 条目

**Next Session**:
- **Suggested**: 选择下一个 open contract（剩余 4 个）
- **Contracts remaining**: branch-version-meta, semantic-review, tdd-enforcement, unify-templates-docs

**Archive**: Move to `contracts/archived/`.
