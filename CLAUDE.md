# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

## Project: MailOps AI

See [AGENTS.md](./AGENTS.md) for full repo reference. Key facts:

- **Monorepo**: `apps/` (api, agent, worker, web) + `packages/` (email_core, llm_router, memory, prompts, shared, workflows)
- **API server**: `uvicorn apps.api.main:app --reload` — must run from repo root (all imports are absolute, e.g. `from apps.api.core.database import Base`)
- **Migrations**: `alembic upgrade head` (new revision: `alembic revision -m "..."`)
- **Infra**: `docker compose up -d` starts PostgreSQL 16 (pgvector) + Redis 7 only — no API/worker service defined in compose
- **Lint**: `black --check . && isort --check-only --diff . && pylint apps/ packages/ --fail-under=6`
- **Tests**: `pytest -v --tb=short` — no tests exist yet; CI runs this and pylint non-blocking (`|| true`)

### LLM providers (`packages/llm_router/`)
- Built on LangChain's `init_chat_model()` / `init_embeddings()` — provider-agnostic by construction, no per-provider Python files
- `settings.py`: `LLMSettings(BaseSettings)` holds `CHAT_PROVIDER`/`CHAT_MODEL`/`CHAT_API_KEY`/`CHAT_BASE_URL` and the `EMBEDDING_*` equivalents, loaded from `.env`
- `factory.py`: `get_chat_provider()` returns a LangChain `BaseChatModel` (call `.invoke(prompt).content`); `get_embedding_provider()` returns a LangChain `Embeddings` (call `.embed_query(text)`)
- Switching or adding a provider is an env var change, not a code change — any `model_provider` LangChain's `init_chat_model`/`init_embeddings` supports works (`openai`, `anthropic`, `google_genai`, `deepseek`, `ollama`, ...), as long as its `langchain-<provider>` package is installed. Currently installed: `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-deepseek`, `langchain-ollama`
- `init_embeddings()` supports fewer providers than `init_chat_model()` (notably no `anthropic`, no `deepseek` as of langchain 1.4) — check LangChain's docs before picking an `EMBEDDING_PROVIDER`
- Embedding dimension is fixed at 3072 (`Vector(3072)` in `apps/api/models/message.py`, sized for Gemini's `gemini-embedding-001`) — swapping embedding providers/models requires a matching column-size migration

### API layer
- One router per feature in `apps/api/routes/`, included in `apps/api/main.py`:
  - `gmail.py` → `GET /gmail/profile`
  - `sync.py` → `POST /sync/gmail`
  - `search.py` → `POST /embeddings/index`, `GET /search`
  - `summary.py` → `POST /summary/threads`
- Routes call `apps/api/services/*` (`gmail_sync_service.py`, `semantic_search_service.py`, `thread_summary_service.py`), which use the SQLAlchemy models directly — no repository/DAO layer
- DB sessions: both `Depends(get_db)` and manual `SessionLocal()` are used interchangeably across routes — match whichever the file you're editing already uses
- Gmail access goes through `packages/email_core/` (`gmail_auth.py`, `gmail_provider.py`, `parser.py`, `sync_engine.py`); OAuth relies on local `credentials.json`/`token.json`, not the DB

### Known drift / stubs
- Migration `5e2c7f30aa75` created `threads.summary` as `String` and added `priority_score`/`created_at` columns; `apps/api/models/thread.py` has `summary` as `Text` and lacks those two columns — model and applied schema are out of sync
- Empty stub files: `apps/agent/runtime.py`, `apps/worker/worker.py`, `packages/memory/vector_store.py`, `packages/workflows/engine.py`, `packages/shared/utils.py`, `packages/shared/constants.py`, `apps/api/core/security.py`, `apps/api/schemas/__init__.py`
