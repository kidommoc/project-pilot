# Contract: README 范围澄清

**Opened**: 2026-03-27T12:55  
**Priority**: medium  
**Type**: Meta (project-pilot 自身改进)

---

## Goal

澄清 README 与 contracts/ 的职责边界，避免状态 drift。

---

## Problem Statement

**现状**：
- README 包含详细进度检查清单
- 检查清单需要手动维护，一定会 drift
- 人类问"做到哪了"，Claw 应该读 README 还是 contracts/？不明确

**后果**：
- README 状态与实际进度不一致
- 人类无法信任 README 的信息

---

## Proposal

### README 应该包含

**稳定内容**（低 drift 风险）：
- 项目简介
- 当前 Phase 名称（如 "Phase 2: Implementation"）
- 当前迭代目标（如 "Sprint 1: 用户认证 MVP"）
- Contract 标题列表（仅标题 + checkbox，无细节）
- 版本历史（最近 3-5 个版本，或链接到 CHANGELOG.md）
- 快速开始指南

**Claw 负责维护**：
- Contract 状态变化 → Claw 自动更新 README（作为 Commit 的一部分）
- 人类不需要手动改 README（除非改高层目标）

### README 不应该包含

**易 drift 内容**：
- 任务级别的进度追踪（在 contracts/ 中）
- 详细的验收标准（在 contracts/ 中）
- Phase 完成检查清单（在 Contract 中）

### 人类问"现在做到哪了"时

Claw 应该：
1. 读取 `contracts/in_progress/` — 当前焦点
2. 读取 `contracts/open/` — 等待开始的任务
3. 读取 `contracts/draft/` — 等待确认的合同
4. 总结后回答

**不依赖 README**。

---

## Acceptance Criteria

1. [x] SKILL.md 添加 README 范围说明
2. [x] README.md 模板更新（Contract 标题列表格式）
3. [x] 更新 project-pilot 自己的 README 作为示例

---

## Implementation Plan

### Phase 1: SKILL.md 更新
1. [x] 添加 README 范围说明
2. [x] 明确 Claw 自动维护 README 的责任

### Phase 2: 示例验证
1. [x] 更新 project-pilot 自己的 README 作为示例

---

## Boundary

- **Touches**: `SKILL.md`, `README.md`
- **Does NOT touch**: 已有项目的历史 README（向后兼容）

---

**Ready to start**. Move to `in_progress/` when human confirms.
