# Project Pilot — 人机协同开发指南

**Claw 驱动进度，人类确认或请求变更。**

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

- 活跃合同 → `contracts/active/`
- 接口文档 → `references/interfaces/`
- 决策记录 → `docs/decisions/`
- 阶段状态 → `README.md`（本文件）

---

## 如何使用

### 启动项目

```
使用 project-pilot 开发 XXX
```

或

```
继续项目 XXX
```

Claw 会检查项目结构，然后开始 Phase 1（合同定义）。

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

Claw 会驱动所有进度，你不需要追问「做到哪了」。

---

## 关键约束

### ⛔ 合同确认前，Claw 不会写代码

如果 Claw 开始写代码但没有合同，这是 **技能失效**，请立即指出。

### ⛔ 阶段完成后，Claw 会停下来等你确认

如果 Claw 没有等你确认就继续，这是 **违规**，请让它退回。

### ⛔ 接口修改后，Claw 必须更新文档

如果 Claw 改了接口但没更新文档，这是 **违规**，请让它补上。

---

## 项目结构

```
your-project/
├── README.md              # 本文件 — 人类可读的项目状态
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

## 合同是什么？

**合同 = 本次开发动作的原子单位 + 接口约定**

不是项目规格说明书，而是：

- 这次修改的意图、范围、接口、验证方法
- 关闭条件：验证通过 + 接口文档更新 + 人类确认
- 关闭后：移动到 `contracts/archived/`，接口文档保留更新

### 合同类型

| 类型 | 使用场景 |
|------|----------|
| **Mini-Contract** | ≤ 8 个合同项，单模块，无复杂依赖（默认） |
| **Full Contract** | > 8 个合同项，多模块，架构影响，复杂依赖 |

### 合同生命周期

```
起草 → 你确认 → 实现中 → 验证通过 → 待你确认 → 已关闭
```

---

## 阶段定义

| 阶段 | 内容 | 你的操作 |
|------|------|----------|
| **Phase 1** | 合同定义 | 确认合同 |
| **Phase 2** | 实现 | 确认每个合同完成 |
| **Phase 3** | 审计 | 确认审计结果 |
| **Phase 4** | 发布 | 确认发布 |

---

## 常见场景

### 场景 1：启动新功能

```
你：添加用户认证功能
Claw：起草 Mini-Contract → 请你确认
你：确认后
Claw：实现 → 验证 → 请你确认完成
```

### 场景 2：继续上次的工作

```
你：继续项目
Claw：检查 contracts/active/ → 找到进行中的合同 → 继续
```

### 场景 3：查看项目状态

```
你：现在做到哪了？
Claw：读取 README.md + contracts/active/ → 汇报当前阶段和进度
```

### 场景 4：修改接口

```
你：修改 XXX 函数的签名
Claw：读取接口文档 → 修改代码 → 更新接口文档 → 验证 → 请你确认
```

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

## 什么时候用？

✅ **适合**：
- 有监督的开发项目
- 需要结构化迭代追踪
- 需要决策可追溯性

❌ **不适合**：
- 一次性脚本
- 多团队协调
- 无人参与的项目

---

## Current Phase

**Phase**: Released (v1.4.1)

### Completed Contracts (v1.4 Iteration)
- [x] 合同状态机重构
- [x] 升级 lightweight-workflow
- [x] 版本管理
- [x] README 范围澄清

### Completed Contracts (v1.4.1 Iteration)
- [x] 移除 Contract 模板中的 Status 字段

### Next Iteration (Draft)
- [ ] _Awaiting human direction_

---

## Version

**Current**: 1.4.1 (2026-03-29)

**Changelog**: See `CHANGELOG.md`

### v1.4 (2026-03-28)

**新增**:
- README 范围规范：明确 README 与 contracts/ 职责边界
- SKILL.md 添加 "README Scope" 章节

**变更**:
- README 简化为 Contract 标题列表，移除易 drift 的详细检查清单
- Claw 自动维护 README Contract 状态

---

### v1.4.1 (2026-03-29)

**变更**:
- 模板文件移除冗余 Status 字段（目录即状态）
- SKILL.md 更新 Contract Structure 示例和 Session Recovery 算法
- workflow.md 移除 "Mark Status as completed" 描述
- 历史合同清理：移除 archived 合同中的 Status 字段

---

### v1.3 (2026-03-28)

**新增**:
- 版本管理规范：明确 lightweight vs Full workflow 差异
- lightweight 规则：每个 Contract = Minor bump，单一 Commit + Tag

**变更**:
- 版本管理 Contract 完成，规范化 Iteration → Release 流程

---

### v1.2 (2026-03-28)

**新增**:
- lightweight-workflow v2.0：整合合同状态机 + README 范围 + 简化版版本管理
- 明确 lightweight 与完整 project-pilot workflow 的定位差异

**变更**:
- 目录结构：`active/` → `in_progress/`，`pending-confirmation/` → 移除，`archive/` → `archived/`
- 单一焦点约束：`in_progress/` 只能包含 1 个 contract
- Session Recovery 算法：不依赖对话历史

### v1.1.2 (2026-03-27)

**新增**:
- 部署标准模板 (`references/templates/DEPLOYMENT.md`, `deploy.sh`)
- OpenClaw 插件项目类型文档更新（目录结构、关键文件、部署流程）

**变更**:
- `openclaw-plugin.md` 目录结构更新为实际项目结构（`plugin/` 替代 `src/`）
- 添加 `openclaw.plugin.json` 配置说明

---

## 相关文档

- [工作流详解](references/workflow.md)
- [检查清单](references/checklists.md)
- [接口文档指南](references/guides/interface-docs.md)
- [测试验证指南](references/guides/test-verification.md)
- [会话任务分解](references/guides/session-tasks.md)

---

**Claw 驱动进度，你确认或请求变更。就这么简单。**
