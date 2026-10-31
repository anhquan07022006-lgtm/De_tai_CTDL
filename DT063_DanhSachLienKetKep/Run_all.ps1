param([string]$Julia='julia')
$ErrorActionPreference='Stop'
$codeRoot=$PSScriptRoot
function Run-JuliaStep([string[]]$JuliaArgs) {
    & $Julia @JuliaArgs
    if ($LASTEXITCODE -ne 0) { throw ('Julia failed: '+($JuliaArgs -join ' ')) }
}
Run-JuliaStep @('--version')
for ($caseId=1; $caseId -le 11; $caseId++) {
    Write-Output ('=== DEMO --ca='+$caseId+' ===')
    Run-JuliaStep @('--startup-file=no',(Join-Path $codeRoot 'demo.jl'),('--ca='+$caseId))
}
Write-Output '=== KHAO SAT n=5,20,100 ==='
Run-JuliaStep @('--startup-file=no',(Join-Path $codeRoot 'demo.jl'),'--khao-sat')
Write-Output '=== BO KIEM THU ==='
Run-JuliaStep @('--startup-file=no',(Join-Path $codeRoot 'test/runtests.jl'))
Write-Output 'END_TO_END_OK: 11 demo, khao sat va bo kiem thu da chay xong.'
