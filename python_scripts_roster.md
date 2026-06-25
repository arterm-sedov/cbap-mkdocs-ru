# Root Python Scripts Roster

Python scripts at the repository root and shared `tools/` helpers. Operator workflows: `readme.md` / `readme-ru.md`. Obsolete scripts: `.legacy/`.

**Line endings:** tracked text from generators uses LF via `tools/text_io.py` (`.gitattributes` `eol=lf`; Git normalizes on `git add`). No per-run verifier in operator workflows.

## Root scripts

| Script | Role | Main side effects / outputs |
|---|---|---|
| `pdf_build_guides.py` | Batch builder for six PDF-oriented MkDocs configs. Streams logs and writes summary. | Writes gitignored `build_log.txt`; builds PDF guide sites. |
| `pdf_duplicate_with_date.py` | Copies PDFs modified today with a `YYYY.MM.DD` suffix. Optional `.env` target via `PDF_DATED_DIR`. | Binary PDF copies only. |
| `kb_html_cleanup_hook.py` | MkDocs `on_post_page` hook — PHPKB-compatible HTML in memory (`\n` normalized before return). | Does not write files; MkDocs writes `for_kb_import_ru/`. |
| `kb_html_cleanup_hook_v4.7.py` | v4.7 variant; fixed `https://kb.comindware.ru/assets/` image URLs. | Legacy v4.7 build configs only. |
| `phpkb_import.py` | Imports PHPKB articles/categories from DB into `phpkb_content/` (default). | DB read; writes `.md`/`.html`/mapping JSON via `tools/text_io`. |
| `phpkb_import_for_rag.py` | Same CLI as `phpkb_import.py`; default `phpkb_content_rag/`, markdown-only RAG export. | DB read; local corpus export via `tools/text_io`. |
| `phpkb_import_cmw_lab.py` | CMW Lab/v4 import into `phpkb_content_cmw_lab/`. | DB read; local export via `tools/text_io`. |
| `phpkb_ingest.py` | Bundles RAG Markdown tree into one LLM ingestion file (`phpkb_ingest_utils`). | Writes bundle (UTF-8 BOM) via `tools/text_io`; optional copy/git to PHPKB assets repo. |
| `phpkb_ingest_cmw_lab.py` | CMW Lab/v4 LLM bundle builder. | Writes `kb.cmwlab.com.platform_v4_for_llm_ingestion.md` via `tools/text_io`. |
| `phpkb_ingest_utils.py` | Shared tree/summary/token helpers for ingest scripts. | Read-only; no file writes. |
| `phpkb_update_articles.py` | Pushes `for_kb_import_ru/` HTML into PHPKB (`article_content`, title, tags, `unlisted`). | DB writes only; reads local HTML. |
| `phpkb_copy_images.py` | Copies images from `for_kb_import_ru/` into PHPKB assets repo. | Binary image copies; optional `utilities/git_sync.py` / `utilities/ssh_pull.py`. |
| `phpkb_replace_related_topics.py` | Post-import cleanup for related-topic blocks under `docs/ru/using_the_system`. | Rewrites matching Markdown via `tools/text_io`. |
| `phpkb_update_article_ids.py` | Read-only prototype: resolve hardcoded KB URLs to hyperlink-map labels. | Prints only; hardcoded `article-2198.md` input. |

## `tools/`

| Script | Role | Main side effects / outputs |
|---|---|---|
| `tools/text_io.py` | Canonical LF text I/O (`open_text_write`, `write_text`, `open_text_append`). | Imported by generators; not run directly. |
| `tools/ssh_kb_ru.py` | SSH tunnel + MySQL connection to PHPKB. | Used by import/update/clone scripts. |
| `tools/graceful_interrupt.py` | Safe interrupt handling for long DB sessions. | Library module. |
| `tools/phpkb_sync.py` | Sync export-tree Markdown into `docs/ru/` by `kbId` (copy missing only). | CSV log via `tools/text_io`. |
| `tools/combine_n3_references.py` | Merge N3 reference Markdown files into one document. | Writes combined `.md` via `tools/text_io`. |

## PHPKB cloning (`utilities/phpkb_cloning/`)

| Script | Role | Main side effects / outputs |
|---|---|---|
| `phpkb_clone.py` | Clone PHPKB categories/articles in DB; resume from mapping JSON; `--dry-run` preflight. | `--mapping` required; DB inserts unless `--dry-run`; mapping via `tools/text_io`. |
| `phpkb_clone_rollback.py` | Delete cloned rows from mapping JSON. | `--write --confirm-delete-cloned-content` deletes DB rows. |
| `phpkb_clone_update_links.py` | Rewrite article/category links in PHPKB after cloning. | DB updates with `--write`. |
| `phpkb_clone_update_mapped_ids.py` | Update `kbId` in `docs/ru/` and hyperlink map from mapping JSON. | `--write` rewrites Markdown via `tools/text_io` (encoding preserved). |

## Other utilities

| Script | Role |
|---|---|
| `utilities/git_sync.py` | Git add/commit/push in PHPKB assets repo (`--git` flags). |
| `utilities/ssh_pull.py` | Remote `git pull` on production (`--pull` flags). |
| `utilities/build_article_id_filename_map_v6.py` | Build V6 article-id → filename gap map JSON. |
| `utilities/remove_entities_param.py` | Strip `Comindware.Entities entities` from `docs/ru/` (writes via `tools/text_io`). |

## Web scraping (`.agents/skills/scrape-sanitize/scripts/`)

| Script | Role |
|---|---|
| `crawl4ai_ingest.py` | Async crawl → dirty Markdown in `.scratch/`. |
| `http_bs4_ingest.py` | BS4 crawl variant for cmwlab.com. |
| `sanitize.py` | Dirty → sanitized bundle under `scraping/`. |
| `common.py` | Shared paths/config; delegates writes to `tools/text_io`. |

Skill: `.agents/skills/scrape-sanitize/SKILL.md`.

## Script clusters

- **Build utilities:** `pdf_build_guides.py`, `pdf_duplicate_with_date.py` (legacy: `.legacy/buildhelp.py`).
- **MkDocs → PHPKB HTML hooks:** `kb_html_cleanup_hook.py`, `kb_html_cleanup_hook_v4.7.py`.
- **PHPKB DB tools:** `phpkb_import*.py`, `phpkb_update_articles.py`.
- **PHPKB cloning:** `utilities/phpkb_cloning/`.
- **Post-import Markdown cleanup:** `phpkb_replace_related_topics.py`, `phpkb_update_article_ids.py` (read-only prototype).
- **RAG / LLM bundles:** `phpkb_import_for_rag.py`, `phpkb_ingest.py`, `phpkb_ingest_cmw_lab.py`, `phpkb_ingest_utils.py`. Skill: `.agents/skills/phpkb-ingestion/SKILL.md`.

## Risk notes

- **Highest-risk DB mutators:** `phpkb_clone.py`, `phpkb_clone_rollback.py --write`, `phpkb_update_articles.py`, `phpkb_clone_update_links.py --write`.
- **Highest-risk local rewriters:** `phpkb_replace_related_topics.py`, `phpkb_clone_update_mapped_ids.py --write`, `phpkb_import*.py` (large generated trees).
