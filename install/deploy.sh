#! /bin/bash

# This script deploys Python vitrual environment, MkDocs and its dependencies
# Run this script to compile and preview the live MkDocs site without building the whole product

echo "Deploying virtual environment with Python, MkDocs, and dependencies"

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)

echo "Current script's directory: $SCRIPT_DIR"

# Go to the parent directory of the script
cd "$SCRIPT_DIR/../"

# Get the current directory
CUR_DIR=$(pwd)

echo "Changed directory to: $CUR_DIR"

echo "Creating venv: python3 -m venv .venv --upgrade-deps"
python3 -m venv .venv --upgrade-deps

echo "Activating venv: source .venv/bin/activate"
source .venv/bin/activate

echo "Updating pip: python3 -m pip install --upgrade pip"
python3 -m pip install --upgrade pip

echo "Installing MkDocs and dependencies: python3 -m pip install -U -r $SCRIPT_DIR/requirements.txt"
python3 -m pip install -U -r "$SCRIPT_DIR/requirements.txt"

echo "Finished deploying Venv with Python and MkDocs"

echo "Checking MkDocs version:"
python3 -m mkdocs -V

echo "Now you can run 'mkdocs serve' to serve the live help site"