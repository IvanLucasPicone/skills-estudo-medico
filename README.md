# Skills de estudo médico

Seis skills (padrão aberto *Agent Skills*, uma pasta com `SKILL.md`) para preparar e comentar
questões de prova médica: objetivas com gabarito comentado, discursivas com espelho de correção,
flashcards para Anki, comentário de questão e extração do estilo de uma banca. Funcionam no
Google Antigravity, no Gemini CLI, no Claude Code e em qualquer agente que leia `SKILL.md`.

| Skill | O que faz |
|---|---|
| `criador-questoes-multipla-escolha` | questões de múltipla escolha com 4 ou 5 alternativas e gabarito comentado, calibradas por prova-modelo quando houver |
| `fazedor-questoes-discursivas` | questões discursivas com espelho de correção prescritível (dose, via, corte de referência) |
| `flashcards-provas` | flashcards em modo completo (caso clínico) ou rápido (fato atômico), em CSV para Anki ou visual |
| `comentador-questoes-prova` | resolve e comenta questão de múltipla escolha, alternativa por alternativa, com valor e corte de referência |
| `extrator-estilo-prova` | lê uma prova real e extrai a Ficha de Estilo da banca, que as outras skills usam como modelo |
| `publicar-no-anki` | publica os cartões num Anki aberto via AnkiConnect, sem duplicar |

## Instalar no Antigravity ou no Gemini CLI

Mac ou Linux, no Terminal:

```bash
git clone https://github.com/USUARIO/skills-estudo-medico.git
cd skills-estudo-medico
./instalar.sh
```

Windows, no PowerShell:

```powershell
git clone https://github.com/USUARIO/skills-estudo-medico.git
cd skills-estudo-medico
.\instalar.ps1
```

O instalador copia as skills para `~/.gemini/config/skills/`, a pasta que Antigravity (IDE e CLI)
e Gemini CLI reconhecem. Depois é só abrir o Antigravity e pedir, por exemplo, "crie 10 questões
de múltipla escolha sobre insuficiência cardíaca a partir deste PDF" ou "faça flashcards deste
capítulo". O agente escolhe a skill pela descrição.

Para atualizar, na mesma pasta:

```bash
git pull && ./instalar.sh
```

## Como usar bem

- **Mande o material junto** (PDF, slide, texto). As skills geram a partir do que recebem e
  ancoram o gabarito no material; sem material, avisam que estão respondendo de conhecimento geral.
- **Mande uma prova antiga da banca** quando tiver: `extrator-estilo-prova` extrai o padrão de
  redação e as outras skills passam a imitá-lo.
- Um pedido por "questões" entrega os três tipos (flashcards, objetivas e discursivas) do mesmo
  material.
- `publicar-no-anki` é opcional: exige o Anki aberto com o complemento AnkiConnect instalado.

## Origem

Fonte mantida por Ivan Lucas Picone Borges dos Anjos (endocrinologista, HUAP/UFF). Este
repositório é gerado a partir da fonte por script; edite lá, não aqui.
