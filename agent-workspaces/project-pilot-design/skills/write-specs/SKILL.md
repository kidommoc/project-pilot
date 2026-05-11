# Write Spec

Read by Design Agent to produce spec files.

## Spec Format

```markdown
# Spec: {Feature Name}

**Date**: {YYYY-MM-DD}
**Design Agent**: {session reference}

### PRD

#### User Stories

- As a {role}, I want {capability}, so that {benefit}.

#### Acceptance Criteria

- {Given/When/Then or plain assertion}

#### Out of Scope

- {What this iteration explicitly does NOT cover}

### Implementation Strategy

#### Technical Decisions

- **Decision**: {what was decided}
  - **Rationale**: {why this choice}
  - **Parameters**: {timeout, limits, retry counts, etc.}

#### Business Logic Topology

Use mermaid codeblock (`flowchart LR`, `sequenceDiagram`, etc) to represent the business logic flow. THIS SHOULD BE MUCH MORE IMPORTANT THAN ANY TEXT DESCRIPTION.

Describe the flow, state transitions, and module interactions. This is the blueprint Review Worker uses in Phase C to verify code matches design intent.

### Changes Summary

**Modules changed**:
- `{module}`: {change description}

**Interfaces changed**:
- `docs/knowledge/interfaces/{name}.md`: {change description}

**Knowledge updated**:
- `modules/{name}.md`: {change description}

**Not changed** (explicitly):
- {module}: {why not applicable}

### Current State Summary

{1-2 paragraphs describing the system state before this iteration. Helps Implement Agent understand baseline without reading full Knowledge.}
```

## Quality Checklist

Check each section against these defects before moving on:

| Defect | Check | Fix |
|--------|-------|-----|
| **INCOMPLETE** | Is every section filled with real content (not placeholders)? | Fill missing sections or explicitly mark deferred items |
| **AMBIGUOUS** | Could any requirement be interpreted multiple ways? Replace "fast", "responsive", "appropriate" with measurable thresholds | Add concrete values |
| **INCONSISTENT** | Do any sections contradict each other? (e.g. overview says sync, topology shows async) | Reconcile |
| **CONFLICT** | Read other specs in `workspace/specs/` — does this spec contradict any existing ones? (e.g. same feature described differently) | Reconcile or flag |

Do NOT skip these checks. Spec quality directly determines impl quality.

## Rules

1. **Don't invent** — only include what was discussed and decided
2. **Flag gaps** — if the discussion didn't cover something important, note it in the spec
3. **Be precise** — vague specs create vague implementations
4. **Kind to agents** — Plan Agent and Implement Agent will read this without conversation history. Include enough context.
5. **Business Logic Topology is the review anchor** — Review Worker compares code against this
6. **Current State Summary is essential** — prevents Implement Agent from guessing
7. **One spec per feature** — don't split a single feature into multiple spec files unless there are clear module boundaries
