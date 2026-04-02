# Python Package Project Structure

For Python libraries, CLI tools, and MCP Server development.

## Standard Structure

```
{package-name}/
├── pyproject.toml          # Required - Project configuration (Poetry/Flit)
├── README.md               # Required - Project description
├── CHANGELOG.md            # Version history
├── contracts/              # ⚠️ Must be in root - project-pilot contracts
│   ├── draft/              # Awaiting human confirmation
│   ├── open/               # Confirmed, waiting to start
│   ├── in_progress/        # Current focus (exactly 1)
│   └── archived/           # Completed
├── docs/                   # Project documentation
│   ├── decisions/          # ADR - Architecture Decision Records
│   └── interfaces/         # Public API interfaces
├── references/             # Reference materials
│   ├── guides/
│   ├── templates/
│   └── ...
├── src/
│   └── {package_name}/     # Source code directory
│       ├── __init__.py
│       ├── module_a.py
│       └── module_b.py
├── tests/
│   ├── __init__.py
│   ├── test_module_a.py
│   └── test_module_b.py
├── scripts/                # Optional - Helper scripts
│   └── {script-name}.py
└── examples/               # Optional - Usage examples
    └── {example-name}.py
```

## Key Files

### pyproject.toml (Poetry)

```toml
[tool.poetry]
name = "{package-name}"
version = "0.1.0"
description = "Project description"
authors = ["Penguin <email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
pytest-cov = "^4.0"
black = "^23.0"
ruff = "^0.1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# CLI entry point (if applicable)
[tool.poetry.scripts]
{cli-command} = "{package_name}.cli:main"
```

### src/{package_name}/__init__.py

```python
"""{package-name} - Project description"""

__version__ = "0.1.0"
__author__ = "Penguin"

from .module_a import function_a
from .module_b import ClassB

__all__ = ["function_a", "ClassB"]
```

### Test Files

```python
# tests/test_module_a.py
import pytest
from {package_name} import function_a

def test_function_a():
    assert function_a(input) == expected_output
```

## Development Process Adjustments

### Phase 1: Specification

Additional clarifications:
- [ ] Package type (library / CLI / MCP Server)
- [ ] Minimum Python version requirement
- [ ] Is CLI entry point needed?

### Phase 2: Implementation

- [ ] Use Poetry for dependency management
- [ ] Follow PEP 8 style
- [ ] Type annotations (recommended)

### Phase 3: Audit

Additional checks:
- [ ] `pytest` passes
- [ ] `ruff check` has no errors
- [ ] `black --check` formatting is correct
- [ ] Type checking (mypy/pyright) passes

### Phase 4: Release

- [ ] Version updated (pyproject.toml)
- [ ] Published to PyPI (if applicable)
- [ ] Git tag: `v{version}`

## Quality Tool Configuration

### pyproject.toml Integration

```toml
[tool.black]
line-length = 88
target-version = ['py310']

[tool.ruff]
line-length = 88
select = ["E", "F", "W", "I"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov={package_name}"

[tool.mypy]
python_version = "3.10"
strict = true
```

## MCP Server Special Case

For MCP Server development, adjust structure to:

```
{mcp-server-name}/
├── pyproject.toml
├── src/
│   └── {server_name}/
│       ├── __init__.py
│       ├── server.py       # FastMCP entry
│       └── tools/          # Tool implementations
│           ├── __init__.py
│           ├── tool_a.py
│           └── tool_b.py
└── tests/
```

server.py example:
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{server-name}")

@mcp.tool()
def tool_a(...) -> str:
    """Tool description"""
    return "Result"

if __name__ == "__main__":
    mcp.run()
```

---

**Reference**:
- [Poetry Documentation](https://python-poetry.org/docs/)
- [FastMCP](https://github.com/jlowin/fastmcp)

**Last Updated**: 2026-04-02 (project-pilot 1.2.0)

## Project Pilot Integration

**Use project-pilot for structured development**:

1. **Activation**: Say "Use project-pilot for this package"
2. **Contract**: Create Contract for each feature/modification
3. **Interface Docs**: Document public APIs in `references/interfaces/`
4. **ADRs**: Record architectural decisions (e.g., Poetry vs setuptools)

**Documentation** (AI-First):
- **Required**: Contract files, Interface docs (public API), ADRs
- **Optional**: `docs/` for user documentation
- **Not needed**: Completion reports, architecture docs

---

**Last Updated**: 2026-03-26 (project-pilot 1.1.0)
