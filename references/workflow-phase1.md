# Phase 1: Contract Definition

**Goal**: Define WHAT to build and HOW to verify it.  
**Hat**: Product + Architect

---

## Overview

Phase 1 establishes the plan for the entire iteration:
- Create iteration branch
- Draft 000 Meta-Contract (iteration planning)
- Create child Contracts for each feature/fix
- Move all Contracts to `open/` (ready for Phase 2)

---

## Branch Model

```
main/master              # Stable branch, always at Release state
iteration/v{version}     # Iteration branch, created from main at Phase 1 start
```

**Main branch principle**: Always maintain Release state. No "in-progress" Contract states on main.

---

## 000 Meta-Contract (Iteration Planning)

In the full workflow, Phase 1 begins with the 000 Meta-Contract.

**File naming**: `C-{MAJOR.MINOR.PATCH}-000-meta.md`

**Lifecycle**:
```
Create iteration branch from main
git checkout -b iteration/v{version}

Phase 1 start: 000 created in iteration branch → draft/
After human confirmation: 000 → open/
Start iteration: 000 → in_progress/  ← First commit: contract: meta v{version}
Create child Contracts: 000 guides creation, children flow through open/ → in_progress/ → archived/
Phase 1 end: 000 archived + all child Contracts in open/
```

**000 Contract items**:
- [ ] Define iteration version `{MAJOR.MINOR.PATCH}`
- [ ] Define child Contract list (names, goals)
- [ ] All child Contracts created and in `open/`

**Adding Contracts mid-Phase 1**:
To add new child Contracts, first modify 000 (append to list), get human confirmation, then create new Contracts.

---

## Contract Naming Convention

**File naming**: `C-{MAJOR.MINOR.PATCH}-{No.}-{name}.md`

| Component | Meaning | Example |
|-----------|---------|---------|
| `C` | Contract prefix | Fixed |
| `{MAJOR.MINOR.PATCH}` | Iteration version | `1.5.0` |
| `{No.}` | Contract sequence in iteration, 000 reserved for meta | `000`, `001`, `002` |
| `{name}` | Lowercase hyphenated | `branch-management` |

**Examples**:
- `C-1.5.0-000-meta.md` — Meta-Contract
- `C-1.5.0-001-branch-version.md` — Child Contract 1

---

## Contract Selection

| Criteria | Selection |
|----------|-----------|
| ≤ 8 items, single module, simple deps | **Mini-Contract** ([template](templates/mini-contract.md)) |
| > 8 items, multi-module, architectural impact | **Full Contract** ([template](templates/contract.md)) |

---

## Steps

1. **Create iteration branch**: `git checkout -b iteration/v{version}`
2. **Draft 000 Meta-Contract**: Define version and child Contract list
3. **Semantic pre-review**: Claw self-reviews 000 (see below)
4. Human confirms 000 plan
5. **000 → in_progress/**, **Commit**: `contract: meta v{version}`
6. Create child Contracts per 000 plan
7. Each child: `draft/` → pre-review → human confirm → `open/`
8. **Phase 1 end**: 000 archived + all children in `open/`

---

## Semantic Pre-Review

**Timing**: Immediately after each Contract draft completes.

**Purpose**: Semantic self-check before human review to ensure alignment with original intent.

**Dimensions**:
| Dimension | Check |
|-----------|-------|
| Intent alignment | Does Contract match original purpose? |
| Coverage | Any human requirements missed? |
| Consistency | Conflicts between items? Boundaries clear? |
| Executability | Specific enough to code? |
| Naming | Terms consistent? No ambiguity? |

**Output format**:
```markdown
## Pre-Review Report: {Contract-name}

### ✅ Covered
- {Implemented requirements}

### ⚠️ Potential Gaps
- {Possibly missed requirements}

### ❓ Needs Clarification
- {Ambiguous points}

### Suggestions
- {Optional improvements}
```

**Human decision**:
- Confirm → Contract to `open/`
- Revise → Claw edits, re-review
- Dismiss → Human confirms directly

**Note**: Pre-review supplements human review, does not replace it.

**Claw**: Proposes complete, actionable Contracts with testable criteria  
**Human**: Audits items (edge cases, boundaries), confirms or requests changes

---

## Exit Criteria

- [ ] Iteration branch created (`iteration/v{version}`)
- [ ] 000 Meta-Contract archived (planning complete)
- [ ] All child Contracts created and in `open/`
- [ ] ADRs created (if architectural decisions involved)
