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
| Design | Spawn `project-pilot-design` (session, thread) | **Do NOT spawn** — Main Agent handles design directly (read `agent-workspaces/project-pilot-design/AGENTS.md` + `skills/write-specs/SKILL.md`, follow same lifecycle) |
| Implement | Spawn session | Spawn `mode: "run"` (Phase A→E in one turn) |
| Test Worker | Inherits parent mode | Inherits parent mode |

## Lifecycle Detection

State is derived purely from the filesystem. Check in order:

| # | Condition | Stage | Action |
|---|-----------|-------|--------|
| 1 | No `PROJECT.AGENT.md` | Init | Spawn `project-pilot-init` |
| 2 | `workspace/specs/` empty | Idle | Await Design trigger (see Session Compatibility for routing) or Bugfix trigger |
| 3 | `workspace/specs/` has symlinks, no `workspace/meta.md` | Plan (meta) | Spawn `project-pilot-plan` |
| 4 | `workspace/meta.md` exists, `workspace/contracts/open/` empty | Plan (contracts) | Spawn `project-pilot-plan` (Phase 2) |
| 5 | `workspace/contracts/in_progress/` has symlink | Implementing | Do NOT spawn — Implement Agent is running |
| 6 | `workspace/contracts/open/` has symlinks, `in_progress/` empty | Ready | Pick next contract (by priority/deps or ask human), `mv` symlink from `open/` to `in_progress/`, spawn `project-pilot-implement` |
| 7 | `workspace/specs/` has symlinks, `open/` and `in_progress/` both empty | Done | Spawn `project-pilot-cicd` |

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

- ⛔ Main agent only routes — does not write code, create contracts, or run reviews *(except design on non-session channels)*
- ⛔ Phase transitions require human confirmation
- ⛔ State is in files (`workspace/` symlinks + `docs/`), not conversation history

## Configuration

Configure agents in `openclaw.json`, see project's `openclaw.json` for reference.

**Version**: 2.2.0