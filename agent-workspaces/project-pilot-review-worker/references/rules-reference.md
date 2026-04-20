# Rules Reference

**Purpose**: Distinguish MUST constraints from Decision Rules and provide complete reference.

---

## MUST Constraints (Non-Negotiable)

Violating these = skill failure. Agent must stop and correct immediately.

### MUST-1: Phase Completion Protocol
After each Phase completes:
1. Execute review (Quality Gate) — except Phase D which is handled by Test Worker session
2. Update interface docs (if interfaces changed)
3. **Explicitly ask user**: "Phase N completed. Continue to Phase N+1?"
4. **FORBIDDEN** to execute next phase code before user confirmation

### MUST-2: Activation Check
Do NOT auto-apply project-pilot. Wait for explicit trigger:
- Human says "use project-pilot" → Apply immediately
- Human says "continue project {name}" → Check project structure first
- No trigger → Do NOT apply

### MUST-3: Contract-First Enforcement
**No code before approved Contract.**
- Before new feature → Mini-Contract or full Contract required
- Before architecture changes → Full Contract + ADR required
- No code before Implementation Brief (Phase 2 Step 1) is written

### MUST-4: Interface Docs Enforcement
**Update interface docs when modifying module interfaces.**
- Read interface docs before modifying (understand callers, deps, invariants)
- Update interface docs after modifying (reflect current state)
- Interface docs = Single Source of Truth

### MUST-5: State Transparency
**Project state must always be findable.**
- Contract files (permanent) → `docs/contracts/{feature,fix}/`
- Open Contracts (symlinks) → `workspace/contracts/open/`
- In-Progress Contract (symlink) → `workspace/contracts/in_progress/` (exactly 1)
- Completed → symlink removed, file stays in `docs/contracts/` (Git history is archive)
- Interface docs → `docs/interfaces/`
- Specs → `docs/specs/`
- Phase status → README.md

---

## Decision Rules

These guide agent decisions. Violating may lead to suboptimal choices but not failure.

### Contract Selection
| Condition | Selection |
|-----------|-----------|
| ≤ 8 contract items, single module, no complex deps | **Mini-Contract** (default) |
| > 8 items, multi-module, architectural impact, complex deps | **Full Contract** |

### ADR Trigger
Create ADR when:
- Changes project structure
- Introduces new dependency patterns
- Makes breaking changes to interfaces
- Involves significant architectural decisions

### State Storage
| Type | Location | Lifecycle |
|------|----------|-----------|
| **Temporary Progress** | Contract checkboxes | Contract lifecycle |
| **Permanent State** | Interface docs | Project lifecycle |

### Phase Transition Rules
| From | To | Condition |
|------|-----|-----------|
| P1 | P2 | All Contracts defined and in `open/` |
| P2 | P3 | All Contracts archived + tests passing |
| P3 | P4 | Audit Summary approved by human |
| P4 | Done | Version bumped + git tagged |

### Session Recovery
```
1. Check workspace/specs/
   ├─ Empty → Idle (no active iteration)
   └─ Has symlinks → Continue:
2. Check workspace/meta.md
   ├─ Missing → Plan phase (meta needed)
   └─ Exists → Continue:
3. Check workspace/contracts/in_progress/
   ├─ 1 symlink → Continue implementation
   ├─ 0 symlinks → Check workspace/contracts/open/ → Start next or ask
   └─ >1 symlinks → ERROR: Report to human
4. workspace/contracts/open/ and in_progress/ both empty → CI/CD phase
```

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-03 | Initial separation of MUST vs Decision Rules |
