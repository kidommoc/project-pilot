---
name: review_code
description: "Intent verification — validate implementation against spec's business logic topology and Knowledge architecture. Triggered during Implement Agent Phase D review."
---

# Review Code (Intent Verification)

Validate that the implementation correctly fulfills the spec's **intent** — not just the contract's literal acceptance criteria.

This is the primary review gate. It checks whether the code does what the **design intended**, not just whether it passes tests.

## Source → Target

- **Source**: `docs/specs/*.md` (especially business logic topology / mermaid diagrams + implementation strategy + PRD) + `{project_root}/docs/knowledge/` (architecture.md, interfaces/, conventions.md)
- **Target**: Implementation code produced by Coding Worker

## What to Check

### MISS Detection (source requires it, code doesn't have it)

**Business Logic Topology**
- A component/module shown in the spec's topology (mermaid) doesn't exist in code
- A data/control flow edge from the spec diagram is missing — e.g. "module A outputs to module B" but code has no such connection
- The implementation strategy from the spec was not followed (e.g. spec says "use observer pattern", code does polling)

**Architecture Compliance**
- Architecture constraints from Knowledge docs not addressed (e.g. "module X must not depend on module Y" but code has that dependency)
- Module boundaries from architecture.md not respected — code puts logic in the wrong module

**Error Handling**
- Error conditions and failure modes described in the spec are not handled in code
- Edge cases mentioned in spec (especially in PRD section) have no code coverage

### EXTRA Detection (code has it, source doesn't require it)

- Features or behavior outside the contract scope are implemented
- New public APIs not defined in Knowledge interface docs (`docs/knowledge/interfaces/*.md`)
- Dependencies on modules listed in "does NOT touch" (from contract boundary)
- Invented patterns or abstractions that don't appear in the spec's implementation strategy
- Code changes in files outside the contract's declared touches

### ERROR Detection (code contradicts or misrepresents source)

**🔴 Intent Mismatch (FAIL level — blocks the contract)**

- **Business logic topology mismatch**: data/control flow in code contradicts the spec's mermaid diagram
  - Example: spec shows synchronous call chain `A → B → C`, code implements event-driven pub/sub
  - Example: spec shows A calling B, but code has A calling C instead
- **Behavior vs intent**: code behavior doesn't match what the spec described, even if it passes tests
  - Tests may pass but miss the spec's intended behavior
  - Code solves a different problem than spec describes
  - Edge case handling contradicts spec's stated priorities
- **Architecture violation**: module responsibilities or dependency direction violates Knowledge docs
  - A module takes on responsibility that architecture.md assigns elsewhere
  - Dependency direction is reversed (higher-level module depends on lower-level one when it should be the other way)

**🟡 Code Quality Issues (WARN level — flag but don't FAIL alone)**

- Obvious bugs or logic errors in the code
- Unreachable code or dead conditions
- Missing error handling for common failure modes (e.g. null checks, network timeouts)
- Code structure concerns: god functions, excessive nesting, unclear separation of concerns
- Naming that doesn't follow project conventions from conventions.md
- Violations of coding patterns established in the codebase
- Duplicate or redundant code

### ⚪ Already Covered Elsewhere (skip in this review)

- Interface signature correctness (param names, types, return types) → already verified by review-interface (Phase A)
- Test coverage adequacy → already verified by review-tests (Phase B)
- Contract acceptance criteria fulfillment → tests already verify these

## Output

Return the review report as your final output (announce to spawning agent).

Report format:
- Apply the MISS/EXTRA/ERROR taxonomy (matching Review Worker AGENTS.md framework)
- For 🔴 items: explain exactly what in the code deviates from the spec/Knowledge. Use spec section numbers and code file:line references.
- For 🟡 items: list as warnings only, with file:line references where applicable
- Verdict: FAIL if any 🔴 items exist. PASS if only 🟡 warnings.
