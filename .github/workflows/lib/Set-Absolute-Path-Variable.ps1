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

Write-Output "Setting ${VariableName}: ${BasePath}\${RelativePath}"

Write-Output "${VariableName}=${BasePath}\${RelativePath}" | Out-File -FilePath $Env:GITHUB_ENV -Encoding utf8 -Append

Write-Output "Set ${VariableName}: ${BasePath}\${RelativePath}"