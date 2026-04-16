# Init Worker

You initialize a new project for use with project-pilot.
Spawned by Main Agent (SKILL.md) when `PROJECT.AGENT.md` does not exist.

## Input

- Project directory path (cwd)
- Optional: user-provided project description or intent

## Steps

### 1. Detect Project Context

If the project directory already has code:
- Detect language/framework (package.json, pyproject.toml, go.mod, etc.)
- Detect existing conventions (naming, directory structure, patterns)
- Detect existing docs, tests, CI config

If the project directory is empty:
- Ask the user: What is this project? Language/framework? Purpose?

### 2. Create Directory Structure

```
{project}/
├── docs/
│   ├── roadmap.md              # Checkbox list of current items
│   ├── architecture.md         # System architecture (scaffold, Design Agent fills)
│   ├── specs/                  # Design specs (YYYY-MM-DD-{name}.md)
│   ├── contracts/              # Permanent contract storage
│   │   ├── feature/            # Minor iteration contracts
│   │   └── fix/                # Patch fix contracts
│   └── interfaces/             # Interface documentation
├── workspace/                  # Working state (symlinks only)
│   └── contracts/
│       ├── open/               # Symlinks to pending contracts
│       └── in_progress/        # Symlink to active contract (exactly 1)
├── PROJECT.AGENT.md            # Project-level context (from template)
├── CHANGELOG.md
└── README.md                   # If not exists
```

**Key rules:**
- `docs/contracts/` holds the actual files — permanent, never deleted
- `workspace/contracts/` holds symlinks only — state changes = move/delete symlinks
- `workspace/current-spec.md` symlink is created later by Design Agent, not init
- Do NOT overwrite existing files. Only create what's missing.

### 3. Initialize docs/roadmap.md

```markdown
# Roadmap

## Current

- [ ] {First item — fill from user input or leave placeholder}
```

### 4. Scaffold docs/architecture.md

```markdown
# {Project Name} Architecture

## System Overview

{2-3 sentences: what the system does, its primary constraints.}

## Layers / Domains

<!-- Design Agent will fill this in during the first design phase -->

## Design Constraints

<!-- Cross-cutting rules that apply system-wide -->

## History

| Date | Change | Source |
|------|--------|--------|
| {today} | Initial scaffold | Init Worker |
```

For existing projects: fill in what you can detect. Mark uncertain sections with `<!-- TODO -->`.
For new projects: leave as placeholder. Design Agent fills it in.

### 5. Generate PROJECT.AGENT.md

This is the project-level context file that all agents and workers read.

Contents:
- **Project overview**: one-sentence purpose
- **Tech stack**: language, framework, key dependencies
- **Conventions**: naming (files, functions, variables), directory structure patterns
- **Testing**: framework, file naming, run command
- **Build/Run**: how to build, run, deploy

Use `references/project-agent-template.md` as the base.

For existing projects: derive conventions from actual code. Don't invent conventions that contradict what's already there.

For new projects: use language-idiomatic defaults. Keep it minimal — conventions will evolve.

### 6. Project-Type-Specific Init

Detect or ask project type, then apply type-specific initialization.
See `references/project-types/` for type templates.

**Prefer external tooling when available:**
- Node.js/Web → `npm create vite@latest`, `npx create-next-app`, etc.
- Python → `poetry new`, `uv init`
- Rust → `cargo init`
- Go → `go mod init`

After external tool runs, supplement with project-pilot structure (docs/, workspace/, etc.).

If external tools aren't applicable or project already has code, skip this step.

### 7. Initialize CHANGELOG.md

```markdown
# Changelog

## [Unreleased]

### Added
- Project initialized with project-pilot
```

### 8. Report

Tell the user what you created/detected. List any decisions you made and why.
Wait for human confirmation before Main Agent proceeds.

## Rules

- **Don't overwrite** existing files — append or skip
- **Don't make design decisions** — you're scaffolding, not designing
- **Match existing style** — if the project uses kebab-case, don't introduce camelCase
- **Keep it minimal** — better to scaffold less and let Design Agent fill in more later
- **Symlinks are state** — `workspace/` is the working view, `docs/` is the permanent store
