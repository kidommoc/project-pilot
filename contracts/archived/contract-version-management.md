# Contract: 版本管理

**Opened**: 2026-03-28T08:50  
**Priority**: high  
**Type**: Meta (project-pilot 自身改进)

**Applicability**: Full project-pilot workflow (4-Phase projects with significant code).  
**Not for**: lightweight-workflow (which uses "Every Contract = One Version").

---

## Phase 2 完成摘要

**更新文件**:
- ✅ README.md: Version 1.2 → 1.3, Current Phase 更新
- ✅ CHANGELOG.md: 添加 v1.3 条目
- ✅ Contract 自身：添加 lightweight vs Full 对比表

**自我审查**:
- ✅ Markdown 语法有效
- ✅ 版本管理规范与 lightweight-workflow 一致
- ✅ 对比表清晰区分两种 workflow
- ✅ 无冲突变更

---

## Goal

为 project-pilot 建立版本管理流程，支持迭代发布和变更追踪。

---

## Problem Statement

**现状**：
- 无版本号规范
- 无 CHANGELOG
- 无 git tag
- Phase 4（Release）无明确操作定义

**后果**：
- 无法追溯历史版本
- 人类不知道"现在是什么版本"
- 发布流程不清晰

---

## Proposal

### 版本号规范

采用 **SemVer**（语义化版本）：`MAJOR.MINOR.PATCH`

- **MAJOR**: 破坏性变更（如 Phase 重构）
- **MINOR**: 向后兼容的功能新增（如新 Contract 类型）
- **PATCH**: 向后兼容的问题修复（如文档修正）

**示例**：`v1.0.0` → `v1.1.0` → `v1.1.1` → `v2.0.0`

### CHANGELOG.md

```markdown
# Changelog

## [v1.1.0] - 2026-03-28
### Added
- 合同状态机重构（单一焦点约束）
- README 范围澄清

### Changed
- SKILL.md 更新目录结构

## [v1.0.0] - 2026-03-27
### Added
- Initial release
- lightweight-workflow.md
```

### Git Tag

每次 Phase 4（Release）完成时：
```bash
git tag -a v1.1.0 -m "Release v1.1.0"
git push origin v1.1.0
```

### Phase 4 操作定义

**Phases 1-3**: No commits. All work happens in working directory.

**Phase 4 (Release)**:
1. 更新 CHANGELOG.md（本迭代完成的 Contracts）
2. 更新 README.md（版本号 + 稳定状态）
3. Bump 版本号（SKILL.md 底部）
4. **Single Git commit**（带简要说明）
5. Git tag（带版本说明）
6. Merge 到 main/master

### Commit Message 格式

```bash
git commit -m "Release v1.1.0: 合同状态机重构 + README 范围澄清"
```

**格式**：`Release v{版本}: {主要变更 1} + {主要变更 2} + ...`

**要求**：
- 标题行 ≤ 72 字符
- 列出本 iteration 完成的主要 Contracts（2-4 个）
- 如果变更太多，用"等"概括

**示例**：
```bash
# 小版本（1-2 个变更）
git commit -m "Release v1.1.0: 合同状态机重构 + README 范围澄清"

# 大版本（多个变更）
git commit -m "Release v2.0.0: 状态机重构 + 版本管理 + 迭代模型等"
```

### Git Tag 说明

```bash
git tag -a v1.1.0 -m "Release v1.1.0 - 2026-03-28

新状态机强制单一焦点约束，README 范围澄清。"
```

**格式**：
- 第 1 行：版本 + 日期
- 第 2 行：空行
- 第 3 行起：1-2 句说明（可选）

### 版本与 Iteration 的关系

- 1 Iteration = 1 Release（通常）
- 小修复可以合并到下次 Release
- 破坏性变更必须单独 Release（MAJOR bump)

**No branches. No intermediate commits. One iteration = One release commit.**

---

## lightweight vs Full Workflow 版本管理对比

| 特性 | lightweight-workflow | Full project-pilot workflow |
|------|---------------------|----------------------------|
| **版本 bump 时机** | 每个 Contract 完成 | 每次 Iteration（多个 Contracts）完成 |
| **版本格式** | `v{Minor}`（如 v1.2, v1.3） | SemVer `MAJOR.MINOR.PATCH` |
| **CHANGELOG 条目** | 每个 Contract 一条 | 每次 Release 一条（包含多个 Contracts） |
| **适用场景** | 单人类 + Claw，快速迭代 | 多 Contract 并行，复杂项目 |
| **Commit 频率** | 每个 Contract 一次 | 每次 Iteration 一次 |

**当前 project-pilot 使用 lightweight-workflow**，因此版本管理遵循简化规则：
- 每个 Contract 完成 = Minor bump（v1.2 → v1.3）
- CHANGELOG 每个 Contract 一条记录
- 单一 Commit + Tag

---

## Acceptance Criteria

1. [x] 明确 lightweight vs Full workflow 版本管理差异
2. [ ] 更新 README.md（Current Phase + Version bump 到 v1.3）
3. [ ] 更新 CHANGELOG.md（v1.3 条目）
4. [ ] Contract 归档

---

## Implementation Plan

### Phase 1: 规范定义（已完成）
1. [x] 添加 lightweight vs Full workflow 对比表
2. [x] 明确当前 project-pilot 使用 lightweight 规则

### Phase 2: 文档更新 + 归档
1. [ ] 更新 README.md（Version: 1.2 → 1.3）
2. [ ] 更新 CHANGELOG.md（添加 v1.3 条目）
3. [ ] 更新 Contract 状态为 completed
4. [ ] 移动到 archived/

---

## Boundary

- **Touches**: `SKILL.md`, `CHANGELOG.md`, `README.md`
- **Does NOT touch**: 已有项目的 contracts/ 目录（向后兼容）

---

**Ready to start**. Move to `in_progress/` when human confirms.
