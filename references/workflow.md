# Development Workflow

Detailed breakdown of each development phase.

## Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Phase 1    │────▶│  Phase 2    │────▶│  Phase 3    │────▶│  Phase 4    │
│ Specification│     │Implementation│     │   Review    │     │   Release   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
   Human               Claw                Human              Human
   directs            executes            approves           releases
       │
       └─── 📋 Documentation Gate: No code without approved spec/ADR
```

## Core Principle: Documentation-First

**Rule**: Implementation cannot begin without approved documentation.

- Spec documents (`docs/specs/`) for feature behavior
- ADRs (`docs/decisions/`) for architecture decisions
- Architecture docs (`docs/architecture/`) for system design
- Exception: hotfixes may document post-facto

This ensures:
- Clarity before investment
- Reduced rework from misunderstandings
- Traceable decision history

---

## Phase 1: Specification

**Goal**: Define what to build before building it.

**Documentation Gate**: Phase 2 cannot start until Phase 1 deliverables are approved.

### Steps

1. **Human provides goal** — High-level description of desired feature
2. **Claw drafts documentation**:
   - Feature spec → `docs/specs/{feature-name}.md`
   - Architecture changes → `docs/architecture/{module}.md` or ADR
   - Naming decisions → Update `docs/naming-conventions.md` if needed
3. **Human reviews** — Approves or requests changes
4. **Spec approved** — Mark status as "Approved" → **documentation gate passed**

### Spec Document Structure

```markdown
# {Feature Name}

**Status**: Draft | Approved | Implemented  
**Author**: Claw  
**Approved By**: {Human name}  
**Date**: YYYY-MM-DD

---

## Goal

One sentence describing what this feature achieves.

## User Story

As a {user}, I want {capability}, so that {benefit}.

## Requirements

### Functional

- [ ] FR-1: {Requirement}
- [ ] FR-2: {Requirement}

### Non-Functional

- Performance: {metric}
- Security: {consideration}

## Technical Approach

{Brief description of implementation strategy}

## Dependencies

| Dependency | Status |
|------------|--------|
| Module A   | ✅ Done |
| Module B   | 🟡 In Progress |

## Test Plan

- Unit tests: {what to test}
- Integration tests: {what to test}

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
```

### Exit Criteria

- [ ] Spec document created (or ADR for architecture decisions)
- [ ] Human approval obtained (explicit or implicit)
- [ ] Dependencies identified
- [ ] Test plan outlined
- [ ] Naming conventions considered/updated
- [ ] **Documentation gate passed** → ready for Phase 2

---

## Phase 2: Implementation

**Goal**: Build the feature according to spec.

### Steps

1. **Create branch** (if using git) — `feature/{feature-name}`
2. **Implement incrementally** — Small commits, frequent checkpoints
3. **Write tests alongside** — Test-driven or test-adjacent
4. **Follow naming conventions** — Check `docs/naming-conventions.md`
5. **Update docs** — Keep docs in sync with code
6. **Mark spec as implemented** — Update status in spec doc

### Implementation Discipline

- Commit frequently with descriptive messages
- Run tests after each significant change
- Update project board in README.md at end of session
- Log significant decisions as ADRs (if architecture changes)
- Verify naming consistency before committing

### Session End Checklist

- [ ] Code committed
- [ ] Tests passing
- [ ] Project board updated
- [ ] Session log written

### Exit Criteria

- [ ] All functional requirements implemented
- [ ] Tests written and passing
- [ ] Code self-reviewed
- [ ] Spec marked "Implemented"

---

## Phase 3: Review

**Goal**: Human validates the implementation.

### Steps

1. **Claw self-review** — Run through quality checklist
2. **Human inspection** — Spot check or full review (human's choice)
3. **Address feedback** — If human requests changes, return to Phase 2
4. **Approval** — Human approves → ready for merge/release

### Quality Checklist (Claw Self-Review)

- [ ] All tests pass
- [ ] No linting errors
- [ ] Code follows project conventions
- [ ] Documentation updated
- [ ] ADRs created (if applicable)
- [ ] CHANGELOG.md draft prepared

### Human Review Options

| Level | Description | When |
|-------|-------------|------|
| **Spot check** | Review key files only | Low-risk changes |
| **Full review** | Complete inspection | Major features, API changes |
| **Delegated** | Trust claw's judgment | Routine patches, well-understood patterns |

### Exit Criteria

- [ ] Human approval obtained
- [ ] Feedback addressed (if any)
- [ ] Ready for merge/release

---

## Phase 4: Release

**Goal**: Package and deliver the completed work.

### Steps

1. **Update CHANGELOG.md** — Document changes
2. **Bump version** — Follow SemVer
3. **Create git tag** — `v{version}`
4. **Write release notes** — If external release
5. **Deploy** (if applicable)

### Version Bumping Guide

| Change Type | Bump | Example |
|-------------|------|---------|
| Breaking API change | MAJOR | 1.0.0 → 2.0.0 |
| New feature (compatible) | MINOR | 1.2.0 → 1.3.0 |
| Bug fix | PATCH | 1.2.3 → 1.2.4 |

### CHANGELOG.md Entry

```markdown
## [{version}] - YYYY-MM-DD

### Added
- {New feature} (#{issue})

### Changed
- {Modification}

### Fixed
- {Bug fix} (#{issue})

### Deprecated
- {Feature to be removed}

### Removed
- {Deleted feature}
```

### Exit Criteria

- [ ] CHANGELOG.md updated
- [ ] Version bumped in all locations
- [ ] Git tag created
- [ ] Release notes written (if external)
- [ ] Deployment completed (if applicable)

---

## Iteration Cycle

Projects typically run in iterations:

| Iteration Length | When to Use |
|------------------|-------------|
| **Single session** | Small features, bug fixes |
| **1-3 days** | Medium features |
| **1-2 weeks** | Large features, milestones |

### Iteration Planning

At start of each iteration:

1. Review project board
2. Select tasks for "In Progress"
3. Estimate effort (rough)
4. Set iteration end date

### Iteration Retrospective

At end of each iteration:

1. What went well?
2. What could be improved?
3. Adjust process for next iteration

---

## Branching Strategy (if using git)

```
main          — Protected, production-ready
develop       — Integration branch (default)
feature/xxx   — Feature branches (from develop)
hotfix/xxx    — Urgent fixes (from main)
```

### Workflow

```bash
# Start feature
git checkout develop
git checkout -b feature/my-feature

# Work... commit frequently

# Finish feature
git checkout develop
git merge feature/my-feature
git branch -d feature/my-feature

# Release
git checkout main
git merge develop
git tag v1.2.0
```

---

## Session Log Template

At end of each session, create/update `docs/notes/YYYY-MM-DD-{topic}.md`:

```markdown
# {Session Topic}

**Date**: YYYY-MM-DD HH:MM  
**Session**: {N}  
**Focus**: {Main focus of this session}

---

## Progress

| Task | Status | Notes |
|------|--------|-------|
| Task A | ✅ Done | {notes} |
| Task B | 🟡 50% | {notes} |

## Decisions Made

1. {Decision} — {Rationale}

## Blockers

- {Blocker} — {Resolution plan}

## Next Session

- Continue: {next task}
- Priority: {high/medium/low}
```

---

**Last Updated**: 2026-03-22 (v0.3.0)
