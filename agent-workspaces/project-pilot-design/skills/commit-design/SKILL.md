# Commit Design

Read by Design Agent to commit design work (spec + Knowledge).

## Before Commit

- Spec is confirmed by human ✅
- Knowledge is verified against spec via git diff ✅

## Steps

### 1. Update roadmap

Add new features as unchecked items in `{project_root}/docs/roadmap.md`. Read existing file first — append, don't overwrite.

### 2. Create spec symlinks

```bash
cd {project_root}
mkdir -p workspace/specs
ln -s ../../docs/specs/{name}.md workspace/specs/{name}.md
```

### 3. Squash and commit

If multiple spec writing iterations occurred during this session (e.g., human asked for revisions), squash into one commit:

```bash
git add docs/specs/ docs/knowledge/ docs/roadmap.md workspace/specs/
git diff --cached --quiet || git commit --author="Openclaw <claw@openclaw.local>" -m "design: {iteration-name}"
```

If previous commits exist from this session that should be squashed:

```bash
git reset --soft <commit-before-this-session>
git add docs/specs/ docs/knowledge/ docs/roadmap.md workspace/specs/
git commit --author="Openclaw <claw@openclaw.local>" -m "design: {iteration-name}"
```

**Important**: Only include design-related files. Do not include code changes in this commit.
