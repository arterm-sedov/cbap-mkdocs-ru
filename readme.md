## AI-Enabled Repo

Chat with DeepWiki to get answers about the Comindware Platform from this repo:

[Ask DeepWiki](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/arterm-sedov/cbap-mkdocs-ru)

**Русская версия:** [readme-ru.md](readme-ru.md) — руководство оператора на русском языке.

# MkDocs Knowledge Base — Workflows & Operator Guide

This repository contains the MkDocs source for the **Comindware Platform** knowledge base.
Markdown articles live under `docs/ru/`, PHPKB HTML export goes to `for_kb_import_ru/`, PHPKB snapshots to `phpkb_content/` and `phpkb_content_rag/`, RAG bundles for platform KB LLM ingestion, and optional **web scraping** of public sites (`comindware.ru`, `cmwlab.com`) into `scraping/`.

**Audience:** this file is the **operator guide** — repo layout, terminal commands, MkDocs configs, and publish/RAG/PDF workflows.

**Editing articles or writing new content?** Human operators follow the **same rules as AI agents** — all formatting, links, anchors, tags, and product placeholders are defined in [`AGENTS.md`](AGENTS.md). This readme does not repeat those rules; it only points to them. Use this readme for *how* to build, import, and publish; use `AGENTS.md` for *how* to write valid Markdown.

**Commands:** run from the repository root. Workflow sections show **PowerShell** (Windows) and **bash** (WSL / Ubuntu / Linux / macOS).

**Python — two equivalent styles:**

| Style | When | Example |
| --- | --- | --- |
| **Full path** (used in workflows below) | New terminal, venv not activated; reliable copy-paste; no `Activate.ps1` step | `.\.venv\Scripts\python.exe -m mkdocs build …` (Win) · `.venv/bin/python -m mkdocs build …` (Linux) |
| **Shorter** (venv **activated**) | After `Activate.ps1` / `source .venv/bin/activate` in this session | `python -m mkdocs build …` · `pip install …` · `python phpkb_update_articles.py …` |

**How it works:** the venv is the `.venv` folder with its own `python.exe`. A **full-path** command points at that executable directly — you do not need to activate the venv first. **Activation** (`Activate.ps1` / `source .venv/bin/activate`) configures the current terminal session once: after that, plain `python` and `pip` work without the long path — handy when you run many commands in a row. Both styles use the **same** interpreter and packages.

Other substitutions: `$env:CMW_KB_REPO_PATH` → `$CMW_KB_REPO_PATH` (export from `.env` first). Details: [First-time setup → Python virtual environment](#1-python-virtual-environment).

## Document map

| Section | Purpose |
| --- | --- |
| [Repository layout](#repository-layout) | Where files live; what is git-tracked |
| [First-time setup](#first-time-setup) | `.venv`, `.env`, PHPKB assets repo |
| [Quick decision tree](#quick-decision-tree) | Pick a workflow |
| Edit / publish / RAG / images / bundle | Step-by-step terminal workflows |
| [JSON mapping files](#json-mapping-files) | Article maps, clone mappings |
| [MkDocs configuration files](#mkdocs-configuration-files) | Which `mkdocs*.yml` to use; YAML inheritance |
| [Repository scripts](#repository-scripts) | Root Python scripts |
| [Theme overrides](#theme-overrides) | `overrides/`, `pdf_templates/` |
| [Jinja templating basics](#jinja-templating-basics) | Placeholders and `{% if %}` in articles |
| [Build PDF guides](#build-pdf-guides) | GTK3, WeasyPrint, batch PDF |
| [MkDocs build hooks](#mkdocs-build-hooks) | `kb_html_cleanup_hook.py` |
| [Git hooks](#git-hooks) | `.githooks/`, commit message format |
| [Live preview](#mkdocs-serve-local-preview) | `mkdocs serve` configs and options |
| [Git remotes and branches](#git-remotes-and-branches) | `origin`, team fork, mirrors |
| [Daily Git workflow](#daily-git-workflow-platform_v5--platform_v6) | Start of day, feature branches, push |
| [Merge and cherry-pick](#merge-and-cherry-pick-between-platform-versions) | `platform_v5` ↔ `platform_v6` rules and commands |
| [GitHub CLI](#github-cli-gh) | `gh pr`, `gh issue`, CI checks |
| [PHPKB assets deploy](#phpkb-assets-repo-propagate-push-and-ssh-pull) | Sibling `kb.comindware.ru` repo + SSH pull on server |
| [Web scraping for LLM ingestion](#web-scraping-for-llm-ingestion) | Crawl public sites → sanitize → commit |
| [Content editing standards](#content-editing-standards) | Article rules — index into `AGENTS.md` + Jinja section below |
| [Agent skills](#agent-skills-reference) | End-to-end playbooks (full index in `AGENTS.md`) |
| [Scratch directory](#scratch-directory) | Disposable temp files (`.scratch/`) |
| [Troubleshooting](#troubleshooting) | Common failures |

**Writing or editing `docs/ru/`?** → [`AGENTS.md`](AGENTS.md) · [Content editing standards](#content-editing-standards). **Running builds, imports, or scripts?** → sections below · [`AGENTS.md` → Human operators cross-reference](AGENTS.md#human-operators--readme-cross-reference) · [Skills Reference](AGENTS.md#skills-reference).


## Content editing standards

Humans and agents share one rulebook: [`AGENTS.md`](AGENTS.md). Before editing any article, skim the rows that apply to your change.

**Article content**

| Topic | `AGENTS.md` | This readme (build mechanics) |
| --- | --- | --- |
| Cross-article `[title][anchor_name]`; named-anchor hub; `autorefs` | [Link formatting](AGENTS.md#link-formatting) | [Include snippets](#include-snippets) · [Link references](#link-references-in-articles) |
| Same-page `[title](#anchor_name)` only | [Link formatting](AGENTS.md#link-formatting) | [Link references](#link-references-in-articles) |
| Map include on **every** `docs/` article | [Hyperlink-map include](AGENTS.md#hyperlink-map-include-required-on-every-article) | [Include snippets](#include-snippets) |
| KB section URLs (`kbId#fragment`) — map only | [Map URLs with fragments](AGENTS.md#map-urls-with-kbidsection_anchor-fragments) | — |
| Map `{% if %}` vs guide / `kbExport` flags | [Map conditionals](AGENTS.md#how-map-conditionals-mirror-yaml-configs) | [Guide flags](#guide-flags-extra-section) · [Conditional content](#conditional-content) |
| Bullet and numbered lists | [List formatting](AGENTS.md#list-formatting) | — |
| Italic and bold | [_Italic_](AGENTS.md#italic) · [**Bold**](AGENTS.md#bold) | — |
| `**{{ productName }}**` and brand placeholders | [Product & brand names](AGENTS.md#product--brand-names) | [Product placeholders](#product-placeholders) |
| Frontmatter tags | [Tags](AGENTS.md#tags) | — |
| `&nbsp;` and similar | [HTML entities](AGENTS.md#html-entities) | — |
| `{: #anchor .pageBreak_* }` on headings (`docs/ru/` only) | [Headings](AGENTS.md#headings) · [Rules](AGENTS.md#rules) (preserve anchors/classes) | — |
| Hard PDF page break | [Headings](AGENTS.md#headings) | [PDF page breaks](#pdf-page-breaks) |

**Repo and git** (operators — full commands in sections below)

| Topic | `AGENTS.md` | This readme |
| --- | --- | --- |
| Do not edit `phpkb_content/` by hand | [Context](AGENTS.md#context) | [Repository layout](#repository-layout) |
| Temp files in `.scratch/` only | [Scratch directory](AGENTS.md#scratch-directory) | [Scratch directory](#scratch-directory) |
| Commit message `[#ticket]` format | [Commit messages](AGENTS.md#commit-messages) | [Git hooks](#git-hooks) · skill `cmwhelp-commit` |
| Cherry-pick / separate commits per artifact layer | [Cherry-picking](AGENTS.md#cherry-picking-between-platform-versions) | [Merge and cherry-pick](#merge-and-cherry-pick-between-platform-versions) |
| Python `.venv` / script invocation | [Python environment](AGENTS.md#python-environment) | [First-time setup](#first-time-setup) |
| End-to-end workflows | [Skills Reference](AGENTS.md#skills-reference) | [Agent skills](#agent-skills-reference) · [Quick decision tree](#quick-decision-tree) |

Reverse index (readme → `AGENTS.md`): [`AGENTS.md` → Human operators cross-reference](AGENTS.md#human-operators--readme-cross-reference).


## Repository layout

| Path | What it is | Git-tracked | Edited by |
| --- | --- | --- | --- |
| `docs/ru/` | Authoritative MkDocs source (Markdown) | Yes | Human editors / agents |
| `for_kb_import_ru/` | PHPKB-compatible HTML export | Yes | `mkdocs build -f mkdocs_for_kb_import_ru.yml` |
| `phpkb_content/` | PHPKB DB snapshot with MkDocs transforms | Yes | `phpkb_import.py` only — **do not edit by hand** |
| `phpkb_content_rag/` | PHPKB DB snapshot for RAG (markdown-only) | Yes | `phpkb_import_for_rag.py` only — **do not edit by hand** |
| `phpkb_content_cmw_lab/` | PHPKB snapshot for CMW Lab / v4 | Yes | `phpkb_import_cmw_lab.py` only — **do not edit by hand** |
| `kb.comindware.ru.platform_v*_for_llm_ingestion.md` | Single-file LLM bundle | Yes | `phpkb_ingest.py` |
| `kb.comindware.ru/platform/` | Local junction/symlink to PHPKB assets repo | **No** (gitignored) | Copy scripts only |
| `scraping/{site}/` | Sanitized web crawl output + checkpoints | Yes | Crawl/sanitize scripts |
| `.scratch/` | Disposable temp files (incl. raw `*_dirty_*.md` crawls) | No | Operators (gitignored) |

Version-specific folders under `phpkb_content/` and `phpkb_content_rag/` follow an **asymmetric** cherry-pick rule: v5 trees (`798-platform_v5/`) and the v5 LLM bundle may be cherry-picked **onto `platform_v6` only**; **never** bring v6 import trees or the v6 bundle onto `platform_v5`. **`for_kb_import_ru/` cannot** be cherry-picked either way — rebuild on the target branch. See [Merge and cherry-pick → Cherry-pick vs rebuild](#cherry-pick-vs-rebuild).

**Two separate Git repositories:**

1. **This repo** (`cbap-mkdocs-ru`) — source Markdown, HTML export, RAG trees, root-level bundle file.
2. **PHPKB static assets repo** (sibling checkout) — path in `.env` as `CMW_KB_REPO_PATH`. Images and LLM bundles are published under `platform/v5.0/` or `platform/v6.0/` there.

Do **not** `git add kb.comindware.ru/` in this repo. Commit assets in the PHPKB repo (manually or via `--git` flags on scripts).

**Platform source code** (sibling repo, for verifying feature behavior): set `PLATFORM_SOURCE_CODE` in `.env` (see `.env.example`). Typical path: `../CBAP_MONO`.


## First-time setup

### 1. Python virtual environment

All Python packages for this repo are listed in `install/requirements.txt` (MkDocs, plugins, PHPKB scripts, scraping tools, etc.). Install them into a local `.venv` at the repo root — never into the system Python.

**First time** (no `.venv` yet) — run the deploy script with **system** Python:

```powershell
# Windows — interactive: creates .venv, upgrades pip, installs requirements.txt
py install\deploy_venv.py
# When prompted for the venv folder name, press Enter — default is `.venv` (hardcoded in install/deploy_venv.py, not .env)

# Smoke test
.\.venv\Scripts\python.exe -c "import mkdocs; print('OK')"
```

```bash
# WSL / Ubuntu / Linux — same flow
python3 install/deploy_venv.py

# Smoke test
.venv/bin/python -c "import mkdocs; print('OK')"
```

`install/deploy_venv.py` creates `.venv`, upgrades `pip`, and runs `pip install -U -r install/requirements.txt`. One-shot Windows alternative (non-interactive): `install\deploymkdocs.ps1`.

**Refresh dependencies** when `install/requirements.txt` changed (e.g. after `git pull`) — venv must already exist:

```powershell
# Windows — with venv activated, or use the full path to python.exe
.\.venv\Scripts\python.exe -m pip install -U -r install\requirements.txt
```

```bash
# WSL / Ubuntu / Linux
.venv/bin/python -m pip install -U -r install/requirements.txt
```

**Activate the venv** (each new terminal session). Run from the repository root:

| Environment | Activate |
| --- | --- |
| Windows (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Windows (cmd.exe) | `.\.venv\Scripts\activate.bat` |
| WSL / Ubuntu / Linux | `source .venv/bin/activate` |

If PowerShell blocks activation (`execution policy`), run once in the current session: `Set-ExecutionPolicy -Scope Process Bypass`, then activate again.

**Full path vs activated venv** — same result, pick what fits the session:

| Task | Without activation (on the fly) | With venv activated |
| --- | --- | --- |
| MkDocs build | `.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml` | `python -m mkdocs build -f mkdocs_for_kb_import_ru.yml` |
| MkDocs serve | `.\.venv\Scripts\python.exe -m mkdocs serve` | `python -m mkdocs serve` |
| PHPKB script | `.\.venv\Scripts\python.exe phpkb_update_articles.py …` | `python phpkb_update_articles.py …` |
| Refresh deps | `.\.venv\Scripts\python.exe -m pip install -U -r install\requirements.txt` | `pip install -U -r install/requirements.txt` |

```bash
# Linux/macOS — without activation
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
.venv/bin/python phpkb_update_articles.py --profile cmw --article-id 123 --yes

# Linux/macOS — after: source .venv/bin/activate
python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
python phpkb_update_articles.py --profile cmw --article-id 123 --yes
```

Workflow sections below use **full paths** so they work in a fresh shell without activation. After `Activate.ps1` or `source .venv/bin/activate`, shorten every `.\.venv\Scripts\python.exe` / `.venv/bin/python` to `python` (and `pip` instead of `python -m pip`).

If the venv is broken (wrong `pip` path, missing plugins), re-run `install/deploy_venv.py` or see `.agents/skills/python-env-setup/SKILL.md`.

### 2. `.env` configuration

```powershell
Copy-Item .env.example .env
# Edit .env — fill in SSH, SQL, and PHPKB repo paths
```

```bash
cp .env.example .env
# Edit .env — fill in SSH, SQL, and PHPKB repo paths
```

Load env vars in bash (from repo root):

```bash
set -a && source .env && set +a
```


| Variable | Required for | Purpose |
| --- | --- | --- |
| `SERVER_PROFILE` | DB scripts | `cmw` (kb.comindware.ru) or `cmwlab` |
| `CMW_SSH_*`, `CMW_SQL_*` | Publish, import | SSH tunnel + MySQL to PHPKB |
| `CMW_KB_REPO_PATH` | Image/bundle `--git` | Local checkout of the PHPKB assets sibling repo |
| `CMW_SSH_KB_REPO_PATH` | `--pull` | Remote path on production for `git pull` |

Optional: `SSH_USE_STORED_CREDENTIALS=1` to skip keychain prompts. See `.env.example` for the full list.

### 3. PHPKB assets repo checkout

Clone the kb.comindware **static assets** repository as a **sibling checkout** next to this repo and point `.env` at it.

**Example (Windows):** if this repo is `C:\Repos\cbap-mkdocs-ru`, clone assets to `C:\Repos\kb.comindware.ru` and set:

```ini
# In .env (gitignored — never commit)
CMW_KB_REPO_PATH=C:/Repos/kb.comindware.ru
CMW_SSH_KB_REPO_PATH=/var/www/html
```

`CMW_KB_REPO_PATH` — local checkout where scripts copy images and LLM bundles (`platform/v5.0/`, `platform/v6.0/`).

`CMW_SSH_KB_REPO_PATH` — **on the production KB server**, the path to the same git repo (used by `utilities/ssh_pull.py` when you pass `--pull`). It is usually **not** the same string as the Windows path.

SSH to PHPKB for publish/import uses the same profile (`CMW_SSH_HOST`, `CMW_SSH_USERNAME`, …) — see `.env.example`. Use `SSH_USE_STORED_CREDENTIALS=1` if you authenticate with keys/agent instead of passwords in `.env`.

Verify the sibling checkout:

```powershell
Test-Path "$env:CMW_KB_REPO_PATH\.git"
Get-ChildItem "$env:CMW_KB_REPO_PATH\platform\v6.0" -ErrorAction SilentlyContinue | Select-Object -First 5
```

```bash
test -d "$CMW_KB_REPO_PATH/.git"
ls "$CMW_KB_REPO_PATH/platform/v6.0" 2>/dev/null | head
```

Optionally create a junction **inside this repo** (not required when `CMW_KB_REPO_PATH` is set):

```powershell
# Example — adjust paths to your machine
New-Item -ItemType Junction -Path "kb.comindware.ru\platform\v6.0" -Target "D:\Repo\kb.comindware.ru\platform\v6.0"
Get-Item kb.comindware.ru\platform\v6.0 | Format-List LinkType, Target
```

```bash
# Optional symlink instead of Windows junction
ln -s /path/to/kb.comindware.ru/platform/v6.0 kb.comindware.ru/platform/v6.0
ls -la kb.comindware.ru/platform/v6.0
```


Verify the junction before copying images or bundles.

### 4. Platform version reference

| Platform | PHPKB root category | RAG folder | Article map | Bundle output | Assets target |
| --- | --- | --- | --- | --- | --- |
| v5.0 | `798` | `phpkb_content_rag/798-platform_v5` | `.article_id_filename_map_v5.json` | `kb.comindware.ru.platform_v5_for_llm_ingestion.md` | `kb.comindware.ru/platform/v5.0` |
| v6.0 | `896` | `phpkb_content_rag/896-platform_v6` | `.article_id_filename_map_v6.json` | `kb.comindware.ru.platform_v6_for_llm_ingestion.md` | `kb.comindware.ru/platform/v6.0` |

Work on the Git branch that matches your target platform (`platform_v5`, `platform_v6`, etc.).


## Quick decision tree

| Goal | Workflow section |
| --- | --- |
| Edit an existing article and publish to PHPKB | [Edit → build HTML → publish → commit](#edit--build-html--publish--commit) |
| Publish many changed articles at once | [Batch publish from git diff](#batch-publish-from-git-diff) |
| Add a brand-new article to PHPKB | [Publish a new article](#publish-a-new-article) |
| Copy new/updated images to PHPKB repo | [Sync images to PHPKB assets repo](#sync-images-to-phpkb-assets-repo) |
| Refresh RAG corpus from PHPKB DB | [Refresh phpkb_content_rag](#refresh-phpkb_content_rag) |
| Refresh MkDocs-oriented PHPKB snapshot | [Refresh phpkb_content](#refresh-phpkb_content) |
| Rebuild the LLM ingestion bundle | [Build AI bundle](#build-ai-bundle) |
| Push bundle to PHPKB repo + production | [Push AI bundle to sibling repo](#push-ai-bundle-to-sibling-repo) |
| Propagate images/bundle to sibling KB repo + SSH pull on server | [PHPKB assets deploy](#phpkb-assets-repo-propagate-push-and-ssh-pull) |
| Crawl a public website for LLM bundle | [Web scraping for LLM ingestion](#web-scraping-for-llm-ingestion) |
| Cherry-pick between `platform_v5` / `platform_v6` | [Merge and cherry-pick](#merge-and-cherry-pick-between-platform-versions) (also in `AGENTS.md`) |
| Preview docs locally | [MkDocs serve](#mkdocs-serve-local-preview) |
| Build PDF guides | [Build PDF guides](#build-pdf-guides) |
| Understand MkDocs configs | [MkDocs configuration files](#mkdocs-configuration-files) |
| Product placeholders / conditional text | [Jinja templating basics](#jinja-templating-basics) |
| Change HTML theme or PHPKB export layout | [Theme overrides](#theme-overrides) |
| Enable commit-message hooks | [Git hooks](#git-hooks) |
| Write or edit article content | [`AGENTS.md`](AGENTS.md) · [Content editing standards](#content-editing-standards) |
| Git remotes, daily sync, `gh` CLI | [Git remotes](#git-remotes-and-branches) · [Daily workflow](#daily-git-workflow-platform_v5--platform_v6) · [GitHub CLI](#github-cli-gh) |


## Edit → build HTML → publish → commit

Standard cycle for an **existing** article that already has `kbId:` in frontmatter.

### 1. Edit Markdown

Edit the file under `docs/ru/`. Apply the same standards as agents — see [Content editing standards](#content-editing-standards) (`AGENTS.md` for full rules).

### 2. Build PHPKB import HTML

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

Wait for `Documentation built in N seconds`. Missing-anchor warnings are non-fatal.

### 3. Verify the export changed

```powershell
git diff --name-only for_kb_import_ru/
git status --short for_kb_import_ru/
```

### 4. Extract `kb-id` and publish to PHPKB

```powershell
# Replace path with your article's HTML file
Select-String -Path for_kb_import_ru\administration\deploy\script_keys.html -Pattern 'kb-id="(\d+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } | Select-Object -First 1

# Publish (--yes skips confirmation prompts)
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --article-id <kb-id> --yes
```

```bash
# Replace path with your article's HTML file
rg -o 'kb-id="([0-9]+)"' for_kb_import_ru/administration/deploy/script_keys.html -r '$1' | head -1

# Publish (--yes skips confirmation prompts)
.venv/bin/python phpkb_update_articles.py --profile cmw --article-id <kb-id> --yes
```

Confirm output: `Updated article <kb-id>`.

Direct article URL after publish: `https://kb.comindware.ru/article.php?id=<kb-id>`.

### 5. Sync images (if the article has new or changed images)

See [Sync images to PHPKB assets repo](#sync-images-to-phpkb-assets-repo).

### 6. Commit and push (this repo)

```powershell
git add docs/ru/<edited-file>.md for_kb_import_ru/<matching-export>.html
git commit -m "[#<ticket>] <concise description>"
git push
```

Commit message format: `[#XXXXX] Imperative description`. See `.agents/skills/cmwhelp-commit/SKILL.md`.


## Batch publish from git diff

When several existing articles were edited and rebuilt HTML is already in `for_kb_import_ru/`.

### 1. Rebuild (if not done yet)

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

### 2. List changed HTML files

```powershell
git diff --name-only for_kb_import_ru/
```

### 3. Collect `kb-id` values

Read `kb-id="…"` from each changed `.html` file. Skip files with `kb-id=""` — they have no PHPKB row yet; add `kbId:` to the source `.md` or clone a placeholder article first.

```powershell
Select-String -Path for_kb_import_ru\**\*.html -Pattern 'kb-id="(\d+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } | Where-Object { $_ } | Sort-Object -Unique
```

```bash
rg -o 'kb-id="([0-9]+)"' for_kb_import_ru/ -r '$1' | sort -u
```

### 4. Publish all IDs in one run

```powershell
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --yes `
  --article-id 5451 --article-id 5558
```

```bash
.venv/bin/python phpkb_update_articles.py --profile cmw --yes \
  --article-id 5451 --article-id 5558
```

Or publish an entire category tree:

```powershell
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --category-id 896 --yes
```

```bash
.venv/bin/python phpkb_update_articles.py --profile cmw --category-id 896 --yes
```

### 5. Commit source + export

```powershell
git add docs/ru/ for_kb_import_ru/
git commit -m "[#<ticket>] Publish updated articles to PHPKB"
git push
```


## Publish a new article

For a local Markdown file **without** `kbId:` that must become a new PHPKB article.

1. Clone an adjacent PHPKB article with `utilities/phpkb_cloning/phpkb_clone.py` (dry-run first). See `.agents/skills/phpkb-cloning/SKILL.md`.
2. Add `kbId: <new-id>` to the Markdown frontmatter.
3. Add hyperlink-map entry in `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` if needed.
4. Rebuild HTML and publish:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --article-id <new-id> --yes
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
.venv/bin/python phpkb_update_articles.py --profile cmw --article-id <new-id> --yes
```

5. Commit `docs/ru/`, `for_kb_import_ru/`, and hyperlink map changes.


## Sync images to PHPKB assets repo

Copies images from `for_kb_import_ru/` into `{CMW_KB_REPO_PATH}/platform/{version}/`.

**Prerequisite:** rebuild HTML first so `for_kb_import_ru/` is current.

```powershell
# Copy only (no git)
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0

# Copy + commit + push in the PHPKB assets repo
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git

# Copy + push + SSH git pull on production
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull

# Fully non-interactive (CI / scripted)
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

```bash
# Copy only (no git)
.venv/bin/python phpkb_copy_images.py --version v6.0

# Copy + commit + push in the PHPKB assets repo
.venv/bin/python phpkb_copy_images.py --version v6.0 --git

# Copy + push + SSH git pull on production
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull

# Fully non-interactive (CI / scripted)
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

`--version` is **required** (`v4.7`, `v5.0`, or `v6.0`).

The script copies **all** images from the export tree — not article-scoped. If only one article's images changed, inspect the diff in the PHPKB repo before committing:

```powershell
git -C "$env:CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$env:CMW_KB_REPO_PATH" diff --name-status -- platform/v6.0
```

```bash
git -C "$CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$CMW_KB_REPO_PATH" diff --name-status -- platform/v6.0
```

### Manual fallback (PHPKB assets repo)

```powershell
# After copy, in the sibling repo
git -C "$env:CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$env:CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$env:CMW_KB_REPO_PATH" push
```

```bash
# After copy, in the sibling repo
git -C "$CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$CMW_KB_REPO_PATH" push
```


## Refresh phpkb_content_rag

Pulls articles from the PHPKB database into `phpkb_content_rag/` (markdown-only, for RAG/LLM). **Read-only against PHPKB** — writes local files only.

**Duration:** 5–10+ minutes for a full category. Wait for `Import finished. Total articles imported: <N>`.

### v6

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py `
  --category-id 896 `
  --article-map .article_id_filename_map_v6.json
```

```bash
.venv/bin/python phpkb_import_for_rag.py \
  --category-id 896 \
  --article-map .article_id_filename_map_v6.json
```

### v5

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py `
  --category-id 798 `
  --article-map .article_id_filename_map_v5.json
```

```bash
.venv/bin/python phpkb_import_for_rag.py \
  --category-id 798 \
  --article-map .article_id_filename_map_v5.json
```

### After import — commit (this repo)

```powershell
git status --short phpkb_content_rag/
git add phpkb_content_rag/
git commit -m "[#<ticket>] Refresh phpkb_content_rag from PHPKB"
git push
```

**Never edit `phpkb_content_rag/` by hand.** Regenerate from PHPKB or fix source in `docs/ru/`.


## Refresh phpkb_content

Pulls articles from PHPKB into `phpkb_content/` with full MkDocs-oriented transforms. Independent from `phpkb_content_rag/` — both read the DB directly.

`--article-map` is **required**.

### v6

```powershell
.\.venv\Scripts\python.exe phpkb_import.py `
  --category-id 896 `
  --article-map .article_id_filename_map_v6.json
```

```bash
.venv/bin/python phpkb_import.py \
  --category-id 896 \
  --article-map .article_id_filename_map_v6.json
```

### v5

```powershell
.\.venv\Scripts\python.exe phpkb_import.py `
  --category-id 798 `
  --article-map .article_id_filename_map_v5.json
```

```bash
.venv/bin/python phpkb_import.py \
  --category-id 798 \
  --article-map .article_id_filename_map_v5.json
```

### After import — commit (this repo)

```powershell
git add phpkb_content/
git commit -m "[#<ticket>] Refresh phpkb_content from PHPKB"
git push
```


## Build AI bundle

Bundles `phpkb_content_rag/` into a single Markdown file for LLM ingestion. No DB access — reads local RAG tree only.

All four arguments are **required**: `--folder`, `--output`, `--target-dir`, `--category-id`.

### v6

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896
```

### v5

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/798-platform_v5 `
  --output kb.comindware.ru.platform_v5_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v5.0 `
  --category-id 798
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/798-platform_v5 \
  --output kb.comindware.ru.platform_v5_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v5.0 \
  --category-id 798
```

### Verify bundle header

After the script finishes, check the output file:

- `Ingestion date` — current timestamp
- `Files analyzed` — markdown file count
- `Estimated tokens` — tiktoken estimate

Console should show: `File copied to: kb.comindware.ru\platform\v6.0\kb.comindware.ru.platform_v6_for_llm_ingestion.md`

### Bundle only (RAG corpus already current)

When `phpkb_content_rag/` is up to date and only the single-file bundle needs rebuilding:

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896
```

With git-sync and production pull:

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896 `
  --version v6.0 --git --pull --no-ask
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896 \
  --version v6.0 --git --pull --no-ask
```

**Safety:** `phpkb_import_for_rag.py` is read-only against PHPKB. `phpkb_ingest.py` reads local RAG tree only. Do not confuse with `phpkb_update_articles.py` (writes to PHPKB DB). **`--article-map` is required** for both import scripts.

### Full refresh (RAG + snapshot + bundle)

When PHPKB DB may have changed and everything should be current:

```powershell
# v6 example — adjust IDs/paths for v5
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896 --article-map .article_id_filename_map_v6.json
.\.venv\Scripts\python.exe phpkb_import.py --category-id 896 --article-map .article_id_filename_map_v6.json
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896
```

```bash
# v6 example — adjust IDs/paths for v5
.venv/bin/python phpkb_import_for_rag.py --category-id 896 --article-map .article_id_filename_map_v6.json
.venv/bin/python phpkb_import.py --category-id 896 --article-map .article_id_filename_map_v6.json
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896
```

### Commit bundle (this repo)

Use **three separate commits** — do not combine import trees and bundle:

```powershell
git add phpkb_content/
git commit -m "[#<ticket>] Refresh phpkb_content from PHPKB"

git add phpkb_content_rag/
git commit -m "[#<ticket>] Refresh phpkb_content_rag from PHPKB"

git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push
```

```bash
git add phpkb_content/
git commit -m "[#<ticket>] Refresh phpkb_content from PHPKB"

git add phpkb_content_rag/
git commit -m "[#<ticket>] Refresh phpkb_content_rag from PHPKB"

git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push
```

Keep article edits, HTML export, and each import/bundle artifact (`phpkb_content/`, `phpkb_content_rag/`, LLM bundle) in **separate commits** — easier to cherry-pick between version branches.


## Push AI bundle to sibling repo

The bundle exists in **two places** after `phpkb_ingest.py`:

1. Repo root — `kb.comindware.ru.platform_v*_for_llm_ingestion.md` (this repo)
2. `{CMW_KB_REPO_PATH}/platform/{version}/` (PHPKB assets sibling repo)

### Automated (recommended)

Add `--git` to commit and push in the PHPKB repo. Add `--pull` to SSH `git pull` on production.

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896 `
  --version v6.0 `
  --git --pull --no-ask
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896 \
  --version v6.0 \
  --git --pull --no-ask
```

`--git` runs `utilities/git_sync.py`: stages files in `CMW_KB_REPO_PATH/platform/{version}/`, prompts for ticket number (or use `--no-ask`), commits, pushes.

`--pull` runs `utilities/ssh_pull.py`: SSH to production and `git pull` in `CMW_SSH_KB_REPO_PATH`.

Full walkthrough (local `C:/Repos/kb.comindware.ru`, SSH pull on server): [PHPKB assets deploy](#phpkb-assets-repo-propagate-push-and-ssh-pull).

### Manual fallback

```powershell
# This repo
git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push

# PHPKB assets sibling repo
git -C "$env:CMW_KB_REPO_PATH" add platform/v6.0/kb.comindware.ru.platform_v6_for_llm_ingestion.md
git -C "$env:CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git -C "$env:CMW_KB_REPO_PATH" push
```

```bash
# This repo
git add kb.comindware.ru.platform_v6_for_llm_ingestion.md
git commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git push

# PHPKB assets sibling repo
git -C "$CMW_KB_REPO_PATH" add platform/v6.0/kb.comindware.ru.platform_v6_for_llm_ingestion.md
git -C "$CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6 RAG ingestion bundle"
git -C "$CMW_KB_REPO_PATH" push
```


## PHPKB assets repo: propagate, push, and SSH pull

Static assets (images, LLM ingestion bundles) live in a **separate git repository** from `cbap-mkdocs-ru`. Typical layout on a developer machine:

```
C:\Repos\
  cbap-mkdocs-ru\          ← this repo (Markdown, HTML export, bundle copy in root)
  kb.comindware.ru\        ← sibling assets repo (CMW_KB_REPO_PATH in .env)
    platform\
      v5.0\                ← images + kb.comindware.ru.platform_v5_for_llm_ingestion.md
      v6.0\                ← images + kb.comindware.ru.platform_v6_for_llm_ingestion.md
```

On the **KB production server**, the same assets repo is checked out at `CMW_SSH_KB_REPO_PATH` (often `/var/www/html` or similar — set in `.env`, not in git).

### Pipeline overview

| Step | Where | What |
| --- | --- | --- |
| 1. Build / copy | Your PC | Scripts write into `CMW_KB_REPO_PATH/platform/{version}/` |
| 2. `--git` | Your PC | `utilities/git_sync.py` → `git add`, `commit`, `push` **in the sibling repo** |
| 3. `--pull` | KB server via SSH | `utilities/ssh_pull.py` → `git pull` in `CMW_SSH_KB_REPO_PATH` |
| 4. PHPKB serves files | Production | KB reads images/bundles from the server checkout |

Article HTML still goes to the PHPKB **database** via `phpkb_update_articles.py` — that is separate from the assets repo.

### Required `.env` variables (profile `cmw`)

| Variable | Example | Purpose |
| --- | --- | --- |
| `CMW_KB_REPO_PATH` | `C:/Repos/kb.comindware.ru` | Local sibling checkout |
| `CMW_SSH_KB_REPO_PATH` | `/var/www/html` | Remote path for `git pull` on KB server |
| `CMW_SSH_HOST` | (your host) | SSH target for `--pull` and DB tunnel |
| `CMW_SSH_USERNAME` | (your user) | SSH login |
| `CMW_SSH_PASSWORD` | (optional) | If not using key/agent — **keep in `.env` only** |

Load into the shell before manual `git -C`:

```powershell
# PowerShell — from cbap-mkdocs-ru root
Get-Content .env | ForEach-Object {
  if ($_ -match '^\s*([^#][^=]+)=(.*)$') { Set-Item -Path "env:$($matches[1].Trim())" -Value $matches[2].Trim() }
}
```

```bash
set -a && source .env && set +a
```

### Propagate images (full chain)

**Prerequisite:** `mkdocs build -f mkdocs_for_kb_import_ru.yml` so `for_kb_import_ru/` is current.

**Copy → commit/push → SSH pull (recommended one-liner):**

```powershell
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull
```

```bash
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull
```

Non-interactive (CI or scripted):

```powershell
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

```bash
.venv/bin/python phpkb_copy_images.py --version v6.0 --git --pull --no-ask
```

**Step by step:**

```powershell
# 1 — copy files into C:\Repos\kb.comindware.ru\platform\v6.0\ (via CMW_KB_REPO_PATH)
.\.venv\Scripts\python.exe phpkb_copy_images.py --version v6.0

# 2 — inspect sibling repo before commit
git -C "$env:CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$env:CMW_KB_REPO_PATH" diff --name-status -- platform/v6.0

# 3 — commit and push sibling repo only
git -C "$env:CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$env:CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$env:CMW_KB_REPO_PATH" push

# 4 — pull on KB server
.\.venv\Scripts\python.exe utilities/ssh_pull.py
```

```bash
.venv/bin/python phpkb_copy_images.py --version v6.0
git -C "$CMW_KB_REPO_PATH" status --short -- platform/v6.0
git -C "$CMW_KB_REPO_PATH" add platform/v6.0/
git -C "$CMW_KB_REPO_PATH" commit -m "[#<ticket>] Update platform v6.0 images"
git -C "$CMW_KB_REPO_PATH" push
.venv/bin/python utilities/ssh_pull.py
```

Use `v5.0` when working on the `platform_v5` branch.

### Propagate LLM bundle (full chain)

After `phpkb_ingest.py` writes the bundle to the sibling repo:

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py `
  --folder phpkb_content_rag/896-platform_v6 `
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md `
  --target-dir kb.comindware.ru/platform/v6.0 `
  --category-id 896 `
  --version v6.0 --git --pull
```

```bash
.venv/bin/python phpkb_ingest.py \
  --folder phpkb_content_rag/896-platform_v6 \
  --output kb.comindware.ru.platform_v6_for_llm_ingestion.md \
  --target-dir kb.comindware.ru/platform/v6.0 \
  --category-id 896 \
  --version v6.0 --git --pull
```

Remember **two commits** when the bundle also changed in this repo root: commit/push `cbap-mkdocs-ru` and the sibling `kb.comindware.ru` separately.

### SSH pull only (assets already pushed)

When someone else pushed to the assets repo, or you pushed manually and only need production updated:

```powershell
.\.venv\Scripts\python.exe utilities/ssh_pull.py
```

```bash
.venv/bin/python utilities/ssh_pull.py
```

Skip confirmation:

```bash
.venv/bin/python utilities/ssh_pull.py --no-ask
```

The script connects with `CMW_SSH_*` credentials, then runs remotely:

```bash
cd $CMW_SSH_KB_REPO_PATH && git pull
```

(path from `.env`, not your local `C:\Repos\…` path).

### Manual SSH on the KB server

If you prefer the shell on the server (same result as `ssh_pull.py`):

```bash
ssh <CMW_SSH_USERNAME>@<CMW_SSH_HOST>
cd /var/www/html    # or your CMW_SSH_KB_REPO_PATH value
git pull
git log -1 --oneline
ls platform/v6.0/ | head
exit
```

Use the host and remote path from `.env` — do not commit real hostnames or passwords to the repo.

### What not to do

- Do **not** `git add kb.comindware.ru/` **inside `cbap-mkdocs-ru`** — that path is either a junction or outside this repo.
- Do **not** put `CMW_KB_REPO_PATH` or SSH secrets in Markdown articles or commit `.env`.
- **`--git` without `--pull`** updates GitHub/GitVerse but production KB may still serve old files until `git pull` runs on the server.


## Web scraping for LLM ingestion

Crawl **public websites** (not PHPKB) into a single sanitized Markdown file per site. Separate from the [platform RAG pipeline](#refresh-phpkb_content_rag) (`phpkb_import_for_rag.py` / `phpkb_ingest.py`), which reads the Comindware KB database.

| Pipeline | Source | Output |
| --- | --- | --- |
| Platform RAG | PHPKB DB | `kb.comindware.ru.platform_v*_for_llm_ingestion.md` |
| Web scraping | Public sitemap | `scraping/{site}/{site}_sanitized_{date}.md` |

Scripts: `.agents/skills/scrape-sanitize/scripts/` (extended playbook: `.agents/skills/scrape-sanitize/SKILL.md`).

### Sites

| `--site` | Sitemap | Crawler |
| --- | --- | --- |
| `comindware_ru` | https://www.comindware.ru | `crawl4ai_ingest.py` |
| `cmwlab_com` | https://www.cmwlab.com | `crawl4ai_ingest.py` |

Site-specific boilerplate removal: `patterns_comindware_ru.py`, `patterns_cmwlab_com.py` in the scripts folder.

### File flow

```
crawl4ai_ingest.py
  → .scratch/{site}_dirty_{YYYYMMDD}.md     (raw, gitignored)
  → scraping/{site}/progress_{YYYYMMDD}.json  (resume checkpoint, tracked)

sanitize.py
  → scraping/{site}/sanitize_checkpoint.json  (resume checkpoint, tracked)
  → scraping/{site}/{site}_sanitized_{YYYYMMDD}.md  (final, tracked)
```

Use the **same `--date`** for crawl and sanitize (default: today as `YYYYMMDD`).

### Standard workflow

Set script path once (repo root):

```powershell
$ss = ".agents/skills/scrape-sanitize/scripts"
```

```bash
ss=".agents/skills/scrape-sanitize/scripts"
```

**1. Crawl** (network required; may take a long time):

```powershell
.\.venv\Scripts\python.exe $ss\crawl4ai_ingest.py --site comindware_ru
```

```bash
.venv/bin/python $ss/crawl4ai_ingest.py --site comindware_ru
```

**2. Sanitize** (use the date from step 1, or omit `--date` if same day):

```powershell
.\.venv\Scripts\python.exe $ss\sanitize.py --site comindware_ru --date 20260616
```

```bash
.venv/bin/python $ss/sanitize.py --site comindware_ru --date 20260616
```

**3. Review** `scraping/comindware_ru/comindware_ru_sanitized_20260616.md`.

**4. Commit** tracked artifacts:

```powershell
git add scraping/comindware_ru/
git commit -m "[#<ticket>] Refresh comindware.ru scraped LLM bundle"
git push
```

Do not commit `.scratch/*_dirty_*.md`.

### Resume vs start over

Interrupted runs resume automatically via checkpoint files. To **start from scratch**:

```powershell
.\.venv\Scripts\python.exe $ss\crawl4ai_ingest.py --site comindware_ru --fresh
.\.venv\Scripts\python.exe $ss\sanitize.py --site comindware_ru --date 20260616 --fresh
```

```bash
.venv/bin/python $ss/crawl4ai_ingest.py --site comindware_ru --fresh
.venv/bin/python $ss/sanitize.py --site comindware_ru --date 20260616 --fresh
```

| Flag | Crawl clears | Sanitize clears |
| --- | --- | --- |
| `--fresh` on crawl | dirty `.md`, `progress_*.json` | — |
| `--fresh` on sanitize | — | `sanitize_checkpoint.json`, sanitized output |

Re-sanitize without re-crawling: run `sanitize.py` only (omit `--fresh` to resume, or `--fresh` to re-process the existing dirty file).

### Dependencies

Already in `install/requirements.txt`: `crawl4ai`, `beautifulsoup4`, `markdownify`, `tiktoken`. Failures log to `.scratch/ralph/{site}_failures.log`.

### Legacy script

`http_bs4_ingest.py` — older requests+BS4 crawler with hardcoded paths; prefer `crawl4ai_ingest.py` for new runs.


## MkDocs serve (local preview)

Run from the repository root with the venv active (or use `.venv/bin/python` / `.\.venv\Scripts\python.exe`). Default URL: http://127.0.0.1:8000 — the server watches `docs/` and reloads on save.

### Which config to serve

| Config | When to use | Output dir |
| --- | --- | --- |
| `mkdocs.yml` | **Default** — full Russian nav for authoring | `compiled_help/` |
| `mkdocs_guide_complete_ru.yml` | Same as default (explicit) | (inherited) |
| `mkdocs_guide_user_ru.yml` | Preview **user guide** subset only | (inherited) |
| `mkdocs_guide_admin_windows_ru.yml` | Admin guide (Windows) subset | (inherited) |
| `mkdocs_guide_admin_linux_ru.yml` | Admin guide (Linux) subset | (inherited) |
| `mkdocs_en_local.yml` | English local preview | (inherited) |
| `mkdocs_for_kb_import_ru.yml` | **Do not serve** — use `mkdocs build` for PHPKB HTML export | `for_kb_import_ru/` |

Match the config to the **platform branch** you are on (`platform_v5` → v5 URLs in YAML; `platform_v6` → v6).

### Common commands

**Full Russian help (default):**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve
```

```bash
.venv/bin/python -m mkdocs serve
```

**Explicit complete nav:**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_guide_complete_ru.yml
```

```bash
.venv/bin/python -m mkdocs serve -f mkdocs_guide_complete_ru.yml
```

**User guide only:**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_guide_user_ru.yml
```

```bash
.venv/bin/python -m mkdocs serve -f mkdocs_guide_user_ru.yml
```

**English:**

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve -f mkdocs_en_local.yml
```

```bash
.venv/bin/python -m mkdocs serve -f mkdocs_en_local.yml
```

**Different host/port** (e.g. when 8000 is busy):

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve --dev-addr 127.0.0.1:8001
```

```bash
.venv/bin/python -m mkdocs serve --dev-addr 127.0.0.1:8001
```

**Strict mode** (fail on broken links — useful before a large publish):

```powershell
.\.venv\Scripts\python.exe -m mkdocs serve --strict
```

```bash
.venv/bin/python -m mkdocs serve --strict
```

Stop the server with `Ctrl+C`. Preview uses web theme (`overrides/`), not PHPKB export HTML (`overrides_for_kb_import/`).


## JSON mapping files

Several **JSON maps** in the repo root (and a few under `docs/ru/`) tie PHPKB database IDs to stable local filenames or record clone migrations. They are git-tracked; commit them when import or clone scripts update them.

### Article / category maps (`--article-map`)

Used by **`phpkb_import.py`**, **`phpkb_import_for_rag.py`**, and related import scripts. **Required** via `--article-map` on every import run.

| File | Platform | Purpose |
| --- | --- | --- |
| `.article_id_filename_map_v5.json` | v5.0 (category `798`) | PHPKB article ID → filename stem; category ID → folder slug under `phpkb_content*` |
| `.article_id_filename_map_v6.json` | v6.0 (category `896`) | Same for v6 |
| `.article_id_filename_map_v4.7.json` | v4.7 | Legacy v4.7 import |
| `.article_id_filename_map_v4_cmw_lab.json` | CMW Lab | Used by `phpkb_import_cmw_lab.py` → `phpkb_content_cmw_lab/` |

Structure (simplified):

```json
{
  "Articles": {
    "5451": "script_keys",
    "5558": "deploy_linux"
  },
  "Categories": {
    "896": "platform_v6",
    "914": "general"
  }
}
```

**Why it exists:**

- PHPKB article titles change; filenames must stay **stable** across re-imports (`5451-script_keys.md`, not `5451-New Title.md` every time).
- Import scripts **gap-fill** the map: known IDs reuse existing stems; new IDs get new stems and the file is updated.
- Maps align imported trees with **`docs/ru/`** naming where articles were authored in MkDocs first.

**Operator actions:**

- Always pass the map matching your `--category-id` / platform branch (v5 file on `platform_v5`, v6 on `platform_v6`).
- After full import, commit the updated map if the script added entries.
- Do not hand-edit unless you know the ID ↔ stem relationship; prefer fixing `docs/ru/` and re-importing.

### Clone migration maps (`--mapping`)

Used by **`utilities/phpkb_cloning/phpkb_clone.py`** and post-clone scripts (`phpkb_clone_update_links.py`, `phpkb_clone_update_mapped_ids.py`, rollback). **Required** via `--mapping`.

| File | Purpose | Lifetime |
| --- | --- | --- |
| `.v5mapping.json`, `.v6mapping.json`, `.v6.5mapping.json`, … | Records **old PHPKB ID → new PHPKB ID** after category/article clone for a **version migration** | **Permanent** repo artifacts — commit and keep for years |
| `.scratch/<purpose>_mapping.json` | One-off article clone / publish experiment | Disposable (gitignored) |

Clone maps differ from article maps: they track **DB row remapping** during cloning, not filename stems for import.

See `.agents/skills/phpkb-cloning/SKILL.md` for workflow. **Never mix** a migration map (`.v6mapping.json`) with a one-off `.scratch/` map.

### Other JSON in the repo

| Location | Purpose |
| --- | --- |
| `docs/ru/tutorials/**/.taxonomies/*.json` | Tutorial course structure (lessons, taxonomies) — not PHPKB import maps |
| `scraping/*/progress_*.json`, `sanitize_checkpoint.json` | Web scrape resume checkpoints |
| `for_kb_import_ru/**/comindware_default_mapping.json` | Asset metadata in export tree — not repo-root article maps |


## MkDocs configuration files

Configs use MkDocs **YAML inheritance** (`INHERIT:`) — child files inherit the parent config and override selected keys. Most settings live in `mkdocs_common.yml`; language- and purpose-specific files inherit and override on top.

### Inheritance chain

```
mkdocs_common.yml          ← shared theme, plugins, extra placeholders, PDF defaults
    └── mkdocs_ru.yml      ← Russian docs_dir, KB URLs, publication date
            ├── mkdocs_guide_*_ru.yml      ← per-guide nav + guide flags (userGuide, apiGuide, …)
            │       └── mkdocs_guide_*_ru_pdf.yml   ← PDF build overrides
            ├── mkdocs_guide_complete_ru.yml        ← full nav for local preview
            ├── mkdocs_for_kb_import_ru.yml           ← PHPKB HTML export
            └── mkdocs_ru_local_files.yml           ← local file:// links
mkdocs.yml                 ← INHERIT: mkdocs_guide_complete_ru.yml (default `mkdocs serve`)
mkdocs_en.yml / mkdocs_en_local.yml                 ← English variants
```

### YAML inheritance approach

MkDocs configs in this repo use **inheritance** (`INHERIT:`) — one shared base, small purpose-specific overrides in child files:

1. **`mkdocs_common.yml`** — single source for theme (Material), plugins (`search`, `macros`, `minify`, …), markdown extensions, and **`extra:` product placeholders** (`productName`, `companyName`, …). Rarely run directly.

2. **`mkdocs_ru.yml`** — `INHERIT: mkdocs_common.yml` plus Russian `docs_dir: docs/ru`, default `site_dir: compiled_help`, KB URL prefixes in `extra`, PDF plugin defaults.

3. **Purpose configs** — `INHERIT: mkdocs_ru.yml` (or `mkdocs_en.yml`) and override only what differs:

   | Override kind | Typical keys | Example file |
   | --- | --- | --- |
   | Output directory | `site_dir` | `for_kb_import_ru` in `mkdocs_for_kb_import_ru.yml` |
   | Public URL base | `site_url` | `https://kb.comindware.ru/platform/v5.0/` (must match platform branch) |
   | Theme template dir | `theme.custom_dir` | `overrides_for_kb_import/` for PHPKB HTML |
   | Build flags | `extra.userGuide`, `extra.kbExport`, `extra.pdfOutput`, … | Each `mkdocs_guide_*_ru.yml` |
   | Navigation | `nav:` | Subset of pages per guide (user, admin, API, …) |
   | Post-process | `hooks:` | `kb_html_cleanup_hook.py` on PHPKB export only |
   | Exclude files | `exclude_docs:` | Skip `AGENTS.md` from PHPKB export |

4. **PDF configs** — `mkdocs_guide_*_ru_pdf.yml` inherit the matching guide YAML and set `extra.pdfOutput: true`, `plugins.with-pdf`, `site_dir: pdf/`.

5. **Entry point** — root `mkdocs.yml` is only `INHERIT: mkdocs_guide_complete_ru.yml` so bare `mkdocs serve` opens the **full** Russian nav.

**Rules of thumb:**

- Put shared settings in **`mkdocs_common.yml`** once; do not duplicate plugins across guide files.
- Pick the **leaf config** matching your task (`-f mkdocs_for_kb_import_ru.yml` for PHPKB, `-f mkdocs_guide_user_ru.yml` for user-guide web build, `*_pdf.yml` for PDF).
- **`extra` booleans drive Jinja** in articles (`{% if userGuide %}`, `{% if kbExport %}`, …) — see [Jinja templating basics](#jinja-templating-basics).
- On **`platform_v5` vs `platform_v6`**, check `site_url` and `productVersion` in the active **YAML inheritance chain** match the target KB version.

Minimal examples:

```yaml
# mkdocs_for_kb_import_ru.yml — export-only overrides
INHERIT: mkdocs_ru.yml
site_url: https://kb.comindware.ru/platform/v5.0/
site_dir: for_kb_import_ru
use_directory_urls: false
theme:
  custom_dir: overrides_for_kb_import
extra:
  kbExport: true
hooks:
  - kb_html_cleanup_hook.py
```

```yaml
# mkdocs_guide_user_ru.yml — subset nav + flags
INHERIT: mkdocs_ru.yml
extra:
  userGuide: true
  completeGuide: false
  apiGuide: false
nav:
  - Общие сведения: …
  - Использование системы: …
```

### Config reference

| File | Purpose | `site_dir` | Command |
| --- | --- | --- | --- |
| `mkdocs.yml` | Default local preview (complete Russian nav) | `compiled_help` | `mkdocs serve` |
| `mkdocs_guide_complete_ru.yml` | Full Russian help nav for authoring | (inherited) | `mkdocs serve -f mkdocs_guide_complete_ru.yml` |
| `mkdocs_guide_user_ru.yml` | User guide subset | (inherited) | `mkdocs build -f mkdocs_guide_user_ru.yml` |
| `mkdocs_guide_*_ru.yml` | Other guide subsets (admin, API, developer, AI) | (inherited) | `-f mkdocs_guide_<name>_ru.yml` |
| `mkdocs_for_kb_import_ru.yml` | PHPKB-compatible HTML export | `for_kb_import_ru` | `mkdocs build -f mkdocs_for_kb_import_ru.yml` |
| `mkdocs_for_kb_import_ru_v4.7.yml` | PHPKB export for v4.7 | `for_kb_import_ru` | same pattern |
| `mkdocs_for_kb_import_en.yml` | English PHPKB export | `for_kb_import_en` | same pattern |
| `mkdocs_guide_*_ru_pdf.yml` | PDF guide build | `pdf/` | see [Build PDF guides](#build-pdf-guides) |
| `mkdocs_guide_*_ru_pdf_gostech.yml` | PDF with ГосТех terminology overrides | `pdf/` | inherits corresponding `*_pdf.yml` |
| `mkdocs_en_local.yml` | English local preview | (inherited) | `mkdocs serve -f mkdocs_en_local.yml` |

### Guide flags (`extra` section)

Each `mkdocs_guide_*_ru.yml` sets boolean flags that Jinja conditionals use to include or exclude content:

| Flag | Typical guide |
| --- | --- |
| `userGuide` | User guide |
| `adminGuideWindows` / `adminGuideLinux` | Admin guides |
| `apiGuide` | API guide |
| `developerGuide` | Developer guide |
| `aiGuide` | AI guide |
| `completeGuide` | Complete / local preview |
| `tutorial` | Tutorial sections |
| `kbExport` | PHPKB HTML export (`mkdocs_for_kb_import_ru.yml`) |
| `pdfOutput` | PDF build (`mkdocs_guide_*_ru_pdf.yml`) |
| `gostech` | ГосТех PDF variants (`*_pdf_gostech.yml`) |

Product and brand placeholders (`productName`, `companyName`, `nginxVariants`, etc.) are defined in `mkdocs_common.yml` `extra:` and can be overridden per config (for example ГосТех renames `nginxVariants` to «Сервис IAM Proxy»).

### Snippets path

`pymdownx.snippets` in `mkdocs_common.yml` sets `base_path: docs/ru/.snippets/` — reusable includes live there (`hyperlinks_mkdocs_to_kb_map.md`, `pdfPageBreakHard.md`, etc.).


## Repository scripts

Scripts live in the repository root unless noted. Run from repo root: `.\.venv\Scripts\python.exe <script>.py` (Windows) or `.venv/bin/python <script>.py` (WSL/Linux). With venv activated: `python <script>.py`.

### MkDocs build

| Script | Purpose |
| --- | --- |
| `buildhelp.py` | Build compiled web help into `compiled_help/` (uses `mkdocs_ru.yml`) |
| `pdf_build_guides.py` | Batch-build all standard PDF configs sequentially; writes `build_log.txt` |
| `pdf_duplicate_with_date.py` | Copy PDFs from repo root to `PDF_DATED_DIR` with `YYYY.MM.DD` suffix |
| `install/deploy_venv.py` | Create `.venv` and install `install/requirements.txt` |

### PHPKB publish and import

| Script | Purpose |
| --- | --- |
| `phpkb_update_articles.py` | Push `for_kb_import_ru/` HTML into PHPKB DB |
| `phpkb_import.py` | Pull PHPKB → `phpkb_content/` |
| `phpkb_import_for_rag.py` | Pull PHPKB → `phpkb_content_rag/` |
| `phpkb_ingest.py` | Bundle RAG tree → LLM ingestion file |
| `phpkb_ingest_cmw_lab.py` | Same for CMW Lab / v4 (`kb.cmwlab.com.platform_v4_for_llm_ingestion.md`) |
| `phpkb_import_cmw_lab.py` | Pull PHPKB → `phpkb_content_cmw_lab/` |
| `phpkb_copy_images.py` | Copy images from export → PHPKB assets repo |
| `phpkb_replace_related_topics.py` | Batch-update PHPKB related-topics markup |
| `phpkb_update_article_ids.py` | Migrate article IDs in local files |

### PHPKB cloning (`utilities/phpkb_cloning/`)

| Script | Purpose |
| --- | --- |
| `phpkb_clone.py` | Clone PHPKB categories/articles in DB |
| `phpkb_clone_update_links.py` | Rewrite links after cloning |
| `phpkb_clone_update_mapped_ids.py` | Update `kbId` in `docs/ru/` and hyperlink map |
| `phpkb_clone_rollback.py` | Roll back a bad clone |

### Shared utilities

| Script | Purpose |
| --- | --- |
| `tools/ssh_kb_ru.py` | SSH tunnel + MySQL connection to PHPKB |
| `utilities/git_sync.py` | Commit/push in PHPKB assets repo (`--git` flag) |
| `utilities/ssh_pull.py` | Remote `git pull` on production (`--pull` flag) |
| `kb_html_cleanup_hook.py` | MkDocs `on_post_page` hook for PHPKB HTML (not a CLI script) |

**Web scraping** (`.agents/skills/scrape-sanitize/scripts/`): `crawl4ai_ingest.py`, `sanitize.py` — see [Web scraping for LLM ingestion](#web-scraping-for-llm-ingestion).

Obsolete scripts are in `.legacy/` — do not use them for current workflows.


## Theme overrides

MkDocs Material theme templates can be overridden by placing files under `theme.custom_dir`. This repo has two override trees:

| Directory | Used by | Purpose |
| --- | --- | --- |
| `overrides/` | `mkdocs_common.yml` → most builds | Web help: logo, CSS, footer, `kbUrl` meta tag |
| `overrides_for_kb_import/` | `mkdocs_for_kb_import_ru.yml` | PHPKB export: stripped-down HTML, PHPKB-specific CSS |

### Key override files

| File | Role |
| --- | --- |
| `overrides/main.html` | Extends Material `base.html`; adds `<meta property="kbUrl" …>` when `page.meta.kbId` is set |
| `overrides/partials/copyright.html` | Footer copyright line |
| `overrides/assets/stylesheets/extra.css` | Comindware brand styles for web help |
| `overrides_for_kb_import/base.html` | Full base template for PHPKB export (no Material chrome) |
| `overrides_for_kb_import/assets/stylesheets/extra.css` | PHPKB-compatible notice/admonition styles |
| `overrides_for_kb_import/partials/toc.html` | Table of contents for export |

Override files use **Jinja2** syntax (`{% extends %}`, `{% block %}`, `{{ config.extra… }}`). Edit overrides only when changing HTML structure or global styling — article content stays in `docs/ru/`.

### PDF templates

`pdf_templates/` holds WeasyPrint templates for `mkdocs-with-pdf`:

| File | Role |
| --- | --- |
| `cover.html.j2` | PDF cover page (logo, `productName`, `productVersion`, `cover_subtitle`) |
| `styles.scss` | PDF-specific print styles |

`mkdocs_common.yml` sets `plugins.with-pdf.custom_template_path: pdf_templates`.


## Jinja templating basics

Build-time templating for articles — wording and link rules: [`AGENTS.md`](AGENTS.md) · [Content editing standards](#content-editing-standards). MkDocs processes Markdown through Jinja2; the `mkdocs-macros` plugin (`plugins.macros` in `mkdocs_common.yml`) exposes `config.extra` values as template variables.

### Product placeholders

In article Markdown, use **double curly braces** for values from `mkdocs_common.yml` `extra:`:

```markdown
**{{ productName }}** allows you to configure templates.
```

Common placeholders: `{{ productName }}`, `{{ companyName }}`, `{{ productNameMobile }}`, `{{ nginxVariants }}`, `{{ openSearchVariants }}`.

Rules:

- No spaces inside names — `{{ product Name }}` is a syntax error.
- Format product names in bold: `**{{ productName }}**`.
- Placeholders are resolved at build time, not in the source editor.

### Conditional content

Wrap optional blocks in `{% if … %} … {% endif %}` to show content only for certain builds:

```markdown
{% if pdfOutput %}
<p class="pdfEndOfBlockHack pageBreakAfter">.</p>
{% endif %}
```

```markdown
{% if adminGuideLinux %}
Linux-specific deployment steps…
{% endif %}
```

```markdown
{% if (not gostech) or adminGuideWindows or completeGuide or kbExport %}
Windows IIS configuration…
{% endif %}
```

Typical condition variables: `pdfOutput`, `kbExport`, `userGuide`, `adminGuideLinux`, `adminGuideWindows`, `apiGuide`, `developerGuide`, `completeGuide`, `gostech`.

### Include snippets

Reusable fragments live in `docs/ru/.snippets/`.

**Hyperlink map (required at end of every article):**

```markdown
{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
```

Include on **every** article under `docs/` so any existing or future `[link title][anchor_name]` resolves at build time — via **`mkdocs-autorefs`** or the **hyperlink map**, whichever is appropriate (see [`AGENTS.md` → Link formatting](AGENTS.md#link-formatting)):

1. **`mkdocs-autorefs`** — target article is in the **current build** (`nav:` of the active YAML) → internal cross-reference to `{: #anchor }` (HTML/PDF).
2. **Hyperlink map** — hub-backed URL (third-party, KB site, out-of-nav fallback, PHPKB export); conditionals (`userGuide`, `adminGuideLinux`, `kbExport`, …) match active `extra:` flags.

The map is the central **named-anchor** hub (portability, deduplication, versioning via `kbArticleURLPrefix`). Authors write one reference syntax; the build chooses autorefs vs map.

### Link references in articles

| Scope | Syntax | Where target is defined |
| --- | --- | --- |
| **Same article** (heading on this page) | `[title](#anchor_name)` | Heading `{: #anchor_name }` in this file |
| **Cross-article / KB / third-party** | `[title][anchor_name]` | Named anchor in hyperlink map, or `autorefs` if in-build |

- **In-page:** `#anchor_name` only — not in the map.
- **Cross-article:** `[title][anchor_name]` — hub entry and/or `autorefs`; never inline URLs or `path.md` in article Markdown.

### PDF page breaks

Include the hard page-break snippet where a PDF must start a new page:

```markdown
{% include-markdown ".snippets/pdfPageBreakHard.md" %}
```

That snippet renders a break only when `pdfOutput` is `true`.


## Build PDF guides

PDF output uses the `mkdocs-with-pdf` plugin (WeasyPrint). See `.agents/skills/mkdocs-pdf-build/SKILL.md` for the full Windows GTK3 playbook.

### One-time GTK3 setup (Windows)

1. Install GTK3 runtime: run `install\gtk3-runtime-…-win64.exe` (or `install\installgtk3.ps1`).
2. Persist environment variables:

```powershell
[Environment]::SetEnvironmentVariable(
  "WEASYPRINT_DLL_DIRECTORIES",
  "C:\Program Files\GTK3-Runtime Win64\bin", "User")
$gtk = "C:\Program Files\GTK3-Runtime Win64\bin"
$cur = [Environment]::GetEnvironmentVariable("PATH", "User")
[Environment]::SetEnvironmentVariable("PATH", "$gtk;$cur", "User")
```

_WSL / Linux / macOS:_ GTK3/WeasyPrint setup — `.agents/skills/mkdocs-pdf-build/SKILL.md` (not the Windows installer above)._


3. Verify:

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe -c "import weasyprint; print(weasyprint.__version__)"
```

_WSL / Linux / macOS:_ GTK3/WeasyPrint setup — `.agents/skills/mkdocs-pdf-build/SKILL.md` (not the Windows installer above)._


### Build a single PDF

Each `mkdocs_guide_*_ru_pdf.yml` inherits the corresponding guide config and sets `extra.pdfOutput: true`, `site_dir: pdf/`, and `with-pdf.output_path` to a filename in the **repo root**.

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_guide_user_ru_pdf.yml --clean
```

```bash
# After GTK3/WeasyPrint setup — see .agents/skills/mkdocs-pdf-build/SKILL.md
.venv/bin/python -m mkdocs build -f mkdocs_guide_user_ru_pdf.yml --clean
```


| Config | Output PDF (repo root) |
| --- | --- |
| `mkdocs_guide_user_ru_pdf.yml` | `Comindware Platform 5.0. Руководство пользователя.pdf` |
| `mkdocs_guide_admin_windows_ru_pdf.yml` | Admin guide (Windows) |
| `mkdocs_guide_admin_linux_ru_pdf.yml` | Admin guide (Linux) |
| `mkdocs_guide_api_ru_pdf.yml` | API guide |
| `mkdocs_guide_developer_ru_pdf.yml` | Developer guide |
| `mkdocs_guide_ai_ru_pdf.yml` | AI guide |
| `mkdocs_guide_complete_ru_pdf.yml` | Complete guide |
| `mkdocs_guide_*_ru_pdf_gostech.yml` | ГосТех variants (inherits `*_pdf.yml`, sets `gostech: true`) |

PDF configs also set `glightbox.manual: true` and `minify.minify_html: false` to avoid breaking print layout.

### Batch-build all standard PDFs

```powershell
$env:PATH = "C:\Program Files\GTK3-Runtime Win64\bin;$env:PATH"
$env:WEASYPRINT_DLL_DIRECTORIES = "C:\Program Files\GTK3-Runtime Win64\bin"
.\.venv\Scripts\python.exe pdf_build_guides.py
```

```bash
.venv/bin/python pdf_build_guides.py
```

Builds, in order: complete → user → developer → admin Linux → admin Windows → API. Summary and per-config timing go to `build_log.txt`.

### Dated PDF copies

After building, archive dated copies (uses `PDF_DATED_DIR` from `.env`):

```powershell
.\.venv\Scripts\python.exe pdf_duplicate_with_date.py
```

```bash
.venv/bin/python pdf_duplicate_with_date.py
```

Produces `original_name.YYYY.MM.DD.pdf` in the target directory.

### Mermaid in PDF

WeasyPrint does not run JavaScript. Mermaid diagrams must be pre-rendered — see [Mermaid diagram support in PDF](#mermaid-diagram-support-in-pdf) below.

### PDF troubleshooting

| Symptom | Fix |
| --- | --- |
| `OSError: cannot load library` on `import weasyprint` | GTK3 not installed or not on `PATH` |
| 0-byte PDF / silent failure mid-render | Same — check GTK3 env vars in the current shell |
| Cyrillic shows as boxes | Set `WEASYPRINT_DLL_DIRECTORIES` |
| `Could not find cross-reference target` | Usually non-fatal; missing anchor in another article |
| `render_js: true` | **Does not work** — use `mkdocs-mermaid-to-svg` + `mmdc` instead |


## MkDocs build hooks

MkDocs supports Python hook modules listed under `hooks:` in the YAML config. This is separate from Git hooks (see next section).

### `kb_html_cleanup_hook.py`

Registered in `mkdocs_for_kb_import_ru.yml` (and English/v4.7 variants). Runs `on_post_page` after each page is rendered — transforms HTML for PHPKB compatibility:

- Maps Material admonition classes → PHPKB `notice-*` classes
- Removes redundant `<h1>` (PHPKB provides its own title)
- Strips HTML comments, empty `<p>` tags
- Adds `class="mkdocs_imported_link"` to links
- Rewrites `<pre>` blocks for PHPKB code display
- Replaces `<body>` with `<div class="md-body" kb-id="…" kb-title="…">` using page frontmatter
- Fixes relative image paths for PHPKB asset hosting

**When it runs:** only during `mkdocs build -f mkdocs_for_kb_import_ru.yml` (or `_en`, `_v4.7`). Not used for web preview or PDF builds.

`kb_html_cleanup_hook_v4.7.py` is the v4.7-specific variant.


## Git hooks

Repository-local Git hooks live in `.githooks/`. Enable once per clone:

```powershell
git config core.hooksPath .githooks
```

See `.gitconfig-hooks.md` for the same instruction.

| Hook | Trigger | Action |
| --- | --- | --- |
| `prepare-commit-msg` | Before commit message editor opens | Prepends `[#XXXXX]` from branch name or recent commits if missing |
| `commit-msg` | After message written | Warns if message does not match `[#XXXXX] …` format (does not block) |
| `pre-push` | Before push | Git LFS pre-push |
| `post-commit` | After commit | Git LFS post-commit |
| `post-merge` | After merge | Git LFS post-merge |
| `post-checkout` | After checkout | Git LFS post-checkout |

Commit message format: `[#XXXXX] Imperative description`. See `.agents/skills/cmwhelp-commit/SKILL.md`.

Git LFS hooks require `git-lfs` on `PATH`. Install Git LFS or remove the LFS hooks if you do not use LFS.


## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `import mkdocs` fails | Broken venv | `install/deploy_venv.py` or `python-env-setup` skill |
| Publish fails / no SSH | Missing `.env` or VPN | Check `SERVER_PROFILE`, `CMW_SSH_*`, `CMW_SQL_*` |
| `CMW_KB_REPO_PATH not set` | `.env` incomplete | Set path to PHPKB assets repo checkout |
| `phpkb_copy_images.py: --version required` | Old command without version | Add `--version v5.0` or `v6.0` |
| Import script errors on start | Missing `--article-map` | Pass `.article_id_filename_map_v5.json` or `_v6.json` |
| Import hangs then times out | Normal for full category | Wait for `Import finished. Total articles imported:` |
| Bundle has stale content | Skipped RAG import | Run `phpkb_import_for_rag.py` before `phpkb_ingest.py` |
| Images not on production | Pushed but not pulled | Run with `--pull` or SSH `git pull` manually |
| `kb-id=""` in HTML | No `kbId:` in frontmatter | Add `kbId:` or clone a new PHPKB article |
| PDF 0 bytes / WeasyPrint error | GTK3 not on PATH | [Build PDF guides](#build-pdf-guides) → GTK3 setup |
| `{{ product Name }}` in article | Space in macro name | Use `{{ productName }}` (no spaces) |
| Jinja block visible in PHPKB HTML | Wrong `{% if %}` flag | Check `kbExport` / guide flags in the active config |
| PHPKB HTML has Material classes | Wrong build config | Use `mkdocs_for_kb_import_ru.yml`, not `mkdocs_ru.yml` |
| Sanitize: input file not found | Wrong `--date` or crawl not run | Match `--date` to crawl; check `.scratch/{site}_dirty_*.md` |
| Crawl stalls / timeouts | Network or site rate limits | Re-run (resumes from `progress_*.json`); check `.scratch/ralph/*_failures.log` |
| Publish: "Found content" but no update | `kbId:` mismatch | Frontmatter `kbId:` must match PHPKB article |
| Publish: SSH connection refused | VPN / credentials | Check `.env`, `SERVER_PROFILE`, SSH key |
| Image sync: path not set | `.env` incomplete | Set `CMW_KB_REPO_PATH`, `CMW_SSH_*` |


## Mermaid diagram support in PDF

PDF generation uses WeasyPrint which does not execute JavaScript, so Mermaid diagrams require pre-rendering to static images.

### Recommended approach: `mkdocs-mermaid-to-svg` + `mmdc`

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

#### How it works

1. `mkdocs-mermaid-to-svg` scans markdown files for mermaid code blocks
2. Each diagram is rendered to SVG via `mmdc`
3. SVG files are saved to `_mermaid_assets/`
4. Original mermaid blocks are replaced with `<img>` tags pointing to SVGs
5. WeasyPrint includes the SVGs in the final PDF

### Alternative: `render_js: true` (does NOT work)

The `with-pdf` plugin has a `render_js: true` option that attempts to use Headless Chrome. **This does not work** with current versions due to a bug in `mkdocs-with-pdf` v0.9.3:

```
AttributeError: property 'text' of 'Tag' object has no setter
```

**Conclusion:** Use `mkdocs-mermaid-to-svg` + `mmdc` — it's the only working approach for Mermaid in PDF.


## Agent skills (reference)

End-to-end task playbooks live in `.agents/skills/<name>/SKILL.md`. **AI agents:** use the skills index in [`AGENTS.md`](AGENTS.md) — load a skill when its description matches the task.

Humans: browse skills as extended playbooks, or use the [Content editing standards](#content-editing-standards) index and [`AGENTS.md` → Human operators cross-reference](AGENTS.md#human-operators--readme-cross-reference) to jump between article rules and workflow sections.

| Task | Skill |
| --- | --- |
| Edit article → rebuild → publish → commit | `kb-edit-publish` |
| RAG import + LLM bundle | `phpkb-ingestion` |
| PDF build on Windows | `mkdocs-pdf-build` |
| PHPKB clone / new article | `phpkb-cloning` |
| Fix venv / plugin imports | `python-env-setup` |
| Crawl & sanitize public websites | `scrape-sanitize` |

Full list: [`AGENTS.md` → Skills Reference](AGENTS.md#skills-reference).


## Git remotes and branches

This repo tracks **platform lines** as long-lived branches. Your clone may define several remotes (names vary by setup):

| Remote | Typical URL | Role |
| --- | --- | --- |
| `origin` | `https://github.com/<user-or-org>/cbap-mkdocs-ru.git` | Default fetch/push remote |
| `github` | `https://github.com/arterm-sedov/cbap-mkdocs-ru.git` | Personal fork (optional) |
| `github-cmw-team` | `https://github.com/cmw-team/cbap-mkdocs-ru.git` | Team org repo (optional) |
| `gitverse` | `https://gitverse.ru/arterm-sedov/cbap-mkdocs-ru.git` | GitVerse mirror (optional) |

Some clones configure `origin` with **multiple push URLs** (GitHub + GitVerse). Inspect without exposing credentials:

```bash
git remote -v
git remote show origin
```

**Main branches:**

| Branch | Platform KB | PHPKB category | Notes |
| --- | --- | --- | --- |
| `platform_v5` | v5.0 | `798` | `site_url` …/v5.0/ in import YAML |
| `platform_v6` | v6.0 | `896` | `site_url` …/v6.0/ in import YAML |
| `master` | — | — | Integration / default on some remotes |
| `<ticket>_<topic>` | — | — | Short-lived feature branches off `platform_v5` or `platform_v6` |

Ticket branches (e.g. `10291999_scripts_keys`) are usually merged back into the matching platform branch via pull request.

**Never commit:** `.env`, SSH keys, passwords, or machine-specific absolute paths. Paths like `CMW_KB_REPO_PATH` belong only in `.env` (gitignored).


## Daily Git workflow (platform_v5 / platform_v6)

### Start of day

```bash
git fetch --all --prune
git status
git branch -vv
```

Switch to the platform branch you are editing (v5 or v6):

```bash
# v6 documentation
git switch platform_v6
git pull origin platform_v6

# or v5
git switch platform_v5
git pull origin platform_v5
```

On Windows PowerShell, `git switch` / `git pull` are the same.

### Feature branch (ticket work)

```bash
git switch platform_v6
git pull origin platform_v6
git switch -c 10291999_scripts_keys

# … edit docs/ru/, build, publish …

git add docs/ru/ for_kb_import_ru/
git commit -m "[#10291999] Update script keys article"
git push -u origin HEAD
```

Open a PR into `platform_v6` (or `platform_v5`) — see [GitHub CLI](#github-cli-gh).

### After merge — update local platform branch

```bash
git switch platform_v6
git pull origin platform_v6
```

### Push to team remote (if configured)

```bash
git push origin platform_v6
git push github-cmw-team platform_v6
```

Use only remotes that exist in your clone (`git remote`).


## Merge and cherry-pick between platform versions

Rules also in [`AGENTS.md`](AGENTS.md). **Cherry-pick** = replay individual commits; **merge** = integrate a whole branch.

**Commit separation:** on the same platform branch, use **separate commits** for (1) **`docs/ru/`**, (2) **`for_kb_import_ru/`**, (3) **`phpkb_content/`**, (4) **`phpkb_content_rag/`**, (5) **`kb.comindware.ru.platform_v*_for_llm_ingestion.md`** — never combine 3–5 in one commit — so cross-version cherry-pick can take article commits only and rebuild the rest on the target branch.

### Cherry-pick vs rebuild

Not every git-tracked tree behaves the same when moving commits between `platform_v5` and `platform_v6`.

| Path | Cherry-pick between platform branches? | Why | On target branch instead |
| --- | --- | --- | --- |
| `docs/ru/` | **Yes** (both directions) | Source Markdown — fix `kbId:` and hyperlinks map on v5 | Review diff; restore v5 `kbId:` if needed |
| `for_kb_import_ru/` | **No** | Branch-specific export HTML (`kb-id`, `site_url`, theme) | `mkdocs build -f mkdocs_for_kb_import_ru.yml`, commit |
| `phpkb_content/798-platform_v5/`, `phpkb_content_rag/798-platform_v5/`, `kb.comindware.ru.platform_v5_for_llm_ingestion.md` | **Yes — v5 → v6 only** | v5 DB snapshot + v5 LLM bundle mirrored on `platform_v6` | Rarely needs action on v6 |
| `phpkb_content/896-platform_v6/`, `phpkb_content_rag/896-platform_v6/`, `kb.comindware.ru.platform_v6_for_llm_ingestion.md` | **No — never to v5** | v6 `kbId`s must not land on `platform_v5` | Re-import on `platform_v6` only |
| `phpkb_content_cmw_lab/` | **Yes** (Lab / v4; outside v5↔v6 rule) | Separate CMW Lab import tree | `phpkb_import_cmw_lab.py` if DB changed |
| Current-version trees on **own** branch (`798-*` on v5, `896-*` on v6) | **No** (cross-version) | Tied to that branch’s DB IDs | `phpkb_import*.py` on that branch |

**Rule of thumb:** cherry-pick **`docs/ru/`** in either direction (fix v5 `kbId:`); cherry-pick **v5 import trees + v5 LLM bundle only onto `platform_v6`**; **never** cherry-pick v6 import artifacts onto v5; **never** cherry-pick `for_kb_import_ru/`; **rebuild** each branch’s current-version `phpkb_content*` locally.

After cherry-picking article commits, always regenerate export:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
git add for_kb_import_ru/
git commit -m "[#<ticket>] Rebuild PHPKB export after cherry-pick"
```

```bash
.venv/bin/python -m mkdocs build -f mkdocs_for_kb_import_ru.yml
git add for_kb_import_ru/
git commit -m "[#<ticket>] Rebuild PHPKB export after cherry-pick"
```

### Safety rules

**Articles (`docs/ru/`) — both directions:**

- **Never bring v6 `kbId:` into v5 articles.** Restore v5 values: `git show platform_v5:docs/ru/<path>.md`
- **Keep `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` at the target branch version** — v6 ID mappings break v5 links.
- **Cherry-pick is unsafe if `kbId` changed or a new article was created** — verify after every cross-version pick.

**Export HTML — neither direction:**

- **Verify `site_url` in `mkdocs_for_kb_import_ru.yml`** matches target (`v5.0/` vs `v6.0/`).
- **Do not cherry-pick `for_kb_import_ru/`** — rebuild with `mkdocs build -f mkdocs_for_kb_import_ru.yml` on the target branch.

**Import trees and LLM bundles — asymmetric (v5 → v6 only):**

- **Onto `platform_v6`:** cherry-pick commits touching `phpkb_content/798-platform_v5/`, `phpkb_content_rag/798-platform_v5/`, and/or `kb.comindware.ru.platform_v5_for_llm_ingestion.md`.
- **Onto `platform_v5`:** **never** cherry-pick v6 import trees or `kb.comindware.ru.platform_v6_for_llm_ingestion.md` — re-import on `platform_v6` instead.
- **On either branch:** rebuild that branch’s **current-version** trees (`798-*` on v5, `896-*` on v6) locally; do not cherry-pick them across versions.

**Workflow / docs — both directions:**

- **Safe:** `.agents/skills/*`, `AGENTS.md`, `discovery_log.md`, `readme.md`, `readme-ru.md`.
- **Avoid `toc_depth` changes** unless required — massive HTML churn.

### Cherry-pick one commit (v6 → v5 example)

```bash
git switch platform_v5
git pull origin platform_v5
git log platform_v6 --oneline -5          # find commit SHA
git cherry-pick <commit-sha>
```

If the commit is empty on v5 (already applied):

```bash
git cherry-pick --skip
```

If conflicts — resolve, then:

```bash
git add <resolved-files>
git cherry-pick --continue
```

Abort:

```bash
git cherry-pick --abort
```

### Restore v5 `kbId:` after a bad cherry-pick

```bash
git show platform_v5:docs/ru/administration/deploy/script_keys.md > .scratch/kbId-restore.md
# Copy kbId: line from .scratch/kbId-restore.md into the working file, then:
git add docs/ru/administration/deploy/script_keys.md
git commit -m "[#<ticket>] Restore v5 kbId after cherry-pick"
```

Or restore the whole file from the v5 branch (overwrites local edits in that file):

```bash
git restore --source=platform_v5 -- docs/ru/administration/deploy/script_keys.md
```

### Merge platform branch (less common)

Integrate all of `platform_v6` into `platform_v5` (or the reverse) only when explicitly planned:

```bash
git switch platform_v5
git pull origin platform_v5
git merge origin/platform_v6
# resolve conflicts; re-check kbId, hyperlinks map, site_url
git commit   # if merge commit not auto-created
git push origin platform_v5
```

Prefer **cherry-pick of doc-only commits** over full branch merges when possible.

### Drop a bad commit from branch tip

```bash
git rebase --onto <good-commit> <bad-commit> HEAD
```

### Empty cherry-pick

```bash
git cherry-pick --skip
```


## GitHub CLI (`gh`)

Install: https://cli.github.com/ — authenticate once per machine (`gh auth login`). No tokens or passwords belong in the repo.

### Status and repo

```bash
gh auth status
gh repo view
gh repo view --web
```

### Pull requests

```bash
gh pr list
gh pr list --base platform_v6
gh pr view 123
gh pr view 123 --web
gh pr checks 123
gh pr checkout 123
```

Create a PR after pushing a feature branch:

```bash
git push -u origin HEAD
gh pr create --base platform_v6 --title "[#10291999] Update script keys article" --body "## Summary
- Updated script keys article

## Test plan
- [ ] mkdocs serve
- [ ] mkdocs build -f mkdocs_for_kb_import_ru.yml
- [ ] Published to PHPKB"
```

### Issues and CI

```bash
gh issue list
gh issue view 10291999
gh run list --limit 5
gh run view <run-id> --log-failed
```

### Fork / team remote workflow

If you push to a personal fork and open PRs against `cmw-team/cbap-mkdocs-ru`:

```bash
gh pr create --repo cmw-team/cbap-mkdocs-ru --base platform_v6 --head <your-user>:<branch>
```


## Customize navigation

If awesome-pages plugin is enabled you can selectively enable only certain documentation folders in the mkdocs.yml:

```
nav:
  - ... | administration/**
  - ... | using_the_system/**
```


## Scratch directory

The `.scratch/` folder is a shared space for temporary and disposable files: script outputs, debug logs, extracted data, one-off clone mappings, and other transient artifacts.

- Contents are **git-ignored** — nothing inside `.scratch/` is tracked except `.gitkeep`.
- Use it for one-off scripts, analysis results, or any data that should not pollute the repository.
- Do not reference `.scratch/` files from documentation or production code.
- Agents: place all temporary/draft outputs in `.scratch/` (see [`AGENTS.md`](AGENTS.md)).


## Self-evolution

After non-trivial tasks, document discoveries per [`AGENTS.md`](AGENTS.md) and `.agents/skills/self-evolution/SKILL.md`.


## Legacy files

Obsolete scripts and configs are archived in `.legacy/`. They are not used by the current workflows.
