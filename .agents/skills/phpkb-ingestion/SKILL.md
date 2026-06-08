---
name: phpkb-ingestion
description: "Use when regenerating or ingesting the Comindware Platform LLM knowledge bundle in this repository: refreshing phpkb_content_rag from PHPKB, running phpkb_import_for_rag.py, running phpkb_ingest.py, or updating kb.comindware.ru.platform_v6_for_llm_ingestion.md."
---

# PHPKB LLM Ingestion

Use this skill to refresh the RAG export tree and rebuild the single-file LLM ingestion bundle for Comindware Platform V6.

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

Dependencies are listed in `install/requirements.txt` (`gitingest`, `pyyaml`, and the PHPKB import stack).

## Script Roster

| Script | Purpose | Main side effects |
| --- | --- | --- |
| `phpkb_import_for_rag.py` | Pull PHPKB articles/categories from DB into `phpkb_content_rag/`. Markdown-only export; no MkDocs link/product transforms. | DB read via SSH tunnel; writes/updates `.md` files under `phpkb_content_rag/`. |
| `phpkb_ingest.py` | Bundle the RAG tree into one LLM-oriented Markdown file via `gitingest`. | Writes `kb.comindware.ru.platform_v6_for_llm_ingestion.md`; copies to `kb.comindware.ru/platform/v6.0/`. |
| `phpkb_ingest_cmw_lab.py` | Same bundling flow for CMW Lab / v4 content. | Writes `kb.cmwlab.com.platform_v4_for_llm_ingestion.md`. |

## Default V6 Workflow

Full refresh (DB export + bundle):

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896 --include-private
.\.venv\Scripts\python.exe phpkb_ingest.py
```

Bundle only (when `phpkb_content_rag/896-platform_v6/` is already current):

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py
```

Skip copying the bundle to `kb.comindware.ru/platform/v6.0/`:

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py --no-copy
```

## Key Paths And Outputs

| Path | Role |
| --- | --- |
| `phpkb_content_rag/896-platform_v6/` | V6 RAG corpus (605 markdown files at last ingest) |
| `kb.comindware.ru.platform_v6_for_llm_ingestion.md` | Root LLM bundle (~927k tokens) |
| `kb.comindware.ru/platform/v6.0/kb.comindware.ru.platform_v6_for_llm_ingestion.md` | Published copy of the bundle |
| `.article_id_filename_map_v6.json` | Article id → filename stem map used during import |
| `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md` | Appended to the bundle as `## HYPERLINKS MAP` |
| `mkdocs_ru.yml` | Source for `kbArticleURLPrefix` / `kbCategoryURLPrefix` in the bundle |

## Import CLI Notes

- `--category-id 896` — V6 root category (non-interactive import).
- `--include-private` — required for category `896` because the V6 root is private.
- `--kb-dir phpkb_content_rag` — default output root.
- `--article-map .article_id_filename_map_v6.json` — default filename map.

Without `--category-id`, `phpkb_import_for_rag.py` falls back to interactive prompts.

Connection setup uses `tools/ssh_kb_ru.establish_connection_interactive()` and `SERVER_PROFILE` from `.env` (default profile: `cmw`).

## Ingest CLI Notes

Defaults in `phpkb_ingest.py`:

- `--folder phpkb_content_rag/896-platform_v6`
- `--output kb.comindware.ru.platform_v6_for_llm_ingestion.md`
- `--target-dir kb.comindware.ru/platform/v6.0`
- `--category-id 896`

Legacy V5 bundle from the 798 tree:

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py --folder phpkb_content_rag/798-platform_v5 --output kb.comindware.ru.platform_v5_for_llm_ingestion.md --target-dir kb.comindware.ru/platform/v5.0 --category-id 798
```

Adjust `--folder` to match the actual `798-*` directory name under `phpkb_content_rag/`.

## Verification

After `phpkb_ingest.py` completes, check the bundle header:

- `Ingestion date` — current timestamp
- `Files analyzed` — markdown file count from `phpkb_content_rag/896-platform_v6/`
- `Estimated tokens` — gitingest summary

Confirm the copy step printed:

`File copied to: kb.comindware.ru\platform\v6.0\kb.comindware.ru.platform_v6_for_llm_ingestion.md`

Use `git status --short` to review changed files under `phpkb_content_rag/` and the bundle outputs.

## References

- Read `references/workflow.md` for the end-to-end decision tree and troubleshooting.
- For PHPKB cloning or publishing MkDocs articles back to PHPKB, use the `phpkb-cloning` skill instead.

## Safety Checklist

- `phpkb_import_for_rag.py` is read-only against PHPKB (DB read + local file write).
- `phpkb_ingest.py` only reads the RAG tree and writes the bundle; no DB access.
- Do not confuse this workflow with `phpkb_import.py` (writes to `phpkb_content/` with MkDocs transforms) or `phpkb_update_articles.py` (writes back to PHPKB).
