param(
    [string]$TaskName = 'Thesis1 Auto Sync'
)

$ErrorActionPreference = 'Stop'
$syncScript = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot 'auto-sync.ps1')).Path
$powershell = (Get-Command powershell.exe).Source
$action = New-ScheduledTaskAction -Execute $powershell -Argument "-NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$syncScript`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(2) -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Days 3650)
$user = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal -UserId $user -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description 'Commit and push all changes in the thesis1 Git repository every hour while the user is signed in.' -Force | Out-Null
Write-Output "Installed '$TaskName' for $user. First run: ~2 minutes; then hourly for 10 years while signed in."
