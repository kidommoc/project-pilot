# Python Package 项目结构

适用于 Python 库、CLI 工具、MCP Server 开发。

## 标准结构

```
{package-name}/
├── pyproject.toml          # 必需 - 项目配置（Poetry/Flit）
├── README.md               # 必需 - 项目说明
├── src/
│   └── {package_name}/     # 源代码目录
│       ├── __init__.py
│       ├── module_a.py
│       └── module_b.py
├── tests/
│   ├── __init__.py
│   ├── test_module_a.py
│   └── test_module_b.py
├── docs/                   # 可选 - 文档
│   └── {doc-files}.md
├── scripts/                # 可选 - 辅助脚本
│   └── {script-name}.py
└── examples/               # 可选 - 使用示例
    └── {example-name}.py
```

## 关键文件说明

### pyproject.toml (Poetry)

```toml
[tool.poetry]
name = "{package-name}"
version = "0.1.0"
description = "项目描述"
authors = ["企鹅 <email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
pytest-cov = "^4.0"
black = "^23.0"
ruff = "^0.1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# CLI 入口（如适用）
[tool.poetry.scripts]
{cli-command} = "{package_name}.cli:main"
```

### src/{package_name}/__init__.py

```python
"""{package-name} - 项目描述"""

__version__ = "0.1.0"
__author__ = "企鹅"

from .module_a import function_a
from .module_b import ClassB

__all__ = ["function_a", "ClassB"]
```

### 测试文件

```python
# tests/test_module_a.py
import pytest
from {package_name} import function_a

def test_function_a():
    assert function_a(input) == expected_output
```

## 开发流程调整

### Phase 1: Specification

额外明确：
- [ ] 包类型（库 / CLI / MCP Server）
- [ ] Python 最低版本要求
- [ ] 是否需要 CLI 入口

### Phase 2: Implementation

- [ ] 使用 Poetry 管理依赖
- [ ] 遵循 PEP 8 风格
- [ ] 类型注解（推荐）

### Phase 3: Review

额外检查：
- [ ] `pytest` 通过
- [ ] `ruff check` 无错误
- [ ] `black --check` 格式正确
- [ ] 类型检查（mypy/pyright）通过

### Phase 4: Release

- [ ] 版本号更新（pyproject.toml）
- [ ] 发布到 PyPI（如适用）
- [ ] Git tag: `v{version}`

## 质量工具配置

### pyproject.toml 集成

```toml
[tool.black]
line-length = 88
target-version = ['py310']

[tool.ruff]
line-length = 88
select = ["E", "F", "W", "I"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov={package_name}"

[tool.mypy]
python_version = "3.10"
strict = true
```

## MCP Server 特例

如开发 MCP Server，结构调整为：

```
{mcp-server-name}/
├── pyproject.toml
├── src/
│   └── {server_name}/
│       ├── __init__.py
│       ├── server.py       # FastMCP 入口
│       └── tools/          # 工具实现
│           ├── __init__.py
│           ├── tool_a.py
│           └── tool_b.py
└── tests/
```

server.py 示例：
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("{server-name}")

@mcp.tool()
def tool_a(...) -> str:
    """工具描述"""
    return "结果"

if __name__ == "__main__":
    mcp.run()
```

---

**参考**:
- [Poetry 文档](https://python-poetry.org/docs/)
- [FastMCP](https://github.com/jlowin/fastmcp)

**Last Updated**: 2026-03-22
