# 🤖 Agentic Platform

AI-powered agent orchestration platform focused on autonomous software development workflows.

This project receives GitHub events, analyzes repositories, understands project context, and prepares AI-driven execution flows for tasks such as planning, code generation, pull request creation, and engineering automation.

---

# 🚀 Vision

The goal of this platform is to simulate and evolve an autonomous engineering system capable of:

* Reading GitHub Issues
* Understanding repository architecture
* Detecting stack and technologies automatically
* Generating implementation plans with AI
* Orchestrating development workflows
* Creating branches and Pull Requests
* Supporting multi-repository environments
* Acting as an AI Software Engineer assistant

This project is heavily inspired by modern Agentic AI concepts and AI SDLC orchestration platforms.

---

# 🧠 Current Features

## ✅ Implemented

* FastAPI backend
* GitHub webhook ingestion
* GitHub event normalization
* Workflow routing
* Repository scanning
* Stack detection
* Multi-project context architecture
* Planning workflow foundation
* Structured logging
* OpenAPI/Swagger support
* Local webhook testing
* ngrok integration support

---

# 🏗️ Project Architecture

```text
agentic-platform/
├── app/
│
│   ├── api/
│   │   └── webhook.py
│   │
│   ├── agents/
│   │   └── planning_agent.py
│   │
│   ├── workflows/
│   │   ├── workflow_router.py
│   │   ├── dispatcher.py
│   │   └── issue_workflow.py
│   │
│   ├── github/
│   │   └── normalizer.py
│   │
│   ├── llm/
│   │
│   ├── skills/
│   │
│   ├── project_context/
│   │   ├── context_builder.py
│   │   ├── scanner.py
│   │   └── stack_detector.py
│   │
│   ├── prompts/
│   │
│   ├── memory/
│   │
│   ├── state/
│   │
│   ├── core/
│   │   └── logger.py
│   │
│   ├── schemas/
│   │   └── github.py
│   │
│   └── main.py
│
├── tests/
├── docker/
├── docs/
├── requirements.txt
├── .env
├── .gitignore
└── docker-compose.yml
```

---

# ⚙️ Tech Stack

## Backend

* Python 3.10+
* FastAPI
* Uvicorn

## AI / Agentic

* OpenAI API
* Modular Agent Architecture

## Infrastructure

* GitHub Webhooks
* ngrok
* Docker (future)
* Docker Compose

## Architecture Concepts

* Workflow orchestration
* Context-aware agents
* Repository intelligence
* Event-driven automation
* Multi-repository support

---

# 🧩 Supported Repository Detection

The platform currently detects:

| Technology  | Detection |
| ----------- | --------- |
| Java        | ✅         |
| Spring Boot | ✅         |
| Maven       | ✅         |
| Gradle      | Planned   |
| Python      | Planned   |
| Node.js     | Planned   |

---

# 🔥 How the Workflow Works

## Example Flow

```text
GitHub Issue Opened
        ↓
Webhook received
        ↓
Event normalization
        ↓
Workflow routing
        ↓
Repository context scan
        ↓
Stack detection
        ↓
Planning agent execution
        ↓
AI-generated implementation plan
```

---

# 📦 Requirements

Install:

* Python 3.10+
* pip
* git
* ngrok account

---

# 🛠️ Environment Setup

## 1. Clone the repository

```bash
git clone https://github.com/mhjmhj2002/agentic-platform.git

cd agentic-platform
```

---

## 2. Create virtual environment

```bash
python3 -m venv venv
```

---

## 3. Activate virtual environment

### Linux / Linux Mint / Ubuntu

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 Environment Variables

Create a `.env` file:

```bash
touch .env
```

Example:

```env
OPENAI_API_KEY=your_openai_key

GITHUB_TOKEN=your_github_token
GITHUB_OWNER=your_github_user

DEBUG=true
ENVIRONMENT=dev
```

---

# ▶️ Running the Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

OpenAPI JSON:

```text
http://localhost:8000/openapi.json
```

---

# 🔌 GitHub Webhook Configuration

## Why ngrok?

GitHub needs to access your local machine.

ngrok creates a secure public tunnel to your local FastAPI server.

---

# 🌐 Installing ngrok

## Linux

```bash
sudo snap install ngrok
```

---

# 🔑 Configure ngrok account

Create account:

```text
https://dashboard.ngrok.com/signup
```

Get your token:

```text
https://dashboard.ngrok.com/get-started/your-authtoken
```

Configure locally:

```bash
ngrok config add-authtoken YOUR_TOKEN
```

---

# 🚀 Start ngrok

Expose FastAPI port:

```bash
ngrok http 8000
```

Example output:

```text
https://abc123.ngrok-free.app
```

---

# 🔗 GitHub Webhook URL

Configure in repository:

```text
GitHub Repository
→ Settings
→ Webhooks
→ Add webhook
```

Payload URL:

```text
https://YOUR_NGROK_URL/webhook/github
```

Example:

```text
https://abc123.ngrok-free.app/webhook/github
```

---

# 📌 Webhook Settings

| Setting      | Value            |
| ------------ | ---------------- |
| Content type | application/json |
| Events       | Issues           |
| Active       | ✅                |

---

# 🧪 Local Testing

## Test endpoint manually

```bash
curl -X POST \
  'http://localhost:8000/webhook/github' \
  -H 'accept: application/json' \
  -H 'x-github-event: issues' \
  -H 'Content-Type: application/json' \
  -d '{
  "action": "opened",
  "repository": {
    "name": "agentic-ms-user"
  },
  "issue": {
    "number": 1,
    "title": "Create POST /users endpoint"
  }
}'
```

---

# 📋 Example Response

```json
{
  "status": "planning",
  "issue": "Create POST /users endpoint"
}
```

---

# 🧠 Context-Aware Repository Analysis

The platform scans repositories dynamically.

Example detected information:

```json
{
  "repository": "agentic-ms-user",
  "language": "Java",
  "framework": "Spring Boot",
  "build_tool": "Maven"
}
```

This allows AI agents to generate implementation plans specific to each repository stack.

---

# 📚 OpenAPI / Swagger

FastAPI automatically generates API documentation.

Access:

```text
http://localhost:8000/docs
```

This is extremely useful for:

* frontend integration
* testing
* webhook debugging
* API exploration

---

# 🧪 Logging

Structured logs are enabled.

Example:

```text
2026-05-09 17:27:12 | INFO | Starting workflow for repo=agentic-ms-user
```

---

# 🛡️ Recommended `.gitignore`

```gitignore
# Python
venv/
__pycache__/
*.pyc

# IDEs
.idea/
.vscode/
.project
.classpath
.settings/

# Environment
.env

# Build
target/
```

---

# 🚧 Roadmap

## Planned Features

* OpenAI integration
* PR creation
* Branch automation
* Code generation
* Multi-agent orchestration
* RAG repository memory
* Semantic repository search
* CI/CD integration
* LangGraph workflows
* Autonomous PR review
* Test generation
* Docker runtime
* Kubernetes deployment

---

# 🧠 Architecture Direction

This project is evolving toward:

* AI Engineering Platform
* Agentic SDLC
* Autonomous Development Workflows
* AI-native Engineering Automation

---

# ⚠️ Important Notes

## This project is experimental

The platform is intended for:

* learning
* architecture exploration
* AI engineering research
* developer productivity experiments

Do NOT use in production without hardening security and execution controls.

---

# 👨‍💻 Author

Created as a study and innovation project focused on:

* Agentic AI
* AI orchestration
* Backend architecture
* Engineering automation
* AI developer platforms
