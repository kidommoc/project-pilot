# Development Workflow

**Contract-First, Acceptance-Driven.**

No code without an approved Contract. Success is defined by Contract items passing, not by code being written.

---

## Contract Close vs Phase Completion

**Two different concepts**:

| Concept | When | What |
|---------|------|------|
| **Contract Close** | Each Contract completes | Verify Contract items, update interface docs, record Next Session |
| **Phase Completion** | All Contracts in Phase complete | Verify all Contracts done, update README, ask human to continue |

---

## 🚨 Contract Close Protocol

**When a Contract completes** (all items implemented and verified):

### Step 1: Verify Contract Items

- [ ] All Contract items pass (Given/When/Then)
- [ ] Tests written and passing
- [ ] Edge cases covered

### Step 2: Update Interface Docs (If Interfaces Changed)

- [ ] Update `references/interfaces/{module}.md`
- [ ] Regenerate dependency graph (if structure changed)

### Step 3: Record Next Session

**Fill in the Contract's "Next Session" section**:

```markdown
## Next Session

**Suggested**: {Next Contract topic or Phase N+1}
**First Contract**: {specific task}
**Context**: {ADRs or docs to read}
```

### Step 4: Human Confirmation

> "Contract '{name}' completed. Next: {suggested task}. Continue?"

**⛔ Wait for confirmation** before starting next Contract.

### Step 5: Archive Contract

- Move to `contracts/archived/`

---

## 🚨 Phase Completion Protocol (MUST-1)

**When all Contracts in a Phase are completed**:

### Step 0: Verify All Contracts Done

- [ ] All Contracts in Phase closed (check `contracts/archived/`)
- [ ] No pending Contracts in `contracts/in_progress/` or `contracts/open/`

### Step 1: Update README.md

```markdown
### Phase N: {phase_name} (✅ Completed - YYYY-MM-DD)

### Phase N+1: {next_phase} (⏳ Pending)
```

### Step 2: Ask User

> "Phase N completed (all Contracts done). Continue to Phase N+1?"

**⛔ Wait for confirmation** before starting Phase N+1.

---

## Phase 1: Contract Definition

**Goal**: Define WHAT to build and HOW to verify it.  
**Hat**: Product + Architect

### Contract Selection

| Criteria | Use |
|----------|-----|
| ≤ 8 contract items, single module, no complex deps | **Mini-Contract** ([template](templates/mini-contract.md)) |
| > 8 items, multi-module, architectural impact, dep graph | **Full Contract** ([template](templates/contract.md)) |

### Steps

1. Human provides high-level goal
2. Claw selects Contract type (Mini or Full) based on scope
3. Claw drafts: Contract + ADRs (if needed)
4. **If interfaces modified**: Include Interface Contract section or separate interface-contract.md
5. Claw presents to human, highlighting Boundary, Contract items, and Interface changes
6. Human confirms OR requests modifications
7. **Contract approved** → Phase 2

**Claw responsibility**: Propose complete, actionable Contract with testable acceptance criteria  
**Human role**: Audit Contract items (especially edge cases and boundaries), confirm or request changes

### Exit Criteria

- [ ] Contract created (Mini or Full, with testable acceptance items)
- [ ] Human approval obtained
- [ ] Dependencies identified
- [ ] ADRs created (if architectural decisions involved)

---

## Phase 2: Implementation

**Goal**: Map Contract to code, execute, and verify each item as you go.

Phase 2 enforces **thinking-stage separation** — same Claw, different hats at each step.

### Step 1: Implementation Brief (Architect Hat)

**Before writing any code**, produce a Contract → Code mapping:

- Each contract item → target file(s), function(s), module(s)
- New interfaces → define signatures first (no implementation yet)
- Execution order → which items have dependencies, which can be parallelized (subagent-eligible)

**Format**: Embed in Contract file (Tasks section) or README. No separate document needed.  
**Scale**: Mini-Contract → 5-10 bullet points. Full Contract → Implementation Plan section.

⛔ **No code before the brief is written.**

### Step 2: Implement + Verify (Developer Hat)

Execute in the order defined by the brief:

- **Per-item verification**: After completing each contract item, immediately verify it passes
- **Interface docs update**: If interface changed, update docs immediately (not after)
- **Regression check**: If verification breaks a previously passing item, fix before continuing
- **Test discipline**: Test-first or test-during. Never test-after.
- **Subagents**: Use for independent tasks (docs, test scaffolding, parallel modules)

📖 **Task decomposition guide**: [guides/session-tasks.md](guides/session-tasks.md)

### Step 3: Self-Check (Tester Hat)

After all items are implemented, switch mindset — **pretend you don't know how the code works**:

- Walk through each contract item, verify it passes independently
- Run full test suite
- Verify interface docs are up to date
- If any item fails → return to Step 2, fix, re-verify

### Exit Criteria

- [ ] Implementation Brief written
- [ ] All Contract items implemented and individually verified
- [ ] Full test suite passing
- [ ] Interface docs updated (if interfaces changed)
- [ ] Contract status updated to "Done"

**Claw responsibility**: Execute plan, maintain quality, verify per item, keep interface docs current  
**Human role**: Available for questions, confirms at Phase end

---

## Phase 3: Audit

**Goal**: Independent audit against the Contract, then deliver to human.  
**Hat**: Auditor (adversarial to the Phase 2 developer)

The Claw in this phase takes an **opposing stance** to its Phase 2 self. The question is not "did I implement it?" but "does it actually satisfy the Contract?"

### Steps

1. **Contract Audit**: Walk each contract item, verify actual behavior matches the criterion
2. **Code quality check**: Lint, naming conventions, documentation
3. **Produce Audit Summary** for human:
   - Contract items: per-item pass/fail
   - Test results
   - Changes summary (files touched, lines changed)
   - Known risks / tech debt
4. Human reviews (depth at human's discretion: spot / full / delegated)
5. Claw addresses feedback (if any)
6. Human confirms

### Audit Checklist

- [ ] All Contract items verified (each one individually checked against actual behavior)
- [ ] Tests pass
- [ ] No lint errors
- [ ] Docs updated
- [ ] ADRs created (if applicable)
- [ ] Naming conventions followed

### Exit Criteria

- [ ] Audit Summary delivered to human
- [ ] Human confirmation obtained
- [ ] Feedback addressed (if any)

**Claw responsibility**: Audit thoroughly from an adversarial perspective, present clearly  
**Human role**: Validate, confirm, or request changes

---

## Phase 4: Release

**Goal**: Package and ship.  
**Hat**: Release Engineer

### Steps

1. Claw updates CHANGELOG.md
2. Claw bumps version (SemVer)
3. Claw creates git tag (`v{version}`)
4. Claw prepares release notes (if external)
5. Claw presents release summary to human
6. Human confirms release

### Version Bumping

| Change | Bump | Example |
|--------|------|---------|
| Breaking | MAJOR | 1.0.0 → 2.0.0 |
| Feature | MINOR | 1.2.0 → 1.3.0 |
| Fix | PATCH | 1.2.3 → 1.2.4 |

### Exit Criteria

- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] Git tag created
- [ ] Human confirmation obtained

**Claw responsibility**: Package correctly, follow SemVer  
**Human role**: Confirm release or request changes

---

## Templates

| Template | Use Case |
|----------|----------|
| [Mini-Contract](templates/mini-contract.md) | Default for most changes |
| [Full Contract](templates/contract.md) | Multi-module, complex features |
| [ADR](templates/adr.md) | Architectural decisions |
| [Naming Conventions](templates/naming-conventions.md) | Reference |

---

**Version**: 0.7.0 | **See also**: [SKILL.md](../SKILL.md), [checklists.md](checklists.md)
