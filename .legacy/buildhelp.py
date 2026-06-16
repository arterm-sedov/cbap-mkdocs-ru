# The language list is set in line 23 as LANGUAGE_LIST 

# After running this script, you should see the newly compiled help subfolders in the `compiled_help` folder:
#     * en
#     * ru

# from __future__ import unicode_literals, absolute_import

import os
import sys
import shutil
import subprocess
from sys import platform

LANGUAGE_LIST = ["ru"]
THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
HELP_SOURCE_DIR = THIS_FILE_DIR
DOCS_DIR = os.path.join(HELP_SOURCE_DIR, "docs")
BUILD_SCRIPT = os.path.join(HELP_SOURCE_DIR, "buildhelp.ps1")
HELP_COMPILED_DIR = os.path.join(THIS_FILE_DIR, "compiled_help")
EXTRA_STYLESHEETS_SOURCE_DIR = os.path.join(DOCS_DIR, "stylesheets")
EXTRA_STYLESHEETS_COMPILED_DIR = os.path.join(HELP_COMPILED_DIR, "stylesheets")

def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if not is_venv():
    print("\nNo Python Virtual Environment Found\nInstead of buildhelp.py run %s\n" % BUILD_SCRIPT)
    sys.exit(1) 
    
os.chdir(HELP_SOURCE_DIR)

print("\nPython Venv found, checking if mkdocs is installed\n")
try:
    import mkdocs
except ImportError:
    print("MkDocs not found\n")
    sys.exit(1) 
os.chdir(HELP_SOURCE_DIR)
print("MkDocs is present")

def build_mkdocs(langCodes):
    if os.path.exists(HELP_COMPILED_DIR):
        print("\nFound %s folder\nDeleting it" % HELP_COMPILED_DIR)
        try:
            shutil.rmtree(HELP_COMPILED_DIR, ignore_errors=True, onerror=None)
            print("\nDeleted the %s folder\n" % HELP_COMPILED_DIR)
        except IOError:
                print("\nCould not delete the the %s folder\n" % HELP_COMPILED_DIR)
    
    for langCode in langCodes:
        CONFIG_FILE = resolve_condig_filename(langCode)
        if CONFIG_FILE:
            print("\nCompiling the mkdocs for %s:\n %s\n" % (langCode.upper(), CONFIG_FILE))
            if platform == "linux" or platform == "linux2":
                mkdocs_process = subprocess.Popen("python3.10 -m mkdocs build -f " + CONFIG_FILE, shell=True)
            else:
                mkdocs_process = subprocess.Popen("py -m mkdocs build -f " + CONFIG_FILE)
            std_op, std_err_op = mkdocs_process.communicate()

            print(std_err_op, "\n", std_op)

    return True

def resolve_condig_filename(langCode):

    fileName = "mkdocs_" + langCode + ".yml"
    CONFIG_FILE = os.path.join(HELP_SOURCE_DIR, fileName)
    if os.path.exists(CONFIG_FILE):
        print("\nFound the %s language config file:\n %s\n" % 
         (langCode.upper(), CONFIG_FILE))
        return CONFIG_FILE
    else: 
        print("\nNo %s language config file:\n %s\n" % 
        (langCode.upper(), CONFIG_FILE))
        return False

if __name__ == "__main__":

    if not os.path.isdir(DOCS_DIR):
        print("This NOT the source Help directory: %s" % HELP_SOURCE_DIR)
        sys.exit(1)
    else: 
        os.chdir(HELP_SOURCE_DIR)

    print("\nLanguages to build:", LANGUAGE_LIST)

    if build_mkdocs(LANGUAGE_LIST):
        print('\nFinished compiling the mkdocs\n')
    else: 
        print('\nCould not compile the mkdocs\n')
        sys.exit(1)
