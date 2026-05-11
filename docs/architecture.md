# Project Pilot — System Architecture

> *Version 3.0. Single-human + AI-collaboration development workflow.*

---

## Overview

project-pilot manages a software development project through five lifecycle stages: **Init → Design → Plan → Implement → Release**. Each stage is handled by a specialized agent (L1), with sub-agents (L2) for specific work units.

State is derived from the filesystem — no database or in-memory state. `workspace/` contains only symlinks that encode the current stage; `docs/` is the permanent archive.

---

## Agent Hierarchy

```
L0: Main Agent (SKILL.md) — router, single-entry point for human
    │
    ├── L1: Init           — project scaffolding (run, one-shot)
    ├── L1: Design         — feature design via discussion (session)
    ├── L1: Plan           — decompose spec into contracts (run)
    ├── L1: Implement      — execute a single contract (run)
    └── L1: CI/CD          — audit, release, cleanup (run)
            │
            └── L2: Workers — spawned by L1 orchestrators (all run)
                ├── Knowledge Maintainer   — extract Knowledge from confirmed Spec
                ├── Contract Writer        — write one contract file
                ├── Interface Worker       — write interface code from Knowledge docs
                ├── Test Worker            — write RED tests
                ├── Coding Worker          — implement GREEN, self-check
                └── Review Worker          — all review skills (meta, contracts, code, tests, audit)
```

| Layer | Role | Communication | Mode |
|-------|------|---------------|------|
| L0 | Detect stage, route to L1, bridge to human | Standard messages | — |
| L1 | Own a lifecycle stage, spawn L2 workers | Subagent spawn + results | session (Design) / run (others) |
| L2 | Execute one work unit, report back | Announced result | run |

### Session Mode

- **Design Agent**: `mode: "session"` on Discord/Telegram (supports threaded conversations). On non-session channels, Main Agent handles design directly by reading Design Agent's AGENTS.md and following its lifecycle.
- **All other agents**: `mode: "run"` — execute work in a single pass, no ongoing conversation.

---

## Lifecycle

```
             ┌────────────────────────────────┐
    ┌────────┤          START                 │
    │        └────────────┬───────────────────┘
    │                     │
    │                     ▼
    │        ┌────────────────────────┐
    │        │   #1  Init             │  No PROJECT.AGENT.md
    │        │  ─→ core: scaffold     │
    │        │  ─→ output: structure, │
    │        │     PROJECT.AGENT.md,  │
    │        │     Knowledge scaffold  │
    │        └────────────┬───────────┘
    │                     │
    │                     ▼
    │        ┌────────────────────────┐
    │        │   #2  Design           │  New feature requested
    │        │  ─→ discuss with human │
    │        │  ─→ write Spec         │
    │        │  ─→ extract Knowledge  │
    │        │  ─→ commit + symlinks  │
    │        └────────────┬───────────┘
    │                     │
    │                     ▼
    │        ┌────────────────────────┐
    │        │   #3  Plan             │  workspace/specs/ has symlinks
    │        │  ─→ write meta contract│
    │        │  ─→ write contracts    │
    │        │  ─→ review gates       │
    │        │  ─→ symlinks → open/   │
    │        └────────────┬───────────┘
    │                     │
    │        ┌────────────▼───────────┐
    │        │   #4  Implement (×N)   │  open/ has contracts
    │        │  ─→ move to in_progress│
    │        │  ─→ Phase A: Interface │
    │        │  ─→ Phase B: Test RED  │
    │   ┌────│  ─→ Phase C: Impl GREEN│
    │   │    │  ─→ Phase D: Intent    │
    │   │    │     Review             │
    │   │    │  ─→ squash commit      │
    │   │    └────────────┬───────────┘
    │   │          (loop) │
    │   └─────────────────┘  more contracts?
    │                     │  no more
    │                     ▼
    │        ┌────────────────────────┐
    │        │   #5  CI/CD            │  All contracts done
    │        │  ─→ Phase 1: audit     │
    │        │     + release plan     │
    │        │  ─→ human confirm      │
    │        │  ─→ Phase 2: merge,    │
    │        │     tag, clean         │
    └────────┴────────┬───────────────┘
                      │
                      ▼
                  Idle (back to #2)
```

---

## Agent Responsibilities

### L0: Main Agent (SKILL.md)

Reads workspace and symlinks to determine current stage. Never spawns simultaneously running agents — one thing at a time.

| Condition | Stage | Action |
|-----------|-------|--------|
| No `PROJECT.AGENT.md` | Init | Spawn Init Agent |
| `workspace/specs/` empty | Idle | Ask human what to build |
| `workspace/specs/` has symlinks, no `workspace/meta.md` | Plan (meta) | Spawn Plan Agent |
| `workspace/meta.md` exists, `open/` empty | Plan (contracts) | Spawn Plan Agent |
| `in_progress/` has symlink | Implementing | Wait |
| `open/` has symlinks, `in_progress/` empty | Ready | Move symlink, spawn Implement |
| All specs done, no contracts left, no `release-plan.md` | Release Prep | Spawn CI/CD Phase 1 |
| `release-plan.md` exists | Release Exec | Show plan, human decides |

### L1: Init Agent

**Input**: Description, type, language (from human via Main Agent)
**Output**: Directory skeleton, `PROJECT.AGENT.md`, Knowledge scaffolds, `CHANGELOG.md`
**Key rules**: Never overwrite existing files. Detect from filesystem when code exists.

### L1: Design Agent

**Input**: Existing Knowledge, human conversation
**Output**: `docs/specs/YYYY-MM-DD-{name}.md`, updated Knowledge documents, workspace spec symlinks
**Lifecycle**: Discuss → Write Spec → Human confirms → Spawn Knowledge Maintainer → Verify Knowledge → Commit

Knowledge Maintainer extracts Knowledge from the confirmed Spec. Design Agent verifies via `git diff -- docs/knowledge/` that nothing drifted.

### L1: Plan Agent

**Input**: Spec from `workspace/specs/`
**Output**: Meta contract + individual contracts (review gates between each phase)
**Lifecycle**: 
- Bugfix (no spec): Write a single fix-contract → review → commit
- Meta: Read specs → draft meta contract → review → human confirms → commit symlink
- Contracts: Per-contract spawn Contract Writer → review gates → symlinks → commit

### L1: Implement Agent

**Input**: A single contract from `workspace/contracts/in_progress/`
**Output**: Interface code + Tests + Implementation, all squashed into one commit
**Lifecycle**: 
- Phase A: Interface Worker writes interface code → Review Gate
- Phase B: Test Worker writes RED tests → Review Gate
- Phase C: Coding Worker implements to GREEN
- Phase D: Review Worker does intent verification
- Final: Squash all work into one `impl:` commit, delete in_progress symlink

### L1: CI/CD Agent

**Input**: All completed contracts, codebase
**Output**: Release (merge + tag + clean workspace)
**Phase 1**: Audit (run review-audit), create `release-plan.md` with PASS/FAIL
**Phase 2**: Human confirms → merge iteration branch to main, tag version, update roadmap, clean workspace

---

## Knowledge Architecture

### Three Layers

| Layer | Purpose | Content | Written By |
|-------|---------|---------|------------|
| **Journeys** | Human view — features & scenarios | Feature index + user stories + module mapping | Design Agent (discussion) |
| **Modules** | Agent view — system structure | Responsibilities, constraints, dependencies, private domain models | Knowledge Maintainer |
| **Interfaces** | Contracts — boundaries between modules | DTO signatures, input/output, errors, examples | Knowledge Maintainer |

### Seven Document Types

```
docs/knowledge/
├── journey-map.md         # Feature index (navigation entry point)
├── journeys/              # Human feature stories + system module mapping
├── architecture.md        # System map: dependencies, module summary table
├── modules/               # Module details (responsibility, constraints, deps)
├── domain-models/         # Shared data models (one file per model)
├── interfaces/            # Interface contracts (DTO signatures only)
└── conventions.md         # Cross-module architectural conventions
```

### Write Order (Knowledge Maintainer)

1. `journey-map.md` — add new journey entry
2. `journeys/{name}.md` — write new journey
3. `architecture.md` — update system map
4. `modules/{name}.md` — update/create modules
5. `domain-models/{name}.md` — update/create shared models
6. `interfaces/{name}.md` — define interface signatures
7. `conventions.md` — update cross-module conventions

After extraction, Knowledge Maintainer appends a `Knowledge Ref` section to the Spec file listing what was created/updated — this feeds Plan Agent's anchor references.

### What vs How

| Content | Knowledge | Spec |
|---------|-----------|------|
| Module constraints | ✅ | ❌ |
| Interface signatures | ✅ | ❌ |
| Business rules (stable) | ✅ | ❌ |
| Implementation strategy | ❌ | ✅ |
| Business logic topology | ❌ | ✅ |
| Technical decisions | ❌ | ✅ |

---

## Workspace State Machine

The `workspace/` directory contains symlinks only — it's a lightweight state encoding.

| State | What's in workspace/ |
|-------|---------------------|
| Idle | Empty |
| Design done | `specs/{name}.md` → `docs/specs/{name}.md` |
| Plan done | `meta.md` → `docs/contracts/meta-{iteration}.md` + `contracts/open/{name}.md` → `docs/contracts/feature/{name}.md` |
| Implementing | `contracts/in_progress/{name}.md` → (globally unique) |
| Release Prep | `release-plan.md` |
| Complete | Empty again |

**Key rules**:
- Symlink in `in_progress/` is globally unique — only one contract at a time
- Deleting a symlink completes the contract; the original stays in `docs/` (Git archive)
- CI/CD cleanup clears all workspace symlinks → returns to Idle

### PROJECT.AGENT.md

The project-roots `PROJECT.AGENT.md` acts as the agent instruction file (similar to Claude Code's `CLAUDE.md`). All agents read it on startup.

- **Instructions**: Positive rules — build, test, run commands, coding conventions
- **Boundaries**: Negative rules — what agents must NOT do
- **Maintenance**: Any agent may append new entries (never modify existing). Human consolidates periodically. No single agent owns it.

---

## Review System

Review gates are mandatory checkpoints. Each has a specific skill:

| Skill | Verifies | Against | At Stage |
|-------|----------|---------|----------|
| `review-meta` | Meta contract | Spec + consistency | Plan (meta phase) |
| `review-contracts` | Individual contracts | Meta + Knowledge | Plan (contracts phase) |
| `review-interface` | Interface code | Knowledge docs + contract | Implement Phase A |
| `review-tests` | Tests | Knowledge docs + contract | Implement Phase B |
| `review-code` | Implementation | Spec + Knowledge + contract | Implement Phase D |
| `review-audit` | Full codebase | All contracts | CI/CD Phase 1 |

**Defect classification** (for reviews with upstream source):
- **MISS** — source says it, output doesn't
- **EXTRA** — source doesn't say it, output added it
- **ERROR** — output contradicts source

**Defect classification** (for spec — no upstream source):
- **INCOMPLETE** — missing or too vague
- **AMBIGUOUS** — multiple interpretations
- **INCONSISTENT** — self-contradiction

All review skills output via **announce** (returned to spawner as result), not written to files.

---

## Path Convention

All agents use two path variables:

- `{project_root}` — the project's root directory (passed as spawn parameter)
- `{your_workspace}` — the agent's own workspace (their pwd)

Spawn parameters use `{project_root}/` prefix for project files. Agent workspace paths are relative to `{your_workspace}`.

---

## Git Workflow

- **Branches**: `main` (stable) + `iteration/v{version}` (active work)
- **Branch creation**: Plan Agent creates iteration branch from main
- **Commits**: Plan Agent commits meta + contracts; Implement Agent squashes all phase work into one `impl:` commit
- **Commit author**: `Openclaw <claw@openclaw.local>`
- **Finish**: CI/CD merges iteration branch into main (squash), tags version
- **Git proxy**: `http.proxy=http://localhost:1081` (configured globally)

---

## Key Design Principles

1. **State from filesystem** — no database, no in-memory state. Symlinks = current stage.
2. **Knowledge ≠ Spec** — Knowledge is "what" (stable constraints, interfaces). Spec is "how" (iteration-specific design).
3. **One in_progress at a time** — globally unique active contract. No parallelism.
4. **Review gates are mandatory** — never self-review. Always spawn Review Worker.
5. **All workers are named** — anonymous subagents inherit parent AGENTS.md, causing role confusion.
6. **Skill routing via spawn task** — Review Worker reads `Read skills/{skill-name}/SKILL.md and follow it` from the spawn task, not from a registry.
7. **Append-only PROJECT.AGENT.md** — any agent can add, never modify existing, human consolidates.
