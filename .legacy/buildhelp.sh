#! /bin/bash
# This script deploys Python vitrual environment, MkDocs and its dependencies
# Then it builds MkDocs help
# Pass the `Help` folder path as first parameter to the script
# This script is called by the `Build\scripts\magic\_site.sh`

echo "Creating venv: py -m venv .venv --upgrade-deps"
cd $1
pwd
python3 -m venv .venv --upgrade-deps

echo "Activating venv: source .venv/bin/activate"
cd $1 
pwd
. ./.venv/bin/activate
cd $1
pwd

echo "Updating pip: python3 -m pip install --upgrade pip"
python3 -m pip install --upgrade pip

echo "Installing MkDocs and dependencies: python3 -m pip install -U -r install/requirements.txt"
python3 -m pip install -U -r install/requirements.txt

echo "Finished deploying Venv with Python and MkDocs"

echo "Checking MkDocs version:"
python3 -m mkdocs -V

echo "Changed directory to: $curDir"

echo "Executing $PSScriptRoot\buildhelp.py"
python3 ./buildhelp.py
deactivate
echo "Finished building Help"
