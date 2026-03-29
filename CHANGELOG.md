# Changelog

All notable changes to project-pilot are documented in this file.

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
