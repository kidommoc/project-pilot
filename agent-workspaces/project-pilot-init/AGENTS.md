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

### 2. Ensure Git Repository

If no `.git` directory exists in the project root, run `git init`.
This ensures branch management (iteration branches, tags) works from the start.

### 3. Create Directory Structure

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
│   ├── specs/                  # Symlinks to active specs (Design Agent creates)
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
- `workspace/specs/` holds symlinks to active specs — created by Design Agent, cleaned by CI/CD Agent
- Do NOT overwrite existing files. Only create what's missing.

### 4. Initialize docs/roadmap.md

```markdown
# Roadmap

## Current

- [ ] {First item — fill from user input or leave placeholder}
```

### 5. Scaffold docs/architecture.md

Use `references/architecture-scaffold.md` as the template.

For existing projects: fill in what you can detect. Mark uncertain sections with `<!-- TODO -->`.
For new projects: leave as placeholder. Design Agent fills it in.

### 6. Generate PROJECT.AGENT.md

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

### 7. Project-Type-Specific Init

**Step 1: Detect type** from filesystem or ask user.

**Step 2: Read the corresponding template file** from `references/project-types/`:

| Type | Template File | External Tool |
|------|---------------|---------------|
| OpenClaw Plugin | `references/project-types/openclaw-plugin.md` | Manual |
| CLI Tool | `references/project-types/cli-tool.md` | Manual |
| Python Package | `references/project-types/python-package.md` | `poetry new`, `uv init` |
| Web App | `references/project-types/web-app.md` | `npm create vite@latest`, etc. |

**Step 3: Follow the template exactly.** The template defines:
- Directory structure to create
- Special files (e.g., `openclaw.plugin.json` for plugins)
- Deployment steps

**Do NOT improvise the structure.** Read the template file and follow it precisely.

If the type is not in the table, use the generic structure from Step 3 and skip this step.

### 8. Initialize CHANGELOG.md

```markdown
# Changelog

## [Unreleased]

### Added
- Project initialized with project-pilot
```

### 9. Report

Tell the user what you created/detected. List any decisions you made and why.
Wait for human confirmation before Main Agent proceeds.

## Rules

- **Don't overwrite** existing files — append or skip
- **Don't make design decisions** — you're scaffolding, not designing
- **Match existing style** — if the project uses kebab-case, don't introduce camelCase
- **Keep it minimal** — better to scaffold less and let Design Agent fill in more later
- **Symlinks are state** — `workspace/` is the working view, `docs/` is the permanent store
