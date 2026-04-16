# PROJECT.AGENT.md Template

```markdown
# {Project Name}

> {One-sentence description}

## Tech Stack

- **Language**: {language} {version}
- **Framework**: {framework} (if applicable)
- **Key Dependencies**: {list}
- **Package Manager**: {npm/pip/go mod/etc.}

## Conventions

### Naming
- **Files**: {kebab-case / snake_case / camelCase}
- **Functions/Methods**: {camelCase / snake_case}
- **Types/Classes**: {PascalCase}
- **Constants**: {UPPER_SNAKE_CASE}

### Directory Structure
```
src/           ← source code
tests/         ← test files
docs/          ← documentation
scripts/       ← helper scripts
```

### Patterns
- {e.g. "Services are classes with dependency injection"}
- {e.g. "All async functions return Promises, no callbacks"}

## Testing

- **Framework**: {jest / pytest / go test / etc.}
- **File Pattern**: `{*.test.ts / test_*.py / *_test.go}`
- **Run**: `{npm test / pytest / go test ./...}`

## Build & Run

- **Build**: `{command}`
- **Run**: `{command}`
- **Deploy**: `{command or "see scripts/deploy.sh"}`

## Notes

{Anything else workers should know about this project}
```
