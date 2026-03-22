# CLI Tool 项目结构

适用于命令行工具开发（Node.js 或 Python）。

## Node.js CLI 结构

```
{cli-name}/
├── package.json
├── tsconfig.json             # 如使用 TypeScript
├── src/
│   ├── index.ts              # CLI 入口
│   ├── commands/             # 命令实现
│   │   ├── command-a.ts
│   │   └── command-b.ts
│   └── utils/                # 工具函数
├── tests/
│   └── {test-file}.test.ts
└── bin/                      # 可执行文件（可选）
    └── cli.js
```

### package.json (Node.js CLI)

```json
{
  "name": "{cli-name}",
  "version": "0.1.0",
  "type": "module",
  "bin": {
    "{cli-command}": "./dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch",
    "test": "vitest"
  },
  "dependencies": {
    "commander": "^11.0",
    "chalk": "^5.0",
    "ora": "^7.0"
  }
}
```

### src/index.ts (Commander 示例)

```typescript
#!/usr/bin/env node
import { Command } from 'commander';
import { commandA } from './commands/command-a.js';
import { commandB } from './commands/command-b.js';

const program = new Command();

program
  .name('{cli-name}')
  .version('0.1.0')
  .description('CLI 描述');

program
  .command('command-a')
  .description('命令 A 描述')
  .action(commandA);

program
  .command('command-b')
  .description('命令 B 描述')
  .option('-f, --file <path>', '输入文件')
  .action(commandB);

program.parse();
```

---

## Python CLI 结构

```
{cli-name}/
├── pyproject.toml
├── src/
│   └── {package_name}/
│       ├── __init__.py
│       ├── cli.py              # CLI 入口
│       └── commands/           # 命令实现
│           ├── __init__.py
│           ├── command_a.py
│           └── command_b.py
└── tests/
```

### pyproject.toml (Python CLI)

```toml
[tool.poetry]
name = "{cli-name}"
version = "0.1.0"
description = "CLI 描述"

[tool.poetry.scripts]
{cli-command} = "{package_name}.cli:main"

[tool.poetry.dependencies]
python = "^3.10"
click = "^8.0"
rich = "^13.0"
```

### src/{package_name}/cli.py (Click 示例)

```python
#!/usr/bin/env python3
import click
from rich.console import Console

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """CLI 描述"""
    pass

@main.command()
@click.option('--name', '-n', default='World', help='Name to greet')
def command_a(name):
    """命令 A 描述"""
    console.print(f"Hello, {name}!")

@main.command()
@click.argument('file', type=click.Path(exists=True))
def command_b(file):
    """命令 B 描述"""
    console.print(f"Processing {file}")

if __name__ == '__main__':
    main()
```

---

## 开发流程调整

### Phase 1: Specification

额外明确：
- [ ] 目标平台（跨平台 / 特定 OS）
- [ ] 命令列表及功能
- [ ] 是否需要交互式输入

### Phase 2: Implementation

- [ ] 命令解析库（Commander/Click/Argparse）
- [ ] 输出格式化（颜色/表格/进度条）
- [ ] 错误处理友好

### Phase 3: Review

额外检查：
- [ ] `--help` 输出正确
- [ ] 错误输入有清晰提示
- [ ] 退出码正确（0=成功，非 0=失败）

### Phase 4: Release

- [ ] 发布到 npm/PyPI
- [ ] 全局安装测试
- [ ] README 包含安装和使用说明

## 用户体验建议

- ✅ 彩色输出（使用 chalk/rich）
- ✅ 进度指示（使用 ora/rich）
- ✅ 清晰的错误信息
- ✅ `--help` 包含示例
- ✅ 合理的默认值

---

**参考**:
- [Commander.js](https://github.com/tj/commander.js)
- [Click](https://click.palletsprojects.com/)

**Last Updated**: 2026-03-22
