# Session & Task Management

**Purpose**: Prevent context overflow, split tasks into session-sized chunks.

---

## Context Budget

| Resource | Limit | Action |
|----------|-------|--------|
| Files/session | ≤7 writes | `/new` |
| Response tokens | ≤1500 | Split reply |
| Tool calls | ≤12 | Use subagent |
| Duration | ≤30 min | Evaluate `/new` |

**Symptoms of overload**: Slow responses, incomplete replies, forgotten context

---

## When to `/new`

- ✅ Phase completed (1→2, 2→3, etc.)
- ✅ Context feels "heavy"
- ✅ Switching unrelated tasks
- ✅ Model degradation signs

**State carryover**: Use project README.md or WARMUP.md

---

## When to Use Subagent

| Use Case | Pattern |
|----------|---------|
| Parallel work | `mode: "run"` for docs/code/tests simultaneously |
| Isolated tasks | `mode: "run", cleanup: "delete"` |
| Persistent work | `mode: "session", thread: true` |
| Research | "Research best practices for X" |

### Example

```typescript
// Main session (coordinator)
sessions_spawn({
  task: "Generate API documentation",
  mode: "run",
  cleanup: "delete",
});
```

---

## Task Decomposition

### Techniques

**1. By Component**
```
Memory Engine
├── Synapse Graph (query, add, mutate)
├── Knowledge Graph (read, write, version)
└── Emotion Graph (query, add)
```

**2. By Phase**
```
Feature
├── Phase 1: Spec (1 session)
├── Phase 2: Implementation (3-5 sessions)
├── Phase 3: Review (1 session)
└── Phase 4: Release (1 session)
```

**3. By CRUD**
```
Entity: Knowledge Asset
├── Create (write_atomic_asset)
├── Read (read_atomic_asset)
├── Update (write + UPDATE mode)
└── Delete (update_asset_status)
```

### Task Sizing

| Size | Duration | Files | Action |
|------|----------|-------|--------|
| Micro | <5 min | 1 | Quick fix |
| Small | 5-15 min | 1-3 | Single function |
| Medium | 15-30 min | 3-5 | Feature component |
| Large | >30 min | >5 | ⚠️ Split |

---

## Session Lifecycle

### Start
1. Read project README.md
2. Check last session log
3. Review task decomposition
4. Collect subagent results (if any)

### During
- Track file writes (count: __/7)
- Monitor response quality
- Use subagents for heavy subtasks

### End
1. Commit: `git commit -m "{type}: {desc}"`
2. Update project board
3. Write session log
4. Kill idle subagents
5. Decide: Continue or `/new`?

---

## Example: Memory Warmup System

```
Session 1: Spec + Design (2 docs)
Session 2: Synapse Query (1-2 files)
Session 3: Knowledge Query (1-2 files)
Session 4: Emotion Query (1 file)
Session 5: Assembly (1-2 files)
Session 6: Tests + Release
```

**Each session**: 3-5 files, 15-30 min, clear output

---

## Task Card Template

```markdown
## Task {N}.{M}: {Name}
**Goal**: {One sentence}
**Files**: `path/to/file.ts`
**Dependencies**: Task X.Y
**Criteria**: [ ] C1, [ ] C2
**Time**: {X} min
**Session**: {N}
```

---

**Version**: 0.4.0 | **Back to**: [SKILL.md](../SKILL.md), [workflow.md](../workflow.md)
