# Contract: Multi-Agent Architecture Refactor (v2)

**Opened**: 2026-04-12T23:50 | **Priority**: high
**Revised**: 2026-04-17T01:22

## Goal

重构 project-pilot 为三层 agent 架构（L0→L1→L2），明确职责边界、统一质量检查、支持 bugfix 短路径，并建立分支管理与版本控制规范。

## Context

v1 架构的问题：层级不清、职责混乱（iteration agent 既做设计又做规划）、缺乏系统性审查、无分支管理。

## Acceptance Criteria

### Agent 架构
- [x] L0 Main Agent (SKILL.md): 状态机路由 + human bridge，不执行开发工作
- [x] L1 Init Agent: 项目初始化，生成 PROJECT.AGENT.md
- [x] L1 Design Agent: thread-bound session，与人类讨论需求，产出 specs
- [x] L1 Plan Agent: orchestrator，specs→meta→contracts，支持 bugfix 模式 (Phase 0)
- [x] L1 Implement Agent: orchestrator，执行 contract Phase A→E
- [x] L1 CI/CD Agent: 审计 + 发布，从分支名读版本号
- [x] L2 Interface Worker: 写接口文档
- [x] L2 Test Worker: session mode，Phase B 写测试 + Phase D 验证
- [x] L2 Coding Worker: 写实现
- [x] L2 Review Worker: 统一质量检查员，6 个 skills

### Review 体系
- [x] 缺陷分类: MISS/EXTRA/ERROR (常规) + INCOMPLETE/AMBIGUOUS/INCONSISTENT (spec)
- [x] 修复路由: auto-fixable→重新 spawn + feedback；needs-human→escalate；max 2 轮
- [x] 6 个 review skills: specs/contracts/interface/tests/code/audit

### 项目结构
- [x] docs/ (永久存储) + workspace/ (symlink 工作态) 分离
- [x] 文件追踪链: markdown 相对链接（meta↔spec↔contract）
- [x] 状态流转: symlink 移动驱动（open/→in_progress/→删除）

### 分支管理与版本控制
- [x] 双分支模型: main (稳定) + iteration/v{version} (工作)
- [x] Plan Agent 创建 iteration 分支
- [x] CI/CD Agent merge 回 main + tag
- [x] 版本号 single source of truth: iteration 分支名
- [x] SemVer: Minor→MINOR bump, Bugfix→PATCH bump
- [x] Commit 规范: plan:/design:/impl:/fix:/release: 前缀

### Bugfix 模式
- [x] SKILL.md: Idle 状态识别 bugfix trigger
- [x] Plan Agent Phase 0: 无 spec，直接产 fix-contract
- [x] fix-contract 模板: 轻量级，无 spec 引用，直接从 Phase B 开始

### Contract 模板体系
- [x] fix-contract.md: bug 修复专用，最轻
- [x] mini-contract.md: 小功能，中等
- [x] contract.md (full): 复杂功能，最重
- [x] meta-contract.md: 迭代索引

### 文档
- [x] README.md: 重写（intro + how it works + architecture overview）
- [x] ARCHITECTURE.md: 完整设计记录 (D1-D16)
- [x] openclaw.json: 全部 agent 注册

### 清理
- [x] Agent workspace 统一 `project-pilot-` 前缀
- [x] 删除旧重复目录（contract-worker, test-execution-worker 等）
- [x] 命名规范分发到各 worker references

### 设计决策（否决项）
- ~~Contract Schema: 声明式 @step/@worker/@depends DSL~~ → **D5 否决**: 沿用 Phase A→E markdown 格式
- ~~ID 追踪系统: @contract @step @depends 标记~~ → **D5 否决**: markdown 链接已足够

## Boundary

- **Touches**: SKILL.md, README.md, ARCHITECTURE.md, openclaw.json, agent-workspaces/\*/AGENTS.md, agent-workspaces/\*/references/
- **Does NOT touch**: demos/, contracts/archived/

## Close Contract

- [ ] All acceptance criteria pass
- [ ] Human confirmed
- [ ] Archive to contracts/archived/
