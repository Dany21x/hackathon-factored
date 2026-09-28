# Banking System

Production-oriented implementation of the AI-first Card Emergency Support system.

## Phase 0 Status

Phase 0 establishes the local repository foundation only:

- backend Python project managed with `uv`
- Ruff and pytest configuration
- frontend Next.js project managed with `npm`
- TypeScript strict mode
- local development commands
- runtime configuration and secrets conventions

AWS infrastructure, AgentCore, Cognito, API Gateway, Lambda deployment, and
banking workflows are introduced in later phases.

## Local Backend Development

From the backend directory:

```bash
cd banking-system/backend
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Local Frontend Development

From the frontend directory:

```bash
cd banking-system/frontend
npm install
npm run dev
npm run lint
npm run typecheck
npm run build
```

## Phase 0 Verification

Backend:

```bash
cd banking-system/backend
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Frontend:

```bash
cd banking-system/frontend
npm run lint
npm run typecheck
npm run build
```

## Runtime Configuration

Do not store secrets in `.env` files or source control.

Production and AWS development secrets should be stored in AWS Secrets Manager.
Non-sensitive runtime configuration should be provided through CDK configuration,
safe defaults, or documented local configuration when needed.

During local development, use only non-sensitive defaults unless a later phase
documents a specific AWS-backed configuration flow.

If a service requires sensitive values, add the required secret to AWS Secrets
Manager through CDK or a documented reproducible script. Do not hardcode secrets
in application code, CDK code, tests, or local config files.

## Repository Areas

- `backend/`: FastAPI backend and banking service code.
- `frontend/`: Next.js frontend.
- `agent/`: Agent instructions and AgentCore integration assets.
- `lambdas/`: AWS Lambda tool handlers.
- `rag/`: Banking policy documents and retrieval assets.
- `infrastructure/`: AWS CDK infrastructure.
- `evaluation/`: Agent and workflow evaluation assets.
