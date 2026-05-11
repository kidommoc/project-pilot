# ID 可追踪性系统设计笔记

> 来源：kidom 的 AI 产品经理设计流经验
> 日期：2026-04-12
> 状态：设计想法，待验证

---

## 背景问题

当文档/代码存在多层关联时，agent 的"全量阅读→理解→分析"模式时间复杂度高（O(n²)）。

**kidom 的实际场景**：
- 领域层（角色实体状态机业务行为）
- 体验层（demo 和 UI 组件定义）
- 交互层（gherkin 语法定义的主流程/分支流程/防御性边界）
- 生成的 PRD（以功能点为中心）

内容成型后要改一点东西（比如补个用户旅程），agent 需要跑半小时以上，因为要读完几个文件 + 理解 + 分析 + 找关联。

**最终解决方案**：自己找出需要修改哪些文件的哪些行，直接告诉 agent。

---

## 核心设计：锚点 + ID 关联

### 架构分层

| 层级 | 职责 | 对应 project-pilot |
|------|------|-------------------|
| **领域层** | 最终锚点，真理来源 | Contract 文件 |
| **体验层** | UI 组件和领域层的关系，交互层联动 | Interface 产物 (Step A) |
| **交互层** | 用户旅程枚举，事件/行为/状态机/边界条件 | Test 产物 (Step B) |
| **生成层** | 人类友好 PRD | - |

### 关键机制

**1. 领域层埋点**
- 关键组件全部埋点（带唯一 ID）
- 作为整个系统的锚点

**2. ID 关联**
- UI 定义通过 ID 引用领域层
- Gherkin 通过 ID 引用领域层的事件/行为/状态机变更/边界条件
- 同时关联到角色、实体、UI 组件

**3. 变更定位**
```bash
# 通过 ID 快速 grep 所有关联文件（O(k) 复杂度）
grep -r "<contract-id>" --include="*.ts" --include="*.md" .
```

---

## 应用到 project-pilot Phase2

### 标记系统提案

#### Step A (Interface) —— 埋点
生成的接口文件自带可追踪标记：
```typescript
// src/api/user.ts
// @contract: user-auth-001
// @phase: A
// @generated: 2026-04-12T21:51:00Z

export interface UserAuth {
  // @ref: domain:user#authenticate
  login(credentials: Credentials): Promise<AuthResult>;
}
```

#### Step B (Test) —— 关联
测试文件通过 ID 引用接口：
```typescript
// tests/user.test.ts
// @contract: user-auth-001
// @phase: B
// @depends: src/api/user.ts#UserAuth

describe("UserAuth", () => {
  // @ref: domain:user#authenticate
  it("should authenticate valid user", () => {
    // ...
  });
});
```

#### Step C (Impl) —— 实现
```typescript
// src/impl/user.ts
// @contract: user-auth-001
// @phase: C
// @implements: src/api/user.ts#UserAuth
// @tests: tests/user.test.ts
```

### Phase2-Agent 优化执行流

**当需要修改 contract `user-auth-001` 时：**

```bash
# 1. 找到所有关联文件
grep -r "user-auth-001" --include="*.ts" --include="*.md" .

# 2. 按 phase 分组
grep -l "@phase: A" $(grep -rl "user-auth-001" .)  # 接口层
grep -l "@phase: B" $(grep -rl "user-auth-001" .)  # 测试层  
grep -l "@phase: C" $(grep -rl "user-auth-001" .)  # 实现层

# 3. Agent 只读这些文件，而非全仓库
```

---

## 关键洞见

> 不要让 agent 在"理解关联"上消耗算力，而是让**文件系统本身携带关联信息**，agent 只需要 `grep` 就能定位。

**复杂度对比**：
- 传统模式：全量阅读 → 理解 → 分析 → 找关联（O(n²)）
- 标记系统：`git diff + grep` → 定位关联（O(k)）

---

## 待讨论问题

1. 标记语法是否应标准化？（`@contract:` `@phase:` `@depends:` `@ref:`）
2. 是否需要在 Contract 文件中显式声明"影响域"？
3. Phase2-Agent 执行时，Main Agent 是否应预计算关联文件列表？
4. 如何与 git diff 结合，实现"增量感知"的执行模式？

---

## 相关参考

- `~/.openclaw/pp-agents.md` —— agent 架构设计演变记录
- `~/.openclaw/workspace/deep/deep-dive-cc/insights/` —— Claude Code 学习洞察
