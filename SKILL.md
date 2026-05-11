---
name: project-pilot
description: "Project management for single human + claw collaboration. Triggers on 'use project-pilot', 'start development', or 'continue project {name}' when docs/contracts/ or workspace/contracts/ directory exists."
---

# Project Pilot v3 — Main Agent Skill

**Detect project lifecycle stage and spawn corresponding agentId to execute work.**

## Responsibilities

1. **Detect lifecycle stage** from filesystem
2. **Spawn corresponding agent**
3. **Bridge human ↔ agent interaction**

All development workflows are defined by each agent's AGENTS.md.

## Response Timing

- **Always respond within 3 seconds** (send quick ack, then spawn subagent)
- Subagents must NOT announce — end with `NO_REPLY`; Main Agent summarizes

## Session Compatibility

Session mode (`mode: "session"`) supported on: **Discord, Telegram** only.

Check `channel` or `provider` in inbound metadata.

| Agent | Session supported | Not supported |
|-------|------------------|---------------|
| Design | Discord/Telegram: spawn `project-pilot-design` (`runtime: "subagent"`, `mode: "session"`) | **Do NOT spawn** — Main Agent handles design directly (see below) |
| All other agents | `mode: "run"` | `mode: "run"` |

### Design on non‑session channels

When channel is NOT Discord/Telegram, Main Agent handles design directly:
1. Read `agent-workspaces/project-pilot-design/AGENTS.md` + `skills/write-specs/SKILL.md` + `skills/knowledge-verify/SKILL.md` + `skills/commit-design/SKILL.md`
2. Follow the same lifecycle (discuss → write spec → human confirms → spawn Knowledge Maintainer → verify → commit → symlinks)
3. After spec approved, end with a Result block (follow design AGENTS.md format). Then run lifecycle detection → Plan stage.

**On Discord/Telegram**: Do NOT read Design Agent's docs — spawn the agent instead.

---

## PROJECT.AGENT.md — Agent Instruction File

`PROJECT.AGENT.md` at the project root is the agent instruction file (analogous to Claude Code's `CLAUDE.md`).
Every spawned agent reads it as their first step.

- **Instructions**: positive rules — how to build, test, run, code conventions
- **Boundaries**: negative rules — what agents must NOT do

Init Agent creates the initial scaffold. Rules evolve as the project grows.

---

## Path Convention

All agents receive `{project_root}` as a spawn parameter. The `{your_workspace}` variable is the agent's own workspace directory (their pwd). All file paths in spawn tasks use `{project_root}/` prefix for project files.

---

## Lifecycle Detection

State is derived purely from the filesystem. Check in order:

| # | Condition | Stage | Action |
|---|-----------|-------|--------|
| 1 | No `PROJECT.AGENT.md` | Init | Read `agent-workspaces/project-pilot-init/references/maintainer-init-checklist.md` → ask human for info → spawn `project-pilot-init` with collected parameters (`runtime: "subagent"`, `mode: "run"`) |
| 2 | `workspace/specs/` empty | Idle | Ask human what to do next — start a new feature or report a bug |
| 3 | `workspace/specs/` has symlinks, no `workspace/meta.md` | Plan (meta) | Spawn `project-pilot-plan` (`runtime: "subagent"`, `mode: "run"`) |
| 4 | `workspace/meta.md` exists, `workspace/contracts/open/` empty | Plan (contracts) | Spawn `project-pilot-plan` (`runtime: "subagent"`, `mode: "run"`) |
| 5 | `workspace/contracts/in_progress/` has symlink | Implementing | Do NOT spawn — Implement Agent is running |
| 6 | `workspace/contracts/open/` has symlinks, `in_progress/` empty | Impl Pending | Read `workspace/meta.md` Contract Index. Pick the first contract in `open/` whose "Depends On" is `—` (or the dependency is NOT in `open/`). Move symlink from `open/` to `in_progress/` then:

```
Spawn with:
  task: "Implement contract {name} for iteration.
    Project root: {project_root}
    Contract: {project_root}/workspace/contracts/in_progress/{name}.md"
  runtime: subagent
  mode: run
  agentId: project-pilot-implement
```

If no eligible contract in `open/` → ask human. |
| 7 | `workspace/specs/` has symlinks, `open/` and `in_progress/` both empty, no `release-plan.md` | Release Prep | Spawn `project-pilot-cicd` with Phase 1 (`runtime: "subagent"`, `mode: "run"`, task includes `Phase: 1`) |
| 8 | `workspace/release-plan.md` exists | Release Exec | Read `release-plan.md`. If PASS → show human (audit summary + plan), wait for confirmation, then spawn CI/CD Phase 2. If FAIL → show human failures, let them decide (re-audit / force / cancel). To re-audit, delete `release-plan.md` (state returns to Release Prep). |

**After every spawn**: wait for agent return, read its Result block:
- **DONE** — check Human Confirmation; if empty → run lifecycle detection, if has content → show to human and wait
- **FAILED** — stop lifecycle, show Summary to human

### L0 Responsibilities

- **State routing**: Read workspace, determine stage, spawn agent
- **Contract selection**: Move symlink from `open/` → `in_progress/` before spawning Implement
- **Human bridge**: Relay agent results to human, relay human decisions to agents
- **Does NOT**: Write code, create contracts, run reviews, make design decisions

## Result Protocol

Every spawned agent (L1/L2) returns a structured Result as their final output.
L0 reads the Result to decide what to do next.

### Result Format

Agents end with this block (not `NO_REPLY` — L0 reads it as the spawn return value):

```markdown
## Result
**Status**: DONE | FAILED
**Summary**: {<1-2 sentences>}
**Human Confirmation**: {question for human, or empty}
**Next**: {what L0 should do next, or empty}
**Details**: {files changed, review outcomes, etc. for L0 internal use}
```

### L0 Behavior

After an agent returns, L0 reads the Result:

| Status | Human Confirmation | L0 Action |
|--------|-------------------|-----------|
| DONE | empty | Proceed to lifecycle detection → next stage |
| DONE | has question | Show Summary + question to human. Wait for yes/no. On yes → continue lifecycle. On no → ask human what to change. |
| FAILED | has explanation | Stop lifecycle. Show Summary + explanation to human. |
| FAILED | has details | Stop lifecycle. Show Summary to human, ask how to proceed. |

---

## Agent Registry

| agentId | Mode | Role |
|---------|------|------|
| `project-pilot-init` | run | Scaffold project structure + PROJECT.AGENT.md |
| `project-pilot-design` | session | Discuss design with human, write specs |
| `project-pilot-plan` | run | Read specs → meta contract → individual contracts |
| `project-pilot-implement` | run | Execute contract: Phase A→B→C→D |
| `project-pilot-cicd` | run | Release preparation (Phase 1) + merge/tag (Phase 2) |

---

## Iteration Types

| Type | Level | Spec Required | Flow |
|------|-------|---------------|------|
| **Minor** | Full design | Yes | Design → Plan → Implement → CI/CD |
| **Patch** | Quick fix | No | Plan → Implement → CI/CD |

## Bugfix Mode

When user reports a bug from Idle state (no active spec/iteration):

1. Main Agent confirms bug description with human
2. Spawn `project-pilot-plan` with bugfix context (no spec needed, iteration `v${patch}`)
3. Plan Agent creates iteration branch + single fix-contract
4. Symlink to `workspace/contracts/open/` → Main Agent detects Ready state
5. Normal flow continues: Implement → CI/CD

**vs normal iteration**: skips Design stage entirely. No spec or Knowledge updates.

**Detection**: Human says "fix bug", "there's a bug", or similar.

---

## Spawn Instructions

When spawning any agent, use `sessions_spawn` with these parameters:

```
runtime: "subagent"    # Always use subagent (Discord doesn't support thread-bound ACP)
mode: "run"            # All agents except Design
agentId: "<agent-id>"  # From Agent Registry
task: "<task description>
  Project root: {project_root}"
```

**For Design** (session mode on Discord/Telegram):
```
runtime: "subagent"
mode: "session"
agentId: "project-pilot-design"
task: "Design <feature-name> for {project}.
  Project root: {project_root}"
```

**Key rule**: Every spawn task must include `Project root: {project_root}` so the spawned agent knows the project directory.

---

## Key Constraints

- ⛔ **Do NOT read sub‑agent AGENTS.md** — you route to them, you don't become them
- ⛔ Main agent only routes — does not write code, create contracts, or run reviews
- ⛔ State is in files (`workspace/` symlinks + `docs/`), not conversation history
- ⛔ All spawned agents use `runtime: "subagent"`, not `runtime: "acp"`

---

## Directory Structure (v3.0)

```
project-root/
├── docs/
│   ├── knowledge/          # System context (created at init, filled by Design)
│   │   ├── architecture.md
│   │   ├── conventions.md
│   │   ├── journey-map.md
│   │   ├── journeys/
│   │   ├── modules/
│   │   ├── domain-models/
│   │   └── interfaces/
│   ├── specs/              # Per-iteration design
│   │   └── YYYY-MM-DD-{name}.md
│   ├── contracts/
│   │   ├── feature/        # Minor iteration contracts
│   │   ├── fix/            # Patch fix contracts
│   │   └── meta-{iteration}.md
│   └── roadmap.md
├── workspace/              # Working state (symlinks only)
│   ├── specs/              # Symlinks to active specs
│   └── contracts/
│       ├── open/           # Symlinks to pending contracts
│       └── in_progress/    # Symlink to active contract (exactly 1)
├── PROJECT.AGENT.md
├── CHANGELOG.md
└── src/                    # Code
```
