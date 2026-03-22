# Project Initialization Checklist

Complete this checklist when starting a new project.

## Step 0: Identify Project Type

Before creating structure, determine project type:

| Type | When to Use | Template |
|------|-------------|----------|
| **OpenClaw Plugin** | OpenClaw 插件开发 | [project-types/openclaw-plugin.md](project-types/openclaw-plugin.md) |
| **Python Package** | Python 库、CLI、MCP Server | [project-types/python-package.md](project-types/python-package.md) |
| **Web App** | 前端/全栈 Web 应用 | [project-types/web-app.md](project-types/web-app.md) |
| **CLI Tool** | 命令行工具 | [project-types/cli-tool.md](project-types/cli-tool.md) |
| **Generic** | 其他软件项目 | Use default structure below |

**Human specifies project type** → Claw loads corresponding template.

## Step 1: Create Directory Structure

### For Generic Projects

```bash
mkdir -p {project-name}/{docs/{specs,decisions,notes},src,tests,scripts}
cd {project-name}
```

### For Type-Specific Projects

Follow the structure in the corresponding template:
- OpenClaw Plugin → See `project-types/openclaw-plugin.md`
- Python Package → See `project-types/python-package.md`
- Web App → See `project-types/web-app.md`
- CLI Tool → See `project-types/cli-tool.md`

## Step 2: Initialize README.md

Create root `README.md` with:

```markdown
# {Project Name}

> One-line value proposition

**Version**: 0.1.0  
**Status**: 🟡 Development  
**Last Updated**: YYYY-MM-DD

---

## 🎯 Problem

{2-3 sentences on what problem this solves}

## ✨ Core Features

- Feature 1
- Feature 2

## 📋 Current Iteration (YYYY-MM-DD ~ YYYY-MM-DD)

### In Progress
- [ ] {First task}

### Next Up
- [ ] {Planned task}

### Done
- [x] Project initialization

## 📚 Documentation

- [[Specifications]](docs/specs/) - Feature specs
- [[Decisions]](docs/decisions/) - Architecture decisions
- [[Session Logs]](docs/notes/) - Development diary

## 🔗 Links

- [Repository](URL)
```

## Step 3: Create docs/README.md

```markdown
# Documentation Index

| Directory | Purpose |
|-----------|---------|
| [specs/](specs/) | Feature specifications |
| [decisions/](decisions/) | Architecture decision records (ADRs) |
| [notes/](notes/) | Session logs and temporary notes |
```

## Step 4: Create First ADR

Document the foundational architecture choice:

```bash
mkdir -p docs/decisions
```

Create `docs/decisions/ADR-001-project-init.md`:

```markdown
# ADR-001: Project Initialization

**Date**: YYYY-MM-DD  
**Decision**: Use project-pilot skill for project management  
**Rationale**: Single human + claw collaboration requires lightweight but structured process

## Context
New project requires disciplined development without overhead of multi-team processes.

## Alternatives Considered
- Full PROJECT_STEWARD: Overkill for single human + claw
- No formal process: Risk of chaos during iteration

## Consequences
- ✅ Lightweight overhead
- ✅ Decision traceability maintained
- ⚠️ Requires discipline to maintain logs
```

## Step 5: Initialize CHANGELOG.md

```markdown
# Changelog

## [0.1.0] - YYYY-MM-DD

### Added
- Project initialization
```

## Step 6: Create .gitignore (if using git)

```
# Dependencies
node_modules/
__pycache__/
*.pyc

# Build outputs
dist/
build/
*.egg-info/

# Environment
.env
.venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

## Step 7: Initialize Git (optional)

```bash
git init
git add .
git commit -m "chore: project initialization"
```

## Step 8: Create First Session Log

```bash
mkdir -p docs/notes
```

Create `docs/notes/YYYY-MM-DD-kickoff.md`:

```markdown
# Project Kickoff

**Date**: YYYY-MM-DD HH:MM  
**Session**: 1  
**Attendees**: Human (企鹅), Claw

---

## Goals

- [x] Initialize project structure
- [ ] Define first milestone

## Decisions Made

1. Project management approach: project-pilot skill
2. Initial architecture: {brief description}

## Next Session

- Continue with: {next task}
- Blockers: {none / list any}
```

## Verification

Before marking initialization complete:

- [ ] README.md exists with project board
- [ ] docs/ directory structure created
- [ ] First ADR recorded
- [ ] CHANGELOG.md initialized
- [ ] Session log created
- [ ] (Optional) Git repo initialized

---

**Estimated Time**: 15-30 minutes  
**Owner**: Claw (automated)
