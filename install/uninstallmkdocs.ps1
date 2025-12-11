[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

echo 'Uninstalling MKDocs and dependencies'

echo "`nCurrent script's directory: $PSScriptRoot"

& cd $PSScriptRoot\..

$curDir = Get-Location

echo "Changed directory to: $curDir"

echo "`nActivating venv: .\.venv\Scripts\Activate.ps1"
& .\.venv\Scripts\Activate.ps1

echo "`nUninstalling the packages: python3 -m pip uninstall -y -r $PSScriptRoot\requirements.txt"
& python3 -m pip uninstall -y -r $PSScriptRoot\requirements.txt