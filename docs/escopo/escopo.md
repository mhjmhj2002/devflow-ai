# 🚀 DevFlow AI

## AI-Powered SDLC Automation Platform

DevFlow AI is a modern engineering automation platform focused on automating parts of the Software Development Life Cycle (SDLC) using Artificial Intelligence, GitHub events and workflow orchestration.

The platform aims to simulate how next-generation engineering organizations will operate:
- GitHub-driven development
- AI-assisted planning
- Event-driven workflows
- Autonomous code generation
- Intelligent orchestration
- Human-in-the-loop approvals

---

# 🧠 Project Vision

The idea behind DevFlow AI is to create a platform capable of:

1. Receiving GitHub events
2. Understanding software project context
3. Generating technical implementation plans
4. Interacting directly with GitHub issues and pull requests
5. Automating development workflows
6. Assisting engineering teams with AI agents

The platform is NOT intended to replace developers.

Instead, the goal is to:
- accelerate engineering workflows
- reduce repetitive tasks
- automate SDLC operations
- improve developer productivity
- simulate real-world AI engineering platforms

---

# 🎯 Current Objective

The current focus is NOT building a perfect enterprise platform.

The focus is:
- build a functional MVP
- create a strong technical portfolio project
- demonstrate architecture knowledge
- showcase AI orchestration skills
- create something visually impressive in interviews
- simulate modern engineering workflows used by large companies

---

# 🏗️ Architecture Strategy

The project follows a monorepo architecture.

Reasoning:
- easier local development
- easier demonstration
- simpler onboarding
- faster iteration
- centralized infrastructure
- ideal for portfolio projects

---

# 📦 Planned Monorepo Structure

```text
devflow-ai/
│
├── devflow-orchestrator/
├── devflow-web/
├── services/
│   ├── identity-service/
│   └── workflow-service/
│
├── infra/
│   ├── postgres/
│   ├── rabbitmq/
│   ├── redis/
│   └── docker-compose.yml
│
├── docs/
│
└── README.md
````

---

# 🧠 Main Components

---

# 1. devflow-orchestrator

The core AI orchestration service.

Responsibilities:

* GitHub webhooks
* AI planning workflows
* issue orchestration
* GitHub comments
* AI agents
* context analysis
* future code generation
* future PR automation

Tech stack:

* Python
* FastAPI
* OpenAI SDK
* Pydantic
* Uvicorn

This is the MOST important component of the platform.

---

# 2. devflow-web

Frontend dashboard.

Responsibilities:

* workflow visualization
* issue monitoring
* approval flows
* execution tracking

Planned stack:

* Next.js
* TailwindCSS

---

# 3. identity-service

Authentication and authorization service.

Responsibilities:

* users
* JWT
* permissions
* authentication

Planned stack:

* Java 21
* Spring Boot
* PostgreSQL

---

# 4. workflow-service

Workflow execution service.

Responsibilities:

* workflow state
* execution history
* orchestration metadata
* approval lifecycle

Planned stack:

* Java 21
* Spring Boot
* PostgreSQL

---

# 5. Infrastructure Layer

Shared platform infrastructure.

Components:

* RabbitMQ
* Redis
* PostgreSQL
* Docker Compose
* observability tools

---

# 🧠 Core SDLC Workflow

The primary workflow currently envisioned:

```text
Developer creates GitHub Issue
                ↓
GitHub Webhook triggers DevFlow AI
                ↓
Orchestrator receives event
                ↓
Project Context Builder analyzes repository
                ↓
AI Planning Agent generates technical plan
                ↓
Plan is posted as Markdown comment in GitHub Issue
                ↓
Developer reviews the plan
                ↓
Developer approves using:
"approve plan"
                ↓
Future phase:
AI generates implementation code
                ↓
Future phase:
Automatic Pull Request creation
```

---

# 🧠 Current Functional Scope (Phase 1)

The platform already contains or partially contains:

## ✅ GitHub Webhook Receiver

FastAPI endpoint receiving GitHub events.

---

## ✅ GitHub Event Normalization

Normalization layer converting raw GitHub payloads into internal events.

---

## ✅ Workflow Routing

Internal routing system dispatching workflows based on event types.

---

## ✅ Context Builder

Project structure analysis engine.

Current capabilities:

* language detection
* framework detection
* build tool detection
* source directory discovery
* architecture hints

---

## ✅ Stack Detection

Current support:

* Java
* Spring Boot
* Maven

Future:

* Gradle
* Node.js
* Python
* .NET

---

## ✅ AI Planning Agent

Generates implementation plans based on:

* issue title
* project stack
* repository structure
* framework context

---

## ✅ GitHub Comment Automation

Posts AI-generated plans back to GitHub issues.

---

# 🚧 Planned Future Features

---

# Phase 2 — Code Generation

Future capabilities:

* generate controllers
* generate services
* generate repositories
* generate DTOs
* generate entities
* create branches
* commit code automatically
* open pull requests automatically

---

# Phase 3 — Event-Driven Architecture

Future infrastructure:

* RabbitMQ
* async workflows
* distributed events
* Redis cache
* workflow queues

Example events:

* issue.received
* plan.generated
* code.generated
* pr.created

---

# Phase 4 — Frontend Dashboard

Planned capabilities:

* execution dashboard
* workflow monitoring
* approval UI
* issue tracking
* PR visualization

---

# 🧠 Architectural Principles

The platform follows these principles:

* Event-driven architecture
* Separation of concerns
* AI orchestration
* Human-in-the-loop approval
* Context-aware AI generation
* Workflow modularization
* Scalability-oriented design
* Developer experience first

---

# 🚨 Important Strategic Decisions

---

## Monorepo Instead of Multiple Repositories

Reason:

* easier development
* easier onboarding
* easier demonstrations
* faster local setup

---

## Focus on Demonstrable Value

The project is intentionally optimized for:

* portfolio quality
* technical interviews
* architectural demonstration
* modern engineering practices

NOT for:

* hyperscale production deployment
* Kubernetes complexity
* unnecessary distributed complexity

---

## AI as Engineering Accelerator

The platform is NOT intended to fully replace developers.

The philosophy is:

* AI accelerates engineering
* developers remain responsible for decisions
* human approval remains mandatory

---

# 🧠 Current Tech Stack

## Backend AI

* Python 3.10+
* FastAPI
* OpenAI SDK
* Pydantic

---

## Backend Services

* Java 21
* Spring Boot 3.5+

---

## Infrastructure

* Docker Compose
* PostgreSQL
* RabbitMQ (planned)
* Redis (planned)

---

## Frontend

* Next.js (planned)
* TailwindCSS (planned)

---

# 🧠 Development Environment

Primary IDE:

* IntelliJ IDEA

AI Assistant:

* GitHub Copilot

Reasoning and architecture support:

* ChatGPT

---

# 🧠 Development Philosophy

The project prioritizes:

* clean architecture
* real-world workflows
* engineering readability
* demonstrable automation
* practical AI usage

The project intentionally simulates:

* internal developer platforms
* AI engineering copilots
* autonomous SDLC tooling
* modern platform engineering

---

# 🚀 Long-Term Vision

Long term, DevFlow AI could evolve into:

* autonomous engineering platform
* AI-powered GitHub assistant
* workflow orchestration engine
* internal developer platform
* engineering automation toolkit

---

# 🧠 Important Context for AI Assistants

When generating code or architecture decisions for this project:

ALWAYS prioritize:

* modularity
* readability
* modern architecture
* event-driven patterns
* clean naming
* production-like structure
* portfolio-quality code

AVOID:

* tutorial-level code
* overengineering
* unnecessary complexity
* tightly coupled modules
* fake enterprise abstractions

The project should feel:

* modern
* realistic
* technically impressive
* clean
* maintainable

---

# ✅ Current Priority

The CURRENT focus is:

## Finish Phase 1 completely:

* webhook
* planning workflow
* GitHub integration
* AI-generated Markdown plans
* approval workflow

Only AFTER that:

* code generation
* PR automation
* event bus
* frontend

---

# 👨‍💻 Author Context

This project is being developed as:

* portfolio project
* AI engineering showcase
* architecture study
* interview demonstration platform

The goal is to create a realistic modern engineering platform that demonstrates:

* backend architecture
* AI integration
* SDLC automation
* workflow orchestration
* event-driven systems
* modern engineering practices

---

```
```
