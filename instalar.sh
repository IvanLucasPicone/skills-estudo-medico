#!/usr/bin/env bash
# Copia as skills deste repositório para a pasta global do Antigravity / Gemini CLI.
set -euo pipefail
DESTINO="${HOME}/.gemini/config/skills"
mkdir -p "$DESTINO"
cd "$(dirname "$0")"
for skill in */; do
  skill="${skill%/}"
  [ -f "$skill/SKILL.md" ] || continue
  rm -rf "$DESTINO/$skill"
  cp -R "$skill" "$DESTINO/$skill"
  echo "instalada: $skill"
done
echo "Pronto. Skills em $DESTINO"
