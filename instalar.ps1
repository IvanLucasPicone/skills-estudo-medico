# Copia as skills deste repositório para a pasta global de cada agente encontrado na máquina.
Set-Location $PSScriptRoot
# Gemini CLI / Antigravity sempre; os demais só se a ferramenta estiver instalada.
$destinos = @((Join-Path $HOME ".gemini\config\skills"))
foreach ($par in @(@(".claude", ".claude\skills"), @(".codex", ".codex\skills"),
                  @(".agents", ".agents\skills"), @(".cursor", ".cursor\skills"))) {
  if (Test-Path (Join-Path $HOME $par[0])) { $destinos += (Join-Path $HOME $par[1]) }
}
foreach ($destino in $destinos) {
  New-Item -ItemType Directory -Force -Path $destino | Out-Null
  $n = 0
  Get-ChildItem -Directory | ForEach-Object {
    if (Test-Path (Join-Path $_.FullName "SKILL.md")) {
      $alvo = Join-Path $destino $_.Name
      if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }
      Copy-Item -Recurse $_.FullName $alvo
      $n++
    }
  }
  Write-Host "$n skills em $destino"
}
Write-Host "Pronto."
