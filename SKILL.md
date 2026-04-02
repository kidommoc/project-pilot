---
name: project-pilot
description: Project management for single human + claw collaboration. Claw drives progress, human confirms or requests changes.
---

# Project Pilot

**Claw-Led, Human-Confirmed** — Lightweight project management for single human + claw teams.

**Philosophy**: Contract-first, acceptance-driven. Claw proposes, plans, and executes. Human confirms or requests changes.

## 🚨 MUST Constraints (Non-Negotiable)

**Violating these constraints = skill failure, must stop immediately and correct**

### MUST-1: Phase Completion Protocol

**After each Phase completes, MUST execute the following steps, then STOP and wait for confirmation:**

```
0. Execute test verification (Quality Gate)
   - Code: unit tests + functional tests + contract item verification
   - Docs: syntax check + link validation
   - Config: validation command + rollback test
1. Update interface docs (if interfaces changed)
2. Explicitly ask user: "Phase N completed (tests passed). Continue to Phase N+1?"
3. ⛔ Before user confirmation, FORBIDDEN to execute any code for next phase
```

**Note**: README.md phase status is maintained in iteration branches only, not in main.

**Trigger**: When all tasks in current Phase are marked complete

**Violation Examples**:
- ❌ Starting Phase 2 coding immediately after Phase 1 completion
- ❌ Continuing without updating interface docs (if interfaces changed)
- ❌ Declaring Phase complete without tests passing

### MUST-2: Activation Check

**Do NOT auto-apply project-pilot. Wait for explicit trigger:**

1. Human explicitly requests project-pilot → Apply immediately
2. Human says "continue project {name}" → Check project structure first
3. No trigger → Do NOT apply

**Project structure check** (for case 2):
```bash
ls README.md contracts/ references/interfaces docs/decisions
```
- All exist → Apply project-pilot
- Missing → Prompt for initialization

### MUST-3: Contract-First Enforcement

**MUST have an approved Contract before writing any implementation code:**

- Before new feature implementation → Mini-Contract or full Contract required
- Before architecture changes → Full Contract + ADR required
- ⛔ No code before Implementation Brief (Phase 2 Step 1) is written

**Contract Selection**:
- Default: **Mini-Contract** (≤ 8 contract items, single module, no complex deps)
- Upgrade to **Full Contract** when: items > 8, multi-module scope, architectural impact, complex dependency graph

### MUST-4: Interface Docs Enforcement

**MUST update interface docs when modifying module interfaces:**

- Read interface docs before modifying (understand callers, deps, invariants)
- Update interface docs after modifying (reflect current state)
- Interface docs = Single Source of Truth (always reflects current code)

**Violation Examples**:
- ❌ Modifying function signature without updating interface docs
- ❌ Changing module behavior without documenting invariants
- ❌ Adding callers without updating "Called by" section

### MUST-5: State Transparency

**Project state MUST always be findable:**

- Draft Contracts → `contracts/draft/` (awaiting human confirmation)
- Open Contracts → `contracts/open/` (confirmed, waiting to start)
- In-Progress Contract → `contracts/in_progress/` (exactly 1, current focus)
- Archived Contracts → `contracts/archived/` (completed)
- Interface docs → `references/interfaces/` (permanent state)
- Phase status → `README.md` (high-level overview)

---

## Core Principles

1. **Contract-First** — No code without an approved Contract (Mini or Full)
2. **Acceptance-Driven** — Success = all Contract items pass, not "code written"
3. **Interface Docs as Truth** — Interface docs always reflect current code state
4. **Temporary vs Permanent State** — Contract progress is temporary, interface docs are permanent
5. **No Session History Dependency** — Project state is in files, not conversation history
6. **Decision Traceability** — All significant decisions recorded in ADRs

## Contract Definition

**Contract = Development action atomic unit + Interface contract**

A Contract is not a project specification. It is:
- The intent, scope, interfaces, and verification of **this modification**
- Closed when: verification passed + interface docs updated + human confirmed
- After closing: moved to `contracts/archived/`, interface docs remain updated

### Contract vs Phase

| Level | Concept | Definition | Contains |
|-------|---------|------------|----------|
| **L2** | **Phase** | Development stage (human view) | Multiple Contracts |
| **L3** | **Contract** | Atomic development action (AI view) | Tasks + Interface Contract |

**Relationship**:
- **Phase 1** (Contract Definition): 1 Contract (project specification)
- **Phase 2** (Implementation): N Contracts (one per feature/module)
- **Phase 3** (Audit): 0 Contracts (audit all completed Contracts)
- **Phase 4** (Release): 0 Contracts (package and ship)

**Contract closes independently** — each Contract is verified and closed on its own, not waiting for Phase completion.

### Contract Structure

```markdown
**Opened**: YYYY-MM-DDTHH:MM

**Modified Files**:
- `file.py` (description - done)

## Goal
...

## Interface Contract
...
```

### Contract Lifecycle

```
contracts/
├── draft/               # Claw-drafted, awaiting human confirmation
├── open/                # Human-confirmed, waiting to start (multiple allowed)
├── in_progress/         # Current focus (exactly 1 enforced)
└── archived/            # Completed contracts

Flow: draft → human confirms → open → start → in_progress → done → archived

Session Recovery:
1. ls contracts/in_progress/
   - 1 contract → Read and continue
   - 0 contracts → Check open/ → Select next → Move to in_progress/
   - >1 contracts → 🚨 Error state, report to human
2. Read contract → find last completed task (via Tasks/Contract checkboxes) → continue
```

### Temporary Progress vs Permanent State

| Type | Location | Lifecycle |
|------|----------|-----------|
| **Temporary Progress** | Contract Tasks/Contract checkboxes | Contract lifecycle |
| **Permanent State** | Interface docs | Project lifecycle |

### Single Focus Constraint

**`contracts/in_progress/` MUST contain exactly 1 contract at any time.**

| Directory | Purpose | Quantity Constraint |
|-----------|---------|---------------------|
| `draft/` | Claw-drafted, awaiting human confirmation | Multiple allowed |
| `open/` | Human-confirmed, waiting to start | Multiple allowed (like GitHub open issues) |
| `in_progress/` | Current implementation focus | **Exactly 1** (enforced) |
| `archived/` | Completed contracts | Unlimited |

**Violation**: If `in_progress/` has >1 contracts, Claw must report error state and ask human to resolve.

---

## Quick Start

```bash
# 1. Identify project type
# 2. Run initialization checklist
# 3. Start Phase 1 (Contract Definition)
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
Human Goal
  ↓
Phase 1: Contract       — Define WHAT + HOW to verify + Interface Contract
  ↓ (human confirms)
Phase 2: Implementation — Brief → Implement+Verify per item → Update interface docs
  ↓ (auto)
Phase 3: Audit          — Adversarial audit against Contract
  ↓ (human confirms)
Phase 4: Release        — Package and ship
```

**Claw drives progress. Human confirms or requests changes.**

**Key change from traditional**: Interface docs updated during implementation, not after.

📖 **Detailed workflow**: [references/workflow.md](references/workflow.md)

## Related Guides

📖 **Workflow**: [references/workflow.md](references/workflow.md)  
📖 **Checklists**: [references/checklists.md](references/checklists.md)  
📖 **Interface Docs**: [references/guides/interface-docs.md](references/guides/interface-docs.md)  
📖 **Test Verification**: [references/guides/test-verification.md](references/guides/test-verification.md)  
📖 **Task Decomposition**: [references/guides/session-tasks.md](references/guides/session-tasks.md)

## Tools

**Dependency Analysis**:
```bash
# Source code dependencies
python scripts/extract-dependencies.py --src . --output .project-graph.json
python scripts/query-deps.py --graph .project-graph.json --impact module_name

# Documentation dependencies
python scripts/extract-doc-deps.py --src . --output .doc-graph.json
python scripts/query-doc-deps.py --graph .doc-graph.json --impact references/file.md
```

**Use in Contract Impact Analysis** (see templates/mini-contract.md).

## Key Templates

| Document | Template | When to Use |
|----------|----------|-------------|
| Mini-Contract | [templates/mini-contract.md](references/templates/mini-contract.md) | Default for most changes (≤ 8 contract items, single module) |
| Contract | [templates/contract.md](references/templates/contract.md) | Multi-module features, architectural changes, complex deps |
| Interface Contract | [templates/interface-contract.md](references/templates/interface-contract.md) | Supplement when modifying module interfaces |
| ADR | [templates/adr.md](references/templates/adr.md) | Significant architectural decisions |
| Naming Conventions | [templates/naming-conventions.md](references/templates/naming-conventions.md) | Reference |

## Quality Gates

**Before Phase 3**: All Contract items pass, tests pass, Implementation Brief written, Contract marked "Done"

**Before Release**: All tests pass, Audit Summary approved by human, CHANGELOG updated, version bumped, git tag created

📋 **Full checklists**: [references/checklists.md](references/checklists.md)

## When to Use

✅ **Use for**: Development projects with human oversight, structured iteration tracking, decision traceability

❌ **Don't use for**: One-off scripts, multi-team coordination, projects without human involvement

---

## ℹ️ Activation

**Explicit trigger required** — Do NOT auto-apply.

### Triggers

**Apply project-pilot when**:

1. **Explicit request**: Human says "Use project-pilot" or "Follow the workflow"
2. **Project continuation**: Human says "Continue project {name}" AND project structure exists
3. **New development**: Human says "Start development" AND agrees to use structured process

### Project Structure Check

**If triggered by "continue project"**, verify:

```bash
# Required structure
ls README.md contracts/ references/interfaces docs/decisions
```

| Result | Action |
|--------|--------|
| All exist | → Apply project-pilot |
| Missing | → Prompt: "Project structure incomplete. Run initialization?" |

### Key Principle

**Project state = Contract files + Interface docs, not conversation history**

- Check `contracts/in_progress/` for current focus
- Check `contracts/open/` for queued work
- Read interface docs for current system state
- Do NOT rely on session history

### Session Startup After Contract Closed

**Session Recovery Algorithm**:

```
1. ls contracts/in_progress/
   - 1 contract → Read and continue
   - 0 contracts → Check open/ → Select next → Move to in_progress/
   - >1 contracts → 🚨 Error state, report to human

2. Read contract Status section
   - Find last completed task
   - Continue from next pending task
```

**If `contracts/in_progress/` is empty AND `contracts/open/` is empty**:

1. Read README.md → Find last completed Phase
2. Check last archived Contract → Find "Next Session" suggestion
3. Determine context:
   - **Same Phase** (more Contracts to do):
     ```
     Last Contract suggested: {task}
     Create new Contract for this?
     ```
   - **Phase completed** (all Contracts done):
     ```
     Phase N completed (all Contracts done).
     Continue to Phase N+1?
     ```
4. Human confirms → Create new Contract or start Phase N+1
```

**Key Principle**: Project state = Contract files + Interface docs, NOT conversation history.

---

## Documentation Philosophy

**AI-First, Human-Summary**

| Document | Purpose | Reader | When Created |
|----------|---------|--------|--------------|
| **Contract** | Development action tracking | AI | Every modification |
| **Interface Docs** | Single source of truth | AI | When interfaces change |
| **ADR** | Major decision rationale | AI + Human | Architectural decisions |
| **README** | Project status summary | Human | Phase completion |

**Not needed**:
- ❌ Completion reports (Contract Status covers it)
- ❌ Architecture docs (in ADR + interface docs)
- ❌ Specs (in Contract + interface docs)

**Human-readable summary**: 1 sentence at Phase completion, not long reports.

---

**Version**: 1.1.1 (2026-03-26) — Next Session tracking for session continuity
