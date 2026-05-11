# Domain Model Format

Shared data models used across module boundaries.

## Structure

```markdown
# {ModelName}

{One-sentence purpose of this data model.}

## Fields

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| {field_name} | {type} | {description} | {yes/no} |

## Constraints

- {validation rules, invariants, business rules}

## Usage

- Used by: {list of modules}
- Created in: {which module}
```

## Rules

- **Only shared models go here.** Module-private models stay inline in `modules/*.md`.
- **No implementation details.** Just the data shape and constraints.
