#!/usr/bin/env bash
# Copia as skills deste repositório para a pasta global de cada agente encontrado na máquina.
set -euo pipefail
cd "$(dirname "$0")"

# Gemini CLI / Antigravity sempre; os demais só se a ferramenta estiver instalada.
DESTINOS=("${HOME}/.gemini/config/skills")
[ -d "${HOME}/.claude" ] && DESTINOS+=("${HOME}/.claude/skills")
[ -d "${HOME}/.codex" ]  && DESTINOS+=("${HOME}/.codex/skills")
[ -d "${HOME}/.agents" ] && DESTINOS+=("${HOME}/.agents/skills")
[ -d "${HOME}/.cursor" ] && DESTINOS+=("${HOME}/.cursor/skills")

for destino in "${DESTINOS[@]}"; do
  mkdir -p "$destino"
  n=0
  for skill in */; do
    skill="${skill%/}"
    [ -f "$skill/SKILL.md" ] || continue
    rm -rf "${destino:?}/$skill"
    cp -R "$skill" "$destino/$skill"
    n=$((n+1))
  done
  echo "$n skills em $destino"
done
echo "Pronto."
