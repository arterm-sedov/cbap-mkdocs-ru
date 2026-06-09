---
name: python-env-pdf-build
description: Set up, verify, and use the cbap-mkdocs-ru Python virtual environment and the WeasyPrint/GTK3 PDF toolchain on Windows. Use when the venv appears broken, when `pip --version` reports a non-venv interpreter, when `import weasyprint` fails, when pip install from PyPI is slow or blocked, or when the user asks to build a PDF guide and the build silently drops pages.
license: MIT
compatibility: opencode
metadata:
  source: hand-discovered
  applies_to: cbap-mkdocs-ru (Comindware Platform help)
---

# Python env & PDF build on Windows (cbap-mkdocs-ru)

Lessons learned the hard way. Each section is a self-contained recipe.

## 1. Detect portable-Python pollution

The repo's venv (`.venv`) lives in this workspace. On this machine the user
environment also points at a portable interpreter:

- `PYTHONPATH=C:\Users\yboi\python-portable;…`
- `PYTHON_HOME=C:\Users\yboi\python-portable`

When those are set, every Python process (including the venv) has
`C:\Users\yboi\python-portable\Lib\site-packages` prepended to `sys.path`,
**and** `pip --version` reports the portable interpreter.

Sanity check before doing anything else (run from repo root):

```powershell
.\.venv\Scripts\python.exe -m pip --version
# EXPECTED: "from D:\RepOS\cbap-mkdocs-ru\.venv\Lib\site-packages\pip\__init__.py"
# BAD:      "from C:\Users\yboi\python-portable\Lib\site-packages\pip\__init__.py"
```

If the bad path appears, the venv is being polluted. Do **not** try to unset
the env vars in this session only — they will come back in a new shell.
Fix the actual root cause with a `pip.ini` (next section).

## 2. Pin pip to the venv with `.venv\pip.ini`

`pip.ini` placed inside the venv has the highest config priority in pip and
is honoured regardless of `PYTHONPATH`/`PYTHON_HOME`. It also gives you a
mirror that survives PyPI being throttled or blocked from RU IPs.

Create `.venv\pip.ini`:

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
extra-index-url =
    https://pypi.org/simple
    https://mirrors.aliyun.com/pypi/simple
trusted-host =
    pypi.tuna.tsinghua.edu.cn
    pypi.org
    mirrors.aliyun.com
timeout = 60
```

Verify:

```powershell
.\.venv\Scripts\python.exe -m pip config list
# EXPECTED: lists the three index-urls and trusted-hosts above
```

Re-check `pip --version` — it should now report the venv location.

## 3. Mirror strategy for installs in this repo

Always use the venv's `pip.ini`, never pass `-i` flags ad hoc. The dry-run
test is cheap and tells you reachability before you commit to a long install:

```powershell
.\.venv\Scripts\python.exe -m pip install --dry-run -r install\requirements.txt
```

If a package can't be resolved, the order in the `pip.ini` is
**Tsinghua → PyPI → Aliyun**. Tsinghua has the most complete mirror; Aliyun
is the safety net if Tsinghua is missing a brand-new release.

## 4. GTK3 runtime for WeasyPrint (Windows)

`mkdocs-with-pdf` uses WeasyPrint to render PDFs. WeasyPrint needs GTK3 DLLs
on `PATH` and in `WEASYPRINT_DLL_DIRECTORIES`.

### Why the repo script is not enough for headless CI

`install\installgtk3.ps1` calls the tschoonj NSIS installer with **no
flags**. NSIS installers are interactive — they show a UI. The script works
when a human clicks through, but it does not work unattended. For one-off
runs, install GTK3 by hand (the recommended way in this repo): launch
`install\gtk3-runtime-3.24.29-2021-04-29-ts-win64.exe` and click Next.
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

### Per-shell override (for one-off runs, e.g. CI)

```powershell
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
.\.venv\Scripts\python.exe -c "import weasyprint; print(weasyprint.__version__)"
```

`weasyprint 68.1` should print cleanly. The only stderr noise you should
see is a `GLib-GIO-WARNING` about a UWP app (`Microsoft.OutlookForWindows`)
— that is harmless and not from WeasyPrint.

## 5. Verify all 13 mkdocs plugins before building anything

Naive smoke tests (`for p in mkdocs_*.dist-info: import p`) **fail** for
this repo because two plugins have non-standard import names:

| Distribution name (pip)              | Real import          |
| ------------------------------------ | -------------------- |
| `mkdocs-em-img2fig-plugin` 0.3.3     | `import src`         |
| `mkdocs-htmlproofer-plugin` 1.4.1    | `import htmlproofer` |
| `mkdocs-material` 9.7.2              | `import material`    |
| everything else                      | `import <name>`      |

The em-img2fig quirk: its `top_level.txt` ships as `src`, so the package
lives at `.venv\Lib\site-packages\src\__init__.py` and re-exports
`Image2FigurePlugin`. There is no `mkdocs_em_img2fig_plugin` directory.
Don't waste time looking for one.

Reliable verification one-liner:

```powershell
.\.venv\Scripts\python.exe -c "import material, mkdocs_include_markdown_plugin, mkdocs_macros, mkdocs_with_pdf, mkdocs_glightbox, htmlproofer, mkdocs_mermaid_to_svg, mkdocs_section_index, mkdocs_minify_plugin, mkdocs_awesome_pages_plugin, mkdocs_autorefs, mkdocs_autolinks_plugin, src, weasyprint; print('all OK')"
```

And to confirm mkdocs itself can load the project's config:

```powershell
.\.venv\Scripts\python.exe -c "from mkdocs.config import load_config; cfg = load_config('mkdocs.yml'); print(cfg['site_name']); print(len(cfg['plugins']), 'plugins registered')"
```

## 6. Build a PDF guide

After sections 1-5 pass:

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe -m mkdocs build `
  -f mkdocs_guide_api_ru_pdf.yml `
  --clean
```

Known non-fatal warnings during this build (safe to ignore):

- `mkdocs_autorefs: Could not find cross-reference target 'release_notes_6.0'`
- `release_notes_6.0.md is included in the 'nav' configuration, but this file is excluded from the built site.`
- `GLib-GIO-WARNING ... Microsoft.OutlookForWindows ... supports 4 extensions but has no verbs`
- `WARNING - MkDocs 2.0 is incompatible with Material for MkDocs` (upstream notice from Material 9.7.x)

The PDF lands in the **repo root**, not in `pdf/`, because
`output_path: ../Comindware Platform 6.0. Руководство по использованию API.pdf`
is relative to `site_dir: pdf/`.

## 7. Quick triage flowchart

| Symptom                                                         | First check                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `pip --version` shows `python-portable`                         | Section 2: missing/broken `.venv\pip.ini`                                |
| `pip install` times out or `No matching distribution`           | Section 3: mirror layout, run `--dry-run` first                          |
| `import weasyprint` → `OSError: cannot load library`            | Section 4: GTK3 not on PATH or `WEASYPRINT_DLL_DIRECTORIES` not set     |
| `ModuleNotFoundError: mkdocs_em_img2fig_plugin`                 | Section 5: use `import src`, not the dist name                           |
| `ModuleNotFoundError: mkdocs_htmlproofer_plugin`                | Section 5: use `import htmlproofer`                                      |
| `ModuleNotFoundError: mkdocs_material`                          | Section 5: use `import material`                                         |
| `mkdocs build` produces 0-byte PDF / silently drops pages       | Section 4: GTK3 missing → WeasyPrint crashes mid-render                  |
| PDF text shows boxes/glyphs for Cyrillic                        | WeasyPrint not finding system fonts — `WEASYPRINT_DLL_DIRECTORIES` set? |
