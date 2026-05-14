++ README - DevFlow Orchestrator

Resumo
-------
O `devflow-orchestrator` é o núcleo do projeto DevFlow AI: um orquestrador Python/FastAPI responsável por receber webhooks do GitHub, analisar o contexto de repositórios, gerar planos técnicos via LLM e comentar issues com o resultado. Este README descreve como executar o serviço localmente para desenvolvimento e demonstração.

Principais responsabilidades
- Receber webhooks GitHub (/webhook/github)
- Normalizar eventos do GitHub
- Construir contexto do repositório (detecção de linguagem/stack)
- Gerar plano técnico via agente de planejamento (OpenAI)
- Postar comentário na issue com o plano
- Endpoints auxiliares: /health e documentação OpenAPI (/docs)

Estrutura relevante (dentro de `devflow-orchestrator`)
- `app/main.py` — entrypoint FastAPI
- `app/api/webhook.py` — endpoint do webhook
- `app/workflows/workflow_router.py` — roteador de workflows
- `app/workflows/planning_workflow.py` — workflow de planejamento (start_planning_workflow)
- `app/github/normalizer.py` — normalizador de eventos GitHub
- `app/project_context/*` — scanner, detector de stack, context builder
- `app/agents/planning_agent.py` — integração com LLM
- `app/llm/openai_client.py` — cliente OpenAI (geração de texto)
- `app/github/github_commenter.py` — postagem de comentários no GitHub
- `app/core/logger.py` — logger central (`devflow-orchestrator`)

Dependências (sugestão)
------------------------
Prováveis dependências necessárias (adicione em `requirements.txt` no futuro):
- fastapi
- uvicorn
- pydantic
- requests
- openai

Configuração de ambiente
-------------------------
Crie um arquivo `.env` ou exporte as variáveis abaixo no seu ambiente de desenvolvimento.

- `OPENAI_API_KEY` — chave da OpenAI (pode ser mockada para desenvolvimento)
- `GITHUB_TOKEN` — token com permissões para postar comentários (usar mock em demos)
- `DEVFLOW_ENV` — (opcional) `development` / `production`

IMPORTANTE: nunca commit suas chaves. Use `.env` e `.env.example` com placeholders.


Executando localmente
----------------------
Passo a passo mínimo para rodar o serviço localmente (Linux/macOS):

1) Crie e ative um virtualenv

```sh
python3 -m venv .venv
source .venv/bin/activate
```

2) Instale dependências (recomendado: usar o minimal)

ATENÇÃO: o arquivo `requirements.txt` deste repositório foi gerado a partir de um ambiente de desenvolvimento e contém muitos pacotes do sistema (pacotes Ubuntu/Debian ou dependências de desktop). Executar `pip install -r requirements.txt` em um virtualenv limpo muitas vezes falha com erros do tipo "No matching distribution found" (ex.: `apt-clone`, `python-apt`, `systemd-python`) porque esses pacotes não estão disponíveis no PyPI ou exigem dependências nativas.

Por isso, para rodar o orquestrador localmente recomendamos usar o arquivo reduzido `requirements-minimal.txt` incluído aqui. Ele contém apenas as dependências necessárias para desenvolvimento e testes rápidos.

Opção recomendada — instalar o conjunto mínimo (rápido):

```sh
# a partir da pasta devflow-orchestrator
pip install -r requirements-minimal.txt
```

Se preferir instalar pacotes individualmente:

```sh
pip install fastapi uvicorn pydantic pydantic-settings requests openai python-dotenv
```

Se você realmente precisa reproduzir o ambiente completo e quer tentar `requirements.txt`, esteja preparado para instalar dependências de sistema (packages APT) e bibliotecas de desenvolvimento, por exemplo `build-essential`, `libssl-dev`, `python3-dev`, etc. Mesmo assim alguns pacotes como `apt-clone` ou `python-apt` só fazem sentido em ambientes Ubuntu e podem não ser instaláveis via pip.

Exemplo do erro que você pode encontrar ao usar o `requirements.txt`:

```
ERROR: Could not find a version that satisfies the requirement apt-clone==0.2.1
ERROR: No matching distribution found for apt-clone==0.2.1
```

Se isso ocorrer, pare a instalação e use `requirements-minimal.txt`.

Fluxo sugerido para desenvolvimento local

```sh
# 1. ativar .venv
source .venv/bin/activate

# 2. instalar dependências mínimas
pip install -r requirements-minimal.txt

# 3. rodar servidor
uvicorn app.main:app --reload --port 8000
```

Se quiser gerar um `requirements.txt` limpo do seu ambiente depois de instalar apenas o que precisa e confirmar que tudo funciona, rode:

```sh
pip freeze > requirements-clean.txt
```
e use `requirements-clean.txt` em vez do `requirements.txt` original para futuros repositórios ou deploys.

3) Exporte variáveis de ambiente (exemplo usando mocks)

```sh
export OPENAI_API_KEY="sk_test_xxx"
export GITHUB_TOKEN="ghp_test_xxx"
export PYTHONPATH=$(pwd)
```

4) Rode o servidor

```sh
uvicorn app.main:app --reload --port 8000
```

Endpoints úteis
----------------
- Healthcheck: GET http://localhost:8000/health
- Webhook: POST http://localhost:8000/webhook/github
- Swagger UI: http://localhost:8000/docs

Testando o webhook localmente
------------------------------
Exemplo de payload (Issues opened). Use `curl` ou ngrok para integrar com um repositório real.

```sh
curl -X POST "http://localhost:8000/webhook/github" \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: issues" \
  -d '{"action":"opened","repository":{"name":"meu-repo"},"issue":{"number":1,"title":"Adicionar endpoint X","labels":[{"name":"service:identity"}]}}'
```

O fluxo esperado
------------------
1. `webhook/github` recebe o payload
2. `normalizer.normalize_github_event` normaliza o evento
3. `workflow_router.route_workflow` roteia para `start_planning_workflow`
4. `context_builder.build_project_context` analisa o repositório registrado
5. `planning_agent.generate_plan` constrói prompt e chama `llm.openai_client.generate_text`
6. Plano é transformado em Markdown por `skills.plan_markdown_generator` e salvo por `skills.plan_file_writer`
7. `github.github_commenter.post_github_comment` publica o comentário na issue (ou é mockado em dev)

Dicas para desenvolvimento e debugging
-------------------------------------
- Logs: o logger usa a identificação `devflow-orchestrator`; verifique saídas no terminal
- Mocks: se não quiser usar chaves reais, crie funções dummy para `generate_text` e `post_github_comment`
- Projeto modular: você pode rodar partes isoladas em REPL para testar `stack_detector` ou `normalizer`

Como evoluir para demonstração pública (ngrok + GitHub)
--------------------------------------
Para receber webhooks GitHub em um ambiente de desenvolvimento local e demonstrar o fluxo em público, siga estes passos.

1) Instalar e autenticar o ngrok

```sh
# Instalar (exemplo Linux com snap)
sudo snap install ngrok

# Autenticar com seu token (obtenha em https://dashboard.ngrok.com/get-started/your-authtoken)
ngrok config add-authtoken YOUR_NGROK_AUTHTOKEN
```

2) Expor a porta do orquestrador

```sh
# Rode ngrok apontando para a porta onde uvicorn está escutando (por padrão 8000)
ngrok http 8000
```

Anote a URL pública retornada pelo ngrok (ex.: `https://abc123.ngrok-free.app`).

3) Configurar o Webhook no GitHub

- Vá ao repositório no GitHub → Settings → Webhooks → Add webhook
- Payload URL: `https://<YOUR_NGROK_HOST>/webhook/github` (ex.: `https://abc123.ngrok-free.app/webhook/github`)
- Content type: `application/json`
- Which events would you like to trigger this webhook? → `Let me select individual events.` → marque `Issues`
- Active: ✅

4) Testar com um Issue real ou com curl apontando para a URL do ngrok

```sh
curl -X POST "https://abc123.ngrok-free.app/webhook/github" \
  -H "Content-Type: application/json" \
  -H "X-GitHub-Event: issues" \
  -d '{"action":"opened","repository":{"name":"meu-repo"},"issue":{"number":1,"title":"Adicionar endpoint X"}}'
```

Observações de segurança para demos públicas

- Use tokens de teste/contas secundárias quando expor serviços publicamente.
- Para evitar efeitos colaterais (ex.: criar comentários reais), rode em modo `development` e utilize mocks para `github_commenter` ou desative a escrita durante a demo.
- Sempre revogue tokens temporários após a demonstração.

Próximos passos recomendados (rápido)
------------------------------------
1. Criar `requirements.txt` e um `run-local.sh` com os comandos acima
2. Adicionar `.env.example` com variáveis necessárias
3. Implementar mocks para OpenAI e GitHub em modo `development`
4. Escrever 6-8 testes unitários cobrindo `normalizer`, `stack_detector` e `planning_agent` (mock LLM)
5. Melhorar template de Markdown para comentários (visual)

Se preferir, eu posso gerar automaticamente o `requirements.txt` e um `run-local.sh` e adicionar mocks para dev — diga qual ação quer que eu execute em seguida.

Service-aware issues (monorepo support)
--------------------------------------
Em um monorepo é importante que a issue identifique o serviço alvo. O `devflow-orchestrator` suporta duas abordagens para isso:

- Labels: use labels do tipo `service:<name>` (ex.: `service:identity`). O normalizador extrai esse label e o workflow irá analisar apenas o serviço alvo.
- Issue template com campo `Target Service`: preencha o nome do serviço no corpo da issue. Esta implementação inicial prioriza labels.

Exemplo de uso com labels

1. Crie um label no GitHub chamado `service:identity` (ou `service:workflow`, etc.)
2. Ao abrir a issue, aplique o label `service:identity`
3. O orchestrator receberá o webhook, o normalizador extrairá `service = "identity"` e o context builder tentará resolver o caminho do serviço em `../services/identity` ou `../services/identity-service`.

Se preferir que eu implemente suporte adicional para extrair o `Target Service` do corpo da issue (template parsing), posso adicionar essa função também.

