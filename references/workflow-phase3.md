# Phase 3: Audit

**Goal**: Independent audit against the Contract, then deliver to human.  
**Hat**: Auditor (adversarial to Phase 2 developer)

---

## Overview

Take an opposing stance to your Phase 2 self. Question: "Does it actually satisfy the Contract?" (not "Did I implement it?")

---

## Steps

1. **Contract Audit**: Walk each Contract item, verify actual behavior matches criterion
2. **Code Quality Check**: Lint, naming conventions, documentation
3. **Produce Audit Summary** for human:
   - Contract items: per-item pass/fail
   - Test results
   - Changes summary (files touched, lines changed)
   - Known risks / tech debt
4. Human reviews (depth at human's discretion: spot / full / delegated)
5. Claw addresses feedback (if any)
6. Human confirms

---

## Audit Checklist

- [ ] All Contract items verified (each checked against actual behavior)
- [ ] Tests pass
- [ ] No lint errors
- [ ] Docs updated
- [ ] ADRs created (if applicable)
- [ ] Naming conventions followed

---

## Transition Actions (P3→P4)

Execute these steps **immediately after** human confirms audit pass:

1. **Generate Audit Report**: Create `reports/audit-v{version}.md` (lightweight summary)
2. **Human confirms**: Audit pass
3. **Update README**: Change `Phase: 3` → `Phase: 4`
4. **Commit**: `docs: phase 3 → 4`

```bash
git add -A
git commit --author="Openclaw <claw@openclaw.local>" -m "docs: phase 3 → 4"
```

**Human confirmation**: Required before commit.

---

## Exit Criteria

- [ ] Audit Summary delivered to human
- [ ] Audit Report generated
- [ ] Human confirmation obtained
- [ ] Feedback addressed (if any)
- [ ] README updated to Phase 4
- [ ] Transition commit created

**Claw**: Audits thoroughly from adversarial perspective, presents clearly  
**Human**: Validates, confirms, or requests changes
