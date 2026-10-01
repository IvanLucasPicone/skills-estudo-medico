# Skills de estudo médico

Seis skills (padrão aberto *Agent Skills*, uma pasta com `SKILL.md`) para preparar e comentar
questões de prova médica: objetivas com gabarito comentado, discursivas com espelho de correção,
flashcards para Anki, comentário de questão e extração do estilo de uma banca. Funcionam no
Google Antigravity, no Gemini CLI, no Claude Code, no Codex, no Cursor e em qualquer agente que
leia `SKILL.md`.

| Skill | Função |
|---|---|
| `criador-questoes-multipla-escolha` | objetivas A–D em dois cadernos (resolução sem respostas e comentado); pedido ou modelo pode alterar o padrão |
| `fazedor-questoes-discursivas` | questões discursivas com espelho de correção prescritível (dose, via, corte de referência) |
| `flashcards-provas` | flashcards em modo completo (caso clínico) ou rápido (fato atômico), em CSV para Anki ou visual |
| `comentador-questoes-prova` | resolve e comenta questão de múltipla escolha, alternativa por alternativa, com valor e corte de referência |
| `extrator-estilo-prova` | lê uma prova real e extrai a Ficha de Estilo da banca, que as outras skills usam como modelo |
| `publicar-no-anki` | publica os cartões num Anki aberto via AnkiConnect, sem duplicar |

## Instalar

Mac ou Linux, no Terminal:

```bash
git clone https://github.com/IvanLucasPicone/skills-estudo-medico.git
cd skills-estudo-medico
./instalar.sh
```

Windows, no PowerShell:

```powershell
git clone https://github.com/IvanLucasPicone/skills-estudo-medico.git
cd skills-estudo-medico
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

Sem git: baixe o [ZIP](https://github.com/IvanLucasPicone/skills-estudo-medico/archive/refs/heads/main.zip), extraia, abra o Terminal ou o
PowerShell dentro da pasta extraída e rode o mesmo `./instalar.sh` ou `instalar.ps1`.

O instalador copia as skills para a pasta global de cada agente que encontrar na máquina:

| Agente | Pasta de skills |
|---|---|
| Antigravity (IDE e CLI) e Gemini CLI | `~/.gemini/config/skills/` (sempre) |
| Claude Code | `~/.claude/skills/` (se `~/.claude` existir) |
| Codex | `~/.codex/skills/` e `~/.agents/skills/` (se existirem) |
| Cursor | `~/.cursor/skills/` (se `~/.cursor` existir) |

Depois é só abrir o agente e pedir, por exemplo, "crie 10 questões de múltipla escolha sobre
insuficiência cardíaca a partir deste PDF" ou "faça flashcards deste capítulo". O agente escolhe a
skill pela descrição.

Para atualizar, na mesma pasta:

```bash
git pull && ./instalar.sh
```

## Para o agente de IA que recebeu este link ou este ZIP

Se você é um agente (Claude Code, Codex, Gemini CLI, Antigravity, Cursor ou outro) e uma pessoa
colou o link deste repositório ou anexou o ZIP pedindo para instalar, faça isto:

1. **Obtenha os arquivos.** Com git: `git clone https://github.com/IvanLucasPicone/skills-estudo-medico.git`. Sem git: baixe
   `https://github.com/IvanLucasPicone/skills-estudo-medico/archive/refs/heads/main.zip` e extraia. Se o ZIP já foi anexado à conversa, use os
   arquivos dele.
2. **Descubra onde você lê skills.** Cada pasta deste repositório que contém um `SKILL.md` é uma
   skill. Copie cada uma, com o nome da pasta preservado, para a sua pasta de skills:
   `~/.claude/skills/` (Claude Code; ou `.claude/skills/` dentro do projeto), `~/.codex/skills/` ou
   `~/.agents/skills/` (Codex), `~/.gemini/config/skills/` (Gemini CLI e Antigravity),
   `~/.cursor/skills/` ou `.cursor/skills/` (Cursor). Se a sua ferramenta documenta outra pasta,
   use a documentada. O `instalar.sh` e o `instalar.ps1` fazem exatamente isso para as pastas acima.
3. **Confirme** listando as skills carregadas, ou abrindo um `SKILL.md` copiado, e diga à pessoa
   quais das seis ficaram disponíveis.
4. **Sem pasta de skills** (chat na web, agente sem suporte a skills): leia o `SKILL.md` da skill
   pedida **e as referências locais que ele indicar**, e aplique-os à tarefa nesta conversa.
   O link não instala a skill nem garante sua recuperação em outra conversa. Se não conseguir
   abrir os arquivos, peça o ZIP ou o conteúdo necessário; não diga que leu apenas por receber o link.

Não é preciso instalar dependências. A única exceção é `publicar-no-anki`, que chama um Anki
aberto com o complemento AnkiConnect por `scripts/anki_connect.py` (Python 3, sem pacote extra).

## Como usar bem

- **Mande o material junto** (PDF, slide, texto). As skills geram a partir do que recebem e
  ancoram o gabarito no material; sem material, avisam que estão respondendo de conhecimento geral.
- **Mande uma prova antiga da banca** quando tiver: `extrator-estilo-prova` extrai o padrão de
  redação e as outras skills passam a imitá-lo.
- Um pedido por "questões" sem especificar o tipo entrega flashcards, objetivas e discursivas.
  Um ou dois tipos nomeados delimitam a entrega; não é preciso escrever "só".
- Objetivas usam quatro alternativas e dois cadernos por padrão. Não há menu obrigatório para
  reconfirmar esse formato. Quantidade e exceções vêm do pedido e da prova-modelo.
- As três ordens descrevem o percurso de inferência, não dificuldade medida. Revisar os itens
  mesmo quando seguem uma prova-modelo; não reproduzir pistas e ambiguidades da amostra.
- `publicar-no-anki` é opcional: exige o Anki aberto com o complemento AnkiConnect instalado.

## Origem

Fonte mantida por Ivan Lucas Picone Borges dos Anjos (endocrinologista, HUAP/UFF). Este
repositório distribui uma adaptação pública das fontes canônicas. Atualizações devem preservar exemplos genéricos e referências locais, sem depender da wiki privada.

Atualização de 01/10/2026: cinco skills de elaboração/análise alinhadas às fontes canônicas
atuais, com referências locais de ordem e qualidade, exemplos e produção de blocos baseados
em revisão. `publicar-no-anki` e seu helper foram preservados; as diferenças observadas no
texto canônico eram convenções pessoais de baralho. O recorte permanece em seis skills.

O pacote completo privado também contém organizador e resumidor; eles não fazem parte deste
repositório. Este recorte não deve prometer um pacote completo de resumos. A exportação pareada
é descrita de forma portátil, sem exigir scripts ou acesso ao ambiente privado. Os PURPOSE.md
registram o alcance da adaptação.

## Usar pelo link, instalar ou conectar um MCP

- **Link/ZIP:** o agente lê a skill e suas referências para aplicar as instruções à tarefa.
- **Instalação:** uma ferramenta compatível mantém os arquivos disponíveis para acionamento;
  cópias instaladas precisam ser atualizadas, não acompanham o GitHub automaticamente.
- **MCP:** oferece operações executáveis de um serviço conectado. Não é necessário para ler
  estas instruções e gerar questões com as ferramentas que o agente já possui.

Exemplo de pedido: "Leia o SKILL.md de criador-questoes-multipla-escolha deste repositório e
suas referências. Use essas instruções para criar 20 questões a partir do PDF anexado."

Conferir o material gerado e suas fontes. Compartilhar o repositório não compartilha o acervo
privado do autor nem concede acesso a contas ou a um Anki local.

O helper do Anki recebe campos de texto e normaliza entidades HTML antes de calcular o UID. Não enviar HTML de formatação nos campos: ele será tratado como texto. Remover linhas de metadados antes de exportar cartões.
