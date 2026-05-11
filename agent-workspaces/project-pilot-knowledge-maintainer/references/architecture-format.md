# Architecture Format

## Structure

```markdown
# {Project Name} Architecture

## System Overview

{2-3 sentences: what the system does, its primary constraints.}

## Layers / Domains

### {layer_or_domain_name}
- **Purpose**: {one sentence}
- **Contains**: {list of modules}
- **Communicates with**: {which other layers, and how}
- **Constraints**: {rules this layer must follow}

## Communication Patterns

{How layers talk to each other. Default pattern and exceptions.}

## Design Constraints

{Cross-cutting rules that apply system-wide:}
- {e.g. "Dependencies point inward"}
- {e.g. "All inter-service communication is async via events"}

## History

| Date | Change | Source |
|------|--------|--------|
| {YYYY-MM-DD} | Initial scaffold | Knowledge Maintainer |
```
