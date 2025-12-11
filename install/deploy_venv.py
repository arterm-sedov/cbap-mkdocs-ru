#!/usr/bin/env python3
"""
Cross-platform Python virtual environment deployment script for MkDocs
Based on deploy.sh, LinuxInstruction.txt, and deploymkdocs.ps1

This script:
- Creates a Python virtual environment with a user-specified name
- Installs MkDocs and all required dependencies
- Works on Windows, Linux, and macOS
- Provides detailed logging and error handling
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path


def get_script_directory():
    """Get the directory where this script is located."""
    return Path(__file__).parent.absolute()


def get_project_root():
    """Get the project root directory (parent of install directory)."""
    return get_script_directory().parent


def get_python_command():
    """Get the appropriate Python command based on the platform."""
    system = platform.system().lower()
    
    if system == "windows":
        # Try py launcher first, then python3, then python
        for cmd in ["py", "python3", "python"]:
            if shutil.which(cmd):
                return cmd
    else:
        # On Unix-like systems, try python3 first, then python
        for cmd in ["python3", "python"]:
            if shutil.which(cmd):
                return cmd
    
    raise RuntimeError("Python not found. Please install Python 3.7 or higher.")


def run_command(command, cwd=None, check=True):
    """Run a command and return the result."""
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            check=check,
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            print(result.stdout)
        if result.stderr and result.returncode != 0:
            print(f"Error: {result.stderr}")
            
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        raise


def create_virtual_environment(venv_name, project_root):
    """Create a new virtual environment."""
    venv_path = project_root / venv_name
    
    if venv_path.exists():
        response = input(f"Virtual environment '{venv_name}' already exists. Remove it? (y/N): ")
        if response.lower() in ['y', 'yes']:
            print(f"Removing existing virtual environment: {venv_path}")
            shutil.rmtree(venv_path)
        else:
            print("Keeping existing virtual environment.")
            return venv_path
    
    python_cmd = get_python_command()
    print(f"Creating virtual environment '{venv_name}' using {python_cmd}")
    
    # Create virtual environment
    run_command(f"{python_cmd} -m venv {venv_name} --upgrade-deps", cwd=project_root)
    
    return venv_path


def get_activation_command(venv_path):
    """Get the appropriate activation command based on the platform."""
    system = platform.system().lower()
    
    if system == "windows":
        activate_script = venv_path / "Scripts" / "activate.bat"
        python_exe = venv_path / "Scripts" / "python.exe"
    else:
        activate_script = venv_path / "bin" / "activate"
        python_exe = venv_path / "bin" / "python"
    
    return activate_script, python_exe


def install_dependencies(venv_path, requirements_file):
    """Install dependencies in the virtual environment."""
    system = platform.system().lower()
    
    if system == "windows":
        pip_exe = venv_path / "Scripts" / "pip.exe"
        python_exe = venv_path / "Scripts" / "python.exe"
    else:
        pip_exe = venv_path / "bin" / "pip"
        python_exe = venv_path / "bin" / "python"
    
    # Upgrade pip
    print("Upgrading pip...")
    run_command(f'"{python_exe}" -m pip install --upgrade pip')
    
    # Install requirements
    print(f"Installing dependencies from {requirements_file}")
    run_command(f'"{python_exe}" -m pip install -U -r "{requirements_file}"')
    
    return python_exe


def check_mkdocs_version(python_exe):
    """Check and display MkDocs version."""
    try:
        result = run_command(f'"{python_exe}" -m mkdocs -V', check=False)
        if result.returncode == 0:
            print(f"MkDocs version: {result.stdout.strip()}")
        else:
            print("Could not determine MkDocs version")
    except Exception as e:
        print(f"Error checking MkDocs version: {e}")


def main():
    """Main deployment function."""
    print("=" * 60)
    print("MkDocs Virtual Environment Deployment Script")
    print("=" * 60)
    
    # Get script and project directories
    script_dir = get_script_directory()
    project_root = get_project_root()
    
    print(f"Script directory: {script_dir}")
    print(f"Project root: {project_root}")
    
    # Get virtual environment name from user
    while True:
        venv_name = input("\nEnter virtual environment directory name (default: .venv): ").strip()
        if not venv_name:
            venv_name = ".venv"
        
        # Validate directory name (allow dots, hyphens, underscores, and alphanumeric)
        # Remove dots, hyphens, and underscores for validation
        if not venv_name.replace("_", "").replace("-", "").replace(".", "").isalnum():
            print("Invalid directory name. Use only letters, numbers, dots, hyphens, and underscores.")
            continue
        
        break
    
    print(f"\nUsing virtual environment name: {venv_name}")
    
    # Check if requirements file exists
    requirements_file = script_dir / "requirements.txt"
    if not requirements_file.exists():
        print(f"Error: Requirements file not found at {requirements_file}")
        sys.exit(1)
    
    try:
        # Create virtual environment
        venv_path = create_virtual_environment(venv_name, project_root)
        print(f"Virtual environment created at: {venv_path}")
        
        # Install dependencies
        python_exe = install_dependencies(venv_path, requirements_file)
        
        # Check MkDocs version
        check_mkdocs_version(python_exe)
        
        print("\n" + "=" * 60)
        print("Deployment completed successfully!")
        print("=" * 60)
        
        # Display activation instructions
        system = platform.system().lower()
        if system == "windows":
            print(f"\nTo activate the virtual environment, run:")
            print(f"  {venv_path}\\Scripts\\activate.bat")
            print(f"\nTo serve the MkDocs site, run:")
            print(f"  {venv_path}\\Scripts\\python.exe -m mkdocs serve")
        else:
            print(f"\nTo activate the virtual environment, run:")
            print(f"  source {venv_path}/bin/activate")
            print(f"\nTo serve the MkDocs site, run:")
            print(f"  {venv_path}/bin/python -m mkdocs serve")
        
    except Exception as e:
        print(f"\nError during deployment: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
