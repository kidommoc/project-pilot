# Python Package Project Structure

**Init**: `poetry new {package-name}` or `uv init`

```
{package-name}/
├── pyproject.toml
├── src/
│   └── {package_name}/
│       ├── __init__.py
│       ├── module_a.py
│       └── module_b.py
├── tests/
│   ├── test_module_a.py
│   └── test_module_b.py
└── scripts/                # Optional
```

## Key config (pyproject.toml)

- Python: `^3.10`
- Test: pytest + pytest-cov
- Lint: ruff + black
- Types: mypy (strict recommended)
- CLI entry (if needed): `[tool.poetry.scripts]`

## MCP Server Variant

```
{mcp-server-name}/
├── pyproject.toml
├── src/
│   └── {server_name}/
│       ├── __init__.py
│       ├── server.py       # FastMCP entry
│       └── tools/
│           └── tool_a.py
└── tests/
```

Use `mcp.server.fastmcp.FastMCP` for server entry.

## Init Additions

After external tooling, add project-pilot structure (`docs/`, `workspace/`, etc.).
