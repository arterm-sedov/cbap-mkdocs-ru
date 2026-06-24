---
name: generate-pdf-from-source
description: |
  Generate styled Comindware PDFs from external source documents.
  Two workflows: (A) structured data — Excel, CSV, JSON, XML → tables/reports;
  (B) document conversion — DOCX, plain text, HTML, existing Markdown → styled articles;
  multi-file nav supported. Trigger when the user asks to convert an external file into a PDF with Comindware branding,
  or says "make a PDF", "convert to PDF", "generate a styled document/report".
  Uses the cbap-mkdocs-ru pipeline: mkdocs-with-pdf, GTK3, pdf_templates, overrides.
---

# Generate PDF from External Source

Two workflows for converting external files into Comindware-styled PDFs via the mkdocs-with-pdf pipeline.

## When to use this skill

Trigger when the user:
- Provides an Excel/CSV/JSON file and asks for a formatted PDF report
- Provides a DOCX/text/HTML file and asks to convert it to a styled PDF
- Has existing `.md` in an external repo (web + print) and needs a PDF build config
- Says "make a PDF from this file", "convert to PDF", "generate a styled document"

Do NOT use for:
- Building existing mkdocs articles as PDF → use `mkdocs-pdf-build`
- Generating PDFs from the PHPKB knowledge base → use `phpkb-ingestion`

## Pre-flight checklist (always ask before generating)

1. **Source file path** — where is the input file?
2. **Document title** — title / subtitle for the cover page.
3. **Language** — Russian or English.
4. **Output location** — where to place the resulting PDF? Default: next to source.
5. **Logo** — use default Comindware logo or ask for custom path.
6. **Restructure text?** (DOCX/text only) — if unstructured, offer to restructure into sections.

---

## Workflow A — Structured data (Excel, CSV, JSON, XML)

### A1. Parse the source file

Use pandas (Excel/CSV), the `json` module (JSON), or appropriate library. Understand the data structure:

- Header rows, hierarchical markers (section/subsection/scenario labels)
- Column meanings
- Merged cells (in Excel) — use `pd.read_excel(header=None)` and manual detection

### A2. Table handling strategy

Source files often produce wide tables. The pipeline defaults to **A4 portrait**. For tables with 5+ columns, ask the user:

| Strategy | Best for | Page size |
|---|---|---|
| **Landscape** | 5–10 narrow/medium columns | A4 landscape |
| **Split tables** | 8+ columns with distinct semantic groups | A4 portrait |
| **Numbered lists** | Hierarchical step-by-step data | A4 portrait |
| **Mixed hybrid** | Some wide, some narrow sections | Mixed (CSS per-section) |

#### Landscape orientation

```html
<style>
@media print {
  @page { size: A4 landscape; }
}
</style>
```

Place right after frontmatter, before any content.

#### Split tables

Break one wide 8-column table into two 4-column tables with a shared key column.

#### Numbered lists

Convert table rows into hierarchical markdown with bold labels:

```markdown
#### Step 1: Create document
**Role:** System
**Input data:** Required fields...
**Expected result:** Document created.
```

### A3. Generate Markdown

Output a `.md` file with frontmatter, anchors, and tables:

```markdown
---
title: <Document Title>
tags: [tag1, tag2]
hide: tags
---

# <H1 Title> {: #anchor }

## <H2 Section> {: #anchor_section }

| Col1 | Col2 | Col3 |
|---|---|---|
| data | data | data |
```

Rules:
- Always include frontmatter with `tags` and `hide: tags`
- Generate English semantic anchors: `{: #anchor_name }`
- Use `&nbsp;` for empty table cells
- Escape `|` in cell content: `\|`
- Replace newlines with `<br>` for inline table content
- For long **single-file** sources (`heading_shift: false` inherited): use `#` chapters, `{: .pageBreakBefore }` on major sections; orphan H2-only docs break TOC/running headers in PDF

### A4. Generate build artifacts

Create a reproducible generation script (`build_<name>.py`) in `.scratch/` that reads the source and outputs the markdown.

---

## Workflow B — Document conversion (DOCX, text, HTML)

### B1. Convert source to Markdown

For DOCX files:

1. Install `python-docx` in the venv if not present:
   ```powershell
   .\.venv\Scripts\python.exe -m pip install python-docx
   ```

2. Write a conversion script (`.scratch/convert_docx_to_md.py`) that:
   - Reads paragraphs, preserves bold/italic/underline formatting
   - Extracts images to `docs/img/` (relative to the markdown)
   - Detects list paragraphs (`style.name == "List Paragraph"`) → `- item`
   - Detects headings (bold + font size ≥ 14pt) → `## Heading`
   - Wraps images in italic for auto-figcaption: `_![Alt text](img/imageN.png)_`
   - Writes frontmatter with `title`, `tags`, `hide: tags`

3. Run the script from the repo root:
   ```powershell
   .\.venv\Scripts\python.exe .scratch/convert_docx_to_md.py
   ```

### B2. Restructure the document (if needed)

If the source text is unstructured:

1. Break into logical sections with `##` and `###` headings.
2. Remove manual numbering — the plugin auto-numbers via `ordered_chapter_level: 3`.
3. Rephrase informal language into business style.
4. Remove dead hyperlinks (internal instance URLs).
5. Add a summary/recommendations section at the end.

### B3. Format the Markdown article

#### Headings

```markdown
# Document Title {: #anchor_name }

## Section Name {: #anchor_name_section }
```

- Do NOT include manual numbering (1., 1.1, 2.1, etc.) — plugin adds it automatically.
- Use concise semantic anchors in English with H1 anchor as prefix.

#### Images with auto-figcaption

Wrap in underscores (italic). `mkdocs-em-img2fig-plugin` generates `<figure>` + `<figcaption>` from alt text:

```markdown
_![Description of what the image shows](img/image1.png)_
```

- Do NOT add manual `*Рис. N.*` lines.
- Alt text should be descriptive, in the document language.

#### Lists, code blocks, tables

Standard Markdown. Separate nested lists with blank line. Label code fences with language.

#### References section

Add at the end. Use KB article IDs:

```markdown
## Ссылки на материалы {: #references }

### Category

- [Article title](https://kb.comindware.ru/article.php?id=XXXX)
```

Find `kbId:` in article frontmatter under `docs/ru/`.

---

## Common steps (both workflows)

### Create the target folder structure

```
<folder_name>/
├── build.ps1                    # Build script
├── mkdocs.yml                   # MkDocs config
├── docs/                        # docs_dir
│   ├── <article>.md             # Main markdown file
│   └── img/                     # Images (workflow B)
├── .site/                       # site_dir (build output, gitignored)
└── <Output>.pdf                 # Final PDF
```

Ask the user where to create this folder. Common locations:
- Next to the source document
- In `.scratch/` of the repo (for temporary outputs)

**Layout variant — existing Markdown in external repo:** put `mkdocs.yml` + `build.ps1` in a `pdf/` subfolder (MkDocs rejects config inside `docs_dir`). Point `docs_dir` at the parent of source `.md`; use `exclude_docs` to select file(s). Put `site_dir` in consumer repo `.scratch/<project>/.site` (gitignored). Never copy `pdf_templates/` locally — set `MKDOCS_PDF_TEMPLATES` to cbap-mkdocs-ru's `pdf_templates/`. Resolve cbap via `CBAP_MKDOCS_ROOT` → sibling checkout → vendored `.reference-repos/` copy.

### Write the MkDocs config

Create `mkdocs.yml` in the target folder:

```yaml
INHERIT: !ENV [MKDOCS_COMMON, <relative_path_to_cbap>/mkdocs_common.yml]

use_directory_urls: false

site_name: "<Document title>"
site_description: "<Brief description>"
docs_dir: docs
site_dir: .site
site_url: ''

theme:
  name: material
  language: ru
  custom_dir: !ENV [MKDOCS_OVERRIDES, <relative_path_to_cbap>/overrides]

extra:
  pdfOutput: true
  pdf:
    copyright: © Comindware, 2009–2026
    frontpage:
      logo: assets/images/comindware_logo.svg
      headerRight: comindware.ru
      title: <Cover page title>
      subtitle: <Cover page subtitle>
      footerLeft: !ENV [MKDOCS_PDF_FOOTER_LEFT, "<static fallback>"]  # format per project; build script sets env
    pageFooter:
      left: ''

copyright: '<a href="https://www.comindware.ru/" target="_blank">© 2009–2026 Comindware<sup>®</sup></a>'  # site/HTML; PDF uses extra.pdf.copyright — harmless if unused

nav:
  - '<Navigation title>': <article>.md

markdown_extensions:
  toc:
    title: На этой странице
    permalink_title: Скопируйте адрес этой ссылки, чтобы поделиться параграфом
  pymdownx.snippets:
    base_path: !ENV [MKDOCS_SNIPPETS, <relative_path_to_cbap>/docs/ru/.snippets/]

plugins:
  minify:
    minify_html: false
  glightbox:
    manual: true
  with-pdf:
    cover: true
    toc_title: Оглавление
    toc_level: 3
    custom_template_path: !ENV [MKDOCS_PDF_TEMPLATES, <relative_path_to_cbap>/pdf_templates]
    output_path: !ENV ['MKDOCS_PDF_OUTPUT_FILENAME', '../<Output filename>.pdf']
    enabled_if_env: ''

exclude_docs: |
  *.md
  !<article>.md
```

**Key settings:**
- `INHERIT` — always use `!ENV` with relative fallback to `mkdocs_common.yml`.
- `custom_dir` — `overrides/` in cbap-mkdocs-ru (extra.css, logo, templates).
- `custom_template_path` — `pdf_templates/` (cover.html.j2, styles.scss).
- `ordered_chapter_level: 3` — inherited, auto-numbers H1–H3.
- `exclude_docs` — exclude all `*.md` except the target article.
- `output_path` — relative to `site_dir`; use `../` to place PDF in folder root.
- `site_dir` must NOT be inside `docs_dir` (MkDocs validation error).
- **Cover static fields** (`title`, `subtitle`, `logo`, `headerRight`, `extra.pdf.copyright`) in YAML; **dynamic** `footerLeft` and dated `output_path` from build script via env.
- `footerLeft`: `MKDOCS_PDF_FOOTER_LEFT` — any string the project needs (date, author, edition); YAML fallback when env unset.

### Write the build script

Create `build.ps1` in the target folder:

```powershell
# Build <Document title> PDF
# Requires: cbap-mkdocs-ru venv (.venv), GTK3
# Usage: .\build.ps1

$scriptDir = Get-Item (Split-Path -Parent $MyInvocation.MyCommand.Definition)
$reposRoot = $scriptDir
for ($i = 0; $i -lt <N>; $i++) { $reposRoot = $reposRoot.Parent }
$cbapRoot = Join-Path $reposRoot.FullName "Documents\cbap-mkdocs-ru"

$env:MKDOCS_COMMON        = Join-Path $cbapRoot "mkdocs_common.yml"
$env:MKDOCS_OVERRIDES     = Join-Path $cbapRoot "overrides"
$env:MKDOCS_PDF_TEMPLATES = Join-Path $cbapRoot "pdf_templates"
$env:MKDOCS_SNIPPETS      = Join-Path $cbapRoot "docs\ru\.snippets/"
$venvPath                  = Join-Path $cbapRoot ".venv\Scripts\python.exe"
$dateStr                   = Get-Date -Format "yyyy.MM.dd"

$env:MKDOCS_PDF_FOOTER_LEFT = "<footer text>"   # e.g. publication date; project-specific
$env:MKDOCS_PDF_OUTPUT_FILENAME = "../<Document title>. $dateStr.pdf"

$configPath = Join-Path $scriptDir.FullName "mkdocs.yml"

Write-Host "Building <Document title> PDF..." -ForegroundColor Cyan
& $venvPath -m mkdocs build -f $configPath
Write-Host "PDF output: $env:MKDOCS_PDF_OUTPUT_FILENAME" -ForegroundColor Green
```

**Path navigation:**
- Loop count `<N>` depends on folder depth relative to user's home directory.
- `$env:MKDOCS_PDF_OUTPUT_FILENAME` uses `../` to place PDF one level up from `site_dir`.

### Build and verify

```powershell
cd <target_folder>
.\build.ps1
```

Verify:
- No errors or missing-image warnings in output
- PDF created at expected path, reasonable size
- Cover page: logo, title, subtitle, copyright
- Auto-numbered headings, auto figcaptions from alt
- Comindware styling: Arial, #3698D4, A4, page numbers
- References section with clickable KB links

---

## Styling reference

### What the pipeline provides automatically

| Feature | Source |
|---------|--------|
| Arial/Helvetica font | `pdf_templates/styles.scss` |
| Blue #3698D4 brand color | `pdf_templates/styles.scss` + `overrides/assets/stylesheets/extra.css` |
| A4 portrait, 20mm margins | `pdf_templates/styles.scss` |
| Cover page with logo | `pdf_templates/cover.html.j2` |
| Page numbers (N / total) | `pdf_templates/styles.scss` |
| Copyright footer | `pdf_templates/cover.html.j2` |
| Auto-numbering H1–H3 | `ordered_chapter_level: 3` in `mkdocs_common.yml` |
| Auto figcaptions from alt | `mkdocs-em-img2fig-plugin` — wrap image in `_![](...)_` |
| Running chapter header | `pdf_templates/styles.scss` — blue border, top-right |

### !ENV pattern reference

| Config key | Env var | Fallback | Purpose |
|---|---|---|---|
| `INHERIT` | `MKDOCS_COMMON` | `<rel>/mkdocs_common.yml` | Base config |
| `theme.custom_dir` | `MKDOCS_OVERRIDES` | `<rel>/overrides` | Theme overrides |
| `with-pdf.custom_template_path` | `MKDOCS_PDF_TEMPLATES` | `<rel>/pdf_templates` | Cover/page templates |
| `docs_dir` | `MKDOCS_DOCS_DIR` | `docs` or scratch path | Markdown root |
| `site_dir` | `MKDOCS_SITE_DIR` | `.site` or `.scratch/.../.site` | HTML scratch |
| `pymdownx.snippets.base_path` | `MKDOCS_SNIPPETS` | `<rel>/docs/ru/.snippets/` | Snippet includes |
| `pdf.frontpage.footerLeft` | `MKDOCS_PDF_FOOTER_LEFT` | Static string | Cover footer (format per project) |
| `with-pdf.output_path` | `MKDOCS_PDF_OUTPUT_FILENAME` | Relative to site_dir | Output PDF path |

`<rel>` = relative path from the config file's directory to cbap-mkdocs-ru.

---

## Requirements

- Python venv at `cbap-mkdocs-ru/.venv/` with `weasyprint`, `mkdocs`, `mkdocs-material`, `mkdocs-with-pdf`
- For workflow A: `pandas`, `openpyxl`
- For workflow B: `python-docx`
- **Windows:** GTK3 runtime; `WEASYPRINT_DLL_DIRECTORIES` and `PATH` must include GTK3 bin directory
- **Linux:** GTK3 available system-wide (no extra env vars needed for WeasyPrint)
- `git config core.longpaths true` globally (for repos with long Russian filenames)

## Files produced

| File | Location | Purpose |
|---|---|---|
| `<article>.md` | `target_folder/docs/` | Generated/source Markdown |
| `img/*.png` | `target_folder/docs/img/` | Extracted images (workflow B) |
| `<config>.yml` | `target_folder/` | MkDocs PDF build config |
| `build.ps1` | `target_folder/` | PowerShell build wrapper |
| `.site/` | `target_folder/` | Intermediate build output (gitignored) |
| `<output>.pdf` | `target_folder/` | Final PDF document |

Clean up `.site/` after successful build if not needed for debugging.

## Cross-platform build examples

### Sibling directories (no env vars needed)

When source and cbap-mkdocs-ru share a parent directory, the `!ENV` fallbacks resolve directly.

**Windows:**
```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f ..\<source_dir>\<config>.yml --clean
```

**Linux:**
```bash
.venv/bin/python -m mkdocs build -f ../<source_dir>/<config>.yml --clean
```

### External project (env vars required)

When cbap-mkdocs-ru is at an arbitrary location, set `!ENV` variables to absolute paths.

**Windows (PowerShell):**
```powershell
$cbapRoot = "<path\to\cbap-mkdocs-ru>"

$env:MKDOCS_COMMON       = "$cbapRoot\mkdocs_common.yml"
$env:MKDOCS_OVERRIDES    = "$cbapRoot\overrides"
$env:MKDOCS_PDF_TEMPLATES = "$cbapRoot\pdf_templates"
$env:MKDOCS_SNIPPETS     = "$cbapRoot\docs\ru\.snippets\"
$env:MKDOCS_PDF_FOOTER_LEFT = "<footer text>"

# GTK3 for WeasyPrint (Windows-only)
$gtkBin = "<GTK3 bin directory>"
if (Test-Path $gtkBin) {
    $env:WEASYPRINT_DLL_DIRECTORIES = $gtkBin
    $env:PATH = "$gtkBin;$env:PATH"
}

& "$cbapRoot\.venv\Scripts\python.exe" -m mkdocs build -f "$PSScriptRoot\<config>.yml" --clean
```

**Linux/macOS (bash/zsh):**
```bash
cbapRoot="<path/to/cbap-mkdocs-ru>"

export MKDOCS_COMMON="$cbapRoot/mkdocs_common.yml"
export MKDOCS_OVERRIDES="$cbapRoot/overrides"
export MKDOCS_PDF_TEMPLATES="$cbapRoot/pdf_templates"
export MKDOCS_SNIPPETS="$cbapRoot/docs/ru/.snippets/"

"$cbapRoot/.venv/bin/python" -m mkdocs build -f "$(dirname "$0")/<config>.yml" --clean
```

## Known issues

- **Long filenames on Windows:** `git config core.longpaths true` globally.
- **UnicodeEncodeError in PowerShell:** `$env:PYTHONIOENCODING = "utf-8"`, `$env:PYTHONUTF8 = "1"`.
- **GTK3 not found:** Ensure GTK3 `bin` is in PATH, `WEASYPRINT_DLL_DIRECTORIES` points to `lib/`.
- **`site_dir` inside `docs_dir`:** MkDocs validation error — must be in different directory trees.
- **`enabled_if_env` guard:** `mkdocs_common.yml` sets `enabled_if_env: PDF_OUTPUT`. Override with `enabled_if_env: ''` to unconditionally enable.
- **Table cell escaping:** Replace `|` with `\|` in cell content. Use `&nbsp;` for empty cells.
- **MkDocs working directory:** Run build from target folder root, reference config by path.
- **Config inside `docs_dir`:** use a `pdf/` subfolder for `mkdocs.yml` when source `.md` is in the parent folder.
- **Wrong cover:** inherited `productName`, missing logo, or HTML in footer — wrong/stale `MKDOCS_PDF_TEMPLATES`; do not fork local cover templates.
- **PDF file locked:** close open PDF before rebuild (WeasyPrint permission error).
- **MkDocs 2.0 warning:** Cosmetic only, does not affect output.
- **`faq.md` / `portal_index.md` warnings:** Root-level files in `docs/ru/`, not related to target. Safe to ignore.

---

## Cleanup

After building, `.site/` contains intermediate HTML and can be deleted. Files needed for re-build: `build.ps1`, `mkdocs.yml`, `docs/` (markdown + images).
