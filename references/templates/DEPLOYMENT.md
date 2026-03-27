# Plugin Deployment Standard

> **Template for OpenClaw Plugin Projects**  
> This is a template file. Placeholders (`{{...}}`) must be replaced during project initialization.

---

## 📁 Directory Structure

```
{{PROJECT_ROOT}}/                     # Project source (editable)
├── plugin/                           # Plugin source code
│   ├── index.ts
│   ├── openclaw.plugin.json
│   ├── skills/
│   └── hooks/                        # Optional - Gateway hooks
├── docs/
└── scripts/
    ├── deploy.sh                     # Deployment script
    └── sync-to-container.sh          # Optional - Sync helper

/app/extensions/                      # Container runtime (read-only copy)
├── {{PLUGIN_ID}}/                    # Plugin (skills, etc.)
└── (hooks are NOT loaded from here)

/app/dist/bundled/                    # Hooks runtime location
└── {hook-name}/                      # Hooks are loaded from here
```

**Core Principles:**
- **Source editing** → In `{{PROJECT_ROOT}}/plugin/`
- **Skills runtime** → `/app/extensions/{{PLUGIN_ID}}/` (loaded via `openclaw.plugin.json`)
- **Hooks runtime** → `/app/dist/bundled/` (OpenClaw scans this directory for `HOOK.md`)
- **Overwritten on restart** → Both directories are re-synced on container restart

---

## 🚀 Quick Deploy

### Using Deploy Script (Recommended)

```bash
cd {{PROJECT_ROOT}}/scripts/
./deploy.sh
```

Script automatically:
1. Cleans old runtime files
2. Syncs plugin to container
3. Verifies `plugin.json`

### Manual Deploy

```bash
# 1. Edit source
cd {{PROJECT_ROOT}}/plugin/
vim index.ts

# 2. Verify plugin.json
cat openclaw.plugin.json
# Ensure "id": "{{PLUGIN_ID}}" matches directory name

# 3. Sync to container
{{PROJECT_ROOT}}/scripts/sync-to-container.sh

# 4. Restart Gateway
openclaw gateway restart

# 5. Verify
openclaw status
```

---

## ✅ Deployment Checklist

### Before Deploy

- [ ] Source code changes saved
- [ ] `openclaw.plugin.json` `"id"` field is correct
- [ ] `skills` array paths are correct (relative to plugin.json)

### After Deploy

- [ ] `/app/extensions/{{PLUGIN_ID}}/` directory exists
- [ ] `openclaw.plugin.json` content is correct
- [ ] `openclaw status` shows plugin loaded
- [ ] Functional tests pass

---

## 🔧 Troubleshooting

### Plugin shows as `openclaw-bundled`

**Cause:** `openclaw.plugin.json` `"id"` field missing or mismatched with directory name.

**Fix:**
```bash
cat /app/extensions/{{PLUGIN_ID}}/openclaw.plugin.json
# Ensure "id": "{{PLUGIN_ID}}" matches directory name
```

### Changes not taking effect

**Cause:** Sync script not executed or container not restarted.

**Fix:**
```bash
{{PROJECT_ROOT}}/scripts/sync-to-container.sh
openclaw gateway restart
```

### Permission errors

**Cause:** Docker bind-mount directory has 777 permissions, OpenClaw security check rejects.

**Fix:** Use sync script to copy to container-internal directory (permissions auto-corrected).

---

## 📝 Related Documents

- **Main Standard:** `{{PROJECT_ROOT}}/docs/DEPLOYMENT.md`
- **Sync Script:** `{{PROJECT_ROOT}}/scripts/sync-to-container.sh`
- **Deploy Script:** `{{PROJECT_ROOT}}/scripts/deploy.sh`

---

**Version:** v1.0  
**Last Updated:** 2026-03-27  
**Maintainer:** OpenClaw Team
