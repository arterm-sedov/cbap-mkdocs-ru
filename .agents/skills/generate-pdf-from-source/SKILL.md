---
name: generate-pdf-from-source
description: Generate a styled PDF from Excel, CSV, JSON, Markdown, text, or other sources (one or many files) using the cbap-mkdocs-ru MkDocs/WeasyPrint pipeline. Use for datasets, existing .md docs, or multi-file report packs with Comindware KB styling.
---

# Generate PDF from external source files

## Overview

This skill covers the end-to-end workflow of reading data from an external structured file (Excel, CSV, JSON, etc.), generating a MkDocs-compatible Markdown document, wiring it into a YAML configuration, and building a styled PDF via the cbap-mkdocs-ru MkDocs + WeasyPrint pipeline.

The same pipeline applies to **existing Markdown** (no generation step) and **multi-file** builds (one `nav` entry per file). Plain text or Word sources: convert to `.md` first.

## Directory layout expectations

The workflow assumes this directory structure — two sibling directories, or an external project with a known relative path to cbap-mkdocs-ru:

```
<workspace>/
  cbap-mkdocs-ru/           # the docs/kb repo (this repo)
    .scratch/               # disposable temp files
    .venv/                  # Python venv with WeasyPrint
    mkdocs_common.yml
    overrides/
    pdf_templates/
  <source_dir>/             # user's project with source files
    source.xlsx             # the input file
    <config>.yml            # generated YAML config (next to source)
    build_<name>.ps1        # generated PS build script
    <output>.pdf            # final PDF
```

If the layout differs, the `!ENV` variables in the YAML config must be set to absolute paths by the build script (see Step 4).

### Existing Markdown in an external repo (Pattern B)

When source `.md` already lives in the consumer repo (web + print):

- Put `mkdocs.yml` + `build.ps1` in a **`pdf/` subfolder** — MkDocs rejects config inside `docs_dir`.
- `docs_dir`: parent folder of the source file(s); `exclude_docs` selects which `.md` to include.
- `site_dir`: consumer repo `.scratch/<project>/.site` (gitignored), **not** inside `docs_dir`.
- Cover title/subtitle/logo stay in YAML; build script sets only dynamic `footerLeft` and output filename (see below).

Never copy `pdf_templates/` into the consumer repo — set `MKDOCS_PDF_TEMPLATES` to cbap-mkdocs-ru's `pdf_templates/`.

## Pre-flight checklist (always ask before generating)

When a user asks to generate a PDF from an external file, ask these questions **before writing any code**:

1. **Document title** — Title / subtitle for the cover page.
2. **Language** — Russian or English.
3. **Table handling strategy** (see below).
4. **Output location** — Where to place the resulting PDF (default: next to source).

Do not proceed until the user has answered or explicitly told you to use defaults.

## Table handling strategies

Source files (especially Excel) often produce wide tables. The cbap-mkdocs-ru pipeline defaults to **A4 portrait**. For tables with 5+ columns or long cell content, ask the user to pick one of these strategies:

| Strategy | Best for | Document type | Page size |
|---|---|---|---|
| **Landscape** | 5–10 narrow/medium columns | Reference tables, test scenarios | A4 landscape |
| **Split tables** | 8+ columns with distinct semantic groups | Multi-perspective data | A4 portrait |
| **Numbered lists** | Hierarchical step-by-step data | Process descriptions | A4 portrait |
| **Mixed hybrid** | Some wide, some narrow sections | Complex reports | Mixed (CSS per-section) |

### Strategy examples

#### 1. Landscape orientation

Add a `<style>` block to the generated Markdown to override the default `@page` rule:

```html
<style>
@media print {
  @page { size: A4 landscape; }
}
</style>
```

The landscape override **must** appear before any content. Place it right after frontmatter.

#### 2. Split tables

Break one wide 8-column table into two 4-column tables with a shared key column:

```
Table A: № | Действие | Описание | Роль
Table B: № | Система | Данные ввода | Ожидаемый результат
```

Use a subsection heading to group them.

#### 3. Numbered lists

Convert table rows into hierarchical markdown with bold labels:

```markdown
#### Step 1: Create document
**Role:** System
**System:** RBT
**Input data:** Required fields...
**Expected result:** Document created.

#### Step 2: Approve
...
```

#### 4. Mixed hybrid

Use landscape only for sections with wide tables, portrait for others:

```html
<style>
@media print {
  @page { size: A4 portrait; }
  @page.wide { size: A4 landscape; }
}
</style>

<div class="wide">
<!-- wide table here -->
</div>
```

## Workflow

### Step 1: Parse the source file

Use pandas (Excel/CSV), the `json` module (JSON), or appropriate library. Understand the data structure:

- Header rows, hierarchical markers (section/subsection/scenario labels)
- Column meanings
- Merged cells (in Excel) — use `pd.read_excel(header=None)` and manual detection

### Step 2: Generate Markdown

Output a single `.md` file under `cbap-mkdocs-ru/.scratch/` with a reproducible generation script:

```
cbap-mkdocs-ru/.scratch/
  <document_slug>.md       # generated markdown
  build_<name>.py           # generation script (reproducible)
```

Markdown conventions (match existing KB articles):

```markdown
---
title: <Document Title>
tags:
  - tag1
  - tag2
hide: tags
---

<style>
@media print {
  @page { size: A4 landscape; }
}
</style>

# <H1 Title> {: #anchor }

## <H2 Section> {: #anchor_section }

| Col1 | Col2 | Col3 |
|---|---|---|
| ... | ... | ... |
```

Rules:
- Always include frontmatter with `tags` and `hide: tags`
- Generate English semantic anchors: `{: #anchor_name }`
- Use `&nbsp;` for empty table cells
- Escape `|` in cell content: `\|`
- Replace newlines with `<br>` for inline table content
- For long **single-file** sources (`heading_shift: false` inherited): use `#` chapters, `{: .pageBreakBefore }` on major sections; orphan H2-only docs break TOC/running headers in PDF

### Step 3: Create the YAML config

Store the YAML config **next to the source file** (not in cbap-mkdocs-ru). Use `!ENV` with relative `../cbap-mkdocs-ru/` fallback paths for all inherited resources:

```yaml
# Stored at: <source_dir>/<config>.yml
# Built from cbap-mkdocs-ru root:
#   .venv/Scripts/python.exe -m mkdocs build -f ../<source_dir>/<config>.yml --clean

INHERIT: !ENV [MKDOCS_COMMON, ../cbap-mkdocs-ru/mkdocs_common.yml]

site_name: <Title>
docs_dir: !ENV [MKDOCS_DOCS_DIR, ../cbap-mkdocs-ru/.scratch/]
site_dir: _pdf_out/
site_url: ''

theme:
  custom_dir: !ENV [MKDOCS_OVERRIDES, ../cbap-mkdocs-ru/overrides]

extra:
  pdfOutput: true
  pdf:
    copyright: © Comindware, 2009–2026
    frontpage:
      logo: assets/images/comindware_logo.svg
      headerRight: comindware.ru
      title: <Cover Title>
      subtitle: <Cover Subtitle>
      footerLeft: !ENV [MKDOCS_PDF_FOOTER_LEFT, "<static fallback>"]  # e.g. date, author, edition — or leave build script to set env
    pageFooter:
      left: ''

copyright: '<a href="https://www.comindware.ru/" target="_blank">© 2009–2026 Comindware<sup>®</sup></a>'  # site/HTML footer; PDF uses extra.pdf.copyright above — harmless if unused

nav:
  - <Nav Title>: <filename>.md

markdown_extensions:
  toc:
    title: На этой странице
  pymdownx.snippets:
    base_path: !ENV [MKDOCS_SNIPPETS, ../cbap-mkdocs-ru/docs/ru/.snippets/]

plugins:
  minify:
    minify_html: false
  glightbox:
    manual: true
  with-pdf:
    cover: true
    toc_title: Оглавление
    toc_level: 3
    custom_template_path: !ENV [MKDOCS_PDF_TEMPLATES, ../cbap-mkdocs-ru/pdf_templates]
    output_path: !ENV ['MKDOCS_PDF_OUTPUT', ../<OutputName>.pdf]
    enabled_if_env: ''

exclude_docs: |
  *.md
  !<filename>.md
```

Key points:
- The `../cbap-mkdocs-ru/` fallback path assumes the source directory is a **sibling** of cbap-mkdocs-ru. Adjust the fallback to match the actual relative path from the config to cbap-mkdocs-ru.
- Config stored **next to source files**, PDF output goes to the same directory
- `site_dir: _pdf_out/` is relative to config directory — clean up after build
- `site_dir` must NOT be inside `docs_dir` (MkDocs validation error)
- `output_path: ../<Name>.pdf` — goes up from site_dir to the source directory
- `enabled_if_env: ''` — always enable PDF output (override inherited `PDF_OUTPUT` guard)
- **Cover static fields** (`title`, `subtitle`, `logo`, `headerRight`, `extra.pdf.copyright`) belong in YAML. **Only** dynamic `footerLeft` and `output_path` (often dated) come from the build script via env.
- `extra.pdf.copyright` is plain text for PDF footers. Top-level `copyright` (HTML) is for MkDocs HTML/site output only — optional in PDF-only configs; does no harm if present.
- `footerLeft`: build script sets `MKDOCS_PDF_FOOTER_LEFT` to whatever string the project needs (publication date, author + date, edition label, etc.). YAML fallback is static text when env is unset. Project-specific `.env` keys are fine — no fixed format required.

### Step 4: Build the PDF

Build runs from **cbap-mkdocs-ru root**. The config file lives next to the source, referenced by its path.

#### Sibling directories (no env vars needed)

When source and cbap-mkdocs-ru share a parent directory, the `!ENV` fallbacks resolve directly:

**Windows:**
```powershell
$env:WEASYPRINT_DLL_DIRECTORIES = "<GTK3 bin>"
$env:PATH = "<GTK3 bin>;$env:PATH"
.\.venv\Scripts\python.exe -m mkdocs build -f ../<source_dir>/<config>.yml --clean
```

**Linux:**
```bash
.venv/bin/python -m mkdocs build -f ../<source_dir>/<config>.yml --clean
```

#### External project (env vars required)

When cbap-mkdocs-ru is at an arbitrary location, set `!ENV` variables to absolute paths:

**Windows (PowerShell):**
```powershell
$cbapRoot = <path\to\cbap-mkdocs-ru>

$env:MKDOCS_COMMON       = "$cbapRoot\mkdocs_common.yml"
$env:MKDOCS_OVERRIDES    = "$cbapRoot\overrides"
$env:MKDOCS_PDF_TEMPLATES = "$cbapRoot\pdf_templates"
$env:MKDOCS_SNIPPETS     = "$cbapRoot\docs\ru\.snippets\"
$env:MKDOCS_DOCS_DIR     = "$cbapRoot\.scratch\"
# Pattern B: set MKDOCS_DOCS_DIR and MKDOCS_SITE_DIR to absolute consumer-repo paths
$env:MKDOCS_PDF_FOOTER_LEFT = "<footer text>"   # e.g. "Опубликовано $(Get-Date -Format 'dd.MM.yyyy')"
$env:MKDOCS_PDF_OUTPUT   = "$PSScriptRoot\<OutputName>.pdf"

# GTK3 for WeasyPrint (Windows-only; system-dependent path)
$gtkBin = "<GTK3 bin directory>"
if (Test-Path $gtkBin) {
    $env:WEASYPRINT_DLL_DIRECTORIES = $gtkBin
    $env:PATH = "$gtkBin;$env:PATH"
}

& "$cbapRoot\.venv\Scripts\python.exe" -m mkdocs build -f "$PSScriptRoot\<config>.yml" --clean
```

**Linux/macOS (bash/zsh):**
```bash
cbapRoot=<path/to/cbap-mkdocs-ru>

export MKDOCS_COMMON="$cbapRoot/mkdocs_common.yml"
export MKDOCS_OVERRIDES="$cbapRoot/overrides"
export MKDOCS_PDF_TEMPLATES="$cbapRoot/pdf_templates"
export MKDOCS_SNIPPETS="$cbapRoot/docs/ru/.snippets/"
export MKDOCS_DOCS_DIR="$cbapRoot/.scratch/"
export MKDOCS_PDF_FOOTER_LEFT="<footer text>"
export MKDOCS_PDF_OUTPUT="$(dirname "$0")/<OutputName>.pdf"

# GTK3 is typically available system-wide on Linux; no extra env vars needed

"$cbapRoot/.venv/bin/python" -m mkdocs build -f "$(dirname "$0")/<config>.yml" --clean
```

### Step 5: Verify

- Check page count: `from pypdf import PdfReader; len(PdfReader(pdf).pages)`
- Verify the cover page rendered correctly (title, subtitle, logo)
- Verify tables are not truncated (page breaks inside rows)
- Check that all expected sections/scenarios are present

## !ENV pattern reference

The `!ENV` YAML tag resolves to an environment variable value, falling back to a literal string if the variable is not set.

| Config key | Env var | Fallback | Purpose |
|---|---|---|---|
| `INHERIT` | `MKDOCS_COMMON` | `<rel>/cbap-mkdocs-ru/mkdocs_common.yml` | Path to base config |
| `theme.custom_dir` | `MKDOCS_OVERRIDES` | `<rel>/cbap-mkdocs-ru/overrides` | Material theme overrides |
| `with-pdf.custom_template_path` | `MKDOCS_PDF_TEMPLATES` | `<rel>/cbap-mkdocs-ru/pdf_templates` | Cover/page templates |
| `docs_dir` | `MKDOCS_DOCS_DIR` | `<rel>/cbap-mkdocs-ru/.scratch/` | Markdown root |
| `site_dir` | `MKDOCS_SITE_DIR` | `_pdf_out/` or `.scratch/.../.site` | HTML scratch (Pattern B) |
| `pymdownx.snippets.base_path` | `MKDOCS_SNIPPETS` | `<rel>/cbap-mkdocs-ru/docs/ru/.snippets/` | Snippet includes |
| `pdf.frontpage.footerLeft` | `MKDOCS_PDF_FOOTER_LEFT` | Static string | Cover footer (format chosen per project in build script) |
| `with-pdf.output_path` | `MKDOCS_PDF_OUTPUT` | `<relative to site_dir>` | Output PDF path |

The `<rel>` prefix is the relative path from the config file's directory to cbap-mkdocs-ru (e.g., `../cbap-mkdocs-ru/` when they are siblings). When env vars are set, they take precedence over the fallbacks — this is how external projects with different layouts work.

## Requirements

- Python venv at `cbap-mkdocs-ru/.venv/` with `weasyprint`, `mkdocs`, `mkdocs-material`, `mkdocs-with-pdf`, `pandas`, `openpyxl`
- **Windows:** GTK3 runtime (typically `C:\Program Files\GTK3-Runtime Win64\bin\`); `WEASYPRINT_DLL_DIRECTORIES` and `PATH` must include the GTK3 bin directory
- **Linux:** GTK3 available system-wide (no extra env vars needed for WeasyPrint)
- Build commands run from `cbap-mkdocs-ru/` root

## Files produced

| File | Location | Purpose |
|---|---|---|
| `<slug>.md` | `cbap-mkdocs-ru/.scratch/` | Generated Markdown from source data |
| `<config>.yml` | **Next to source file** | MkDocs PDF build config |
| `build_<name>.py` | `cbap-mkdocs-ru/.scratch/` | Reproducible generation script |
| `build_<name>.ps1` | **Next to source file** | PowerShell build wrapper |
| `<output>.pdf` | **Next to source file** | Final PDF document |

All intermediate build artifacts (`_pdf_out/`, `_pmi_pdf/`) must be cleaned up after a successful build.

## Common pitfalls

1. **`site_dir` inside `docs_dir`** — MkDocs errors with "The 'site_dir' should not be within the 'docs_dir'". `site_dir` and `docs_dir` must be in different directory trees. Since `docs_dir` points to `cbap-mkdocs-ru/.scratch/`, the `site_dir` lives next to the config (which is outside cbap-mkdocs-ru).
2. **`INHERIT` path resolution** — MkDocs resolves `INHERIT` relative to the *config file's directory*. This is why the config stays next to source and uses `../cbap-mkdocs-ru/` fallbacks — MkDocs walks up from source dir to the parent, then into cbap-mkdocs-ru.
3. **`enabled_if_env` guard** — `mkdocs_common.yml` sets `enabled_if_env: PDF_OUTPUT`. Override with `enabled_if_env: ''` to unconditionally enable PDF output.
4. **Table cell escaping** — Pipe characters `|` in cell content break Markdown tables. Always replace with `\|`.
5. **Empty cells collapse** — Empty table cells cause rendering issues. Always use `&nbsp;` as placeholder.
6. **MkDocs working directory** — Use cbap-mkdocs-ru's venv Python. Sibling builds may run from cbap root; external projects often `cd` to the config dir and pass `-f mkdocs.yml`. Both work if env paths are set.
7. **Config inside `docs_dir`** — Put config in a `pdf/` subfolder when source `.md` lives in the parent folder.
8. **Wrong cover** — Title shows inherited `productName`/`productVersion`, missing logo, or HTML in footer: wrong/stale `MKDOCS_PDF_TEMPLATES` path. Resolve cbap via `CBAP_MKDOCS_ROOT` → sibling checkout → vendored `.reference-repos/` copy (prefer newest). Do not fork local cover templates.
9. **PDF file locked** — Close open PDF before rebuild (WeasyPrint permission error).
