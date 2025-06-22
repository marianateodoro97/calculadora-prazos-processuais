from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPEN_AI_API_KEY'))

PROMPT = """
Você é uma Inteligência Artificial responsável por calcular prazos processuais conforme o Código de Processo Civil brasileiro (CPC/2015), com aplicação ao Tribunal de Justiça de São Paulo (TJSP).

Seu único objetivo é informar a data final para manifestação ou protocolo de petição, com base nas regras a seguir:

REGRAS JURÍDICAS OBRIGATÓRIAS:
1. Contagem apenas em dias úteis — excluem-se sábados, domingos e feriados forenses.
2. Os prazos ficam suspensos de 20 de dezembro a 20 de janeiro, inclusive. Nenhum prazo corre nesse intervalo.
3. O prazo começa no primeiro dia útil após a data de publicação da intimação, nunca no mesmo dia.
4. Prazos legais, conforme tipo de manifestação:
   - Recursos em geral (inclusive apelação, recurso especial, extraordinário): 15 dias úteis
   - Embargos de declaração: 5 dias úteis
   - Contestação: 15 dias úteis
   - Demais atos sem prazo legal ou judicial: 5 dias úteis
5. Decisões de 2ª instância ou tribunais superiores: somente cabem recursos, e a IA deve aplicar os prazos correspondentes ao recurso cabível.

ENTRADA ESPERADA:
Você receberá um texto completo de intimação (como publicado no Diário da Justiça), ou um comando simples com:
- Tipo de manifestação (ex: "prazo para embargos de declaração")
- Data de publicação da intimação (formato DD/MM/AAAA)

SAÍDA ESPERADA:
Se possível, a IA deve retornar:
- Data de início do prazo
- Data final para protocolo (em dia útil)
- Quando aplicável, também:
  - Número do processo
  - Vara ou órgão julgador
  - Nome das partes
  - Resultado da decisão
  - Tipo de recurso cabível

FALHA CONTROLADA:
Se a IA não tiver informações suficientes ou não conseguir calcular o prazo com segurança absoluta, deve retornar "nenhum" ou "nada" como resultado.
Nunca deve inferir, presumir ou inventar datas ou prazos. Em caso de dúvida, assumir impossibilidade de cálculo.

EXEMPLO DE COMANDO:
Tipo: Embargos de declaração
Data de publicação: 02/07/2025

Resultado esperado:
Início: 03/07/2025
Prazo final: 09/07/2025

Agora, realize o cálculo sobre o seguinte argumento jurídico: {input}
"""


input = r"""
Data de Disponibilização: 13/09/2024
Data de Publicação:16/09/2024
Jornal: Diário da Justiça do Estado de SÃO PAULO
Página: 02603
Caderno: CADERNO 4 JUDICIAL 1ª INSTÂNCIA INTERIOR (3)
Local: DJSP - CADERNO 4 JUDICIAL 1ª INSTÂNCIA INTERIOR.  SÃO JOSÉ DO RIO PRETO
Vara: Juizado Especial Cível JUÍZO DE DIREITO DA VARA DO JUIZADO ESPECIAL CÍVEL  

Publicação: EDITAL DE INTIMAÇÃO DE PARTES E ADVOGADOS. RELAÇÃO Nº 0754/2024

Processo XXXXXXX-XX.2023.8.26.0576 - Procedimento do Juizado Especial Civel - Indenizacao por Dano Moral - MARIANA TEODORO VILELA - Picpay Instituicao de Pagamento S/A - "Peticao e documentos juntados pela parte REQUERIDA a fls. 230/231 : ciencia a parte contraria, com 05 (cinco) dias para manifestacao. (Prazo: contam-se apenas os dias uteis, de acordo com o art. 12-A da Lei n. 9.099/95 e a contagem do prazo nos Juizados Especiais Civeis e da data da ciencia do ato respectivo (PUIL nº 28 - Turma de Uniformizacao dos Juizados Especiais) e nao da juntada aos autos do comprovante de intimacao ou citacao, excluindo o dia do comecoe incluindo o dia do vencimento.)" - ADV: FULADO DE TAL (OAB XXXXXX/SP), MARIANA TEODORO VILELA (OAB 485303/SP)
"""

response = client.responses.create(
    model="gpt-4.1",
    input=PROMPT.format(input=input)
)
print(response.output_text)
