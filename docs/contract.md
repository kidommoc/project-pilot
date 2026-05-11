# Contract — Task Breakdown

> *The actionable work unit. One contract = one squashed commit.*

---

## Core Principle: Minimal Anchor References + Agent Navigation

Contracts reference only 3-5 core files (the anchors agents need to start work). Agents are expected to explore the Knowledge base on demand — an exhaustive file list would bloat the contract, break on file moves, and reduce agent flexibility.

---

## Structure

Two types: **Meta Contract** (iteration index) + **Individual Contracts** (work units).

```
docs/contracts/
├── meta-{iteration}.md      # Iteration overview: contract list + Knowledge refs
├── feature/                 # Minor iteration contracts
│   └── {name}.contract.md
└── fix/                     # Patch fix contracts
    └── {name}.contract.md
```

---

## Meta Contract

```markdown
# Meta Contract: {iteration-name}

**Iteration Spec**: `docs/specs/{date}-{name}.md`

## Knowledge Files (updated in this iteration)

| File | Type |
|------|------|
| `interfaces/auth.md` | updated |
| `modules/auth.md` | created |

## Contract Index

| # | Name | Anchor Refs |
|---|------|-------------|
| 1 | user-auth | `interfaces/auth.md`, `modules/auth.md` |
| 2 | billing-api | `interfaces/billing.md`, `modules/billing.md` |
```

**Purpose**: Gives Plan Agent and human an overview. The Contract Index drives per-contract spawns. Anchor Refs are gathered from the Metadata Ref section of the Spec.

---

## Individual Contract

```markdown
# {Name}

**Opened**: {date}
**Source Spec**: `docs/specs/{name}.md` (Section: {section})
**Anchor Refs**: `interfaces/{name}.md` | `modules/{name}.md`

## Goal

{One sentence — what this contract achieves.}

## Boundary

- **Touches**: {modules this contract modifies}
- **Does NOT touch**: {excluded scope}
- **Depends on**: {preconditions — other contracts, deploy state}
- **Reads**:
  - `docs/knowledge/interfaces/{name}.md` — signatures to implement
  - `docs/knowledge/modules/{name}.md` — constraints to respect
  - `docs/specs/{date}-{name}.md` — design intent (section)

## Contract (Acceptance Criteria)

- [ ] {Checklist of what "done" means}
- [ ] ...

## Tasks

### Phase A: Interface Code ⛔
- [ ] Write interface code per `docs/knowledge/interfaces/`
- [ ] Review Worker PASS

### Phase B: Test (RED) ⛔
- [ ] Write failing tests per interfaces
- [ ] Run tests, confirm RED
- [ ] Review Worker PASS

### Phase C: Impl (GREEN)
- [ ] Implement to pass all tests
- [ ] Run tests, confirm GREEN

### Phase D: Intent Review ⛔
- [ ] Review Worker PASS (intent verification + code quality)
- [ ] If fail → back to Phase C with review report

## Close

- [ ] Squash commit: `git commit -m "impl: {contract-name}"`
- [ ] Delete in_progress symlink
```

### Key Fields

| Field | Purpose |
|-------|---------|
| **Source Spec** | Links back to the design document (with section for large specs) |
| **Anchor Refs** | 3-5 core files the worker must read |
| **Goal** | One sentence — prevents scope creep |
| **Boundary → Touches** | What the contract affects |
| **Boundary → Does NOT touch** | Explicit exclusions |
| **Boundary → Depends on** | Preconditions |
| **Boundary → Reads** | Files the worker reads on startup |
| **Contract** | Acceptance criteria checklist (what "done" means) |
| **Tasks** | Phase-by-phase execution steps with checkboxes |

### Checkbox Tracking

The Implement Agent updates checkboxes as each phase passes (`- [ ]` → `- [x]`). This provides visibility into progress without an external tracker.

---

## Anchor Reference Strategy

**Rule of thumb: 3-5 files max.**

| Role | Files to Reference |
|------|-------------------|
| Interface code | `interfaces/{name}.md` + contract boundary |
| Test | `interfaces/{name}.md` + contract + spec section |
| Implementation | Contract + spec section + Knowledge files on demand |
| Intent review | Spec + contract + Knowledge |

Workers are not limited to anchor refs. They may explore Knowledge or read additional specs. The anchors just ensure they start in the right place.

---

## Contract Sizing

| Too Small | Too Large | Just Right |
|-----------|-----------|------------|
| One function | One iteration's worth | 1-2 days of work |
| One file | Crosses 3+ unrelated modules | 3-5 files, one coherent change |
| Pure refactor | Mixed concern (add feature + refactor + fix bug) | Single logical change |

Signs of too-large contracts: hard to write acceptance criteria for, hard to review, hard to squash-commit.

---

## Bugfix Contract (Patch)

For Patch iterations (no spec):

```markdown
# Fix: {bug-description}

**Type**: fix/
**Opened**: {date}

## Bug

{What's broken, how to reproduce.}

## Expected

{What should happen instead.}

## Fix

- [ ] {Checklist of what to change}
- [ ] Test the fix
```

Bugfix contracts skip the Phase structure — Implement Agent writes test, fixes code, and commits directly.

---

## Lifecycle

```
Plan Agent reads Spec
  → Determines iteration version
  → Creates iteration branch from main
  → Writes Meta Contract
  → Review Gate (meta)
  → Human confirms
  → Per-contract spawn Contract Writer
  → Review Gate (all contracts)
  → Human confirms
  → Create symlinks in workspace/contracts/open/
  → Commit iteration branch
```

After symlinks are in `open/`, the Main Agent picks up from the Ready state.
