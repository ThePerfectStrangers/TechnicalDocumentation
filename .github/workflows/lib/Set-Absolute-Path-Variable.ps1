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

if ($IsLinux) {
    $UpdatedRelativePath = ${RelativePath}.Replace('\','/')
} else {
    $UpdatedRelativePath = ${RelativePath}.Replace('/','\')
}

Write-Output "Setting ${VariableName}: ${BasePath}\${UpdatedRelativePath}"

Write-Output "${VariableName}=${BasePath}\${UpdatedRelativePath}" | Out-File -FilePath $Env:GITHUB_ENV -Encoding utf8 -Append

Write-Output "Set ${VariableName}: ${BasePath}\${UpdatedRelativePath}"