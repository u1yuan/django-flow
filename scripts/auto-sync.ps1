param(
    [string]$Branch = 'main'
)

$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path

function Invoke-Git {
    param([string[]]$GitArgs)
    & git -C $repo @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "git $($GitArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
}

$currentBranch = (& git -C $repo branch --show-current).Trim()
if ($LASTEXITCODE -ne 0 -or $currentBranch -ne $Branch) {
    throw "Auto-sync requires branch '$Branch'; current branch is '$currentBranch'."
}

# Fetch first so an unattended run never force-pushes over remote work.
Invoke-Git -GitArgs @('fetch', 'origin', $Branch)
& git -C $repo merge-base --is-ancestor "origin/$Branch" HEAD
if ($LASTEXITCODE -ne 0) {
    throw "origin/$Branch is ahead or diverged. Resolve it manually before auto-sync resumes."
}

Invoke-Git -GitArgs @('add', '-A')
& git -C $repo diff --cached --quiet
if ($LASTEXITCODE -eq 1) {
    Invoke-Git -GitArgs @('commit', '-m', 'chore: auto-sync local changes')
} elseif ($LASTEXITCODE -ne 0) {
    throw "Could not inspect staged changes (exit code $LASTEXITCODE)."
}

$localHead = (& git -C $repo rev-parse HEAD).Trim()
$remoteHead = (& git -C $repo rev-parse "origin/$Branch").Trim()
if ($localHead -ne $remoteHead) {
    Invoke-Git -GitArgs @('push', 'origin', $Branch)
} else {
    Write-Output 'Nothing to commit or push.'
}
