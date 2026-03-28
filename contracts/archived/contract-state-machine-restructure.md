# Contract: 合同状态机重构

**Opened**: 2026-03-27T12:55  
**Current**: archived  
**Priority**: high  
**Type**: Meta (project-pilot 自身改进)

**Modified Files**:
- `SKILL.md` (更新合同状态机、目录结构、Session Recovery 算法、单一焦点约束 - done)

**Completed**:
- [x] Phase 1: SKILL.md 更新
- [x] Phase 2: 示例验证（本合同演示完整状态流转：draft → open → in_progress → archived）

---

## Goal

解决 project-pilot 在实战中暴露的合同状态追踪问题，通过目录结构强制"单一焦点"约束。

---

## Problem Statement

**现状**：
- `contracts/active/` 可以有多个合同（违反"最多 1 个"约束）
- 状态字段 (`draft`/`in_progress`/`completed`) 语义混乱
- Claw 恢复时无法确定"当前焦点"，被迫依赖对话历史

**后果**：
- 人类被迫在对话中告诉 Claw"现在做 XXX"
- 违反"状态在文件中，不在对话历史里"的原则

---

## Proposal

### 目录结构

```
contracts/
├── draft/           ← Claw 起草完成，等人类确认
├── open/            ← 人类已确认，等待开始（可以有多个）
├── in_progress/     ← 当前焦点（只能有 1 个）
└── archived/        ← 已完成
```

### 状态流转

```
Claw 起草 → draft/ → 人类确认 → open/ → 开始实施 → in_progress/ → 完成 → archived/
                              ↑                                     │
                              └────────── 拒绝/修改 ────────────────┘
```

### 关键约束

| 目录 | 用途 | 数量约束 |
|------|------|----------|
| `draft/` | Claw 起草完成，等人类确认 | 可以有多个 |
| `open/` | 人类已确认，等待开始 | 可以有多个（类似 GitHub open issues） |
| `in_progress/` | 当前实施焦点 | **只能有 1 个**（强制执行） |
| `archived/` | 已完成 | 无限制 |

### Claw 恢复算法

```
1. ls contracts/in_progress/
   - 1 个 → 读取，继续
   - 0 个 → 检查 open/ → 选择下一个 → 移入 in_progress/
   - >1 个 → 🚨 错误状态，报告用户

2. 读取合同 Status 章节，找到最后一个 completed task，继续
```

---

## Acceptance Criteria

1. [x] SKILL.md 更新合同状态机描述
2. [x] SKILL.md 更新目录结构说明
3. [x] SKILL.md 添加"单一焦点"强制约束
4. [x] SKILL.md 添加 Session Recovery 算法
5. [x] 创建示例合同展示新状态机（本合同）

---

## Implementation Plan

### Phase 1: SKILL.md 更新 ✅
1. [x] 修改合同状态机章节
2. [x] 修改目录结构说明
3. [x] 添加 Session Recovery 算法
4. [x] 添加单一焦点约束说明

### Phase 2: 示例验证
1. [ ] 用本合同作为第一个示例
2. [ ] 演示完整状态流转（draft → open → in_progress → archived）

---

## Boundary

- **Touches**: `SKILL.md`
- **Does NOT touch**: 已有项目的 contracts/ 目录（向后兼容）

---

## Next Session

**Suggested**: 执行 Phase 2（示例验证）

**Context**: Phase 1 已完成，等待人类确认后继续 Phase 2。

---

**Phase 1 完成**。SKILL.md 已更新，新状态机已生效。继续执行 Phase 2（用本合同演示完整状态流转）？
