# Plano do Projeto — DevFlow AI

Visão curta
--------------
Transformar o trabalho experimental existente em uma plataforma profissional (startup-level portfolio) para automação do SDLC usando IA, com prioridade em um orquestrador (`devflow-orchestrator`) que recebe webhooks do GitHub, analisa contexto do repositório, gera planos técnicos em Markdown e faz a interação inicial com issues (comentários e fluxos de aprovação).

Checklist (uso diário)
- [ ] Fase 1 completa e demonstrável: webhook → contexto → plano → comentário
- [ ] Demo local com ngrok ou similar
- [ ] README e scripts de execução local (requirements, run-local.sh)
- [ ] Testes unitários básicos para planner, normalizer e detector de stack
- [ ] Backlog priorizado para Fase 2 (codegen)

Estrutura proposta do monorepo
---------------------------------
devflow-ai/
├── devflow-orchestrator/     # Core (FastAPI, agentes, workflows)
├── devflow-gateway/         # API Gateway (fase avançada)
├── devflow-web/             # Frontend (Next.js)
├── identity-service/        # Microsserviço auth (fase avançada)
├── workflow-service/        # Histórico/estado dos workflows
└── infra/                   # docker-compose, postgres, rabbitmq, redis

Princípios de design
- Reaproveitar código bom, sem arrastar dívida técnica
- Nomes com identidade (evitar `ms-user`, `api-web`) — usar `devflow-*`
- Modularidade e separação de responsabilidades
- Human-in-the-loop como requisito de segurança na geração de código
- Desenvolver por fases: primeiro orquestrador (MVP), depois infra e microsserviços

Roadmap por fases (alto nível)
--------------------------------
Fase 1 — Core IA (prioridade máxima)
- Objetivo: receber Issue → gerar plano técnico → postar comentário
- Entregáveis:
  - Endpoint de webhook robusto e normalizador
  - Context builder (detecção de linguagem/stack)
  - Planning agent (prompt + LLM client)
  - GitHub commenter
  - Flow de aprovação (detectar comentário "approve plan")
  - README + run-local script + exemplo de payload
- Critério de aceitação: demo end-to-end local com payload real/simulado

Fase 2 — Geração de código
- Objetivo: gerar artefatos (controllers, services, repos, DTOs) e criar PR
- Entregáveis:
  - Sandbox de geração (evitar execução automática insegura)
  - Gerador de arquivos e branch/commit automático
  - PR criado com template e checklist
- Critério de aceitação: PR gerado automaticamente a partir de um Issue aprovado

Fase 3 — Event-driven e infra
- Objetivo: profissionalizar com RabbitMQ, Redis, Postgres
- Entregáveis:
  - Eventos: issue.received, plan.generated, code.generated, pr.created
  - Workers desacoplados
  - Idempotência e locks via Redis

Fase 4 — Frontend
- Objetivo: dashboard simples com Next.js mostrando issues, status e approvals

Fase 5 — Microsserviços (identity, workflow, gateway)
- Objetivo: transformar componentes em serviços independentes (quando necessário)

Backlog inicial (priorizado)
---------------------------------
1. (Imediato) Criar / atualizar README com instruções de dev local
2. (Imediato) Criar `requirements.txt` e `run-local.sh` para `devflow-orchestrator`
3. (Imediato) Adicionar script de simulação de webhook (curl example)
4. Cobrir com testes unitários: `normalizer`, `stack_detector`, `planning_agent` (mock LLM)
5. Melhorar geração de Markdown (templates) e criar um template de comentário bonito
6. Implementar handling de comando de aprovação (`approve plan`) via webhook
7. Adicionar mocks para `github_commenter` e `llm` em ambiente de dev
8. Preparar demonstração com ngrok + exemplo de Issue

Decisões de nomenclatura e estilo
-----------------------------------
- Pacote principal durante desenvolvimento: `devflow-orchestrator` (contendo `app/` internamente)
- Logger name: `devflow-orchestrator` (consistente em todo o código)
- Funções públicas de workflow: `start_planning_workflow`, `route_workflow`
- Branch naming: `feature/<issue-number>-<short-description>`
- Commit message: `type(scope): short description` (ex.: `feat(orchestrator): add planning workflow`)

Definição de Done (exemplo, por história)
- Código implementado e revisado por PR
- Testes unitários cobrindo o novo comportamento (>= 80% cobertura no módulo alterado)
- Documentação atualizada (README ou docs/)
- Infra/variáveis de ambiente documentadas
- Demonstração end-to-end local verificada

Segurança e credenciais
-------------------------
- Nunca commitar chaves privadas. Usar `.env` e `.env.example` apenas com nomes das variáveis
- Variáveis mínimas esperadas:
  - OPENAI_API_KEY
  - GITHUB_TOKEN
  - DEVFLOW_ENV=development
- Para demos públicas usar mocks e fixtures em vez de chaves reais

CI / QA (recomendado)
-----------------------
- Github Actions pipeline mínima:
  - lint (flake8 / ruff)
  - tests
  - build image (opcional)
- PR template com checklist (tests, docs, run-local)

Como rodar o orquestrador localmente (exemplo)
-----------------------------------------------
1) Criar virtualenv e instalar deps
```sh
python -m venv .venv
. .venv/bin/activate
pip install -r devflow-orchestrator/requirements.txt
```

2) Exportar variáveis mínimas (exemplo)
```sh
export OPENAI_API_KEY=sk_xxx
export GITHUB_TOKEN=ghp_xxx
export PYTHONPATH=$(pwd)/devflow-orchestrator
```

3) Rodar o servidor
```sh
uvicorn app.main:app --reload --port 8000
```

4) Testar webhook com curl
```sh
curl -X POST "http://localhost:8000/webhook/github" \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: issues" \
  -d '{"action":"opened","repository":{"name":"myrepo"},"issue":{"number":1,"title":"Adicionar endpoint X"}}'
```

Critérios de aceitação para a demo da Fase 1
---------------------------------------------
- Receber webhook e retornar 200 OK
- Gerar contexto coerente e logar resultados
- Gerar um plano em JSON/Markdown (mesmo que seja um mock do LLM)
- Postar comentário (ou simular posting) com o markdown gerado
- Registrar no log o status final `planning_completed`

Propostas de tarefas atômicas (próximo sprint de 1-2 semanas)
------------------------------------------------------------
Sprint objetivo: tornar o fluxo local rodável e repetível
Tarefas:
1. Criar `devflow-orchestrator/requirements.txt` e `run-local.sh` (1 dia)
2. Documentar variáveis de ambiente e criar `.env.example` (0.5 dia)
3. Implementar mocks para OpenAI e GitHub (1 dia)
4. Escrever 6 testes unitários básicos (normalizer, stack_detector, planner mocked) (2 dias)
5. Melhorar template de markdown para comentário (0.5 dia)
6. Criar `demo/` com instruções para ngrok e payloads (0.5 dia)

Estimativas: 1–2 semanas de trabalho focado (1 dev full-time)

Governança do repositório e PRs
--------------------------------
- Abrir PRs pequenos, atômicos e com descrição clara do que muda
- Incluir checklist de QA no PR
- Revisão por pelo menos uma pessoa antes de merge

Próximas ações que posso executar agora (me diga qual autorizar)
-----------------------------------------------------------------
1) Gerar `requirements.txt` e `run-local.sh` automaticamente e commitar
2) Adicionar `PROJECT_PLAN.md` (feito) e criar `README.md` inicial
3) Criar mocks para `openai_client` e `github_commenter` em ambiente de dev
4) Implementar testes unitários iniciais e rodá-los

Observação final
------------------
Com o que você já tem é perfeitamente viável concluir a Fase 1 de forma profissional e rápida. Posso começar a aplicar as tarefas atômicas listadas — diga qual você quer que eu execute primeiro e eu procedo com commits atômicos, testes e validações.

