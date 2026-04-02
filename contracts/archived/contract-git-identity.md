# Contract: 规范 Claw 的 Git 提交身份

**Opened**: 2026-04-02T17:20

**Priority**: medium
**Type**: Meta (流程规范)

---

## Goal

明确区分人类提交与 Claw 提交的 Git 身份，确保提交历史可追溯。

## Context

当前 Claw 使用系统默认的 Git 配置（user.name/user.email）进行提交，这可能导致：
- 如果用户覆盖全局配置，Claw 提交会显示为用户身份
- 无法从提交历史中区分哪些是 Claw 自动提交，哪些是人类手动提交

## Proposal

### Claw Git 身份规范

| 属性 | 值 |
|------|-----|
| user.name | `Openclaw` |
| user.email | `claw@openclaw.local` |

### 实现方式

Claw 在执行 `git commit` 时，使用环境变量覆盖全局配置：

```bash
GIT_AUTHOR_NAME="Openclaw" GIT_AUTHOR_EMAIL="claw@openclaw.local" \
git commit -m "{message}"
```

### 影响范围

所有由 Claw 执行的 Git 提交：
- lightweight-workflow: Phase 2 的 release commit
- 完整 workflow: Phase 2 的 feature commit, Phase 4 的 release commit 等

## Boundary

- **Touches**:
  - `contracts/lightweight-workflow.md`
  - `references/workflow.md`
- **Does NOT touch**:
  - 用户的 Git 配置（`~/.gitconfig`）
  - 项目级 Git 配置（`.git/config`）
- **Depends on**: 无

## Acceptance Criteria

- [ ] lightweight-workflow.md 更新：Phase 2 的 git commit 命令使用环境变量指定身份
- [ ] workflow.md 更新：所有 git commit 示例使用环境变量指定身份
- [ ] 验证：文档中所有 Claw 执行的 commit 命令都包含身份覆盖

## Tasks

1. 修改 `lightweight-workflow.md`:
   - Phase 2 "Single Git commit" 步骤更新为使用环境变量
2. 修改 `workflow.md`:
   - Phase 2 Step 4 commit 示例更新
   - Phase 4 Steps 4 和 6 commit/tag 示例更新
3. Self-review：检查两个文档中所有 git commit 相关命令

## Notes

**为什么使用 `--author`？**
- 显式、自包含，命令一目了然
- 不污染环境变量
- 与 `git tag` 等其他命令保持独立

**用户提交不受影响**
- 用户在 shell 中手动执行 `git commit` → 使用其 `~/.gitconfig` 配置
- Claw 通过 exec 执行 → 显式覆盖为 Openclaw 身份

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Human confirmed

**Next Session**:
- **Suggested**: Phase 2 Implementation
- **First Task**: 修改 lightweight-workflow.md

**Archive**: Move to `contracts/archived/`.
ontracts/archived/`.
