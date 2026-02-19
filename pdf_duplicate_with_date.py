#!/usr/bin/env python3
"""
PDF Duplication Utility with Date Suffix

Duplicates PDF files in the current directory and adds a date suffix
in YYYY.MM.DD format to the copies.

Configuration:
    Create a .env file with PDF_DATED_DIR=/path/to/target/directory
    If not specified, copies files to current directory

Usage:
    python duplicate_pdfs_with_date.py

Result:
    original_file.pdf -> original_name.YYYY.MM.DD.pdf (in target directory or current dir)
"""

import os
import sys
import shutil
from datetime import datetime
from pathlib import Path

# Try to import dotenv, but make it optional
try:
    from dotenv import load_dotenv as _load_dotenv
    _dotenv_available = True
except ImportError:
    _dotenv_available = False
    _load_dotenv = None


def get_target_directory():
    """Get target directory from environment or use current directory.
    
    Returns:
        tuple: (directory_path, is_from_env) where is_from_env is True if path came from .env
    """
    target_dir = None
    from_env = False
    
    if _dotenv_available and _load_dotenv is not None:
        _load_dotenv()
        target_dir = os.getenv('PDF_DATED_DIR')
        if target_dir:
            from_env = True
    
    if target_dir:
        # Expand ~ to user's home directory
        target_dir = os.path.expanduser(target_dir)
        return os.path.normpath(target_dir), from_env
    
    # Default to current directory (PWD)
    return os.getcwd(), from_env


def prompt_overwrite(filename):
    """Prompt user for overwrite decision.
    
    Returns:
        tuple: (should_overwrite, yes_to_all) where yes_to_all indicates apply to all future files
    """
    while True:
        response = input(f"File '{filename}' already exists. Overwrite? [y/n/a(=yes to all)/q(=quit)]: ").strip().lower()
        if response in ('y', 'yes'):
            return True, False
        elif response in ('n', 'no'):
            return False, False
        elif response in ('a', 'all'):
            return True, True
        elif response in ('q', 'quit'):
            print("Aborted by user.")
            sys.exit(0)
        else:
            print("Please enter y (yes), n (no), a (all), or q (quit)")


def duplicate_pdfs_with_date():
    """
    Duplicate PDF files modified today with date suffix.
    
    Copies PDFs modified today to target directory with YYYY.MM.DD suffix.
    """
    # Get target directory
    target_dir, from_env = get_target_directory()
    
    # Validate target directory
    target_path = Path(target_dir)
    if not target_path.is_absolute():
        target_dir = os.path.join(os.getcwd(), target_dir)
        target_path = Path(target_dir)
    
    # Create target directory only if configured via .env
    if from_env:
        try:
            target_path.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            print(f"Error: Permission denied creating directory: {target_dir}")
            print("Try using a different PDF_DATED_DIR in .env file")
            return
        except Exception as e:
            print(f"Error creating directory {target_dir}: {e}")
            return
        print(f"Target directory (from .env): {target_dir}\n")
    else:
        print(f"Target directory (.env not configured, using current directory): {target_dir}\n")
    
    # Get current working directory for source files
    cwd = Path.cwd()
    
    # Get today's date
    today = datetime.now().date()
    date_suffix = today.strftime('%Y.%m.%d')
    
    # Find all PDF files
    pdf_files = [f for f in cwd.iterdir() if f.is_file() and f.suffix.lower() == '.pdf']
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    # Filter PDFs modified today
    today_pdfs = []
    for pdf_file in pdf_files:
        try:
            mod_time = datetime.fromtimestamp(pdf_file.stat().st_mtime).date()
            if mod_time == today:
                today_pdfs.append(pdf_file)
        except OSError:
            continue
    
    if not today_pdfs:
        print(f"No PDF files modified today ({date_suffix}).")
        return
    
    print(f"Found {len(today_pdfs)} PDF file(s) modified today.")
    print(f"Date suffix: {date_suffix}\n")
    
    # Duplicate each PDF file
    duplicated_count = 0
    skipped_count = 0
    errors = []
    yes_to_all = False
    
    for pdf_file in today_pdfs:
        # Skip files that already have today's date suffix
        if date_suffix in pdf_file.name:
            print(f"Skipping {pdf_file.name} (already has date suffix)")
            continue
        
        # Construct new filename: original_name.YYYY.MM.DD.pdf
        new_filename = f"{pdf_file.stem}. {date_suffix}{pdf_file.suffix}"
        dest_path = target_path / new_filename
        
        # Check if duplicate already exists
        if dest_path.exists():
            if not yes_to_all:
                should_overwrite, yes_to_all = prompt_overwrite(new_filename)
                if not should_overwrite:
                    print(f"Skipping {pdf_file.name} -> {new_filename}")
                    skipped_count += 1
                    continue
            # If yes_to_all is True, we proceed with overwrite
        
        # Create copy
        try:
            shutil.copy2(str(pdf_file), str(dest_path))
            action = "Overwritten" if dest_path.exists() else "Created"
            print(f"{action}: {pdf_file.name} -> {new_filename}")
            duplicated_count += 1
        except PermissionError:
            errors.append(f"Permission denied copying {pdf_file.name}")
            print(f"Error: Permission denied copying {pdf_file.name}")
        except Exception as e:
            errors.append(f"Error copying {pdf_file.name}: {e}")
            print(f"Error copying {pdf_file.name}: {e}")
    
    print(f"\nCompleted: {duplicated_count} file(s) duplicated, {skipped_count} skipped.")
    
    if errors:
        print(f"\n{len(errors)} error(s) occurred:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)


if __name__ == "__main__":
    duplicate_pdfs_with_date()
