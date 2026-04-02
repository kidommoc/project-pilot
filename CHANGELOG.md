# Changelog

All notable changes to project-pilot are documented in this file.

---

## v1.8.0 (2026-04-02)

**Contract**: TDD 强制化

**新增**:
- Phase 2 Step 1 (Implementation Brief): 必须包含 Test Strategy（测试类型、关键用例、Mock 处理）
- Phase 2 Step 2: 改为 "Test-First Development"，明确红-绿-重构循环
- Contract item 与测试映射格式: `**Test**: test_file.py::test_case()`
- Phase 2 Step 3 (Self-Check): 新增 TDD 验证检查点（每个 Contract item 都有对应测试）

**变更**:
- workflow.md Phase 2: 全面 TDD 化，测试先行成为必需步骤

---

## v1.7.0 (2026-04-02)

**Contract**: 语义预审查机制

**新增**:
- 语义预审查机制：每个 Contract draft 创建后立即进行自我审查
- 审查维度：意图一致性、需求覆盖度、逻辑自洽性、可执行性、命名一致性
- 预审查报告标准格式（✅已覆盖 / ⚠️可能遗漏 / ❓需要澄清 / 建议）
- 人类决策路径：确认 / 修改 / 忽略

**变更**:
- workflow.md Phase 1: 插入预审查步骤，新增「语义预审查机制」章节

---

## v1.6.0 (2026-04-02)

**Contract**: 分支管理、版本管理与元合约模式

**新增**:
- 000 Meta-Contract 模式：Phase 1 从元合约开始，定义迭代版本号和子合约列表
- 合约命名规范：`C-{MAJOR.MINOR.PATCH}-{No.}-{name}.md`，000 保留给元合约
- 分支模型：`main` 保持 Release 终态，`iteration/v{version}` 为工作分支
- Commit 触发点规范：000/子合约/Feature/Fix/Release 的 commit message 规则
- README.md Current Iteration 章节模板（仅 iteration 分支）

**变更**:
- workflow.md Phase 1: 增加 000 元合约流程、合约命名规范、分支创建时机
- workflow.md Phase 2: 增加 Contract 完成时的 commit 说明
- workflow.md Phase 4: 增加 iteration 分支合并到 main 步骤
- checklists.md Phase 1 Completion: 增加 000 archived 检查
- checklists.md Pre-Release Git: 增加 iteration 分支检查
- naming-conventions.md: `feat` → `feature`，新增 Contract 命名规范章节

---

## v1.5.0 (2026-04-02)

**Contract**: 统一简化 README 中的版本记录和 Phase 追踪

**新增**:
- 分支区分策略：main 仅显示 `Current release`，iteration 分支显示 `Current Iteration`
- Release 前 Cleanup 步骤：移除 Current Iteration，提交 `chore: cleanup iteration tracking`

**变更**:
- SKILL.md MUST-1: 移除 "Update README.md phase status" 步骤
- workflow.md Phase Completion Protocol: 移除 Update README 步骤
- workflow.md Phase 4: 增加 Cleanup README 步骤，明确 CHANGELOG 是唯一版本记录
- lightweight-workflow.md: 更新 Phase 2 README 管理、Release Checklist、README Scope
- README.md: 简化为仅显示 `Current release: v{X.Y.Z}`，移除 Phase/Version 详细章节

---

## v1.4.1 (2026-03-29)

**Contract**: 移除 Contract 模板中的 Status 字段

**变更**:
- 模板文件移除冗余 Status 字段（目录即状态）
- SKILL.md 更新 Contract Structure 示例和 Session Recovery 算法
- workflow.md 移除 "Mark Status as completed" 描述
- 历史合同清理：移除 archived 合同中的 Status 字段

---

## v1.4 (2026-03-28)

**Contract**: README 范围澄清

**新增**:
- README 范围规范：明确 README 与 contracts/ 职责边界
- SKILL.md 添加 "README Scope" 章节

**变更**:
- README 简化为 Contract 标题列表，移除易 drift 的详细检查清单
- Claw 自动维护 README Contract 状态

---

## v1.3 (2026-03-28)

**Contract**: 版本管理

**新增**:
- 版本管理规范：明确 lightweight vs Full workflow 差异
- lightweight 规则：每个 Contract = Minor bump，单一 Commit + Tag

**变更**:
- 版本管理 Contract 完成，规范化 Iteration → Release 流程

---

## v1.2 (2026-03-28)

**Contract**: 升级 lightweight-workflow

**新增**:
- lightweight-workflow v2.0：整合合同状态机 + README 范围 + 简化版版本管理
- 明确 lightweight 与完整 project-pilot workflow 的定位差异

**变更**:
- 目录结构：`active/` → `in_progress/`，`pending-confirmation/` → 移除，`archive/` → `archived/`
- 单一焦点约束：`in_progress/` 只能包含 1 个 contract
- Session Recovery 算法：不依赖对话历史

---

## v1.1.3 (2026-03-27)

**修正**:
- `openclaw-plugin.md` hooks 目录从实际名称改为占位符（`{hook-name-1}`）
- 添加 `configSchema` vs `config.schema.json` 说明

---

## v1.1.2 (2026-03-27)

**新增**:
- 部署标准模板 (`references/templates/DEPLOYMENT.md`, `deploy.sh`)
- OpenClaw 插件项目类型文档更新（目录结构、关键文件、部署流程）

**变更**:
- `openclaw-plugin.md` 目录结构更新为实际项目结构（`plugin/` 替代 `src/`）
- 添加 `openclaw.plugin.json` 配置说明

---

## v1.1.1 (2026-03-27)

**修正**:
- 修复文档链接

---

## v1.1.0 (2026-03-27)

**新增**:
- 合同状态机重构
- 单一焦点约束
- Session Recovery 算法

---

## v1.0.0 (2026-03-26)

**新增**:
- Initial release of project-pilot skill
