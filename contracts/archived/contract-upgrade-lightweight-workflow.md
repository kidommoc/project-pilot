# Contract: 升级 lightweight-workflow

**Opened**: 2026-03-28T08:57  
**Completed**: 2026-03-28T09:15  
**Current**: archived  
**Priority**: high  
**Type**: Meta (project-pilot 自身改进)

---

## Goal

升级 lightweight-workflow.md v2.0，整合合同状态机 + README 范围 + 简化版版本管理（每 Contract = 一版本）。

**定位**：lightweight-workflow 是独立于完整 project-pilot workflow 的简化版，用于超轻量项目（如 project-pilot 自身开发）。

---

## Problem Statement

**现状**：
- lightweight-workflow.md 是 1.0 版本（2026-03-27）
- 仍使用旧目录结构（`active/`）
- 未包含 README 范围规范
- 版本管理流程缺失

**问题**：
- 新 Contract 参照旧 workflow，会产生不一致
- 流程演进后，workflow 文档 drift

---

## Proposal

### 保持 2-Phase 简化模型

**Phase 1: Contract Definition**
1. 人类提供目标
2. Claw 起草 Mini-Contract → `contracts/draft/`
3. 人类确认 → 移到 `contracts/open/`
4. **新增**：更新 README（Phase 名称 + Contract 列表）+ Commit

**Phase 2: Implementation**
1. 移到 `contracts/in_progress/`（单一焦点）
2. 实现 + 自审
3. 人类确认 → 移到 `contracts/archived/`
4. **自动更新**：README（checkbox 标记）+ CHANGELOG + Bump Version（minor +1）
5. Git commit（`Release v{新版本}: {Contract 名称}`）
6. Git tag 可选

### 整合内容

**来自合同状态机重构**：
- 目录结构：`draft/` → `open/` → `in_progress/` → `archived/`
- 单一焦点约束
- Session Recovery 算法

**来自 README 范围澄清**：
- README 包含：Phase 名称、Contract 标题列表（仅标题 + checkbox）
- Claw 自动维护 README

**来自版本管理**（简化版，仅适用于 lightweight）：
- 每 Contract = 一小版本（自动 bump minor：v1.0 → v1.1 → v1.2）
- 不需要人类确认发布
- README + CHANGELOG 随 Contract 自动更新
- Git tag 可选（视项目需要）

**注意**：完整版版本管理（4-Phase、MAJOR/MINOR/PATCH 区分）在 project-pilot skill 中定义，不适用于 lightweight-workflow。

### 文档结构（保持简洁）

```markdown
# Workflow for Project-Pilot Self-Development

**Version**: 2.0 (2026-03-28)

## What
（保持现有内容，简化措辞）

## How

### Contract State Machine
- 目录结构 + 单一焦点约束
- Session Recovery 算法

### Phase 1: Contract Definition
- 步骤 1-4（含 README 更新 + Commit）

### Phase 2: Implementation
- 步骤 1-5（含 README 更新 + 可选 Release）

### Version Management（简化）
- SemVer 说明
- CHANGELOG 格式（简要）
- Release checklist（3-4 项）

### README Scope
- 包含/不包含内容
- Claw 自动维护责任
```

---

## Acceptance Criteria

1. [x] lightweight-workflow.md 升级到 v2.0
2. [x] 整合合同状态机、README 范围、简化版版本管理（每 Contract = 一版本）
3. [x] 保持 2-Phase 模型（不扩充为 4 Phase）
4. [x] 明确 lightweight 与完整 project-pilot workflow 的定位差异
5. [x] 移除过时的 `contracts/active/` 引用
6. [x] 文档长度控制在 1.0 版本的 120% 以内（保持轻量）— 149 行 vs 156 行

---

## Implementation Plan

### Phase 1: 文档更新
- [x] 重写 lightweight-workflow.md v2.0
- [x] 整合三个 open contracts 的核心内容
- [x] 移除过时内容

### Phase 2: 验证
- [x] 用本合同作为第一个使用 v2.0 workflow 的示例
- [x] 演示完整流程（README + CHANGELOG + Version bump）

---

## Boundary

- **Touches**: `contracts/lightweight-workflow.md`
- **Does NOT touch**: 已有项目的 contracts/ 目录（向后兼容）

---

## Completion Summary

**Phase 1 完成** ✅
- lightweight-workflow.md v2.0 已更新（149 行）
- README.md 已更新（Current Phase + Contract 列表 + v1.2）
- CHANGELOG.md 已创建（v1.2 条目）

**Phase 2 完成** ✅
- 本合同演示了完整 v2.0 流程
- 等待人类确认后归档

---

**Completed**. Move to `archived/` after human confirmation.
