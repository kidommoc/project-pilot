# Contract: AgentId-Based Architecture for Project-Pilot

**Opened**: 2026-04-07T10:42 | **Priority**: high

## Goal
Restructure project-pilot to use agentId + dedicated workspace architecture, replacing attachment-based and skill-embedded approaches.

## Problem Statement
Current architecture mixes approaches: attachments (disabled by default), task-embedded instructions, inherited skill context. Need a clean, unified approach where each agent's behavior is defined by its own workspace AGENTS.md, accessed via agentId.

## Proposal
- Each agent has a dedicated workspace under `projects/project-pilot/agent-workspaces/project-pilot-{role}/`
- Each workspace contains an AGENTS.md defining that agent's complete behavioral instructions
- Main agent skill (installed in `skills/project-pilot/`) only contains routing logic: detect lifecycle stage → spawn correct agentId
- No attachments needed: AGENTS.md provides behavior, task provides context, cwd inheritance provides file access
- All agentId prefixed with `project-pilot-` for easy identification

## Agent Registry

| agentId | Role | Spawned by |
|---------|------|------------|
| `project-pilot-iteration` | Manage P1→P2→P3→P4 workflow, coordinate work agents | Main agent |
| `project-pilot-contract` | Draft contracts | Iteration agent |
| `project-pilot-interface` | Write interface docs | Iteration agent |
| `project-pilot-test-creation` | Write test cases | Iteration agent |
| `project-pilot-implementation` | Write code | Iteration agent |
| `project-pilot-review` | Review work products (contract/interface/test/code) | Iteration agent |
| `project-pilot-testing-execution` | Run tests, report results | Iteration agent |

Note: init and design phases may not need dedicated agents initially — can be handled by iteration-agent or main agent directly.

## Acceptance Criteria
- [x] Main agent skill (`SKILL.md`) contains only routing logic, no workflow details
- [x] Each agent workspace has AGENTS.md with complete behavioral instructions
- [x] All agentId follow `project-pilot-{role}` naming convention
- [x] No attachments used — behavior via AGENTS.md, context via task, files via cwd
- [x] Iteration agent can coordinate work agents via nested spawning (requires maxSpawnDepth >= 2)
- [x] openclaw.json config documented for all required agents
- [x] Old attachment-based files (workflows/, skills/) cleaned up

## Implementation Plan
1. Rename existing agent-workspaces to `project-pilot-{role}` convention
2. Refine each AGENTS.md to be self-contained behavioral instructions
3. Rewrite main agent skill to pure routing logic
4. Remove workflows/ directory (content absorbed into AGENTS.md)
5. Remove skills/ subdirectory under projects/ (replaced by agent-workspaces)
6. Document required openclaw.json configuration
7. Update README to reflect new architecture

## Boundary
- **Touches**: agent-workspaces (rename + refine), main skill (rewrite), README, openclaw.json config docs
- **Does NOT touch**: Original references/ directory, contracts/ structure, lightweight-workflow