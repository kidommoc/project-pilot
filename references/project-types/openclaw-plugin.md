# OpenClaw Plugin 项目结构

适用于 OpenClaw 插件开发（TypeScript + 可选 MCP）。

## 标准结构

```
{plugin-name}/
├── package.json              # 必需 - 插件元数据 + 依赖
├── tsconfig.json             # 必需 - TypeScript 配置
├── src/
│   └── index.ts              # 必需 - 插件入口
├── mcp/                      # 可选 - MCP Server
│   ├── server.py             # MCP 服务器入口
│   └── tools/                # MCP 工具实现
│       └── {tool-name}.py
├── docs/                     # 可选 - 插件文档
│   └── README.md
├── tests/                    # 推荐 - 测试
│   └── {test-file}.test.ts
└── scripts/                  # 可选 - 辅助脚本
    └── {script-name}.ts
```

## 关键文件说明

### package.json

必需字段：
```json
{
  "name": "@openclaw/plugin-{name}",
  "version": "0.1.0",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "test": "vitest"
  },
  "dependencies": {
    "@openclaw/sdk": "^1.0.0"
  }
}
```

### src/index.ts

插件入口，导出 plugin 定义：
```typescript
import { definePlugin } from '@openclaw/sdk';

export default definePlugin({
  name: '{plugin-name}',
  version: '0.1.0',
  description: '插件描述',
  
  // 生命周期钩子
  async onLoad() {
    // 插件加载时执行
  },
  
  async onUnload() {
    // 插件卸载时执行
  }
});
```

### MCP Server（可选）

如需提供 MCP 工具：

```
mcp/
├── server.py           # FastMCP 服务器
└── tools/
    ├── tool_a.py       # 工具 A
    └── tool_b.py       # 工具 B
```

server.py 模板：
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{plugin-name}")

@mcp.tool()
def {tool_name}(...) -> str:
    """工具描述"""
    return "结果"

if __name__ == "__main__":
    mcp.run()
```

## 开发流程调整

### Phase 1: Specification

除常规规格外，需明确：
- [ ] 是否需要 MCP 工具？
- [ ] 插件类型（gateway plugin / MCP bridge）
- [ ] 依赖的 OpenClaw API 版本

### Phase 2: Implementation

- [ ] 使用 `tsc` 编译 TypeScript
- [ ] MCP server 使用 Python（如需要）
- [ ] 遵循 OpenClaw 插件规范

### Phase 3: Review

额外检查：
- [ ] package.json 版本正确
- [ ] 插件能正确加载到 OpenClaw
- [ ] MCP 工具（如有）能正常注册

### Phase 4: Release

- [ ] 构建产物放入 `dist/`
- [ ] 发布到 npm（如适用）或本地安装

## 测试建议

```typescript
// tests/plugin.test.ts
import { describe, it, expect } from 'vitest';
import plugin from '../src/index';

describe('{plugin-name}', () => {
  it('should load without errors', async () => {
    await expect(plugin.onLoad()).resolves.not.toThrow();
  });
});
```

## 常见插件类型

| 类型 | 描述 | 示例 |
|------|------|------|
| **Gateway Plugin** | 扩展 Gateway 功能 | 自定义认证、日志 |
| **MCP Bridge** | 桥接外部 MCP 服务 | 连接 Obsidian、Notion |
| **Tool Provider** | 提供新工具 | 天气查询、代码执行 |
| **UI Extension** | 扩展 UI（未来） | 自定义面板 |

---

**参考**:
- [OpenClaw Plugin API](https://docs.openclaw.ai/plugins/api)
- [MCP Protocol](https://modelcontextprotocol.io/)

**Last Updated**: 2026-03-22
