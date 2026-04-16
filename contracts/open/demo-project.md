# Contract: Demo Project for Project-Pilot v2.0

**Opened**: 2026-04-07T12:27 | **Priority**: high

## Goal
Create a demo project (file-stats CLI tool) with guided walkthrough for users to experience project-pilot's core workflow.

## Problem Statement
Users have no way to quickly experience project-pilot's value. Need a pre-configured demo that lets users walk through the core flow (contract → interface → test → implementation → review) without lengthy setup or design discussions.

## Proposal
Create `demos/file-stats/` under project-pilot with: (1) pre-written design specs simulating completed design phase, (2) project skeleton ready for P1 entry, (3) DEMO.md walkthrough guide telling users what to say and what to expect at each step.

## Acceptance Criteria
- [x] `demos/file-stats/` contains initialized project structure (contracts/, etc.)
- [x] Design specs document present describing scanner/analyzer/formatter modules
- [x] `DEMO.md` walkthrough guide with step-by-step instructions
- [ ] User can start from P1 (contract) by saying "继续项目 file-stats，使用 project-pilot"
- [ ] Each step in DEMO.md describes: user action, expected agent behavior, what to confirm
- [ ] Demo covers full P1→P2→P3→P4 cycle
- [x] Test fixtures directory with sample files for testing file-stats

## Implementation Plan
1. Create `demos/file-stats/` project skeleton (contracts/, src/, tests/)
2. Write design specs document (scanner/analyzer/formatter interfaces)
3. Create test fixtures directory with sample files
4. Write DEMO.md walkthrough guide
5. Update project-pilot README to mention demo

## Boundary
- **Touches**: New `demos/` directory, project-pilot README
- **Does NOT touch**: Agent workspaces, SKILL.md, openclaw.json, existing contracts