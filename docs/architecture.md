# MailOps AI — System Architecture

## Overview

MailOps AI is an AI-native email intelligence platform that transforms traditional email workflows into an intelligent memory, retrieval, and automation system.

The platform currently supports:

* Gmail OAuth authentication
* Gmail inbox synchronization
* Email thread ingestion
* PostgreSQL persistence
* Semantic vector embeddings
* AI semantic search
* Thread summarization
* Provider abstraction for LLMs

---

# High-Level Architecture

```text
                        ┌─────────────────────┐
                        │      Gmail API      │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   OAuth Layer       │
                        │ Google Authentication│
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Sync Engine       │
                        │ Incremental Sync    │
                        └──────────┬──────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     ▼                           ▼
          ┌──────────────────┐        ┌──────────────────┐
          │ Thread Parser    │        │ Message Parser   │
          └────────┬─────────┘        └────────┬─────────┘
                   │                            │
                   └────────────┬───────────────┘
                                ▼
                    ┌────────────────────────┐
                    │ PostgreSQL + pgvector │
                    └───────────┬────────────┘
                                │
              ┌─────────────────┴─────────────────┐
              ▼                                   ▼
    ┌────────────────────┐             ┌────────────────────┐
    │ Embedding Pipeline │             │ Summarization Layer│
    └─────────┬──────────┘             └─────────┬──────────┘
              │                                  │
              ▼                                  ▼
     ┌──────────────────┐              ┌──────────────────┐
     │ Gemini Embedding │              │ Gemini Chat LLM  │
     └────────┬─────────┘              └────────┬─────────┘
              │                                  │
              └──────────────┬───────────────────┘
                             ▼
                  ┌─────────────────────┐
                  │ AI Intelligence API │
                  └─────────────────────┘
```

---

# Repository Structure

```text
MailOps-AI/
│
├── apps/
│   └── api/
│       ├── core/
│       ├── models/
│       ├── routes/
│       └── services/
│
├── packages/
│   ├── email_core/
│   ├── llm_router/
│   ├── memory/
│   ├── prompts/
│   ├── shared/
│   └── workflows/
│
├── alembic/
├── infrastructure/
├── docs/
└── docker-compose.yml
```

---

# Core Components

## 1. API Layer

Location:

```text
apps/api/
```

Responsibilities:

* REST APIs
* Route management
* Dependency injection
* Database sessions
* Service orchestration

Main Technologies:

* FastAPI
* SQLAlchemy
* Pydantic

---

# 2. Email Infrastructure Layer

Location:

```text
packages/email_core/
```

Responsibilities:

* Gmail sync engine
* Email parsing
* Thread ingestion
* Incremental synchronization

Features:

* Duplicate prevention
* Thread tracking
* Message normalization
* Gmail metadata extraction

---

# 3. Database Layer

Database:

* PostgreSQL
* pgvector extension

Responsibilities:

* Persistent email storage
* Semantic vector storage
* AI summaries
* Metadata indexing

Main Tables:

## users

Stores user identity and tenant ownership.

## threads

Stores:

* Gmail thread IDs
* Subjects
* AI-generated summaries

## messages

Stores:

* Sender
* Email body
* Cleaned content
* Embedding vectors

---

# 4. Embedding Layer

Location:

```text
packages/llm_router/
```

Responsibilities:

* Embedding generation
* Vector provider abstraction
* Future multi-provider support

Current Provider:

* Gemini Embeddings

Current Model:

```text
gemini-embedding-001
```

Vector Dimension:

```text
3072
```

Purpose:

Transforms emails into semantic vectors for AI retrieval.

---

# 5. Semantic Search Layer

Responsibilities:

* Vector similarity search
* AI retrieval
* Semantic inbox querying

Pipeline:

```text
User Query
   ↓
Embedding Generation
   ↓
pgvector Similarity Search
   ↓
Nearest Semantic Emails
```

Current Search Type:

* Cosine similarity

---

# 6. AI Summarization Layer

Responsibilities:

* Thread summarization
* Context compression
* Memory optimization

Pipeline:

```text
Thread Messages
   ↓
Prompt Construction
   ↓
Gemini Chat Model
   ↓
AI Summary
   ↓
Database Persistence
```

Purpose:

Convert long email threads into concise AI-readable memory.

---

# 7. LLM Provider Abstraction

Location:

```text
packages/llm_router/
```

Purpose:

Avoid vendor lock-in.

Current Providers:

* Gemini Embeddings
* Gemini Chat

Future Providers:

* OpenAI
* Claude
* Ollama
* Mistral
* Groq
* TogetherAI

Architecture:

```text
Base Provider
    ↓
Factory Router
    ↓
Specific Provider Implementation
```

---

# Current AI Capabilities

## Implemented

### Gmail Sync

```text
POST /sync/gmail
```

### Embedding Indexing

```text
POST /embeddings/index
```

### Semantic Search

```text
POST /search
```

### Thread Summarization

```text
POST /summary/threads
```

---

# Current Data Flow

```text
Gmail Inbox
    ↓
OAuth Authentication
    ↓
Sync Engine
    ↓
Parser
    ↓
PostgreSQL Storage
    ↓
Embedding Generation
    ↓
pgvector Index
    ↓
Semantic Retrieval
    ↓
AI Summarization
```

---

# Docker Infrastructure

Services:

## PostgreSQL + pgvector

Container:

```text
mailops-postgres
```

Responsibilities:

* relational storage
* vector search
* semantic memory

## Redis

Container:

```text
mailops-redis
```

Responsibilities:

* caching
* background workers
* future queues

---

# Migrations

Tool:

* Alembic

Purpose:

* schema versioning
* production-safe migrations
* vector schema evolution

Workflow:

```bash
alembic revision --autogenerate -m "message"

alembic upgrade head
```

---

# Current Platform Status

## Completed

### Infrastructure Core

* FastAPI backend
* Docker infrastructure
* PostgreSQL
* Redis
* SQLAlchemy ORM
* Alembic migrations

### Email Platform Core

* Gmail OAuth
* Gmail sync engine
* Thread ingestion
* Incremental sync

### AI Semantic Layer

* pgvector integration
* Embeddings pipeline
* Semantic search
* Vector retrieval

### AI Intelligence Layer

* Thread summarization
* LLM abstraction
* AI memory compression

---

# Planned Future Architecture

## Intelligence Features

* Action item extraction
* Priority scoring
* AI categorization
* Daily digest generation
* Workflow intelligence

## Agent Runtime

* Autonomous inbox actions
* Human approval layer
* AI copilots
* Workflow engine

## Production Platform

* Multi-tenancy
* Kubernetes deployment
* Observability
* Monitoring
* Enterprise security

---

# Long-Term Vision

MailOps AI is evolving into:

```text
AI Operating System for Email
```

The goal is to transform email from:

```text
passive communication storage
```

into:

```text
active AI memory and workflow intelligence
```

