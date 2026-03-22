---
name: project-pilot
description: Project management system for single human + claw collaboration. Use when starting or managing a development project where human provides design guidance and oversight while claw handles implementation, testing, and documentation. Provides workflows for project initialization, iterative development, decision tracking, and release management.
---

# Project Pilot

Project management for single human + claw collaboration.

## Core Principles

1. **Human = Commander, Claw = Pilot** — Human sets direction and approves key decisions; claw executes details
2. **State Transparency** — Project status always visible in README.md
3. **Decision Traceability** — All significant decisions recorded with rationale
4. **Documentation as Code** — Docs live in version control, updated incrementally
5. **Automation First** — Claw auto-maintains checklists, status boards, and changelogs
6. **Flexible Structure** — Adapt directory layout to project type

## Quick Start

### New Project Initialization

```bash
# 1. Identify project type (see Project Types below)
# 2. Create project structure per type template
# 3. Initialize README.md with project board
# 4. Create first decision record (architecture choice)
# 5. Set up iteration tracker
```

See [references/project-init.md](references/project-init.md) for complete initialization checklist.

## Project Types

Select the appropriate structure based on project type:

| Type | Template | Use Case |
|------|----------|----------|
| **OpenClaw Plugin** | [openclaw-plugin.md](references/project-types/openclaw-plugin.md) | OpenClaw 插件、MCP 桥接 |
| **Python Package** | [python-package.md](references/project-types/python-package.md) | Python 库、CLI、MCP Server |
| **Web App** | [web-app.md](references/project-types/web-app.md) | 前端/全栈 Web 应用 |
| **CLI Tool** | [cli-tool.md](references/project-types/cli-tool.md) | 命令行工具 |
| **Generic** | (default below) | 其他软件项目 |

### Generic Project Structure (Default)

```
{project-root}/
├── README.md                 # Entry point + project board (REQUIRED)
├── CHANGELOG.md              # Auto-maintained by claw
│
├── docs/
│   ├── README.md             # Doc navigation
│   ├── specs/                # Feature specifications
│   │   └── {feature-name}.md
│   ├── decisions/            # Decision records (ADRs)
│   │   └── ADR-{NNN}-{topic}.md
│   └── notes/                # Session logs
│       └── YYYY-MM-DD-{topic}.md
│
├── src/                      # Source code
├── tests/                    # Tests
└── scripts/                  # Automation scripts
```

### File Naming Rules

| Type | Pattern | Example |
|------|---------|---------|
| Specs | `kebab-case.md` | `warmup-system.md` |
| ADRs | `ADR-{NNN}-{topic}.md` | `ADR-001-use-mcp.md` |
| Notes | `YYYY-MM-DD-{topic}.md` | `2026-03-22-kickoff.md` |

**Prohibited:**
- ❌ Chinese filenames (except notes)
- ❌ Spaces in filenames
- ❌ >2 `.md` files in root directory

## Development Workflow

### Phase 1: Specification

1. Human provides high-level goal
2. Claw drafts spec → `docs/specs/{feature}.md`
3. Human reviews + approves (or requests changes)
4. Spec marked "Approved" → ready for implementation

### Phase 2: Implementation

1. Claw creates feature branch (if using git)
2. Implement + write tests
3. Update docs incrementally
4. Mark spec as "Implemented"

### Phase 3: Review

1. Claw self-reviews against checklist
2. Human inspects (spot check or full review)
3. Human approves → merge to main

### Phase 4: Release (if applicable)

1. Update CHANGELOG.md
2. Bump version (SemVer)
3. Create git tag
4. Release notes

See [references/workflow.md](references/workflow.md) for detailed phase descriptions.

## Decision Recording

Record decisions when:
- Choosing between multiple viable approaches
- Architecture changes
- API design choices
- Dependency selection

**Lightweight ADR format** (single human + claw):

```markdown
# ADR-001: {Decision Topic}

**Date**: YYYY-MM-DD  
**Decision**: {Chosen option}  
**Rationale**: {Why this over alternatives}

## Context
{Brief background}

## Alternatives Considered
- Option A: {Why rejected}
- Option B: {Why rejected}

## Consequences
- {Positive/negative outcomes}
```

Full template: [references/templates/adr.md](references/templates/adr.md)

## Project Board (README.md)

Maintain a simple kanban in README.md:

```markdown
## 📋 Current Iteration (YYYY-MM-DD ~ YYYY-MM-DD)

### In Progress
- [ ] Feature A (Spec: ✅ Approved | Dev: 🟡 50% | Test: ⏳ Pending)

### Next Up
- [ ] Feature B (Spec: 🟡 Draft)

### Done
- [x] Feature X (YYYY-MM-DD)
```

Claw auto-updates this board at end of each session.

## Session Discipline

### Start of Session

1. Read project README.md for current state
2. Check `docs/notes/` for last session's log
3. Update iteration board if needed

### End of Session

1. Commit work with descriptive message
2. Update project board status
3. Write session log → `docs/notes/YYYY-MM-DD-{topic}.md`
4. If spec completed: update CHANGELOG.md

## Quality Gates

### Before Human Review

Claw self-checks:
- [ ] Tests pass
- [ ] No linting errors
- [ ] Docs updated
- [ ] Decision records created (if applicable)

### Before Release

- [ ] All tests pass
- [ ] CHANGELOG.md updated
- [ ] Version bumped
- [ ] Git tag created
- [ ] Human approval obtained

See [references/checklists.md](references/checklists.md) for complete checklists.

## Version Management

Follow SemVer (`MAJOR.MINOR.PATCH`):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

CHANGELOG.md format:
```markdown
# Changelog

## [1.2.0] - 2026-03-22

### Added
- Feature X (#1)

### Changed
- API improvement for Y

### Fixed
- Bug Z (#2)
```

## When to Use This Skill

Use project-pilot when:
- Starting a new development project with human oversight
- Need structured iteration tracking
- Want decision traceability without heavy process
- Managing complex multi-session projects

Do NOT use for:
- One-off scripts or trivial tasks
- Multi-team coordination (use full PROJECT_STEWARD instead)
- Projects without human involvement

## References

- [Project Initialization](references/project-init.md) — Complete startup checklist
- [Workflow Details](references/workflow.md) — Phase-by-phase breakdown
- [Checklists](references/checklists.md) — Quality gates and release prep
- [Templates](references/templates/) — ADR, spec, session log templates
- **Project Types**:
  - [OpenClaw Plugin](references/project-types/openclaw-plugin.md)
  - [Python Package](references/project-types/python-package.md)
  - [Web App](references/project-types/web-app.md)
  - [CLI Tool](references/project-types/cli-tool.md)

---

**Skill Version**: 0.2.0  
**Last Updated**: 2026-03-22
