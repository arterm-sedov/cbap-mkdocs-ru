#!/usr/bin/env python
"""Simple test runner script for SSH utility tests.

This script can be used to run tests without pytest if needed,
or as a wrapper around pytest for convenience.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path so we can import tools.ssh_kb_ru
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def main():
    """Run tests using pytest."""
    try:
        import pytest
    except ImportError:
        print("ERROR: pytest is not installed.")
        print("Install it with: pip install pytest pytest-cov pytest-mock")
        return 1
    
    # Change to project root directory
    os.chdir(project_root)
    
    # Run pytest with test directory
    test_dir = project_root / ".tests"
    return pytest.main([
        str(test_dir),
        "-v",
        "--tb=short",
    ])

if __name__ == "__main__":
    sys.exit(main())
