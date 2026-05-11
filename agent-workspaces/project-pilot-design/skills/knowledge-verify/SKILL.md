# Knowledge Verify

Read by Design Agent to verify Knowledge Maintainer output is a faithful extraction.

## Steps

### 1. Read the spec

Read `{project_root}/docs/specs/{date}-{name}.md` — specifically the PRD and Implementation Strategy sections.

### 2. Check git diff

```bash
git diff HEAD -- docs/knowledge/
```

This shows all changes made by Knowledge Maintainer.

### 3. For each changed file, compare against the spec

| Knowledge field | Compare against | Check for |
|----------------|----------------|----------|
| Architecture updates | Implementation Strategy | New modules/layers exist in diagram |
| Module constraints | Changes Summary | Responsibilities match, no extras |
| Interface signatures | Changes Summary + Business Logic Topology | Signatures match the flow |
| Domain models | Changes Summary | Fields match the spec |
| Journeys | PRD | User stories mapped correctly |
| Conventions | PRD + Implementation Strategy | Only what was discussed |

Only verify **what the spec says**. Do not spot-check for design improvements — that's human territory.

### 4. If issues

If a Knowledge file deviates from the spec:
1. Tell the human what's wrong
2. Re-spawn Knowledge Maintainer with specific corrections
3. Re-run git diff to confirm fix

### 5. If clean

Proceed to commit.
