# Root Python Scripts Roster

This report lists the Python scripts found in the repository root of `D:\Repo\CBAP_MKDOCS_RU`.

| Script | Role | Main side effects / outputs |
|---|---|---|
| `buildhelp.py` | Legacy MkDocs build wrapper for `LANGUAGE_LIST = ["ru"]`. Checks venv and MkDocs, then runs `mkdocs build`. | Deletes/recreates `compiled_help`. |
| `pdf_build_guides.py` | Batch builder for six PDF-oriented MkDocs configs. Streams logs and writes summary. | Writes `build_log.txt`; builds PDF guide sites. |
| `pdf_duplicate_with_date.py` | Copies PDFs modified today with a `YYYY.MM.DD` suffix. Optional `.env` target via `PDF_DATED_DIR`. | Creates dated PDF copies. |
| `kb_html_cleanup_hook.py` | MkDocs `on_post_page` hook that converts generated HTML into PHPKB-compatible HTML. | Used by MkDocs build pipeline; modifies output HTML in memory. |
| `kb_html_cleanup_hook_v4.7.py` | Older v4.7 variant of the PHPKB cleanup hook. Uses fixed `https://kb.comindware.ru/assets/` image URLs. | Used by legacy v4.7 build configs. |
| `phpkb_import.py` | Imports Russian PHPKB articles/categories from DB into Markdown/HTML files under `phpkb_content` by default. | Connects to PHPKB DB; writes imported `.md` and `.html`; updates `.article_id_filename_map_v5.json`. |
| `phpkb_import_for_rag.py` | Same category/filename/CLI behavior as `phpkb_import.py` (V6 map, `--include-private`), but default target is `phpkb_content_rag` and export is markdown-only without mkdocs link/product transforms. | DB read plus local file export for RAG-oriented corpus. Run with repo `.venv`: `.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896 --include-private`. |
| `phpkb_import_cmw_lab.py` | CMW Lab/v4 import variant. Uses `phpkb_content_cmw_lab`, language ID `1`, and `.article_id_filename_map_v4_cmw_lab.json`. | DB read plus local export of CMW Lab KB content. |
| `phpkb_update_articles.py` | Pushes local Markdown/HTML content from `for_kb_import_ru` back into PHPKB articles. Also updates title, tags, `unlisted`. | Connects to DB; asks confirmation per article; updates PHPKB rows. |
| `phpkb_copy_images.py` | Copies image assets from `for_kb_import_ru/` into `kb.comindware.ru/platform/v6.0`. | Copies `.png`, `.svg`, `.jpg`, `.jpeg`, `.gif`; overwrites by default. |
| `phpkb_ingest.py` | Builds one LLM-ingestion Markdown bundle via `gitingest` (default: `phpkb_content_rag/896-platform_v6/`). | Writes `kb.comindware.ru.platform_v6_for_llm_ingestion.md` and copies to `kb.comindware.ru/platform/v6.0/`; `--folder`/`--output` for V5 798 tree. Run with repo `.venv`: `.\.venv\Scripts\python.exe phpkb_ingest.py`. |
| `phpkb_ingest_cmw_lab.py` | Builds a single LLM-ingestion Markdown bundle for CMW Lab/v4 content. | Writes `kb.cmwlab.com.platform_v4_for_llm_ingestion.md`. |
| `phpkb_replace_related_topics.py` | Post-import local Markdown cleanup for related-topic sections under `docs/ru/using_the_system`. Converts bold reference links into italic bullet links inside a wrapper div. | Rewrites matching Markdown files in place. |
| `phpkb_update_article_ids.py` | Post-import prototype for finding direct KB article URLs in a hardcoded Markdown file and resolving them to labels in the shared hyperlinks snippet. | Prints matching labels; currently runs immediately on hardcoded `article-2198.md`; no `__main__` guard. |

## PHPKB Cloning

These scripts support cloning PHPKB category/article trees and then cleaning up the cloned content, IDs, and links.

| Script | Role | Main side effects / outputs |
|---|---|---|
| `utilities/phpkb_cloning/phpkb_clone.py` | Clones PHPKB categories and articles inside the DB. Can clone whole category trees or individual articles, resume from a mapping JSON, and produce a dry-run preflight report. | `--mapping` required. Inserts new DB rows unless `--dry-run`; maintains article/category mapping. |
| `utilities/phpkb_cloning/phpkb_clone_rollback.py` | Deletes cloned PHPKB rows by reading mapped target IDs from a clone mapping JSON. | `--mapping` required. Dry-run by default; deletes DB rows only with `--write --confirm-delete-cloned-content`. |
| `utilities/phpkb_cloning/phpkb_clone_update_links.py` | Updates article/category links in PHPKB after cloning/migration using mapping JSON. Optional product/version replacements can be enabled explicitly. | `--mapping` required. Connects to DB; CLI mode is dry-run unless `--write` is passed. |
| `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py` | Updates local docs IDs using a clone mapping. Handles `kbId` frontmatter in `docs/ru` and article/category IDs in `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`. | `--mapping` required. Dry-run by default; rewrites Markdown files only with `--write`. |

## Script Clusters

- **Build utilities:** `buildhelp.py`, `pdf_build_guides.py`, `pdf_duplicate_with_date.py`.
- **MkDocs-to-PHPKB HTML hooks:** `kb_html_cleanup_hook.py`, `kb_html_cleanup_hook_v4.7.py`.
- **PHPKB DB tools:** `phpkb_import*.py`, `phpkb_update_articles.py`.
- **PHPKB cloning:** scripts under `utilities/phpkb_cloning/`.
- **Post-import Markdown cleanup:** `phpkb_replace_related_topics.py`, `phpkb_update_article_ids.py`.
- **RAG/LLM bundle builders:** `phpkb_import_for_rag.py`, `phpkb_ingest.py`, `phpkb_ingest_cmw_lab.py`. Skill: `.agents/skills/phpkb-ingestion/SKILL.md`.

## Risk Notes

- Highest-risk DB-mutating scripts: `utilities/phpkb_cloning/phpkb_clone.py`, `utilities/phpkb_cloning/phpkb_clone_rollback.py --write`, `phpkb_update_articles.py`, and `utilities/phpkb_cloning/phpkb_clone_update_links.py`.
- Highest-risk local file rewriters: `phpkb_replace_related_topics.py` and `utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --write`.
