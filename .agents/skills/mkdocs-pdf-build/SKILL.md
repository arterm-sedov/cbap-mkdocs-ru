---
name: mkdocs-pdf-build
description: "Install GTK3 runtime and build PDF guides with mkdocs-with-pdf / WeasyPrint on Windows. Use when `import weasyprint` fails with `OSError: cannot load library`, when the user asks to build a PDF guide, when PDF output is 0-byte or silently drops pages, or when mkdocs builds succeed but the PDF renderer fails. Load `python-env-setup` first if the venv itself is broken."
license: MIT
metadata:
  source: hand-discovered
  applies_to: cbap-mkdocs-ru
---

# PDF build with WeasyPrint / GTK3 (cbap-mkdocs-ru)

Prerequisite: the venv is healthy and all plugins import. If not, load the
`python-env-setup` skill first.

## 1. GTK3 runtime for WeasyPrint (Windows)

`mkdocs-with-pdf` uses WeasyPrint to render PDFs. WeasyPrint needs GTK3 DLLs
on `PATH` and in `WEASYPRINT_DLL_DIRECTORIES`.

### Install GTK3 (one-time, manual)

The repo ships `install\installgtk3.ps1` which calls the tschoonj NSIS
installer. NSIS installers are interactive — they show a UI. For one-off
runs, install GTK3 by hand: launch `install\gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe`
and click Next.

The installer drops files at:

```
C:\Program Files\GTK3-Runtime Win64\bin\
```

(Not `C:\Program Files\GTK3\` — that's a different distribution.)

### Persist env vars to user scope (one-time, after install)

```powershell
[Environment]::SetEnvironmentVariable(
  "WEASYPRINT_DLL_DIRECTORIES",
  "C:\Program Files\GTK3-Runtime Win64\bin",
  "User")

$gtkPath = "C:\Program Files\GTK3-Runtime Win64\bin"
$current = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($current -notlike "*GTK3-Runtime Win64\bin*") {
  [Environment]::SetEnvironmentVariable("PATH", "$gtkPath;$current", "User")
}
```

### Per-shell override (for CI or one-off runs)

```powershell
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
.\.venv\Scripts\python.exe -c "import weasyprint; print(weasyprint.__version__)"
```

`weasyprint 68.1` should print cleanly. The only stderr noise you should
see is a `GLib-GIO-WARNING` about a UWP app (`Microsoft.OutlookForWindows`)
— that is harmless and not from WeasyPrint.

## 2. Build a PDF guide

After GTK3 is set up:

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe -m mkdocs build `
  -f mkdocs_guide_api_ru_pdf.yml `
  --clean
```

Available PDF configs (`mkdocs_guide_*_pdf.yml`):

| Config                                      | Output PDF                                      |
| ------------------------------------------- | ----------------------------------------------- |
| `mkdocs_guide_api_ru_pdf.yml`               | API guide                                       |
| `mkdocs_guide_user_ru_pdf.yml`              | User guide                                      |
| `mkdocs_guide_admin_windows_ru_pdf.yml`     | Admin guide (Windows)                           |
| `mkdocs_guide_admin_linux_ru_pdf.yml`       | Admin guide (Linux)                             |
| `mkdocs_guide_developer_ru_pdf.yml`         | Developer guide                                 |
| `mkdocs_guide_ai_ru_pdf.yml`                | AI guide                                        |
| `mkdocs_guide_complete_ru_pdf.yml`          | Complete guide                                  |
| `mkdocs_guide_user_ru_pdf_gostech.yml`      | User guide (ГосТех)                             |
| `mkdocs_guide_api_ru_pdf_gostech.yml`       | API guide (ГосТех)                              |
| `mkdocs_guide_admin_linux_ru_pdf_gostech.yml` | Admin guide Linux (ГосТех)                    |

The PDF lands in the **repo root**, not in `pdf/`, because `output_path` is
relative to `site_dir: pdf/` in each config (e.g., `output_path: ../Comindware Platform 6.0. Руководство по использованию API.pdf`).

### Known non-fatal warnings (safe to ignore)

- `mkdocs_autorefs: Could not find cross-reference target 'release_notes_6.0'`
- `release_notes_6.0.md is included in the 'nav' configuration, but this file is excluded from the built site.`
- `GLib-GIO-WARNING ... Microsoft.OutlookForWindows ... supports 4 extensions but has no verbs`
- `WARNING - MkDocs 2.0 is incompatible with Material for MkDocs` (upstream notice from Material 9.7.x)

## 3. Quick triage

| Symptom                                                      | First check                                                             |
| ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| `import weasyprint` → `OSError: cannot load library`         | Section 1: GTK3 not on PATH or `WEASYPRINT_DLL_DIRECTORIES` not set    |
| `mkdocs build` produces 0-byte PDF / silently drops pages    | GTK3 missing → WeasyPrint crashes mid-render; check Section 1           |
| PDF text shows boxes/glyphs for Cyrillic                     | WeasyPrint not finding system fonts — `WEASYPRINT_DLL_DIRECTORIES` set? |
| `pip --version` shows `python-portable`                      | Not a PDF problem — load `python-env-setup` skill                       |
| Any `ModuleNotFoundError` for mkdocs plugins                 | Not a PDF problem — load `python-env-setup` skill                       |
