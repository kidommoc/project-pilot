# Session Startup Checklist (MUST-2)

**Execute this checklist at the beginning of each Session**

---

## 1. Skill Activation Check

**Question**: Should current project use project-pilot?

| Condition | Yes | No |
|-----------|-----|-----|
| Has clear human supervisor? | → | → |
| Is development project (not one-off script)? | → | → |
| Needs decision and state tracking? | → | → |

**If all 3 are "Yes"** → Load project-pilot skill

---

## 2. Project State Check

**Read project README.md, confirm:**

- [ ] What is the current Phase? (e.g., Phase 1: Specification)
- [ ] What is the task checklist status for current Phase?
- [ ] Are there any blocking issues?
- [ ] Is previous Phase completed and waiting for confirmation?

**If previous Phase completed but not waiting for confirmation** → ⛔ STOP, complete Phase Completion Protocol first

---

## 3. Session Goal Check

**Clarify Session objectives:**

```
Tasks to complete in this Session:
1. {task 1}
2. {task 2}
3. {task 3} (optional)
```

**Task count check**:
- ✅ ≤3 tasks → Continue
- ⚠️ >3 tasks → Consider splitting into multiple Sessions or using subagent

---

## 4. Context Budget Check

**Estimate resource consumption for this Session:**

| Metric | Budget | Estimated | Status |
|--------|--------|-----------|--------|
| File writes | ≤7 | ? | 🟡 |
| Response tokens | ≤1500 | ? | 🟡 |
| Tool calls | ≤12 | ? | 🟡 |

**If over budget** → Plan `/new` or use subagent in advance

---

## 5. Documentation Check

**Confirm documentation status:**

- [ ] Is Spec/ADR approved? (if applicable)
- [ ] Is README.md up to date?
- [ ] Are there any unfinished Quality Gates?

---

## 6. Session Log Setup

**Create Session log (in docs/notes/ or memory/):**

```markdown
# YYYY-MM-DD Session Log

**Phase**: {current_phase}
**Goal**: {session_goal}
**Tasks**: 
- [ ] Task 1
- [ ] Task 2

**Progress**: (update in real-time)
**Decisions**: (record decisions)
**Next**: (next steps)
```

---

## 7. Attention Anchor

**Set attention anchor to prevent drift:**

```
🎯 Single goal for this Session: {one-sentence summary}
🚨 MUST constraint: Stop after phase completion and wait for confirmation
⏰ Estimated duration: ≤30 minutes
```

---

## Quick Version (When Time-Constrained)

**30-second check**:

1. What is current Phase in README? → {phase}
2. What is this Session's goal? → {goal}
3. Are there MUST constraints? → Stop after phase completion

---

**Version**: 0.5.0  
**Related**: [SKILL.md](../SKILL.md), [workflow.md](workflow.md)
