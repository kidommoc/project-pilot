# Interface Documentation Format

One file per module. Stored in the project's `docs/interfaces/` directory (or equivalent).

## Structure

```markdown
# {module_name}

## Overview
One-sentence purpose of this module.

## Layer / Domain
Which architecture layer and domain this module belongs to (must match `docs/architecture.md`).

## Functions

### `function_name(param: type, param: type) -> return_type`
- **Purpose**: One sentence
- **Constraints**: Pre/post-conditions, invariants
- **Errors**: What can fail and when

### `another_function(...) -> ...`
- ...

## Types
- Type definitions, enums, constants used by this module's interface

## Dependencies
- calls → `other_module.func()` — why
- called by ← `caller_module.func()` — context

## History
- YYYY-MM-DD: Change description (Contract: xxx)
```

## Rules

- **Signatures + Constraints + Topology** — that's it
- No implementation details
- Keep entries minimal — one line per function unless constraints are complex
- Update history when modifying existing entries
- If a module is new, create the file; if it exists, update in place
