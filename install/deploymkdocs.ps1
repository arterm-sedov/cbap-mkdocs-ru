# This script deploys Python vitrual environment, MkDocs and its dependencies
# Run this script to compile and preview the live MkDocs site without building the whole product
# This script is also called by buildhelp.ps1

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

echo "`nDeploying virtual environment with Python, MkDocs, and dependencies"

echo "`nCurrent script's directory: $PSScriptRoot"

& cd $PSScriptRoot/../

$curDir = Get-Location

echo "Changed directory to: $curDir"

if ([System.Environment]::OSVersion.Platform -eq 'Unix') {
 echo "`nCreating venv: python3 -m venv .venv --upgrade-deps"
 & python3 -m venv .venv --upgrade-deps

 echo "`nActivating venv: ./.venv/bin/Activate.ps1"
 ./.venv/bin/Activate.ps1
 
 echo "`nUpdating pip: python3 -m pip install --upgrade pip"
 & python3 -m pip install --upgrade pip
 
 echo "`nInstalling MkDocs and dependencies: python3 -m pip install -U -r $PSScriptRoot/requirements.txt"
 & python3 -m pip install -U -r $PSScriptRoot/requirements.txt

 echo "`nFinished deploying Venv with Python and MkDocs"

 echo "`nChecking MkDocs version:"
 & python3 -m mkdocs -V
}
else{
 echo "`nCreating venv: py -m venv .venv --upgrade-deps"
 & py -m venv .venv --upgrade-deps

 echo "`nActivating venv: ./.venv/Scripts/Activate.ps1"
 ./.venv/Scripts/Activate.ps1
 
 echo "`nUpdating pip: py -m pip install --upgrade pip"
 & py -m pip install --upgrade pip
 
 echo "`nInstalling MkDocs and dependencies: py -m pip install -U -r $PSScriptRoot/requirements.txt"
 & py -m pip install -U -r $PSScriptRoot/requirements.txt

 echo "`nFinished deploying Venv with Python and MkDocs"

 echo "`nChecking MkDocs version:"
 & py -m mkdocs -V
}

echo "`nNow you can run 'mkdocs serve' to serve the live help site"