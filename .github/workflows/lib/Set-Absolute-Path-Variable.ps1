param(
    [Parameter(Mandatory)]
    [String]$BasePath,

    [Parameter(Mandatory)]
    [String]$RelativePath,

    [Parameter(Mandatory)]
    [String]$VariableName
)

Write-Output "BasePath: ${BasePath}"
Write-Output "RelativePath: ${RelativePath}"
Write-Output "VariableName: ${VariableName}"

$FinalPath = "${BasePath}\${RelativePath}"

if ($IsLinux) {
    $FinalPath = ${FinalPath}.Replace('\','/')
} else {
    $FinalPath = ${FinalPath}.Replace('/','\')
}

Write-Output "Setting ${VariableName}: ${FinalPath}"

Write-Output "${VariableName}=${FinalPath}" | Out-File -FilePath $Env:GITHUB_ENV -Encoding utf8 -Append

Write-Output "Set ${VariableName}: ${FinalPath}"