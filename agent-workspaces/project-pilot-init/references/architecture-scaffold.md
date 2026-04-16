# Architecture Scaffold

Used by Init Worker to create `docs/architecture.md`.

```markdown
# {Project Name} Architecture

## System Overview

{2-3 sentences: what the system does, its primary constraints.}

## Layers / Domains

### {layer_or_domain_name}
- **Purpose**: {one sentence}
- **Contains**: {list of modules — link to docs/interfaces/ when they exist}
- **Communicates with**: {which other layers, and how}
- **Constraints**: {rules this layer must follow}

<!-- Add more layers as the design evolves -->

## Communication Patterns

{How layers talk to each other. Default pattern and exceptions.}

## Design Constraints

{Cross-cutting rules that apply system-wide:}
- {e.g. "Dependencies point inward"}
- {e.g. "All inter-service communication is async via events"}

## History

| Date | Change | Source |
|------|--------|--------|
| {YYYY-MM-DD} | Initial scaffold | Init Worker |
```

## Rules

- For existing projects: fill in what you can detect. Mark uncertain sections with `<!-- TODO -->`.
- For new projects: leave most sections as placeholders. Design Agent fills them in.
- Keep it concise — this is a map, not documentation.
