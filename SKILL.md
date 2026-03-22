---
name: project-pilot
description: Project management for single human + claw collaboration. Human = Commander (design/oversight), Claw = Pilot (implementation/testing/docs).
---

# Project Pilot

**Human = Commander, Claw = Pilot** — Lightweight project management for single human + claw teams.

## Core Principles

1. **Documentation-First** — No code without approved spec/ADR
2. **State Transparency** — Project status always visible in README.md
3. **Decision Traceability** — All significant decisions recorded
4. **Session Discipline** — Keep sessions lightweight, split aggressively

## Quick Start

```bash
# 1. Identify project type
# 2. Run initialization checklist
# 3. Start Phase 1 (Specification)
```

📋 **Full checklist**: [references/project-init.md](references/project-init.md)

## Project Types

| Type | Template | Use Case |
|------|----------|----------|
| OpenClaw Plugin | [openclaw-plugin.md](references/project-types/openclaw-plugin.md) | OpenClaw 插件、MCP 桥接 |
| Python Package | [python-package.md](references/project-types/python-package.md) | Python 库、CLI、MCP Server |
| Web App | [web-app.md](references/project-types/web-app.md) | 前端/全栈 Web 应用 |
| CLI Tool | [cli-tool.md](references/project-types/cli-tool.md) | 命令行工具 |
| Generic | (default) | 其他软件项目 |

## Workflow Overview

```
Phase 1: Specification → Phase 2: Implementation → Phase 3: Review → Phase 4: Release
     ↓                        ↓                        ↓                   ↓
  Human directs           Claw executes           Human approves      Human releases
```

📖 **Detailed workflow**: [references/workflow.md](references/workflow.md)

## Session Discipline

**Context Budget**:
- Files/session: ≤7 writes
- Response tokens: ≤1500
- Tool calls: ≤12
- Duration: ≤30 min

**When to `/new`**: Phase completion, context heavy, task switching, model degradation

**When to use subagent**: Parallel work, isolated tasks, heavy computation, research

📖 **Full guide**: [references/guides/session-tasks.md](references/guides/session-tasks.md)

## Key Templates

| Document | Template |
|----------|----------|
| ADR | [templates/adr.md](references/templates/adr.md) |
| Spec | [templates/spec.md](references/templates/spec.md) |
| Session Log | [templates/session-log.md](references/templates/session-log.md) |
| Naming Conventions | [templates/naming-conventions.md](references/templates/naming-conventions.md) |

## Quality Gates

**Before Human Review**: Tests pass, no lint errors, docs updated, ADRs created, naming consistent

**Before Release**: All tests pass, CHANGELOG updated, version bumped, git tag created, human approval

📋 **Full checklists**: [references/checklists.md](references/checklists.md)

## When to Use

✅ **Use for**: Development projects with human oversight, structured iteration tracking, decision traceability

❌ **Don't use for**: One-off scripts, multi-team coordination, projects without human involvement

---

**Version**: 0.4.0  
**Last Updated**: 2026-03-22
