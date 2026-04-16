# Contract: Document Integration Into Skills

**Opened**: 2026-04-07T03:57 | **Priority**: high

## Goal
Integrate useful content from legacy documentation into new unified agent skills without removing original files.

## Problem Statement
Legacy documentation contains valuable templates and guidelines that should be accessible within new unified agent skills. Need to incorporate useful content (project init, contracts, naming, etc.) into skills while preserving original files.

## Proposal
Create internal documentation sections within unified project-pilot-agent skill containing: (1) project initialization guidelines from project-init.md, (2) contract templates from contract.md, (3) naming conventions from naming-conventions.md, (4) interface guidelines from interface-contracts, (5) ADR template from adr.md. Keep original files intact.

## Acceptance Criteria
- [ ] Project initialization content integrated into unified agent
- [ ] Contract templates available within agent skill
- [ ] Naming conventions accessible to agent
- [ ] Interface contract guidelines incorporated
- [ ] ADR template available for design phase
- [ ] Original legacy files remain untouched
- [ ] New internal documentation organized by usage context

## Implementation Plan
1. Extract project initialization content from project-init.md into init workflow
2. Incorporate contract templates into design/iteration workflows
3. Add naming conventions to relevant workflows
4. Include interface contract guidelines in appropriate contexts
5. Integrate ADR template for decision-making processes
6. Organize internal documentation with clear usage contexts

## Boundary
- **Touches**: New unified agent skill with internal documentation, workflow attachments
- **Does NOT touch**: Original legacy documentation files in references/ (preserved intact)