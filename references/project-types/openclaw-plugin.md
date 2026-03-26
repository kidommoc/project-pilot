# OpenClaw Plugin Project Structure

For OpenClaw plugin development (TypeScript + optional MCP).

## Standard Structure

```
{plugin-name}/
├── package.json              # Required - Plugin metadata + dependencies
├── tsconfig.json             # Required - TypeScript configuration
├── src/
│   └── index.ts              # Required - Plugin entry point
├── mcp/                      # Optional - MCP Server
│   ├── server.py             # MCP server entry
│   └── tools/                # MCP tool implementations
│       └── {tool-name}.py
├── docs/                     # Optional - Plugin documentation
│   └── README.md
├── tests/                    # Recommended - Tests
│   └── {test-file}.test.ts
└── scripts/                  # Optional - Helper scripts
    └── {script-name}.ts
```

## Key Files

### package.json

Required fields:
```json
{
  "name": "@openclaw/plugin-{name}",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "test": "vitest"
  },
  "dependencies": {
    "@openclaw/sdk": "^1.0.0"
  }
}
```

### src/index.ts

Plugin entry point, exports plugin definition:
```typescript
import { definePlugin } from '@openclaw/sdk';

export default definePlugin({
  name: '{plugin-name}',
  version: '0.1.0',
  description: 'Plugin description',
  
  // Lifecycle hooks
  async onLoad() {
    // Executed when plugin loads
  },
  
  async onUnload() {
    // Executed when plugin unloads
  }
});
```

### MCP Server (Optional)

If providing MCP tools:

```
mcp/
├── server.py           # FastMCP server
└── tools/
    ├── tool_a.py       # Tool A
    └── tool_b.py       # Tool B
```

server.py template:
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{plugin-name}")

@mcp.tool()
def {tool_name}(...) -> str:
    """Tool description"""
    return "Result"

if __name__ == "__main__":
    mcp.run()
```

## Development Process Adjustments

### Phase 1: Specification

In addition to standard specs, clarify:
- [ ] Are MCP tools needed?
- [ ] Plugin type (gateway plugin / MCP bridge)
- [ ] Required OpenClaw API version

### Phase 2: Implementation

- [ ] Use `tsc` to compile TypeScript
- [ ] MCP server uses Python (if needed)
- [ ] Follow OpenClaw plugin specifications

### Phase 3: Audit

Additional checks:
- [ ] package.json version is correct
- [ ] Plugin loads correctly into OpenClaw
- [ ] MCP tools (if any) register correctly

### Phase 4: Release

- [ ] Build artifacts go to `dist/`
- [ ] Publish to npm (if applicable) or install locally

## Testing Recommendations

```typescript
// tests/plugin.test.ts
import { describe, it, expect } from 'vitest';
import plugin from '../src/index';

describe('{plugin-name}', () => {
  it('should load without errors', async () => {
    await expect(plugin.onLoad()).resolves.not.toThrow();
  });
});
```

## Common Plugin Types

| Type | Description | Example |
|------|-------------|---------|
| **Gateway Plugin** | Extends Gateway functionality | Custom auth, logging |
| **MCP Bridge** | Bridges external MCP services | Connect to Obsidian, Notion |
| **Tool Provider** | Provides new tools | Weather query, code execution |
| **UI Extension** | Extends UI (future) | Custom panels |

---

## Project Pilot Integration

**Use project-pilot for structured development**:

1. **Activation**: Say "Use project-pilot for this plugin"
2. **Contract**: Create Contract for each feature/modification
3. **Interface Docs**: Document plugin APIs in `references/interfaces/`
4. **ADRs**: Record architectural decisions (e.g., MCP integration approach)

**Documentation** (AI-First):
- **Required**: Contract files, Interface docs, ADRs
- **Optional**: `docs/README.md` for human users
- **Not needed**: Completion reports, architecture docs

---

**Reference**:
- [OpenClaw Plugin API](https://docs.openclaw.ai/plugins/api)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [project-pilot SKILL.md](../SKILL.md)

**Last Updated**: 2026-03-26 (project-pilot 1.1.0)
