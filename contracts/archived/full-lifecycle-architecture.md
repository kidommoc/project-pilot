# Contract: Full Lifecycle Architecture for Project-Pilot

**Opened**: 2026-04-07T03:15 | **Priority**: high

## Goal
Extend three-tier architecture to support complete project lifecycle: init → discussion/design → contract(Phase 1) → implementation(Phase 2) → audit(Phase 3) → release(Phase 4).

## Problem Statement
Current three-tier architecture only covers Phase 1-4. Missing: project initialization for new projects, discussion/design phase before contracts. Need unified architecture covering complete project lifecycle.

## Proposal
Extend architecture with: (1) Rename "project agent" to "iteration agent" focusing on single iteration cycle, (2) Add "init agent" for project setup, (3) Add "design agent" for discussion/design phase, (4) Unified workflow spanning complete lifecycle.

## Acceptance Criteria
- [ ] Iteration agent renamed from project agent (focus on single iteration)
- [ ] Init agent created for new project setup and initialization
- [ ] Design agent created for discussion/design/specification phase
- [ ] Complete lifecycle workflow: init → design → contract → impl → audit → release
- [ ] Main agent can detect lifecycle stage and spawn appropriate agent
- [ ] Work agents remain compatible across all lifecycle stages

## Implementation Plan
1. Rename project-agent to iteration-agent with updated skill
2. Create init-agent for project initialization workflows
3. Create design-agent for discussion/design/specification workflows
4. Update main agent to detect lifecycle stages
5. Integrate all agents into unified workflow

## Boundary
- **Touches**: Renamed iteration-agent, new init-agent, new design-agent, updated main agent
- **Does NOT touch**: Existing work agents (contract, interface, test, impl, review, testing agents remain same)