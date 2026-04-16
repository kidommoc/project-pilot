# Contract: Node.js HTTP Server Template

**Opened**: 2026-04-09 | **Closed**: 2026-04-09 | **Status**: ✅ Completed

## Goal
Create a dedicated project template for Node.js HTTP server development (pure backend, no frontend) to extend project-pilot's template coverage.

## Problem Statement
Current templates don't cleanly fit Node.js HTTP server projects:
- **web-app.md**: Designed for frontend/fullstack; includes public/, pages/, frontend assets that pure servers don't need
- **cli-tool.md**: Focused on command-line interfaces; server lifecycle (port binding, request handling, graceful shutdown) is fundamentally different

Users writing REST APIs, microservices, or backend services need a template that reflects their actual project structure.

## Proposal
Create `references/project-types/nodejs-api-server.md` with:

1. **Standard project structure** optimized for HTTP servers:
   - `src/server.ts` - Server entry point
   - `src/routes/` - Route handlers
   - `src/middleware/` - Express middleware
   - `src/services/` - Business logic layer
   - `src/config/` - Environment configuration

2. **Express-based structure**:
   - Express (battle-tested, middleware ecosystem)
   - Standard middleware patterns (cors, helmet, morgan)

3. **Dev/Prod configuration**:
   - Environment-based config (dev/prod/test)
   - Port management
   - Graceful shutdown handling
   - Request logging setup

4. **Testing approach**:
   - Supertest for HTTP endpoint testing
   - Unit test examples for handlers/services

## Acceptance Criteria
- [x] `references/project-types/nodejs-api-server.md` created with complete structure
- [x] Includes example `package.json` for Express
- [x] Includes `src/server.ts` entry point example
- [x] Includes route organization example (`src/routes/`)
- [x] Includes middleware pattern example
- [x] Includes environment configuration approach
- [x] Includes testing setup with supertest
- [x] `project-init.md` table updated to include the new template
- [x] Phase adjustments documented (P1-P4 specific to server projects)

## Implementation Summary

**Created Files:**
- `references/project-types/nodejs-api-server.md` - Complete Express HTTP server template
- Updated `references/project-init.md` - Added Node.js API Server to template table

**Template Includes:**
- Project directory structure
- package.json with Express + TypeScript + Supertest
- src/server.ts with graceful shutdown
- src/app.ts with middleware stack (helmet, cors, morgan)
- src/config/index.ts for environment variables
- src/routes/ organization pattern
- src/middleware/error-handler.ts
- .env.example
- Testing setup with Vitest + Supertest
- Phase-specific guidance (P1-P3)

## Boundary
- **Touches**: `references/project-types/nodejs-api-server.md`, `references/project-init.md`
- **Does NOT touch**: Agent workspaces, SKILL.md, core workflow logic, existing contracts, examples/

## Notes
- **Tech stack**: Express only
- **Keep it simple**: No ORM, no database layer - focus on HTTP server fundamentals
- **Testing**: Supertest for HTTP endpoint testing
