# Project Initialization

**Time**: 15-30 min | **Owner**: Claw (automated)

---

## Step 0: Identify Project Type

| Type | Template |
|------|----------|
| OpenClaw Plugin | [openclaw-plugin.md](project-types/openclaw-plugin.md) |
| Python Package | [python-package.md](project-types/python-package.md) |
| Web App | [web-app.md](project-types/web-app.md) |
| CLI Tool | [cli-tool.md](project-types/cli-tool.md) |
| Generic | (default structure below) |

---

## Step 1: Create Directory Structure

### Generic Project
```bash
mkdir -p {project}/{docs/{specs,decisions,notes,architecture},src,tests,scripts}
```

### Type-Specific
Follow corresponding template in `project-types/`.

---

## Step 2: Initialize README.md

**README.md is the single source of truth for project status (MUST-4)**

```markdown
# {Project Name}

> {One-sentence description}

**Version**: 0.1.0  
**Status**: 🟡 Development  
**Last Updated**: YYYY-MM-DD

---

## 🎯 Problem
{2-3 sentences}

## ✨ Solution
{2-3 sentences}

---

## 📋 Current Iteration (YYYY-MM-DD ~ )

### Design Phase (✅ Completed)
- [x] Initial design
- [x] Architecture decisions

### Phase 1-4: Implementation

#### Phase 1: {phase_name} (🟡 In Progress / ⏳ Pending / ✅ Completed - YYYY-MM-DD)
- [ ] Task 1
- [ ] Task 2

#### Phase 2: {phase_name} (⏳ Pending)
- [ ] Task 1

### Phase 5-7: {stage_name} (⏳ Pending)
- [ ] Phase 5: {name}
- [ ] Phase 6: {name}

---

## 📚 Documentation

| Directory | Content | Reader |
|-----------|---------|--------|
| [docs/decisions/](docs/decisions/) | ADRs (major decisions) | AI + Human |
| [references/interfaces/](references/interfaces/) | Interface docs | AI |
| [contracts/](contracts/) | Contracts | AI |

---

**Project Type**: {type}  
**Tech Stack**: {stack}  
**Maintainer**: {name}
```

**Key sections**:
- Current Phase clearly labeled with emoji (🟡/⏳/✅)
- Date-stamped completion
- Task checkboxes for transparency

---

## Step 3: Create docs/decisions/ Directory

```bash
mkdir -p docs/decisions
```

**ADRs track major decisions** — See [templates/adr.md](../templates/adr.md)

**First ADR** (`docs/decisions/ADR-001-project-init.md`):

```markdown
# ADR-001: Project Initialization

**Decision**: Use project-pilot skill

**Rationale**: Lightweight but structured process for human+claw collaboration
```

---

## Step 4: Create Naming Conventions

Copy template:
```bash
cp ../templates/naming-conventions.md docs/naming-conventions.md
```

Edit for project-specific rules.

---

## Step 5: Create First ADR

`docs/decisions/ADR-001-project-init.md`:

```markdown
# ADR-001: Project Initialization
**Date**: YYYY-MM-DD
**Decision**: Use project-pilot skill
**Rationale**: Lightweight but structured process for human+claw
```

---

## Step 6: Initialize CHANGELOG.md

```markdown
# Changelog

## [0.1.0] - YYYY-MM-DD

### Added
- Project initialization
```

---

## Step 7: Create Contract Directory Structure

```bash
mkdir -p contracts/{active,pending-confirmation,archive}
mkdir -p references/interfaces
```

---

## Step 8: Initialize Git (optional)

```bash
git init && git add . && git commit -m "chore: init"
```

---

## Verification

- [ ] README.md with project board
- [ ] `docs/decisions/` directory created
- [ ] ADR-001 created
- [ ] CHANGELOG.md initialized
- [ ] `references/interfaces/` directory created
- [ ] `contracts/` directory structure (`active/`, `pending-confirmation/`, `archive/`)
- [ ] Dependency graph scripts available (`scripts/*.py`)

---

**Version**: 1.1.2 (2026-03-26) — Contract Close vs Phase Completion clarified | **See also**: [guides/interface-docs.md](guides/interface-docs.md), [SKILL.md](../SKILL.md)
