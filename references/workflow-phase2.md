# Phase 2: Implementation

**Goal**: Map Contract to code, execute, and verify each item as you go.  
**Hat**: Developer (with Architect and Tester modes)

---

## Overview

Phase 2 executes the work defined in Phase 1 Contracts:
- Move Contracts from `open/` to `in_progress/` one at a time
- Implement per Contract with thinking-stage separation
- Verify each item, update interface docs
- Archive completed Contracts

---

## Step 1: Implementation Brief (Architect Mode)

**Before any code**, produce Contract → Code mapping:
- Each Contract item → target file(s), function(s), module(s)
- New interfaces → define signatures first (no implementation)
- Execution order → dependencies, parallelization opportunities
- **Test Strategy** per item:
  - Test type (unit/integration/e2e)
  - Key test cases (Given/When/Then → test description)
  - Mock/dependency handling

**Format**: Embed in Contract Tasks section. No separate doc needed.  
**Scale**: Mini-Contract → 5-10 bullets. Full Contract → Implementation Plan section.

⛔ **No code before brief is written.**

---

## Step 2: Phase-Gated Development

**Document-First + Test-Driven**: 严格按 Phase A → B → C 顺序执行，不可跳过。

### Phase A: Interface Definition ⛔ GATE A
**准入**: Contract 已批准  
**禁止**: 任何实现代码

- 分析 Contract 场景和边界条件
- 定义接口签名（输入参数、返回值、异常类型）
- 更新 `references/interfaces/{module}.md`
- **Commit**: `[A] docs: interface for {contract-name}`

**⛔ 检查**: Gate A 未完成，禁止开始 Phase B

---

### Phase B: Test Development ⛔ GATE B
**准入**: Gate A commit 完成  
**禁止**: 任何实现代码

- 根据接口编写测试框架
- 实现 Contract items 的测试（必须先失败 - Red）
- 运行测试，确认 Red 状态（截图或日志记录）
- **Commit**: `[B] test: red tests for {contract-name}`

**⛔ 检查**: Gate B 未完成，禁止开始 Phase C

---

### Phase C: Implementation ⛔ GATE C
**准入**: Gate B commit 完成

- 编写最小实现使测试通过（Green）
- 重构优化（保持测试通过）
- 验证接口文档与实际代码一致
- **Commit**: `[C] feat: implement {contract-name}`

---

**Subagents**: 可用于独立任务（文档、测试脚手架、并行模块）

📖 **Task decomposition**: [guides/session-tasks.md](guides/session-tasks.md)

---

## Step 3: Self-Check (Tester Mode)

After Phase C, switch mindset — **assume you don't know the code**:
- Walk through each Contract item, verify passes independently
- Run full test suite
- Verify interface docs current
- Any failure → return to Phase C, fix, re-verify

---

## Step 4: Contract Close Verification

**执行时机**: 所有 Contract items 实现完成，准备 archive 前

### 4.1 Phase Sequence 验证

验证最近 3 个 commit 符合 `[A] → [B] → [C]` 顺序：

```bash
git log -3 --format=%s
```

**通过标准**:
- [ ] Commit-3: `[A] docs: interface for {contract}` — 接口文档
- [ ] Commit-2: `[B] test: red tests for {contract}` — 测试先行
- [ ] Commit-1: `[C] feat: implement {contract}` — 实现代码
- [ ] 当前测试全部通过（Green）

### 4.2 结果处理

**✅ 验证通过 → Squash**:
```bash
git reset --soft HEAD~3
git commit -m "feat: {contract-name}"
```

**❌ 验证失败 → Rollback**:
```bash
git reset --hard HEAD~3
```
**动作**: 返回 Phase A，重新执行 A → B → C

### 4.3 关闭 Contract
- [ ] Squash 后的 commit 已创建
- [ ] 人类最终确认
- [ ] Move to `contracts/archived/`

---

## Step 4: Commit

Commit completed Contract in iteration branch:
```bash
git commit --author="Openclaw <claw@openclaw.local>" -m "feature: {contract-name}"
```

**Commit** (on iteration branch):
```bash
git commit --author="Openclaw <claw@openclaw.local>" -m "feature: {contract-name}"
```

---

## Transition Actions (P2→P3)

Execute these steps **immediately after** all Contracts are archived:

1. **Verify**: `contracts/open/` and `contracts/in_progress/` are empty
2. **Update README**: Change `Phase: 2` → `Phase: 3`
3. **Commit**: `docs: phase 2 → 3`

```bash
git add -A
git commit --author="Openclaw <claw@openclaw.local>" -m "docs: phase 2 → 3"
```

**Human confirmation**: Required before commit.

---

## Exit Criteria

- [ ] Implementation Brief written
- [ ] All Contract items implemented and individually verified
- [ ] Full test suite passing
- [ ] Interface docs updated (if interfaces changed)
- [ ] All Contracts archived
- [ ] README updated to Phase 3
- [ ] Transition commit created

**Claw**: Executes plan, maintains quality, verifies per item, keeps docs current  
**Human**: Available for questions, confirms at Phase end
