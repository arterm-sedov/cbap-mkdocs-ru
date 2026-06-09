# PHPKB LLM Ingestion Workflow

## When To Run What

| User request | Steps |
| --- | --- |
| Regenerate / ingest the LLM bundle | RAG import (if corpus may be stale) → `phpkb_ingest.py` |
| Refresh PHPKB snapshots and ingest | `phpkb_import_for_rag.py` → `phpkb_import.py` → `phpkb_ingest.py` |
| Refresh RAG corpus only | `phpkb_import_for_rag.py --category-id 896` |
| Rebuild bundle from existing RAG tree | `phpkb_ingest.py` only |

## Step 1 — Refresh RAG Export

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896
```

What happens:

1. Opens SSH tunnel and MySQL connection via `tools/ssh_kb_ru.py`.
2. Walks the Russian (`language_id=2`) public category tree under `896`.
3. `--include-private` is optional and usually unnecessary for the public V6 root.
4. Exports markdown-only articles into `phpkb_content_rag/{category-id}-{slug}/`.
5. Uses `.article_id_filename_map_v6.json` to resolve filename stems for gap-fill articles.

Expected console output ends with:

`Import finished. Total articles imported: <N>`

Do not treat PHPKB imports as timed out. They can take several minutes; wait for
the final import summary when running through agent tooling.

## Step 2 — Refresh MkDocs-Oriented PHPKB Snapshot When Needed

```powershell
.\.venv\Scripts\python.exe phpkb_import.py --category-id 896
```

This updates `phpkb_content/896-platform_v6/` from PHPKB using the full
MkDocs-oriented transform path. Run it when the user asks for `phpkb_content` to
be current in addition to the RAG corpus.

## Step 3 — Build LLM Bundle

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py
```

What happens:

1. The script walks `phpkb_content_rag/896-platform_v6/` and reads `*.md` files as UTF-8 text.
2. Rewrites relative `/article.php` links to absolute `https://kb.comindware.ru/...` URLs.
3. Strips `{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}` placeholders from article bodies.
4. Writes bilingual LLM prompts, directory tree, all articles, and the hyperlinks map footer.
5. Copies the bundle to `kb.comindware.ru/platform/v6.0/` unless `--no-copy`.

The bundle shape is a compatibility contract. Preserve the existing header,
prompt section, `## Sections`, `Directory structure:` tree, `## Articles`,
`FILE:` blocks, and `## HYPERLINKS MAP` presence/absence for each artifact.

Token estimates mirror the old `gitingest` behavior: count
`tiktoken.get_encoding("o200k_base").encode(tree + content, disallowed_special=())`
and format the result as raw tokens, `k`, or `M`.

## Bundle Header Template

```text
Ingestion date: YYYY-MM-DD HH:MM:SS
Title: Comindware Platform V6 knowledge base for AI ingestion
Source: https://kb.comindware.ru/category.php?id=896
Files analyzed: <count>
Estimated tokens: <estimate>
```

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `UnicodeError` while reading Markdown | Imported file is not valid UTF-8 text | Inspect and fix the reported Markdown file before rebuilding |
| SSH / DB connection failure | Missing `.env`, keyring creds, or VPN | Check `SERVER_PROFILE` and `tools/ssh_kb_ru.py` profiles |
| Category 896 not found | Wrong profile or stale DB | Confirm `--profile` / `.env` points at kb.comindware.ru PHPKB |
| Import count unchanged but KB updated | Skipped import step | Run step 1 before step 2 |
| Wrong bundle version (V5 vs V6) | Wrong `--folder` / `--category-id` | Use V6 defaults or explicit V5 flags (see SKILL.md) |

## Related Scripts (Not This Workflow)

- `phpkb_import.py` — full MkDocs-oriented import into `phpkb_content/`.
- `phpkb_update_articles.py` — push MkDocs HTML back into PHPKB (DB write).
- `utilities/phpkb_cloning/*` — clone/migrate PHPKB content (see `phpkb-cloning` skill).
