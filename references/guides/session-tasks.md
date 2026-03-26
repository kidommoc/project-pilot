# Task Decomposition

**Purpose**: Split large tasks into manageable, trackable units.

---

## By Component

Decompose by module or subsystem:

```
Memory Engine
├── Synapse Graph (query, add, mutate)
├── Knowledge Graph (read, write, version)
└── Emotion Graph (query, add)
```

**Contract per component** — Each component gets its own Contract or Contract section.

---

## By Phase

Decompose by development phase:

```
Feature
├── Phase 1: Contract (1 session)
├── Phase 2: Implementation (3-5 sessions)
├── Phase 3: Audit (1 session)
└── Phase 4: Release (1 session)
```

**Phase boundaries** — Complete one Phase before starting the next (MUST-1).

---

## By CRUD

Decompose by operation type:

```
Entity: Knowledge Asset
├── Create (write_knowledge_asset)
├── Read (read_knowledge_asset)
├── Update (write + UPDATE mode)
└── Delete (update_knowledge_status)
```

**Interface per operation** — Document each operation in interface docs.

---

## By Dependency Order

Decompose by execution order:

```
1. Define interfaces (no implementation)
2. Implement core logic (depends on interfaces)
3. Implement callers (depends on core)
4. Integration tests (depends on all)
```

**Contract reflects order** — Tasks section shows dependency chain.

---

## Parallelization

**Subagent-eligible tasks**:
- Documentation updates
- Test scaffolding
- Independent modules
- Research tasks

**Pattern**:
```
Main session (coordinator)
├── Subagent 1: Generate docs
├── Subagent 2: Write tests
└── Main: Integration
```

---

**Related**: [workflow.md](../workflow.md), [SKILL.md](../SKILL.md)
