# External Tool Integration

> *Ideas for integrating project-pilot with external tools and services.*
> *Date: 2026-03-29 (first discussed), 2026-05-11 (extracted)*

---

Leverage existing tool ecosystems to reduce coordination overhead and provide automated workflows.

## GitHub Issues Sync

Contract creation/closing triggers automatic Issue sync:

- New contract in `docs/contracts/` → creates a GitHub Issue
- Contract closes (in_progress → done) → closes the Issue
- Bidirectional: commenting on Issue updates contract status

**Challenge**: OAuth/token management. Need a secure way to store and use GitHub credentials.

## CI/CD Triggers

Contract verification stages trigger GitHub Actions:

- **Review Gate PASS**: Auto-trigger lint + build on the iteration branch
- **Contract completion**: Auto-trigger test suite, report results back
- **Release**: Auto-trigger deployment pipeline

Current CI/CD is agent-driven (spawn CI/CD Agent, run audits). Integration would add a parallel automation path.

## PR Association

After contract completion, automatically:

1. Create a pull request from iteration branch to main
2. Link the PR to the contract file and meta contract
3. Human reviews and approves before merge

Currently CI/CD merges directly after audit + human confirm. PR would add an intermediate review step.

## Status Board

GitHub Projects or similar kanban board visualizing contract status:

- `open/` → "To Do"
- `in_progress/` → "In Progress"  
- done → "Done"

Sync workspace symlink state to board columns. Bidirectional: moving card changes symlink.

---

## Current Status

All items are **forward-looking ideas**. Not implemented. Blocking research item: OAuth/token storage for GitHub API access.

## Related

- `docs/architecture.md` — current agent-driven CI/CD flow
- `docs/contract.md` — contract lifecycle and status tracking
