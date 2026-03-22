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

```markdown
# {Project Name}

**Version**: 0.1.0 | **Status**: 🟡 Development

## 🎯 Problem
{2-3 sentences}

## 📋 Current Iteration (YYYY-MM-DD ~ )
### In Progress
- [ ] {First task}

### Done
- [x] Project initialization
```

---

## Step 3: Create docs/README.md

```markdown
# Documentation Index

| Directory | Purpose |
|-----------|---------|
| [architecture/](architecture/) | System design |
| [specs/](specs/) | Feature specs |
| [decisions/](decisions/) | ADRs |
| [notes/](notes/) | Session logs |

**Naming**: [naming-conventions.md](naming-conventions.md)
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

## Step 7: Create First Session Log

`docs/notes/YYYY-MM-DD-kickoff.md`:

```markdown
# Project Kickoff
**Date**: YYYY-MM-DD
**Goals**: [x] Init structure, [ ] Define milestone
**Next**: {next task}
```

---

## Step 8: Initialize Git (optional)

```bash
git init && git add . && git commit -m "chore: init"
```

---

## Verification

- [ ] README.md with project board
- [ ] docs/ structure (including `architecture/`)
- [ ] naming-conventions.md
- [ ] ADR-001 created
- [ ] CHANGELOG.md initialized
- [ ] Session log created

---

**Version**: 0.4.0 | **See also**: [guides/session-tasks.md](guides/session-tasks.md)
