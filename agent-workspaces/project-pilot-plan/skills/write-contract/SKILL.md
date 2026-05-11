# Write Contract

Write a single contract file from a meta contract. One-shot: read inputs, write one file, done.

No review, no commit.

## Steps

### 1. Read context

Read from the project (prefix with `{project_root}`):

- Meta contract — for context, dependency order
- Each anchor ref in `{project_root}/docs/knowledge/`
- Source spec (if feature) — for design intent and implementation strategy

### 2. Write contract file

Location: `{project_root}/docs/contracts/{feature|fix}/{name}.md`
Template: `references/contract.md` (in pwd's `references/` directory)

Map sections from inputs to template:

| Template Section | Source |
|-----------------|--------|
| Goal | One sentence from meta |
| Boundary > Touches | Meta anchor refs + spec Changes Summary |
| Boundary > Depends on | Dependencies from spawn task |
| Boundary > Reads | Knowledge anchor refs from task |
| Contract (Acceptance Criteria) | Spec PRD section, broken into testable items |
| Tasks > Phase A | TDD — test per interface signatures in anchor refs |
| Tasks > Phase B | Implementation to pass tests |
| Tasks > Phase C | Review gate (delegated) |

### 3. Quality check

Acceptance criteria must be:

- **Testable** — can write a test for it
- **Independent** — one criterion per checkbox
- **Complete** — covers happy path + edge cases + errors

Quick self-check:
- Clear Goal sentence?
- Acceptance criteria testable?
- Anchor refs accurate?

Don't overthink — the contract will be reviewed by review-worker.
