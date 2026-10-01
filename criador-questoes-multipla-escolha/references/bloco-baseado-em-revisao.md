# Bloco de questões baseado em revisão

Usar para converter aula, revisão, transcrição, resumo ou roteiro em questões.
Ler também [ordem-e-qualidade.md](ordem-e-qualidade.md).

Aplicar A–D e dois cadernos como padrão, respeitando alterações do pedido ou modelo.
A quantidade vem do pedido e contexto; 40 itens não são uma cota universal. Selecionar
objetivos sustentados pela fonte e gerar ambos os cadernos da mesma base estruturada.

## Da revisão ao lote

1. **Delimitar a fonte.** Registrar disciplina, público, objetivo, quantidade, formato e limites
   da avaliação. Ler integralmente a unidade solicitada, incluindo perguntas e correções
   acadêmicas. Em transcrição, separar quem pergunta de quem responde. Se só houver resumo
   automático, áudio parcial ou trecho, declarar a extensão acessível; não chamar de integral.
   Informações pessoais e casos identificáveis não entram no material.
2. **Mapear objetivos antes de escrever.** Para cada assunto, anotar a distinção, decisão ou
   fundamento cobrável e o localizador que o sustenta. Reunir trechos distantes do mesmo tema
   e identificar contradições ou correções posteriores. Prioridade decorre da finalidade e
   da ênfase verificável, não apenas dos minutos falados ou de contar repetições. Não prometer
   cobertura de toda a prova por ter coberto a revisão.
3. **Conferir o conteúdo.** Consultar slides/aulas originais para esclarecer omissões e fontes
   primárias atuais para precisão clínica. Não transferir automaticamente erro de transcrição
   ou lapso oral ao gabarito. Registrar correção e sua fonte nos bastidores. Divergência de aula
   e orientação clínica segue a regra canônica de referencial explícito; não ampliar o programa.
4. **Planejar a matriz.** Distribuir objetivos e três ordens conforme a referência canônica.
   Variar reconhecimento de fundamento, interpretação, aplicação e integração sem usar o
   mesmo comando com números diferentes para inflar o lote. Restrições temporárias de uma avaliação são
   locais: não perpetuar exclusões de conteúdo em avaliações futuras.
5. **Construir e revisar.** Definir resposta e percurso antes da vinheta, usando casos inéditos
   quando a aplicação os exigir. Cada alternativa deve representar um erro plausível ligado
   ao objetivo. Aplicar suficiência, unicidade, completude, paridade e testes de atalhos da
   skill. Comentários explicam a resposta já completa; não a corrigem silenciosamente.
6. **Reconciliar o conjunto.** Conferir objetivos distintos, cobertura e ordens finais, inclusive
   os últimos itens. Alteração de alternativa exige atualizar chave e comentário correspondente.
   Não reproduzir uma sequência previsível de letras apenas porque havia equilíbrio no exemplo.
7. **Exportar e inspecionar.** Gerar resolução sem qualquer chave e comentado com as mesmas
   perguntas e opções. Manter mapa de fontes, matriz e auditoria fora do caderno para resolver.
   Conferir PDFs após renderização: pareamento, numeração, legibilidade, cortes, símbolos e
   ausência de respostas no caderno do aluno. Exportação Markdown não confirma qualidade do PDF.

Quando o pedido for especificamente o bloco de objetivas no modelo aprovado, entregar os
dois cadernos sem impor menu já respondido, flashcards, discursivas ou publicação no Anki.
Esses produtos só entram quando fizerem parte do pedido. Isso delimita este modo, sem mudar
pedidos gerais de outros tipos. Quantidade e fontes faltantes só exigem pergunta quando não
puderem ser resolvidas pelo contexto.

## Molde da matriz nos bastidores

Uma linha por objetivo; localizar os segmentos antes de redigir:

| ID | Tema | Objetivo/decisão | Localizador(s) | Ênfase/dúvida/correção observada | Ordem pretendida | Item(s) | Ordem final e percurso mínimo | Conferência |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [id] | [tema] | [uma competência] | [fonte e trecho reais] | [observação ou sem ênfase explícita] | [1/2/3] | [números] | [justificativa] | [achados concretos] |

Objetivo previsto sem item deve ser coberto ou constar como exclusão justificada; item sem
fonte ou fora do programa deve ser revisto. Manter o registro de revisão exigido em
ordem-e-qualidade.md. Preenchimento da tabela não demonstra qualidade por si.

## Base estruturada e exportação

Manter uma lista JSON com os campos abaixo. Produzir `resolucao.md`, `comentado.md`
e `rastreabilidade.md` a partir dessa única lista, com as ferramentas de escrita disponíveis.
Este pacote público não inclui o exportador do ambiente privado. A geração de arquivos
requer uma ferramenta capaz de escrevê-los; em chat sem essa capacidade, entregar os dois
cadernos em blocos separados. Preservar as fontes na rastreabilidade e exibi-las no comentado
quando solicitado.

| Campo | Conteúdo |
| --- | --- |
| `n` | Inteiro sequencial, começando em 1. |
| `tema` | Tema/objetivo técnico; não é exibido como pista no caderno para resolver. |
| `tempo` | Localizador real: intervalo na transcrição, página ou seção; pode indicar vários segmentos. O nome do campo mantém compatibilidade com o precedente. |
| `stem` | Enunciado e comando em um parágrafo. |
| `alts` | Lista de quatro ou cinco alternativas na ordem exibida. |
| `key` | Letra única, correspondente à posição correta. |
| `comments` | Um comentário não vazio para cada opção, na mesma ordem. |
| `fonte` | Identificação da fonte que sustenta o item e das conferências pertinentes. |

Antes de exportar, conferir quantidade, sequência de numeração, alternativas distintas,
chave válida, um comentário por opção e ausência de respostas nos campos públicos. Usar
título neutro. Reutilizar exatamente os mesmos enunciados e opções nos dois cadernos.
Não incluir temas técnicos, fontes, comentários, ordem ou chaves na versão para resolver.
A rastreabilidade contém respostas e fica separada do caderno do aluno.

Nenhuma verificação de formato demonstra precisão clínica, existência da fonte, complexidade,
plausibilidade ou ausência de pistas semânticas. Conferir esses pontos antes de exportar e
inspecionar os PDFs depois de renderizar. Não declarar PDF conferido após gerar apenas Markdown.

## Entrega e continuidade

Registrar a fonte, a base final e as conferências. Preservar versões anteriores e identificar
a edição vigente conforme a organização escolhida pelo usuário. Não misturar rastreabilidade
com respostas e caderno sem respostas. Reproduzir o processo de um modelo aprovado sem presumir
que o novo lote também foi aprovado ou que defeitos do exemplo devam ser preservados.
