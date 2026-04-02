# OpenClaw Plugin Project Structure

For OpenClaw plugin development (TypeScript + optional MCP).

## Standard Structure

```
{plugin-name}/
├── plugin/                   # Required - Plugin source code (OpenClaw runtime)
│   ├── index.ts              # Plugin entry point
│   ├── openclaw.plugin.json  # Plugin manifest (id, skills, config)
│   ├── skills/               # Optional - OpenClaw skills
│   │   └── {skill-name}/
│   │       └── SKILL.md
│   └── hooks/                # Optional - Gateway hooks
│       ├── {hook-name-1}/
│       │   ├── HOOK.md       # Hook metadata (required for discovery)
│       │   └── handler.ts    # Hook implementation
│       └── {hook-name-2}/
├── docs/                     # Required - Project documentation
│   ├── README.md
│   ├── DEPLOYMENT.md         # Deployment standard (generated from template)
│   ├── architecture/         # Architecture docs
│   ├── decisions/            # Design decisions
│   ├── notes/                # Implementation notes
│   └── specs/                # Specifications
├── contracts/                # Required - project-pilot contracts
│   ├── active/               # In-progress contracts
│   ├── archive/              # Completed contracts
│   └── pending-confirmation/ # Awaiting human confirmation
├── references/               # Optional - Reference materials
├── scripts/                  # Required - Helper scripts
│   ├── deploy.sh             # Deployment script (generated from template)
│   └── sync-to-container.sh  # Sync script for container deployment
└── tests/                    # Recommended - Tests
    └── {test-file}.test.ts
```

## Key Files

### plugin/openclaw.plugin.json

Plugin manifest (required):
```json
{
  "id": "{plugin-id}",
  "kind": "plugin",
  "name": "Plugin Name",
  "description": "Plugin description",
  "version": "0.1.0",
  "skills": ["./skills/{skill-name}"],
  "configSchema": {
    "type": "object",
    "additionalProperties": false,
    "properties": {
      "optionName": {
        "type": "string",
        "default": "default-value",
        "description": "Option description"
      }
    }
  }
}
```

**Critical**: `"id"` must match the plugin directory name, otherwise it shows as `openclaw-bundled`.

**Note on `configSchema`**: The JSON Schema can be:
- **Inline** in `openclaw.plugin.json` (recommended for simple schemas)
- **External file** (e.g., `config.schema.json`) for maintainability, then embedded during build

Some projects (like memory-engine) maintain a detailed `config.schema.json` for internal use or MCP integration, while `openclaw.plugin.json` contains a minimal schema for OpenClaw config validation. The runtime only reads `openclaw.plugin.json`.

### plugin/index.ts

Plugin entry point:
```typescript
// Plugin initialization
import { skills } from './skills';

export default {
  name: '{plugin-id}',
  version: '0.1.0',
  skills,
  
  async onLoad(config) {
    // Executed when plugin loads
  },
  
  async onUnload() {
    // Executed when plugin unloads
  }
};
```

### plugin/skills/{skill-name}/SKILL.md

Skill definition:
```markdown
---
name: {skill-name}
description: Skill description
---

# Skill Name

Skill implementation details...
```

### scripts/deploy.sh

Deployment script (generated from template):
```bash
#!/bin/bash
# deploy.sh - Plugin Quick Deploy Script
./deploy.sh
```

### docs/DEPLOYMENT.md

Deployment documentation (generated from template with actual paths).

## Development Process Adjustments

### Phase 1: Specification

In addition to standard specs, clarify:
- [ ] Plugin type (gateway plugin / MCP bridge / skill provider)
- [ ] Required OpenClaw API version
- [ ] Deployment target (container / local)

### Phase 2: Implementation

- [ ] Plugin entry point: `plugin/index.ts`
- [ ] Plugin manifest: `plugin/openclaw.plugin.json` (ensure `id` matches directory name)
- [ ] Skills in `plugin/skills/`
- [ ] Deployment script generated from template

### Phase 3: Audit

Additional checks:
- [ ] `openclaw.plugin.json` → `"id"` matches directory name
- [ ] Plugin loads correctly into OpenClaw
- [ ] Skills register correctly
- [ ] Deployment script works

### Phase 4: Release

- [ ] Documentation complete (README.md, DEPLOYMENT.md)
- [ ] Version bumped in `openclaw.plugin.json`
- [ ] CHANGELOG updated
- [ ] Git tag created

## Testing Recommendations

```typescript
// tests/plugin.test.ts
import { describe, it, expect } from 'vitest';

describe('{plugin-id}', () => {
  it('should load without errors', async () => {
    // Test plugin initialization
  });
  
  it('should register skills correctly', () => {
    // Test skill registration
  });
});
```

## Common Plugin Types

| Type | Description | Example |
|------|-------------|---------|
| **Gateway Plugin** | Extends Gateway functionality | Custom auth, logging |
| **MCP Bridge** | Bridges external MCP services | Connect to Obsidian, Notion |
| **Skill Provider** | Provides OpenClaw skills | memory-engine, feishu |
| **Channel Plugin** | Messaging channel integration | Discord, Telegram, Signal |

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

## 🚀 Deployment

**After development completes, follow the standard deployment process:**

### Quick Deploy

```bash
# Using deploy script (recommended)
cd {project-root}/scripts/
./deploy.sh

# Or manually
{project-root}/scripts/sync-to-container.sh
openclaw gateway restart
```

### Key Checks

- [ ] `openclaw.plugin.json` → `"id"` matches directory name
- [ ] `skills` array paths are correct (relative to plugin.json)
- [ ] Run sync script or restart container
- [ ] Verify with `openclaw status`

### Common Issue: `openclaw-bundled`

If plugin shows as `openclaw-bundled` instead of its name:
- **Cause**: `openclaw.plugin.json` `"id"` field missing or mismatched
- **Fix**: Ensure `"id": "plugin-name"` matches the directory name

### Project Initialization

During project init, deployment files are generated from templates:

| Template | Generated File |
|----------|----------------|
| `references/templates/DEPLOYMENT.md` | `docs/DEPLOYMENT.md` |
| `references/templates/deploy.sh` | `scripts/deploy.sh` |

Placeholders (`{{PLUGIN_ID}}`, `{{PROJECT_ROOT}}`) are replaced with actual values.

### Full Documentation

📄 **Deployment Standard**: `/home/node/.openclaw/workspace/DEPLOYMENT.md`  
📄 **Template**: `/app/skills/project-pilot/references/templates/DEPLOYMENT.md`

---

**Reference**:
- [OpenClaw Plugin API](https://docs.openclaw.ai/plugins/api)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [project-pilot SKILL.md](../SKILL.md)
- [Deployment Standard](../../../../workspace/DEPLOYMENT.md)
- [Deployment Template](../templates/DEPLOYMENT.md)

**Last Updated**: 2026-03-27 (project-pilot 1.1.1 + Deployment Standard v1.0)
