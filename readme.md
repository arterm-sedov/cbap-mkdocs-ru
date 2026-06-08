## AI-Enabled Repo

Chat with DeepWiki to get answers about the Comindware Plafrom from this repo:

[Ask DeepWiki](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

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

## Mermaid Diagram Support in PDF

PDF generation uses WeasyPrint which does not execute JavaScript, so Mermaid diagrams require pre-rendering to static images.

### Recommended Approach: `mkdocs-mermaid-to-svg` + `mmdc`

#### Dependencies

1. **Python package** (already in `install/requirements.txt`):
   ```
   pip install mkdocs-mermaid-to-svg
   ```

2. **Node.js** (required for `mmdc` — Mermaid CLI):
   - Install from https://nodejs.org/ or via package manager
   - Verify: `node --version` (tested with v18.20.7+)

3. **Mermaid CLI** (global npm package):
   ```
   npm install -g @mermaid-js/mermaid-cli
   ```
   - Verify: `mmdc --version` (tested with 11.12.0+)

#### Configuration

Add to your MkDocs YAML config:

```yaml
plugins:
  mermaid-to-svg:
    output_dir: _mermaid_assets
  with-pdf:
    # ... existing with-pdf config
```

#### How It Works

1. `mkdocs-mermaid-to-svg` scans markdown files for ` ```mermaid ` code blocks
2. Each diagram is rendered to SVG via `mmdc` (Node.js Mermaid CLI)
3. SVG files are saved to `_mermaid_assets/` directory
4. Original mermaid blocks are replaced with `<img>` tags pointing to SVGs
5. WeasyPrint includes the SVGs in the final PDF (vector quality, infinite scaling)

### Alternative: `render_js: true` (Does NOT Work)

The `with-pdf` plugin has a `render_js: true` option that attempts to use Headless Chrome to execute JavaScript before PDF generation. **This does not work** with current versions due to a bug in `mkdocs-with-pdf` v0.9.3:

```
AttributeError: property 'text' of 'Tag' object has no setter
```

The plugin (last updated 2021) is incompatible with newer BeautifulSoup versions. The `_render_js` method tries to set the read-only `.text` property of a BeautifulSoup `Tag` object.

**Conclusion:** Use `mkdocs-mermaid-to-svg` + `mmdc` — it's the only working approach for Mermaid in PDF.

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

On `platform_v6`, `mkdocs_for_kb_import_ru.yml` sets `site_url` to `https://kb.comindware.ru/platform/v6.0/` so exported HTML image paths match the V6 PHPKB web folder. Rebuild after doc changes:

``` shell
mkdocs build -f mkdocs_for_kb_import_ru.yml
```

Copy exported images into the PHPKB web asset tree when needed:

``` shell
python phpkb_copy_images.py
```

For English PHPKB export:

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

## Scratch Directory

The `.scratch/` folder is a shared space for temporary and disposable files: script outputs, debug logs, extracted data, and other transient artifacts.

- Contents are **git-ignored** — nothing inside `.scratch/` is tracked except `.gitkeep`.
- Use it for one-off scripts, analysis results, or any data that should not pollute the repository.
- Do not reference `.scratch/` files from documentation or production code.
