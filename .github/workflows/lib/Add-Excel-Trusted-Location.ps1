param(
    [Parameter(Mandatory)]
    [String]$Path
)

$baseRegistryPath = "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations\"

Write-Output "Adding Excel Trusted Location: ${Path}"
Write-Output "Base Target Trusted Location Key: ${baseRegistryPath}"

$locations = Get-ChildItem -Path $baseRegistryPath
$locationCount = $locations.Count

if($locationCount -ge 20)
{
    Write-Error "There are too many trusted locations already. The maximum is 20. There are currently: ${locationCount}"
    Exit
}

$registryPath = "${baseRegistryPath}Location${locationCount}"

Write-Output "New Target Trusted Location Key: ${registryPath}"

New-Item -Path ${registryPath} -Force
Set-ItemProperty -Path $registryPath -Name "Path" -Value ${Path}
Set-ItemProperty -Path $registryPath -Name "Description" -Value "GitHub Action Trusted Location"
Set-ItemProperty -Path $registryPath -Name "AllowSubfolders" -Value 1

Write-Output "Added Excel Trusted Location: ${Path} to ${registryPath}"
