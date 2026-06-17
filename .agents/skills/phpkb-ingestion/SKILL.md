---
name: phpkb-ingestion
description: "Use when regenerating or ingesting the Comindware Platform LLM knowledge bundle in this repository: refreshing phpkb_content_rag from PHPKB, running phpkb_import_for_rag.py, running phpkb_ingest.py, or updating the LLM ingestion bundle."
---

# PHPKB LLM Ingestion

Use this skill to refresh the RAG export tree and rebuild the single-file LLM ingestion bundle.

All scripts require explicit `--folder`, `--output`, `--target-dir`, `--category-id` args (no hardcoded version defaults). Examples below show both v5 and v6 invocations.

Scripts live in the repository root. Run them from the repository root with the repo virtual environment.

## Python Environment

Always use the repo `.venv`. Do not install packages into the global interpreter.

Windows (PowerShell):

```powershell
.\.venv\Scripts\python.exe <script>.py
```

Linux/macOS:

```bash
.venv/bin/python <script>.py
```

Dependencies are listed in `install/requirements.txt` (`pyyaml`, `tiktoken`, and the PHPKB import stack).

## Script Roster

| Script | Purpose | Main side effects |
| --- | --- | --- |
| `phpkb_import_for_rag.py` | Pull PHPKB articles/categories from DB into `phpkb_content_rag/`. Markdown-only export; no MkDocs link/product transforms. | DB read via SSH tunnel; writes/updates `.md` files under `phpkb_content_rag/`. |
| `phpkb_ingest.py` | Bundle the RAG tree into one LLM-oriented Markdown file. Supports `--git` and `--pull` for auto-sync. | Writes output bundle; copies to `--target-dir`. |
| `phpkb_ingest_cmw_lab.py` | Same bundling flow for CMW Lab / v4 content. | Writes `kb.cmwlab.com.platform_v4_for_llm_ingestion.md`. |
| `phpkb_import.py` | Pull PHPKB articles/categories into the MkDocs-oriented `phpkb_content/` tree. | DB read via SSH tunnel; rewrites Markdown/HTML files under `phpkb_content/`. |
| `utilities/git_sync.py` | Git add-commit-push assets in the PHPKB repo with interactive ticket prompt. Used by `--git` flag. | Commits and pushes staged files in `CMW_KB_REPO_PATH`. |
| `utilities/ssh_pull.py` | SSH into production server and git pull the PHPKB repo. Used by `--pull` flag. | Connects via `CMW_SSH_*` credentials, runs `git pull` remotely. |

## Key Paths And Outputs

| Path | Role |
| --- | --- |
| `phpkb_content_rag/{category_id}-platform_v{version}/` | Platform RAG corpus |
| `phpkb_content/{category_id}-platform_v{version}/` | Platform MkDocs-oriented PHPKB snapshot |
| `kb.comindware.ru.platform_v{version}_for_llm_ingestion.md` | Root LLM bundle |
| `.article_id_filename_map_v{version}.json` | Article id → filename stem map used during import |
| `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` | Appended to the bundle as `## HYPERLINKS MAP` |
| `mkdocs_ru.yml` | Source for `kbArticleURLPrefix` / `kbCategoryURLPrefix` in the bundle |

Set `CMW_KB_REPO_PATH` in `.env` (e.g. `CMW_KB_REPO_PATH=/var/www/html`) to target
the PHPKB repo directly instead of using a junction. Scripts then copy assets into
`{CMW_KB_REPO_PATH}/platform/{version}/` and can auto-commit-push them.

Alternatively, the `kb.comindware.ru/platform/{version}/` path can be a local junction or
symlink to the external PHPKB web asset checkout. Do not commit machine-specific
absolute targets; verify the link with `Get-Item ... | Format-List LinkType,Target`
when troubleshooting copy/publish behavior.

## .env Configuration

Copy `.env.example` to `.env` and set at minimum:

| Variable | Purpose |
| --- | --- |
| `CMW_KB_REPO_PATH` | Local PHPKB repo path (e.g. `/var/www/html`). Used by `--git` to commit/push assets. |
| `CMW_SSH_HOST` | Production server hostname. |
| `CMW_SSH_USERNAME` | SSH user for production server. |
| `CMW_SSH_KB_REPO_PATH` | PHPKB repo path on the production server (e.g. `/var/www/html`). Used by `--pull`. |

See `.env.example` for the full list (SQL, ports, cmwlab profile).

## Import CLI Notes

- `--category-id` is required (e.g. `798` for v5, `896` for v6).
- `--include-private` — optional legacy flag.
- `--kb-dir phpkb_content_rag` — default output root.
- `--article-map` — e.g. `.article_id_filename_map_v5.json` or `.article_id_filename_map_v6.json`.
- PHPKB imports can take several minutes and should not be treated as timed out.
  When running via agent tooling, use a very long command timeout and wait for
  `Import finished. Total articles imported: <N>`.

Without `--category-id`, `phpkb_import_for_rag.py` falls back to interactive prompts.

Connection setup uses `tools/ssh_kb_ru.establish_connection_interactive()` and `SERVER_PROFILE` from `.env` (default profile: `cmw`).

## Ingest CLI Notes

All version-specific paths are CLI-required for `phpkb_ingest.py` — no hardcoded defaults.

**V5 example:**

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py --folder phpkb_content_rag/798-platform_v5 --output kb.comindware.ru.platform_v5_for_llm_ingestion.md --target-dir kb.comindware.ru/platform/v5.0 --category-id 798
```

**V6 example:**

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py --folder phpkb_content_rag/896-platform_v6 --output kb.comindware.ru.platform_v6_for_llm_ingestion.md --target-dir kb.comindware.ru/platform/v6.0 --category-id 896
```

Bundle shape is a compatibility contract. Preserve the existing header, prompt
section, `## Sections`, `Directory structure:` tree, `## Articles`, `FILE:`
blocks, and `## HYPERLINKS MAP` presence/absence for each generated artifact.

Token estimates intentionally mirror the previous `gitingest` behavior:
`tiktoken.get_encoding("o200k_base")` over `tree + content`, formatted as raw
tokens, `k`, or `M`.

Flags in `phpkb_ingest.py`:

- `--git` — auto-commit-push the copied bundle in `CMW_KB_REPO_PATH`.
- `--pull` — SSH into production and git pull after push.
- `--no-ask` — skip all confirmation prompts (for CI / fully automated runs).
- `--kb-repo-path` — override `CMW_KB_REPO_PATH` from `.env`.
- `--version` — version string for commit message (e.g. `v5.0`). Derived from `--target-dir` if omitted.

## Full refresh examples

**V5:**

```powershell
.\.venv\Scripts\python.exe phpkb_import.py --category-id 798 --article-map .article_id_filename_map_v5.json
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 798 --article-map .article_id_filename_map_v5.json
.\.venv\Scripts\python.exe phpkb_ingest.py --folder phpkb_content_rag/798-platform_v5 --output kb.comindware.ru.platform_v5_for_llm_ingestion.md --target-dir kb.comindware.ru/platform/v5.0 --category-id 798
```

**V6:**

```powershell
.\.venv\Scripts\python.exe phpkb_import.py --category-id 896 --article-map .article_id_filename_map_v6.json
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896 --article-map .article_id_filename_map_v6.json
.\.venv\Scripts\python.exe phpkb_ingest.py --folder phpkb_content_rag/896-platform_v6 --output kb.comindware.ru.platform_v6_for_llm_ingestion.md --target-dir kb.comindware.ru/platform/v6.0 --category-id 896
```

## Publishing the bundle with git auto-sync

After `phpkb_ingest.py` completes, the bundle is updated in **two locations** that are **separate git repos**:

1. **Root repo** — the output bundle file (tracked in this repo)
2. **PHPKB static assets repo** (`CMW_KB_REPO_PATH`) — copy at `platform/{version}/` (tracked in the PHPKB repo)

### Automated workflow (recommended)

Uses `phpkb_ingest.py --git` to auto-commit-push the bundle in the PHPKB repo after copy:

```bash
# Build bundle and git-sync the copy to PHPKB repo
# (add --version v5.0 for v5, --version v6.0 for v6)
python3 phpkb_ingest.py <required-args> --git

# Also SSH into production and git pull after push
python3 phpkb_ingest.py <required-args> --git --pull

# Skip ticket prompt for fully automated runs
python3 phpkb_ingest.py <required-args> --git --pull --no-ask
```

The `--git` flag runs `utilities/git_sync.py` which:
1. Stages new/changed files in `CMW_KB_REPO_PATH/platform/{version}/`
2. Shows a default commit message: `[#auto] Update platform v{version} ingestion bundle`
3. Prompts: "Ticket number? (Enter to keep 'auto', or type a number)"
4. Commits and pushes to the PHPKB remote

The `--pull` flag runs `utilities/ssh_pull.py` which:
1. Connects to the production server via `CMW_SSH_*` credentials
2. Shows confirmation: "SSH into host and run: git -C {remote_path} pull? [Y/n]"
3. On confirmation, executes the remote pull

### Manual workflow (fallback)

```powershell
# Root repo
git add <output-filename>
git commit -m "[#ticket] Update platform v{version} RAG ingestion bundle"
git push

# PHPKB assets repo
git -C "$CMW_KB_REPO_PATH" add platform/{version}/<output-filename>
git -C "$CMW_KB_REPO_PATH" commit -m "[#ticket] Update platform v{version} RAG ingestion bundle"
git -C "$CMW_KB_REPO_PATH" push
```

Do **not** force-add the gitignored junction folder `kb.comindware.ru/` to the root repo — commit in each repo separately.

## Verification

After `phpkb_ingest.py` completes, check the bundle header:

- `Ingestion date` — current timestamp
- `Files analyzed` — markdown file count from `phpkb_content_rag/{category_id}-platform_v{version}/`
- `Estimated tokens` — `tiktoken` estimate over `tree + content`

Confirm the copy step printed:

`File copied to: kb.comindware.ru\platform\{version}\{output-filename}`

Use `git status --short` to review changed files under `phpkb_content_rag/`,
`phpkb_content/`, and the bundle outputs.

## References

- Read `references/workflow.md` for the end-to-end decision tree and troubleshooting.
- For PHPKB cloning or publishing MkDocs articles back to PHPKB, use the `phpkb-cloning` skill instead.

## Safety Checklist

- `phpkb_import_for_rag.py` is read-only against PHPKB (DB read + local file write).
- `phpkb_ingest.py` only reads the RAG tree and writes the bundle; no DB access.
- Do not confuse this workflow with `phpkb_import.py` (writes to `phpkb_content/` with MkDocs transforms) or `phpkb_update_articles.py` (writes back to PHPKB).