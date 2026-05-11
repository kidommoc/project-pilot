# Architecture Document Format

One file per project: `docs/knowledge/architecture.md`.

This is the **system-level map** — the top-down view that interface docs don't provide.

## Structure

```markdown
# {project_name} Architecture

## System Dependencies
- PostgreSQL 15 (primary database)
- Redis 7 (session storage, cache)
- SendGrid (email delivery)

## Architecture Overview
- Layered: Frontend → API → Domain → Infrastructure
- Communication: Sync API calls, async events for notifications

## Modules

| Module | Responsibility | Dependencies | File |
|--------|---------------|--------------|------|
| Auth | User authentication, session management | User, Session, Logger | `modules/auth.md` |
| User | User data storage, profile management | DB | `modules/user.md` |
```

## Rules

- **Top-down, not bottom-up** — describe the system's shape, not individual function signatures
- **Keep concise** (~50 lines) — this is a map, not a novel
- **Summary only** — details go in `modules/*.md`
- **Every module** should be listed in the Modules table
- **Design Agent** owns this document; update when modules change
