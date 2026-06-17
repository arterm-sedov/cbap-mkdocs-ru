[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

echo "`nBuilding Help"

$originalFolder = $PSScriptRoot

echo "`nHelp source folder: $originalFolder"

& cd $originalFolder

$curDir = Get-Location
echo "Changed directory to: $curDir"

& ./install/deploymkdocs.ps1

& cd $originalFolder

$curDir = Get-Location
echo "Changed directory to: $curDir"

echo "`nExecuting $PSScriptRoot\buildhelp.py"
if ([System.Environment]::OSVersion.Platform -eq 'Unix') {
 & python3 ./buildhelp.py
}
else {
 & py ./buildhelp.py
}

echo "`nFinished building Help"
