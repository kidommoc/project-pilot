# Phase 4: Release

**Goal**: Package and ship.  
**Hat**: Release Engineer

---

## Overview

Finalize the iteration, bump version, merge to main, tag release.

**Version History**: CHANGELOG.md is the **single source of truth** for version history. README only shows current release.

---

## Transition Actions (P4→Done)

Execute these steps **as a single transaction** after all preparation:

### Step 1: Prepare

1. **Cleanup README**:
   - Remove `## Current Iteration` section
   - Header shows: `Current release: v{version}` (date optional)
2. **Update CHANGELOG.md**
3. **Bump version** (SemVer)

### Step 2: Plan Release Actions

Present to human for confirmation:

```
Release Plan for v{version}:

Git commands to execute:
1. git add -A
2. git commit --author="Openclaw <claw@openclaw.local>" -m "release: v{version}"
3. git checkout main
4. git merge iteration/v{version}
5. git tag v{version}
6. git branch -d iteration/v{version}

Confirm execution? [yes/no]
```

### Step 3: Execute (after human confirms)

```bash
git add -A
git commit --author="Openclaw <claw@openclaw.local>" -m "release: v{version}"
git checkout main
git merge iteration/v{version}
git tag v{version}
git branch -d iteration/v{version}
```

**Human confirmation**: Required before **any** git command executes.

---

## Version Bumping

| Change | Bump | Example |
|--------|------|---------|
| Breaking | MAJOR | 1.0.0 → 2.0.0 |
| Feature | MINOR | 1.2.0 → 1.3.0 |
| Fix | PATCH | 1.2.3 → 1.2.4 |

---

## Version Bumping

| Change | Bump | Example |
|--------|------|---------|
| Breaking | MAJOR | 1.0.0 → 2.0.0 |
| Feature | MINOR | 1.2.0 → 1.3.0 |
| Fix | PATCH | 1.2.3 → 1.2.4 |

---

## Exit Criteria

- [ ] README cleaned up (Current Iteration section removed)
- [ ] CHANGELOG updated
- [ ] Version bumped
- [ ] Release actions planned and presented
- [ ] Human confirmation obtained
- [ ] **Committed**: `release: v{version}` (iteration branch)
- [ ] **Merged**: iteration branch → main
- [ ] **Git tag created**: `v{version}` (main branch)
- [ ] **Iteration branch deleted**

**Claw**: Packages correctly, follows SemVer  
**Human**: Confirms release or requests changes
