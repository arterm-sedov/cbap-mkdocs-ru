## AI-Enabled Repo

Chat with DeepWiki to get answers about the Comindware Platform from this repo:

[Ask DeepWiki](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

# MkDocs Knowledge Base — Workflows

This repository contains the MkDocs source for the **{{ productName }}** knowledge base.
Markdown articles live under `docs/ru/`, PHPKB HTML export goes to `for_kb_import_ru/`, and RAG bundles are generated for LLM ingestion.

## Environment Setup

The repo uses a Python virtual environment (`.venv`) for all builds and scripts.

```powershell
.\.venv\Scripts\python.exe -c "import mkdocs"  # smoke test
```

If the venv is broken, load the `python-env-setup` skill for the full playbook.

Dependencies are listed in `install/requirements.txt`.

## .env Configuration

Copy `.env.example` to `.env` and fill in the profile values. Required for PHPKB publish, image sync, and RAG ingestion workflows. See `.env.example` for the full variable list.

## Build PHPKB Import HTML

Converts Markdown articles to PHPKB-compatible HTML in `for_kb_import_ru/`:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

Verify the export changed:

```powershell
git diff --name-only for_kb_import_ru/
```

## Publish to PHPKB

Pushes local HTML back into the PHPKB database:

```powershell
# Extract kb-id from the generated HTML
Select-String -Path for_kb_import_ru\<path>.html -Pattern 'kb-id="(\d+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } | Select-Object -First 1

# Publish
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --article-id <kb-id> --yes
```

## Sync Images to PHPKB Assets Repo

Copies exported images into the PHPKB static assets repo and optionally commits/pushes:

```powershell
# Copy images only
.\.venv\Scripts\python.exe phpkb_copy_images.py

# Copy + auto-commit-push to PHPKB repo
.\.venv\Scripts\python.exe phpkb_copy_images.py --git

# Copy + commit-push + SSH pull on production
.\.venv\Scripts\python.exe phpkb_copy_images.py --git --pull
```

Requires `CMW_KB_REPO_PATH` and `CMW_SSH_*` in `.env`.

## RAG / LLM Ingestion

Refreshes the RAG corpus from PHPKB and builds a single-file LLM bundle:

```powershell
# Full refresh: pull from DB + bundle
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896
.\.venv\Scripts\python.exe phpkb_ingest.py

# Bundle only (when RAG corpus is already current)
.\.venv\Scripts\python.exe phpkb_ingest.py

# Bundle + git-sync to PHPKB repo + SSH pull on production
.\.venv\Scripts\python.exe phpkb_ingest.py --git --pull --no-ask
```

## Build PDF Guides

PDF output requires GTK3 installed. Load the `mkdocs-pdf-build` skill for the full Windows playbook.

```powershell
mkdocs build -f mkdocs_ru_pdf.yml
```

Dated copies (with `YYYY.MM.DD` suffix):

```powershell
.\.venv\Scripts\python.exe pdf_duplicate_with_date.py
```

## Live Preview

Serve the Russian docs locally at http://127.0.0.1:8000:

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve
```

English version:

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_en_local.yml
```

The server watches for edits in `docs/` and updates on the fly.

## Mermaid Diagram Support in PDF

PDF generation uses WeasyPrint which does not execute JavaScript, so Mermaid diagrams require pre-rendering to static images.

### Recommended Approach: `mkdocs-mermaid-to-svg` + `mmdc`

#### Dependencies

1. **Python package** (already in `install/requirements.txt`):
   ```
   pip install mkdocs-mermaid-to-svg
   ```

2. **Node.js** (required for `mmdc`):
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

1. `mkdocs-mermaid-to-svg` scans markdown files for mermaid code blocks
2. Each diagram is rendered to SVG via `mmdc`
3. SVG files are saved to `_mermaid_assets/`
4. Original mermaid blocks are replaced with `<img>` tags pointing to SVGs
5. WeasyPrint includes the SVGs in the final PDF

### Alternative: `render_js: true` (Does NOT Work)

The `with-pdf` plugin has a `render_js: true` option that attempts to use Headless Chrome. **This does not work** with current versions due to a bug in `mkdocs-with-pdf` v0.9.3:

```
AttributeError: property 'text' of 'Tag' object has no setter
```

**Conclusion:** Use `mkdocs-mermaid-to-svg` + `mmdc` — it's the only working approach for Mermaid in PDF.

## Agent Skills

This repo includes AI agent skills under `.agents/skills/`. They provide end-to-end workflows for common tasks:

| Skill | When to use |
|---|---|
| `kb-edit-publish` | Edit an article, rebuild HTML, publish to PHPKB, commit |
| `phpkb-ingestion` | Refresh RAG corpus from PHPKB, build LLM ingestion bundle |
| `mkdocs-pdf-build` | Install GTK3, build PDF guides on Windows |
| `phpkb-cloning` | Clone PHPKB categories/articles, sync IDs and links |
| `mkdocs_add_file` | Add an article to mkdocs YAML navigation |
| `cmwhelp-commit` | Format git commit messages |
| `self-evolution` | Document discoveries after non-trivial tasks |
| `python-env-setup` | Fix broken venv, verify mkdocs plugin imports |
| `generate-pdf-from-source` | Generate styled PDFs from Excel/CSV/JSON data |

Skills are auto-discovered by AI agents. Refer to individual `SKILL.md` files for detailed workflows.

## Customize Navigation

If awesome-pages plugin is enabled you can selectively enable only certain documentation folders in the mkdocs.yml:

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

## Legacy Files

Obsolete scripts and configs are archived in `.legacy/`. They are not used by the current workflows.
