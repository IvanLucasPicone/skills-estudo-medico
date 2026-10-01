# Exemplos e contraprovas de classificação

Ler com [ordem-e-qualidade.md](ordem-e-qualidade.md). Os exemplos abaixo são autorais, para testar
a estrutura. O modelo fictício evita converter um exemplo editorial em recomendação clínica.
Em produção médica, substituir o modelo por conteúdo ensinado e clinicamente conferido.

## Modelo didático de laboratório

Conhecimento fornecido ao elaborador e previamente ensinado ao aluno; não repetir a tabela no
enunciado de cada item. Não corresponde a doença ou protocolo real.

| Achado da amostra | Perfil inferido | Condição adicional | Procedimento indicado | Alvo do procedimento |
|---|---|---|---|---|
| Ensaio R positivo, ensaio S negativo | Alfa | Inibidor ausente | P | Enzima M |
| Ensaio R positivo, ensaio S negativo | Alfa | Inibidor presente | Q | Enzima N |
| Ensaio R negativo, ensaio S positivo | Beta | Inibidor ausente | T | Enzima O |
| Ensaio R negativo, ensaio S positivo | Beta | Inibidor presente | U | Enzima V |

Outras combinações de ensaio não têm regra neste modelo e não podem ser usadas sem informação
adicional. A escolha entre P, Q, T e U e seus alvos foi ensinada, sem associações mnemônicas
adicionais entre nomes dos ensaios e enzimas.

## Três itens sobre o mesmo conteúdo

**Primeira ordem.** Qual enzima é o alvo do procedimento Q?

A) Enzima M. B) Enzima N. C) Enzima O. D) Enzima V.

Resposta: B. Recupera diretamente a relação entre Q e N. Não acrescentar uma história de
coleta da amostra para aparentar aplicação. Fundamento legítimo para fixação.

**Segunda ordem.** Uma amostra apresenta ensaio R positivo, ensaio S negativo e inibidor presente.
Qual procedimento deve ser aplicado segundo o modelo estudado?

A) Procedimento P. B) Procedimento T. C) Procedimento U. D) Procedimento Q.

Resposta: D. Deriva perfil Alfa dos ensaios e usa o inibidor para selecionar Q. Intermediário
indispensável: perfil. A condição do inibidor já é fornecida; não contá-la como outra conclusão.

**Terceira ordem.** Uma amostra apresenta ensaio R positivo, ensaio S negativo e inibidor presente.
Qual enzima é alvo do procedimento indicado para processá-la segundo o modelo estudado?

A) Enzima N. B) Enzima O. C) Enzima V. D) Enzima M.

Resposta: A. Deriva Alfa, seleciona Q e recupera seu alvo N. Intermediários: perfil e procedimento.
Os distratores correspondem a escolher procedimento para outro perfil ou desconsiderar o inibidor.
Todos têm mesma extensão, categoria e especificidade. Essa classificação vale para o conhecimento
estipulado; se a aula ensinou diretamente a associação dessa combinação de ensaios ao alvo N,
reavaliar o percurso mínimo. Não se presume dificuldade empírica pela etiqueta.

**Teste de dependência do terceiro item.** Mantendo Alfa e retirando o inibidor, o alvo passa a M;
mantendo o inibidor e trocando os ensaios para Beta, passa a V. Reconhecer apenas Alfa não basta,
porque há dois procedimentos possíveis. Reconhecer apenas presença de inibidor também não basta.
O registro explica por que as etapas importam, em vez de apenas declarar `ordem=3`.

## Terceira ordem aparente: defeitos e correções

| Versão defeituosa | Achado | Correção e classificação |
|---|---|---|
| A vinheta termina com “será aplicado Q” e pergunta seu alvo. | O procedimento já foi dado; ensaios e perfil não são necessários. | Retirar a conclusão Q, preservando ensaios e inibidor, como no terceiro item; ou assumir objetivo de primeira ordem. |
| A terceira questão oferece “Enzima N”, “Cor da bancada”, “Nome do coletor”, “Horário de abertura”. | Três distratores não respondem ao comando; pista de categoria. | Usar quatro alvos concorrentes da tabela. Reprovar a versão original, sem validá-la como primeira ordem. |
| A correta diz “aplicar Q e controlar interferência”; as demais só dizem “P”, “T” e “U”. | A correta tem extensão e abrangência exclusivas. | Delimitar o comando e oferecer quatro procedimentos no mesmo formato; se o plano completo é o objetivo, construir quatro planos comparáveis. |
| A terceira questão omite o resultado do inibidor. | Alfa permite P ou Q, com alvos distintos. | Informar o inibidor. O dado necessário não pode ser omitido para fabricar uma etapa. |
| O comando pede procedimento e alvo; a chave oferece apenas Q, e o comentário acrescenta N. | Alternativa incompleta para a tarefa solicitada. | Incluir procedimento e alvo em todas as opções, ou reduzir explicitamente o comando a procedimento. Reavaliar a ordem após mudar as opções. |
| O comentário enumera coleta, leitura de R, leitura de S, diagnóstico, escolha e alvo. | Contagem inflada por operações de leitura e detalhes narrativos. | Contar somente os intermediários de conhecimento indispensáveis. |

## Discursiva e vazamento entre subitens

Versão defeituosa: A) “Qual o perfil da amostra?”; B) “Considerando que o perfil é Alfa e o
procedimento indicado é Q, qual seu alvo?”. B entrega A e torna sua própria resposta recuperação
direta. Não classificar o conjunto como terceira ordem pela extensão do espelho.

Versão coerente: A) “Identifique o perfil e justifique pelos ensaios”; B) “Indique o procedimento
e justifique pela condição adicional”; C) “Identifique o alvo do procedimento indicado”. Com
todos os comandos visíveis, nenhum fornece as respostas dos outros. O aluno pode reutilizar as
próprias conclusões, o que constitui apoio da sequência, registrado no mapa de subitens. Não
tratar essa sequência como três medidas independentes nem usar a ordem predominante para ocultar
diferenças entre A, B e C. No espelho, aceitar raciocínio justificável e delimitar pontuação por
demanda quando o modo usar pontos; não penalizar o mesmo erro em cascata sem critério declarado.

## Flashcard e objetivo único

Frente: resultados R positivo, S negativo e inibidor presente; perguntar o alvo do procedimento
indicado. Verso: Alfa pelos ensaios; Q pela presença de inibidor; alvo N. Um objetivo final com
dois intermediários. Não transformar a frente numa bateria que exige também coleta, classificação,
justificativa completa, acompanhamento e efeitos adversos. Não ocultar o resultado do inibidor.

## Casos de regressão para futuras revisões

Verificar com as regras acima: fato direto aceito; caminho encadeado sustentado; conclusão
entregue reclassificada; distrator absurdo reprovado; opções de tamanho igual mas conteúdo
implausível reprovadas; dado indispensável ausente reprovado; resposta completada só no comentário
reprovada; subitem que revela outro identificado; interpretação por conhecimento preservada;
fonte curta sem conteúdo para terceira ordem não ampliada artificialmente. Em lote misto de seis
itens, planejar as três ordens; em pedido de duas questões, respeitar o total; em pedido exclusivo
de terceira ordem, conferir todas nessa ordem. Relatar os resultados como revisão de construção,
sem alegar desempenho de alunos ou validação psicométrica.
