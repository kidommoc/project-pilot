---
name: project-pilot
description: "Project management for single human + claw collaboration. Triggers on 'use project-pilot', 'start development', or 'continue project {name}' when docs/contracts/ or workspace/contracts/ directory exists."
---

# Project Pilot — Main Agent Skill

**Detect project lifecycle stage and spawn corresponding agentId to execute work.**

## Trigger Conditions

- User says "use project-pilot", "continue project XXX", "start development"
- Project directory contains `docs/contracts/` or `workspace/contracts/` directory

## How It Works

This skill contains NO development workflow logic. Its sole responsibilities are:

1. **Detect lifecycle stage**
2. **Spawn corresponding agent**
3. **Bridge human and agent interaction**

All development workflows, contract management, phase transitions, etc. are defined by each agent's AGENTS.md.

## Response Timing

### Discord Quick Response
- **Always respond within 3 seconds** to acknowledge the interaction
- Send a quick confirmation first (e.g., "Starting project-pilot workflow...")
- Then spawn subagent for slow work
- This prevents "Interaction already acknowledged" error

### No Announce
- Subagents must NOT post results back to the main chat
- To suppress announce, end with `NO_REPLY` or `no_reply`
- Main agent will summarize results for the user

## Lifecycle Detection

State is derived purely from the filesystem. Check in order:

| # | Condition | Stage | Action |
|---|-----------|-------|--------|
| 1 | No `PROJECT.AGENT.md` | Init | Spawn `project-pilot-init` |
| 2 | `workspace/specs/` empty | Idle | Await Design trigger → spawn `project-pilot-design` (session, thread-bound); or Bugfix trigger from human |
| 3 | `workspace/specs/` has symlinks, no `workspace/meta.md` | Plan (meta) | Spawn `project-pilot-plan` |
| 4 | `workspace/meta.md` exists, `workspace/contracts/open/` empty | Plan (contracts) | Spawn `project-pilot-plan` (Phase 2) |
| 5 | `workspace/contracts/in_progress/` has symlink | Implementing | Do NOT spawn — Implement Agent is running |
| 6 | `workspace/contracts/open/` has symlinks, `in_progress/` empty | Ready | Pick next contract (by priority/deps or ask human), `mv` symlink from `open/` to `in_progress/`, spawn `project-pilot-implement` |
| 7 | `workspace/specs/` has symlinks, `open/` and `in_progress/` both empty | Done | Spawn `project-pilot-cicd` |

### L0 Responsibilities

- **State routing**: Read workspace, determine stage, spawn agent
- **Contract selection**: Move symlink from `open/` → `in_progress/` before spawning Implement
- **Human bridge**: Relay agent results to human, relay human decisions to agents
- **Does NOT**: Write code, create contracts, run reviews, make design decisions

## Agent Registry

| agentId | Mode | Role | When to Spawn |
|---------|------|------|---------------|
| `project-pilot-init` | run | Initializes project structure + PROJECT.AGENT.md | No PROJECT.AGENT.md found |
| `project-pilot-design` | session, thread-bound | Discusses design with human, writes specs | Human triggers design from Idle state |
| `project-pilot-plan` | run | Reads specs, produces contracts | Main agent after specs confirmed |
| `project-pilot-implement` | session | Executes a single contract | Main agent for each open contract |
| `project-pilot-interface-worker` | run | Defines interfaces (code + docs) | Spawned by implement agent |
| `project-pilot-test-worker` | session | Writes tests (RED) + verifies (GREEN) | Spawned by implement agent |
| `project-pilot-coding-worker` | run | Implements interfaces to pass tests | Spawned by implement agent |
| `project-pilot-review-worker` | run | Reviews work output (multiple skills) | Spawned by design/plan/implement agents |

## Spawn Examples

```
// One-shot agent (e.g. init, plan, cicd)
sessions_spawn({
  task: "Initialize project: [project context]",
  runtime: "subagent",
  mode: "run",
  agentId: "project-pilot-init"
})

// Session agent with thread binding (e.g. design)
// After spawn, report the returned session key to the user
sessions_spawn({
  task: "Design feature: [user intent and project context]",
  runtime: "subagent",
  mode: "session",
  thread: true,
  agentId: "project-pilot-design"
})
// → Tell user: "Design session started, session key: <key>"
```

## Design Stage

When user triggers design from Idle state:

1. Spawn `project-pilot-design` in session mode (thread-bound), with `streamTo: "parent"` disabled (no announce)
2. Report the session key to the user so they can focus into the design session
3. Design Agent discusses requirements and architecture with the human directly
4. After discussion converges, Design Agent writes specs, spawns review-worker for validation
5. After review passes, commits specs + creates symlinks in `workspace/specs/`
6. Main Agent then detects state #3 (Plan) and continues the workflow

**Important**: Main Agent does NOT relay messages for Design Agent. The human interacts with Design Agent directly via the session.

## Bugfix Mode

When user reports a bug from Idle state (no active spec/iteration):

1. Main Agent confirms bug description with human
2. Spawn `project-pilot-plan` with bugfix context (no spec needed)
3. Plan Agent creates iteration branch (`iteration/v<patch-version>`) + single fix-contract
4. Normal flow continues: Implement → CI/CD

**Key difference from normal iteration**: skips Design stage entirely. No spec is written. Plan Agent uses `references/fix-contract.md` template instead of mini/full contract.

**Detection**: Human explicitly says "fix bug", "there's a bug", or similar. Main Agent asks for bug description, then spawns Plan Agent with the description as context.

## Key Constraints

### ⛔ Main agent does NOT execute development workflows
Main agent only routes; does not do contract management, interface writing, code implementation, etc.

### ⛔ Phase transitions require human confirmation
Each agent must pause and wait for human confirmation after completing a phase.

### ⛔ State is in files
Project state is visible through `workspace/contracts/` symlinks and `docs/` files, not dependent on conversation history.

## Configuration Requirements

Before use, configure agents in `openclaw.json`, see project's `openclaw.json` for reference.

**Version**: 2.0.5
**Release**: v2.0.5