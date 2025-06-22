# 🧠 Calculadora de Prazos Processuais - CPC (Brasil)

Este projeto define um **prompt para agentes de IA** capazes de calcular prazos processuais com base nas regras do **Código de Processo Civil brasileiro (CPC/2015)**, considerando feriados e recesso forense aplicáveis ao **Tribunal de Justiça de São Paulo (TJSP)**.

## 📌 Objetivo

Fornecer a **data final para manifestação ou protocolo processual** com base na data da publicação da intimação e no tipo de ato praticado (contestação, recurso, embargos etc.).

---

## ⚖️ Regras Aplicadas

- **Contagem apenas em dias úteis** (excluem-se sábados, domingos e feriados).
- **Suspensão de prazos entre 20/12 e 20/01**, inclusive.
- **Início da contagem**: primeiro dia útil após a data da publicação.
- **Prazos legais**:
  - Recursos em geral: 15 dias úteis
  - Embargos de declaração: 5 dias úteis
  - Contestação: 15 dias úteis
  - Outros atos sem previsão legal: 5 dias úteis
- Em **decisões de 2ª instância ou tribunais superiores**, considerar apenas os recursos cabíveis.

---

## 🧾 Entrada Esperada

A IA aceita dois formatos de entrada:

### 1. Comando Simples

```text
Tipo: Contestação
Data de publicação: 23/06/2025
```

### 2. Intimação Completa

Trecho transcrito da publicação no Diário da Justiça contendo:
- Número do processo
- Vara ou órgão julgador
- Partes
- Decisão
- Data de disponibilização e publicação

---

## ✅ Saída Esperada

Se possível, a IA deve retornar:
- Data de início do prazo
- Data final para protocolo
- (Se disponível) número do processo, partes, resultado da decisão e recurso cabível

---

## ❌ Falha Controlada

Se não for possível calcular com precisão, a IA **deve retornar "nenhum" ou "nada" como resultado**, **sem fazer suposições** ou inventar prazos.

---

## 📦 Uso Sugerido

Este prompt pode ser utilizado com:
- OpenAI GPT API (ex: `gpt-4`)
- Frameworks como LangChain, LlamaIndex
- Aplicações jurídicas internas com LLMs personalizados

---

## 📁 Arquivo do Prompt

O prompt principal está disponível no arquivo [`main.py`](main.py).

---

# 🤖 Exemplo de execução

## Entrada

Data de Disponibilização: 13/09/2024
Data de Publicação:16/09/2024
Jornal: Diário da Justiça do Estado de SÃO PAULO
Página: 02603
Caderno: CADERNO 4 JUDICIAL 1ª INSTÂNCIA INTERIOR (3)
Local: DJSP - CADERNO 4 JUDICIAL 1ª INSTÂNCIA INTERIOR.  SÃO JOSÉ DO RIO PRETO
Vara: Juizado Especial Cível JUÍZO DE DIREITO DA VARA DO JUIZADO ESPECIAL CÍVEL  

Publicação: EDITAL DE INTIMAÇÃO DE PARTES E ADVOGADOS. RELAÇÃO Nº 0754/2024

Processo XXXXXXX-XX.2023.8.26.0576 - Procedimento do Juizado Especial Civel - Indenizacao por Dano Moral - MARIANA TEODORO VILELA - Picpay Instituicao de Pagamento S/A - "Peticao e documentos juntados pela parte REQUERIDA a fls. 230/231 : ciencia a parte contraria, com 05 (cinco) dias para manifestacao. (Prazo: contam-se apenas os dias uteis, de acordo com o art. 12-A da Lei n. 9.099/95 e a contagem do prazo nos Juizados Especiais Civeis e da data da ciencia do ato respectivo (PUIL nº 28 - Turma de Uniformizacao dos Juizados Especiais) e nao da juntada aos autos do comprovante de intimacao ou citacao, excluindo o dia do comecoe incluindo o dia do vencimento.)" - ADV: FULADO DE TAL (OAB XXXXXX/SP), MARIANA TEODORO VILELA (OAB 485303/SP)

## Saída

Resultado:

- **Processo:** XXXXXXX-XX.2023.8.26.0576
- **Vara:** Juizado Especial Cível — JUÍZO DE DIREITO DA VARA DO JUIZADO ESPECIAL CÍVEL
- **Partes:** Mariana Teodoro Vilela (autora) x Picpay Instituição de Pagamento S/A (ré)
- **Resultado da decisão:** Ciência à parte contrária de petição e documentos juntados; prazo de 5 dias úteis para manifestação
- **Tipo de manifestação:** Manifestação sobre documentos/ciência de petição — **5 dias úteis**

**Cálculo do prazo:**

- **Data de publicação:** 16/09/2024
- **Início do prazo:** 17/09/2024 (primeiro dia útil seguinte à publicação)
- **Contagem:** 5 dias úteis

Verificação de dias úteis a partir de 17/09/2024 (considerando calendário oficial e feriados forenses/regras nacionais; não há recesso ou feriado nacional relevante):

1. 17/09/2024 (terça)
2. 18/09/2024 (quarta)
3. 19/09/2024 (quinta)
4. 20/09/2024 (sexta)
5. 23/09/2024 (segunda)

**Resposta final:**

- **Início:** 17/09/2024
- **Prazo final:** 23/09/2024

Caso precise do detalhamento da contagem dos dias úteis ou atualização por feriados locais (município de São José do Rio Preto), favor informar.

---

## 🧑‍💼 Autor

Prompt desenvolvido por [Mariana Teodoro](https://github.com/marianateodoro97), advogada com interesse em automações jurídicas inteligentes.
