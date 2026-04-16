---
name: write_specs
description: "Write structured spec files from design discussion. Trigger when the human says to write/produce/finalize the spec."
---

# Write Specs

When the design discussion has converged, use this skill to produce spec files.

## Process

1. **Review the conversation** — identify all decisions, constraints, and open items
2. **Organize by feature/component** — one spec file per coherent unit
3. **Write to `docs/specs/`** — use the template below
4. **Confirm with human** — show what you wrote, ask if anything is missing

## Granularity

**One spec = one module/component**, not one feature, not one contract.

- A feature discussion may produce multiple spec files (one per component)
- Each spec typically maps to 1-N contracts (Plan Agent handles the split)
- If a feature is small enough to be a single module, one spec file is fine
- Don't over-split: if two things are tightly coupled, keep them in one spec

## Output Location

```
<project-root>/docs/specs/<module-name>.spec.md
```

## Spec Template

```markdown
# Spec: <Feature Name>

**Created**: YYYY-MM-DDTHH:MM
**Status**: draft
**Design Thread**: <link or reference to thread>

## Summary

One paragraph: what this feature does and why.

## Context & Motivation

Why this feature exists. What problem it solves. What triggered the design.

## Design Decisions

Key decisions made during design discussion, with rationale:

1. **Decision**: <what was decided>
   - **Alternatives considered**: <what else was on the table>
   - **Rationale**: <why this choice>

## Architecture

How the feature fits into the system. Include:
- Component boundaries
- Data flow
- Integration points
- Diagrams (mermaid/ASCII) where helpful

## Behavior

What the feature does, described precisely:
- Core flows
- Edge cases
- Error handling
- State transitions (if applicable)

## Constraints

- Performance requirements
- Security considerations
- Compatibility requirements
- Technical limitations

## Open Questions

Items that surfaced during design but weren't resolved:
- [ ] Question 1
- [ ] Question 2

## Acceptance Signals

How we'll know this feature is correctly implemented (high-level, not test cases):
- Signal 1
- Signal 2
```

## Rules

1. **Don't invent** — only include what was actually discussed and decided
2. **Flag gaps** — if the discussion didn't cover something important, note it in Open Questions
3. **Be precise** — vague specs create vague implementations
4. **Keep it readable** — this document will be read by Plan Agent and Implement Agent
5. **One spec per coherent unit** — don't cram unrelated features into one file
6. **Include context** — future agents reading this spec have zero conversation history

## After Writing

Tell the human:
- What spec file(s) you created
- Any gaps you noticed (Open Questions section)
- That the spec is ready for the Plan Agent to pick up
