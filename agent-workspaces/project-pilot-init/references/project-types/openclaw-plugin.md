# OpenClaw Plugin Project Structure

**Init**: Manual setup (no external scaffolding tool)

```
{plugin-name}/
├── plugin/
│   ├── index.ts              # Plugin entry point
│   ├── openclaw.plugin.json  # Plugin manifest
│   ├── skills/               # Optional
│   │   └── {skill-name}/
│   │       └── SKILL.md
│   └── hooks/                # Optional
│       └── {hook-name}/
│           ├── HOOK.md
│           └── handler.ts
├── scripts/
│   ├── deploy.sh
│   └── sync-to-container.sh
└── tests/
    └── {test-file}.test.ts
```

## Critical: Plugin Manifest

`plugin/openclaw.plugin.json`:
- `"id"` **must** match the plugin directory name (otherwise shows as `openclaw-bundled`)
- `"skills"` array uses relative paths from plugin.json

## Deploy

```bash
./scripts/deploy.sh
# or: sync-to-container.sh + openclaw gateway restart
```

## Init Additions

After setup, add project-pilot structure (`docs/`, `workspace/`, etc.).
