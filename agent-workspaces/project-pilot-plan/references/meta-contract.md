# Meta Contract: {Iteration Name}

**Created**: YYYY-MM-DDTHH:MM
**Source Spec**: [{spec-name}](../specs/{spec-name}.spec.md)

## Contracts

| # | Contract | Priority | Dependencies |
|---|----------|----------|--------------|
| 1 | [{contract-name}](./feature/{contract-name}.md) | high/medium/low | none |
| 2 | [{contract-name}](./feature/{contract-name}.md) | high/medium/low | 1 |

## Execution Order

Parallel group 1: C-1, C-2 (no dependencies)
Sequential: C-3 (depends on C-1)
...

## Notes

Any cross-contract concerns, risks, or open questions.
