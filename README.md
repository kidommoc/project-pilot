# Project-Pilot

**人机协作的多 agent 项目管理工具。**

Project-pilot 将你的想法引导通过一个结构化的开发生命周期——设计、规划、实现、发布——由多个专职 agent 分工协作。你始终掌控全局：每个阶段转换都需要你确认后才会继续。

### 是什么

- 一个**调度框架**，协调 9 个 agent 完成完整开发周期
- 一个**文件驱动的状态机**——项目状态基于文件系统，跨会话不丢失
- 一个**文档先行**的工作流：spec → 合同 → 代码，每一步都经过 review

### 不是什么

- 不是编码 agent——它调度会编码的 agent
- 不是自治系统——每个关键节点都需要人类确认
- 不是团队工具——为单人 + claw 协作设计

---

## 工作流程

1. **初始化**（仅首次）：claw 创建项目结构和 `PROJECT.AGENT.md` — **你确认**
2. **设计**：claw 跟你讨论需求，产出 spec 文档 — **你确认**
3. **规划**：claw 将 spec 拆解为具体任务（contracts）— **你确认**
4. **实现**：claw 逐个执行任务（接口 → 测试 → 代码 → review）— **你确认**
5. **发布**：claw 审计所有变更，合并分支，提交版本 — **你确认**

每次迭代循环 2→5。说 `use project-pilot` 开始，claw 自动检测当前阶段，从断点继续。

### Bugfix 模式

遇到 bug 时可以跳过设计阶段，直接进入规划→实现→发布的快速路径。

---

## 架构概览

```
L0: Main Agent (SKILL.md)          ← 路由 + 状态机
    ├── L1: Init Agent             ← 项目初始化
    ├── L1: Design Agent           ← 与人类讨论需求，产出 spec
    │       └── L2: Review Worker
    ├── L1: Plan Agent             ← spec → 合同
    │       └── L2: Review Worker
    ├── L1: Implement Agent        ← 执行合同
    │       ├── L2: Interface Worker
    │       ├── L2: Test Worker
    │       ├── L2: Coding Worker
    │       └── L2: Review Worker
    └── L1: CI/CD Agent            ← 审计 + 发布
            └── L2: Review Worker
```

每个 agent 有独立的工作空间，位于 `agent-workspaces/`。设计决策和技术细节见 [ARCHITECTURE.md](ARCHITECTURE.md)。

---

*面向 AI 辅助开发的调度工程。*
