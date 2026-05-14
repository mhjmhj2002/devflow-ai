# 🤖 Guia de Modelos AI + Aider (Setup Dev / Produção)

Este documento serve como referência rápida para escolher modelos e usar o Aider no dia a dia.

---

# 🚀 COMO INICIAR O AIDER

## Uso básico
```bash
aider --model gpt-5-mini
````

## Com modelos específicos

```bash
aider --model gpt-5
aider --model gpt-5-mini
aider --model gpt-5-nano
aider --model gpt-4o
```

## Rodar dentro de um repo git

```bash
cd seu-projeto
aider --model gpt-5-mini
```

## Ajuda rápida

```bash
aider --help
```

## Ver modelos disponíveis

Dentro do aider:

```
/models
```

---

# 🧠 MODELOS RECOMENDADOS (POR USO)

## 🥇 TOP DEV (equivalente ao Claude Sonnet nível forte)

Use para arquitetura, refactor, sistemas grandes, decisões críticas:

```bash
gpt-5.1-chat
gpt-5.2-chat
gpt-5.3-chat-latest
```

👉 Melhor equilíbrio entre:

* raciocínio
* código correto
* consistência em projetos grandes

---

## ⚡ CODING MODELS (tipo “Codex moderno”)

Use para:

* CRUDs
* APIs
* controllers
* features completas
* implementação rápida

```bash
gpt-5.2-codex
openrouter/openai/gpt-5-codex
openrouter/openai/gpt-5.1-codex-max
```

👉 Melhor custo/benefício pra “fazer produto”

---

## 🧪 MODELO RÁPIDO (protótipo / sprint)

Use para:

* testar ideias
* gerar boilerplate
* scripts simples
* debugging leve

```bash
gpt-5-mini
gpt-4o-mini
gpt-5-nano
```

---

## 🧠 MODELO ULTRA (máxima qualidade)

Use para:

* decisões críticas de arquitetura
* debugging difícil
* sistemas distribuídos
* performance / concorrência

```bash
gpt-5
gpt-5.4
gpt-5.5
```

---

## 🧾 MODELO LEGADO / COMPATIBILIDADE

```bash
gpt-4o
gpt-4.1
gpt-4-turbo
```

---

# 🧑‍💻 CONFIGURAÇÃO IDEAL (STARTUP / PRODUTO)

## Setup recomendado real (stack prática):

### 🔥 Main model (padrão)

```bash
gpt-5.2-chat
```

### ⚡ Fast model (tarefas rápidas)

```bash
gpt-5-mini
```

### 🧠 Code specialist (CRUD / features)

```bash
gpt-5.2-codex
```

---

# 🧰 COMANDOS ÚTEIS DENTRO DO AIDER

## Ver modelos

```
/models
```

## Trocar modelo principal

```
/model gpt-5.2-chat
```

## Trocar modelo fraco (fallback)

```
/weak-model gpt-5-mini
```

## Ver contexto do repo

```
/map
```

## Rodar comandos shell

```
/run ls -la
```

## Ver diff

```
/diff
```

## Commit automático

```
/commit
```

---

# ⚠️ BOAS PRÁTICAS

* Use **mini/nano para iterar rápido**
* Use **chat/codex para construir features**
* Use **gpt-5.x full para decisões críticas**
* Nunca misturar tudo no mesmo modo sem necessidade

---

# 🧠 RESUMO SIMPLES

* 🧱 Construção séria: `gpt-5.2-chat`
* ⚡ Velocidade: `gpt-5-mini`
* 💻 Código (CRUD/produto): `gpt-5.2-codex`
* 🧠 Deep thinking: `gpt-5.4 / gpt-5.5`