# Copia as skills deste repositório para a pasta global do Antigravity / Gemini CLI.
$destino = Join-Path $HOME ".gemini\config\skills"
New-Item -ItemType Directory -Force -Path $destino | Out-Null
Set-Location $PSScriptRoot
Get-ChildItem -Directory | ForEach-Object {
  if (Test-Path (Join-Path $_.FullName "SKILL.md")) {
    $alvo = Join-Path $destino $_.Name
    if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }
    Copy-Item -Recurse $_.FullName $alvo
    Write-Host "instalada: $($_.Name)"
  }
}
Write-Host "Pronto. Skills em $destino"
