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

## Exit Criteria

- [ ] Audit Summary delivered to human
- [ ] Human confirmation obtained
- [ ] Feedback addressed (if any)

**Claw**: Audits thoroughly from adversarial perspective, presents clearly  
**Human**: Validates, confirms, or requests changes
