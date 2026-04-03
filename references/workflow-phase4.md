# Phase 4: Release

**Goal**: Package and ship.  
**Hat**: Release Engineer

---

## Overview

Finalize the iteration, bump version, merge to main, tag release.

**Version History**: CHANGELOG.md is the **single source of truth** for version history. README only shows current release.

---

## Steps

1. **Cleanup README** (iteration branches only)
   - Remove `## Current Iteration` section
2. Update CHANGELOG.md
3. Bump version (SemVer)
4. **Commit** (Claw identity):
   ```bash
   git commit --author="Openclaw <claw@openclaw.local>" -m "release: v{version}"
   ```
   (on iteration branch)
5. **Merge to main**:
   ```bash
   git checkout main
   git merge iteration/v{version}
   ```
6. Create git tag (`v{version}`) on main:
   ```bash
   git tag v{version}
   ```
7. Present release summary to human
8. Human confirms release

---

## Version Bumping

| Change | Bump | Example |
|--------|------|---------|
| Breaking | MAJOR | 1.0.0 → 2.0.0 |
| Feature | MINOR | 1.2.0 → 1.3.0 |
| Fix | PATCH | 1.2.3 → 1.2.4 |

---

## Exit Criteria

- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] **Committed**: `release: v{version}` (iteration branch)
- [ ] **Merged**: iteration branch → main
- [ ] **Git tag created**: `v{version}` (main branch)
- [ ] Human confirmation obtained

**Claw**: Packages correctly, follows SemVer  
**Human**: Confirms release or requests changes
