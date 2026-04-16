# Contract: Three-Tier Architecture for Project-Pilot

**Opened**: 2026-04-07T02:31 | **Priority**: high

## Goal
Implement three-tier architecture: main agent (human interaction), project agent (workflow management), and specialized work agents (execution) with proper review cycles.

## Problem Statement
Current project-pilot lacks clear separation of concerns between interaction, workflow management, and execution layers. Need structured architecture that ensures workflow discipline while enabling specialized execution.

## Proposal
Design three-tier system:
- **Main Agent**: Detects project-pilot context, spawns project agent, bridges communication
- **Project Agent**: Manages P1→P2→P3→P4 workflow, coordinates work agents, enforces discipline
- **Work Agents**: Specialized agents for contracts, interfaces, tests, implementation, testing (each with paired review agents)

Work agents types: Contract, Interface, Test Creation, Implementation, Testing Execution (+ Review agents for first 4).

## Acceptance Criteria
- [ ] Main agent skill handles detection and project agent spawning only
- [ ] Project agent manages complete P1→P2→P3→P4 workflow with gate enforcement
- [ ] Six specialized work agents implemented: Contract, Interface, Test Creation, Implementation, Testing Execution, Review
- [ ] Review agents spawned after each of first 4 work agent types
- [ ] Proper communication protocols between tiers
- [ ] Workflow discipline maintained throughout all phases

## Implementation Plan
1. Design main agent skill (context detection + project agent spawning)
2. Design project agent skill (workflow management + work agent coordination)
3. Design six specialized work agent skills
4. Implement communication protocols between tiers
5. Test complete workflow execution

## Boundary
- **Touches**: New skill files for main agent, project agent, 6 work agent types
- **Does NOT touch**: Existing workflow-phase files (these guide project agent behavior)