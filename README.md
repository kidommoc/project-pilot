# Project-Pilot

**Multi-agent project management for human + claw collaboration.**

Project-pilot takes your idea through a structured development lifecycle — design, planning, implementation, release — with multiple specialized agents handling different phases. You stay in control: every phase transition requires your confirmation before moving forward.

### What it is

- A **harness** that coordinates 9 agents across a full development lifecycle
- A **state machine** driven by the filesystem — project state survives session restarts
- A **document-first** workflow: specs → contracts → code, each reviewed before proceeding

### What it isn't

- Not a coding agent — it orchestrates agents that code
- Not autonomous — human confirmation is required at every gate
- Not a team tool — designed for single human + claw collaboration

---

## How It Works

1. **初始化**（仅首次）: claw 创建项目结构和 `PROJECT.AGENT.md` — **你确认**
2. **设计**: claw 跟你讨论需求，产出 spec 文档 — **你确认**
3. **规划**: claw 将 spec 拆解为具体任务（contracts）— **你确认**
4. **实现**: claw 逐个执行任务（接口 → 测试 → 代码 → review）— **你确认**
5. **发布**: claw 审计所有变更，提交迭代版本 — **你确认**

每次迭代循环 2→5。说 `use project-pilot` 开始，claw 自动检测当前阶段，从断点继续。

---

## Architecture Overview

```
L0: Main Agent (SKILL.md)          ← Router + state machine
    ├── L1: Init Agent             ← Project scaffolding
    ├── L1: Design Agent           ← Spec writing with human
    │       └── L2: Review Worker
    ├── L1: Plan Agent             ← Specs → contracts
    │       └── L2: Review Worker
    ├── L1: Implement Agent        ← Contract execution
    │       ├── L2: Interface Worker
    │       ├── L2: Test Worker
    │       ├── L2: Coding Worker
    │       └── L2: Review Worker
    └── L1: CI/CD Agent            ← Audit + release
            └── L2: Review Worker
```

Each agent has its own workspace under `agent-workspaces/`. Design decisions and technical details are in [ARCHITECTURE.md](ARCHITECTURE.md).

---

*Harness engineering for AI-assisted development.*
