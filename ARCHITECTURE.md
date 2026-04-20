# Agent Hierarchy v2 — 设计记录

**Date**: 2026-04-16
**Status**: Draft
**Authors**: 企鹅 + claw
**Context**: Discord #deep-work 设计讨论

---

## 核心原则

1. **单一来源**: 每个信息只在一个地方维护
2. **版本号后置**: 设计阶段用日期+名称（`YYYY-MM-DD-{name}`），版本号只在发布时确定
3. **最小仪式**: 不同迭代类型走不同流程（见 D13）
4. **软链接状态**: 状态变化只移动/创建/删除 symlinks，不动原文件

---

## 背景

project-pilot v1 的 agent 架构是扁平的：所有 agent（iteration/contract/interface/test/review/coding）由 SKILL.md 中的 Main Agent 直接调度。问题：

1. **层级不清** — 不知道谁管谁，谁向谁汇报
2. **职责混乱** — iteration agent 既做设计又做规划
3. **缺乏审查** — 产出物之间没有系统性验证

## 决定

### D1: 三层 Agent 架构

```
L0: Main Agent (project-pilot SKILL.md)
    ├── L1: Init Agent          (one-shot, run)
    ├── L1: Design Agent        (thread-bound, session)
    ├── L1: Plan Agent          (orchestrator, run)
    ├── L1: Implement Agent     (orchestrator, session)
    └── L1: CI/CD Agent         (one-shot, run)
        │
        └── L2: Workers (spawned by L1 orchestrators)
            ├── Interface Worker
            ├── Test Worker      (session mode, Phase B 写测试 + Phase D 跑测试)
            ├── Coding Worker
            └── Review Worker
```

**注意**: Test Worker 在 Phase B（写测试 RED）和 Phase D（验证 GREEN）复用同一个 session，不是两个独立 worker。Contract Worker 已合并到 Plan Agent。

**Rationale**: 清晰的指挥链。L0 对人类负责，L1 管理各自阶段，L2 执行具体任务。

### D2: Review Worker — 统一质量检查员

Review Worker 是一个多 skill 的 worker，根据 task 加载不同 skill：

| Skill | Source → Target | 阶段 |
|-------|----------------|------|
| `review-specs` | N/A → specs | Design 产出后 |
| `review-contracts` | specs → contracts | Plan 产出后 |
| `review-interface` | contract → interface docs | Implement Phase A 后 |
| `review-tests` | contract → tests | Implement Phase B 后 |
| `review-code` | contract+tests → code | Implement Phase C 后 |
| `review-audit` | all contracts → codebase | CI/CD 阶段 |

**Rationale**: 一个 worker 六个 skill，比六个独立 review agent 更简洁，核心框架一致。

### D3: 缺陷分类体系

#### 常规 Review（有上游 source）

| 类型 | 定义 |
|------|------|
| **MISS** | Source 明确有，output 漏了 |
| **EXTRA** | Source 没有，output 自己加了 |
| **ERROR** | Output 与 source 矛盾 |

#### Spec Review（无上游 source）

| 类型 | 定义 |
|------|------|
| **INCOMPLETE** | 必填 section 缺失或太模糊 |
| **AMBIGUOUS** | 需求可以有多种解读 |
| **INCONSISTENT** | spec 内部自相矛盾 |

**Rationale**: Spec 没有上游文档可对照，不能用 MISS/EXTRA/ERROR。用专门的分类更准确。

### D4: Review 问题处理 — 谁改？

**核心原则：改下游产出物 → auto-fix；需要改上游源 → escalate to human。**

Review Report 分两个 section：

- **Auto-fixable** — source 明确，fix 方向确定 → orchestrator 重新 spawn 原 worker 附带 review feedback
- **Needs Human** — source 本身可能有问题，或者判断模糊 → 暂停，上报人类

处理流程：
```
Review FAIL
  → Needs Human 非空？→ 上报人类，等待决策
  → 仅 Auto-fixable → 重新 spawn 原 worker + review feedback
  → 再次 review
  → Max 2 轮 fix-review cycle，之后 escalate
```

**Rationale**: Worker 永远不改自己不拥有的文件。避免 agent 自行做设计决策。

### D5: 不发明新 DSL，沿用现有 Phase 格式

Contract 模板已有 Phase A→B→C 结构。不引入 `@step/@worker/@depends` 语法，扩展为：

```
Phase A: Interface Definition ⛔ GATE A
Phase B: Test Development ⛔ GATE B
Phase C: Implementation ⛔ GATE C
Phase D: Test Execution ⛔ GATE D    ← 新增
Phase E: Code Review ⛔ GATE E       ← 新增
```

Implement Agent 解析 markdown phase gates 来驱动 worker spawning。

**Rationale**: 减少认知负担，保持模板可读性，避免"给工具链写工具链"。

### D6: Naming Conventions 分发

每个 worker 只拿到自己需要的命名规范子集：

| Worker | 内容 |
|--------|------|
| Contract Worker | contract 命名 + git 规范 |
| Interface Worker | 代码 + API 命名 |
| Test Worker | 测试文件命名 |
| Coding Worker | 代码 + 存储 + commit 格式 |
| Review Worker | 全量（需对照验证所有命名） |

**Rationale**: 减少 worker context 大小，同时 review worker 保留全量用于检查。允许重叠。

**当前状态**: 散落在各 worker references 中。规模不大，更新时改 plan 的主份后 git diff + grep 同步即可。暂不集中。

### D7: Interface 文档与 Contract 的关系

接口文档是**长期活文档**，contract 是**短期任务单**。

- 接口文档通过 `History` 表记录哪些 contract 修改过它
- Contract 通过 `Boundary.touches` 声明会修改哪些接口文档
- **双向可达，互不依赖**

```markdown
## History
| Date | Change | Contract |
|------|--------|----------|
| 2026-04-16 | Initial creation | C-1.5.0-001-scanner |
```

**Rationale**: 接口文档生命周期远长于 contract，不应把 contract 做主键。

### D8: CI/CD 不需要额外 Review

CI/CD Agent 的工作**本身就是审计**。它调用 `review-worker` 的 `review-audit` skill 做全局检查。在审计者之上再加审计是冗余的。最终产出（git commit + tag）有人类确认兜底。

---

## Agent Workspace 结构

```
agent-workspaces/
├── project-pilot-init/             ← L1: one-shot, 项目初始化
│   ├── AGENTS.md
│   └── references/
│       ├── project-agent-template.md
│       ├── architecture-scaffold.md
│       └── project-types/
├── project-pilot-design/           ← L1: thread-bound, 产出 specs
│   ├── AGENTS.md
│   └── skills/write-specs/SKILL.md
├── project-pilot-plan/             ← L1: orchestrator, specs→contracts
│   ├── AGENTS.md
│   ├── TOOLS.md
│   └── references/
│       ├── contract.md
│       └── mini-contract.md
├── project-pilot-implement/        ← L1: orchestrator, 执行 contract phases
│   └── AGENTS.md
├── project-pilot-cicd/             ← L1: one-shot, 审计+发布
│   └── AGENTS.md
├── project-pilot-interface-worker/ ← L2: 写接口文档
│   ├── AGENTS.md
│   └── references/
│       ├── interface-contract.md
│       ├── interface-docs.md
│       └── naming-conventions.md
├── project-pilot-test-worker/      ← L2: 写测试 + 跑测试 (session mode)
│   ├── AGENTS.md
│   └── references/
│       ├── test-verification.md
│       └── naming-conventions.md
├── project-pilot-coding-worker/    ← L2: 写实现
│   ├── AGENTS.md
│   └── references/naming-conventions.md
└── project-pilot-review-worker/    ← L2: 质量检查（6 skills）
    ├── AGENTS.md
    ├── references/
    │   ├── naming-conventions.md   (全量)
    │   └── rules-reference.md
    └── skills/
        ├── review-specs/SKILL.md
        ├── review-contracts/SKILL.md
        ├── review-interface/SKILL.md
        ├── review-tests/SKILL.md
        ├── review-code/SKILL.md
        └── review-audit/SKILL.md
```

---

### D9: PROJECT.AGENT.md — 项目级上下文文件

目标项目根目录放 `PROJECT.AGENT.md`，包含项目 conventions、技术栈、结构信息。

- 类似 `CLAUDE.md`（Claude Code）、`AGENTS.md`（OpenClaw），但属于 project-pilot 管理
- 所有 worker spawn 到项目目录时自动读到
- Plan Agent 不负责生成——由专门的 **Init Worker** 在首次初始化时创建

**Rationale**: 项目约定属于项目本身，不应散落在各 worker 的 references 里。Worker 只需读项目的 `PROJECT.AGENT.md`，不用内嵌 conventions。

### D10: Init Worker — 项目初始化

新增 `project-pilot-init` worker，由 SKILL.md（L0）直接 spawn：

```
用户触发 project-pilot
  ↓
SKILL.md 检查：有 PROJECT.AGENT.md 吗？
  ├─ 没有 → spawn init worker → 初始化 → 人确认
  └─ 有   → spawn Plan Agent → 正常迭代
```

职责：
1. 分析已有代码（检测语言、框架、conventions）；空项目则询问
2. 创建目录结构（contracts/、specs/、references/interfaces/）
3. 生成 `PROJECT.AGENT.md`
4. 报告结果，等人确认

**Rationale**: 初始化是一次性的，不应让 Plan Agent 每次迭代都检查。L0 入口判断，Init Worker 执行。

**当前状态**: ✅ 已实现。`agent-workspaces/project-pilot-init/AGENTS.md` + references。

---

### D11: Agent Workspace 重命名

所有 agent-workspaces 目录统一加 `project-pilot-` 前缀（2026-04-16 已执行）：

**L1 Agents:** init → project-pilot-init, plan → project-pilot-plan, design → project-pilot-design, implement → project-pilot-implement, cicd → project-pilot-cicd

**L2 Workers:** interface-worker → project-pilot-interface-worker, test-worker → project-pilot-test-worker, coding-worker → project-pilot-coding-worker, review-worker → project-pilot-review-worker

已删除旧的重复目录（project-pilot-contract, project-pilot-implementation 等）、contract-worker（naming-conventions 已移到 plan/references/）和 test-execution-worker（测试执行由 Test Worker session 复用）。

---

### D12: 项目目录结构 — docs/ + workspace/ 设计

**来源**: NOTE.md v3.0 (2026-04-09) + 2026-04-16 讨论

项目文件分两层：**永久存储 (`docs/`)** 和 **工作态 (`workspace/`)**。

#### docs/ — 永久存储

实际文件在这里，不删除，Git 历史即归档。

```
docs/
├── roadmap.md              # 项目级，Checkbox 列表，持续更新
├── architecture.md         # 项目级，系统架构，持续更新
├── specs/                  # Feature 级，YYYY-MM-DD-{name}.md
├── contracts/              # Task 级
│   ├── meta-{iteration}.md # 迭代索引（列出所有 contracts）
│   ├── feature/            # Minor 迭代合同
│   └── fix/                # Patch 修复合同
└── interfaces/             # Module 级，随 contract 更新
```

#### workspace/ — 工作态（全是 symlinks）

```
workspace/
├── specs/               # Symlinks → ../docs/specs/*.spec.md (one per spec)
├── meta.md ─────────────→ ../docs/contracts/meta-{iteration}.md
└── contracts/
    ├── open/               # 待开始（symlinks → docs/contracts/）
    └── in_progress/        # 进行中（全局唯一！）
```

#### 状态流转

```
Design Agent 写 spec → docs/specs/
    ↓ 创建 symlinks → workspace/specs/
Plan Agent 写 meta → docs/contracts/meta-{iteration}.md
    ↓ 创建 symlink workspace/meta.md
Plan Agent 写 contracts → docs/contracts/{feature,fix}/
    ↓ 创建 symlinks → workspace/contracts/open/
    ↓
L0 (Main Agent) 选择 contract，mv symlink: open/ → in_progress/
    ↓
Implement Agent 执行 Phase A→D
    ↓
完成：删除 symlink（rm workspace/contracts/in_progress/{name}）
    ↓
L0 检查 open/ → 还有？→ 重复；没有？→ CI/CD
    ↓
CI/CD Agent：审计、发布、清空 workspace/specs/ + 删除 workspace/meta.md → 回到 Idle
```

#### 文件追踪链（Markdown 相对链接）

所有关联通过 markdown 相对链接实现，不需要额外机制：

- **Meta → Spec**: `[spec-name](../specs/xxx.spec.md)`
- **Meta → Contract**: `[contract-name](./feature/xxx.md)`
- **Contract → Meta**: `[meta-name](../meta-xxx.md)`
- **Contract → Spec**: `[spec-name](../../specs/xxx.spec.md)`

#### Spec 命名约定

使用 `YYYY-MM-DD-{feature-name}.md` 格式，如 `2026-04-09-auth.md`。
版本号只在 CHANGELOG 和 git tag 中出现。

#### Roadmap 格式

```markdown
## Current

- [x] Auth module (spec: 2026-04-09-auth.md)
- [ ] Cache layer (spec: 2026-04-12-cache.md)
- [ ] API v2
```

#### 各角色职责

| 角色 | 读 | 写 |
|------|-----|-----|
| Init Agent (L1) | — | 创建整个 docs/ + workspace/ 骨架 |
| Design Agent (L1) | docs/roadmap.md, docs/architecture.md | docs/specs/, docs/architecture.md, workspace/specs/ (symlinks) |
| Plan Agent (L1) | docs/specs/, workspace/specs/ | docs/contracts/meta-*.md, docs/contracts/{feature,fix}/, workspace/meta.md (symlink), workspace/contracts/open/ (symlinks) |
| L0 Main Agent | workspace/contracts/open/, in_progress/ | mv symlink open/ → in_progress/ |
| Implement Agent (L1) | workspace/contracts/in_progress/ (symlink) | 代码, 完成后删 symlink |
| CI/CD Agent (L1) | 全部, workspace/meta.md | docs/roadmap.md (勾选), CHANGELOG.md, 清空 workspace/specs/ + 删 workspace/meta.md |
| Interface Worker (L2) | workspace/contracts/in_progress/ | docs/interfaces/ |
| Test Worker (L2) | workspace/contracts/in_progress/, docs/interfaces/ | test files |
| Coding Worker (L2) | workspace/contracts/in_progress/, docs/interfaces/, tests | src files |
| Review Worker (L2) | 全部 | review 结果（不写文件） |

**Rationale**: 状态和存储分离。`docs/` 是真理源，`workspace/` 是工作视图。归档不需要移动文件，Git 历史已足够。

---

### D13: 迭代类型与流程

**来源**: NOTE.md v3.0 (2026-04-09)

| 类型 | 对应层级 | Spec | 流程 | Contract 分类 |
|------|---------|------|------|--------------|
| **Minor** | 完整设计 | 单 Spec | Design→Plan→Implement→CI/CD | `feature/` |
| **Patch** | 快速修复 | 无 | Plan(bugfix)→Implement→CI/CD | `fix/` |

**Rationale**: 不同规模的工作走不同仪式。Patch 不需要 spec 和完整设计流程。

---

### D16: 分支管理与版本控制

**来源**: 2026-04-17 讨论

#### 分支模型

```
main                        # 稳定分支，始终保持 Release 终态
iteration/v{version}        # 迭代分支，Plan 阶段从 main 创建
```

**main 分支原则**: 始终保持 Release 终态。不保留任何“进行中”的 Contract 状态。

#### 分支生命周期

| 时机 | 操作 | 负责人 |
|------|------|--------|
| Plan Phase 1 开始 | `git checkout -b iteration/v{version}` from main | Plan Agent |
| 整个迭代过程 | 所有 commit 在 iteration 分支上 | Plan/Implement Agent |
| Release | `git merge iteration/v{version}` into main + `git tag v{version}` on main | CI/CD Agent |

#### Commit 规范

| 时机 | Commit Message | 示例 |
|------|----------------|------|
| Meta 进入 in_progress | `plan: meta for {iteration-name}` | `plan: meta for auth-module` |
| 子合约确认 | `plan: contracts for {iteration-name}` | `plan: contracts for auth-module` |
| 设计产出 | `design: {feature-name}` | `design: auth-module` |
| Contract 实现完成 | `impl: {contract-name}` | `impl: user-login` |
| 审计修复 | `fix: audit feedback - {description}` | `fix: audit feedback - missing validation` |
| 发布 | `release: v{version}` | `release: v1.3.0` |

所有 commit 使用 `--author="Openclaw <claw@openclaw.local>"`。

#### 版本号规则 (SemVer)

| 变更类型 | Bump | 示例 |
|----------|------|------|
| Breaking change | MAJOR | 1.0.0 → 2.0.0 |
| New feature (Minor 迭代) | MINOR | 1.2.0 → 1.3.0 |
| Bug fix (Patch 迭代) | PATCH | 1.2.3 → 1.2.4 |

**Rationale**: 简单的双分支模型，避免 Git Flow 的复杂性。iteration 分支是唯一的工作分支，完成后合并回 main。单人 + claw 协作不需要更复杂的分支策略。

---

### D14: L0 状态机与合同选择

**来源**: 2026-04-16 数据流推演

L0 (Main Agent) 负责状态判断和合同选择。状态纯籹从文件系统推断：

| # | 条件 | 阶段 | 动作 |
|---|-----------|-------|--------|
| 1 | 无 `PROJECT.AGENT.md` | Init | Spawn init |
| 2 | `workspace/specs/` 空 | Idle | 等待 Design |
| 3 | `workspace/specs/` 有 symlinks，无 `workspace/meta.md` | Plan (meta) | Spawn plan |
| 4 | 有 meta，open/ 空 | Plan (contracts) | Spawn plan Phase 2 |
| 5 | in_progress/ 有 symlink | Implementing | 不操作，Implement 运行中 |
| 6 | open/ 有 symlinks，in_progress/ 空 | Ready | mv symlink open/→in_progress/，spawn implement |
| 7 | `workspace/specs/` 有 symlinks，open/ 和 in_progress/ 都空 | Done | Spawn cicd |

CI/CD 完成后清空 `workspace/specs/` + 删 `workspace/meta.md` → 回到 #2 Idle。

**Rationale**: 消除了“未开始”与“全部完成”的歧义。不需要额外状态文件或数据库。

---

### D15: Markdown 链接追踪链

**来源**: 2026-04-17 讨论

所有文档关联通过 markdown 相对链接实现：

- Meta 合同用 markdown 链接引用 source spec 和每个 contract 文件
- 每个 contract 文件反向引用 meta 和 source spec
- Plan Agent Phase 1 确定文件名，Phase 2 必须使用相同名称
- CI/CD 审计通过遍历 meta 的 markdown 链接找到所有合同

**Rationale**: Git 友好，编辑器可点击，agent 可解析。零额外机制。

---

## 待完成

- [x] Init Worker AGENTS.md（2026-04-16 完成）
- [x] L2 Worker AGENTS.md（全部完成）
- [x] agent-hierarchy-v2.md 文件结构图更新（反映重命名）
- [x] D12 路径同步：所有 agent AGENTS.md 更新为 docs/ + workspace/ 路径
- [x] SKILL.md 更新（Main Agent 入口，7 步状态机 + L0 职责）
- [x] openclaw.json agent 注册
- [x] Meta contract 模板 + markdown 链接追踪
- [x] Contract 模板加反向引用
- [x] CI/CD Agent 读 meta + 清理 workspace
- [ ] review-worker references 清理（naming-conventions.md 模板化，rules-reference.md 整合或删除）

---

## Open Questions

| Question | Status |
|----------|--------|
| 旧 project-init.md 内容 | ✅ 已从 git history 恢复，内容融入 init worker |
| review-worker/references/rules-reference.md 归属 | 内容属于主 SKILL.md 层级，待整合 |
| naming-conventions 模板是否放 init worker references | 不放。conventions 属于 PROJECT.AGENT.md，init worker 检测后生成 |
