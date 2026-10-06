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

function Get-AutoSyncCommitMessage {
    $raw = (& git -C $repo diff --cached --name-status --no-renames 2>$null)
    if ($LASTEXITCODE -ne 0 -or -not $raw) {
        return @('chore: auto-sync local changes', $null)
    }

    $entries = @(
        foreach ($line in $raw) {
            if ($line -match '^(?<status>[AMDRCU?])\s+(?<path>.+)$') {
                [pscustomobject]@{
                    Status = $matches['status']
                    Path   = $matches['path'].Trim()
                }
            }
        }
    )
    if ($entries.Count -eq 0) {
        return @('chore: auto-sync local changes', $null)
    }

    $added = @($entries | Where-Object Status -eq 'A').Count
    $modified = @($entries | Where-Object Status -eq 'M').Count
    $deleted = @($entries | Where-Object Status -eq 'D').Count
    $other = $entries.Count - $added - $modified - $deleted

    $parts = @()
    if ($added) { $parts += "$added added" }
    if ($modified) { $parts += "$modified updated" }
    if ($deleted) { $parts += "$deleted removed" }
    if ($other) { $parts += "$other other" }
    $changeSummary = $parts -join ', '

    function Get-TopArea {
        param([string]$Path)
        if ($Path -match '^([^/\\]+)[/\\]') { return $matches[1] }
        return $Path
    }

    $areas = $entries.Path | ForEach-Object { Get-TopArea $_ } |
        Group-Object | Sort-Object Count -Descending
    $areaBits = @(
        foreach ($g in ($areas | Select-Object -First 4)) {
            if ($g.Count -gt 1) { "$($g.Name) ($($g.Count))" } else { $g.Name }
        }
    )
    $areaSummary = $areaBits -join ', '
    if ($areas.Count -gt 4) {
        $areaSummary += ", +$($areas.Count - 4) more"
    }

    if ($entries.Count -eq 1) {
        $subject = "chore: sync $($entries[0].Path)"
    } else {
        $subject = "chore: sync $($entries.Count) files ($changeSummary) in $areaSummary"
    }

    if ($subject.Length -gt 72) {
        $subject = $subject.Substring(0, 69) + '...'
    }

    $bodyLines = @('Auto-sync staged changes:', '')
    $maxLines = 40
    $listed = $entries | Select-Object -First $maxLines
    foreach ($e in $listed) {
        $label = switch ($e.Status) {
            'A' { 'add' }
            'M' { 'update' }
            'D' { 'remove' }
            default { $e.Status.ToLowerInvariant() }
        }
        $bodyLines += "- $label $($e.Path)"
    }
    if ($entries.Count -gt $maxLines) {
        $remaining = $entries.Count - $maxLines
        $bodyLines += "- ... and $remaining more"
    }

    return @($subject, ($bodyLines -join "`n"))
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
    $subject, $body = Get-AutoSyncCommitMessage
    if ($body) {
        Invoke-Git -GitArgs @('commit', '-m', $subject, '-m', $body)
    } else {
        Invoke-Git -GitArgs @('commit', '-m', $subject)
    }
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
