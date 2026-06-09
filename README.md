# MailOps AI

Production-grade Agentic AI platform for autonomous email management, prioritization, workflows, and inbox intelligence.

## Vision

MailOps AI transforms email from a passive inbox into an autonomous operating system powered by AI agents.

Instead of manually sorting, prioritizing, summarizing, and replying to emails, MailOps AI enables intelligent agents to:

- Understand email context
- Prioritize important conversations
- Execute workflows autonomously
- Draft and send responses
- Organize inboxes intelligently
- Learn user behavior over time
- Integrate with external tools and platforms

---

# Core Features

## Inbox Intelligence

- AI-powered email categorization
- Smart priority scoring
- Thread summarization
- Semantic email search
- Deadline and action detection
- VIP sender identification
- Sentiment and urgency analysis

---

## Autonomous Inbox Operations

- Auto-archive and cleanup
- Smart labeling and foldering
- Bulk cleanup agents
- Newsletter and promotion management
- Intelligent retention policies
- Duplicate email detection

---

## AI Workflow Automation

- Draft AI responses
- Auto-reply workflows
- Calendar event extraction
- Task generation
- CRM integrations
- Slack/Discord notifications
- Invoice and receipt extraction

---

## Conversational AI Assistant

Examples:

- "Clean my inbox"
- "Show important unread emails"
- "Summarize today's emails"
- "Archive newsletters older than 30 days"
- "Reply professionally"

---

## Multi-LLM Support

MailOps AI is model-provider agnostic.

Supported providers:

- OpenAI
- Anthropic Claude
- Google Gemini
- Groq
- Ollama
- Local models

---

# System Architecture

```text
                    ┌─────────────────────┐
                    │     Frontend UI     │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │      API Layer      │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌──────────────┐      ┌────────────────┐     ┌────────────────┐
│ Email Engine │      │ Agent Runtime  │     │ Workflow Engine│
└──────┬───────┘      └────────┬───────┘     └────────────────┘
       │                        │
       ▼                        ▼
┌──────────────┐      ┌────────────────┐
│ Gmail/Outlook│      │ Multi-LLM Core │
└──────────────┘      └────────┬───────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
      OpenAI                Claude                Gemini
```

---

# Tech Stack

## Backend

- Python
- FastAPI
- PostgreSQL
- Redis
- Celery / Temporal

## AI & Agents

- LangGraph
- LiteLLM
- PydanticAI
- pgvector

## Frontend

- Next.js
- TailwindCSS

## Infrastructure

- Docker
- Kubernetes
- Terraform

---

# Roadmap

## Phase 1 — Core Infrastructure

- Gmail OAuth integration
- Email synchronization engine
- Thread storage
- Background workers
- Label management

## Phase 2 — AI Intelligence Layer

- Email summarization
- Semantic search
- Categorization
- Priority scoring
- Embedding pipelines

## Phase 3 — Agent Tooling

- Tool calling
- Workflow execution
- Safe autonomous actions
- Confirmation systems

## Phase 4 — Autonomous Agents

- Memory systems
- Behavioral learning
- Multi-step planning
- Proactive inbox management

## Phase 5 — Enterprise Platform

- Multi-tenant architecture
- RBAC
- Compliance
- Billing
- Observability
- Agent analytics

---

# Safety Principles

MailOps AI is designed with strict safety controls.

- Human approval for destructive actions
- Action audit logs
- Rollback support
- Permission boundaries
- Rate limiting
- Encrypted credential storage

---

# Quick Start

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Docker Desktop
- A Gemini API key ([get one free](https://ai.google.dev/gemini-api/docs/api-key))

## Setup

```bash
# 1. Clone and enter the repo
git clone https://github.com/your-org/mailops-ai.git
cd mailops-ai

# 2. Install dependencies with uv
uv venv
source venv/bin/activate
uv pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
```

Edit `.env` with your keys:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mailops
REDIS_URL=redis://localhost:6379
EMBEDDING_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=
```

> Note: `.env` is gitignored — your secrets stay local.

## Run

```bash
# 1. Start PostgreSQL and Redis
docker compose up -d

# 2. Run database migrations
source venv/bin/activate && alembic upgrade head

# 3. Start the API server
source venv/bin/activate && uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8000
```

The API is now live at **http://localhost:8000**. Open **http://localhost:8000/docs** for the interactive Swagger UI.

## Test the APIs

### 1. Health check

```bash
curl http://localhost:8000/health
# {"status":"healthy"}
```

### 2. Gmail profile (requires OAuth)

```bash
curl http://localhost:8000/gmail/profile
```

On first run, a browser window opens for Gmail OAuth consent. After authorizing, a `token.json` file is created for subsequent requests.

### 3. Sync Gmail threads

```bash
curl -X POST http://localhost:8000/sync/gmail
# {"synced_threads": 5, "synced_messages": 12}
```

### 4. Index embeddings (after sync)

```bash
curl -X POST http://localhost:8000/embeddings/index
# {"indexed_messages": 12}
```

### 5. Semantic search

```bash
curl "http://localhost:8000/search?query=meeting+schedule"
```

### 6. Summarize threads

```bash
curl -X POST http://localhost:8000/summary/threads
# {"summarized_threads": 3}
```

> **Quota note**: The free Gemini tier is limited (~60 requests/day). If you get a 429 error, wait for the daily reset or enable billing on your Google Cloud project.

---

# Long-Term Goal

Build the operating system for email powered by autonomous AI agents.

---

# License

MIT License

# Development Progress

## Phase 1 — Infrastructure Core ✅

### Completed

- [x] Monorepo architecture
- [x] FastAPI backend setup
- [x] Environment configuration
- [x] Docker infrastructure
- [x] PostgreSQL integration
- [x] Redis integration
- [x] SQLAlchemy ORM setup
- [x] Alembic migrations
- [x] Initial database schemas
- [x] Health check APIs

---

## Phase 2 — Email Platform Core 🚧

### In Progress

- [x] Gmail OAuth integration
- [x] Gmail API integration
- [ ] Email sync engine
- [ ] Thread ingestion pipeline
- [ ] Incremental sync architecture
- [ ] Background workers

---

## Phase 3 — AI Intelligence Layer ⏳

### Planned

- [ ] Email summarization
- [ ] Semantic search
- [ ] Priority scoring
- [ ] Action detection
- [ ] Embedding pipeline

---

## Phase 4 — Agent Runtime ⏳

### Planned

- [ ] Tool calling
- [ ] Workflow engine
- [ ] Memory system
- [ ] Autonomous inbox actions
- [ ] Human approval layer

---

## Phase 5 — Production Platform ⏳

### Planned

- [ ] Multi-tenant architecture
- [ ] Observability
- [ ] Monitoring
- [ ] CI/CD pipelines
- [ ] Kubernetes deployment
- [ ] Enterprise security

