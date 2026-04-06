# Contract: 修复 project-pilot 自身使用时的 workflow violation

**Opened**: 2026-04-06T23:30 | **Priority**: high

## Goal
修复 project-pilot 在自身使用过程中未遵循其定义的 workflow 的问题。

## Problem Statement
在 new-me 项目开发中，project-pilot 未能严格遵循其自身定义的 workflow-phase2：
- 未从 `contracts/open/` 移动到 `contracts/in_progress/`
- 未执行 Implementation Brief 步骤
- 未按 Phase A→B→C 分离提交
- 未进行 Self-Check (Tester Mode) 步骤
- 未经人工确认就归档合同

## Proposal
1. 为 project-pilot 本身创建一个修复合同，遵循 lightweight-workflow
2. 在 description 中强化必须读取 location 的指令
3. 可选：在 skill matching 机制中增强强制读取验证

## Acceptance Criteria
- [ ] 修复方案实施完毕
- [ ] 项目版本已提升
- [ ] 修复合同已归档

## Implementation Plan
1. 更新 project-pilot skill description 添加强制读取指令
2. 可选：提出其他增强机制

## Boundary
- **Touches**: SKILL.md (description), CHANGELOG.md
- **Does NOT touch**: 其他项目文件、core logic