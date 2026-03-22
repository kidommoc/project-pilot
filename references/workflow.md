# Development Workflow

**Documentation-First**: No implementation without approved spec/ADR.

---

## 🚨 Phase Completion Protocol (MUST-1)

**After each Phase completes, MUST execute the following, then STOP and wait for confirmation:**

### Step 1: Update README.md

```markdown
### Phase N: {phase_name} (✅ Completed - YYYY-MM-DD)
- [x] Task 1
- [x] Task 2

### Phase N+1: {next_phase} (🟡 In Progress / ⏳ Pending)
- [ ] Task 1
```

### Step 2: Write Completion Report

**File**: `docs/notes/YYYY-MM-DD-phaseN-completion.md`

**Template**:
```markdown
# YYYY-MM-DD Phase N Completion Report

**Session**: Date-time range
**Executor**: claw
**Phase**: Phase N - Phase Name

## Task Objectives
{List objectives for this Phase}

## Completed Work
{Detailed list of completed tasks}

## Verification Results
{Command output, test results, etc.}

## Next: Phase N+1
{Next phase tasks}

**Status**: ✅ Phase N completed, waiting confirmation to proceed to Phase N+1
```

### Step 3: Ask User

**Must explicitly ask**:
> "Phase N completed (verification passed). Continue to Phase N+1?"

### Step 4: ⛔ Wait for Confirmation

**Forbidden behaviors**:
- ❌ Execute Phase N+1 code while waiting
- ❌ Assume "continue is default behavior"
- ❌ Skip confirmation step

---

## Phase Overview

```
Phase 1: Specification → Phase 2: Implementation → Phase 3: Review → Phase 4: Release
     ↓                        ↓                        ↓                   ↓
  Human directs           Claw executes           Human approves      Human releases
```

---

## Phase 1: Specification

**Goal**: Define what to build + decompose into session-sized tasks.

### Steps

1. Human provides goal
2. Claw drafts: spec + ADRs (if needed) + task decomposition
3. Human reviews + approves
4. **Documentation gate passed** → Phase 2

### Task Decomposition

Break feature into sessions (1-3 tasks per session):

```markdown
## Implementation Plan
### Session 1: Task 1.1, 1.2
### Session 2: Task 2.1
### Subagents: docs, tests
```

📖 **Techniques**: [guides/session-tasks.md](guides/session-tasks.md)

### Exit Criteria

- [ ] Spec/ADR created
- [ ] Human approval obtained
- [ ] Task decomposition complete
- [ ] Dependencies identified

---

## Phase 2: Implementation

**Goal**: Build per spec, one session = 1-3 tasks.

### Steps

1. Create branch (`feature/{name}`)
2. Implement incrementally (small commits)
3. Use subagents for parallel work (docs/tests)
4. Write tests alongside
5. Update docs
6. Mark spec "Implemented"

### Session Discipline

- Files/session: ≤7
- Tokens/response: ≤1500
- End of session: `/new` or continue

📖 **Full guide**: [guides/session-tasks.md](guides/session-tasks.md)

### Exit Criteria

- [ ] All requirements implemented
- [ ] Tests passing
- [ ] Code self-reviewed
- [ ] Spec marked "Implemented"

---

## Phase 3: Review

**Goal**: Human validates implementation.

### Steps

1. Claw self-review (checklist below)
2. Human inspection (spot/full/delegated)
3. Address feedback (if any)
4. Human approves

### Self-Review Checklist

- [ ] Tests pass
- [ ] No lint errors
- [ ] Docs updated
- [ ] ADRs created (if applicable)
- [ ] Naming conventions followed

### Exit Criteria

- [ ] Human approval obtained
- [ ] Feedback addressed

---

## Phase 4: Release

**Goal**: Package and deliver.

### Steps

1. Update CHANGELOG.md
2. Bump version (SemVer)
3. Create git tag (`v{version}`)
4. Release notes (if external)

### Version Bumping

| Change | Bump | Example |
|--------|------|---------|
| Breaking | MAJOR | 1.0.0 → 2.0.0 |
| Feature | MINOR | 1.2.0 → 1.3.0 |
| Fix | PATCH | 1.2.3 → 1.2.4 |

### Exit Criteria

- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] Git tag created
- [ ] Human approval

---

## Templates

### Spec Structure

```markdown
# {Feature}
**Status**: Draft|Approved|Implemented
**Goal**: One sentence
**Requirements**: FR-1, FR-2...
**Technical Approach**: {description}
**Test Plan**: {tests}
**Acceptance Criteria**: [ ] C1, [ ] C2
```

### Session Log

```markdown
# {Topic}
**Date**: YYYY-MM-DD
**Progress**: Task A ✅, Task B 🟡
**Decisions**: {decision} — {rationale}
**Next**: {task}
```

📖 **Full templates**: [templates/](templates/)

---

**Version**: 0.5.0 | **See also**: [SKILL.md](../SKILL.md), [checklists.md](checklists.md)
