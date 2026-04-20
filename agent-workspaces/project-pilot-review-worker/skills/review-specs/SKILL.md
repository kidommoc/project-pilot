---
name: review_specs
description: "Review spec files for completeness, clarity, and internal consistency. Triggered after Design Agent writes a spec."
---

# Review Specs

Validate that spec files are complete, unambiguous, and internally consistent.

**This review has no upstream source document.** Specs are derived from human conversation, which cannot be structurally compared. Instead, use a different defect taxonomy.

## Source → Target

- **Source**: N/A (human intent — not available as a file)
- **Target**: `docs/specs/<module>.spec.md`

## Defect Taxonomy

Unlike other reviews (MISS/EXTRA/ERROR), spec review uses:

| Type | Definition | Example |
|------|-----------|---------|
| **INCOMPLETE** | A required section is missing or too vague to act on | "Constraints" section is empty |
| **AMBIGUOUS** | A requirement could be interpreted multiple ways | "fast response time" — how fast? |
| **INCONSISTENT** | Two parts of the spec contradict each other | Overview says async, but API section shows sync signatures |

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

## Verdict Rules

- **PASS**: No INCOMPLETE, AMBIGUOUS, or INCONSISTENT issues
- **NEEDS-REVISION**: Any issues found → Design Agent should revise

Use standard review report format from AGENTS.md, replacing MISS/EXTRA/ERROR with the taxonomy above.
