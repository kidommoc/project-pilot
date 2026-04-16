# Web Application Project Structure

For frontend/fullstack web application development.

## Standard Structure (Frontend)

```
{app-name}/
├── package.json              # Required
├── tsconfig.json             # If using TypeScript
├── index.html                # Entry HTML
├── README.md                 # Project overview
├── CHANGELOG.md              # Version history
├── docs/                    # project-pilot docs (specs, contracts, interfaces)
│   ├── contracts/
│   └── interfaces/
├── workspace/               # project-pilot working state (symlinks)
│   ├── draft/                # Awaiting human confirmation
│   ├── open/                 # Confirmed, waiting to start
│   ├── in_progress/          # Current focus (exactly 1)
│   └── archived/             # Completed
├── docs/                     # Project documentation
│   ├── decisions/            # ADR - Architecture Decision Records
│   └── interfaces/           # API interfaces (if applicable)
├── references/               # Reference materials
│   ├── guides/
│   ├── templates/
│   └── ...
├── src/
│   ├── main.ts(x)            # Application entry
│   ├── App.tsx               # Root component
│   ├── components/           # Reusable components
│   │   └── {Component}.tsx
│   ├── pages/                # Page components
│   │   └── {Page}.tsx
│   ├── hooks/                # Custom hooks
│   ├── utils/                # Utility functions
│   └── styles/               # Style files
├── public/                   # Static assets
│   ├── favicon.ico
│   └── assets/
├── tests/
│   └── {test-file}.test.tsx
└── dist/                     # Build output (gitignore)
```

## Standard Structure (Fullstack - Next.js Example)

```
{app-name}/
├── package.json
├── next.config.js
├── README.md                 # Project overview
├── CHANGELOG.md              # Version history
├── docs/                    # project-pilot docs (specs, contracts, interfaces)
│   ├── contracts/
│   └── interfaces/
├── workspace/               # project-pilot working state (symlinks)
│   ├── draft/                # Awaiting human confirmation
│   ├── open/                 # Confirmed, waiting to start
│   ├── in_progress/          # Current focus (exactly 1)
│   └── archived/             # Completed
├── docs/                     # Project documentation
│   ├── decisions/            # ADR - Architecture Decision Records
│   └── interfaces/           # API interfaces
├── references/               # Reference materials
│   ├── guides/
│   ├── templates/
│   └── ...
├── src/
│   ├── app/                  # App Router
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── api/              # API routes
│   │       └── {route}/
│   │           └── route.ts
│   ├── components/
│   ├── lib/                  # Shared logic
│   └── styles/
├── tests/
└── prisma/                   # If using database
    └── schema.prisma
```

## Key Files

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

## Development Process Adjustments

### Phase 1: Specification

Additional clarifications:
- [ ] Frontend framework (React/Vue/Svelte/Next.js)
- [ ] Is backend API needed?
- [ ] Database requirements (if applicable)
- [ ] Deployment target (Vercel/Netlify/self-hosted)

### Phase 2: Implementation

- [ ] Component-driven development
- [ ] Responsive design
- [ ] API integration (if applicable)

### Phase 3: Audit

Additional checks:
- [ ] Build has no errors (`npm run build`)
- [ ] Lint passes (`npm run lint`)
- [ ] Tests pass
- [ ] Cross-browser testing (if needed)

### Phase 4: Release

- [ ] Build optimization
- [ ] Environment variable configuration
- [ ] Deployment scripts/CI configuration

## Testing Recommendations

```typescript
// tests/components/Button.test.tsx
import { render, screen } from '@testing-library/react';
import { Button } from '../src/components/Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});
```

## Common Tech Stacks

| Type | Recommended Stack |
|------|-------------------|
| **Static Site** | Next.js + Tailwind |
| **SPA** | Vite + React + TypeScript |
| **Fullstack** | Next.js App Router + Prisma |
| **Dashboard** | React + TanStack Query + shadcn/ui |

---

**Reference**:
- [Next.js Documentation](https://nextjs.org/docs)
- [Vite Documentation](https://vitejs.dev/)

## Project Pilot Integration

**Use project-pilot for structured development**:

1. **Activation**: Say "Use project-pilot for this web app"
2. **Contract**: Create Contract for each feature/modification
3. **Interface Docs**: Document APIs in `docs/interfaces/`
4. **ADRs**: Record architectural decisions (e.g., framework choice)

**Documentation** (AI-First):
- **Required**: Contract files, Interface docs, ADRs
- **Optional**: `docs/` for user docs
- **Not needed**: Completion reports, architecture docs

---

**Last Updated**: 2026-04-02 (project-pilot 1.2.0)
