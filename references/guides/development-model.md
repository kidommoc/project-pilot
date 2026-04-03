# Development Model

**Purpose**: Define the relationship between Iteration, Phase, and Contract in project-pilot.

---

## Two-Level Structure

```
L1: Iteration ────────────────────────────────────► Release
     │
     └── L2: Phases
          ├── P1: Contract Definition
          ├── P2: Implementation
          ├── P3: Audit
          └── P4: Release
```

**Contract** is NOT a third level of process—it is the **atomic work unit** within Phases.

---

## Phase and Contract Relationship

| Phase | Contract Role | Output |
|-------|---------------|--------|
| **P1** | Define WHAT to build | Multiple Contracts created → `contracts/open/` |
| **P2** | Execute the work | Contracts move: `open/` → `in_progress/` → `archived/` |
| **P3** | Verify against Contract | Audit; if issues found → create fix Contract → back to P2 |
| **P4** | (No Contracts) | Package and ship |

---

## Key Principles

### 1. Phase Drives Flow, Contract Drives Work
- **Phase** determines the "hat" (Product, Developer, Auditor, Release Engineer)
- **Contract** determines the specific tasks and acceptance criteria

### 2. README as Phase Authority
- Agent reads README first to determine current Phase
- README `## Current Iteration` section tracks Phase state
- Contracts directory reflects work progress within Phase

### 3. One Contract = One Commit
- Each completed Contract results in exactly one git commit
- No commits without a Contract
- Contract archives when commit is made

---

## Session Startup Logic

```
1. Read README.md → Determine Phase
2. Based on Phase:
   ├─ P1 → Continue defining Contracts
   ├─ P2 → Check contracts/open/ and in_progress/ → Continue or start implementation
   ├─ P3 → Perform audit
   ├─ P4 → Prepare release
   └─ Done → Ask for new iteration
```

---

## Contract Lifecycle

```
draft/        → Claw drafts, awaits human confirmation
open/         → Human confirmed, waiting to start
in_progress/  → Current focus (exactly 1 at any time)
archived/     → Completed
```

**Single Focus Constraint**: `in_progress/` must contain exactly 1 Contract.

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-04-03 | Initial definition of two-level structure |
