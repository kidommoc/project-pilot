# Interface Documentation Guide

**Interface docs = Single Source of Truth for module behavior**

---

## When to Update

**MUST update** when:
- Modifying function signatures (parameters, return types)
- Changing semantic behavior
- Adding/removing callers or dependencies
- Introducing new invariants

**DO NOT update**:
- Internal implementation details
- Variable names (unless public API)

---

## Structure

```markdown
# Module: {module_name}

## Overview
{1-2 sentences}

## Functions

### `function_name(param: type) -> return_type`

**Purpose**: {one sentence}

**Parameters**:
- `param` (type): constraint/expectation

**Returns**: {description + edge cases}

**Invariants**:
- Semantic constraints (e.g., "idempotent")
- Pre-conditions (caller must ensure)
- Post-conditions (guaranteed)

**Called By**:
- `module.py:func()`

**Depends On**:
- `module.py:func()`

**History**:
- YYYY-MM-DD: Change description (Contract #123)
```

---

## Location

```
references/interfaces/
├── {module-name}.md
└── ...
```

---

## Dependency Graph (Auto-Generated)

The project maintains two auto-generated dependency graphs for impact analysis.

### Source Code Dependencies

```bash
# Extract dependencies from source code
python scripts/extract-dependencies.py --src . --output .project-graph.json
```

**Query**:
```bash
# Who calls X?
python scripts/query-deps.py --graph .project-graph.json --calls module_name

# What does X depend on?
python scripts/query-deps.py --graph .project-graph.json --depends module_name
```

### Documentation Dependencies

```bash
# Extract dependencies from Markdown files
python scripts/extract-doc-deps.py --src . --output .doc-graph.json
```

**Query**:
```bash
# What files are impacted by changes to X?
python scripts/query-doc-deps.py --graph .doc-graph.json --impact references/project-init.md

# What does X reference?
python scripts/query-doc-deps.py --graph .doc-graph.json --refs SKILL.md

# Show orphaned documents
python scripts/query-doc-deps.py --graph .doc-graph.json --orphaned

# Show highly referenced docs
python scripts/query-doc-deps.py --graph .doc-graph.json --popular
```

### When to Use

| Scenario | Tool |
|----------|------|
| Modifying code interfaces | `extract-dependencies.py` |
| Modifying documentation | `extract-doc-deps.py` |
| Contract Impact Analysis | Both (if both code and docs changed) |
| Phase Completion | Both (consistency check) |

### When to Regenerate

- After adding new modules or documents
- After changing structure or references
- Before closing a Contract (impact analysis)

---

## Interface Contract in Mini-Contract

When modifying interfaces, Mini-Contract MUST include:

```markdown
## Interface Contract

**Modified Interfaces**:
- `file.py:func()` → change description

**Callers**:
- List modules

**Invariants**:
- Semantic constraints

**Interface Docs Updated**:
- [ ] `references/interfaces/module.md`
```

---

## Quality Checklist

Before closing Contract:

- [ ] Interface signature updated
- [ ] "Called By" section updated
- [ ] "Depends On" section updated
- [ ] Invariants documented
- [ ] History entry added

---

## Example

```markdown
# Module: MCP Server

### `get_tenant_paths(tenant_id: str) -> dict`

**Purpose**: Returns file paths for tenant data storage.

**Returns**:
```python
{
  "graph": "{STORAGE_ROOT}/{tenant_id}/logic_nodes.jsonl",
  "emotion": "{STORAGE_ROOT}/{tenant_id}/emotion_nodes.jsonl",
  "obsidian": "{STORAGE_ROOT}/{tenant_id}/vault/"
}
```

**Invariants**:
- `STORAGE_ROOT` = `~/.openclaw/memory/data/tenants/`
- Tenant isolation at directory level
- File names do NOT include tenant_id suffix

**History**:
- 2026-03-25: Changed STORAGE_ROOT path (Contract: storage-path-fix)
```

---

**Version**: 1.0.0 (2026-03-26)  
**Related**: [mini-contract.md](../templates/mini-contract.md), [SKILL.md](../SKILL.md)
