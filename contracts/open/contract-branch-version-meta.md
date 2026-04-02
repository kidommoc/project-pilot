# Contract: 分支管理、版本管理与元合约模式

**Opened**: 2026-04-02T15:17

**Priority**: high
**Type**: Meta (project-pilot 核心工作流升级)

---

## Goal

在 project-pilot 完整 workflow (A) 中引入：
1. 明确的分支管理策略（main + iteration）
2. 版本管理规范（何时 commit、tag）
3. 元合约（000）模式——用 Contract 来定义 Phase 1
4. 合约命名规范

解决当前 "何时 commit" 不明确、Phase 1 范围管理缺失的问题。

## Context

当前 A 相比 B 缺少清晰的 git 规则。通过本次升级：
- 引入 000 元合约来规划迭代范围
- 明确 iteration 分支生命周期
- 固化 commit 触发点和命名规范

## Boundary

- **Touches**: 
  - `references/workflow.md` (Phase 1/2/4 步骤更新)
  - `references/checklists.md` (checklist 更新)
  - `references/templates/naming-conventions.md` (Commit types、Contract 命名更新)
- **Does NOT touch**: 
  - `contracts/lightweight-workflow.md` (B 保持不变)
  - `SKILL.md` (MUST 约束保持不变)
- **Depends on**: 无

## Proposal

### 1. 元合约（000）模式

**定义**：`C-{MAJOR.MINOR.PATCH}-000-meta.md`，Phase 1 的规划 Contract。

**生命周期**：
```
从 main 切 iteration 分支
Phase 1 开始: 000 在 iteration 分支创建 → draft/
人类确认后: 000 → open/
开始迭代: 000 → in_progress/  ← iteration 分支第一个 commit
创建子合约: 000 指导子合约创建，子合约逐个进入 open/ → in_progress/ → archived/
Phase 1 结束: 000 archived + 所有子合约 open
```

**main 分支原则**：始终保持 Release 终态，不保留任何"进行中"的 Contract 状态。

**000 的 Contract items**：
- [ ] 定义本次迭代的版本号 {MAJOR.MINOR.PATCH}
- [ ] 定义本次迭代要创建的子合约列表（名称、目标）
- [ ] 所有子合约已创建并进入 open/

### 2. 合约命名规范

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
- `C-1.5.0-002-semantic-review.md` — 子合约

**Phase 1 创建流程**：
1. 从 main 切分支：`git checkout -b iteration/v{version}`
2. 在 iteration 分支起草 000：`C-{version}-000-meta.md`
3. 000 进入 open/（人类确认规划）
4. 000 进入 in_progress/，**commit**: `contract: meta v{version}` ← iteration 分支第一个 commit
5. 按 000 规划创建子合约：`C-{version}-001-{name}.md`

**Phase 1 中途新增 Contract**：
- 如需新增子合约，先修改 000（追加到子合约列表）
- 人类确认 000 修改
- 再创建新子合约（Contract-first 原则）

### 3. 分支模型

```
main/master              # 稳定分支，始终保持 Release 终态
iteration/v{version}     # 迭代分支，Phase 1 开始时从 main 创建
```

**分支创建时机**：
1. 确定迭代版本号 `{MAJOR.MINOR.PATCH}`
2. 从 main 切分支：`git checkout -b iteration/v{version}`
3. 在 iteration 分支上创建 000

**分支记录**：README.md 新增 Current Iteration 章节：
```markdown
## Current Iteration
- **Version**: v1.5.0
- **Branch**: iteration/v1.5.0
- **Started**: 2026-04-02
- **Status**: Phase 2 (1 open, 2 archived)
- **000**: C-1.5.0-000-meta.md
```

### 4. Commit 触发点

| 时机 | 分支 | Commit Message |
|------|------|----------------|
| 000 进入 in_progress | iteration/* | `contract: meta v{version}` ← iteration 分支第一个 commit |
| Phase 1 子合约确认进入 open | iteration/* | `contract: define {contract-name}` |
| Phase 2 Contract 完成 | iteration/* | `feature: {contract-name}` |
| Phase 3 Audit 小问题修复 | iteration/* | `fix: audit feedback - {description}` |
| Phase 3 Audit 大问题 | iteration/* | 新建 Contract → `feature: {new-name}` |
| Phase 4 Release | iteration/* | `release: v{version}` |
| Phase 4 结束 | main | Merge iteration/* → main |
| Phase 4 结束 | main | `git tag v{version}` |

### 5. Commit Type 更新

`references/templates/naming-conventions.md`：
- `feat` → `feature` (更直观)
- 保留: `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Contract

- [ ] `references/workflow.md` Phase 1 步骤更新：增加 000 元合约流程、子合约创建步骤、合约命名规范
- [ ] `references/workflow.md` Phase 2 步骤更新：增加 Contract 完成时 commit 说明
- [ ] `references/workflow.md` Phase 4 步骤更新：增加 iteration 分支合并到 main 步骤
- [ ] `references/checklists.md` Phase 1 Completion checklist 更新：增加 000 archived 检查
- [ ] `references/checklists.md` Pre-Release Git 部分更新：明确 iteration 分支检查
- [ ] `references/templates/naming-conventions.md` Commit types: `feat` → `feature`
- [ ] `references/templates/naming-conventions.md` 新增 Contract 命名规范章节
- [ ] README.md 更新：新增 Current Iteration 章节模板
- [ ] 验证：完整流程文档自洽，与 B (lightweight) 保持兼容

## Tasks

1. 阅读当前 workflow.md Phase 1/2/4 结构，标记修改点
2. 修改 Phase 1：
   - 增加 000 元合约作为 Phase 1 起点的说明
   - 增加子合约创建步骤（由 000 指导）
   - 增加合约命名规范
   - 增加 iteration 分支创建时机（000 → in_progress/）
3. 修改 Phase 2：
   - 在 "Contract 完成" 步骤后增加 "Commit: `feature: {contract-name}`"
4. 修改 Phase 4：
   - 增加 "Merge iteration branch to main"
   - 调整 tag 创建步骤到 main 分支
5. 修改 checklists.md：
   - Phase 1 Completion: 增加 000 archived 检查
   - Pre-Release Git: 增加 "Iteration branch merged to main"
6. 修改 naming-conventions.md：
   - Commit types: `feat` → `feature`
   - 新增 "Contract Naming" 章节
7. 修改 README.md：
   - 新增 Current Iteration 章节模板
8. Self-review：检查所有修改点

## Notes

**与 B (lightweight) 的关系**：
- B 保持简化：无 000、无 iteration 分支、One contract = One commit、直接 main 分支
- A 增强：000 规划、iteration 分支、main 始终干净、多 commit per Contract 允许

**main 分支原则**：
- 始终保持 Release 终态
- 不包含任何 draft/open/in_progress 的 Contract
- iteration 分支是"工作区"，main 是"展示区"

**000 的 scope creep 处理**：
- Phase 1 进行中如需新增合约：**先修改 000**（追加合约到列表），人类确认后再创建新子合约
- Contract-first 原则：改规划文档先于执行

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Interface docs updated (if interfaces changed)
- [ ] Human confirmed

**Next Session** (for reference):
- **Suggested**: Phase 2 Implementation
- **First Task**: 阅读当前 workflow.md，标记修改点
- **Context**: 本文件 + workflow.md 原文

**Archive**: Move to `contracts/archived/`.
