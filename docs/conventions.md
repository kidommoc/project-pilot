# Project Pilot — Internal Conventions

> *Cross-module conventions that all project-pilot agents and workers follow.*

---

## Path Convention

**Two-variable system** used in every AGENTS.md and spawn task:

| Variable | Meaning | Example |
|----------|---------|---------|
| `{project_root}` | Project root directory (passed as spawn parameter) | `/home/user/project` |
| `{your_workspace}` | Agent's own workspace (their pwd) | `/app/agents/.../project-pilot-design` |

**Rules:**
- Spawn parameters use `{project_root}/` prefix for project files
- Agent references use relative paths from `{your_workspace}`
- Never hardcode absolute paths
- Symlink commands use `cd {project_root} && ln -s <relative-path> <target>`

---

## Agent Workspace Layout

All agent workspaces follow this structure:

```
agent-workspaces/{agent-name}/
├── AGENTS.md             # Agent definition (lifecycle, responsibilities, boundaries)
├── TOOLS.md              # Agent-specific tool notes (optional)
├── references/           # Templates, format guides, scaffolds
│   ├── {template-name}.md
│   └── project-types/    # (Init Agent only) Per-project-type templates
└── skills/               # Skills this agent can execute
    └── {skill-name}/
        └── SKILL.md
```

**Rules:**
- `references/` contains templates and format guides — read-only by the agent
- `skills/` contains executable skills — kill files that the agent follows step-by-step
- Shared templates use symlinks: `ln -s ../../{source-agent}/references/{file}.md references/{file}.md`

---

## AGENTS.md Format

Every AGENTS.md should include:

```markdown
# {Agent Name}

{Purpose — one paragraph.}

## Path Convention

{project_root} and {your_workspace} definitions.

### Step 0: Read PROJECT.AGENT.md

Read, follow, and contribute.

---
{Lifecycle}
---
{Boundaries}
---
{Failure Handling} (optional)
```

### Step 0 Is Mandatory

Every agent must read `PROJECT.AGENT.md` on startup. The exact text:

```markdown
### Step 0: Read PROJECT.AGENT.md

Read `{project_root}/PROJECT.AGENT.md` for project-level instructions and boundaries.
Follow any rules specified there.
```

---

## Preflight Check

Every agent must perform a Preflight check before starting work.
This catches environment/precondition failures early and returns a clean FAILED status.

```markdown
### Preflight

Before starting work, check required conditions:
- `{project_root}` exists and is accessible
- Input files from spawn task are readable
- Required tools/commands are available
- Any preconditions listed in this file

If any check fails → end with Status: FAILED and describe what is missing.
```

**L2 workers** add agent-specific checks (e.g. Test Worker checks test framework installation).
The Preflight section lives after Step 0 in each AGENTS.md.

---

## Result Protocol

Every spawned agent ends with a structured Result block. L0 reads it to decide next action.

```markdown
## Result
**Status**: DONE | FAILED
**Summary**: {1-2 sentences}
**Human Confirmation**: {question for human, or empty}
**Next**: {what L0 should do next, or empty}
**Details**: {files changed, review outcomes, etc.}
```

### L0 Behavior

| Status | Human Confirmation | L0 Action |
|--------|-------------------|-----------|
| DONE | empty | Continue lifecycle detection |
| DONE | has question | Show human, wait for yes/no |
| FAILED | has explanation | Stop lifecycle, show human |
| FAILED | empty | Stop lifecycle, ask human how to proceed |

**Review workers** use `PASS` instead of `DONE`:
```markdown
**Status**: PASS | FAILED
```

---

## Skill File Format

Skills follow the OpenClaw standard:

```
skills/{skill-name}/
└── SKILL.md
```

**Content:**
```
# {Skill Name}

{Purpose}

## Steps

1. ...
2. ...

## Output

{What the agent should produce or announce.}
```

**Skill routing**: The spawn task specifies which skill to read: `Read skills/{skill-name}/SKILL.md and follow it.` Skills are NOT registered in `openclaw.json`.

---

## Review Gate Convention

All mandatory review points follow this pattern:

```markdown
### Phase {X}: {Name} ⛔

#### Work
{Description of work to do.}

#### ⛔ Review Gate
Spawn project-pilot-review-worker as a run-mode subagent:
...
**STOP. You MUST spawn project-pilot-review-worker — do NOT review it yourself.
Do NOT proceed until review-worker returns PASS.**

#### Outcome
- **PASS** → update checkboxes, proceed to next phase
- **Auto-fixable** → re-spawn worker with feedback (max 2 rounds), then re-review
- **Failed** → return FAILED
```

**Key elements:**
- ⛔ emoji in phase title and gate subheading
- Explicit spawn block with complete task text
- "You MUST spawn" warning
- Three-outcome handling (PASS / auto-fix / Failed)
- NEVER self-review — always spawn Review Worker

---

## Spawn Task Format

All spawn tasks follow this structure:

```markdown
Spawn with:
  task: "Read skills/{skill-name}/SKILL.md and follow it.
    Project root: {project_root}
    {Additional parameters per spawn.}"
  runtime: subagent
  mode: run
  agentId: {agent-id}
```

**Rules:**
- `runtime: "subagent"` always (never `"acp"` — Discord doesn't support ACP spawning)
- L1 agents: `mode: "run"` (except Design Agent: `mode: "session"`)
- L2 workers: `mode: "run"` always
- All workers must be named (`agentId:`) — anonymous subagents inherit parent AGENTS.md
- Task text is a quoted string, not YAML indented block
- File paths use `{project_root}/` prefix
- `Project root: {project_root}` is a required parameter in every spawn task

---

## Commit Convention

| Stage | Message Format | Author |
|-------|----------------|--------|
| Design | `design: {iteration-name}` | `Openclaw <claw@openclaw.local>` |
| Plan (meta) | `plan: meta for {iteration-name}` | `Openclaw <claw@openclaw.local>` |
| Plan (contracts) | `plan: contracts for {iteration-name}` | `Openclaw <claw@openclaw.local>` |
| Implement | `impl: {contract-name}` | `Openclaw <claw@openclaw.local>` |
| CI/CD (release) | `release: v{version}` | `Openclaw <claw@openclaw.local>` |

**Commit command:**
```bash
git commit --author="Openclaw <claw@openclaw.local>" -m "{type}: {message}"
```

**Rules:**
- Implement Agent squashes all phase work into ONE commit (`git reset --soft $SQUASH_BASE`)
- No WIP or intermediate commits during phases
- Plan meta and Plan contracts are separate commits on the same iteration branch

---

## Checkbox Convention

All task checkboxes use markdown format:

```markdown
- [ ] Task not done
- [x] Task done
```

**Checkbox update pattern:**
- Implement Agent updates contract checkbox after each review gate PASS
- Meta contract checkboxes NOT updated during implementation (meta is index, not task list)
- Roadmap checkboxes updated by CI/CD on release

---

## Symlink Management

**Key rule: `workspace/` contains symlinks only.** No actual files.

| Operation | Command |
|-----------|---------|
| Create symlink | `cd {project_root} && ln -s ../../docs/contracts/feature/{name}.md workspace/contracts/open/{name}.md` |
| Move symlink | `cd {project_root} && mv workspace/contracts/open/{name}.md workspace/contracts/in_progress/{name}.md` |
| Delete symlink | `cd {project_root} && rm workspace/contracts/in_progress/{name}.md` |

Always use `cd {project_root} &&` then relative paths — `ln -s` stores the literal string, so relative paths remain valid.

---

## Agent Naming

All agents use the `project-pilot-` prefix:

| ID | Workspace |
|----|-----------|
| `project-pilot-init` | `agent-workspaces/project-pilot-init` |
| `project-pilot-design` | `agent-workspaces/project-pilot-design` |
| `project-pilot-plan` | `agent-workspaces/project-pilot-plan` |
| `project-pilot-implement` | `agent-workspaces/project-pilot-implement` |
| `project-pilot-cicd` | `agent-workspaces/project-pilot-cicd` |
| `project-pilot-knowledge-maintainer` | `agent-workspaces/project-pilot-knowledge-maintainer` |
| `project-pilot-contract-writer` | `agent-workspaces/project-pilot-contract-writer` |
| `project-pilot-interface-worker` | `agent-workspaces/project-pilot-interface-worker` |
| `project-pilot-test-worker` | `agent-workspaces/project-pilot-test-worker` |
| `project-pilot-coding-worker` | `agent-workspaces/project-pilot-coding-worker` |
| `project-pilot-review-worker` | `agent-workspaces/project-pilot-review-worker` |

All agents must be registered in `openclaw.json` under `agents.list` and `agents.defaults.subagents.allowAgents`.

---

## L1/L2 Pattern

| Aspect | L1 Agent | L2 Worker |
|--------|----------|-----------|
| Role | Owns a lifecycle stage | Executes a single work unit |
| Communication | Talks to Main Agent + spawns L2 | Reports to spawner (announce) |
| Context | Full project scope | Specific task only |
| Output type | Files + state transitions | Code/tests/reviews |
| Session mode | Design only (session), others (run) | Always run |
| Spawn depth from L0 | 1 | 2 |
| Reads sub-agent docs | NEVER | N/A |

---

## Deployment

```bash
# From project directory to skills directory
rsync --delete -av ~/.openclaw/projects/project-pilot/ ~/.openclaw/skills/project-pilot/
```

**Notes:**
- Use `rsync --delete` to avoid orphan files from removed agents/skills
- Git proxy is set globally: `git config --global http.proxy http://localhost:1081`
