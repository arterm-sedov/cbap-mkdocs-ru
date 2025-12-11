[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# This script collects all currently installed 
# Python packages in a list: frozen.txt
# This file can then be used to populate the requirements.txt
# for the purposes of configuration management

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

echo "`nWriting current dependencies list into frozen.txt"

echo "`nCurrent script's directory: $PSScriptRoot"

& cd $PSScriptRoot

$curDir = Get-Location

echo "Changed directory to: $curDir"

if ([System.Environment]::OSVersion.Platform -eq 'Unix') {
    echo "`nActivating venv: ./.venv/bin/Activate.ps1"
    ./.venv/bin/Activate.ps1

    echo "`nCreating  frozen.txt: py -m pip freeze > frozen.txt"
    & python3 -m pip freeze > frozen.txt
}
else {

    echo "`nActivating venv: ./.venv/Scripts/Activate.ps1"
    & ../.venv/Scripts/Activate.ps1
    
    echo "`nCreating  frozen.txt: py -m pip freeze > frozen.txt"
    & py -m pip freeze > frozen.txt
    
}