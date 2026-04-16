# Contract: Unified Agent Architecture for Project-Pilot

**Opened**: 2026-04-07T03:31 | **Priority**: high

## Goal
Replace multiple specialized agents with single universal agent that adapts behavior based on attached workflow content via attachments.

## Problem Statement
Current architecture creates multiple agent types (init, design, iteration) when single agent could handle all phases via workflow attachments. Need simplified architecture with one agent adapting to different lifecycle phases through injected content.

## Proposal
Create unified "project-pilot-agent" that receives different workflow content via attachments based on lifecycle phase: (1) init workflow, (2) design workflow, (3) iteration workflow (P1-P4). Main agent detects phase and injects appropriate workflow via attachment.

## Acceptance Criteria
- [ ] Single universal agent handles all lifecycle phases
- [ ] Different workflows injected via attachments based on phase
- [ ] Main agent detects lifecycle phase and attaches appropriate workflow
- [ ] All functionality preserved from previous multi-agent approach
- [ ] Simplified architecture with reduced component complexity
- [ ] Work agents remain compatible with unified approach

## Implementation Plan
1. Create unified project-pilot-agent with capability to adapt based on workflow content
2. Prepare different workflow attachments: init, design, iteration (P1-P4)
3. Update main agent to detect phase and attach appropriate workflow
4. Remove redundant specialized agent files
5. Test all lifecycle phases with unified approach

## Boundary
- **Touches**: New unified agent, updated main agent, workflow attachment content
- **Does NOT touch**: Work agents (contract, interface, test, impl, review, testing agents)