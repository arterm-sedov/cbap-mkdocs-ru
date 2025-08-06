## AI-enabled Repo

Chat with DeepWiki to get answers about the Comindware Plafrom from this repo:

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

# How to Initialize MkDocs Environment and Build Help Files

This is the MkDocs repository with source files for the RU CMW knowledge base.

## Initialize the Environment

1. Install Python:

   - Change dir to `Help` under the solution root directory.

   - Run:

        ``` shell
        ./install/installpy.ps1
        ```

        or

        ``` shell
        sh install/install.sh
        ```

        - This script downloads and installs the latest Python from python.org (including the `pip` package manager).
        - `install.sh` also installs GTK3 framework used for PDF output.
        - In Windows, UAC request may pop-up during the silent installation.

> [!NOTE]
> Python is not used in runtime, it is only used to build the static HTML site from the source .MD files.

1. Initialize Python virtual environment, an install MkDocs with dependencies:

    ``` shell
    ./install/deploymkdocs.ps1
    ```

    or

    ``` shell
    sh install/deploy.sh
    ```

## Build Help

1. Run:

    ``` shell
    ./buildhelp.ps1
    ```

    or

    ``` shell
    sh buildhelp.sh
    ```

   - This script runs `buildhelp.py` in the virtual environment and builds languages help to `compiled_help`.

   - The language list is set on the line 15 in `buildhelp.py`:

        `LANGUAGE_LIST = ["en", "ru"]`

2. You should see the newly compiled help subdirectories in the `compiled_help` directory:

   - en
   - ru

> [!NOTE]
>    * `buildhelp.py` will not run on it's own, instead execute `buildhelp.ps1` or `buildhelp.sh`.

## Build PDF Manual

1. Install GTK3: `installgtk3.ps1` or `apt install -y libgtk-3-dev`. 

    > [!NOTE]
    > In Windows, for GTK3 to work properly the PATH variable might need to be set (and put on top of the PATH list) to its installation directory.

2. Build the PDF manual:

    ``` shell
    mkdocs build -f mkdocs_ru_pdf.yml
    ```

## Serve Live Help Site

You can view the live MkDocs site without building it or compiling the product. The live server watches for changes in the `docs` folder and update accordingly.

Serve Russian docs locally at <http://127.0.0.1:8000>

1. Change dir to `Help` under the solution root directory.

2. Run:

    ``` shell
    ./install/deploymkdocs.ps1
    ```

    or

    ``` shell
    sh install/deploy.sh
    ```

    - This script deploys the Python virtual environment in `Help/venv` with MKDocs and its dependencies listed in the `requirements.txt` file. It does not build the help files.

3. Run:

    ``` shell
    mkdocs serve
    ```

    or  

    ``` shell
    py -m mkdocs serve
    ```

   - For English version run:

       ``` shell
       mkdocs serve -f mkdocs_en_local.yml

       ```

> [!NOTE]
>  * The help is not build by `mkdocs serve`, it is only served locally to <http://127.0.0.1:8000>
>  * The server watches for edits in the `Help\docs` directory and updates the help on the fly. Any edits you make in the `docs` directory will be immediately reflected at <http://127.0.0.1:8000>

## Build files to import into PHPKB

The files will be compiled to the `for_kb_import_ru` or `for_kb_import_en` folder.

The `kb_html_cleanup_hook.py` does all the magic.

``` shell
mkdocs build -f mkdocs_for_kb_import_ru.yml
```

or

``` shell
mkdocs build -f mkdocs_for_kb_import_en.yml
```

## Uninstall MkDocs

- `install\uninstallmkdocs.ps1` — uninstalls installs all MKDocs dependencies listed in the `requirements.txt` config file.

- `install\uninstallpy.ps1` — silently uninstalls Python, runs a single command: `.\python_latest.exe /uninstall /quiet`

**The help is powered by the very popular and well-maintained MkDocs framework:**
<https://squidfunk.github.io/mkdocs-material/>
<https://github.com/squidfunk/mkdocs-material>
<https://www.mkdocs.org/>

## Customize navigation

If awesome-pages plugin is enabled you can selectively enable only certain documentation folders in the mkdocs.yml, for instance:

```
nav:
  - ... | administration/**
  - ... | using_the_system/**
```
