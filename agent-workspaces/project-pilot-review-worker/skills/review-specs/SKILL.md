---
name: review_specs
description: "Review spec files for completeness, clarity, internal consistency, and cross-spec conflicts. Triggered after Design Agent writes a spec."
---

# Review Specs

Validate that spec files are complete, unambiguous, internally consistent, and compatible with related specs.

**This review has no upstream source document.** Specs are derived from human conversation, which cannot be structurally compared. Instead, use a different defect taxonomy.

## Source → Target

- **Source**: N/A (human intent — not available as a file)
- **Target**: `docs/specs/<module>.spec.md`
- **Cross-check**: Related specs (see "Cross-Spec Consistency" below)

## Defect Taxonomy

Unlike other reviews (MISS/EXTRA/ERROR), spec review uses:

| Type | Definition | Example |
|------|-----------|---------|
| **INCOMPLETE** | A required section is missing or too vague to act on | "Constraints" section is empty |
| **AMBIGUOUS** | A requirement could be interpreted multiple ways | "fast response time" — how fast? |
| **INCONSISTENT** | Two parts of the spec contradict each other | Overview says async, but API section shows sync signatures |
| **CONFLICT** | Target spec contradicts a related spec | Spec A says REST, spec B says WebSocket for the same data flow |

## What to Check

### Structural Completeness
- All required sections per spec template are present and non-empty
- Module boundary is clearly defined
- Dependencies on other modules are listed

### Actionability
- Can Plan Agent split this into contracts without guessing?
- Are acceptance criteria specific enough to write tests against?
- Are constraints measurable (not "fast" but "< 200ms")?

### Internal Consistency
- Overview matches detailed sections
- Data flow descriptions match API signatures
- Constraints don't contradict each other
- Naming is consistent throughout

### Scope Clarity
- Clear what is IN scope vs OUT of scope
- No implicit assumptions that should be explicit
- Edge cases and error handling are addressed (or explicitly deferred)

### Cross-Spec Consistency

Check the target spec against **related specs** for contradictions:

**Which specs to read:**
1. All specs symlinked in `workspace/specs/` (same iteration)
2. Specs listed in the target spec's "Dependencies" section (from `docs/specs/`)

**What to look for:**
- Shared interfaces described differently (e.g. REST vs WebSocket, sync vs async)
- Data format mismatches (field names, types, structures)
- Contradictory constraints (e.g. one says "must be stateless", another assumes shared state)
- Overlapping scope (two specs claiming ownership of the same responsibility)

If no related specs exist, skip this section.

## Verdict Rules

- **PASS**: No INCOMPLETE, AMBIGUOUS, INCONSISTENT, or CONFLICT issues
- **NEEDS-REVISION**: Any issues found → Design Agent should revise

Use standard review report format from AGENTS.md, replacing MISS/EXTRA/ERROR with the taxonomy above.
