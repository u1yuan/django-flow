$ErrorActionPreference = 'Stop'

$repo = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$syncScript = Join-Path $repo 'scripts\auto-sync.ps1'
if (-not (Test-Path -LiteralPath $syncScript -PathType Leaf)) {
    throw "Auto-sync script not found: $syncScript"
}

$taskName = 'ResearchTeam-Git-AutoSync'
$powerShell = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
$action = New-ScheduledTaskAction -Execute $powerShell -Argument "-NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$syncScript`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(2) -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Days 3650)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 15)

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Description "Commit and push repository changes hourly from $repo" -Force | Out-Null
Write-Output "Installed hourly scheduled task '$taskName' for $repo"
