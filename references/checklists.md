# Quality Checklists

Use these checklists to ensure quality before reviews and releases.

---

## Pre-Review Checklist (Claw Self-Check)

Complete before requesting human review.

### Code Quality

- [ ] All tests pass (`npm test` / `pytest` / etc.)
- [ ] No linting errors
- [ ] No TypeScript/Python type errors
- [ ] Code follows project style guide
- [ ] No TODO comments left in critical paths
- [ ] No debug/logging statements in production code

### Documentation

- [ ] README.md updated (if user-facing changes)
- [ ] Inline comments for complex logic
- [ ] API docs updated (if API changed)
- [ ] Spec document marked "Implemented"

### Decision Tracking

- [ ] ADR created (if architecture/design decision made)
- [ ] Session log written

### Project Board

- [ ] README.md project board updated
- [ ] Status reflects current state

---

## Pre-Release Checklist

Complete before tagging a release.

### Functional

- [ ] All tests pass
- [ ] All acceptance criteria met
- [ ] No known critical bugs
- [ ] Smoke test passed (manual verification)

### Documentation

- [ ] CHANGELOG.md updated with all changes
- [ ] Version number updated in:
  - [ ] package.json / pyproject.toml / etc.
  - [ ] README.md badge
  - [ ] Any other version references
- [ ] Migration guide written (if breaking changes)

### Version Control

- [ ] All changes committed
- [ ] On correct branch (main/develop)
- [ ] Git tag created: `v{MAJOR}.{MINOR}.{PATCH}`
- [ ] Tag pushed to remote

### Release Notes (if external release)

- [ ] Release notes drafted
- [ ] Highlights section (key features)
- [ ] Breaking changes section (if applicable)
- [ ] Upgrade instructions (if applicable)
- [ ] Human approved release notes

### Deployment (if applicable)

- [ ] Deployment script tested
- [ ] Rollback plan documented
- [ ] Monitoring/alerting configured
- [ ] Human approved deployment

---

## Spec Review Checklist (Human)

Use when reviewing a spec document.

### Clarity

- [ ] Goal is clear and specific
- [ ] User story makes sense
- [ ] Requirements are testable

### Completeness

- [ ] All functional requirements listed
- [ ] Non-functional requirements specified
- [ ] Dependencies identified
- [ ] Edge cases considered

### Feasibility

- [ ] Technical approach is sound
- [ ] Dependencies available
- [ ] Effort estimate reasonable

### Approval

- [ ] Approved as-is
- [ ] Approved with minor changes (list below)
- [ ] Needs major revision (return to claw)

**Feedback**:
```
{Specific feedback if not approved as-is}
```

---

## Code Review Checklist (Human)

Use when reviewing implementation.

### Functionality

- [ ] Implements all requirements from spec
- [ ] Handles edge cases
- [ ] Error handling appropriate

### Code Quality

- [ ] Code is readable and well-organized
- [ ] No obvious bugs or logic errors
- [ ] Tests cover key scenarios

### Documentation

- [ ] Code comments where needed
- [ ] README/docs updated

### Approval

- [ ] Approved for merge
- [ ] Approved with minor fixes (list below)
- [ ] Needs significant revision (return to claw)

**Feedback**:
```
{Specific feedback}
```

---

## Session End Checklist

Complete at end of each development session.

- [ ] All work committed
- [ ] Commit messages are descriptive
- [ ] Project board updated in README.md
- [ ] Session log written to `docs/notes/`
- [ ] Any draft specs saved to `_drafts/` (if applicable)
- [ ] Next session priorities noted

---

## Project Health Check

Run weekly or at milestone boundaries.

### Progress

- [ ] Iteration goals on track
- [ ] No tasks stuck > 3 days
- [ ] Blockers identified and addressed

### Quality

- [ ] Test coverage acceptable (>80% recommended)
- [ ] No accumulating technical debt
- [ ] Documentation up to date

### Process

- [ ] ADRs being created for decisions
- [ ] Session logs being written
- [ ] Project board reflects reality

### Retrospective Notes

**What went well**:
- ...

**What to improve**:
- ...

**Action items for next iteration**:
- [ ] ...

---

**Last Updated**: 2026-03-22
