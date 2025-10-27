#!/usr/bin/env python3
"""
PDF Duplication Utility with Date Suffix

Duplicates PDF files in the current directory and adds a date suffix
in YYYY.MM.DD format to the copies.

Usage:
    python duplicate_pdfs_with_date.py

Result:
    original_file.pdf -> original_file.YYYY.MM.DD.pdf
"""

import shutil
from datetime import datetime
from pathlib import Path


def duplicate_pdfs_with_date():
    """
    Duplicate PDF files modified today in the current directory with date suffix.
    
    Only processes PDF files that were modified today (based on modification time),
    creates copies with the current date appended in YYYY.MM.DD format.
    """
    # Get current working directory
    cwd = Path('.')
    
    # Get today's date
    today = datetime.now().date()
    date_suffix = today.strftime('%Y.%m.%d')
    
    # Find all PDF files
    pdf_files = list(cwd.glob('*.pdf'))
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    # Filter PDFs modified today
    today_pdfs = []
    for pdf_file in pdf_files:
        mod_time = datetime.fromtimestamp(pdf_file.stat().st_mtime).date()
        if mod_time == today:
            today_pdfs.append(pdf_file)
    
    if not today_pdfs:
        print(f"No PDF files modified today ({date_suffix}).")
        return
    
    print(f"Found {len(today_pdfs)} PDF file(s) modified today.")
    print(f"Date suffix: {date_suffix}\n")
    
    # Duplicate each PDF file
    duplicated_count = 0
    for pdf_file in today_pdfs:
        # Skip files that already have today's date suffix
        if date_suffix in pdf_file.name:
            print(f"Skipping {pdf_file.name} (already has date suffix)")
            continue
        
        # Construct new filename: original_name.YYYY.MM.DD.pdf
        new_filename = pdf_file.stem + f'. {date_suffix}.pdf'
        new_path = pdf_file.parent / new_filename
        
        # Check if duplicate already exists
        if new_path.exists():
            print(f"Skipping {pdf_file.name} -> {new_filename} (file already exists)")
            continue
        
        # Create copy
        try:
            shutil.copy2(pdf_file, new_path)
            print(f"Created: {pdf_file.name} -> {new_filename}")
            duplicated_count += 1
        except Exception as e:
            print(f"Error copying {pdf_file.name}: {e}")
    
    print(f"\nCompleted duplicating {duplicated_count} file(s).")


if __name__ == "__main__":
    duplicate_pdfs_with_date()

