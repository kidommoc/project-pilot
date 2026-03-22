# Web Application 项目结构

适用于前端/全栈 Web 应用开发。

## 标准结构（前端）

```
{app-name}/
├── package.json              # 必需
├── tsconfig.json             # 如使用 TypeScript
├── index.html                # 入口 HTML
├── src/
│   ├── main.ts(x)            # 应用入口
│   ├── App.tsx               # 根组件
│   ├── components/           # 可复用组件
│   │   └── {Component}.tsx
│   ├── pages/                # 页面组件
│   │   └── {Page}.tsx
│   ├── hooks/                # 自定义 hooks
│   ├── utils/                # 工具函数
│   └── styles/               # 样式文件
├── public/                   # 静态资源
│   ├── favicon.ico
│   └── assets/
├── tests/
│   └── {test-file}.test.tsx
└── dist/                     # 构建输出（gitignore）
```

## 标准结构（全栈 - Next.js 示例）

```
{app-name}/
├── package.json
├── next.config.js
├── src/
│   ├── app/                  # App Router
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── api/              # API 路由
│   │       └── {route}/
│   │           └── route.ts
│   ├── components/
│   ├── lib/                  # 共享逻辑
│   └── styles/
├── tests/
└── prisma/                   # 如使用数据库
    └── schema.prisma
```

## 关键文件说明

### package.json

```json
{
  "name": "{app-name}",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "vitest"
  },
  "dependencies": {
    "next": "^14.0",
    "react": "^18.0",
    "react-dom": "^18.0"
  },
  "devDependencies": {
    "@types/node": "^20.0",
    "@types/react": "^18.0",
    "typescript": "^5.0",
    "vitest": "^1.0"
  }
}
```

## 开发流程调整

### Phase 1: Specification

额外明确：
- [ ] 前端框架（React/Vue/Svelte/Next.js）
- [ ] 是否需要后端 API
- [ ] 数据库需求（如适用）
- [ ] 部署目标（Vercel/Netlify/自托管）

### Phase 2: Implementation

- [ ] 组件驱动开发
- [ ] 响应式设计
- [ ] API 集成（如适用）

### Phase 3: Review

额外检查：
- [ ] 构建无错误（`npm run build`）
- [ ] Lint 通过（`npm run lint`）
- [ ] 测试通过
- [ ] 跨浏览器测试（如需要）

### Phase 4: Release

- [ ] 构建优化
- [ ] 环境变量配置
- [ ] 部署脚本/CI 配置

## 测试建议

```typescript
// tests/components/Button.test.tsx
import { render, screen } from '@testing-library/react';
import { Button } from '../src/components/Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});
```

## 常见技术栈

| 类型 | 推荐栈 |
|------|--------|
| **静态站点** | Next.js + Tailwind |
| **SPA** | Vite + React + TypeScript |
| **全栈** | Next.js App Router + Prisma |
| **Dashboard** | React + TanStack Query + shadcn/ui |

---

**参考**:
- [Next.js 文档](https://nextjs.org/docs)
- [Vite 文档](https://vitejs.dev/)

**Last Updated**: 2026-03-22
