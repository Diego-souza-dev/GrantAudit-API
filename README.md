# GrantAudit API 📊🤖

**Link da API em Produção:** [[https://SEU-LINK-AQUI.onrender.com/docs]](https://grantaudit-api.onrender.com/docs)

Uma API REST desenvolvida em Python e FastAPI focada na automação de pré-auditoria financeira e análise de risco corporativo, integrada à Inteligência Artificial Generativa (Google Gemini).

Este projeto foi desenvolvido como um *business case* prático demonstrando como a engenharia de software e as ferramentas modernas de IA podem ser aplicadas para otimizar fluxos de consultoria de negócios e auditoria, reduzindo o tempo de análise documental e padronizando a identificação de *red flags* contábeis.

## 💼 Valor de Negócio
Na rotina de auditoria financeira, equipes dedicam extensas horas na triagem de balanços para identificar inconsistências básicas. O **GrantAudit API** atua como uma camada automatizada que:
1. Recebe parâmetros de demonstrações financeiras (DRE/Balanço).
2. Calcula automaticamente indicadores matemáticos de liquidez e margem de lucro.
3. Classifica o risco de conformidade (BAIXO, MÉDIO, ALTO).
4. Utiliza um LLM (Gemini 2.5 Flash) estruturado com um *prompt* especialista para emitir um parecer executivo preliminar para a equipe de campo.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Framework Web:** FastAPI
* **Validação de Dados:** Pydantic
* **Integração de IA:** Google Generative AI SDK (Gemini)
* **Servidor:** Uvicorn
* **Deploy:** Render

## 🚀 Como Executar Localmente

### 1. Clone o repositório
```bash
git clone [https://github.com/Diego-souza-dev/GrantAudit-API.git](https://github.com/Diego-souza-dev/GrantAudit-API.git)
cd GrantAudit-API
