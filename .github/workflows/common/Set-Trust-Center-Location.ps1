<#
    .NOTES
        Author:         Chad Birch
        Version:        1.0
        Last Updated:   2024/08/07
    .SYNOPSIS
        This script sets the path passsed in via parameter as a Trusted Location
    .DESCRIPTION
        This script sets the path passsed in via parameter as a Trusted Location
    .EXAMPLE
        .\Set-Trust-Center-Location.ps1 -Path "C:\My\Code"
    .LINK
        https://github.com/ThePerfectStrangers
#>

param (
    [Parameter(Mandatory = $true, HelpMessage = "The path to trust.")][string]$Path
)


Write-Host "Setting Trust Center Location: $Path"

$trustCenterPath = "HKCU:\Software\Microsoft\Office\16.0\Excel\Security\Trusted Locations\LocationX"
New-Item -Path $trustCenterPath -Force
Set-ItemProperty -Path $trustCenterPath -Name "Path" -Value $Path
Set-ItemProperty -Path $trustCenterPath -Name "AllowSubfolders" -Value 1

Write-Host "New Trust Center Location: $Path"
