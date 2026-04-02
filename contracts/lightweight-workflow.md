# Workflow for Project-Pilot Self-Development

**Purpose**: Development workflow for project-pilot itself (ultra-lightweight projects).  
**Version**: 2.0 (2026-03-28)

---

## What

Contract-first workflow for documentation/logic-intensive projects.

### Core Principles

- ✅ Contract-first | ✅ Claw-led progress | ✅ Single focus constraint
- ✅ Human confirmation (contracts) | ✅ State transparency | ✅ Every Contract = One Version

### Positioning

| lightweight-workflow | Full project-pilot workflow |
|---------------------|----------------------------|
| Ultra-lightweight (docs-heavy) | Projects with significant code |
| 2 Phases | 4 Phases |
| Every Contract = Minor bump | SemVer + human-confirmed releases |

---

## How

### Contract State Machine

```
contracts/
├── draft/       ← Awaiting human confirmation
├── open/        ← Confirmed, waiting to start
├── in_progress/ ← Current focus (exactly 1)
└── archived/    ← Completed

Flow: draft → open → in_progress → archived
```

**Single Focus**: `in_progress/` must contain exactly 1 contract.

### Phase Model

**Phase 1: Contract Definition**
1. Human provides goal → Claw drafts → `contracts/draft/`
2. Human confirms → `contracts/open/`
3. Claw updates README (Phase + Contract list) — **No commit yet**

**Phase 2: Implementation**
1. Move to `contracts/in_progress/`
2. Implement + self-review. **DON'T COMMIT NOW**
3. Human confirms → `contracts/archived/`
4. Claw auto-updates:
   - CHANGELOG + Bump Version (minor +1)
5. **Single Git commit**: `Release v{version}: {Contract name}`
6. Git tag: **MUST**

**No branches, no Phase 1 commits.** One contract = One commit.

### Version Management (Simplified)

**Every Contract = One Minor Version**

| Contract | Version | Example |
|----------|---------|---------|
| 1st | v1.0 → v1.1 | State machine refactor |
| 2nd | v1.1 → v1.2 | README scope |
| 3rd | v1.2 → v1.3 | Bug fix |

**Release Checklist** (auto by Claw):
- [ ] Cleanup README (remove `## Current Iteration`)
- [ ] Update CHANGELOG.md
- [ ] Update version
- [ ] Git commit + optional tag

**Git Commit Format**:
```
Release v{version}: {Contract name}

{Optional: 1-2 sentence summary}
```

**Example**:
```
Release v1.2: 升级 lightweight-workflow

整合合同状态机 + README 范围 + 简化版版本管理。
```

**CHANGELOG Format**:
```markdown
## v1.1 (2026-03-28)
- Contract: State machine refactor
  - New directory structure, single focus constraint
```

**No branches. No Phase 1 commits. One contract = One commit.**

### README Scope

**Include** (main branch): Project overview, `Current release: v{X.Y.Z}`, Quick Start, related links  
**Include** (iteration branches): Add `## Current Iteration` with version, phase, contract count  
**Exclude**: Detailed phase tracking, version history (use CHANGELOG.md), contract lists (use contracts/ directory)

**Claw auto-updates README on state changes.**

### Contract Template

```markdown
# Contract: {name}
**Opened**: YYYY-MM-DDTHH:MM | **Priority**: high|medium|low

## Goal
One-sentence objective.

## Problem Statement
Why needed?

## Proposal
Concrete solution.

## Acceptance Criteria
- [ ] Criterion 1

## Implementation Plan
1. Task 1

## Boundary
- **Touches**: Files to modify
- **Does NOT touch**: Files to avoid
```

### Session Recovery

```
1. ls contracts/in_progress/
   - 1 → Read and continue
   - 0 → Select from open/ → Move to in_progress/
   - >1 → 🚨 Error, report to human

2. Find last completed task → Continue from next
```

**Do NOT rely on conversation history.**

### Verification Checklist

- [ ] Markdown valid | [ ] Links valid | [ ] Logic consistent | [ ] No constraint conflicts

---

## Boundary

**Applies To**: project-pilot self-development, SKILL.md/README/templates changes  
**Does NOT Apply To**: Other projects using project-pilot

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 2.0 | 2026-03-28 | Integrated state machine + README scope + simplified versioning |
| 1.0 | 2026-03-27 | Initial version |

---

**Location**: `contracts/lightweight-workflow.md`
