# {Feature Name}

**Opened**: YYYY-MM-DDTHH:MM

**Author**: Claw
**Approved By**: {Human}

**Modified Files**:
- `file.py` (description - done)

**Pending**:
- [ ] Task 1
- [ ] Interface docs updated (`references/interfaces/xxx.md`)

---

## Goal

{One sentence: what this feature achieves and why it matters.}

## User Story

As a {role}, I want {capability}, so that {benefit}.

## Context

{Background, problem being solved, trigger. Link to related ADRs if any.}

---

## Boundary

### System Scope

- **Touches**: {modules, files, APIs affected}
- **Does NOT touch**: {explicitly excluded scope}
- **Depends on**: {preconditions, external services, other features}

### Dependencies

| Dependency | Type | Status |
|------------|------|--------|
| {Module/Service} | Internal/External | ✅ Done / 🟡 In Progress / ❌ Blocked |

## Impact Analysis

**Run before starting implementation**:

```bash
# Find files impacted by changes
python scripts/extract-doc-deps.py --src . --output .doc-graph.json
python scripts/query-doc-deps.py --graph .doc-graph.json --impact {modified_file.md}
```

**Referenced by**:
- {List files that reference the modified files}

**Requires update**:
- [ ] project-types/*.md (if project-init.md or SKILL.md changed)
- [ ] Templates (if core workflow changed)
- [ ] Guides (if referenced)

---

## Contract

> Each item is an acceptance criterion. Phase completion requires ALL items to pass.
> Use Given/When/Then where it aids clarity; plain assertions are acceptable.

### Core Scenarios (must pass)

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}

### Edge Cases

- [ ] {Given ... When ... Then ...}
- [ ] {Given ... When ... Then ...}

### Error Handling

- [ ] {Given ... When ... Then ...}

### Non-Functional (if applicable)

- [ ] {Performance: e.g., "Response time < 100ms for ..."}
- [ ] {Security: e.g., "Input X is sanitized before ..."}
- [ ] {Compatibility: e.g., "Works with Node 18+"}

---

## Interface Contract

> **MUST**: If this change modifies module interfaces, document the interface contract below.

**Modified Interfaces**:
- `file.py:function()` → parameter/return type changes

**Callers**:
- List modules that call this interface

**Invariants**:
- Semantic constraints the interface must satisfy

## Technical Approach

{Brief description of implementation strategy. Keep it concise — the Contract above defines WHAT; this section explains HOW.}

### API Changes (if applicable)

```
POST /api/v1/{endpoint}
Request: {schema}
Response: {schema}
```

---

## Implementation Plan

> Tasks with dependency ordering. Use `→` to indicate sequential deps.

### Phase 1: {name}
1. {Task}
2. {Task}
3. Verify: `{test command}`

### Phase 2: {name} (depends on Phase 1)
1. {Task}
2. Verify: `{test command}`

### Parallel Tasks (subagent-eligible)
- [ ] Documentation updates
- [ ] Test coverage expansion

---

## Test Plan

### Automated Tests

| Category | File/Command | Contract Items Covered |
|----------|-------------|----------------------|
| Unit | `{test file/command}` | Core 1-3 |
| Integration | `{test file/command}` | Edge 1-2 |

### Manual Verification (if needed)

- [ ] {Scenario requiring human verification}

---

## Open Questions

| Question | Status | Resolution |
|----------|--------|------------|
| {Question} | Open / Resolved | {Answer} |

---

## Revision History

| Date | Version | Change | Author |
|------|---------|--------|--------|
| YYYY-MM-DD | 1.0 | Initial draft | Claw |

---

## Close Contract

**Verification**:
- [ ] All Contract items pass
- [ ] Interface docs updated (if interfaces changed)
- [ ] Human confirmed

**Next Session** (for reference):
- **Suggested**: {Phase N+1 or specific task}
- **First Contract**: {suggested topic}
- **Context**: {ADRs or docs to read}

**Archive**: Move to `contracts/archived/`.

---

> **Downgrade path**: If this Contract has ≤ 5 items, no dependency graph, and single-module scope, consider using a Mini-Contract instead (see [mini-contract.md](mini-contract.md)).
