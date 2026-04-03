---
name: project-pilot
description: Project management for single human + claw collaboration. Triggers on "use project-pilot", "start development", or "continue project {name}" when contracts/ directory exists.
---

# Project Pilot

**Claw-led, human-confirmed project management.**

## MUST Constraints

Violating these = skill failure. Stop and correct immediately.

### MUST-1: Proactive Execution
Claw actively drives progress; human provides high-level direction only.
- Human: Sets goals ("implement X")
- Claw: Designs Contracts, proposes plans, reports progress
- **Human confirms at decision points**: Contract approval, Phase transitions, release

Never wait for detailed instructions. Propose complete next steps. But **never proceed past a decision point without explicit human confirmation**.

### MUST-2: Contract-First
No implementation without approved Contract in `contracts/in_progress/`.
Contract closes only when all items pass verification.
"Code written" ≠ "Contract closed".

### MUST-3: Single Focus
`contracts/in_progress/` must contain exactly 1 file.
more than 1 files = error state. Stop and report to human.

### MUST-4: Interface Docs
Update `references/interfaces/{module}.md` when modifying module interfaces.
Interface docs = Single Source of Truth (always reflect current code).

### MUST-5: Process Adherence
Follow Phase sequence: P1 → P2 → P3 → P4.
No Phase skipping. No next-Phase action without explicit user confirmation.

### MUST-6: State in Files
Project state must be recoverable from files without session history.
Always write state to contracts/, interfaces/, README — never assume conversation continuity.

## Session Startup

```
1. Read README.md → Determine Phase
2. Based on Phase:
   ├─ P1 → Continue defining Contracts
   ├─ P2 → Check contracts/open/ and in_progress/ → Continue or start Contract
   ├─ P3 → Perform audit
   ├─ P4 → Prepare release
   └─ Done → Ask: "New iteration?"
```

**Phase Detection:**
| Phase | Indicator |
|-------|-----------|
| P1 | Iteration just created, Contracts being defined |
| P2 | Contracts in `open/` or `in_progress/` |
| P3 | All Contracts archived, awaiting audit |
| P4 | Audit passed, awaiting release |

## Decision Rules

### Contract Selection
| Condition | Selection |
|-----------|-----------|
| ≤8 items, single module, simple deps | Mini-Contract (default) |
| >8 items OR multi-module OR architectural | Full Contract |

### ADR Trigger
Create ADR when:
- Changes project structure
- New dependency patterns
- Breaking interface changes

### State Storage
| Type | Location | Lifecycle |
|------|----------|-----------|
| Temporary progress | Contract checkboxes | Contract |
| Permanent truth | references/interfaces/ | Project |

## Phase Quick Reference

| Phase | Goal | Detail |
|-------|------|--------|
| P1 | Contract Definition | [workflow-phase1.md](references/workflow-phase1.md) |
| P2 | Implementation | [workflow-phase2.md](references/workflow-phase2.md) |
| P3 | Audit | [workflow-phase3.md](references/workflow-phase3.md) |
| P4 | Release | [workflow-phase4.md](references/workflow-phase4.md) |

## Templates & Tools

| Use | File |
|-----|------|
| Mini-Contract | references/templates/mini-contract.md |
| Full Contract | references/templates/contract.md |
| Interface Contract | references/templates/interface-contract.md |
| ADR | references/templates/adr.md |

## Project Types

| Type | Template |
|------|----------|
| OpenClaw Plugin | references/project-types/openclaw-plugin.md |
| Python Package | references/project-types/python-package.md |
| Web App | references/project-types/web-app.md |
| CLI Tool | references/project-types/cli-tool.md |

**Version**: 2.0.0 | **See also**: [CHANGELOG](CHANGELOG.md)
