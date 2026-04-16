# Architecture Document Format

One file per project: `docs/architecture.md`.

This is the **system-level map** — the top-down view that interface docs don't provide.

## Structure

```markdown
# {project_name} Architecture

## System Overview
2-3 sentences: what the system does, its primary constraints.

## Layers / Domains

### {layer_or_domain_name}
- **Purpose**: One sentence
- **Contains**: List of modules (link to interface docs)
- **Communicates with**: Which other layers, and how (direct call, event, message queue, HTTP, etc.)
- **Constraints**: Rules this layer must follow (e.g. "no direct DB access", "stateless")

### {another_layer}
- ...

## Communication Patterns
How layers talk to each other. Call out the default pattern and any exceptions.

## Design Constraints
Cross-cutting rules that apply system-wide:
- Naming conventions
- Error handling strategy
- Dependency direction (e.g. "dependencies point inward")

## History
- YYYY-MM-DD: Change description (Spec: xxx)
```

## Rules

- **Top-down, not bottom-up** — describe the system's shape, not individual function signatures
- Keep it concise — this is a map, not a novel
- Every module in `docs/interfaces/` should be traceable to a layer/domain listed here
- Update history when the architecture changes
- Design Agent owns this document; Interface Worker references it but doesn't modify it
