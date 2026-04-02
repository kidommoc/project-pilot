# CLI Tool Project Structure

For command-line tool development (Node.js or Python).

## Node.js CLI Structure

```
{cli-name}/
├── package.json
├── tsconfig.json             # If using TypeScript
├── README.md                 # Project overview
├── CHANGELOG.md              # Version history
├── contracts/                # ⚠️ Must be in root - project-pilot contracts
│   ├── draft/                # Awaiting human confirmation
│   ├── open/                 # Confirmed, waiting to start
│   ├── in_progress/          # Current focus (exactly 1)
│   └── archived/             # Completed
├── docs/                     # Project documentation
│   ├── decisions/            # ADR - Architecture Decision Records
│   └── interfaces/           # CLI command interfaces
├── references/               # Reference materials
│   ├── guides/
│   ├── templates/
│   └── ...
├── src/
│   ├── index.ts              # CLI entry
│   ├── commands/             # Command implementations
│   │   ├── command-a.ts
│   │   └── command-b.ts
│   └── utils/                # Utility functions
├── tests/
│   └── {test-file}.test.ts
└── bin/                      # Executable (optional)
    └── cli.js
```

### package.json (Node.js CLI)

```json
{
  "name": "{cli-name}",
  "version": "0.1.0",
  "type": "module",
  "bin": {
    "{cli-command}": "./dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "test": "vitest"
  },
  "dependencies": {
    "commander": "^11.0",
    "chalk": "^5.0",
    "ora": "^7.0"
  }
}
```

### src/index.ts (Commander Example)

```typescript
#!/usr/bin/env node
import { Command } from 'commander';
import { commandA } from './commands/command-a.js';
import { commandB } from './commands/command-b.js';

const program = new Command();

program
  .name('{cli-name}')
  .version('0.1.0')
  .description('CLI description');

program
  .command('command-a')
  .description('Command A description')
  .action(commandA);

program
  .command('command-b')
  .description('Command B description')
  .option('-f, --file <path>', 'Input file')
  .action(commandB);

program.parse();
```

---

## Python CLI Structure

```
{cli-name}/
├── pyproject.toml
├── README.md                 # Project overview
├── CHANGELOG.md              # Version history
├── contracts/                # ⚠️ Must be in root - project-pilot contracts
│   ├── draft/                # Awaiting human confirmation
│   ├── open/                 # Confirmed, waiting to start
│   ├── in_progress/          # Current focus (exactly 1)
│   └── archived/             # Completed
├── docs/                     # Project documentation
│   ├── decisions/            # ADR - Architecture Decision Records
│   └── interfaces/           # CLI command interfaces
├── references/               # Reference materials
│   ├── guides/
│   ├── templates/
│   └── ...
├── src/
│   └── {package_name}/
│       ├── __init__.py
│       ├── cli.py              # CLI entry
│       └── commands/           # Command implementations
│           ├── __init__.py
│           ├── command_a.py
│           └── command_b.py
└── tests/
```

### pyproject.toml (Python CLI)

```toml
[tool.poetry]
name = "{cli-name}"
version = "0.1.0"
description = "CLI description"

[tool.poetry.scripts]
{cli-command} = "{package_name}.cli:main"

[tool.poetry.dependencies]
python = "^3.10"
click = "^8.0"
rich = "^13.0"
```

### src/{package_name}/cli.py (Click Example)

```python
#!/usr/bin/env python3
import click
from rich.console import Console

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """CLI description"""
    pass

@main.command()
@click.option('--name', '-n', default='World', help='Name to greet')
def command_a(name):
    """Command A description"""
    console.print(f"Hello, {name}!")

@main.command()
@click.argument('file', type=click.Path(exists=True))
def command_b(file):
    """Command B description"""
    console.print(f"Processing {file}")

if __name__ == '__main__':
    main()
```

---

## Development Process Adjustments

### Phase 1: Specification

Additional clarifications:
- [ ] Target platform (cross-platform / specific OS)
- [ ] Command list and functionality
- [ ] Is interactive input needed?

### Phase 2: Implementation

- [ ] Command parsing library (Commander/Click/Argparse)
- [ ] Output formatting (colors/tables/progress bars)
- [ ] User-friendly error handling

### Phase 3: Audit

Additional checks:
- [ ] `--help` output is correct
- [ ] Clear prompts for invalid input
- [ ] Exit codes are correct (0=success, non-0=failure)

### Phase 4: Release

- [ ] Publish to npm/PyPI
- [ ] Test global installation
- [ ] README includes installation and usage instructions

## User Experience Recommendations

- ✅ Colored output (use chalk/rich)
- ✅ Progress indicators (use ora/rich)
- ✅ Clear error messages
- ✅ `--help` includes examples
- ✅ Reasonable defaults

---

## Project Pilot Integration

**Use project-pilot for structured development**:

1. **Activation**: Say "Use project-pilot for this CLI tool"
2. **Contract**: Create Contract for each command/feature
3. **Interface Docs**: Document CLI commands in `references/interfaces/`
4. **ADRs**: Record architectural decisions (e.g., CLI framework choice)

**Documentation** (AI-First):
- **Required**: Contract files, Interface docs (CLI commands), ADRs
- **Optional**: `docs/` for user manual
- **Not needed**: Completion reports, architecture docs

---

**Reference**:
- [Commander.js](https://github.com/tj/commander.js)
- [Click](https://click.palletsprojects.com/)
- [project-pilot SKILL.md](../SKILL.md)

**Last Updated**: 2026-04-02 (project-pilot 1.2.0)
