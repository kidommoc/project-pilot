# Project Pilot — 人机协同开发指南

**Claw 驱动进度，人类确认或请求变更。**

Current release: v1.10.0

---

## 这是什么？

`project-pilot` 是一个 **OpenClaw 技能**，专为「单人类 + 单 Claw」团队设计的项目管理框架。

它不是传统的项目管理工具，而是一套 **Claw 的行为规范** — 告诉 Claw 如何与你协作开发项目。

---

## 核心理念

### 1. 合同优先 (Contract-First)

**没有合同，不写代码。**

- 任何功能开发前，Claw 会先起草一份「合同」
- 合同包含：目标、验收标准、接口约定、验证方法
- 你确认后，Claw 才开始实现

> [!TIP]
> **合同 = 本次开发动作的原子单位 + 接口约定**
> 
> 不是项目规格说明书，而是：
> 
> - 这次修改的意图、范围、接口、验证方法
> - 关闭条件：验证通过 + 接口文档更新 + 人类确认

### 2. 验收驱动 (Acceptance-Driven)

**成功 = 所有合同条款通过验收，而非「代码写完」。**

- 每个功能独立验证
- 测试通过后，Claw 会请你确认
- 你确认后，该功能才算完成

### 3. 接口文档即真相 (Interface Docs as Truth)

**接口文档永远反映当前代码状态。**

- 修改接口前，Claw 会先读接口文档
- 修改接口后，Claw 会立即更新文档
- 文档与代码同步，不会脱节

### 4. 状态透明 (State Transparency)

**项目状态在文件中，不在对话历史里。**

- 活跃合同 → `contracts/in_progress/`
- 待处理合同 → `contracts/open/`
- 接口文档 → `references/interfaces/`
- 决策记录 → `docs/decisions/`
- 版本历史 → `CHANGELOG.md`

---

## 快速开始

## 什么时候用？

| ✅ 适合 | ❌ 不适合 |
|--------|----------|
| 有监督的开发项目 | 一次性脚本 |
| 需要结构化迭代追踪 | 多团队协调 |
| 需要决策可追溯性 | 无人参与的项目 |

### 启动项目

`使用 project-pilot 开发 XXX` 或 `继续项目 XXX`，Claw 会检查项目结构，然后开始 Phase 1（合同定义）。

### 典型工作流

```
你的目标
  ↓
Phase 1: 合同定义
  Claw 起草合同 → 你确认
  ↓
Phase 2: 实现
  Claw 实现每个功能 → 验证 → 你确认
  ↓
Phase 3: 审计
  Claw 对抗性审计 → 你确认
  ↓
Phase 4: 发布
  打包、打标签、写变更日志
```

### 你只需要做两件事

1. **确认** — Claw 完成每个阶段后，会请你确认是否继续
2. **变更请求** — 如果 Claw 的理解有误，直接告诉它

**Claw 会驱动所有进度，你不需要追问「做到哪了」。**

---

## 关键约束

### ⛔ 合同确认前，Claw 不会写代码

如果 Claw 开始写代码但没有合同，这是 **技能失效**，请立即指出。

### ⛔ 阶段完成后，Claw 会停下来等你确认

如果 Claw 没有等你确认就继续，这是 **违规**，请让它退回。

### ⛔ 接口修改后，Claw 必须更新文档

如果 Claw 改了接口但没更新文档，这是 **违规**，请让它补上。

---

## 质量门槛

### 合同完成前

- [ ] 所有合同项验证通过
- [ ] 接口文档已更新（如有修改）
- [ ] 你已确认

### 发布前

- [ ] 所有测试通过
- [ ] 审计摘要你已确认
- [ ] CHANGELOG 已更新
- [ ] 版本号已提升
- [ ] Git tag 已创建

---

## 项目结构

```
project-pilot/
├── README.md              # 项目概述 — 仅显示 Current release
├── CHANGELOG.md           # 版本历史（唯一来源）
├── contracts/             # 合同（开发动作追踪）
│   ├── draft/             # Claw 起草，待人类确认
│   ├── open/              # 人类已确认，等待开始
│   ├── in_progress/       # 当前焦点（最多 1 份）
│   └── archived/          # 已关闭的合同
├── references/
│   ├── interfaces/        # 接口文档（真相来源）
│   ├── templates/         # 合同/文档模板
│   ├── guides/            # 开发指南
│   └── project-types/     # 项目类型模板
├── docs/
│   └── decisions/         # 架构决策记录 (ADR)
└── scripts/               # 工具脚本（依赖分析等）
```

---

## 相关文档

- [CHANGELOG](CHANGELOG.md) — 版本历史
- [工作流详解](references/workflow.md)
- [检查清单](references/checklists.md)
- [接口文档指南](references/guides/interface-docs.md)
- [测试验证指南](references/guides/test-verification.md)

---

**Claw 驱动进度，你确认或请求变更。就这么简单。**
