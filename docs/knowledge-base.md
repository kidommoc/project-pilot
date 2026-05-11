# Knowledge Base — System Context

> *The project's permanent system description, maintained by Design Agent.*

---

## Core Insight

**Humans think in features. Agents think in modules.** The knowledge base bridges this gap with three layers:

| Layer | Perspective | Purpose | Example |
|-------|-------------|---------|---------|
| **Journeys** | Human | Feature index + user scenarios | "User logs in with Google" |
| **Modules** | Agent | System structure + constraints | "Auth handles login, cannot access DB directly" |
| **Interfaces** | Contract | Boundary signatures | `login(credentials) -> token` |

---

## What vs How

The most important boundary in the system.

| Content | Knowledge | Location |
|---------|-----------|----------|
| Module constraints ("Auth cannot access DB directly") | ✅ | `modules/{name}.md` |
| Interface signatures (`login() -> token`) | ✅ | `interfaces/{name}.md` |
| Business rules ("OAuth users cannot change password") | ✅ | `modules/{name}.md` (constraints) |
| Implementation strategy ("Use Redis for blacklist") | ❌ | Spec (per-iteration) |
| Business logic topology (flow diagrams) | ❌ | Spec (per-iteration) |
| Technical decisions ("JWT with HS256, 7-day expiry") | ❌ | Spec (per-iteration) |
| Code-level details | ❌ | Code |

**Knowledge = "What exists" + "What you can get".** Constraints, contracts, functional summary.
**Knowledge ≠ "How it works".** That's in Spec or Code.

---

## Directory Structure

```
docs/knowledge/
├── journey-map.md         # Feature index (navigation entry point)
├── journeys/              # User stories + system module mapping
├── architecture.md        # System map: dependencies, module summary
├── modules/               # Module specs (responsibility, constraints, deps)
├── domain-models/         # Shared data models (one file per model)
├── interfaces/            # Interface contracts (DTO signatures only)
└── conventions.md         # Cross-module architectural conventions
```

---

## Document Types

### journey-map.md — Feature Index

```markdown
# Journey Map

| Journey | Description | File |
|---------|-------------|------|
| User Login | User logs in with credentials | `journeys/user-login.md` |
| Place Order | User places an order | `journeys/place-order.md` |
```

Navigation entry point. Agent reads this when human mentions a feature → finds the journey file.

### journeys/{name}.md — Feature Stories

Each file contains:
- **Human View**: User journey in plain language
- **System View**: Module interaction mapping (mermaid preferred)
- **Participating Modules**: Which modules are involved

Journeys are the **alignment contract** between human and agent. Written during design discussion (human validates the flow), not extracted from Spec.

### architecture.md — System Map

```markdown
# System Architecture

## System Dependencies
- PostgreSQL 15 (primary database)
- Redis 7 (session storage)

## Architecture Overview
- Layered: Frontend → API → Domain → Infrastructure

## Modules

| Module | Responsibility | Dependencies | File |
|--------|---------------|--------------|------|
| Auth | User auth, session mgmt | User, Session | `modules/auth.md` |
```

Concise (~50 lines). Summary only — details in modules.

### modules/{name}.md — Module Specs

Contains:
- **Responsibility**: What the module does
- **Non-Responsibility**: What it does NOT do (explicit exclusions)
- **Constraints**: Boundaries it must respect
- **Private Domain Models**: Data models owned by this module only
- **Shared Domain Models**: References to domain-models/
- **Interfaces**: References to interfaces/
- **Dependencies**: Other modules it depends on

### domain-models/{name}.md — Shared Models

One file per model, for models used by multiple modules.

```markdown
# User Domain Model

{
  user_id: str (UUID)
  email: str (unique, validated)
  username: str (unique, 3-32 chars)
}

## Usage
- Auth Module: authentication
- Order Module: order ownership
```

### interfaces/{name}.md — Interface Contracts

DTO signatures only. Enables parallel development.

```markdown
## Auth Interfaces

### login(credentials) -> token

**Input:**
credentials: { username: str, password: str }

**Output:**
token: str (JWT format)

**Errors:**
- AuthError.invalid_credentials
- AuthError.account_locked

**Example:**
```python
token = auth.login({"username": "user", "password": "pass"})
```
```

### conventions.md — Cross-Module Conventions

```markdown
## Error Handling
- All API errors use unified format: `{error: {code, message, details}}`

## Naming
- snake_case for files, PascalCase for classes, camelCase for functions
```

Only cross-module rules. Single-module conventions go in that module's file.

---

## Write Order (Knowledge Maintainer)

Always follows this sequence. Each step builds on context from the previous.

1. **journey-map.md** — add/reorder journey entries
2. **journeys/{name}.md** — write new journey
3. **architecture.md** — update system map if modules/layers change
4. **modules/{name}.md** — update/create modules
5. **domain-models/{name}.md** — update/create shared models
6. **interfaces/{name}.md** — define interface signatures (needs module context)
7. **conventions.md** — update cross-module conventions (needs full picture of all changes)

---

## Content Boundaries

| What | Where | Why |
|------|-------|-----|
| System dependencies | `architecture.md` | Overview information |
| Module responsibilities | `modules/{name}.md` | Per-module detail |
| Private domain models | `modules/{name}.md` | Not shared |
| Shared domain models | `domain-models/{name}.md` | Referenced by multiple modules |
| Interface signatures | `interfaces/{name}.md` | Contract boundary |
| Business rules (stable) | `modules/{name}.md` | Constraints section |
| Implementation strategy | Spec | Per-iteration, not permanent |
| Tech stack | PROJECT.AGENT.md or README.md | Not architecture |
| Agent instructions | PROJECT.AGENT.md | Not Knowledge |

---

## Navigation Flow

### Feature lookup
```
Human: "Modify login"
  → Agent reads journey-map.md
  → Finds journeys/user-login.md
  → Reads human view + system module mapping
  → Reads modules/auth.md, interfaces/auth.md
```

### New feature
```
Human: "Add OAuth"
  → Agent reads journey-map.md (not found)
  → Asks human: "New feature?"
  → Reads similar journey as reference
  → Writes Spec → human confirms → updates Knowledge
```

### Module lookup
```
Human: "Modify Auth module"
  → Agent reads architecture.md
  → Finds modules/auth.md
  → Reads module details + interfaces/auth.md
```

---

## Update Strategy

| Document | Updated When | Reason |
|----------|-------------|--------|
| `interfaces/`, `architecture.md`, `modules/`, `domain-models/` | Immediately after design confirmed | These guide implementation |
| `journeys/`, `journey-map.md` | At design time (with human) | Journey = alignment contract |
| `conventions.md` | During design, when cross-module patterns emerge | Written by Knowledge Maintainer in step 7 |

No Status markers needed. Git diff tracks what changed between iterations.
