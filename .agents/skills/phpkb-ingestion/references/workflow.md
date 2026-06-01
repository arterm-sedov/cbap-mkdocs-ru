# PHPKB LLM Ingestion Workflow

## When To Run What

| User request | Steps |
| --- | --- |
| Regenerate / ingest the LLM bundle | Import (if corpus may be stale) → `phpkb_ingest.py` |
| Refresh RAG corpus only | `phpkb_import_for_rag.py --category-id 896 --include-private` |
| Rebuild bundle from existing RAG tree | `phpkb_ingest.py` only |

## Step 1 — Refresh RAG Export

```powershell
.\.venv\Scripts\python.exe phpkb_import_for_rag.py --category-id 896 --include-private
```

What happens:

1. Opens SSH tunnel and MySQL connection via `tools/ssh_kb_ru.py`.
2. Walks the Russian (`language_id=2`) public category tree under `896`.
3. With `--include-private`, also walks `category_status='private'` subtrees (needed for the V6 root).
4. Exports markdown-only articles into `phpkb_content_rag/{category-id}-{slug}/`.
5. Uses `.article_id_filename_map_v6.json` to resolve filename stems for gap-fill articles.

Expected console output ends with:

`Import finished. Total articles imported: <N>`

## Step 2 — Build LLM Bundle

```powershell
.\.venv\Scripts\python.exe phpkb_ingest.py
```

What happens:

1. `gitingest` walks `phpkb_content_rag/896-platform_v6/` (excludes `*.html`).
2. Rewrites relative `/article.php` links to absolute `https://kb.comindware.ru/...` URLs.
3. Strips `{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}` placeholders from article bodies.
4. Writes bilingual LLM prompts, directory tree, all articles, and the hyperlinks map footer.
5. Copies the bundle to `kb.comindware.ru/platform/v6.0/` unless `--no-copy`.

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
| `ModuleNotFoundError: gitingest` | Wrong Python interpreter | Use `.venv\Scripts\python.exe` |
| SSH / DB connection failure | Missing `.env`, keyring creds, or VPN | Check `SERVER_PROFILE` and `tools/ssh_kb_ru.py` profiles |
| Category 896 not found | Wrong profile or stale DB | Confirm `--profile` / `.env` points at kb.comindware.ru PHPKB |
| Import count unchanged but KB updated | Skipped import step | Run step 1 before step 2 |
| Wrong bundle version (V5 vs V6) | Wrong `--folder` / `--category-id` | Use V6 defaults or explicit V5 flags (see SKILL.md) |

## Related Scripts (Not This Workflow)

- `phpkb_import.py` — full MkDocs-oriented import into `phpkb_content/`.
- `phpkb_update_articles.py` — push MkDocs HTML back into PHPKB (DB write).
- `utilities/phpkb_cloning/*` — clone/migrate PHPKB content (see `phpkb-cloning` skill).
