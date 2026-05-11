# Conventions Format

Cross-module conventions that multiple modules must follow.

## Structure

```markdown
# Conventions

## {Convention Name}

**Scope**: {which modules this applies to}
**Type**: {naming / error handling / logging / testing / etc}

### Rule

{Describe the convention clearly. Include examples where helpful.}

### Rationale

{Why this convention exists — helps agents understand when to deviate.}
```

## Rules

- **Only cross-module conventions.** Single-module conventions go in that module's file.
- **Avoid collecting things that don't belong together.** Each convention should be standalone.
- **Delete outdated conventions.** Don't accumulate cruft.
