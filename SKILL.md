---
name: project-pilot
description: "Project management for single human + claw collaboration. Triggers on 'use project-pilot', 'start development', or 'continue project {name}' when docs/contracts/ or workspace/contracts/ directory exists."
---

# Project Pilot — Main Agent Skill

**Detect project lifecycle stage and spawn corresponding agentId to execute work.**

## Trigger Conditions

- User says "use project-pilot", "continue project XXX", "start development"
- Project directory contains `docs/contracts/` or `workspace/contracts/` directory

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

Check `channel` or `provider` in inbound metadata. Fallback:

| Agent | Session supported | Not supported |
|-------|------------------|---------------|
| Design | Discord/Telegram: spawn `project-pilot-design` (`runtime: "subagent"`, `mode: "run"`) — one-shot, re-spawn for feedback | **Do NOT spawn** — Main Agent handles design directly (see "Design on non‑session channels" below) |
| Implement | Spawn session (`runtime: "subagent"`, `mode: "session"`) | Spawn `mode: "run"` (Phase A→E in one turn) |
| Test Worker | Inherits parent mode | Inherits parent mode |

### Design on non‑session channels

When channel is NOT Discord/Telegram, Main Agent handles design directly:
1. Read `agent-workspaces/project-pilot-design/AGENTS.md` + `skills/write-specs/SKILL.md`
2. Follow the same lifecycle (discuss → write spec → spawn review → commit → symlinks)
3. After spec approved, continue to Plan stage

**On Discord/Telegram**: Do NOT read Design Agent's docs — spawn the agent instead.

## Lifecycle Detection

State is derived purely from the filesystem. Check in order:

| # | Condition | Stage | Action |
|---|-----------|-------|--------|
| 1 | No `PROJECT.AGENT.md` | Init | Spawn `project-pilot-init` (`runtime: "subagent"`, `mode: "run"`) |
| 2 | `workspace/specs/` empty | Idle | Await Design trigger (see Session Compatibility for routing) or Bugfix trigger |
| 3 | `workspace/specs/` has symlinks, no `workspace/meta.md` | Plan (meta) | Spawn `project-pilot-plan` (`runtime: "subagent"`, `mode: "run"`) |
| 4 | `workspace/meta.md` exists, `workspace/contracts/open/` empty | Plan (contracts) | Spawn `project-pilot-plan` (`runtime: "subagent"`, `mode: "run"`) |
| 5 | `workspace/contracts/in_progress/` has symlink | Implementing | Do NOT spawn — Implement Agent is running |
| 6 | `workspace/contracts/open/` has symlinks, `in_progress/` empty | Ready | Pick next contract (by priority/deps or ask human), `mv` symlink from `open/` to `in_progress/`, spawn `project-pilot-implement` (`runtime: "subagent"`, mode per Session Compatibility) |
| 7 | `workspace/specs/` has symlinks, `open/` and `in_progress/` both empty | Done | Spawn `project-pilot-cicd` (`runtime: "subagent"`, `mode: "run"`) |

### L0 Responsibilities

- **State routing**: Read workspace, determine stage, spawn agent
- **Contract selection**: Move symlink from `open/` → `in_progress/` before spawning Implement
- **Human bridge**: Relay agent results to human, relay human decisions to agents
- **Does NOT**: Write code, create contracts, run reviews, make design decisions *(except on non-session channels where Main Agent handles design directly)*

## Agent Registry

| agentId | Mode | Role |
|---------|------|------|
| `project-pilot-init` | run | Initializes project structure + PROJECT.AGENT.md |
| `project-pilot-design` | session (Discord/Telegram only) | Discusses design with human, writes specs |
| `project-pilot-plan` | run | Reads specs, produces contracts |
| `project-pilot-implement` | session or run (see Session Compatibility) | Executes a single contract |
| `project-pilot-interface-worker` | run | Defines interfaces (code + docs) |
| `project-pilot-test-worker` | inherits parent mode | Writes tests (RED) + verifies (GREEN) |
| `project-pilot-coding-worker` | run | Implements interfaces to pass tests |
| `project-pilot-review-worker` | run | Reviews work output (multiple skills) |

## Bugfix Mode

When user reports a bug from Idle state (no active spec/iteration):

1. Main Agent confirms bug description with human
2. Spawn `project-pilot-plan` with bugfix context (no spec needed)
3. Plan Agent creates iteration branch (`iteration/v<patch-version>`) + single fix-contract
4. Normal flow continues: Implement → CI/CD

**vs normal iteration**: skips Design stage entirely. No spec needed. Plan Agent uses `references/fix-contract.md` template instead of mini/full contract.

**Detection**: Human says "fix bug", "there's a bug", or similar. Main Agent asks for bug description, then spawns Plan Agent with the description as context.

## Key Constraints

- ⛔ **Do NOT read sub‑agent AGENTS.md** — you route to them, you don't become them
  - Exception: On non‑session channels, Main Agent reads Design Agent's docs to handle design directly
- ⛔ Main agent only routes — does not write code, create contracts, or run reviews *(except design on non‑session channels)*
- ⛔ Phase transitions require human confirmation
- ⛔ State is in files (`workspace/` symlinks + `docs/`), not conversation history

## Spawn Instructions

When spawning any agent, use `sessions_spawn` with these parameters:

```yaml
runtime: "subagent"    # Always use subagent, NOT acp (Discord doesn't support thread-bound ACP)
mode: "run" | "session"  # See Session Compatibility table above
agentId: "<agent-id>"   # From Agent Registry
cwd: "~/.openclaw/projects/project-pilot"
task: "<task description>"
```

**Critical**: Do NOT use `runtime: "acp"` — Discord channel does not support thread-bound ACP sessions.

## Configuration

Configure agents in `openclaw.json`, see project's `openclaw.json` for reference.

**Version**: 2.2.1