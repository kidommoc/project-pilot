#!/bin/bash
# deploy.sh - Plugin Quick Deploy Script
# Usage: ./deploy.sh [plugin-name]
# Default: {{PLUGIN_ID}}

set -e

PLUGIN_NAME="${1:-{{PLUGIN_ID}}}"
SOURCE_DIR="{{PROJECT_ROOT}}/plugin"
EXTENSIONS_DIR="/app/extensions"
BUNDLED_HOOKS_DIR="/app/dist/bundled"

echo "========================================"
echo "  OpenClaw Plugin Deploy"
echo "  Plugin: $PLUGIN_NAME"
echo "========================================"

# 1. Clean runtime directory
echo "[1/4] Cleaning runtime directory..."
rm -rf "$EXTENSIONS_DIR/$PLUGIN_NAME"
echo "       ✓ Removed $EXTENSIONS_DIR/$PLUGIN_NAME"

# 2. Sync plugin (skills, etc.)
echo "[2/4] Syncing plugin..."
if [ -d "$SOURCE_DIR" ]; then
  cp -r "$SOURCE_DIR" "$EXTENSIONS_DIR/$PLUGIN_NAME"
  echo "       ✓ Plugin synced to $EXTENSIONS_DIR/$PLUGIN_NAME"
else
  echo "       ✗ Source not found: $SOURCE_DIR"
  exit 1
fi

# 3. Sync hooks to /app/dist/bundled/ (if hooks exist)
echo "[3/4] Syncing hooks..."
if [ -d "$SOURCE_DIR/hooks" ]; then
  for hook_dir in "$SOURCE_DIR/hooks"/*/; do
    if [ -d "$hook_dir" ]; then
      hook_name=$(basename "$hook_dir")
      hook_dst="$BUNDLED_HOOKS_DIR/$hook_name"
      rm -rf "$hook_dst"
      cp -r "$hook_dir" "$hook_dst"
      echo "       ✓ Hook '$hook_name' synced to $hook_dst"
    fi
  done
else
  echo "       ℹ No hooks directory, skipping"
fi

# 4. Verify
echo "[4/4] Verifying..."
PLUGIN_JSON="$EXTENSIONS_DIR/$PLUGIN_NAME/openclaw.plugin.json"
if [ -f "$PLUGIN_JSON" ]; then
  PLUGIN_ID=$(cat "$PLUGIN_JSON" | grep -o '"id"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)
  echo "       ✓ Plugin ID: $PLUGIN_ID"
  if [ "$PLUGIN_ID" != "$PLUGIN_NAME" ]; then
    echo "       ⚠ WARNING: Plugin ID mismatch! Expected '$PLUGIN_NAME', got '$PLUGIN_ID'"
  fi
else
  echo "       ✗ openclaw.plugin.json not found"
  exit 1
fi

echo "========================================"
echo "  ✓ Deploy Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "  1. Restart gateway: openclaw gateway restart"
echo "  2. Verify: openclaw status"
echo "  3. Verify hooks: openclaw hooks list"
echo ""
