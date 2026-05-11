# Init Checklist — for Main Agent

Read this before spawning Init. Collect these from the human.

## How to use

When `PROJECT.AGENT.md` does not exist, tell the human you're setting up the project,
then ask:

## Required

1. **Project description** — one sentence: what does this project do?
2. **Project type** — choose one:
   - `openclaw-plugin` — OpenClaw plugin
   - `cli-tool` — CLI application
   - `python-package` — Python library/package
   - `web-app` — Web application
   - `generic` — None of the above

## Recommended (ask if new/empty project)

3. **Language/Framework** — e.g. Python 3.12, TypeScript/React, Go
4. **Package manager** — e.g. uv, npm, yarn, go modules

## Optional (defaults available)

5. **Custom conventions** — naming style, directory layout preferences
6. **Testing framework preference** — only if different from language default
7. **Build/Run commands** — only if non-standard

## Spawn Init with

```
runtime: "subagent"
mode: "run"
agentId: "project-pilot-init"
task: "Initialize project at {project_root}.
  Description: <description>
  Type: <type>
  Language: <language>
  Package manager: <manager>
  Project root: {project_root}"
```
