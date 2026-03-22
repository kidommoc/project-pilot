# Test Verification Guide

**Quality Gate for Phase Completion (MUST-1)**

---

## Overview

**Rule**: No Phase is complete without passing tests.

| Phase Type | Required Tests | Examples |
|------------|----------------|----------|
| Code development | Unit tests + Functional tests | New functions, API endpoints |
| Documentation | Syntax check + Link validation | README, specs, ADRs |
| Configuration | Validation command + Rollback test | Config files, environment |
| Integration | End-to-end tests | MCP + Plugin联调 |

---

## Test Types

### 1. Unit Tests

**Purpose**: Verify individual functions/components work correctly.

**When**: After writing each function or component.

**Examples**:
```python
# Python function test
def test_add_dialogue_node():
    result = add_dialogue_node(
        tenant_id='default',
        node_type='Decision',
        content='Test decision',
        topic='test-topic'
    )
    assert result['status'] == 'success'
    assert 'node_id' in result
```

```typescript
// TypeScript function test
describe('addDialogueNode', () => {
  it('should return success status', async () => {
    const result = await client.addDialogueNode(...);
    expect(result.status).toBe('success');
  });
});
```

---

### 2. Functional Tests

**Purpose**: Verify feature works end-to-end from user perspective.

**When**: After completing a feature or tool.

**Examples**:
```bash
# Test MCP tool via HTTP
curl -X POST http://localhost:8765/add_dialogue_node \
  -H "Content-Type: application/json" \
  -d '{"tenant_id":"default","node_type":"Decision",...}'
```

---

### 3. Edge Case Tests

**Purpose**: Verify behavior with invalid/unusual inputs.

**When**: After core functionality works.

**Test cases**:
- Empty/missing required parameters
- Invalid enum values
- Boundary values (0, max, negative)
- Malformed data

**Examples**:
```python
# Invalid node_type should fail
result = add_dialogue_node(node_type='InvalidType', ...)
assert result['status'] == 'error'

# Empty content should fail or sanitize
result = add_dialogue_node(content='', ...)
```

---

### 4. Error Handling Tests

**Purpose**: Verify graceful failure and clear error messages.

**When**: After implementing error paths.

**Test cases**:
- File not found
- Permission denied
- Network timeout
- Invalid JSON

---

## Test Documentation

### In Completion Report

**Required sections**:
```markdown
## Verification Results

### Unit Tests
```bash
$ python3 -m pytest tests/test_add_node.py -v
✅ 5 passed, 0 failed
```

### Functional Tests
```bash
$ curl -X POST http://localhost:8765/add_dialogue_node ...
✅ {"status":"success","node_id":"DN_20260322_D01"}
```

### Edge Cases
- [x] Invalid node_type rejected
- [x] Empty content handled
- [x] Missing topic rejected
```

---

## Quick Test Checklist

**Before declaring Phase complete:**

- [ ] New functions have unit tests
- [ ] Features have functional tests
- [ ] Edge cases tested (invalid input, boundaries)
- [ ] Error handling verified
- [ ] Test results documented
- [ ] All tests pass (0 failures)

---

## Test-First Mindset

**Preferred order**:
```
1. Write test (defines expected behavior)
2. Write code (make test pass)
3. Refactor (clean up, keep tests passing)
```

**Acceptable order**:
```
1. Write code
2. Write tests alongside
3. Run tests together
```

**Forbidden**:
```
❌ Write all code first
❌ Write tests "later"
❌ Declare complete without tests
```

---

**Version**: 0.5.0  
**Related**: [workflow.md](../workflow.md), [checklists.md](checklists.md)
