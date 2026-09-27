# Banking System

Production-oriented implementation of the AI-first Card Emergency Support system.

## Local Backend Development

From the backend directory:

```bash
cd banking-system/backend
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Configuration

Do not store secrets in `.env` files or source control.

Production and AWS development secrets should be stored in AWS Secrets Manager.
Non-sensitive runtime configuration should be provided through CDK configuration,
safe defaults, or documented local configuration when needed.

## Repository Areas

- `backend/`: FastAPI backend and banking service code.
- `frontend/`: Next.js frontend.
- `agent/`: Agent instructions and AgentCore integration assets.
- `lambdas/`: AWS Lambda tool handlers.
- `rag/`: Banking policy documents and retrieval assets.
- `infrastructure/`: AWS CDK infrastructure.
- `evaluation/`: Agent and workflow evaluation assets.
