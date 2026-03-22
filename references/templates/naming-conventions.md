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

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting (no code change)
- `refactor`: Code restructuring (no behavior change)
- `test`: Adding tests
- `chore`: Maintenance tasks

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
- **Code review**: Check naming during Phase 3 review
- **Documentation**: Update this file when new patterns emerge

---

**References**:
- [Google Style Guides](https://google.github.io/styleguide/)
- [PEP 8](https://peps.python.org/pep-0008/) (Python)
- [Airbnb Style Guide](https://github.com/airbnb/javascript) (JavaScript)
