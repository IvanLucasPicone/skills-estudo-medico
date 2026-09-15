---
name: publicar-no-anki
description: "Publica material de estudo (flashcards, questões de múltipla escolha, discursivas) num Anki vivo via AnkiConnect, de forma idempotente (upsert sem duplicar), com decks/subdecks, note types e tags padronizados, e sincronização. NÃO gera conteúdo — é a ponte que leva a saída dos geradores (flashcards-provas, criador-questoes-multipla-escolha, fazedor-questoes-discursivas) para o Anki. Use quando o pedido for 'jogar no Anki', 'espelhar no Anki', 'sincronizar com o Anki', 'criar os cards no baralho' ou montar/atualizar um baralho a partir de conteúdo já estruturado."
---

# 🃏 Publicar no Anki (ponte AnkiConnect)

## Papel
Engenheiro de automação de estudo. Recebe **conteúdo já estruturado** (flashcards, questões de múltipla escolha ou discursivas) e o publica num **Anki vivo** via **AnkiConnect**, de forma **idempotente** (re-rodar não duplica), com decks, note types e tags padronizados, terminando com `sync`. **Não gera conteúdo médico** — isso é das skills geradoras. Separação de responsabilidades: *os geradores produzem; esta skill publica*.

## Quando usar / não usar
- **Usar:** "joga no Anki", "espelha no Anki", "sincroniza com o Anki", "cria os cards", "atualiza o baralho", ou como passo final depois de gerar flashcards/questões.
- **Não usar** para *escrever* as perguntas/respostas (use `flashcards-provas`, `criador-questoes-multipla-escolha`, `fazedor-questoes-discursivas`) nem para sync bidirecional Notion↔Anki (esta ponte é **uma via**: conteúdo → Anki).

## Pré-requisitos (checar antes)
1. **Anki aberto** no desktop com o add-on **AnkiConnect** (escuta em `127.0.0.1:8765` — usar o IP, **nunca** `localhost`: no Windows a resolução tenta IPv6 primeiro e adiciona **2,1 s de overhead fixo por chamada**, o que num lote de ~290 notas é a diferença entre ~40 min e ~50 s. Medido em 2026-07-29: 2,097 s vs 0,038 s).
2. **Python 3** disponível (só usa a stdlib — `urllib`, `hashlib`, `json`).
3. Se o AnkiConnect estiver offline, a skill **não perde conteúdo**: grava um fallback `anki_fallback.jsonl` e avisa; retomar quando o Anki abrir.

## Ferramenta empacotada
`scripts/anki_connect.py` — helper testado. Funções principais:
- `is_available()` · `ensure_deck(nome)` · `ensure_model(spec)` · `ensure_canonical_models()` · `ensure_uid_field(model)`
- `upsert_note(deck, model, fields, tags, key_field)` → insere **ou** atualiza sem duplicar; retorna `("added"|"updated", noteId)`
- `publish_batch({"sync": bool, "notes": [...]})` → publica um lote e sincroniza; offline → grava fallback
- CLI: `python3 scripts/anki_connect.py lote.json` (ou lote por stdin)

## Fluxo
1. **Checar** `is_available()`. Offline → avisar e oferecer gerar CSV/`.apkg` como plano B.
2. **Montar o lote** a partir do conteúdo estruturado: para cada card, um objeto `{deck, model, fields, tags, key_field}`.
3. **Publicar** com `publish_batch` (ele garante deck/note type, faz upsert e `sync`).
4. **Conferir** o retorno (`added`/`updated`/`errors`) e reportar; se `errors`, investigar.

## Convenções de deck, note type e tags
- **Decks/subdecks** por matéria e tipo. Exemplo: `Cardiologia::Flashcards`, `Cardiologia::Objetivas`, `Cardiologia::Discursivas`. Para outro contexto, criar hierarquia análoga (ex.: `Residência::Pendências`).
- **Note types canônicos** (o helper cria via `ensure_canonical_models()` se faltarem; todos com campo `UID` para idempotência robusta):
  - **`Estudo Flashcard`** — campos `Frente, Verso, Fonte, UID`.
  - **`Estudo MCQ (A-E)`** — campos `Enunciado, A, B, C, D, E, Correta, Comentário, Fonte, UID`. O template mostra a alternativa E via bloco condicional `{{#E}}…{{/E}}` — para questões **A–D basta deixar o campo `E` vazio** e a alternativa E some.
  - **`Estudo Discursiva`** — campos `Enunciado, Espelho, Fonte, UID`.
  - *Compatibilidade:* se o baralho já usa modelos sem `UID` (ex.: o `Básico` e outros já existentes), o helper cai no **dedup nativo pelo 1º campo** — funciona igual. Para endurecer, `ensure_uid_field(model)` adiciona `UID` a um modelo existente (melhor esforço).
- **Tags:** sempre marcar tema/origem (ex.: `Cardiologia`, `InsuficienciaCardiaca`, `residencia`). Facilita filtrar e montar baralhos de erro.

## Idempotência (o ponto central)
Publicar o mesmo material duas vezes **não** cria duplicatas:
- Modelo **com `UID`** → chave estável `UID = sha1(deck + campo-chave)`; acha e **atualiza**, ou insere.
- Modelo **sem `UID`** → usa a identidade nativa do Anki (1º campo); se já existe, localiza e atualiza.
- Escolha o `key_field` que identifica unicamente o card (ex.: `Frente` no flashcard, `Enunciado` na questão). Mantê-lo estável entre publicações.

## Exemplo de lote
```json
{
  "sync": true,
  "notes": [
    {"deck": "Cardiologia::Flashcards", "model": "Estudo Flashcard",
     "fields": {"Frente": "Nova nomenclatura do DI central?", "Verso": "AVP-D (deficiência de AVP).", "Fonte": "Angelousi 2023"},
     "tags": ["Cardiologia", "DiabetesInsipidus"], "key_field": "Frente"},
    {"deck": "Cardiologia::Objetivas", "model": "Estudo MCQ (A-E)",
     "fields": {"Enunciado": "...", "A": "...", "B": "...", "C": "...", "D": "...", "E": "", "Correta": "C", "Comentário": "...", "Fonte": "..."},
     "tags": ["Cardiologia", "DiabetesInsipidus"], "key_field": "Enunciado"}
  ]
}
```

## Sinais de corte (`<` e `>`)
Os geradores produzem cortes de referência com `<` e `>` (`Na 108 (<135)`), e o Anki renderiza o campo como HTML: `(<135)` seria lido como abertura de tag e o corte sumiria da tela. O helper `anki_connect.py` escapa `<` e `>` em todo campo de texto antes de calcular o UID (`_html_norm`, idempotente: lote já escapado não é escapado de novo). Nada a fazer no lote; conferir um card depois do `sync`, porque o erro só aparece na renderização.

## Restrições
- Nunca gerar conteúdo médico aqui; só transportar o que os geradores produziram.
- Sempre publicar de forma idempotente (upsert), nunca `addNote` cego que duplica.
- Sempre terminar com `sync` (salvo se o usuário pedir o contrário) e reportar `added/updated/errors`.
- Offline nunca é falha silenciosa: gravar o fallback e avisar.
- Não apagar decks/notas do usuário sem pedido explícito.
