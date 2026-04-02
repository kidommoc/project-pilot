# Contract: 语义预审查机制

**Opened**: 2026-04-02T15:20

**Priority**: medium
**Type**: Meta (质量保障机制)

---

## Goal

在 Contract 创建后立即进行语义层面的预审查，确保生成的文档与原始意图一致，避免 LLM 生成偏离需求。

## Context

LLM 生成机制存在"幻觉"或理解偏差风险。当前 workflow 中，Contract draft 创建后直接由人类审阅，缺少结构化自检环节。

引入语义预审查：每写完一个 Contract，Claw 立即进行自我审查，输出检查报告，供人类参考。

## Boundary

- **Touches**: 
  - `references/workflow.md` (Phase 1 步骤更新)
  - `references/templates/mini-contract.md` (可选：增加预审查章节)
- **Does NOT touch**: 
  - Contract 状态机
  - 其他 Phase 流程
- **Depends on**: 无

## Proposal

### 审查时机

**每完成一个 Contract draft 后立即进行**（而非等 Phase 1 所有 Contract 完成）。

```
Phase 1: Contract Definition
├── 000 起草 → 预审查 → 人类审阅 → 确认
├── 子合约 1 起草 → 预审查 → 人类审阅 → 确认
├── 子合约 2 起草 → 预审查 → 人类审阅 → 确认
└── ...
```

### 审查维度

| 维度 | 检查内容 |
|------|----------|
| **意图一致性** | Contract 是否匹配最初讨论的 idea/purpose？ |
| **需求覆盖度** | 是否遗漏了人类提出的要求？ |
| **逻辑自洽性** | Contract items 之间是否有冲突？Boundary 是否清晰？ |
| **可执行性** | Contract items 是否足够具体，能转化为代码/行动？ |
| **命名一致性** | 术语使用是否一致？是否有歧义？ |

### 审查输出格式

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

### 人类决策

收到预审查报告后，人类选择：
- **确认**：Contract 进入 open/
- **修改**：Claw 根据反馈修改，重新预审查
- **忽略**：人类认为报告误报，直接确认

## Contract

- [x] `references/workflow.md` Phase 1 步骤更新：每个 Contract draft 创建后增加"语义预审查"步骤
- [x] 预审查输出格式标准化（如上方模板）
- [x] 验证：预审查机制与现有 Contract 状态机兼容

## Tasks

1. 阅读当前 workflow.md Phase 1 结构
2. 在"Claw drafts"和"Human reviews"之间插入"语义预审查"步骤
3. 定义预审查报告模板
4. Self-review

## Notes

**预审查不是替代人类审阅**，而是帮助人类更快发现问题。

**上下文保持**：立即审查（每 Contract 一完就审）优于批量审查（所有 Contract 完再审），因为上下文正"热"。

---

## Close Contract

**Verification**:
- [x] All Contract items pass
- [ ] Human confirmed

**Next Session**:
- **Suggested**: 处理剩余 open contracts（`contract-tdd-enforcement.md` 或 `contract-unify-templates-docs.md`）
- **First Contract**: 任选其一，建议按优先级顺序
- **Context**: `contracts/open/`

**Archive**: Move to `contracts/archived/`.
