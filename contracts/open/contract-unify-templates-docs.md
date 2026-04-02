# Contract: 统一项目类型模板的 docs 目录结构

**Opened**: 2026-04-02T15:20

**Priority**: low
**Type**: Meta (模板一致性)

---

## Goal

统一各项目类型模板（web-app, cli-tool, python-package, openclaw-plugin）中的 `docs/` 目录定义，消除不一致。

## Context

检查 `references/project-types/*.md` 发现，各模板对 `docs/` 目录的定义存在差异：
- 有的包含 `docs/decisions/`，有的没有
- 有的将 `contracts/` 放在根目录，有的建议放在 `docs/`
- 有的缺少 `docs/interfaces/` 说明

这种不一致导致使用 project-pilot 初始化项目时，目录结构不统一。

## Boundary

- **Touches**: 
  - `references/project-types/web-app.md`
  - `references/project-types/cli-tool.md`
  - `references/project-types/python-package.md`
  - `references/project-types/openclaw-plugin.md`
- **Does NOT touch**: 
  - `project-pilot` 自身目录结构（本项目用 lightweight-workflow，结构不同）
  - 其他 workflow 文件
- **Depends on**: 无

## Proposal

### 统一目录结构

所有项目类型模板使用以下标准结构：

```
project-root/
├── README.md              # 项目概述、Phase 状态
├── CHANGELOG.md           # 版本历史
├── contracts/             # ⚠️ 必须在根目录，不在 docs/ 下
│   ├── draft/
│   ├── open/
│   ├── in_progress/
│   └── archived/
├── docs/
│   ├── decisions/         # ADR 文档
│   └── interfaces/        # 接口文档（如果项目有代码接口）
├── references/            # 参考资料、指南
│   ├── guides/
│   ├── templates/
│   └── ...
└── src/ 或具体代码目录
```

### 关键规范

| 目录 | 位置 | 说明 |
|------|------|------|
| `contracts/` | **根目录** | 固定位置，便于 Claw 快速定位 |
| `docs/decisions/` | docs/ 下 | ADR 文档 |
| `docs/interfaces/` | docs/ 下 | 接口文档（代码项目） |
| `references/` | 根目录 | 指南、模板、checklists |

### 各模板需更新的内容

每个 `project-types/*.md` 的 "Project Structure" 或 "Initialization" 章节：
- 明确列出上述目录结构
- 说明 `contracts/` 为何在根目录
- 说明各子目录用途

## Contract

- [ ] `web-app.md` 目录结构更新为标准结构
- [ ] `cli-tool.md` 目录结构更新为标准结构
- [ ] `python-package.md` 目录结构更新为标准结构
- [ ] `openclaw-plugin.md` 目录结构更新为标准结构
- [ ] 验证：4 个模板定义一致

## Tasks

1. 读取 4 个 project-types/*.md 文件，标记当前目录结构定义
2. 修改 `web-app.md`：更新为标准目录结构
3. 修改 `cli-tool.md`：更新为标准目录结构
4. 修改 `python-package.md`：更新为标准目录结构
5. 修改 `openclaw-plugin.md`：更新为标准目录结构
6. Self-review：对比 4 个文件，确保一致性

## Notes

**为什么 contracts/ 必须在根目录？**
- Claw 需要快速定位 `contracts/in_progress/` 进行 Session Recovery
- 放在 docs/ 下增加路径复杂度，无实际收益

**docs/ 与 references/ 的区别？**
- `docs/`：项目文档（决策、接口）
- `references/`：可复用的参考资料、指南、模板

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Human confirmed

**Next Session**:
- **Suggested**: Phase 2 Implementation
- **First Task**: 读取 4 个 project-types/*.md 文件

**Archive**: Move to `contracts/archived/`.
