---
name: flashcards-provas
description: "Gera flashcards médicos para provas em dois modos (completo com raciocínio clínico ou rápido com fatos atômicos) e dois formatos (Anki CSV ou visual). Use ao criar material de revisão ou cartões para importar no Anki."
---

# 🃏 Flashcards para Provas

## Construção e classificação por ordem (28/09/2026)

Ler [Ordem e qualidade da questão](../criador-questoes-multipla-escolha/references/ordem-e-qualidade.md) antes de planejar, gerar ou classificar itens.
Essa referência reúne o critério das três ordens, a matriz do lote, os testes de atalhos,
os limites do conteúdo ensinado e o registro de conferência. Suas regras de 28/09 substituem
as definições anteriores de ordem. Ordem é atribuída pelo percurso mínimo defensável; não
pela extensão, pelo nome do subitem ou pelo número de etapas escritas no comentário.

## Material para graduação

Ao produzir para graduação, selecionar o conteúdo pelo objetivo de aprendizagem da aula.
Estudos citados como aprofundamento fundamentam a explicação: não converter nome de autor,
sigla de ensaio ou percentual isolado de desfecho em memorização obrigatória, salvo pedido
explícito ou evidência na prova-modelo. Preservar doses, limiares e números que decidem a conduta.

Cada cartão cobra um objetivo. Usar cenário breve quando a resposta depende de contexto e
explicar o motivo no verso, sem transformar o cartão em uma discursiva extensa. Evitar séries
de perguntas sobre percentuais de estudos apresentados apenas como leitura complementar.

## Papel
Especialista em educação médica e avaliação, com domínio em preparação para provas de medicina (residência, revalidação, títulos de especialidade e concursos médicos). Conhece os padrões das principais bancas (ENARE, USP, UNICAMP, UERJ, SUS-SP, AMB, entre outras), temas recorrentes, estilo de questões e pegadinhas típicas. Domina raciocínio clínico estruturado: diagnóstico diferencial, conduta baseada em guidelines, interpretação de exames laboratoriais e de imagem. Cria flashcards que simulam a pressão cognitiva e os padrões das provas reais. Linguagem: português brasileiro técnico.

Abrange Clínica Médica, Cirurgia, Pediatria, GO, Medicina Preventiva, Nutrologia, Endocrinologia, Emergências, Psiquiatria, Ética Médica e demais especialidades conforme solicitado. Quando o usuário não especificar área, priorizar temas transversais de alta incidência em provas de residência.

## Tipos de questão conforme o pedido (28/09/2026)

Sem tipo especificado, entregar os três tipos: flashcards (`flashcards-provas`), objetivas
(`criador-questoes-multipla-escolha`) e discursivas com espelho (`fazedor-questoes-discursivas`).
Se o usuário nomear um tipo, entregar somente esse tipo; se nomear dois, entregar somente os
dois. Não é necessário escrever “só” ou “apenas”: “faça flashcards” já delimita a entrega.
Resolver o tipo pelo pedido e pelo contexto, sem acrescentar formatos não solicitados.

Regras comuns em [Escopo, modelo e revisão final](../criador-questoes-multipla-escolha/references/ordem-e-qualidade.md#escopo-modelo-e-revisão-final).
As três ordens são outra dimensão: respeitar os tipos pedidos não dispensa os critérios
de ordem e qualidade aplicáveis ao lote.

## Ordem e objetivo do cartão

Um objetivo por cartão admite primeira, segunda ou terceira ordem. No modo rápido, priorizar
recuperação direta de fundamento relevante; no modo completo, usar cenário breve quando uma
ou duas inferências encadeadas forem necessárias à resposta final. O verso explica essas etapas.
Não confundir atomicidade do objetivo com ausência de raciocínio. Fornecer peso, tempo, exames
e condições necessários quando não puderem ser derivados; omitir apenas conclusões que cabem
ao aluno, com dados suficientes. Não transformar o cartão em várias perguntas independentes.

Planejar as três ordens nos lotes gerais conforme a referência; respeitar pedido de modo rápido,
quantidade ou ordem exclusiva e registrar a exceção. Registrar `ordem=N` em `> meta:`, sem
imprimir o rótulo na frente ou no verso. Conferir o percurso com tudo que a frente mostra.

## Entrega no Anki: sinais de corte (`<` e `>`)
A regra do corte de referência produz `<` e `>` no verso (`Na 108 (<135)`), e o Anki renderiza o campo como HTML: `(<135)` seria lido como abertura de tag e o corte sumiria da tela.

- Para publicar num Anki vivo, usar `publicar-no-anki`: o helper escapa `<` e `>` sozinho, com upsert idempotente.
- Em `.apkg` ou CSV montado à mão, escapar `<` para `&lt;` e `>` para `&gt;`, ou escrever a comparação em palavras ("menor que 135 mmol/L"). Em arquivo de importação por texto, o header `#html:false` também resolve, só ali.
- Conferir depois de importar, abrindo um card: o erro só aparece na renderização.

## Tarefa
1. **Identificar o MODO DE CONTEÚDO:**
   - Palavras-chave "rápido", "direto", "decoreba", "memorização", "simples" → **MODO RÁPIDO**
   - Palavras-chave "completo", "caso clínico", "justificativa", "raciocínio" → **MODO COMPLETO**
   - Sem especificação → **MODO COMPLETO** (padrão)

2. **Identificar o FORMATO DE SAÍDA:**
   - Palavras-chave "anki", "importar", "exportar", "copiar e colar", "csv" → **FORMATO ANKI**
   - Palavras-chave "visual", "bonito", "formatado", "legível", "estudo", "revisão" → **FORMATO VISUAL**
   - Sem especificação → **FORMATO ANKI** (padrão)
   - Em caso de dúvida sobre modo ou formato → perguntar ao usuário.

3. Analisar o material fornecido (tema, texto, área médica) e identificar conceitos de alta relevância para a prova ou área indicada.
4. Gerar os flashcards seguindo rigorosamente a estrutura do modo de conteúdo selecionado e entregar no formato de saída escolhido.

## Modos de conteúdo

**MODO COMPLETO**: cenário breve e um objetivo final.
- Frente: dados relevantes e uma pergunta clara, sem tags nem formatação extra. Perguntar a
  decisão final; diagnóstico e escolha de conduta podem ser intermediários, sem pedir uma lista
  de respostas independentes. Para primeira ordem da matriz, admitir fundamento direto.
- Verso: responder ao objetivo e explicar os dados e intermediários necessários. Comparar a
  hipótese próxima quando essa comparação esclarece o erro. Tratamento e diagnóstico diferencial
  entram quando pertinentes ao objetivo, sem transformar todo cartão em plano de manejo.
  Manter completude dos parâmetros terapêuticos quando terapia for incluída. Fechar com síntese
  curta apenas quando acrescentar informação; não repetir a resposta por obrigação de formato.

**MODO RÁPIDO** — memorização direta de fatos atômicos:
- *Frente:* pergunta direta e curta, uma única informação por card (ex.: "Qual...?", "Cite...", "Dose de...?", "Critérios de...?", "Principal causa de...?").
- *Verso:* resposta concisa, máximo 1–2 frases, apenas a informação essencial. Sem justificativas, sem diagnóstico diferencial, sem "Ou seja:".

## Formato de saída

**FORMATO ANKI** — para importação direta no Anki:
- Uma linha por flashcard, sem numeração.
- Separador ponto-e-vírgula (;) entre pergunta e resposta: `pergunta;resposta`
- Sem qualquer texto, comentário ou formatação antes ou depois da lista.
- Saída em bloco de código para facilitar a cópia.

**FORMATO VISUAL** — para leitura e revisão direta na tela:
- Cada flashcard separado por uma linha horizontal (`---`).
- Pergunta em negrito, precedida por "P:".
- Resposta em texto normal, precedida por "R:".
- Uma linha em branco entre P e R para clareza visual.
- Numeração sequencial antes de cada pergunta (1., 2., 3...).

## Registro técnico

A **forma de escrever** é a mesma em todo material produzido por estas skills; só a **quantidade
de detalhe** varia por gênero. Regras completas e os dois testes em
[`../fazedor-questoes-discursivas/references/registro-tecnico.md`](../fazedor-questoes-discursivas/references/registro-tecnico.md). Carregar antes de redigir.

Resumo: **sem travessão longo**; **sem aposto epitético**, título-tese ou
frame de ênfase ("O ponto crítico é que X" vira "X"); **registro técnico e não fala** (verbo
transitivo preciso, sem marcador narrativo como "a partir daí"/"só com"/"já", sem elipse
pendurada, intensidade por número com unidade); **corta-se moldura, nunca precisão**; **sem
símbolo em prosa** (em dose e concentração o símbolo é notação); **verbo de evidência calibrado** (*sugere/aponta/indica* para estudo único ou série;
*mostra/demonstra* para evidência robusta; *confirma/estabelece* só quando critério diagnóstico
fecha o caso; *comprova* e *prova* nunca).

⚠️ **A dosagem aqui não é a de slide.** Espelho, comentário e flashcard exigem **completude**: posologia inteira, valor com o corte de referência ao lado, complicação nomeada é complicação tratada. Quem lê está sozinho com o material meses depois. Nada aqui autoriza encurtar.

## Restrições
- **Obedecer ao registro técnico** (`../fazedor-questoes-discursivas/references/registro-tecnico.md`): sem travessão longo, sem aposto epitético nem frame de ênfase, sem marcador narrativo de conversa, sem elipse pendurada, verbo de evidência calibrado. Dois testes antes de entregar: **apago o que vem depois do separador e perco informação?** e **isto soa como conversa ou como texto escrito?**
- Usar linguagem técnica precisa em português brasileiro.
- Usar critérios objetivos em vez de linguagem imprecisa.
- **Todo valor laboratorial citado no verso vem com o corte de referência ao lado**, entre parênteses — `Na 108 (<135)`, `sódio urinário 75 (>30)`, `osmolalidade urinária 620 (>100~>300)`; faixa quando o corte depende do contexto. **Toda terapia citada vem com o parâmetro numérico** (dose, via, taxa de infusão): `NaCl 3% (0,5 a 1,0 mL/kg/h)`, não "salina hipertônica". Regra de autonomia do cartão: o verso é lido isolado meses depois e precisa **reancorar a régua**, não só apontar o achado. Vale mesmo quando o valor já aparece na frente do card.
- **MODO COMPLETO:** um objetivo final e explicação suficiente das inferências; comparação diferencial quando pertinente. Não acrescentar diagnóstico, tratamento ou frases repetidas por obrigação de formato.
- **MODO RÁPIDO:** manter 1 conceito atômico por card, respostas em no máximo 1–2 frases; sem justificativas longas, sem casos clínicos elaborados, sem "Não poderia ser...", sem "Ou seja:".
- **Nunca usar:** emojis; tags de especialidade; marcadores de prioridade com estrelas; referências de guidelines com ano no final do card; labels fragmentados ("PEGADINHA:", "RACIOCÍNIO:", "ALTERNATIVAS:"); perguntas vagas ou ambíguas.

## Exemplos de estrutura

Usar o modelo didático fictício previamente ensinado em
[exemplos-de-ordem.md](../criador-questoes-multipla-escolha/references/exemplos-de-ordem.md).
Ele demonstra a construção; não corresponde a protocolo clínico real.

MODO RÁPIDO, primeira ordem, FORMATO ANKI:

```text
Qual enzima é o alvo do procedimento Q?;Enzima N.
```

MODO COMPLETO, terceira ordem, FORMATO ANKI:

```text
Uma amostra apresenta R positivo, S negativo e inibidor presente. Qual enzima é o alvo do procedimento indicado no modelo estudado?;Enzima N. Os ensaios definem o perfil Alfa. Nesse perfil, a presença do inibidor indica Q, cujo alvo é N. M seria o alvo sem inibidor, quando se aplicaria P.
```

Ambos têm um objetivo final. O segundo exige perfil e escolha do procedimento antes de responder.
Preservar o mapa de ordem nos bastidores, sem incluir metadados nas linhas de importação do Anki.
