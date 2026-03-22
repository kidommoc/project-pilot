# Development Workflow

**Documentation-First**: No implementation without approved spec/ADR.

---

## 🚨 Phase Completion Protocol (MUST-1)

**After each Phase completes, MUST execute the following, then STOP and wait for confirmation:**

### Step 0: Test Verification (Quality Gate)

**Before declaring Phase complete, MUST verify with tests:**

| Phase Type | Required Tests |
|------------|----------------|
| Code development | Unit tests + Functional tests |
| Documentation | Syntax check + Link validation |
| Configuration changes | Validation command + Rollback test |

**Test Pass Criteria**:
- [ ] New features have corresponding tests
- [ ] Edge cases covered
- [ ] Error handling verified
- [ ] Test results documented in completion report

**If tests fail**: ⛔ STOP, fix issues, re-run tests before proceeding.

---

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
  Claw proposes           Claw executes           Claw self-reviews   Claw packages
  Human confirms          Human confirms          Human validates     Human confirms
```

**Claw drives progress. Human confirms or requests changes.**

---

## Phase 1: Specification

**Goal**: Claw drafts spec + decomposes tasks, human confirms or requests changes.

### Steps

1. Human provides high-level goal
2. Claw drafts: spec + ADRs (if needed) + task decomposition + effort estimate
3. Claw presents plan to human
4. Human confirms OR requests modifications
5. **Documentation gate passed** → Phase 2

**Claw responsibility**: Propose complete, actionable plan  
**Human role**: Confirm or request changes (not design details)

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

**Goal**: Claw executes per spec, human confirms progress at Phase end.

### Steps

1. Claw creates branch (`feature/{name}`)
2. Claw implements incrementally (small commits)
3. **Claw writes tests alongside code** (test-first or test-during, never test-after)
4. Claw uses subagents for parallel work (docs/tests)
5. Claw updates docs
6. Claw marks spec "Implemented"
7. Claw proceeds to Phase 3 (no human confirmation needed during Phase 2)

### Session Discipline

- Files/session: ≤7
- Tokens/response: ≤1500
- End of session: `/new` or continue

📖 **Full guide**: [guides/session-tasks.md](guides/session-tasks.md)

### Exit Criteria

- [ ] All requirements implemented
- [ ] Tests passing (unit + functional)
- [ ] Code self-reviewed
- [ ] Spec marked "Implemented"

**Claw responsibility**: Execute plan, maintain quality  
**Human role**: Available for questions, confirms at Phase end

---

## Phase 3: Review

**Goal**: Claw self-reviews, human validates and confirms.

### Steps

1. Claw performs self-review (checklist below)
2. Claw presents results to human: test results, changes summary, known issues
3. Human inspects (spot/full/delegated — human chooses depth)
4. Claw addresses feedback (if any)
5. Human confirms

### Self-Review Checklist

- [ ] Tests pass
- [ ] No lint errors
- [ ] Docs updated
- [ ] ADRs created (if applicable)
- [ ] Naming conventions followed

### Exit Criteria

- [ ] Human confirmation obtained
- [ ] Feedback addressed (if any)

**Claw responsibility**: Self-review thoroughly, present clearly  
**Human role**: Validate, confirm, or request changes

---

## Phase 4: Release

**Goal**: Claw packages, human confirms release.

### Steps

1. Claw updates CHANGELOG.md
2. Claw bumps version (SemVer)
3. Claw creates git tag (`v{version}`)
4. Claw prepares release notes (if external)
5. Claw presents release summary to human
6. Human confirms release

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
- [ ] Human confirmation obtained

**Claw responsibility**: Package correctly, follow SemVer  
**Human role**: Confirm release or request changes

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
