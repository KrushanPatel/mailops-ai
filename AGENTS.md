# AGENTS.md — MailOps AI

## Repo structure

```
apps/           # Application entrypoints
  api/          # FastAPI app — main.py, routes/, services/, models/, core/
  agent/        # Agent runtime (stub — runtime.py is empty)
  worker/       # Background worker (stub)
  web/          # Frontend (placeholder)
packages/       # Shared libraries
  email_core/   # Gmail OAuth, sync engine, email parser
  llm_router/   # LLM provider abstraction (Gemini only, OpenAI/Anthropic stubs)
  memory/       # Vector store (stub)
  prompts/      # Prompt templates
  shared/       # Utils & constants (stubs)
  workflows/    # Workflow engine (stub)
```

## Entrypoints & commands

- **API server**: `uvicorn apps.api.main:app --reload` (must run from repo root — all imports are absolute)
- **Migrations**: `alembic upgrade head`
- **DB + Redis**: `docker compose up` (PostgreSQL 16 + pgvector, Redis 7)
- **Settings** (from `.env`): `DATABASE_URL`, `REDIS_URL`, `EMBEDDING_PROVIDER`, `GEMINI_API_KEY`, `OPENAI_API_KEY`
- **Gmail auth**: `credentials.json` + `token.json` — manual OAuth flow on first run

## Key gotchas

- **Run everything from repo root** — imports like `from apps.api.core.database import Base` are absolute to project root
- **Only Gemini is wired** — `EMBEDDING_PROVIDER=gemini`. OpenAI/Anthropic providers are empty stubs
- **Factory quirk** — `get_chat_provider()` reads `settings.EMBEDDING_PROVIDER` (not a separate chat setting) to decide which LLM to use
- **Embedding dimension**: 3072 (gemini-embedding-001 → `Vector(3072)` in Message model)
- **Model/drift mismatch**: migration `5e2c7f30aa75` created `threads.summary` as `String`, but model `thread.py` has it as `Text`; migration also has `priority_score` and `created_at` columns that the model file lacks
- **Many stubs**: `agent/runtime.py`, `worker/worker.py`, `memory/vector_store.py`, `workflows/engine.py`, `shared/utils.py`, `shared/constants.py`, `llm_router/openai_provider.py`, `llm_router/anthropic_provider.py`, `api/core/security.py`, `api/schemas/__init__.py`, `pyproject.toml`, `.env.example`, `CONTRIBUTING.md`, `.github/workflows/api-ci.yml` — all empty
- **No tests exist** anywhere in the repo
- **No lint/format config** — black, isort, and pylint are in `requirements.txt` but unconfigured
- **`.env` is gitignored** — copy `.env.example` (also empty) to create one
- **`docker-compose.yml`** only defines postgres + redis — no API/worker service

## Conventions

- FastAPI route files in `apps/api/routes/`, models in `apps/api/models/`, services in `apps/api/services/`
- DB session via `Depends(get_db)` or manual `SessionLocal()` (both patterns exist)
- LLM providers extend `BaseChatProvider` / `BaseEmbeddingProvider` with a `generate()` / `generate_embedding()` method
- Alembic `env.py` imports `apps.api.core.database.Base` and all models directly for autogenerate
