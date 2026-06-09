---
name: python-env-setup
description: Set up and verify the cbap-mkdocs-ru Python virtual environment on Windows. Use when the venv appears broken, `pip --version` reports a non-venv interpreter, pip cannot reach PyPI (timeouts or blocked from RU IPs), or Python packages fail to import. Also use for smoke-testing mkdocs plugin imports before a build.
license: MIT
compatibility: opencode
metadata:
  source: hand-discovered
  applies_to: cbap-mkdocs-ru
---

# Python venv setup for cbap-mkdocs-ru (Windows)

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

After a real install, verify no broken dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip check
```

## 4. Verify all 13 mkdocs plugins

Naive smoke tests (`for p in mkdocs_*.dist-info: import p`) **fail** for
this repo because three packages have non-standard import names:

| Distribution (pip)                  | Real import          |
| ----------------------------------- | -------------------- |
| `mkdocs-em-img2fig-plugin` 0.3.3    | `import src`         |
| `mkdocs-htmlproofer-plugin` 1.4.1   | `import htmlproofer` |
| `mkdocs-material` 9.7.2             | `import material`    |
| everything else                     | `import <name>`      |

The em-img2fig quirk: its `top_level.txt` ships as `src`, so the package
lives at `.venv\Lib\site-packages\src\__init__.py` and re-exports
`Image2FigurePlugin`. There is no `mkdocs_em_img2fig_plugin` directory.

Reliable verification one-liner:

```powershell
.\.venv\Scripts\python.exe -c "import material, mkdocs_include_markdown_plugin, mkdocs_macros, mkdocs_with_pdf, mkdocs_glightbox, htmlproofer, mkdocs_mermaid_to_svg, mkdocs_section_index, mkdocs_minify_plugin, mkdocs_awesome_pages_plugin, mkdocs_autorefs, mkdocs_autolinks_plugin, src, weasyprint; print('all OK')"
```

Confirm mkdocs itself can load the project's config:

```powershell
.\.venv\Scripts\python.exe -c "from mkdocs.config import load_config; cfg = load_config('mkdocs.yml'); print(cfg['site_name']); print(len(cfg['plugins']), 'plugins registered')"
```

## 5. Quick triage

| Symptom                                                         | First check                                                              |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `pip --version` shows `python-portable`                         | Section 2: missing/broken `.venv\pip.ini`                                |
| `pip install` times out or `No matching distribution`           | Section 3: mirror layout, run `--dry-run` first                          |
| `ModuleNotFoundError: mkdocs_em_img2fig_plugin`                 | Section 4: use `import src`, not the dist name                           |
| `ModuleNotFoundError: mkdocs_htmlproofer_plugin`                | Section 4: use `import htmlproofer`                                      |
| `ModuleNotFoundError: mkdocs_material`                          | Section 4: use `import material`                                         |

If WeasyPrint/GTK3 or PDF build problems arise, load the `mkdocs-pdf-build` skill.
