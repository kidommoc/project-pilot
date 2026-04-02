# Naming Conventions

**Project**: {Project Name}  
**Created**: YYYY-MM-DD  
**Last Updated**: YYYY-MM-DD

---

This document tracks project-specific naming conventions. Update as the project evolves.

## Code Naming

### Variables

| Type | Convention | Example |
|------|------------|---------|
| Local variables | `snake_case` | `user_count`, `max_retries` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_BUFFER_SIZE`, `DEFAULT_TIMEOUT` |
| Private variables | `_prefix` | `_internal_cache` |

### Functions

| Type | Convention | Example |
|------|------------|---------|
| Regular functions | `snake_case` (Python) / `camelCase` (JS) | `calculate_total()`, `getUserById()` |
| Private functions | `_prefix` | `_validate_input()` |
| Constructors | `PascalCase` | `UserManager`, `DatabaseConnection` |

### Classes & Types

| Type | Convention | Example |
|------|------------|---------|
| Classes | `PascalCase` | `MemoryEngine`, `PluginManager` |
| Interfaces | `PascalCase` (optionally `I` prefix) | `IConfig`, `PluginInterface` |
| Type aliases | `PascalCase` | `UserId`, `CallbackFn` |

### Modules & Files

| Type | Convention | Example |
|------|------------|---------|
| Python modules | `snake_case.py` | `memory_engine.py`, `vault_inspector.py` |
| JavaScript/TypeScript | `kebab-case.ts` or `camelCase.ts` | `memory-engine.ts`, `vaultInspector.ts` |
| Test files | `{module}.test.{ext}` or `test_{module}.{ext}` | `engine.test.ts`, `test_engine.py` |

---

## API Naming

### Endpoints

| Method | Pattern | Example |
|--------|---------|---------|
| REST | `/api/v{version}/{resource}` | `/api/v1/memory/assets` |
| RPC | `{service}.{method}` | `memory.readAsset`, `vault.writeDraft` |

### Request/Response Fields

| Type | Convention | Example |
|------|------------|---------|
| JSON fields | `snake_case` or `camelCase` | `user_id` / `userId`, `asset_path` / `assetPath` |
| Query parameters | `snake_case` | `?include_metadata=true` |
| Path parameters | `snake_case` in `{braces}` | `/assets/{asset_id}` |

**Consistency rule**: Match the convention of your API framework.

---

## Database & Storage

| Type | Convention | Example |
|------|------------|---------|
| Tables | `snake_case` (plural) | `users`, `memory_assets` |
| Columns | `snake_case` | `created_at`, `user_id` |
| Indexes | `idx_{table}_{column}` | `idx_users_email` |
| Files (data) | `kebab-case.ext` | `synapse-graph.jsonl`, `emotion-graph.jsonl` |

---

## Git & Versioning

| Type | Convention | Example |
|------|------------|---------|
| Branches | `{type}/{description}` | `feature/memory-engine`, `fix/issue-123` |
| Tags | `v{semver}` | `v1.2.0`, `v0.3.0-beta.1` |
| Commit messages | `{type}: {message}` | `feat: add memory engine`, `fix: resolve null pointer` |

### Commit Types

- `feature`: New feature (was `feat`, changed for clarity)
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting (no code change)
- `refactor`: Code restructuring (no behavior change)
- `test`: Adding tests
- `chore`: Maintenance tasks

---

## Contract Naming (project-pilot)

**文件命名**：`C-{MAJOR.MINOR.PATCH}-{No.}-{name}.md`

| 组件 | 含义 | 示例 |
|------|------|------|
| `C` | Contract 前缀 | 固定 |
| `{MAJOR.MINOR.PATCH}` | 迭代版本号 | `1.5.0` |
| `{No.}` | 该迭代内的 Contract 序号，000 保留给元合约 | `000`, `001`, `002` |
| `{name}` | 短横线连接的小写名称 | `branch-management` |

**示例**：
- `C-1.5.0-000-meta.md` — 元合约（规划迭代范围）
- `C-1.5.0-001-branch-version.md` — 子合约 1
- `C-1.5.0-002-semantic-review.md` — 子合约 2

**000 Meta-Contract**：
- 仅用于完整 workflow（A）
- lightweight workflow（B）不使用 000

### Contract Commit Messages

| 时机 | Commit Message |
|------|----------------|
| 000 进入 in_progress | `contract: meta v{version}` |
| Phase 1 子合约确认 | `contract: define {contract-name}` |
| Phase 2 Contract 完成 | `feature: {contract-name}` |
| Phase 3 小问题修复 | `fix: audit feedback - {description}` |
| Phase 4 Release | `release: v{version}` |

---

## Project-Specific Conventions

### Add your project-specific rules here:

```
Example:
- Memory engine nodes: `{type}-{id}` format (e.g., `T-001`, `D-042`)
- Knowledge assets: `{project}/{category}/{slug}.md`
- Emotion nodes: `E_{type}_{subject}` (e.g., `E_pref_claw_voice`)
```

---

## Enforcement

- **Linting**: Configure linter rules where possible
- **Code review**: Check naming during Phase 3 audit
- **Documentation**: Update this file when new patterns emerge

---

**References**:
- [Google Style Guides](https://google.github.io/styleguide/)
- [PEP 8](https://peps.python.org/pep-0008/) (Python)
- [Airbnb Style Guide](https://github.com/airbnb/javascript) (JavaScript)
