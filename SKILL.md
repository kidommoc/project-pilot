---
name: project-pilot
description: Project management for single human + claw collaboration. Claw drives progress, human confirms or requests changes.
---

# Project Pilot

**Claw-Led, Human-Confirmed** — Lightweight project management for single human + claw teams.

**Philosophy**: Claw proposes, plans, and executes. Human reviews, confirms, or requests modifications.

## 🚨 MUST Constraints (Non-Negotiable)

**Violating these constraints = skill failure, must stop immediately and correct**

### MUST-1: Phase Completion Protocol

**After each Phase completes, MUST execute the following steps, then STOP and wait for confirmation:**

```
0. Execute test verification (Quality Gate)
   - Code: unit tests + functional tests
   - Docs: syntax check + link validation
   - Config: validation command + rollback test
1. Update checklists in project README.md
2. Write completion report to docs/notes/YYYY-MM-DD-phaseN-completion.md
3. Explicitly ask user: "Phase N completed (tests passed). Continue to Phase N+1?"
4. ⛔ Before user confirmation, FORBIDDEN to execute any code for next phase
```

**Trigger**: When all tasks in current Phase are marked complete

**Violation Examples**:
- ❌ Starting Phase 2 coding immediately after Phase 1 completion
- ❌ Continuing without updating README status
- ❌ Continuing without writing completion report
- ❌ Declaring Phase complete without tests passing

### MUST-2: Session Startup Check

**At the beginning of each Session, MUST check:**

```
1. Is current project using project-pilot? → If yes, load this skill
2. What is the current Phase in README.md?
3. Is previous Phase completed and waiting for confirmation?
4. Are there any unfinished Quality Gates?
```

### MUST-3: Documentation-First Enforcement

**MUST write documentation before code in these situations:**

- New Phase starts → Update README status first
- Before new feature implementation → Spec/ADR required
- Before architecture changes → ADR required
- After Phase completion → Write completion report first

### MUST-4: State Transparency

**Project state MUST always be findable in README.md:**

- Current Phase (explicitly labeled)
- Completed task checklist
- Blocking issues (if any)
- Next step plan

---

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
| OpenClaw Plugin | [openclaw-plugin.md](references/project-types/openclaw-plugin.md) | OpenClaw plugins, MCP bridges |
| Python Package | [python-package.md](references/project-types/python-package.md) | Python libraries, CLI, MCP Server |
| Web App | [web-app.md](references/project-types/web-app.md) | Frontend/Fullstack Web applications |
| CLI Tool | [cli-tool.md](references/project-types/cli-tool.md) | Command-line tools |
| Generic | (default) | Other software projects |

## Workflow Overview

```
Phase 1: Specification → Phase 2: Implementation → Phase 3: Review → Phase 4: Release
     ↓                        ↓                        ↓                   ↓
  Claw proposes           Claw executes           Claw self-reviews   Claw packages
  Human confirms          Human confirms          Human validates     Human confirms
```

**Claw drives progress. Human confirms or requests changes.**

📖 **Detailed workflow**: [references/workflow.md](references/workflow.md)

## Session Discipline

**Context Budget**:
- Files/session: ≤7 writes
- Response tokens: ≤1500
- Tool calls: ≤12
- Duration: ≤30 min

**When to `/new`**: Phase completion, context heavy, task switching, model degradation

**When to use subagent**: Parallel work, isolated tasks, heavy computation, research

📖 **Session Startup**: [references/guides/session-startup.md](references/guides/session-startup.md)  
📖 **Session Tasks**: [references/guides/session-tasks.md](references/guides/session-tasks.md)  
📖 **Test Verification**: [references/guides/test-verification.md](references/guides/test-verification.md)

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

## ℹ️ Usage Notes

**When to follow this skill**:
- Working in a development project with `README.md` tracking phases
- User mentions "project-pilot" or "follow the workflow"
- Starting a new session in an ongoing project

**Key reminder**: Check `README.md` at session start to find current Phase.

---

**Version**: 0.7.0 (2026-03-22) — Claw-led model
