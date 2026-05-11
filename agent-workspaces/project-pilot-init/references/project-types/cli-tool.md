# CLI Tool Project Structure

## Node.js CLI

**Init**: `npm create` or manual setup

```
{cli-name}/
├── package.json
├── tsconfig.json
├── src/
│   ├── index.ts              # CLI entry (use commander)
│   ├── commands/
│   └── utils/
├── tests/
│   └── {test-file}.test.ts
└── bin/
    └── cli.js
```

**Key config** (package.json):
- `"type": "module"`
- `"bin": { "{cli-command}": "./dist/index.js" }`
- Test: vitest
- Build: tsc

## Python CLI

**Init**: `poetry new` or `uv init`

```
{cli-name}/
├── pyproject.toml
├── src/
│   └── {package_name}/
│       ├── __init__.py
│       ├── cli.py              # CLI entry (use click)
│       └── commands/
└── tests/
```

**Key config** (pyproject.toml):
- `[tool.poetry.scripts]` → `{cli-command} = "{package_name}.cli:main"`
- Test: pytest
- Lint: ruff + black

## Default Conventions

### Node.js
- TypeScript, `node:` import prefix for Node builtins
- CLI: commander, `bin/` entry point
- Tests: vitest
- Files: kebab-case

### Python
- snake_case for files, functions, variables
- CLI: click
- Tests: pytest + pytest-cov
- Lint: ruff + black

## Init Additions

After external tooling, add project-pilot structure (`docs/`, `workspace/`, etc.).
