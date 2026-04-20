# Web Application Project Structure

## Frontend SPA

**Init**: `npm create vite@latest {app-name} -- --template react-ts`

```
{app-name}/
├── package.json
├── tsconfig.json
├── index.html
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   └── utils/
├── public/
├── tests/
└── dist/                     # gitignore
```

## Fullstack (Next.js)

**Init**: `npx create-next-app@latest {app-name}`

```
{app-name}/
├── package.json
├── next.config.js
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── api/
│   ├── components/
│   └── lib/
├── tests/
└── prisma/                   # If using database
```

## Stack Selection

| Type | Stack |
|------|-------|
| Static Site | Next.js + Tailwind |
| SPA | Vite + React + TypeScript |
| Fullstack | Next.js App Router + Prisma |
| Dashboard | React + TanStack Query + shadcn/ui |

## Init Additions

After external tooling, add project-pilot structure (`docs/`, `workspace/`, etc.).
