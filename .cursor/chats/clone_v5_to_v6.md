# Pleas
_Exported on 5/25/2026 at 19:07:02 GMT+3 from Cursor (3.5.33)_

---

**User**

Do you thingk we can l=clone the KB now to V6?


-------------------------------------


# List root Python scripts

> analyze the python scripts in the repo root and output in the chat the scripts rooster

<details><summary>3 previous messages</summary>

> I’ll scan the repository root for Python scripts, then read their entry points/imports enough to summarize what each one does and how they fit together.
>
> I found 17 root-level Python scripts and the worktree is clean. Next I’m pulling their headers, imports, and main blocks so the roster is useful rather than just a filename dump.
>
> The scripts cluster pretty clearly now: MkDocs/PDF builders, PHPKB import/export/update utilities, and smaller cleanup/migration helpers. I’m checking a few bodies for inputs/outputs and side effects so I can call out which ones touch files, databases, or build artifacts.
</details>

**Root Python Scripts Roster**

I found **17 Python scripts** in `D:\Repo\CBAP_MKDOCS_RU`. Worktree is clean; I only inspected files.

| Script | Role | Main side effects / outputs |
|---|---|---|
| [buildhelp.py](./buildhelp.py) | Legacy MkDocs build wrapper for `LANGUAGE_LIST = ["ru"]`. Checks venv and MkDocs, then runs `mkdocs build`. | Deletes/recreates `compiled_help`. |
| [pdf_build_guides.py](./pdf_build_guides.py) | Batch builder for six PDF-oriented MkDocs configs. Streams logs and writes summary. | Writes `build_log.txt`; builds PDF guide sites. |
| [pdf_duplicate_with_date.py](./pdf_duplicate_with_date.py) | Copies PDFs modified today with a `YYYY.MM.DD` suffix. Optional `.env` target via `PDF_DATED_DIR`. | Creates dated PDF copies. |
| [kb_html_cleanup_hook.py](./kb_html_cleanup_hook.py) | MkDocs `on_post_page` hook that converts generated HTML into PHPKB-compatible HTML. | Used by MkDocs build pipeline; modifies output HTML in memory. |
| [kb_html_cleanup_hook_v4.7.py](./kb_html_cleanup_hook_v4.7.py) | Older v4.7 variant of the PHPKB cleanup hook. Uses fixed `https://kb.comindware.ru/assets/` image URLs. | Used by legacy v4.7 build configs. |
| [phpkb_import.py](./phpkb_import.py) | Imports Russian PHPKB articles/categories from DB into Markdown/HTML files under `phpkb_content` by default. | Connects to PHPKB DB; writes imported `.md` and `.html`; updates `.article_id_filename_map_v5.json`. |
| [phpkb_import_for_rag.py](./phpkb_import_for_rag.py) | Same import pipeline as `phpkb_import.py`, but default target is `phpkb_content_rag`. | DB read plus local file export for RAG-oriented corpus. |
| [phpkb_import_cmw_lab.py](./phpkb_import_cmw_lab.py) | CMW Lab/v4 import variant. Uses `phpkb_content_cmw_lab`, language ID `1`, and `.article_id_filename_map_v4_cmw_lab.json`. | DB read plus local export of CMW Lab KB content. |
| [phpkb_update_articles.py](./phpkb_update_articles.py) | Pushes local Markdown/HTML content from `for_kb_import_ru` back into PHPKB articles. Also updates title, tags, `unlisted`. | Connects to DB; asks confirmation per article; updates PHPKB rows. |
| [phpkb_update_links.py](./phpkb_update_links.py) | Updates article/category links in PHPKB after cloning/migration using mapping JSON. Also performs product/version text replacements. | Connects to DB; rewrites article HTML/title after prompts. |
| [phpkb_clone.py](./phpkb_clone.py) | Clones PHPKB categories and articles inside the DB. Can clone whole category trees or individual articles. | Inserts new DB rows; maintains article/category mapping. |
| [phpkb_copy_images.py](./phpkb_copy_images.py) | Copies image assets from `for_kb_import_ru/` into `kb.comindware.ru/platform/v5.0`. | Copies `.png`, `.svg`, `.jpg`, `.jpeg`, `.gif`; overwrites by default. |
| [phpkb_ingest.py](./phpkb_ingest.py) | Builds a single LLM-ingestion Markdown bundle for v5 KB content using `gitingest`. | Writes `kb.comindware.ru.platform_v5_for_llm_ingestion.md` and copies it to `kb.comindware.ru/platform/v5.0/`. |
| [phpkb_ingest_cmw_lab.py](./phpkb_ingest_cmw_lab.py) | Builds a single LLM-ingestion Markdown bundle for CMW Lab/v4 content. | Writes `kb.cmwlab.com.platform_v4_for_llm_ingestion.md`. |
| [replace_related_topics.py](./replace_related_topics.py) | Mass-edits related-topic sections in `docs/ru/using_the_system`. Converts bold reference links into italic bullet links inside a wrapper div. | Rewrites matching Markdown files in place. |
| [update_article_ids.py](./update_article_ids.py) | Prototype/helper for finding KB article IDs in Markdown links and resolving them via the hyperlinks snippet. | Currently runs immediately on hardcoded `article-2198.md`; no `__main__` guard. |
| [update_kbids_to_v5.py](./update_kbids_to_v5.py) | Migrates `kbId` frontmatter values in `docs/ru` using `.v5mapping.json`. | Rewrites Markdown files in place. |

**Notable Clusters**

- **Build utilities:** `buildhelp.py`, `pdf_build_guides.py`, `pdf_duplicate_with_date.py`.
- **MkDocs-to-PHPKB HTML hooks:** `kb_html_cleanup_hook.py`, `kb_html_cleanup_hook_v4.7.py`.
- **PHPKB DB tools:** `phpkb_import*.py`, `phpkb_update_*.py`, `phpkb_clone.py`.
- **RAG/LLM bundle builders:** `phpkb_ingest.py`, `phpkb_ingest_cmw_lab.py`.
- **Migration/content maintenance helpers:** `replace_related_topics.py`, `update_article_ids.py`, `update_kbids_to_v5.py`.

Highest-risk scripts are the DB-mutating ones: `phpkb_clone.py`, `phpkb_update_articles.py`, and `phpkb_update_links.py`. Highest-risk local file rewriters are `replace_related_topics.py` and `update_kbids_to_v5.py`.

> Save this report in .md file in the repo root

<details><summary>3 previous messages</summary>

> I’ll save the roster as a Markdown report in the repo root, keeping the same structure and adding a short title so it’s easy to find later.
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./python_scripts_roster.md` (+36 -0)
>
> </details>
>
> The Markdown file is in place. I’ll do a quick check that Git sees only that new report file, then I’ll wrap up with the path.
</details>

Saved the report here:

[python_scripts_roster.md](./python_scripts_roster.md)

Git sees it as a new untracked file: `?? python_scripts_roster.md`.

> Ggroup the following scripts in the report under the PHPKB cloning section
>
> replace_related_topics.py	Mass-edits related-topic sections in docs/ru/using_the_system. Converts bold reference links into italic bullet links inside a wrapper div.	Rewrites matching Markdown files in place.update_article_ids.py	Prototype/helper for finding KB article IDs in Markdown links and resolving them via the hyperlinks snippet.	Currently runs immediately on hardcoded article-2198.md; no __main__ guard.update_kbids_to_v5.py	Migrates kbId frontmatter values in docs/ru using .v5mapping.json.	Rewrites Markdown files in place.
>
> phpkb_update_links.py	Updates article/category links in PHPKB after cloning/migration using mapping JSON. Also performs product/version text replacements.	Connects to DB; rewrites article HTML/title after prompts.phpkb_clone.py	Clones PHPKB categories and articles inside the DB. Can clone whole category trees or individual articles.	Inserts new DB rows; maintains article/category mapping.

<details><summary>3 previous messages</summary>

> I’ll update the report structure so those migration helpers and DB tools sit together under a dedicated PHPKB cloning section, instead of being split between the main table and later clusters.
>
> I’m going to keep the full roster complete, but move those five scripts into their own `PHPKB Cloning` subsection so the cloning workflow reads as one group.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./python_scripts_roster.md` (+11 -4)
>
> </details>
</details>

Updated [python_scripts_roster.md](./python_scripts_roster.md) with a new **PHPKB Cloning** section and moved those five scripts into it:

`phpkb_clone.py`, `phpkb_update_links.py`, `replace_related_topics.py`, `update_article_ids.py`, and `update_kbids_to_v5.py`.

> Git create meaningful commit and push

<details><summary>6 previous messages</summary>

> I’ll commit the report update with the repo’s commit-message rules, then push the current branch. First I’m checking the local branch and the exact staged/untracked state so I don’t accidentally include unrelated work.
>
> The current branch is `platform_v5`, tracking `origin/platform_v5`, and only the new report file is untracked. The commit rule points to the local skill, so I’m opening that before composing the message.
>
> The branch has no issue number, so I’ll use the most recent issue prefix from history: `[#10607271]`. I’m staging only `python_scripts_roster.md`, then committing it as `Add Python scripts roster`.
>
> Git is blocked by an existing `.git/index.lock`. I’ll check whether a Git process is actually running before removing a stale lock; if it’s stale, clearing it is the normal recovery path.
>
> The lock disappeared while I was checking it, and there’s no visible `git.exe` process holding it. I’ll retry staging and continue.
>
> Commit created successfully. I’ll push `platform_v5` to its tracked remote now, then verify the branch is clean and up to date.
</details>

Committed and pushed.

Commit: `3e7348f2 [#10607271] Add Python scripts roster`

Pushed `platform_v5` to the configured `origin` push URLs:
- GitVerse `arterm-sedov/cbap-mkdocs-ru`
- GitHub `arterm-sedov/cbap-mkdocs-ru`
- GitHub `vit-fedorov/cbap-mkdocs-ru`

Working tree is clean.

> [$skill-creator](C://Users//ased//.codex//skills//.system//skill-creator//SKILL.md)
>
> Convert the PHPKB Cloning section from the report to skill under .agents/skills here

<details><summary>7 previous messages</summary>

> I’ll use the `skill-creator` instructions and turn the report’s PHPKB cloning notes into a local skill under `.agents/skills`, matching the repo’s existing skill layout.
>
> The skill should live in `.agents/skills` as requested. I’m checking the existing local skill shape and the skill-creator helper scripts so the new folder is valid instead of hand-shaped.
>
> The skill scaffold is created at `.agents/skills/phpkb-cloning`. I’ll replace the template with focused workflow instructions from the report and keep it concise so it’s useful when triggered.
>
> <details><summary>Created 1 file, deleted 1 file</summary>
>
> - Deleted `./.agents/skills/phpkb-cloning/SKILL.md` (+0 -82)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+78 -0)
>
> </details>
>
> The skill body is now written around the five cloning scripts, with safety checks for DB and batch file mutations. I’ll run the skill validator and inspect the resulting diff.
>
> The validator caught a YAML frontmatter issue from the colon in the description. Easy fix: I’ll quote that description and validate again.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+1 -1)
>
> </details>
</details>

Created the new local skill:

[.agents/skills/phpkb-cloning/SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)

It includes the PHPKB cloning workflow, the five requested scripts, common task guidance, and safety checks for DB-mutating and batch file-rewriting scripts. The scaffold also includes:

[.agents/skills/phpkb-cloning/agents/openai.yaml](./.agents/skills/phpkb-cloning/agents/openai.yaml)

Validation passed: `Skill is valid!`

Git status: the new skill folder is untracked.

> .agents/skills/phpkb-cloning/agents/openai.yaml
>
> Explain this file

[openai.yaml](./.agents/skills/phpkb-cloning/agents/openai.yaml) is UI metadata for the skill.

It does not define the skill logic. The actual instructions are in [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md). This file tells Codex/OpenAI-facing skill interfaces how to present the skill to a user.

Current contents mean:

```yaml
interface:
  display_name: "PHPKB Cloning"
  short_description: "Clone PHPKB content and clean up migrated IDs and links."
  default_prompt: "Help me run or update the PHPKB cloning workflow for cloned categories, articles, IDs, and related links."
```

- `display_name`: human-friendly skill name shown in UI lists or chips.
- `short_description`: one-line explanation shown in skill pickers.
- `default_prompt`: starter prompt a UI can prefill when the user chooses this skill.

The trigger/discovery metadata that Codex actually reads for deciding when to use the skill is still the YAML frontmatter in `SKILL.md`, especially `name` and `description`.

> OPENAI-specific?

Yes. `agents/openai.yaml` is **OpenAI/Codex UI-specific metadata**.

It is not part of the core skill definition and is not needed for the skill’s actual behavior. The portable/core skill file is:

[SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)

`openai.yaml` is used by OpenAI-facing clients to display the skill nicely: name, short description, and default prompt. Other agents or tools may ignore it completely.

> Git meaningful commit and push

<details><summary>3 previous messages</summary>

> I’ll commit just the new `phpkb-cloning` skill files and push the current branch. I’ll re-check the branch and status first so the commit stays tidy.
>
> The branch is `platform_v5`, and only the new skill folder is untracked. I’ll reuse the current ticket prefix `[#10607271]` and commit it as a new PHPKB cloning skill.
>
> Commit created. I’ll push `platform_v5` now and then verify the branch is clean.
</details>

Committed and pushed.

Commit: `aaabac09 [#10607271] Add PHPKB cloning skill`

Pushed `platform_v5` to the configured `origin` push URLs. Working tree is clean.

> phpkb_clone.py
>
> Does it use the same shared SSH/DB connector other scripts like [phpkb_update_articles.py](phpkb_update_articles.py) ?

<details><summary>1 previous message</summary>

> I’ll check the imports and connection setup in both scripts side by side so the answer is grounded in the current files.
</details>

Yes. [phpkb_clone.py](./phpkb_clone.py:2) uses the same shared SSH/DB connector pattern as [phpkb_update_articles.py](./phpkb_update_articles.py:1):

```python
from tools.ssh_kb_ru import establish_connection_interactive, close_connection
from tools.graceful_interrupt import safe_input, ensure_cleanup
```

Both scripts keep a global `CONNECTION`, open it in `main()`, and clean it up in `finally` with `ensure_cleanup(CONNECTION, server)`.

Small difference: [phpkb_clone.py](./phpkb_clone.py:218) calls:

```python
CONNECTION, server = establish_connection_interactive("cmw")
```

while [phpkb_update_articles.py](./phpkb_update_articles.py:187) calls:

```python
CONNECTION, server = establish_connection_interactive()
```

So: same shared connector module and cleanup mechanism, but `phpkb_clone.py` explicitly passes `"cmw"` as the connection/profile argument.

> Other sklss for PHPKB cloning too?

Do you mean **other skills**?

Currently, for PHPKB cloning specifically, the dedicated skill is:

[phpkb-cloning](./.agents/skills/phpkb-cloning/SKILL.md)

Nearby/relevant existing skills are:

- [search-knowledge-base](./.agents/skills/search-knowledge-base/SKILL.md) — useful for Comindware KB article/content research, but not PHPKB cloning operations.
- [mkdocs_add_file](./.agents/skills/mkdocs_add_file/SKILL.md) — useful after migration/import when adding articles to MkDocs navigation.
- [cmwhelp_commit](./.agents/skills/cmwhelp_commit/SKILL.md) — useful for commit message formatting.

So: **no other dedicated PHPKB cloning skill yet**. The new `phpkb-cloning` skill is the one that covers `phpkb_clone.py`, `phpkb_update_links.py`, `replace_related_topics.py`, `update_article_ids.py`, and `update_kbids_to_v5.py`.

> "cmw" as the connection/profile argument connects where? to CMWLAB or to COMINDWARE?

<details><summary>1 previous message</summary>

> I’ll inspect the shared connector code and any local config names it references. The answer should come from `tools/ssh_kb_ru.py`, not guesswork from the profile label.
</details>

`"cmw"` connects to **COMINDWARE / comindware.ru**, not CMW Lab.

The connector defines the profiles in [tools/ssh_kb_ru.py](./tools/ssh_kb_ru.py:293):

- `cmw` = `comindware.ru`
- `cmwlab` = `cmwlab.com`

And `_load_server_credentials()` maps them like this:

```python
profile_prefix_map = {"cmw": "CMW_", "cmwlab": "CMWLAB_"}
```

So when [phpkb_clone.py](./phpkb_clone.py:218) calls:

```python
CONNECTION, server = establish_connection_interactive("cmw")
```

it explicitly forces the **CMW / comindware.ru** profile and uses the `CMW_*` values from `.env`.

For CMW Lab, the call would need to be:

```python
establish_connection_interactive("cmwlab")
```

> phpkb_update_links.py, replace_related_topics.py, update_article_ids.py, update_kbids_to_v5.py all use the establish_connection_interactive?

<details><summary>1 previous message</summary>

> I’ll verify each of the four scripts directly for connector imports and calls, then summarize which ones use DB/SSH and which are local-only.
</details>

No. Only **one** of those four uses `establish_connection_interactive()`.

| Script | Uses `establish_connection_interactive()`? | Notes |
|---|---:|---|
| [phpkb_update_links.py](./phpkb_update_links.py:1) | Yes | Imports `tools.ssh_kb_ru`, opens `CONNECTION, server = establish_connection_interactive()` in `main()`, then cleans up with `ensure_cleanup(CONNECTION, server)`. |
| [replace_related_topics.py](./replace_related_topics.py:1) | No | Local Markdown batch rewrite only. Uses `os`, `re`. |
| [update_article_ids.py](./update_article_ids.py:1) | No | Local helper/prototype. Reads Markdown and hyperlink snippet files. Uses `os`, `re`. |
| [update_kbids_to_v5.py](./update_kbids_to_v5.py:1) | No | Local `kbId` migration from `.v5mapping.json`. Uses `re`, `os`, `json`. |

Also important: `phpkb_update_links.py` calls `establish_connection_interactive()` **without** an explicit profile argument, so it uses `SERVER_PROFILE` from `.env`, defaulting to `cmw` if unset.

> .v5mapping.json, .mapping.json
>
> if we run the cloning, will it create a new mapping.json?

<details><summary>1 previous message</summary>

> I’ll inspect `phpkb_clone.py`’s mapping read/write code and compare it with the mapping filenames used by the update scripts.
</details>

Yes. If you run [phpkb_clone.py](./phpkb_clone.py:293), it writes a new root-level `.mapping.json`.

The relevant function is:

```python
def updateMappingJson():
    MAPPING.update({'Categories':CATEGORY_MAPPING, 'Articles':ARTICLE_MAPPING})
    with open(".mapping.json", "w") as mappingFile:
        mappingJson = json.dumps(MAPPING, indent = 4, ensure_ascii=False)
        print(mappingJson)
        mappingFile.write(mappingJson)
```

A few important details:

- It writes exactly `.mapping.json` in the current working directory.
- It uses mode `"w"`, so if `.mapping.json` already exists, it will overwrite it.
- It writes mappings in this shape:

```json
{
    "Categories": {
        "oldCategoryId": "newCategoryId"
    },
    "Articles": {
        "oldArticleId": "newArticleId"
    }
}
```

- [phpkb_update_links.py](./phpkb_update_links.py:286) later reads that same `.mapping.json`.
- `.v5mapping.json` is separate. It is used by [update_kbids_to_v5.py](./update_kbids_to_v5.py:6), not generated by `phpkb_clone.py`.

Right now the repo root has `.v5mapping.json`, but no `.mapping.json`. So yes, cloning should create `.mapping.json` fresh.

> Also important: phpkb_update_links.py calls establish_connection_interactive() without an explicit profile argument, so it uses SERVER_PROFILE from .env, defaulting to cmw if unset.
>
> Should we unify this in the cloning skills to rely on SERVER_PROFILE from .env? What do the other scripts do like [phpkb_update_articles.py](phpkb_update_articles.py) ?

<details><summary>2 previous messages</summary>

> I’ll use the `phpkb-cloning` skill context here and check all PHPKB root scripts for how they call the shared connector, then I’ll give you a recommendation.
>
> The first glob was PowerShell-hostile, so I’ll rerun that search through `rg`’s own glob handling.
</details>

Yes, I think we should unify the **PHPKB cloning workflow** around `SERVER_PROFILE` from `.env`, with one caveat: DB-mutating scripts should print/confirm the selected profile before doing anything destructive.

Current pattern:

| Script | Connector call | Profile behavior |
|---|---|---|
| `phpkb_update_articles.py` | `establish_connection_interactive()` | Uses `SERVER_PROFILE` from `.env`, default `cmw` |
| `phpkb_update_links.py` | `establish_connection_interactive()` | Uses `SERVER_PROFILE` from `.env`, default `cmw` |
| `phpkb_import.py` | `establish_connection_interactive()` | Uses `SERVER_PROFILE` from `.env`, default `cmw` |
| `phpkb_import_for_rag.py` | `establish_connection_interactive()` | Uses `SERVER_PROFILE` from `.env`, default `cmw` |
| `phpkb_clone.py` | `establish_connection_interactive("cmw")` | Hardcoded to Comindware / `CMW_*` |
| `phpkb_import_cmw_lab.py` | `establish_connection_interactive("cmwlab")` | Hardcoded to CMW Lab / `CMWLAB_*` |

So `phpkb_clone.py` is the odd one out among the cloning pair:

- `phpkb_clone.py` always clones on `cmw`.
- `phpkb_update_links.py` updates links on whatever `.env SERVER_PROFILE` says.

That can be dangerous: if someone sets `SERVER_PROFILE=cmwlab`, then runs clone and update-links expecting both on CMW Lab, clone still hits Comindware while update-links hits CMW Lab.

My recommendation:

1. Change `phpkb_clone.py` to call:

```python
CONNECTION, server = establish_connection_interactive()
```

2. Keep `.env` as the single source of truth:

```env
SERVER_PROFILE=cmw
# or
SERVER_PROFILE=cmwlab
```

3. Update the `phpkb-cloning` skill to explicitly say that clone/update-links must use the same `SERVER_PROFILE`.

4. Optionally add a printed confirmation before DB changes, e.g. “Using SERVER_PROFILE=cmw”. That is a nice little seatbelt for scripts that mutate PHPKB.

> Yes, update the [phpkb_clone.py](phpkb_clone.py) very leanly and elegantly

<details><summary>3 previous messages</summary>

> I’ll make the smallest useful change: let `phpkb_clone.py` follow `SERVER_PROFILE` like the companion scripts, and add a tiny connection-profile note so the behavior is visible when someone runs it.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./phpkb_clone.py` (+4 -2)
>
> </details>
>
> The code now follows `.env` like the other scripts and prints the chosen profile before connecting. I’ll do a quick syntax check and diff review.
</details>

Updated [phpkb_clone.py](./phpkb_clone.py:218) leanly:

```python
server_profile = os.getenv("SERVER_PROFILE", "cmw")
print(f"Using PHPKB server profile: {server_profile}")
CONNECTION, server = establish_connection_interactive()
```

So it now follows the same `.env`-driven profile behavior as `phpkb_update_links.py` and `phpkb_update_articles.py`, while still making the selected profile visible before connecting.

Validation: `python -m py_compile phpkb_clone.py` passed.

> does it load the .env?

Yes.

`phpkb_clone.py` itself does **not** explicitly load `.env`, but the imported connector does.

At the top of [phpkb_clone.py](./phpkb_clone.py:2), it imports:

```python
from tools.ssh_kb_ru import establish_connection_interactive, close_connection
```

Then [tools/ssh_kb_ru.py](./tools/ssh_kb_ru.py:67) loads the repo-root `.env` at import time:

```python
if DOTENV_AVAILABLE:
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
```

Since `Path(__file__).resolve().parent.parent` points to the repo root, it loads:

```text
D:\Repo\CBAP_MKDOCS_RU\.env
```

So by the time `phpkb_clone.py` calls:

```python
os.getenv("SERVER_PROFILE", "cmw")
```

`.env` has already been loaded, assuming `python-dotenv` is installed.

> git meaningful commit and push

<details><summary>3 previous messages</summary>

> I’ll commit the `phpkb_clone.py` connector-profile cleanup and push `platform_v5`. First I’ll verify only that file is changed.
>
> Only `phpkb_clone.py` is modified, and the ticket prefix remains `[#10607271]`. I’ll stage it, commit with a concise message, and push.
>
> Commit created. I’ll push it and then check the branch is clean.
</details>

Committed and pushed.

Commit: `b824f69c [#10607271] Use configured PHPKB profile for cloning`

Pushed `platform_v5` to the configured `origin` push URLs. Working tree is clean.

> phpkb_clone.py does it clone all the article fields or just some hardcoded set? Does it clone recursively related records in the DB or only the articles? Eg. articles can have linked file attachment records and other referenced DB records

<details><summary>1 previous message</summary>

> I’ll inspect `phpkb_clone.py`’s SQL statements and table usage, then search for PHPKB attachment/link table names elsewhere in the repo to see whether this script handles them indirectly or not.
</details>

`phpkb_clone.py` clones **all fields from the main article row**, but it does **not** recursively clone related DB records.

What it does:

- For articles, [cloneArticle()](./phpkb_clone.py:88) runs:

```sql
CREATE TEMPORARY TABLE tmp SELECT * from phpkb_articles WHERE article_id={article_id};
ALTER TABLE tmp DROP article_id;
INSERT INTO phpkb_articles SELECT 0,tmp.* FROM tmp;
```

So it copies the full `phpkb_articles` row, except the primary key `article_id`, then inserts a new row with a new ID.

- It optionally changes only:
  - `article_title`, if `suffix` is passed.
  - `article_show`, depending on `show`.

- For categories, [cloneCategory()](./phpkb_clone.py:137) does the same pattern for `phpkb_categories`: copies all fields except `category_id`, then changes `parent_id`.

What it does **not** do:

- It does not inspect foreign keys.
- It does not recursively clone attachment/file records.
- It does not clone comments, ratings, visits, versions, permissions, custom metadata, or other auxiliary PHPKB tables.
- It only creates a new row in `phpkb_relations` with:

```sql
INSERT INTO phpkb_relations (article_id, category_id, article_priority)
VALUES ({newArticleId}, {newCategoryId}, {article_priority});
```

So the cloned article is placed into the cloned/target category, but only through `phpkb_relations`.

Bottom line: it is a **shallow clone** of `phpkb_articles` and `phpkb_categories`, plus the category/article relation. If PHPKB stores attachments or linked files in separate tables keyed by `article_id`, those records are **not cloned** by the current script.

> Can you use our SSH connector and saved credentials and fetch the complete DB schema for comindware?

<details><summary>2 previous messages</summary>

> I’ll fetch it read-only through `tools.ssh_kb_ru` using the `cmw` profile and stored credentials. Since a complete schema is too bulky for chat, I’ll save a Markdown schema report in the repo root and summarize the result here.
>
> The schema fetch succeeded over the shared connector with the `cmw` profile. I’ll quickly check the generated file and Git status so you know exactly what changed locally.
</details>

Fetched the complete schema through the shared SSH/DB connector using the `cmw` profile and saved credentials.

Saved here:

[phpkb_schema_cmw.md](./phpkb_schema_cmw.md)

Summary:

- Database: `phpkbv9`
- Tables: `39`
- Columns: `303`
- Indexes: `110`
- Foreign keys reported by `information_schema`: `0`
- File size: about 54 KB

Notable for our cloning question: the DB has tables like `phpkb_attachments`, `phpkb_article_versions`, `phpkb_article_feedback`, `phpkb_comments`, `phpkb_custom_data`, etc., so `phpkb_clone.py` currently cloning only `phpkb_articles`, `phpkb_categories`, and `phpkb_relations` is definitely a shallow clone.

> Explain SELECT 0,tmp.* FROM tmp;

`SELECT 0, tmp.* FROM tmp` is a trick used to insert a cloned row while forcing a new auto-increment primary key.

In [phpkb_clone.py](./phpkb_clone.py:94), the script does roughly this:

```sql
CREATE TEMPORARY TABLE tmp
SELECT * FROM phpkb_articles
WHERE article_id = {article_id};

ALTER TABLE tmp DROP article_id;

INSERT INTO phpkb_articles
SELECT 0, tmp.* FROM tmp;
```

Meaning:

1. Copy the original article row into a temporary table.
2. Drop `article_id` from the temp table, so the old ID is not reused.
3. Insert into `phpkb_articles` using:

```sql
SELECT 0, tmp.* FROM tmp
```

The `0` is supplied as the first column value, where `article_id` normally goes. In MySQL, inserting `0` into an `AUTO_INCREMENT` primary key usually means “generate the next auto-increment value,” unless SQL mode `NO_AUTO_VALUE_ON_ZERO` is enabled.

`tmp.*` supplies the rest of the article fields in their existing order.

So if `phpkb_articles` columns are:

```text
article_id, article_title, article_content, article_show, ...
```

then:

```sql
SELECT 0, tmp.* FROM tmp
```

produces:

```text
0, copied_article_title, copied_article_content, copied_article_show, ...
```

and MySQL creates a new `article_id`.

Caveat: this relies on column order matching exactly after `ALTER TABLE tmp DROP article_id`. It works, but it is brittle. A safer version would name the target columns explicitly.

> Git meaningful commit

<details><summary>2 previous messages</summary>

> I’ll commit the generated schema report only, using the repo’s ticket-prefixed commit convention.
>
> Only the schema report is untracked. I’ll stage it and commit with the current ticket prefix.
</details>

Committed.

Commit: `2e7b6a1a [#10607271] Add PHPKB schema report`

Branch `platform_v5` is now ahead of `origin/platform_v5` by 1 commit. I did not push, since you asked only for a commit.

> phpkb_clone.py currently cloning only phpkb_articles, phpkb_categories, and phpkb_relations
>
> can it clone phpkb_attachments? do not code, analyse

<details><summary>2 previous messages</summary>

> I’ll inspect the generated schema around `phpkb_attachments` and the current clone SQL, then reason through whether attachments can be cloned safely and what else might need to move with them.
>
> The attachment table is simple: it has its own `attachment_id`, an `article_id`, and file metadata including `file_guid`. The tricky part is not the SQL mechanics; it is deciding whether sharing the same physical file via `file_guid` is acceptable for cloned articles.
</details>

Yes, `phpkb_clone.py` **can be extended to clone `phpkb_attachments`**, and the schema makes that fairly straightforward.

`phpkb_attachments` has these columns:

```text
attachment_id  auto_increment primary key
article_id     linked article
file_guid
file_name
file_type
file_views
file_status
```

So the cloning logic would be:

1. Clone the article in `phpkb_articles`.
2. Get `oldArticleId -> newArticleId`.
3. Copy all rows from `phpkb_attachments` where `article_id = oldArticleId`.
4. Insert them as new rows with:
   - new `attachment_id`
   - `article_id = newArticleId`
   - same `file_guid`, `file_name`, `file_type`, `file_status`
   - probably either copied or reset `file_views`

This would clone the **attachment records**, but likely not duplicate the **physical files**. The `file_guid` probably points to the stored file on disk. If the cloned attachment row keeps the same `file_guid`, both original and cloned articles would reference the same stored file. That may be perfectly fine if attachments are immutable downloads. It may be wrong if deleting/replacing an attachment in one article can affect the other.

The DB has no declared foreign keys (`information_schema` reported `0`), and tables are `MyISAM`, so the database will not enforce consistency for us. The script must be careful.

Important distinction:

- `phpkb_attachments` can be cloned by remapping `article_id`.
- `phpkb_files` is a separate table, currently with `0` rows in the CMW schema report, so it does not appear to be the active attachment store here.
- Other article-related tables exist too: `phpkb_article_versions`, `phpkb_article_feedback`, `phpkb_comments`, `phpkb_custom_data`, `phpkb_favorites`, `phpkb_ratings`, `phpkb_subscribers`, visits, etc. Those should not automatically be cloned unless there is a business reason.

My recommendation: cloning `phpkb_attachments` is reasonable, but do it deliberately as **article-owned content**, not as part of a blind recursive DB clone. I would clone attachment metadata rows with the new `article_id`, preserve `file_guid`, and probably reset `file_views` to `0` unless you want cloned articles to inherit download statistics.

> we do not need to duplicate the files, we want the cloned articles to have linked attachments by backref

Then yes, `phpkb_attachments` is exactly the table to clone.

You would not duplicate physical files. You would duplicate only the attachment metadata rows and point them to the new cloned article ID:

```text
old attachment row:
attachment_id = 123
article_id    = 456
file_guid     = abc-def
file_name     = example.docx
...

new attachment row:
attachment_id = new auto ID
article_id    = new cloned article ID
file_guid     = abc-def
file_name     = example.docx
...
```

That gives the cloned article its own attachment record, while both records reference the same underlying stored file through `file_guid`.

Conceptually, this fits the current clone pattern:

- `phpkb_articles`: clone row, replace `article_id`
- `phpkb_relations`: add relation for new article/category
- `phpkb_attachments`: clone rows, replace `attachment_id` and `article_id`

The only field I would consider changing is `file_views`: reset it to `0` for cloned articles, unless you want inherited attachment download counters. Everything else can probably stay as-is.

> phpkb_custom_data - does it have any rows in the current db linked to articles with new Ids from [.v5mapping.json](.v5mapping.json) ?

<details><summary>2 previous messages</summary>

> I’ll use the PHPKB cloning context and check this read-only: load article IDs from `.v5mapping.json`, then query `phpkb_custom_data` on the CMW database for matching article IDs.
>
> The schema says `phpkb_custom_data` has `field_id`, `article_id`, and `field_data`. I’ll query the live DB for rows whose `article_id` is one of the mapped v5/new IDs.
</details>

No. In the current CMW database, `phpkb_custom_data` has **no rows linked to the new/v5 article IDs** from [.v5mapping.json](./.v5mapping.json).

Read-only query result:

```text
MAPPED_ARTICLES=480
NEW_IDS_CHECKED=480
CUSTOM_DATA_TOTAL=117
NEW_ID_CUSTOM_DATA_ROWS=0
NEW_ID_ARTICLES_WITH_CUSTOM_DATA=0
```

But the old/source IDs from the same mapping do have custom data:

```text
OLD_ID_CUSTOM_DATA_ROWS=66
OLD_ID_ARTICLES_WITH_CUSTOM_DATA=64
```

So for cloning/migration purposes: yes, `phpkb_custom_data` appears to be another shallow-clone gap. The old articles had custom field data, but the mapped new articles do not.

> Now implement cloning with phpkb_attachments and phpkb_custom_data
>
> Implement, TDD, SDD, @AGENTS.md , lean, dry, brilliant, minimal, abstract, pythonic, genius code, non-breaking, clean, impeccable
>
> If tests are needed put under .tests folder

<details><summary>10 previous messages</summary>

> I’ll use the `phpkb-cloning` skill and keep this as a small, testable extension: clone article-owned child rows after the article ID is known, without changing the existing interactive flow.
>
> I see `.tests` already exists, so I’ll add focused unit tests there rather than touching live PHPKB. The design is to test the SQL shape with a fake cursor, then wire the helper into `cloneArticle`.
>
> I’m going to avoid the fragile temp-table pattern for the new child rows. The new helper will explicitly insert the non-PK columns, remap only `article_id`, and preserve `file_guid` so attachments remain linked to the same stored files.
>
> <details><summary>Created 1 file, edited 1 file</summary>
>
> - Wrote `./phpkb_clone.py` (+75 -25)
> - Wrote `./.tests/test_phpkb_clone.py` (+101 -0)
>
> </details>
>
> The helper and tests are in place. I’ll run the targeted tests and a syntax check now; if anything shakes loose, I’ll tighten it before touching broader tests.
>
> The first test run exposed a missing optional local dependency (`pathvalidate`) during import. I’ll stub only that import in the unit test so these tests stay hermetic and do not need the PHPKB import toolchain installed.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./.tests/test_phpkb_clone.py` (+5 -0)
>
> </details>
>
> The targeted unit tests pass now. I’m also updating the local cloning skill note so future runs remember that article attachments and custom data are now part of the clone surface.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+2 -1)
>
> </details>
>
> Everything targeted is green: the new tests pass and the updated skill still validates. I’ll do one final diff summary so I can give you a clean handoff.
</details>

Implemented lean cloning for article-owned child rows in [phpkb_clone.py](./phpkb_clone.py):

- Clones `phpkb_attachments` rows to the new `article_id`.
- Preserves `file_guid`, so physical files are not duplicated.
- Clones `phpkb_custom_data` rows to the new `article_id`.
- Avoids duplicate child-row cloning when an article is already present in `ARTICLE_MAPPING`.
- Uses explicit insert columns instead of the brittle `SELECT 0,tmp.*` pattern for these child tables.

Added targeted tests under [.tests/test_phpkb_clone.py](./.tests/test_phpkb_clone.py).

Also updated [phpkb-cloning/SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md) so the skill reflects the new behavior.

Verification passed:

```text
python -m py_compile phpkb_clone.py .tests\test_phpkb_clone.py
python -m pytest .tests\test_phpkb_clone.py -q
4 passed
python C:\Users\ased\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

I did not run the live clone script against PHPKB.

> git meaningful commit? tests run? are tests dangerours or dry-run?

Not committed yet.

Tests were run, and they passed:

```text
python -m py_compile phpkb_clone.py .tests\test_phpkb_clone.py
python -m pytest .tests\test_phpkb_clone.py -q
4 passed
quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

The tests are **safe/dry-run unit tests**. They do **not** connect to SSH, MySQL, PHPKB, or `.env`. They use fake cursor/connection objects and only assert the SQL that would be executed.

Current uncommitted changes:

- [phpkb_clone.py](./phpkb_clone.py)
- [.tests/test_phpkb_clone.py](./.tests/test_phpkb_clone.py)
- [.agents/skills/phpkb-cloning/SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)

One note: your branch is already ahead by 1 commit from the schema report commit, which was committed but not pushed.

> git commit

<details><summary>2 previous messages</summary>

> I’ll commit the cloning enhancement and tests, keeping the existing unpushed schema commit as-is. First I’ll stage only the three files from this change.
>
> The right files are staged. I’ll commit them with the current ticket prefix.
</details>

Committed.

Commit: `7c33a782 [#10607271] Clone PHPKB article backrefs`

Working tree is clean. Branch `platform_v5` is now ahead of `origin/platform_v5` by 2 commits:

- `7c33a782 [#10607271] Clone PHPKB article backrefs`
- `2e7b6a1a [#10607271] Add PHPKB schema report`

Tests were run before the commit and passed: `4 passed`.

> should we move the cloning scripts to references folder of the clonning skill?
>
> is the phpkb_clone.py interactive or follows some args?

I would **not move the actual cloning scripts** into the skill’s `references/` folder.

They are operational repo-root scripts, not passive reference material. Moving them would break current usage patterns and likely surprise anyone who runs `phpkb_clone.py` from the root. The skill should reference them where they are, which it already does.

A better structure would be:

- Keep executable scripts in repo root:
  - `phpkb_clone.py`
  - `phpkb_update_links.py`
  - `replace_related_topics.py`
  - `update_article_ids.py`
  - `update_kbids_to_v5.py`

- Optionally add reference docs under:
  - `.agents/skills/phpkb-cloning/references/schema-notes.md`
  - `.agents/skills/phpkb-cloning/references/workflow.md`

Those reference files could summarize the DB tables, mapping JSON behavior, and cloning caveats without relocating runnable code.

And yes, `phpkb_clone.py` is **interactive**. It does not take CLI args.

It prompts for:

- SSH/DB connection details indirectly through `establish_connection_interactive()`, using `.env` and stored credentials where available.
- Whether to clone specific articles:

```python
safe_input('Clone specific articles? Y/N')
```

- Article IDs, if cloning specific articles:

```python
safe_input('Enter article ID to clone or E to exit')
```

- Target category ID for each specific article:

```python
safe_input(
    f"Enter target category ID to clone article {article_id} into ..."
)
```

- Or, if cloning category trees, it interactively browses categories and asks which category to clone.

So current behavior is: **interactive TUI-style script, no argparse, no command-line parameters**.

> they are not operationsl skills they are used once a year for a very specific task: create a new PHPKB section for the new product version
>
> Lets start with adding phkpb_clone prefix to all of the cloning scripts

<details><summary>12 previous messages</summary>

> I’ll treat `phkpb_clone` as a typo for `phpkb_clone` and add a consistent `phpkb_clone_` filename prefix to the cloning helper scripts. I’ll first find all references so the rename doesn’t leave stale docs or commands behind.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg -n "phpkb_clone\.py|phpkb_update_links\.py|replace_related_topics\.py|update_article_ids\.py|update_kbids_to_v5\.py|phpkb-cloning|phpkb cloning|PHPKB cloning" . --glob "!*.pdf"`
> - Ran `git status --short --branch`
> - Ran `Get-ChildItem -File -Filter "*.py" | Select-Object -ExpandProperty Name`
>
> </details>
>
> The primary script already has the `phpkb_clone` prefix, so I’ll keep `phpkb_clone.py` stable and rename the companion scripts to match it. I’m also checking hidden skill/test files before the move.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg -n --hidden "phpkb_clone\.py|phpkb_update_links\.py|replace_related_topics\.py|update_article_ids\.py|update_kbids_to_v5\.py" . --glob "!.git/**" --glob "!*.pdf"`
> - Ran `Get-ChildItem -Path .tests -Filter "*phpkb*" -File | Select-Object -ExpandProperty FullName`
> - Ran `Get-ChildItem -Path .agents\skills\phpkb-cloning -Recurse -File | Select-Object -ExpandProperty FullName`
>
> </details>
>
> I found references only in the skill and roster docs, plus the test for the primary clone script. I’ll rename the four companion scripts with `git mv`, then update those references.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `git mv phpkb_update_links.py phpkb_clone_update_links.py`
> - Ran `git mv replace_related_topics.py phpkb_clone_replace_related_topics.py`
> - Ran `git mv update_article_ids.py phpkb_clone_update_article_ids.py`
> - Ran `git mv update_kbids_to_v5.py phpkb_clone_update_kbids_to_v5.py`
>
> </details>
>
> Two of the parallel renames completed, and the other two collided on Git’s index lock. I’ll inspect the current state and finish the remaining moves sequentially.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `git status --short`
> - Ran `Get-ChildItem -File -Filter "*.py" | Select-Object -ExpandProperty Name`
> - Ran `Test-Path .git\index.lock; if (Test-Path .git\index.lock) { Get-Item .git\index.lock | Select-Object FullName,Length,LastWriteTime }`
> - Ran `git mv replace_related_topics.py phpkb_clone_replace_related_topics.py; git mv update_kbids_to_v5.py phpkb_clone_update_kbids_to_v5.py; git status --short`
>
> </details>
>
> All four companion scripts are now renamed. I’ll update the skill and roster docs to point at the new names.
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+12 -12)
> - Wrote `./python_scripts_roster.md` (+7 -7)
>
> </details>
>
> The references are updated. I’ll check for stale filenames and run lightweight validation over the renamed scripts and the existing clone tests.
>
> <details><summary>Ran 7 commands</summary>
>
> - Ran `rg -n --hidden "phpkb_update_links\.py|replace_related_topics\.py|update_article_ids\.py|update_kbids_to_v5\.py" . --glob "!.git/**" --glob "!*.pdf"`
> - Ran `python -m py_compile phpkb_clone.py phpkb_clone_update_links.py phpkb_clone_replace_related_topics.py phpkb_clone_update_article_ids.py phpkb_clone_update_kbids_to_v5.py .tests\test_phpkb_clone.py`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
> - Ran `python C:\Users\ased\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\phpkb-cloning`
> - Ran `git status --short --branch`
> - Ran `Get-ChildItem -File -Filter "phpkb_clone*.py" | Select-Object -ExpandProperty Name`
> - Ran `git diff --stat`
>
> </details>
</details>

Done. I renamed the companion cloning scripts with the `phpkb_clone_` prefix:

- `phpkb_update_links.py` -> `phpkb_clone_update_links.py`
- `replace_related_topics.py` -> `phpkb_clone_replace_related_topics.py`
- `update_article_ids.py` -> `phpkb_clone_update_article_ids.py`
- `update_kbids_to_v5.py` -> `phpkb_clone_update_kbids_to_v5.py`

Kept `phpkb_clone.py` unchanged because it already has the prefix and is the main cloning script.

Also updated:

- [.agents/skills/phpkb-cloning/SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
- [python_scripts_roster.md](./python_scripts_roster.md)

Validation passed:

```text
python -m py_compile phpkb_clone.py phpkb_clone_update_links.py phpkb_clone_replace_related_topics.py phpkb_clone_update_article_ids.py phpkb_clone_update_kbids_to_v5.py .tests\test_phpkb_clone.py
python -m pytest .tests\test_phpkb_clone.py -q
4 passed
quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

Not committed yet.

> move cloning scripts to some uitils/utilities/tools folder maybe?
>
> add reference docs under:
>
> .agents/skills/phpkb-cloning/references/schema-notes.md
> .agents/skills/phpkb-cloning/references/workflow.md

<details><summary>14 previous messages</summary>

> I’ll move them into a dedicated utility folder rather than the skill folder, so they remain runnable repo tools while the skill carries the guidance. I’ll use `utilities/phpkb_cloning/` unless the existing tree suggests a better local convention.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-ChildItem -Path tools -Force | Select-Object Name,Mode`
> - Ran `Get-ChildItem -Path utilities -Force | Select-Object Name,Mode`
> - Ran `git status --short --branch`
> - Ran `rg -n --hidden "phpkb_clone(?:_|\.py)|phpkb_clone_update|phpkb_clone_replace|python_scripts_roster|test_phpkb_clone" . --glob "!.git/**" --glob "!*.pdf"`
>
> </details>
>
> `tools/` already contains shared connector code, while `utilities/` is free for task-specific scripts. I’ll create `utilities/phpkb_cloning/`, move all five PHPKB cloning scripts there, and add small import-path shims only where the scripts import repo-root `tools`.
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `New-Item -ItemType Directory -Force -Path utilities\phpkb_cloning | Out-Null; git mv phpkb_clone.py utilities/phpkb_cloning/phpkb_clone.py; git mv phpkb_clone_update_links.py utilities/phpkb_cloning/phpkb_clone_update_links.py; git mv phpkb_clone_replace_related_topics.py utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py; git mv phpkb_clone_update_article_ids.py utilities/phpkb_cloning/phpkb_clone_update_article_ids.py; git mv phpkb_clone_update_kbids_to_v5.py utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py; git status --short`
>
> </details>
>
> The files are moved. I’ll patch the two DB scripts so they can still import `tools.ssh_kb_ru` when run by path from the repo root or elsewhere.
>
> <details><summary>Edited 3 files, ran 2 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py -TotalCount 35`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_links.py -TotalCount 35`
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+16 -10)
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+11 -4)
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+14 -8)
>
> </details>
>
> Next I’ll update the test import and refresh the skill/roster text so the new location is clear rather than just mechanically renamed.
>
> <details><summary>Edited 3 files, ran 3 commands</summary>
>
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py -TotalCount 30`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
> - Ran `Get-Content -Path python_scripts_roster.md`
> - Wrote `./.tests/test_phpkb_clone.py` (+2 -1)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+17 -10)
> - Wrote `./python_scripts_roster.md` (+8 -8)
>
> </details>
>
> I’ll add the two reference docs now: one for the annual workflow and one for the schema/cloning surface, keeping detailed context out of `SKILL.md` but easy to load when needed.
>
> <details><summary>Created 2 files</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+41 -0)
> - Wrote `./.agents/skills/phpkb-cloning/references/schema-notes.md` (+94 -0)
>
> </details>
>
> The reference docs are in place. I’ll scan for stale paths, compile the moved scripts, run the dry unit tests, and validate the skill metadata.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `rg -n --hidden "(?<!utilities/phpkb_cloning/)phpkb_clone\.py|(?<!utilities/phpkb_cloning/)phpkb_clone_update_links\.py|(?<!utilities/phpkb_cloning/)phpkb_clone_replace_related_topics\.py|(?<!utilities/phpkb_cloning/)phpkb_clone_update_article_ids\.py|(?<!utilities/phpkb_cloning/)phpkb_clone_update_kbids_to_v5\.py|phpkb_update_links\.py|replace_related_topics\.py|update_article_ids\.py|update_kbids_to_v5\.py" . --glob "!.git/**" --glob "!*.pdf"`
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py utilities\phpkb_cloning\phpkb_clone_update_links.py utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py utilities\phpkb_cloning\phpkb_clone_update_article_ids.py utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py .tests\test_phpkb_clone.py`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
> - Ran `python C:\Users\ased\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\phpkb-cloning`
>
> </details>
>
> The compile, unit tests, and skill validation are green. My stale-reference regex used unsupported lookbehind, so I’ll rerun that check with simpler searches.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `rg -n --hidden "phpkb_update_links\.py|replace_related_topics\.py|update_article_ids\.py|update_kbids_to_v5\.py" . --glob "!.git/**" --glob "!*.pdf"`
> - Ran `rg -n --hidden "phpkb_clone\.py|phpkb_clone_update_links\.py|phpkb_clone_replace_related_topics\.py|phpkb_clone_update_article_ids\.py|phpkb_clone_update_kbids_to_v5\.py" . --glob "!.git/**" --glob "!*.pdf"`
> - Ran `git diff --stat`
> - Ran `git status --short --branch`
>
> </details>
</details>

Moved the PHPKB cloning scripts into:

[utilities/phpkb_cloning](./utilities/phpkb_cloning)

The moved scripts are:

- [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py)
- [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py)
- [phpkb_clone_replace_related_topics.py](./utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py)
- [phpkb_clone_update_article_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_article_ids.py)
- [phpkb_clone_update_kbids_to_v5.py](./utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py)

Added the requested references:

- [.agents/skills/phpkb-cloning/references/schema-notes.md](./.agents/skills/phpkb-cloning/references/schema-notes.md)
- [.agents/skills/phpkb-cloning/references/workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)

Also updated the skill, roster report, and unit test import path. I added a small repo-root import shim to the two DB scripts so `tools.ssh_kb_ru` still imports correctly after the move.

Validation passed:

```text
python -m py_compile ...
python -m pytest .tests\test_phpkb_clone.py -q
4 passed
quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

Not committed yet.

> D:\Repo\CBAP_MKDOCS_RU\python_scripts_roster.md updated?
>
> git commit and push

<details><summary>8 previous messages</summary>

> Yes, `python_scripts_roster.md` was updated to point at `utilities/phpkb_cloning/`. I’ll commit the move plus docs/references together and push the current branch.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff -- python_scripts_roster.md`
> - Ran `git log -n 3 --pretty=%B`
>
> </details>
>
> The roster has the new utility paths. I’ll run the targeted safe checks once more before committing, then push both local commits plus this one.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py utilities\phpkb_cloning\phpkb_clone_update_links.py utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py utilities\phpkb_cloning\phpkb_clone_update_article_ids.py utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py .tests\test_phpkb_clone.py`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
> - Ran `python C:\Users\ased\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\phpkb-cloning`
> - Ran `git add -- .agents/skills/phpkb-cloning/SKILL.md .agents/skills/phpkb-cloning/references/schema-notes.md .agents/skills/phpkb-cloning/references/workflow.md .tests/test_phpkb_clone.py python_scripts_roster.md utilities/phpkb_cloning/phpkb_clone.py utilities/phpkb_cloning/phpkb_clone_update_links.py utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py utilities/phpkb_cloning/phpkb_clone_update_article_ids.py utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py phpkb_clone.py phpkb_update_links.py replace_related_topics.py update_article_ids.py update_kbids_to_v5.py`
>
> </details>
>
> The old root files are already moved, so that explicit pathspec tripped on a deleted source. I’ll stage the rename set with `git add -A` now.
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `git add -A -- .agents/skills/phpkb-cloning .tests/test_phpkb_clone.py python_scripts_roster.md utilities/phpkb_cloning phpkb_clone.py phpkb_update_links.py replace_related_topics.py update_article_ids.py update_kbids_to_v5.py; git status --short`
> - Ran `git add -A; git status --short`
>
> </details>
>
> Everything is staged. I’ll commit this as a focused organization change, then push `platform_v5`.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `git commit -m "[#10607271] Organize PHPKB cloning utilities"`
> - Ran `git push origin platform_v5`
> - Ran `git status --short --branch`
> - Ran `git log -3 --oneline`
>
> </details>
</details>

Yes, [python_scripts_roster.md](./python_scripts_roster.md) was updated with the new `utilities/phpkb_cloning/` paths.

Committed and pushed.

Latest commit: `4521c63f [#10607271] Organize PHPKB cloning utilities`

Pushed `platform_v5` to the configured `origin` push URLs. Working tree is clean.

Tests/validation run before commit:

```text
python -m py_compile ...
python -m pytest .tests\test_phpkb_clone.py -q
4 passed
quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

> D:/Repo/CBAP_MKDOCS_RU/utilities/phpkb_cloning/phpkb_clone.py
> Can we make it support the cli args to be used via scripts?

<details><summary>12 previous messages</summary>

> I’ll add a small argparse layer while preserving the current interactive mode as the default. I’ll support script-friendly article and category cloning by IDs, with `--profile` overriding `.env` only when supplied.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py`
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git status --short --branch`
>
> </details>
>
> I’ll add a tiny command layer, not a rewrite: `--article-id` for one or more articles, `--target-category-id` for scripted article placement, and `--category-id` with optional `--target-parent-id` for scripted tree cloning. Existing no-arg interactive behavior will stay intact.
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+160 -72)
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+163 -103)
>
> </details>
>
> The CLI layer is now in place; I spotted one tiny compatibility bug while reviewing: the article helper still forced hidden clones internally. I’ll fix that and add dry unit tests for the argument/dispatch behavior.
>
> <details><summary>Edited 3 files</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+1 -1)
> - Wrote `./.tests/test_phpkb_clone.py` (+58 -0)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+17 -1)
>
> </details>
>
> I’ll run the dry tests and syntax checks now. These should only exercise fake cursors and argument parsing, not SSH or MySQL.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --help`
>
> </details>
>
> The dry tests pass, but `--help` exposed an old import-time dependency on `pathvalidate`. I’ll make that import tolerant so basic CLI help works even outside the full PHPKB import environment.
>
> <details><summary>Edited 1 file, ran 3 commands</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+5 -1)
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --help`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py`
>
> </details>
>
> The CLI help now works without connecting or needing the extra filename package. I’ll validate the skill doc and check the final diff/status before wrapping up.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `python C:\Users\ased\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\phpkb-cloning`
> - Ran `git diff --stat`
> - Ran `git status --short --branch`
>
> </details>
</details>

Implemented CLI support in [utilities/phpkb_cloning/phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py).

It still runs the old interactive flow when called with no action args, but now supports scripted usage:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --category-id 798 --target-parent-id 1000
```

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --article-id 4578 --target-category-id 900 --suffix _CLONE
```

Added options:

- `--profile {cmw,cmwlab}`
- `--category-id`
- `--target-parent-id`
- `--article-id` repeatable
- `--target-category-id`
- `--suffix`
- `--show`

Also updated the workflow reference and added dry unit tests for argument parsing and CLI dispatch.

Validation passed:

```text
python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py
python -m pytest .tests\test_phpkb_clone.py -q
7 passed
python utilities\phpkb_cloning\phpkb_clone.py --help
quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

No live SSH/DB clone was run. Changes are not committed yet.

> Tests run well?

Yes. The tests ran cleanly.

```text
python -m pytest .tests\test_phpkb_clone.py -q
7 passed
```

Also passed:

```text
python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py
python utilities\phpkb_cloning\phpkb_clone.py --help
quick_validate.py .agents\skills\phpkb-cloning
Skill is valid!
```

These were dry/unit checks only. No SSH or DB cloning was run.

> git commit

<details><summary>2 previous messages</summary>

> I’ll commit the CLI support and its dry tests/docs with the existing ticket prefix.
>
> <details><summary>Ran 9 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git log -n 3 --pretty=%B`
> - Ran `git add -- utilities/phpkb_cloning/phpkb_clone.py .tests/test_phpkb_clone.py .agents/skills/phpkb-cloning/references/workflow.md`
> - Ran `git status --short`
> - Ran `git status --short`
> - Ran `git commit -m "[#10607271] Add CLI support for PHPKB cloning"`
> - Ran `git status --short --branch`
> - Ran `git log -1 --oneline`
>
> </details>
</details>

Committed.

Commit: `d4457aa8 [#10607271] Add CLI support for PHPKB cloning`

Working tree is clean. Branch `platform_v5` is ahead of `origin/platform_v5` by 1 commit.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py
>
> Analyse how this script works and how to make it agnostic and controllable instead of fixed to v4-v5 migration,

<details><summary>2 previous messages</summary>

> I’ll inspect the script and its mapping inputs, then outline what is hardcoded today and what a cleaner configurable shape would look like.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py`
> - Ran `Get-Content -Path .v5mapping.json -TotalCount 40`
> - Ran `rg -n "kbId:|\.v5mapping|update_kbids|phpkb_clone_update_kbids" . --glob "!*.pdf" --glob "!.git/**"`
> - Ran `git status --short --branch`
>
> </details>
</details>

[phpkb_clone_update_kbids_to_v5.py](./utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py) is currently a very narrow one-off migration script.

**How It Works**
It hardcodes these inputs:

```python
KB_ID_MAP_FILE = '.v5mapping.json'
DOCS_RU_FOLDER = 'docs/ru'
HYPERLINKS_FILE = 'docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md'
```

Then:

1. Loads `.v5mapping.json`.
2. Takes only `mapping["Articles"]`.
3. Recursively walks `docs/ru`.
4. For every `.md` file, replaces exact frontmatter-like strings:

```text
kbId: oldId
```

with:

```text
kbId: newId
```

5. Writes files in place if any match was found.

There is commented-out logic for categories and hyperlink snippets, but currently only article `kbId` values in Markdown files are updated.

**Current Limitations**
It is fixed to v5:

- Fixed mapping file: `.v5mapping.json`
- Fixed source section: `Articles`
- Fixed target directory: `docs/ru`
- Fixed field name: `kbId`
- Fixed file extension: `.md`
- No dry-run
- No backup
- No summary report beyond noisy counter prints
- No CLI args
- No way to include `.pages`, snippets, or category mappings without editing code
- It rewrites files with default encoding in `open(file_path, "w+")`, not explicit UTF-8
- Regex is simple and only matches `kbId: {key}` exactly, not `kbId: "123"` or extra spacing

**How To Make It Agnostic And Controllable**
I’d turn it into a general “mapped ID replacer” utility.

Suggested CLI:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_ids.py `
  --mapping .mapping.json `
  --section Articles `
  --root docs/ru `
  --field kbId `
  --glob *.md `
  --dry-run
```

Useful options:

- `--mapping`: mapping JSON path, e.g. `.mapping.json`, `.v5mapping.json`
- `--section`: mapping section, e.g. `Articles`, `Categories`
- `--root`: target folder or file
- `--field`: frontmatter/key field to update, default `kbId`
- `--glob`: file glob, repeatable, default `*.md`
- `--include-snippet`: optionally update hyperlink snippet
- `--dry-run`: print planned changes only
- `--write`: required to actually modify files, or dry-run by default
- `--encoding`: default `utf-8`
- `--report`: optional JSON/Markdown report of changed files and replacements

Core design:

- Load mapping once.
- Discover files from configurable roots/globs.
- Build a safe regex for the selected field:

```regex
^(\s*kbId\s*:\s*)oldId(\s*)$
```

- Replace only field values, not arbitrary article IDs in body text unless explicitly requested.
- Return structured results: file path, old ID, new ID, count.
- Write only changed files.
- Make dry-run the default for safety.

**Recommended Rename**
Since it should no longer be v5-specific:

```text
phpkb_clone_update_kbids_to_v5.py
```

could become:

```text
phpkb_clone_update_mapped_ids.py
```

or more specific:

```text
phpkb_clone_update_frontmatter_ids.py
```

Best fit in this workflow: `phpkb_clone_update_mapped_ids.py`.

**Key Principle**
Make the script mapping-driven, not version-driven. The version belongs in the mapping file name or CLI args, not in the code.

> how does it use:
> V4_KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map.json'
> V5_KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map_v5.json'
> HYPERLINKS_FILE = os.path.join(DOCS_RU_FOLDER, '.snippets/hyperlinks_mkdocs_to_kb_map.md')

It currently **does not use them**.

In [phpkb_clone_update_kbids_to_v5.py](./utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py), these constants are defined:

```python
V4_KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map.json'
V5_KB_ID_TO_TITLE_MAP_FILE = '.article_id_filename_map_v5.json'
HYPERLINKS_FILE = os.path.join(DOCS_RU_FOLDER, '.snippets/hyperlinks_mkdocs_to_kb_map.md')
```

But their usage is commented out:

```python
# v4TtitleMapping = loadMappingJson(V4_KB_ID_TO_TITLE_MAP_FILE)
# v5TtitleMapping = loadMappingJson(V5_KB_ID_TO_TITLE_MAP_FILE)
```

And:

```python
# updateIdsInFile(HYPERLINKS_FILE, v5IdMapping.get('Articles'))
# updateIdsInFile(HYPERLINKS_FILE, v5IdMapping.get('Categories'))
```

So the active script only uses:

```python
KB_ID_MAP_FILE = '.v5mapping.json'
DOCS_RU_FOLDER = 'docs/ru'
```

Specifically:

1. Loads `.v5mapping.json`.
2. Takes `v5IdMapping.get('Articles')`.
3. Walks `docs/ru`.
4. Replaces `kbId: oldArticleId` with `kbId: newArticleId` in `.md` files.

The title map constants are dead/legacy leftovers, and `HYPERLINKS_FILE` is a planned or previous target that is currently disabled.

> explain --section logic

`--section` would tell the generalized script **which part of the mapping JSON to use**.

Your mapping files are shaped like this:

```json
{
  "Categories": {
    "378": "798",
    "384": "799"
  },
  "Articles": {
    "2198": "4578",
    "2201": "4582"
  }
}
```

So:

```powershell
--section Articles
```

means:

```python
mapping = mapping_json["Articles"]
```

and the script updates article IDs, for example:

```md
kbId: 2198
```

to:

```md
kbId: 4578
```

While:

```powershell
--section Categories
```

means:

```python
mapping = mapping_json["Categories"]
```

and the script would use category ID mappings instead.

The important bit: `--section` prevents the script from guessing. The same JSON file can contain multiple ID maps, and each map is meant for a different kind of target.

Example commands:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --section Articles --root docs/ru --field kbId
```

updates article `kbId` fields.

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --section Categories --root docs/ru --glob "*.pages"
```

would use category mappings, if we implement `.pages` category ID replacement.

> Why would we run phpkb_cloning/phpkb_clone_update_mapped_ids.py for category ids? To execute updateIdsInFile(HYPERLINKS_FILE, v5IdMapping.get('Categories')) ? the files under docs folder do not use category ids

Exactly. For the normal `docs/ru/**/*.md` frontmatter use case, `--section Categories` would **not** make sense because article files use `kbId`, which is an article ID.

Category mappings would only matter for targets that actually contain category IDs, such as:

- `HYPERLINKS_FILE`, if it contains category link references using `kbCategoryURLPrefix`
- `.pages` files, if they contain category IDs
- Any generated/import metadata file that stores PHPKB category IDs
- A future navigation/map file that references PHPKB category IDs

So yes, the old commented line:

```python
# updateIdsInFile(HYPERLINKS_FILE, v5IdMapping.get('Categories'))
```

is the main clue for why `Categories` was considered.

But for the actual docs folder Markdown articles:

```powershell
--section Articles --field kbId --root docs/ru --glob *.md
```

is the right shape.

A cleaner design would avoid implying category mappings are generally useful for docs frontmatter. It could have presets instead:

```powershell
--target article-frontmatter
```

Uses:

```text
mapping section: Articles
files: docs/ru/**/*.md
field: kbId
```

And maybe later:

```powershell
--target hyperlink-snippet-categories
```

Uses:

```text
mapping section: Categories
file: docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md
pattern: kbCategoryURLPrefix category IDs
```

So the generic `--section` is technically flexible, but for this repo the safer UX is probably named targets/presets.

> --glob "*.pages" seems to be useless?

Yes, probably useless in the current repo.

The old script has this commented block:

```python
# for root, _, files in os.walk(DOCS_RU_FOLDER):
#     for file in files:
#         if file.endswith(".pages"):
#             file_path = os.path.join(root, file)
#             updateIdsInFile(file_path, v5IdMapping.get('Categories'))
```

But that only makes sense if `.pages` files actually contain raw PHPKB category IDs in a replaceable form like:

```text
categoryId: 378
```

or links with old category IDs.

From what we’ve seen, the active docs content uses article `kbId` in `.md` files. So a command like:

```powershell
--section Categories --root docs/ru --glob "*.pages"
```

is more of a hypothetical leftover from the commented code, not a useful current workflow.

For this repo, the practical first target should be narrow:

```powershell
--target article-frontmatter
```

Meaning:

- Mapping section: `Articles`
- Files: `docs/ru/**/*.md`
- Pattern: `kbId: <oldArticleId>`

Then, only if we confirm category IDs exist somewhere, add a separate category-aware target. Right now I’d drop the `.pages` example from the recommendation.

> and  --glob *.md? they are always mds, no?

For the current `kbId` frontmatter migration, yes: it should always be Markdown files.

So `--glob *.md` is probably unnecessary as a user-facing option for the default/common path. It adds configurability, but not much practical value.

A better UX would be:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py `
  --target article-frontmatter `
  --mapping .mapping.json `
  --root docs/ru `
  --dry-run
```

Where `--target article-frontmatter` implies:

```text
section = Articles
file type = .md
field = kbId
```

Then advanced options can exist only if needed later, but they do not need to be the main interface.

So I’d simplify the concept to:

- Required: `--mapping`
- Optional: `--root`, default `docs/ru`
- Optional: `--dry-run` / `--write`
- Fixed for this target:
  - `Articles`
  - `.md`
  - `kbId`

The script name could be specific too:

```text
phpkb_clone_update_article_kbids.py
```

That may be better than a too-generic `mapped_ids` tool.

> No Categories anymore? We need to update the [hyperlink_calculate_formula.md](docs/ru/examples/hyperlink_calculate_formula.md) actually and it has categories and articles ids

<details><summary>5 previous messages</summary>

> Good catch. I’ll inspect that article and the hyperlink snippet patterns so we can separate “article frontmatter only” from “content body links containing both article and category IDs.”
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-Content -Path docs\ru\examples\hyperlink_calculate_formula.md`
> - Ran `rg -n "kbArticleURLPrefix|kbCategoryURLPrefix|article\.php\?id=|category\.php\?id=|kbId:|category" docs\ru\examples\hyperlink_calculate_formula.md docs\ru\.snippets\hyperlinks_mkdocs_to_kb_map.md .v5mapping.json`
> - Ran `Get-Content -Path docs\ru\.snippets\hyperlinks_mkdocs_to_kb_map.md -TotalCount 120`
>
> </details>
>
> Context compaction
>
> Source: automatic
> Status: completed
>
> I’m using the PHPKB cloning skill context here because this is exactly the migration helper territory. I’ll check the actual article and snippet wiring so the answer is grounded in the repository instead of guessing from the script name.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
> - Ran `Select-String -Path docs\ru\examples\hyperlink_calculate_formula.md -Pattern 'kbId|kbArticleURLPrefix|kbCategoryURLPrefix|include-markdown|\[[^\]]+\]' -Context 0,0`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py`
> - Ran `Select-String -Path docs\ru\.snippets\hyperlinks_mkdocs_to_kb_map.md -Pattern 'kbArticleURLPrefix|kbCategoryURLPrefix' | Select-Object -First 40`
>
> </details>
</details>

Yes, you’re right. Categories are still relevant, just not in the narrow `kbId:` frontmatter path.

For [hyperlink_calculate_formula.md](./docs/ru/examples/hyperlink_calculate_formula.md:301), the article includes:

```markdown
{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
```

So its rendered links come from [hyperlinks_mkdocs_to_kb_map.md](./docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md:5), and that snippet absolutely contains both:

```markdown
[...]: {{ kbArticleURLPrefix }}4593
[...]: {{ kbCategoryURLPrefix }}813
```

So my earlier framing should be corrected:

- `--glob "*.pages"` is probably not useful for this repo unless category IDs are stored in `.pages` files somewhere.
- `--glob "*.md"` is useful only for `kbId:` frontmatter article IDs.
- Category IDs still need migration in the shared hyperlink snippet, because docs can reference categories through labels like `[examples_cat]`, `[admin_guide_cat]`, etc.
- For `hyperlink_calculate_formula.md`, the category/article IDs are not directly inline in the article body; they are inherited through the included snippet.

The better script design is not “run `--section Categories` over docs.” It should have explicit targets, for example:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --target frontmatter-kbids --root docs/ru --write
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --target hyperlink-map --file docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md --write
```

And `hyperlink-map` should update both sections intelligently:

- `{{ kbArticleURLPrefix }}<id>` using `mapping["Articles"]`
- `{{ kbCategoryURLPrefix }}<id>` using `mapping["Categories"]`

That’s the clean split: article frontmatter is article-only; hyperlink map is article plus category.

> Final plan to make
> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py usable as CLI tool for D:\Repo\CBAP_MKDOCS_RU\.agents\skills\phpkb-cloning skill and V5>V6 migration

<details><summary>1 previous message</summary>

> I’ll keep this as a design plan, not code yet. The key is to turn the current one-off “v5 kbId replacer” into a small migration utility with named targets, so the skill can call it safely for V5 to V6 and future annual clones.
</details>

**Final Plan**

Turn [phpkb_clone_update_kbids_to_v5.py](./utilities/phpkb_cloning/phpkb_clone_update_kbids_to_v5.py) from a hardcoded V4 to V5 helper into a generic post-clone ID migration CLI.

1. Rename or repurpose the tool around mapped IDs, not V5 specifically.

Preferred new name:

```text
utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py
```

Keep the old file as a thin compatibility wrapper only if we want to avoid breaking old notes.

2. Make `.mapping.json` / `.v5mapping.json` an explicit CLI input.

Example:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --target all --write
```

For V5 to V6, the cloning step should produce or use a mapping like:

```json
{
  "Articles": {
    "4918": "6001"
  },
  "Categories": {
    "871": "940"
  }
}
```

3. Replace `--section` with task-oriented `--target`.

Recommended targets:

```text
frontmatter-kbids
hyperlink-map
all
```

Meaning:

- `frontmatter-kbids`: update `kbId:` values in Markdown frontmatter under `docs/ru`.
- `hyperlink-map`: update article/category IDs in `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`.
- `all`: run both.

This is clearer than asking the user to know when `Articles` or `Categories` applies.

4. Handle Articles and Categories differently by context.

For Markdown frontmatter:

```text
kbId: 4918
```

Use only:

```python
mapping["Articles"]
```

For hyperlink snippet:

```markdown
{{ kbArticleURLPrefix }}4918
{{ kbCategoryURLPrefix }}871
```

Use:

```python
mapping["Articles"]   for kbArticleURLPrefix
mapping["Categories"] for kbCategoryURLPrefix
```

This fixes the `hyperlink_calculate_formula.md` case correctly, because that article gets its article/category links through the included snippet.

5. Add safe CLI defaults.

Suggested CLI:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py `
  --mapping .mapping.json `
  --target all `
  --root docs/ru `
  --hyperlinks-file docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md `
  --dry-run
```

Use `--dry-run` by default. Require `--write` to modify files.

6. Output a migration report.

The tool should print:

```text
Mapping: .mapping.json
Target: all
Mode: dry-run

Frontmatter kbIds:
  files scanned: 1234
  files changed: 18
  replacements: 18

Hyperlink map:
  article links changed: 42
  category links changed: 9
```

No noisy per-ID prints.

7. Add tests under `.tests`.

Test cases should cover:

- article frontmatter replacement;
- no replacement when ID is missing from mapping;
- preserving unrelated Markdown;
- hyperlink article prefix replacement;
- hyperlink category prefix replacement;
- dry-run does not write;
- `--write` writes expected content.

These tests are safe: temp files only, no SSH, no DB.

8. Update the PHPKB cloning skill docs.

Update:

```text
.agents/skills/phpkb-cloning/SKILL.md
.agents/skills/phpkb-cloning/references/workflow.md
```

Document V5 to V6 flow as:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py ...
python utilities/phpkb_cloning/phpkb_clone_update_links.py ...
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --target all --dry-run
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .mapping.json --target all --write
```

That gives us a lean, reusable migration tool: no hardcoded V5 naming, no misleading `.pages` glob, and correct support for both article IDs and category IDs where the repo actually stores them.

> Keep the old file as a thin compatibility wrapper only if we want to avoid breaking old notes.
>  ? explain, why would we need this?

We may not need it.

I mentioned it only because the current filename, `phpkb_clone_update_kbids_to_v5.py`, might already be referenced in:

- `.agents/skills/phpkb-cloning/SKILL.md`
- `python_scripts_roster.md`
- workflow notes
- old chat/task notes
- someone’s local command history

A thin wrapper would let old commands keep working:

```python
# phpkb_clone_update_kbids_to_v5.py
from phpkb_clone_update_mapped_ids import main

if __name__ == "__main__":
    main()
```

So if someone runs the old script name, it still executes the new generic CLI.

But for this repo, since this is a once-a-year internal workflow and we’re actively cleaning it up, I’d prefer **not** keeping the wrapper. Better to rename cleanly, update the skill docs and roster, and avoid carrying a misleading “to_v5” file into V5 to V6 work.

My recommendation: **rename it outright to `phpkb_clone_update_mapped_ids.py`, no compatibility wrapper**, unless you know another automation or external note still calls the old filename.

> why do you mention hyperlink_calculate_formula.md? we use [hyperlinks_mkdocs_to_kb_map.md](docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md)

Because you brought up [hyperlink_calculate_formula.md](./docs/ru/examples/hyperlink_calculate_formula.md) as the example that “has categories and articles ids.”

After checking it, the important correction is: it does **not** really own those article/category IDs directly. It includes [hyperlinks_mkdocs_to_kb_map.md](./docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md), and that snippet is where the `kbArticleURLPrefix` and `kbCategoryURLPrefix` IDs live.

So yes, for the migration tool we should focus on:

```text
docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md
```

`hyperlink_calculate_formula.md` is only evidence that docs consume that shared snippet. It should not be a special target.

> We update
> .agents/skills/phpkb-cloning/SKILL.md
> python_scripts_roster.md
>
> WE care only about hyperlinks_mkdocs_to_kb_map.md
>
> Implement

<details><summary>12 previous messages</summary>

> Got it. I’ll implement the generic CLI around the shared hyperlink map plus frontmatter IDs, update only the skill docs and roster references, and keep the snippet as the only hyperlink target.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `Get-Content -Path python_scripts_roster.md`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
> - Ran `Get-ChildItem -Path .tests -Force | Select-Object Name`
>
> </details>
>
> I found the current helper is still the old hardcoded script. I’m going to replace it with a generic mapped-ID CLI, rename the file so the name no longer lies about V5, then add focused dry-run tests around the hyperlink snippet behavior.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py`
> - Ran `rg "phpkb_clone_update_kbids_to_v5|update_mapped_ids" -n`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
>
> </details>
>
> I’m dropping the misleading `.pages`/`--section` idea entirely. The CLI will know the two real local-doc jobs: `kbId:` frontmatter under `docs/ru`, and the one shared `hyperlinks_mkdocs_to_kb_map.md` file for article/category URL IDs.
>
> <details><summary>Created 1 file, edited 3 files, ran 2 commands</summary>
>
> - Ran `git mv utilities\phpkb_cloning\phpkb_clone_update_kbids_to_v5.py utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py`
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py` (+193 -69)
> - Wrote `./.tests/test_phpkb_clone_update_mapped_ids.py` (+102 -0)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+11 -8)
> - Wrote `./python_scripts_roster.md` (+2 -2)
> - Ran `rg "phpkb_clone_update_kbids_to_v5|\.v5mapping|\.pages|--section" -n .agents\skills\phpkb-cloning python_scripts_roster.md utilities\phpkb_cloning .tests`
>
> </details>
>
> There are still two stale references inside the skill’s workflow reference, so I’m updating those too. Even though you named the main skill file and roster, leaving the skill’s own reference page stale would make the CLI harder to use later.
>
> <details><summary>Edited 1 file, ran 3 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+2 -2)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone_update_mapped_ids.py`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py --help`
> - Ran `rg "phpkb_clone_update_kbids_to_v5|\.pages|--section" -n .agents\skills\phpkb-cloning python_scripts_roster.md utilities\phpkb_cloning .tests`
>
> </details>
>
> The CLI help and syntax check are clean, and the old `to_v5`/`.pages`/`--section` references are gone from the touched skill/tool area. I’m running the focused tests now.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `python -m pytest .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone.py -q`
> - Ran `Test-Path .mapping.json; Test-Path .v5mapping.json`
> - Ran `git status --short`
> - Ran `git diff --stat`
>
> </details>
>
> The tests are all green: 12 passed, including the existing cloning tests. I also noticed this checkout has `.v5mapping.json` but no `.mapping.json`, so I’ll do one dry-run with `.v5mapping.json` to prove the CLI works against the current repo without writing anything.
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `python utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py --mapping .v5mapping.json --target hyperlink-map`
> - Ran `git diff -- .agents\skills\phpkb-cloning\SKILL.md python_scripts_roster.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git diff -- utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py`
> - Ran `git diff -- .tests\test_phpkb_clone_update_mapped_ids.py`
> - Ran `rg "phpkb_clone_update_kbids_to_v5" -n`
> - Ran `git status --short --branch`
>
> </details>
</details>

Implemented.

What changed:
- Renamed the old V5-specific script to [phpkb_clone_update_mapped_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py).
- Added CLI support:
  - `--mapping`, default `.mapping.json`
  - `--target frontmatter-kbids|hyperlink-map|all`, default `all`
  - `--root`, default `docs/ru`
  - `--hyperlinks-file`, default [hyperlinks_mkdocs_to_kb_map.md](./docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md)
  - `--write`; without it, dry-run only
- `hyperlink-map` updates only the shared snippet:
  - `{{ kbArticleURLPrefix }}...` from `Articles`
  - `{{ kbCategoryURLPrefix }}...` from `Categories`
- Updated [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md), [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md), and [python_scripts_roster.md](./python_scripts_roster.md).
- Added focused tests in [test_phpkb_clone_update_mapped_ids.py](./.tests/test_phpkb_clone_update_mapped_ids.py).

Verification:
- `python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone_update_mapped_ids.py`
- `python utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py --help`
- `python -m pytest .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone.py -q`

Result: `12 passed`.

I also ran a dry-run against the current `.v5mapping.json` for the hyperlink map; it would update 5 article links and 0 category links, with no files written.

> git commit and push

<details><summary>4 previous messages</summary>

> I’ll commit the CLI migration work and push it now, using the repo’s commit-message rule so the history stays consistent.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-Content -Path .agents\skills\cmwhelp_commit\SKILL.md`
> - Ran `git status --short --branch`
> - Ran `git rev-parse --abbrev-ref HEAD`
> - Ran `git log -n 5 --pretty=%B`
> - Ran `git diff --stat`
>
> </details>
>
> The branch name has no ticket number, so the commit rule falls back to recent messages. The latest matching ticket is `#5`, so I’ll use that prefix for this commit.
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `git add -A`
> - Ran `git status --short --branch`
> - Ran `git diff --cached --stat`
> - Ran `git commit -m "[#5] Add mapped ID migration CLI"`
> - Ran `git push`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed and pushed.

Commit: `55505056 [#5] Add mapped ID migration CLI`

Pushed `platform_v5` to the configured remotes. Working tree is clean.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning
> D:\Repo\CBAP_MKDOCS_RU\.agents\skills\phpkb-cloning
>
> Are the scripts and skills ready to really clone the kb content? Analyze do not change code

<details><summary>8 previous messages</summary>

> I’ll use the PHPKB cloning skill and inspect the actual scripts plus the skill references as they stand now. I’ll keep this read-only and focus on whether the workflow is operationally ready, where it is safe, and where it still has sharp edges.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
> - Ran `Get-ChildItem -Path utilities\phpkb_cloning -File | Select-Object Name,Length,LastWriteTime`
> - Ran `Get-ChildItem -Path .agents\skills\phpkb-cloning -Recurse -File | Select-Object FullName,Length`
> - Ran `git status --short --branch`
>
> </details>
>
> The repo is clean and the skill points at the expected utility folder. Now I’m reading the operational scripts themselves, especially the DB-mutating ones, to separate “ready to execute” from “documented but still prototype-ish.”
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_links.py`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\schema-notes.md`
>
> </details>
>
> The core clone script and the mapped-ID tool look much more operational than the older helpers. I’m checking the remaining support scripts and connector assumptions now, because the weakest link in an annual clone is often the script that still has a hardcoded path or import-time side effect.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_article_ids.py`
> - Ran `Get-Content -Path tools\ssh_kb_ru.py`
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py`
> - Ran `Get-Content -Path .tests\test_phpkb_clone_update_mapped_ids.py`
>
> </details>
>
> I’ve got enough to make the call, but I’m doing one last read-only verification: CLI help, unit tests, and a quick scan for hardcoded assumptions that would bite during a real clone.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --help`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py --help`
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_mapped_ids.py -q`
> - Ran `rg "TODO|FIXME|article-2198|\.mapping\.json|4\\.7|5\.0|docs/ru/using_the_system|SERVER_PROFILE|establish_connection_interactive|SELECT MAX|CREATE TEMPORARY|INSERT INTO phpkb_articles" utilities\phpkb_cloning .agents\skills\phpkb-cloning -n`
>
> </details>
</details>

Short answer: **ready for a controlled real clone, but not a fully hardened “press button and forget” migration.**

What is ready:
- [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py) can really clone DB content. It uses the shared SSH/DB connector, supports `--profile`, category-tree cloning, selected article cloning, writes `.mapping.json`, clones full `phpkb_articles` / `phpkb_categories` rows except regenerated IDs, creates `phpkb_relations`, and copies `phpkb_attachments` plus `phpkb_custom_data` backrefs.
- [phpkb_clone_update_mapped_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py) is ready for local docs ID migration. It is dry-run by default and correctly updates [hyperlinks_mkdocs_to_kb_map.md](./docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md) using `Articles` and `Categories`.
- The skill docs in [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md) and [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md) are broadly aligned with the scripts.
- Read-only verification passed: CLI help works, and focused tests pass: `12 passed`.

Main caveats before a real KB clone:
- `phpkb_clone.py` does **not load an existing `.mapping.json` before cloning**. If a clone is interrupted and restarted, it may duplicate already cloned categories/articles instead of resuming from the saved mapping.
- New IDs are detected with `SELECT MAX(article_id)` / `SELECT MAX(category_id)`. That is risky if another process inserts PHPKB rows at the same time.
- `phpkb_clone_update_links.py` is operational but still old-style and interactive. It has hardcoded `4.7 -> 5.0` prompts, so for V5 to V6 it is **not cleanly ready** unless those replacements are intentionally skipped or updated.
- `phpkb_clone_update_article_ids.py` is **not operational workflow code**. It runs immediately against hardcoded `article-2198.md`; treat it as a prototype only.
- `phpkb_clone_replace_related_topics.py` is narrow and hardcoded to `docs/ru/using_the_system`; fine for that cleanup, not part of the core clone.
- I did **not** run a live DB clone or open a live SSH connection in this analysis.

My operational verdict: **the core clone path is usable if we take a fresh backup, run once in a quiet DB window, verify `.env SERVER_PROFILE`, and treat `.mapping.json` as the critical artifact.** For a safer annual V5 to V6 run, I would harden resume behavior and remove/update the hardcoded `4.7 -> 5.0` link-update logic before touching production-like content.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_article_ids.py
>
> What does it do exactly? Formats migrated hyperlinks?

<details><summary>1 previous message</summary>

> I’ll answer from the file itself, not from the roster description. This one is small but a bit misleading, because it discovers hyperlink labels and then stops short of rewriting anything.
</details>

No, it does **not** format migrated hyperlinks.

[phpkb_clone_update_article_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_article_ids.py) is a prototype lookup script. What it does exactly:

1. Hardcodes:

```python
docs_ru_folder = 'docs/ru'
hyperlinks_file = 'docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md'
md_file_path = 'article-2198.md'
```

2. Opens `article-2198.md`.

3. Searches that file for direct PHPKB URLs matching roughly:

```text
https://kb.comindware.ru...id=123
https://kb.comindware.ru...-123.html
```

4. For each found article ID, it scans [hyperlinks_mkdocs_to_kb_map.md](./docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md) and tries to find a reference label pointing to that same ID.

Example conceptually:

```markdown
[some_article]: {{ kbArticleURLPrefix }}123
```

5. If it finds one, it prints something like:

```text
Found linkd and URL for articleId 123: [some_article]
```

That’s all.

Important caveats:
- It runs immediately at import time; no `if __name__ == "__main__"` guard.
- It only processes hardcoded `article-2198.md`.
- `search_kbId_in_docs()` exists but is unused.
- It does not edit the Markdown file.
- It does not replace direct links with reference-style links.
- It does not use `.mapping.json`.
- It does not migrate old IDs to new IDs.
- It does not touch category IDs.

So its practical purpose is: **given a Markdown file with direct KB links, identify whether those article IDs already have labels in the shared hyperlink snippet.**

It’s more of a half-built helper for converting direct PHPKB URLs into reference labels, not part of the real clone/migration pipeline yet.

> phpkb_clone_update_article_ids.py add docstring to it to make this clear?

<details><summary>2 previous messages</summary>

> I’ll add a clear module docstring at the top, keeping the script behavior untouched. This is a good place for a warning label: useful lookup prototype, not a migration formatter.
>
> <details><summary>Edited 1 file, ran 1 command</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_article_ids.py` (+23 -5)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_article_ids.py; git diff -- utilities\phpkb_cloning\phpkb_clone_update_article_ids.py`
>
> </details>
</details>

Added a module docstring to [phpkb_clone_update_article_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_article_ids.py:1) clarifying that it is a prototype lookup helper, not a hyperlink formatter or migration tool.

Verified with:

```powershell
python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_article_ids.py
```

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_links.py is a useful script, right? But not agnostic and not fit for V5>V6 migration?

Yes. [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py) is useful, but it is **not agnostic** and is **not cleanly fit for V5 to V6 as-is**.

What it usefully does:
- Loads `.mapping.json`.
- Connects to PHPKB through the shared SSH/DB connector.
- Walks a chosen category tree interactively.
- Updates cloned PHPKB article HTML in `phpkb_articles.article_content`.
- Rewrites mapped article references:
  - `data-value="oldArticleId"`
  - `Article-ID:oldArticleId`
  - `article.php?id=oldArticleId`
- Rewrites mapped category references:
  - `category.php?id=oldCategoryId`
- Updates `article_title` and `article_content` in DB when changes are found.

Why it is not agnostic:
- Hardcodes `.mapping.json`.
- Has no CLI args.
- Has no dry-run mode.
- Requires interactive category browsing.
- Has hardcoded product/version migrations:
  - `Comindware Business Application Platform` -> `Comindware Platform`
  - `(Comindware )?Architect` -> `«Архитектор»`
  - `4.7` -> `5.0`
- Does not let you specify source/target version strings.
- Does not cleanly separate “ID remapping” from “product/version text migration.”

For V5 to V6, the ID-remapping part is still valuable, but the text-replacement part is wrong or at least suspicious. A V5 to V6 migration should not have hardwired `4.7 -> 5.0` prompts sitting in the operational path.

So I’d classify it as:

```text
Useful legacy post-clone DB link updater.
Needs parameterization before V5 -> V6.
```

Minimum to make it V5 to V6-ready:
- Add dry-run.
- Add CLI category root selection.
- Keep ID replacement always available.
- Move product/version replacements behind explicit flags/options.
- Replace hardcoded `4.7` / `5.0` with `--old-version` / `--new-version`, or disable version replacement by default.

> Can we make it agnostic and prorgammatic cli use ready?
>
> Also (Comindware )?Architect -> «Архитектор» and omindware Business Application Platform -> Comindware Platform replacements are probably already done at v4.7>V5 migration, so we should make these optional maybe?

<details><summary>12 previous messages</summary>

> I’ll treat this as an implementation request and keep the old interactive behavior available, while adding a safer CLI path for V5 to V6. The main idea is: ID remapping is core, product/version text rewrites become explicit options.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_links.py`
> - Ran `git status --short --branch`
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py`
>
> </details>
>
> There’s one local uncommitted docstring change in `phpkb_clone_update_article_ids.py` from the previous request; I’ll leave it intact and work alongside it. I’m refactoring the link updater without making any live DB calls.
>
> 4.7 -> 5.0  replacement is valud, but 5.0 to 6.0 of course
>
> <details><summary>Deleted 1 file</summary>
>
> - Deleted `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+0 -300)
>
> </details>
>
> Exactly, that’s the shape I’m building: the version replacement stays valid as a feature, but it becomes parameterized. Legacy interactive can still default to `4.7 -> 5.0`; scripted V5 to V6 would use `--old-version 5.0 --new-version 6.0`.
>
> <details><summary>Created 1 file, edited 1 file</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+465 -0)
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+3 -3)
>
> </details>
>
> The live-update path is now split into reusable transformations plus DB orchestration. I’m adding unit tests around the transformation and dry-run behavior, so we verify without SSH or DB writes.
>
> <details><summary>Created 1 file, edited 3 files</summary>
>
> - Wrote `./.tests/test_phpkb_clone_update_links.py` (+109 -0)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+7 -2)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+5 -0)
> - Wrote `./python_scripts_roster.md` (+1 -1)
>
> </details>
>
> The skill docs now describe the safer usage: dry-run first, `--write` explicit, product names optional, and V5 to V6 version replacement expressed as `--old-version 5.0 --new-version 6.0`. Next I’m verifying syntax, help output, and tests.
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_links.py .tests\test_phpkb_clone_update_links.py`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_update_links.py --help`
> - Ran `git diff --stat`
> - Ran `python -m pytest .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone.py -q`
> - Ran `git status --short --branch`
> - Ran `rg "old-version|new-version|replace-product-names|4\.7|5\.0|6\.0" utilities\phpkb_cloning\phpkb_clone_update_links.py .agents\skills\phpkb-cloning python_scripts_roster.md .tests\test_phpkb_clone_update_links.py -n`
>
> </details>
>
> <details><summary>Plan</summary>
>
> - [x] Refactor link updater into reusable replacement functions
> - [x] Add safe CLI with dry-run/write and optional text replacements
> - [x] Add dry unit tests for link updater behavior
> - [x] Run verification without touching DB
>
> </details>
</details>

Yes. I made [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py) agnostic and CLI-ready.

What changed:
- Added programmatic CLI:
  - `--profile cmw|cmwlab`
  - `--mapping .mapping.json`
  - `--category-id <id>` for recursive category updates
  - `--article-id <id>` repeatable for targeted article updates
  - `--write`; without it, CLI mode is dry-run
  - `--old-version 5.0 --new-version 6.0`
  - `--replace-product-names`
- Made product-name replacements optional:
  - `Comindware Business Application Platform` -> `Comindware Platform`
  - `(Comindware )?Architect` -> `«Архитектор»`
- Made version replacement parameterized:
  - old legacy interactive behavior still defaults to `4.7 -> 5.0`
  - V5 to V6 CLI use is now `--old-version 5.0 --new-version 6.0`
- Added dry tests in [test_phpkb_clone_update_links.py](./.tests/test_phpkb_clone_update_links.py).
- Updated the cloning skill docs and roster.

Example V5 to V6 dry run:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .mapping.json --category-id 900 --old-version 5.0 --new-version 6.0
```

Actual DB write:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .mapping.json --category-id 900 --old-version 5.0 --new-version 6.0 --write
```

Optional legacy product-name cleanup:

```powershell
--replace-product-names
```

Verification passed, with no DB calls:

```powershell
python -m pytest .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone.py -q
```

Result: `18 passed`.

> Skills updated?

Yes. The PHPKB cloning skill was updated.

Changed:
- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
  - `phpkb_clone_update_links.py` now described as CLI dry-run by default.
  - Product-name replacements documented as optional via `--replace-product-names`.
  - Version replacement documented as parameterized, e.g. `--old-version 5.0 --new-version 6.0`.
  - Legacy no-arg interactive behavior noted as preserving `4.7 -> 5.0` prompts.

- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)
  - Added dry-run example.
  - Added V5 to V6 example using `--old-version 5.0 --new-version 6.0`.
  - Noted `--replace-product-names` should only be used if still needed.
  - Noted `--write` should only be added after dry-run looks correct.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_links.py doccumented inline ?

Not really. [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py) is documented through:

- CLI `--help` text
- clearer function names
- skill docs / workflow docs
- tests

But it does **not** yet have good inline/module documentation like the docstring we added to `phpkb_clone_update_article_ids.py`.

I’d add a top-level module docstring explaining:

- this is the DB post-clone link updater;
- CLI mode is dry-run by default;
- `--write` mutates PHPKB;
- ID remapping is always core behavior;
- product-name replacements are optional;
- version replacement is parameterized, e.g. `5.0 -> 6.0`;
- no-arg interactive mode preserves legacy `4.7 -> 5.0` prompts.

That would make the script self-explanatory when opened directly.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_links.py document and make sure it's tested

<details><summary>2 previous messages</summary>

> I’ll add a concise module docstring to the link updater and run the focused tests again. The code already has behavior tests, so this is mostly making the script self-documenting without changing how it runs.
>
> <details><summary>Edited 1 file, ran 3 commands</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+26 -0)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_links.py .tests\test_phpkb_clone_update_links.py; python -m pytest .tests\test_phpkb_clone_update_links.py -q`
> - Ran `python -m pytest .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone.py -q`
> - Ran `git status --short --branch`
>
> </details>
</details>

Documented [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py:1) with a top-level docstring covering:

- what the script does after cloning;
- which PHPKB link forms it remaps;
- dry-run vs `--write`;
- category/article CLI modes;
- V5 to V6 version replacement;
- optional legacy product-name cleanup;
- preserved no-arg legacy interactive behavior.

Tested:

```powershell
python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_links.py .tests\test_phpkb_clone_update_links.py
python -m pytest .tests\test_phpkb_clone_update_links.py -q
python -m pytest .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone.py -q
```

Result: `18 passed`.

> git meaningful commit

<details><summary>4 previous messages</summary>

> I’ll commit the current PHPKB cloning utility updates only, using the repo’s ticketed commit-message convention.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git log -n 5 --pretty=%B`
> - Ran `git diff --stat`
>
> </details>
>
> The latest ticket prefix in this branch history is `#5`, so I’m using that. I’ll stage all current changes, commit them, and leave pushing alone since you asked only for a commit.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `git add -A`
> - Ran `git status --short --branch`
> - Ran `git diff --cached --stat`
> - Ran `git commit -m "[#5] Make PHPKB link updates scriptable"`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed.

Commit: `6a0edfd7 [#5] Make PHPKB link updates scriptable`

Branch `platform_v5` is now ahead of origin by 1 commit. I did not push.

> You wrote:
>
> phpkb_clone.py does not load an existing .mapping.json before cloning. If a clone is interrupted and restarted, it may duplicate already cloned categories/articles instead of resuming from the saved mapping.
> New IDs are detected with SELECT MAX(article_id) / SELECT MAX(category_id). That is risky if another process inserts PHPKB rows at the same time.
>
> What improvements do you suggest?

I’d make two focused improvements before a real clone run.

**1. Load and reuse `.mapping.json`**

At startup, `phpkb_clone.py` should load an existing mapping file if present:

```json
{
  "Categories": {
    "798": "920"
  },
  "Articles": {
    "4918": "6001"
  }
}
```

Then:

- if source category `798` is already mapped, reuse `920` instead of cloning the category again;
- if source article `4918` is already mapped, reuse `6001` instead of cloning the article again;
- still insert missing `phpkb_relations` when an already-cloned article needs to be linked into a newly cloned category;
- write `.mapping.json` atomically after each successful category/article clone.

This turns the clone into a resumable operation instead of a one-shot script.

**2. Replace `SELECT MAX(...)` with `cursor.lastrowid`**

Current pattern:

```sql
INSERT INTO phpkb_articles SELECT 0,tmp.* FROM tmp;
SELECT MAX(article_id) FROM phpkb_articles;
```

Risk: if another user/process inserts an article between those two statements, `MAX(article_id)` can return someone else’s row.

Better:

```python
cursor.execute("INSERT INTO phpkb_articles SELECT 0,tmp.* FROM tmp")
new_article_id = str(cursor.lastrowid)
```

Same for categories:

```python
cursor.execute("INSERT INTO phpkb_categories SELECT 0,tmp.* FROM tmp")
new_category_id = str(cursor.lastrowid)
```

That gives the ID generated by this connection’s insert, not the latest row globally.

**Nice extra**

Add CLI flags:

```powershell
--mapping .mapping.json
--resume
--fresh
```

Recommended behavior:

- default: load `.mapping.json` if it exists and resume;
- `--fresh`: refuse to run if `.mapping.json` already exists, unless maybe `--mapping new-file.json`;
- print a startup summary:

```text
Mapping: .mapping.json
Loaded mapped categories: 42
Loaded mapped articles: 318
Mode: resume
```

These two changes would make the clone much safer without turning the script into a big framework.

> Implement
>
> Explain to me `cursor.lastrowid`

<details><summary>8 previous messages</summary>

> I’ll implement the resumable mapping load plus `lastrowid` ID capture in `phpkb_clone.py`, and I’ll add dry tests so this stays safe without touching the DB. I’ll also explain `cursor.lastrowid` plainly after the implementation.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py`
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py`
> - Ran `git status --short --branch`
>
> </details>
>
> I’m going to make resume the default: load the chosen mapping file if it exists, reuse mapped categories/articles, and only `--fresh` refuses to continue from an existing mapping. I’ll also capture generated IDs immediately from the insert cursor via `lastrowid`, before dropping the temp table.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+121 -59)
>
> </details>
>
> The core change is in place. I’m adjusting the existing dry tests now because the expected DB call sequence changed: the tests should assert `lastrowid` is used and `SELECT MAX(...)` is gone.
>
> <details><summary>Edited 1 file, ran 3 commands</summary>
>
> - Wrote `./.tests/test_phpkb_clone.py` (+69 -3)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py`
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --help`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
>
> </details>
>
> The clone script’s focused tests pass now. I’m updating the skill notes so future runs know about `--mapping`, `--fresh`, resume behavior, and the safer ID capture.
>
> <details><summary>Edited 3 files, ran 3 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+3 -0)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+8 -0)
> - Wrote `./python_scripts_roster.md` (+1 -1)
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py -q`
> - Ran `rg "SELECT MAX\((article_id|category_id)\)|lastrowid|--fresh|--mapping" utilities\phpkb_cloning\phpkb_clone.py .agents\skills\phpkb-cloning python_scripts_roster.md .tests\test_phpkb_clone.py -n`
> - Ran `git diff --stat`
>
> </details>
</details>

Implemented.

Changes made:
- [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py)
  - Adds `--mapping`, default `.mapping.json`.
  - Adds `--fresh`.
  - Loads existing mapping by default and resumes from it.
  - Reuses mapped categories/articles instead of cloning duplicates.
  - Skips inserting duplicate `phpkb_relations` if the relation already exists.
  - Writes mapping atomically via temp file replace.
  - Replaces `SELECT MAX(article_id)` / `SELECT MAX(category_id)` with `cursor.lastrowid`.

- Updated:
  - [test_phpkb_clone.py](./.tests/test_phpkb_clone.py)
  - [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
  - [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)
  - [python_scripts_roster.md](./python_scripts_roster.md)

Verified without DB calls:

```powershell
python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py -q
```

Result: `23 passed`.

`cursor.lastrowid` means: after this connection executes an `INSERT` into a table with an auto-increment primary key, MySQL tells the client which auto-generated ID was assigned by that insert.

So instead of:

```sql
INSERT INTO phpkb_articles SELECT 0,tmp.* FROM tmp;
SELECT MAX(article_id) FROM phpkb_articles;
```

we now do conceptually:

```python
cursor.execute("INSERT INTO phpkb_articles SELECT 0,tmp.* FROM tmp")
new_article_id = cursor.lastrowid
```

Why it is safer: `MAX(article_id)` asks “what is the largest article ID in the whole table right now?” If someone else inserts a row at the same time, that can be the wrong row. `cursor.lastrowid` asks “what ID did my insert just generate on this connection?” That is the one we need.

> The cloning now supports resuming, right?
>
> D:\Repo\CBAP_MKDOCS_RU\.tests The tests for cloning workflow test behavior rather than implementaion, as per best parcitces, Right?

Yes, cloning now supports resuming.

`phpkb_clone.py` now loads the mapping file at startup:

```powershell
--mapping .mapping.json
```

Default is `.mapping.json`. If it already contains:

```json
{
  "Categories": { "798": "920" },
  "Articles": { "4918": "6001" }
}
```

then the clone reuses those mapped IDs instead of cloning those categories/articles again. `--fresh` is the opposite mode: it refuses to run if the mapping file already exists.

On the tests: mostly yes, they are behavior-focused, but not perfectly pure black-box.

Good behavior-level coverage now includes:
- already mapped article is reused;
- article dependents are not duplicated for mapped articles;
- existing relation is skipped;
- category mapping is reused;
- existing mapping file is loaded;
- `--fresh` refuses an existing mapping;
- CLI accepts mapping/resume flags.

There are a couple of implementation-aware assertions, intentionally:
- tests check that `SELECT MAX(article_id)` / `SELECT MAX(category_id)` are no longer used;
- tests use `cursor.lastrowid`.

That’s a reasonable exception here because the bug/risk was specifically the implementation strategy for retrieving generated IDs. So the tests are mainly behavioral, with a small targeted guard against the dangerous old implementation.

> tests check that SELECT MAX(article_id) / SELECT MAX(category_id) are no longer used;
>
> if we already commited the change, why would we need this test?

Because the commit only records the fix once. The test keeps the fix from quietly disappearing later.

This specific assertion is a regression guard. The risk we fixed was not just “the output is wrong in a normal fake DB test”; it was “the implementation can choose the wrong row under concurrent inserts.” A normal behavior test with a fake cursor might still pass even if someone later reintroduces:

```sql
SELECT MAX(article_id)
```

because the fake cursor would happily return the expected value.

So the test says: this particular strategy is forbidden because it is concurrency-unsafe.

That said, you’re right to question it. In general, tests should prefer behavior over implementation. Here I’d keep one narrow implementation guard because it protects a real production safety property. If we wanted to make it more behavior-like, we could instead simulate this scenario:

- insert returns `lastrowid = 9001`;
- fake `SELECT MAX(article_id)` would return `9999`;
- assert cloned ID is `9001`.

That tests the behavior we care about: “uses the ID generated by this insert, not the global max.” It’s cleaner than checking for the literal SQL string.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py
>
> document

<details><summary>2 previous messages</summary>

> I’ll add a clear module docstring to the related-topics helper, similar to the other cloning utilities, and leave its behavior unchanged.
>
> <details><summary>Edited 1 file, ran 1 command</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py` (+27 -5)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py`
>
> </details>
</details>

Documented [phpkb_clone_replace_related_topics.py](./utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py:1) with a module docstring explaining:

- it is a local Markdown formatter, not a DB script;
- it does not use `.mapping.json`;
- it walks the hardcoded `docs/ru/using_the_system`;
- it wraps related-topic blocks in `<div class="relatedTopics" markdown="block">`;
- it converts bold reference links into italic bullet links;
- it rewrites files in place;
- it should get CLI/dry-run support before being broadened.

Verified syntax:

```powershell
python -m py_compile utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py
```

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_replace_related_topics.py is it related to cloning or more for post-import cleanup?

It is **more post-import / local Markdown cleanup** than true cloning.

[phpkb_clone_replace_related_topics.py](./utilities/phpkb_cloning/phpkb_clone_replace_related_topics.py) does not:

- connect to PHPKB;
- read `.mapping.json`;
- update cloned DB articles;
- remap article/category IDs;
- know anything about source or target product versions.

It only rewrites local Markdown files under:

```text
docs/ru/using_the_system
```

Specifically, it reformats related-topic sections after the docs have already been imported/generated/migrated into local Markdown.

So I’d classify it as:

```text
Post-import Markdown cleanup helper
```

It may live near the cloning workflow because that annual workflow can include “clean up the local docs after migration,” but it is not a PHPKB cloning utility in the strict sense.

> D:\Repo\CBAP_MKDOCS_RU\phpkb_replace_related_topics.py, moved it here. Redocument

<details><summary>4 previous messages</summary>

> I’ll check where the file lives now and update the documentation to match the new root-level, post-import cleanup role. I’ll keep the code behavior unchanged unless the move left stale paths in the skill/roster.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `Get-Content -Path phpkb_replace_related_topics.py`
> - Ran `rg "phpkb_clone_replace_related_topics|phpkb_replace_related_topics" -n python_scripts_roster.md .agents\skills\phpkb-cloning utilities phpkb_replace_related_topics.py`
>
> </details>
>
> The move is visible as a delete from `utilities/phpkb_cloning` plus a new root file. I’ll update the root script’s docstring wording and remove the stale cloning-skill references so it no longer looks like an operational clone script.
>
> <details><summary>Edited 4 files, ran 3 commands</summary>
>
> - Wrote `./phpkb_replace_related_topics.py` (+11 -9)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+2 -3)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+3 -2)
> - Wrote `./python_scripts_roster.md` (+3 -2)
> - Ran `python -m py_compile phpkb_replace_related_topics.py`
> - Ran `rg "phpkb_clone_replace_related_topics|phpkb_replace_related_topics" -n python_scripts_roster.md .agents\skills\phpkb-cloning phpkb_replace_related_topics.py utilities`
> - Ran `git status --short --branch`
>
> </details>
</details>

Redocumented it as root-level post-import cleanup.

Updated:
- [phpkb_replace_related_topics.py](./phpkb_replace_related_topics.py:1)
  - Docstring now says it is for post-import/local Markdown cleanup.
  - Explicitly says it is not part of PHPKB DB cloning, does not use `.mapping.json`, and does not remap IDs.

- [python_scripts_roster.md](./python_scripts_roster.md)
  - Moved it into the root script roster as `phpkb_replace_related_topics.py`.
  - Removed it from the PHPKB cloning script table.
  - Classified it under “Post-import Markdown cleanup.”

- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
  - Removed it from the cloning utilities table.
  - Notes it as a root-level post-import cleanup helper, not DB cloning.

- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)
  - Removed it from the cloning script list.
  - Added a note that it is outside the DB cloning scripts.

Verified:

```powershell
python -m py_compile phpkb_replace_related_topics.py
```

> git diff and meaningful commit

<details><summary>6 previous messages</summary>

> I’ll review the current diff so the commit message matches the whole batch, then stage and commit it. This includes the resume-safe clone changes plus the related-topics move/documentation.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git diff --name-status`
> - Ran `git log -n 3 --pretty=%B`
>
> </details>
>
> The diff shows one untracked moved file, so I’ll stage with `-A` to preserve the delete/add pair correctly. I’ll run the focused test set once more before committing.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py -q`
> - Ran `git add -A`
> - Ran `git status --short --branch`
> - Ran `git diff --cached --stat`
> - Ran `git diff --cached --name-status`
>
> </details>
>
> Staged diff is cleanly recognized as a rename for the related-topics helper, plus the resumable clone changes. I’m committing this as a safety/resume improvement.
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `git commit -m "[#5] Make PHPKB cloning resumable"`
> - Ran `git status --short --branch`
>
> </details>
</details>

Diff reviewed, tests passed, and commit created.

Commit: `0ee5aabe [#5] Make PHPKB cloning resumable`

Included:
- resumable `.mapping.json` loading in `phpkb_clone.py`;
- `--mapping` and `--fresh`;
- `cursor.lastrowid` instead of `SELECT MAX(...)`;
- relation duplicate check;
- atomic mapping writes;
- behavior tests for resume/fresh/mapping reuse;
- moved related-topics helper to root as `phpkb_replace_related_topics.py`;
- updated skill docs and roster.

Verification:

```powershell
python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py -q
```

Result: `23 passed`.

Branch `platform_v5` is ahead of origin by 2 commits. I did not push.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_article_ids.py is this also a local post-import formatter prototapy not PHP cloning related?

Yes. [phpkb_clone_update_article_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_article_ids.py) is also **not really PHPKB cloning-related**.

It is best classified as:

```text
Local post-import Markdown hyperlink lookup prototype
```

What it does:
- scans a hardcoded local Markdown file, `article-2198.md`;
- finds direct `kb.comindware.ru` article URLs;
- extracts article IDs from those URLs;
- looks up matching reference labels in [hyperlinks_mkdocs_to_kb_map.md](./docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md);
- prints the matching labels.

What it does **not** do:
- no DB connection;
- no PHPKB cloning;
- no `.mapping.json`;
- no article/category ID remapping;
- no V5/V6 migration logic;
- no file rewrite;
- no proper CLI;
- no `__main__` guard around the hardcoded execution.

So yes, it probably should be moved out of `utilities/phpkb_cloning/`, similar to `phpkb_replace_related_topics.py`, unless you want to first turn it into a real clone/migration helper.

> I moved phpkb_clone_update_article_ids.py to D:\Repo\CBAP_MKDOCS_RU\phpkb_update_article_ids.py
>
> Reducment

<details><summary>4 previous messages</summary>

> I’ll redocument it in its new root-level role and clean up stale cloning-skill references, the same way we did for related topics.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `rg "phpkb_clone_update_article_ids|phpkb_update_article_ids" -n python_scripts_roster.md .agents\skills\phpkb-cloning utilities phpkb_update_article_ids.py`
> - Ran `Get-Content -Path phpkb_update_article_ids.py`
>
> </details>
>
> The moved file already has a useful warning docstring, but I’ll retitle it as a root-level post-import lookup prototype and remove it from the cloning utility list.
>
> <details><summary>Edited 4 files, ran 3 commands</summary>
>
> - Wrote `./phpkb_update_article_ids.py` (+9 -8)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+3 -4)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+2 -2)
> - Wrote `./python_scripts_roster.md` (+2 -2)
> - Ran `python -m py_compile phpkb_update_article_ids.py`
> - Ran `git status --short --branch`
> - Ran `rg "phpkb_clone_update_article_ids|phpkb_update_article_ids" -n python_scripts_roster.md .agents\skills\phpkb-cloning phpkb_update_article_ids.py utilities`
>
> </details>
</details>

Redocumented it as a root-level post-import prototype.

Updated:
- [phpkb_update_article_ids.py](./phpkb_update_article_ids.py:1)
  - Docstring now says it is for local Markdown analysis after import/migration.
  - Explicitly says it is not DB cloning, does not use `.mapping.json`, does not remap IDs, and does not format migrated hyperlinks.

- [python_scripts_roster.md](./python_scripts_roster.md)
  - Added `phpkb_update_article_ids.py` to the root script roster.
  - Removed stale `utilities/phpkb_cloning/phpkb_clone_update_article_ids.py`.
  - Classified it under post-import Markdown cleanup.

- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
  - Removed it from the cloning utilities table.
  - Notes it as a root-level post-import lookup prototype.

- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)
  - Removed it from the DB cloning script list.
  - Added a note that it is not part of PHPKB DB cloning.

Verified:

```powershell
python -m py_compile phpkb_update_article_ids.py
```

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py
> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning\phpkb_clone.py
>
> Document

<details><summary>4 previous messages</summary>

> I’ll add top-level documentation to both core cloning utilities, keeping behavior unchanged. Then I’ll run syntax and the focused tests so the docs edits don’t accidentally disturb anything.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py -TotalCount 40`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py -TotalCount 40`
> - Ran `git status --short --branch`
>
> </details>
>
> There are already uncommitted move/doc updates for the article-ID prototype; I’ll leave those intact and only add docstrings to the two requested clone utilities.
>
> <details><summary>Edited 2 files, ran 3 commands</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+30 -0)
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py` (+20 -0)
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_mapped_ids.py -q`
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py`
> - Ran `git diff --stat`
>
> </details>
</details>

Documented both requested utilities.

Added module docstrings to:
- [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py:1)
  - explains DB-mutating role;
  - category/article cloning behavior;
  - attachment/custom data backrefs;
  - resumable mapping behavior;
  - `--mapping`, `--fresh`;
  - why `cursor.lastrowid` must be used instead of `SELECT MAX(...)`.

- [phpkb_clone_update_mapped_ids.py](./utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py:1)
  - explains it is local-file only;
  - documents `frontmatter-kbids`, `hyperlink-map`, and `all`;
  - documents article/category prefix-aware hyperlink updates;
  - notes dry-run default and `--write`.

Verified:

```powershell
python -m py_compile utilities\phpkb_cloning\phpkb_clone.py utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py
python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_mapped_ids.py -q
```

Result: `17 passed`.

> Git meaningful commit

<details><summary>4 previous messages</summary>

> I’ll package the latest documentation/move updates into a focused commit, keeping the existing unpushed commits as they are.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git diff --name-status`
> - Ran `git log -n 3 --pretty=%B`
>
> </details>
>
> The current changes are documentation-oriented plus the article-ID helper move. I’ll stage all of it so Git records the move correctly, then commit with the same `#5` prefix.
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `git add -A`
> - Ran `git status --short --branch`
> - Ran `git diff --cached --stat`
> - Ran `git diff --cached --name-status`
> - Ran `git commit -m "[#5] Document PHPKB cloning utilities"`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed.

Commit: `52c6ef96 [#5] Document PHPKB cloning utilities`

Included:
- docstrings for `phpkb_clone.py` and `phpkb_clone_update_mapped_ids.py`;
- moved `phpkb_update_article_ids.py` out of cloning utilities;
- updated PHPKB cloning skill docs and roster references.

Branch `platform_v5` is ahead of origin by 3 commits. I did not push.

> If we run the cloning pipeline we will get a .v6mapping.json file with new mapping or just  mapping.json?

By default: **just `.mapping.json`**.

Current behavior:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py ...
```

writes/updates:

```text
.mapping.json
```

because `--mapping` defaults to `.mapping.json`.

If you want a V6-specific mapping file, run it explicitly like this:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --mapping .v6mapping.json --fresh --category-id <source_id> --target-parent-id <target_parent_id>
```

Then the clone script will write:

```text
.v6mapping.json
```

And the downstream tools should use the same file:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .v6mapping.json --category-id <new_category_id> --old-version 5.0 --new-version 6.0
```

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .v6mapping.json --target all --write
```

So: **automatic default is `.mapping.json`; recommended V5 to V6 run should explicitly use `.v6mapping.json`.**

> Is this idea documented in the cloning skill?

<details><summary>5 previous messages</summary>

> I’ll check the skill docs for explicit `.v6mapping.json` guidance. If it’s missing, I’ll add it so the workflow does not accidentally default to `.mapping.json` for V5 to V6.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg "v6mapping|\.mapping-v6|\.mapping\.json|--mapping" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
>
> </details>
>
> It’s partially documented, but the workflow still uses `.mapping-v6.json` in one example and mostly defaults to `.mapping.json`. I’ll make the V5 to V6 recommendation explicit as `.v6mapping.json` and update the downstream examples to use the same file.
>
> <details><summary>Edited 2 files, ran 2 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+8 -6)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+1 -0)
> - Ran `rg "v6mapping|mapping-v6|\.mapping\.json|--mapping" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git diff -- .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
>
> </details>
>
> It was only **partially** documented. The workflow mentioned using a separate mapping file, but the example used `.mapping-v6.json`, and most downstream examples still used `.mapping.json`.
</details>

It was only **partially** documented before. The workflow mentioned using a separate mapping file, but the example used `.mapping-v6.json`, and several examples still implied `.mapping.json`.

I updated the cloning skill docs to make the V5 to V6 idea explicit:

- Prefer `--mapping .v6mapping.json` for V5 to V6 migrations.
- Pass the same `.v6mapping.json` to post-clone scripts.
- Updated workflow examples for:
  - clone
  - DB link update
  - local mapped ID update

Key documented example now:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --fresh --category-id 798 --target-parent-id 1000
```

And downstream:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_links.py --mapping .v6mapping.json --category-id 900
```

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_mapped_ids.py --mapping .v6mapping.json --target all
```

> CLI mode is designed for scripted annual migrations:
>
> here and everywhere it's not necessarly annual but per-release migrations

<details><summary>2 previous messages</summary>

> Good catch. I’ll replace the “annual” framing with “per-release” wherever it describes the cloning workflow, since this can happen for any product release cadence.
>
> <details><summary>Edited 3 files, ran 4 commands</summary>
>
> - Ran `rg "annual|Annual" -n utilities\phpkb_cloning .agents\skills\phpkb-cloning python_scripts_roster.md`
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_update_links.py` (+1 -1)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+1 -1)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+1 -1)
> - Ran `rg "annual|Annual" -n utilities\phpkb_cloning .agents\skills\phpkb-cloning python_scripts_roster.md`
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_update_links.py`
> - Ran `git diff --stat`
>
> </details>
</details>

Fixed. Replaced the “annual migration/workflow” wording with “per-release” in:

- [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py:14)
- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md:22)
- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md:68)

Verified no remaining `annual` references in the cloning utility/docs scope, and syntax check passed for the updated Python file.

> D:\Repo\CBAP_MKDOCS_RU\utilities\phpkb_cloning
> D:\Repo\CBAP_MKDOCS_RU\.agents\skills\phpkb-cloning
>
> All up-to-date, well-documented, and ready for production?

<details><summary>4 previous messages</summary>

> I’ll do a read-only readiness pass across the cloning utilities and the skill docs, plus run the focused dry tests. I won’t touch code unless I find a documentation mismatch that you ask me to fix.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-ChildItem -Path utilities\phpkb_cloning -File | Select-Object Name,Length`
> - Ran `Get-ChildItem -Path .agents\skills\phpkb-cloning -Recurse -File | Select-Object FullName,Length`
> - Ran `rg "annual|phpkb_clone_update_article_ids|phpkb_clone_replace_related_topics|mapping-v6|TODO|FIXME|SELECT MAX\((article_id|category_id)\)" -n utilities\phpkb_cloning .agents\skills\phpkb-cloning`
> - Ran `git status --short --branch`
>
> </details>
>
> The folder now contains only the three true cloning/migration utilities, and the stale prototype/helper names are gone from the skill scope. I do see three uncommitted documentation wording changes, so “up-to-date” is true in the working tree but not yet committed. I’m running the focused tests now.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py -q`
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py utilities\phpkb_cloning\phpkb_clone_update_links.py utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py`
> - Ran `git diff -- .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md utilities\phpkb_cloning\phpkb_clone_update_links.py`
>
> </details>
</details>

Mostly yes, with one important caveat: **ready for a controlled production run, not “fire and forget.”**

What looks good:
- `utilities/phpkb_cloning` now contains only the real cloning/migration utilities:
  - `phpkb_clone.py`
  - `phpkb_clone_update_links.py`
  - `phpkb_clone_update_mapped_ids.py`
- Skill docs are aligned with the scripts.
- Stale helper scripts were moved out of the cloning folder.
- `.v6mapping.json` guidance is now documented for V5 to V6.
- “annual” wording was corrected to “per-release.”
- Syntax checks passed.
- Focused dry tests passed: `23 passed`.

Production caveats:
- I did **not** run a live PHPKB DB clone in this check.
- `phpkb_clone.py` and `phpkb_clone_update_links.py` are DB-mutating tools, so production readiness still requires a DB backup, correct `SERVER_PROFILE`, dry-run where available, and a quiet/content-freeze window.
- There are 3 uncommitted documentation wording changes:
  - `.agents/skills/phpkb-cloning/SKILL.md`
  - `.agents/skills/phpkb-cloning/references/workflow.md`
  - `utilities/phpkb_cloning/phpkb_clone_update_links.py`

So my verdict: **functionally and documentation-wise ready in the working tree; not fully “up-to-date” in Git until those last doc changes are committed.**

> git meaningful commit

<details><summary>2 previous messages</summary>

> I’ll commit the remaining per-release wording and `.v6mapping.json` documentation updates.
>
> <details><summary>Ran 8 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git log -n 3 --pretty=%B`
> - Ran `git add -A`
> - Ran `git diff --cached --stat`
> - Ran `git status --short --branch`
> - Ran `git commit -m "[#5] Clarify PHPKB release migration docs"`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed.

Commit: `c5b214c3 [#5] Clarify PHPKB release migration docs`

Branch `platform_v5` is ahead of origin by 1 commit. I did not push.

> do we have a script to drop the cloned cats and articles from the phpkb_clone.py run? like read them from the mapping json? Could be useful to cleanup a mess if something goes wrong?

<details><summary>2 previous messages</summary>

> I’ll check the repo for any existing rollback/delete helper before answering. If there isn’t one, I’ll outline what a safe cleanup script would need to delete and in what order.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg "delete|DELETE|drop|DROP|mapping|rollback|cleanup|remove" -n utilities\phpkb_cloning tools .agents\skills\phpkb-cloning python_scripts_roster.md`
> - Ran `Get-ChildItem -Path utilities\phpkb_cloning -File | Select-Object Name`
> - Ran `git status --short --branch`
>
> </details>
</details>

No, we don’t currently have a rollback/drop script for a bad `phpkb_clone.py` run.

Right now the pipeline can create and use a mapping JSON, but there is no helper that reads `.mapping.json` / `.v6mapping.json` and deletes the cloned DB rows.

I agree it would be useful, but it needs to be deliberately conservative because it would be the most dangerous script in the folder.

A safe rollback helper should probably be something like:

```text
utilities/phpkb_cloning/phpkb_clone_rollback.py
```

Expected behavior:

- Read `--mapping .v6mapping.json`.
- Dry-run by default.
- Require `--write` to mutate DB.
- Require a second confirmation flag like `--confirm-delete-cloned-content`.
- Delete only IDs present as **values** in the mapping, never keys.
- Delete in dependency order:
  1. `phpkb_attachments` where `article_id in mapped article values`
  2. `phpkb_custom_data` where `article_id in mapped article values`
  3. `phpkb_relations` where `article_id in mapped article values` or `category_id in mapped category values`
  4. `phpkb_articles` where `article_id in mapped article values`
  5. `phpkb_categories` where `category_id in mapped category values`
- Delete categories deepest-first if we can resolve depth, or at minimum delete by mapped IDs after relations/articles are gone.
- Print exact counts before writing.
- Optionally write a rollback report file.

I would not use `DROP`; this should be `DELETE FROM ... WHERE id IN (...)`. “Drop” would mean dropping whole tables, which we absolutely do not want.

So the answer is: **not yet, but yes, it would be a very good safety tool before a production clone run.**

> Implement

<details><summary>11 previous messages</summary>

> I’ll add a rollback utility with dry-run by default and two-part confirmation for actual deletes. I’ll also wire it into the skill docs and add tests that verify it deletes only mapped target IDs, in the safe dependency order, without touching a DB.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py -TotalCount 80`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `Get-Content -Path python_scripts_roster.md`
> - Ran `git status --short --branch`
>
> </details>
>
> I’ll build this as `phpkb_clone_rollback.py` in the cloning utilities folder. It will be DB-mutating only with `--write --confirm-delete-cloned-content`; otherwise it just reports what would be deleted.
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone_rollback.py` (+170 -0)
>
> </details>
>
> The rollback script is in place. I’m adding tests for the safety-critical parts: mapped values only, dry-run without deletes, destructive flag validation, and delete order.
>
> <details><summary>Created 1 file</summary>
>
> - Wrote `./.tests/test_phpkb_clone_rollback.py` (+122 -0)
>
> </details>
>
> Now I’m wiring the rollback script into the skill and roster so it’s visible as part of the production safety story, with the same “dry-run first” language.
>
> <details><summary>Edited 3 files, ran 3 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+11 -0)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+19 -0)
> - Wrote `./python_scripts_roster.md` (+2 -1)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone_rollback.py .tests\test_phpkb_clone_rollback.py`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_rollback.py --help`
> - Ran `python -m pytest .tests\test_phpkb_clone_rollback.py -q`
>
> </details>
>
> The new rollback helper passes its focused tests and its help output is clear. I’m running the full cloning test set now to make sure the folder stays coherent.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone_rollback.py -q`
> - Ran `rg "phpkb_clone_rollback|confirm-delete|rollback" -n utilities\phpkb_cloning .agents\skills\phpkb-cloning python_scripts_roster.md .tests\test_phpkb_clone_rollback.py`
> - Ran `git diff --stat`
> - Ran `git status --short --branch`
>
> </details>
>
> <details><summary>Plan</summary>
>
> - [x] Add rollback utility for mapped cloned rows
> - [x] Add dry unit tests for ID extraction and delete order
> - [x] Document rollback in skill and roster
> - [x] Run focused verification
>
> </details>
</details>

Implemented a rollback helper.

Added:
- [phpkb_clone_rollback.py](./utilities/phpkb_cloning/phpkb_clone_rollback.py)
- [test_phpkb_clone_rollback.py](./.tests/test_phpkb_clone_rollback.py)

Behavior:
- Reads mapping JSON, default `.mapping.json`.
- Uses only mapped target IDs, meaning mapping values, never source keys.
- Dry-run by default.
- Requires both flags for deletion:

```powershell
--write --confirm-delete-cloned-content
```

- Deletes in this order:
  1. `phpkb_attachments` by cloned `article_id`
  2. `phpkb_custom_data` by cloned `article_id`
  3. `phpkb_relations` by cloned `article_id`
  4. `phpkb_relations` by cloned `category_id`
  5. `phpkb_articles` by cloned `article_id`
  6. `phpkb_categories` by cloned `category_id`

Dry-run example:

```powershell
python utilities/phpkb_cloning/phpkb_clone_rollback.py --profile cmw --mapping .v6mapping.json
```

Actual delete:

```powershell
python utilities/phpkb_cloning/phpkb_clone_rollback.py --profile cmw --mapping .v6mapping.json --write --confirm-delete-cloned-content
```

Also updated the PHPKB cloning skill docs, workflow reference, and scripts roster.

Verification:

```powershell
python -m py_compile utilities\phpkb_cloning\phpkb_clone_rollback.py .tests\test_phpkb_clone_rollback.py
python utilities\phpkb_cloning\phpkb_clone_rollback.py --help
python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone_rollback.py -q
```

Result: `29 passed`.

No live DB calls were made.

> git commit push

<details><summary>2 previous messages</summary>

> I’ll commit the rollback helper and documentation, then push the branch.
>
> <details><summary>Ran 9 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git log -n 3 --pretty=%B`
> - Ran `git diff --stat`
> - Ran `git add -A`
> - Ran `git diff --cached --stat`
> - Ran `git status --short --branch`
> - Ran `git commit -m "[#5] Add PHPKB clone rollback tool"`
> - Ran `git push`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed and pushed.

Commit: `f6d0f370 [#5] Add PHPKB clone rollback tool`

Pushed `platform_v5` to the configured remotes. Working tree is clean.

> Is there a way to implement dry run mode for to the manin cloning scripts? Not sure it would be practical or useful though....
>
> You wrote:
> phpkb_clone.py and phpkb_clone_update_links.py are DB-mutating tools, so production readiness still requires a DB backup, correct SERVER_PROFILE, dry-run where available, and a quiet/content-freeze window.

Yes, but with an important distinction:

- For [phpkb_clone_update_links.py](./utilities/phpkb_cloning/phpkb_clone_update_links.py), dry-run is practical and already implemented.
- For [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py), a true dry-run is possible but less useful unless we define it as a **clone plan**, not as “simulate every INSERT.”

For `phpkb_clone.py`, I’d implement dry-run like this:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --mapping .v6mapping.json --category-id 798 --target-parent-id 1000 --dry-run
```

It should:
- connect read-only;
- fetch the category tree;
- count categories that would be cloned;
- count visible/public articles that would be cloned;
- account for existing mapping entries and show reused vs new;
- count attachment/custom data rows for affected articles;
- report target parent/category decisions;
- not create temp tables;
- not insert rows;
- not write mapping JSON.

Example output:

```text
Mode: dry-run
Mapping: .v6mapping.json
Source category: 798
Target parent: 1000

Categories:
  would clone: 42
  already mapped/reused: 3

Articles:
  would clone: 318
  already mapped/reused: 12
  relations to create: 318

Backrefs:
  attachment rows to link: 84
  custom data rows to clone: 9

No DB rows were inserted.
No mapping file was written.
```

What it cannot fully guarantee:
- exact new article/category IDs, because those only exist after inserts;
- all DB constraint/runtime behavior, because PHPKB has no declared foreign keys and MyISAM-style tables;
- final relation shape if data changes between dry-run and write.

So yes, it is useful as a **preflight / scope report**, not as a perfect transactional simulation.

My recommendation:
- Keep `phpkb_clone_update_links.py` dry-run as-is.
- Add `--dry-run` to `phpkb_clone.py` only if we want a preflight summary before production clone.
- Name it clearly in docs as “preflight dry-run” so nobody assumes it proves the write path will be identical.

> Could also be useful for resume operations?
>
> Implement?

<details><summary>11 previous messages</summary>

> Yes, it can be especially useful for resume operations: it can show what the existing mapping will reuse and what the next run would still create. I’ll implement it as a preflight dry-run for `phpkb_clone.py`, not a fake insert simulation, and add tests/docs around that behavior.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `rg "def cloneCategoryChildren|def cloneArticlesInCategory|def cloneArticle|def run_cli|def parse_args|def initializeMapping|def updateMappingJson" -n utilities\phpkb_cloning\phpkb_clone.py`
> - Ran `Get-Content -Path utilities\phpkb_cloning\phpkb_clone.py`
> - Ran `Get-Content -Path .tests\test_phpkb_clone.py`
> - Ran `git status --short --branch`
>
> </details>
>
> I’m going to keep the write path untouched and add separate planning functions for dry-run. For category trees the preflight will walk the tree, count already-mapped versus would-clone categories/articles, and count attachment/custom-data rows for articles that are not already mapped.
>
> <details><summary>Edited 2 files</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+2 -2)
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+149 -1)
>
> </details>
>
> The preflight mode is now separate from the mutation code path. I’m adding tests to prove `--dry-run` plans work, reuse mapping entries, and avoid mapping writes or clone calls.
>
> <details><summary>Edited 1 file</summary>
>
> - Wrote `./.tests/test_phpkb_clone.py` (+66 -0)
>
> </details>
>
> I’m updating the skill docs next, because dry-run is valuable only if the operational workflow makes clear it’s a preflight report and does not create IDs.
>
> <details><summary>Edited 3 files, ran 3 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+2 -0)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+7 -0)
> - Wrote `./python_scripts_roster.md` (+1 -1)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py`
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --help`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
>
> </details>
>
> The focused clone tests pass and the help text exposes `--dry-run`. I’m running the full PHPKB cloning test set now, including rollback and post-clone helpers.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone_rollback.py -q`
> - Ran `git diff --stat`
> - Ran `rg "dry-run|preflight|No DB rows were inserted|No mapping file was written" -n utilities\phpkb_cloning\phpkb_clone.py .agents\skills\phpkb-cloning python_scripts_roster.md .tests\test_phpkb_clone.py`
> - Ran `git status --short --branch`
>
> </details>
>
> <details><summary>Plan</summary>
>
> - [x] Add preflight dry-run mode to phpkb_clone.py
> - [x] Test dry-run planning and resume reporting
> - [x] Document dry-run/preflight in skill docs
> - [x] Run focused verification
>
> </details>
</details>

Implemented `--dry-run` for [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py).

What it does:
- Works for scripted `--category-id` and `--article-id` runs.
- Loads the selected mapping first, so it is useful for resume checks.
- Reports:
  - categories seen;
  - categories that would clone;
  - categories reused from mapping;
  - articles seen;
  - articles that would clone;
  - articles reused from mapping;
  - relations to create/check;
  - attachment rows to link;
  - custom data rows to clone.
- Does not insert rows.
- Does not create temp tables.
- Does not clone backrefs.
- Does not write the mapping file.

Example:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --target-parent-id 1000 --dry-run
```

It is explicitly a **preflight/resume report**, not a perfect simulation: it cannot know final new IDs because MySQL generates those only during real inserts.

Updated:
- [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py)
- [test_phpkb_clone.py](./.tests/test_phpkb_clone.py)
- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)
- [python_scripts_roster.md](./python_scripts_roster.md)

Verification:

```powershell
python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py
python utilities\phpkb_cloning\phpkb_clone.py --help
python -m pytest .tests\test_phpkb_clone.py .tests\test_phpkb_clone_update_links.py .tests\test_phpkb_clone_update_mapped_ids.py .tests\test_phpkb_clone_rollback.py -q
```

Result: `33 passed`.

> git meaningful commit and push
>
> how do we specify the category to clone with our skills and will it be clonet adjacent or to a certain parent cat?

<details><summary>2 previous messages</summary>

> I’ll commit and push the dry-run preflight work first, then I’ll answer the category-targeting question from the current CLI and skill workflow.
>
> <details><summary>Ran 9 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git log -n 3 --pretty=%B`
> - Ran `git diff --stat`
> - Ran `git add -A`
> - Ran `git diff --cached --stat`
> - Ran `git status --short --branch`
> - Ran `git commit -m "[#5] Add PHPKB clone dry-run preflight"`
> - Ran `git push`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed and pushed.

Commit: `38067cf0 [#5] Add PHPKB clone dry-run preflight`

Working tree is clean.

For category cloning, the source category is specified with:

```powershell
--category-id <source_category_id>
```

Where the clone lands depends on `--target-parent-id`:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --target-parent-id 1000
```

That clones source category `798` and its visible/public child tree **under parent category `1000`**.

If you omit `--target-parent-id`:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798
```

then it clones the source category under the **same parent ID as the original category**. In practice, that means the cloned category becomes adjacent/sibling to the original.

Recommended production flow:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --target-parent-id 1000 --dry-run
```

Then, if the preflight report looks right:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --fresh --category-id 798 --target-parent-id 1000
```

Use `--fresh` only for the first real run with a new mapping file. For resume, omit `--fresh` so it reuses `.v6mapping.json`.

> Is this well-documented?

<details><summary>4 previous messages</summary>

> I’ll check the cloning skill and workflow docs for whether source category vs target parent is explicit enough. If it’s vague, I’ll tighten the docs.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg "category-id|target-parent|same parent|adjacent|sibling|dry-run|fresh" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md utilities\phpkb_cloning\phpkb_clone.py python_scripts_roster.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
>
> </details>
>
> It’s documented by example, but not quite explicitly enough: the current workflow shows `--category-id` and `--target-parent-id`, but does not spell out that omitting `--target-parent-id` makes the clone a sibling of the source. I’ll tighten that now.
>
> <details><summary>Edited 2 files, ran 2 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+3 -0)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+5 -0)
> - Ran `git diff -- .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `rg "target-parent-id|adjacent|source category" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
>
> </details>
</details>

It was documented by example, but not explicit enough.

I updated the skill docs to spell it out:

- `--category-id` is the source category tree to clone.
- `--target-parent-id` is the destination parent category for the cloned root category.
- If `--target-parent-id` is omitted, the cloned root category keeps the source category’s parent ID, so the clone is created adjacent to the source category.

Updated:
- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)

> other scripts, flow and flags for cloining are well documented?

<details><summary>4 previous messages</summary>

> I’ll do a documentation coverage pass across the cloning scripts, workflow, and skill text, then tell you where it’s solid and where any gaps remain.
>
> <details><summary>Ran 8 commands</summary>
>
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --help`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_update_links.py --help`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_update_mapped_ids.py --help`
> - Ran `python utilities\phpkb_cloning\phpkb_clone_rollback.py --help`
> - Ran `rg "phpkb_clone.py|phpkb_clone_update_links.py|phpkb_clone_update_mapped_ids.py|phpkb_clone_rollback.py|--profile|--mapping|--fresh|--dry-run|--write|--confirm-delete|--old-version|--new-version|--replace-product-names|--target|--hyperlinks-file|--target-parent-id|--target-category-id|--article-id|--category-id" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md python_scripts_roster.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git status --short --branch`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
>
> </details>
>
> The coverage is good now, but I see two small documentation gaps worth tightening: `phpkb_clone_update_links.py --category-id` should explicitly mean the cloned category tree to update, and the skill examples should consistently point V5 to V6 work at `.v6mapping.json`. I’ll make that small doc pass.
>
> <details><summary>Edited 2 files, ran 4 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+4 -2)
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+7 -1)
> - Ran `rg "--category-id|--article-id|--target-category-id|--target-parent-id|--mapping .v6mapping|--write|--dry-run|--confirm-delete|--target all" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git diff --stat`
> - Ran `git status --short --branch`
> - Ran `rg -e "--category-id|--article-id|--target-category-id|--target-parent-id|--mapping \.v6mapping|--write|--dry-run|--confirm-delete|--target all" -n .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
>
> </details>
</details>

Yes, they are now well documented.

Coverage is in three places:

- CLI `--help` for every cloning script:
  - `phpkb_clone.py`
  - `phpkb_clone_update_links.py`
  - `phpkb_clone_update_mapped_ids.py`
  - `phpkb_clone_rollback.py`

- Skill overview:
  - [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)

- Operational workflow:
  - [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)

I also tightened two remaining gaps:
- `phpkb_clone_update_links.py --category-id` is now documented as the **cloned category tree to update**, not the original source category.
- Article cloning is now explicit:
  - `--article-id` is the source article.
  - `--target-category-id` is the category that receives the cloned article.
  - if omitted, the clone is related to the source article’s first category.

Current uncommitted docs changes are only in:
- [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md)
- [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md)

> git commit and push

<details><summary>2 previous messages</summary>

> I’ll commit the final documentation clarifications and push them.
>
> <details><summary>Ran 7 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git log -n 3 --pretty=%B`
> - Ran `git add .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git commit -m "[#5] Clarify PHPKB clone targeting docs"`
> - Ran `git push`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed and pushed.

Commit: `0c9d2e3a [#5] Clarify PHPKB clone targeting docs`

Pushed `platform_v5` to the configured remotes. Working tree is clean.

> can we create platform_v6 branch for further work?

<details><summary>2 previous messages</summary>

> I’ll create and switch to a `codex/platform_v6` branch from the current clean `platform_v5` state, following the branch prefix convention.
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git rev-parse --abbrev-ref HEAD`
> - Ran `git switch -c codex/platform_v6`
> - Ran `git status --short --branch`
>
> </details>
</details>

Created and switched to branch `codex/platform_v6`.

Working tree is clean.

> What is the command for mySQL to create a complete DB backup? I do not think we can create a script for this that would be useful. So probably I'll just save the backup before any runs

Yes, best approach: make a DB backup manually before any clone run.

For a complete MySQL dump:

```powershell
mysqldump `
  -h <host> `
  -P <port> `
  -u <user> `
  -p `
  --default-character-set=utf8mb4 `
  --routines `
  --triggers `
  --events `
  --lock-tables `
  --databases phpkbv9 `
  > phpkbv9_backup_before_v6_clone.sql
```

For PHPKB specifically, because the schema notes say the DB uses MyISAM tables, prefer `--lock-tables` over pretending `--single-transaction` gives a consistent snapshot.

If you are running through an SSH tunnel, use the tunnel’s local host/port, for example:

```powershell
mysqldump `
  -h 127.0.0.1 `
  -P 3307 `
  -u <sql_user> `
  -p `
  --default-character-set=utf8mb4 `
  --routines `
  --triggers `
  --events `
  --lock-tables `
  --databases phpkbv9 `
  > phpkbv9_backup_before_v6_clone.sql
```

Quick sanity check after backup:

```powershell
Get-Item phpkbv9_backup_before_v6_clone.sql
```

And optionally inspect the first lines:

```powershell
Get-Content phpkbv9_backup_before_v6_clone.sql -TotalCount 20
```

The important bits are: backup the whole DB, include routines/triggers/events, use UTF-8, and take it during a quiet window because `--lock-tables` can block writes while dumping.

> I'll be on the machine directly via SSH

Then run `mysqldump` on the server itself, no tunnel needed.

Basic full DB backup:

```bash
mysqldump \
  -u <sql_user> \
  -p \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

If MySQL requires host explicitly:

```bash
mysqldump \
  -h localhost \
  -u <sql_user> \
  -p \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

Check it:

```bash
ls -lh phpkbv9_backup_before_v6_clone_*.sql
head -40 phpkbv9_backup_before_v6_clone_*.sql
```

If you want it compressed right away:

```bash
mysqldump \
  -u <sql_user> \
  -p \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  | gzip > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql.gz
```

Use `--lock-tables` because these PHPKB tables are MyISAM-style, so `--single-transaction` is not the right safety net here.

> Explain this command:
> mysqldump \
>   -h localhost \
>   -u <sql_user> \
>   -p \
>   --default-character-set=utf8mb4 \
>   --routines \
>   --triggers \
>   --events \
>   --lock-tables \
>   --databases phpkbv9 \
>   > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql

This command creates a full SQL backup of the `phpkbv9` MySQL database and saves it to a timestamped `.sql` file.

```bash
mysqldump \
  -h localhost \
  -u <sql_user> \
  -p \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

Line by line:

```bash
mysqldump
```

Runs the MySQL backup utility. It outputs SQL statements that can recreate the database.

```bash
-h localhost
```

Connects to MySQL on the same server where you are running the command.

```bash
-u <sql_user>
```

Uses the MySQL username you provide. Replace `<sql_user>` with the real DB user.

```bash
-p
```

Prompts you for the MySQL password. No space after `-p`; MySQL will ask interactively.

```bash
--default-character-set=utf8mb4
```

Uses full UTF-8 support, including Cyrillic and special characters.

```bash
--routines
```

Includes stored procedures and functions, if any.

```bash
--triggers
```

Includes triggers.

```bash
--events
```

Includes scheduled MySQL events.

```bash
--lock-tables
```

Locks tables during the dump so the backup is consistent. This matters because PHPKB uses MyISAM-style tables, where `--single-transaction` is not enough.

```bash
--databases phpkbv9
```

Backs up the whole `phpkbv9` database and includes `CREATE DATABASE` / `USE` statements in the dump.

```bash
>
```

Redirects the dump output into a file.

```bash
phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

Creates a filename with the current timestamp, for example:

```text
phpkbv9_backup_before_v6_clone_20260525_143012.sql
```

So the result is a restoreable SQL file containing the database backup as it existed at that moment.

> what if I am sudo

If you are `sudo` / root on the server, you may be able to run the dump without knowing the DB user password, depending on MySQL auth setup.

Try this first:

```bash
sudo mysqldump \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

If that fails with access denied, use MySQL root explicitly:

```bash
sudo mysqldump \
  -u root \
  -p \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

On some Linux installs, root login uses socket authentication, so this may work without `-p`:

```bash
sudo mysqldump \
  -u root \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

Important shell detail: if you use `sudo mysqldump ... > file.sql`, the redirection `>` is handled by your current shell, not by `sudo`. If the target folder needs root permission, use:

```bash
sudo sh -c 'mysqldump -u root --default-character-set=utf8mb4 --routines --triggers --events --lock-tables --databases phpkbv9 > /root/phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql'
```

Then check:

```bash
sudo ls -lh /root/phpkbv9_backup_before_v6_clone_*.sql
```

> this worked well
>
> sudo mysqldump \
>   --default-character-set=utf8mb4 \
>   --routines \
>   --triggers \
>   --events \
>   --lock-tables \
>   --databases phpkbv9 \
>   > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql

Perfect. That means the server’s MySQL auth lets `sudo mysqldump` access the DB, likely through root/socket credentials.

I’d do two quick checks:

```bash
ls -lh phpkbv9_backup_before_v6_clone_*.sql
```

```bash
head -40 phpkbv9_backup_before_v6_clone_*.sql
```

Optional but useful:

```bash
grep -m 1 "CREATE DATABASE" phpkbv9_backup_before_v6_clone_*.sql
grep -m 1 "CREATE TABLE.*phpkb_articles" phpkbv9_backup_before_v6_clone_*.sql
```

If the file size looks plausible and it contains `phpkbv9` plus PHPKB tables, you’ve got the safety net we wanted before clone runs.

> root@kb:/home/ased# ls
> cbap-mkdocs-ru  intelephense  phpkbv9.21.11.2024.sql  phpkbv9backup.18.11.2024.sql
> root@kb:/home/ased# sudo mysqldump \
>   --default-character-set=utf8mb4 \
>   --routines \
>   --triggers \
>   --events \
>   --lock-tables \
>   --databases phpkbv9 \
>   > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
> root@kb:/home/ased# ls
> cbap-mkdocs-ru  phpkbv9.21.11.2024.sql                              phpkbv9backup.18.11.2024.sql
> intelephense    phpkbv9_backup_before_v6_clone_20260525_170554.sql
> root@kb:/home/ased# ls -lh phpkbv9_backup_before_v6_clone_*.sql
> -rw-r--r-- 1 root root 1.5G May 25 17:06 phpkbv9_backup_before_v6_clone_20260525_170554.sql
> root@kb:/home/ased# head -40 phpkbv9_backup_before_v6_clone_*.sql
> -- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
> --
> -- Host: localhost    Database: phpkbv9
> -- ------------------------------------------------------
> -- Server version       8.0.45-0ubuntu0.22.04.1
>
> /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
> /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
> /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
> /*!50503 SET NAMES utf8mb4 */;
> /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
> /*!40103 SET TIME_ZONE='+00:00' */;
> /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
> /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
> /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
> /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
>
> --
> -- Current Database: `phpkbv9`
> --
>
> CREATE DATABASE /*!32312 IF NOT EXISTS*/ `phpkbv9` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
>
> USE `phpkbv9`;
>
> --
> -- Table structure for table `phpkb_api_keys`
> --
>
> DROP TABLE IF EXISTS `phpkb_api_keys`;
> /*!40101 SET @saved_cs_client     = @@character_set_client */;
> /*!50503 SET character_set_client = utf8mb4 */;
> CREATE TABLE `phpkb_api_keys` (
>   `key_id` int unsigned NOT NULL AUTO_INCREMENT,
>   `created_on` datetime NOT NULL,
>   `key_value` varchar(100) NOT NULL,
>   `key_md5` varchar(50) NOT NULL,
>   `key_status` enum('active','inactive') NOT NULL DEFAULT 'active',
>   PRIMARY KEY (`key_id`)
> ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;
> root@kb:/home/ased#
>
> can we document this in the cloning skill or readme under

<details><summary>4 previous messages</summary>

> Yes, this belongs in the PHPKB cloning skill, right before the clone step. I’ll add a concise “DB backup” section to the workflow reference with the exact sudo command and sanity checks from your successful run.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `Get-Content -Path .agents\skills\phpkb-cloning\SKILL.md`
>
> </details>
>
> I’m placing it under `references/workflow.md` as a “Database Backup” step before any clone run, and I’ll add a short pointer from `SKILL.md` so the skill always checks it.
>
> <details><summary>Edited 2 files, ran 3 commands</summary>
>
> - Wrote `./.agents/skills/phpkb-cloning/references/workflow.md` (+40 -5)
> - Wrote `./.agents/skills/phpkb-cloning/SKILL.md` (+1 -0)
> - Ran ``rg "Database Backup|mysqldump|phpkbv9_backup|lock-tables|single-transaction|full `?phpkbv9`? DB backup" -n .agents\skills\phpkb-cloning``
> - Ran `git diff -- .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md`
> - Ran `git status --short --branch`
>
> </details>
</details>

Documented it in the PHPKB cloning skill workflow.

Added:
- A required backup step before clone runs in [workflow.md](./.agents/skills/phpkb-cloning/references/workflow.md).
- A new **Database Backup** section with the exact working command:

```bash
sudo mysqldump \
  --default-character-set=utf8mb4 \
  --routines \
  --triggers \
  --events \
  --lock-tables \
  --databases phpkbv9 \
  > phpkbv9_backup_before_v6_clone_$(date +%Y%m%d_%H%M%S).sql
```

- Backup verification commands:

```bash
ls -lh phpkbv9_backup_before_v6_clone_*.sql
head -40 phpkbv9_backup_before_v6_clone_*.sql
```

- Sanity checks: file size, `Database: phpkbv9`, `CREATE DATABASE`, `USE phpkbv9`, and PHPKB tables.
- A safety checklist reminder in [SKILL.md](./.agents/skills/phpkb-cloning/SKILL.md).

> root@kb:/home/ased# grep -m 1 "CREATE DATABASE" phpkbv9_backup_before_v6_clone_*.sql
> CREATE DATABASE /*!32312 IF NOT EXISTS*/ `phpkbv9` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
> root@kb:/home/ased# grep -m 1 "CREATE TABLE.*phpkb_articles" phpkbv9_backup_before_v6_clone_*.sql
> CREATE TABLE `phpkb_articles` (
> root@kb:/home/ased#

That backup looks good.

You verified the key things:

- the dump exists and is large: `1.5G`;
- header says `Database: phpkbv9`;
- it contains:

```sql
CREATE DATABASE ... `phpkbv9`
```

- it contains the core table:

```sql
CREATE TABLE `phpkb_articles`
```

So yes, this is a valid-looking full DB backup to keep before the V6 clone run.

> how do I scp it to my machine

From your local machine, run:

```bash
scp root@kb:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql .
```

That copies it into your current local directory.

To copy to a specific local folder:

```bash
scp root@kb:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql /path/to/local/backups/
```

On Windows PowerShell, for example:

```powershell
scp root@kb:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql D:\Backups\
```

If `kb` is not resolvable from your local machine, use the server IP or hostname:

```bash
scp root@<server-ip>:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql .
```

> like so:
>
> scp ased@kb.comindware.ru:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql .

Yes, exactly:

```bash
scp ased@kb.comindware.ru:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql .
```

That means:

- connect as SSH user `ased`;
- to host `kb.comindware.ru`;
- copy `/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql`;
- into your current local directory, because of the final `.`.

After it finishes, check locally:

```bash
ls -lh phpkbv9_backup_before_v6_clone_20260525_170554.sql
```

On Windows PowerShell:

```powershell
Get-Item .\phpkbv9_backup_before_v6_clone_20260525_170554.sql
```

> git meaningful commit

<details><summary>2 previous messages</summary>

> I’ll commit the backup workflow documentation changes on the current `codex/platform_v6` branch.
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git log -n 3 --pretty=%B`
> - Ran `git add .agents\skills\phpkb-cloning\SKILL.md .agents\skills\phpkb-cloning\references\workflow.md && git commit -m "[#5] Document PHPKB backup workflow"`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed.

Commit: `fabf0ca6 [#5] Document PHPKB backup workflow`

Branch `codex/platform_v6` is ahead by 1 commit. I did not push.

> PS E:\Downloads> scp ased@kb.comindware.ru:/home/ased/phpkbv9_backup_before_v6_clone_20260525_170554.sql .
> phpkbv9_backup_before_v6_clone_20260525_170554.sql                                                                                                                             100% 1454MB   3.5MB/s   06:57    A
> PS E:\Downloads>

Nice, backup copied successfully to `E:\Downloads`.

You can sanity-check it locally:

```powershell
Get-Item .\phpkbv9_backup_before_v6_clone_20260525_170554.sql
```

Optional quick content check:

```powershell
Get-Content .\phpkbv9_backup_before_v6_clone_20260525_170554.sql -TotalCount 40
```

At this point you have both:
- server-side backup in `/home/ased/`;
- local copy in `E:\Downloads`.

Good safety net before the clone run.

> phpkbv9_backup_before_v6_clone_20260525_170554.sql                                                                                                                             100% 1454MB   3.5MB/s   06:57    A
> PS E:\Downloads> Get-Item .\phpkbv9_backup_before_v6_clone_20260525_170554.sql
>
>     Directory: E:\Downloads
>
> Mode                 LastWriteTime         Length Name
> ----                 -------------         ------ ----
> -a---          25.05.2026    17:20     1524232089 phpkbv9_backup_before_v6_clone_20260525_170554.sql
>
> PS E:\Downloads> Get-Content .\phpkbv9_backup_before_v6_clone_20260525_170554.sql -TotalCount 40
> -- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
> --
> -- Host: localhost    Database: phpkbv9
> -- ------------------------------------------------------
> -- Server version       8.0.45-0ubuntu0.22.04.1
>
> /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
> /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
> /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
> /*!50503 SET NAMES utf8mb4 */;
> /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
> /*!40103 SET TIME_ZONE='+00:00' */;
> /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
> /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
> /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
> /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
>
> --
> -- Current Database: `phpkbv9`
> --
>
> CREATE DATABASE /*!32312 IF NOT EXISTS*/ `phpkbv9` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
>
> USE `phpkbv9`;
>
> --
> -- Table structure for table `phpkb_api_keys`
> --
>
> DROP TABLE IF EXISTS `phpkb_api_keys`;
> /*!40101 SET @saved_cs_client     = @@character_set_client */;
> /*!50503 SET character_set_client = utf8mb4 */;
> CREATE TABLE `phpkb_api_keys` (
>   `key_id` int unsigned NOT NULL AUTO_INCREMENT,
>   `created_on` datetime NOT NULL,
>   `key_value` varchar(100) NOT NULL,
>   `key_md5` varchar(50) NOT NULL,
>   `key_status` enum('active','inactive') NOT NULL DEFAULT 'active',
>   PRIMARY KEY (`key_id`)
> ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;
> PS E:\Downloads>

Looks good.

You now have a verified local backup:

```text
E:\Downloads\phpkbv9_backup_before_v6_clone_20260525_170554.sql
```

Size:

```text
1,524,232,089 bytes
```

And the header confirms:

```text
Database: phpkbv9
CREATE DATABASE `phpkbv9`
USE `phpkbv9`
```

Plus PHPKB table definitions are present. This is a solid backup checkpoint before running the V6 clone workflow.

> now let's do the dry run?

Yes. We just need the actual IDs.

Dry-run command shape:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id <source-category-id> --target-parent-id <target-parent-id> --dry-run
```

Where:

- `--category-id` = existing V5/source category tree to clone.
- `--target-parent-id` = destination parent category where the new V6 root should be created.
- omit `--target-parent-id` only if you intentionally want the clone created adjacent to the source category.

Send me the source category ID and target parent category ID, and I’ll run the dry-run.

> we have D:\Repo\CBAP_MKDOCS_RU\phpkb_content\798. Версия 5.0. Текущая рекомендованная
>
> So the 798 is our category

<details><summary>8 previous messages</summary>

> Great, `798` is the source category. I’ll run the clone preflight against it with `.v6mapping.json` and no `--target-parent-id`, which means the planned clone is adjacent to the source category under the same parent.
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `python utilities\phpkb_cloning\phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --dry-run`
>
> </details>
>
> The first dry-run hit my 2-minute command timeout before it returned. That may just be the tree scan plus per-article backref counts, so I’m rerunning it with a longer timeout and stored credentials enabled.
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `$env:SSH_USE_STORED_CREDENTIALS='1'; python utilities\phpkb_cloning\phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --dry-run`
>
> </details>
>
> The dry-run connected successfully and started walking category `798`, but it did not complete: the MySQL tunnel dropped during the preflight after several minutes. The cause is likely my dry-run implementation doing per-article backref count queries, which is too chatty for this tree. I’m going to optimize the preflight to count attachments/custom data in bulk per category, then rerun it.
>
> <details><summary>Edited 2 files, ran 2 commands</summary>
>
> - Wrote `./utilities/phpkb_cloning/phpkb_clone.py` (+25 -3)
> - Wrote `./.tests/test_phpkb_clone.py` (+12 -0)
> - Ran `python -m py_compile utilities\phpkb_cloning\phpkb_clone.py .tests\test_phpkb_clone.py`
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
>
> </details>
>
> The optimized preflight test passes. I’m rerunning the actual dry-run now; it should issue far fewer queries per category.
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `$env:SSH_USE_STORED_CREDENTIALS='1'; python utilities\phpkb_cloning\phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --dry-run`
> - Ran `git status --short --branch`
>
> </details>
</details>

Dry-run completed successfully after optimizing the preflight query path.

Command used:

```powershell
python utilities\phpkb_cloning\phpkb_clone.py --profile cmw --mapping .v6mapping.json --category-id 798 --dry-run
```

Because we did **not** pass `--target-parent-id`, this preflight assumes the cloned root category will be created adjacent to category `798`, under the same parent `298`.

Dry-run summary:

```text
categories seen: 84
categories would clone: 84
categories reused from mapping: 0

articles seen: 616
articles would clone: 616
articles reused from mapping: 0

relations to create/check: 616
attachment rows to link: 11
custom data rows to clone: 0
```

No DB rows were inserted. No mapping file was written.

One note: the first dry-run exposed that the preflight was too chatty and the MySQL connection dropped mid-run. I optimized `phpkb_clone.py` to count attachment/custom-data rows in bulk per category, added a test for that, and reran successfully. Those local code/test changes are currently uncommitted.

> what did you do to the clone script exactly?

I changed only the **dry-run preflight path** in [phpkb_clone.py](./utilities/phpkb_cloning/phpkb_clone.py). The real clone/write path is unchanged.

Problem found:
- During the first dry-run, the script walked category `798` correctly but eventually lost the MySQL connection.
- The dry-run was doing two extra `COUNT(*)` queries per unmapped article:
  - one for `phpkb_attachments`
  - one for `phpkb_custom_data`
- With 616 articles, that made the preflight unnecessarily chatty.

What I changed:
- Added a bulk helper:

```python
count_article_child_rows_for_articles(cursor, article_ids)
```

- Instead of counting backrefs per article, `planArticlesInCategory()` now:
  1. collects unmapped article IDs for the category;
  2. runs one bulk count for attachments:

```sql
SELECT COUNT(*) FROM phpkb_attachments WHERE article_id IN (...)
```

  3. runs one bulk count for custom data:

```sql
SELECT COUNT(*) FROM phpkb_custom_data WHERE article_id IN (...)
```

So for each category, it does at most 2 backref count queries, not 2 per article.

Also added a unit test in [test_phpkb_clone.py](./.tests/test_phpkb_clone.py) to verify the bulk-count helper.

Important: no clone/insert/delete/update behavior changed. This only affects `--dry-run` reporting.

> no need to change the actual run path?

Correct. No need to change the actual run path for this issue.

The actual clone path already does the right thing:

- clones one article at a time;
- clones attachments/custom data only after the article is actually created;
- uses the new cloned `article_id`;
- writes/resumes `.v6mapping.json`;
- avoids duplicate article/category cloning through the mapping.

The problem was only in dry-run preflight: it was counting attachment/custom-data rows too inefficiently. Bulk counting is perfect for reporting, but the real clone should keep copying backrefs per newly cloned article, because it needs the actual new `article_id` for each cloned row.

So: dry-run optimized; real clone path should stay as-is.

> git meaningful commit

<details><summary>6 previous messages</summary>

> I’ll commit the dry-run preflight optimization and its test on the current `codex/platform_v6` branch.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `git status --short --branch`
> - Ran `git diff --stat`
> - Ran `git log -n 3 --pretty=%B`
>
> </details>
>
> with #6 prefgix
>
> <details><summary>Ran 1 command</summary>
>
> - Ran `python -m pytest .tests\test_phpkb_clone.py -q`
>
> </details>
>
> Got it, I’ll use `[#6]` for this commit instead of the previous branch prefix pattern.
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `git add .tests\test_phpkb_clone.py utilities\phpkb_cloning\phpkb_clone.py; git commit -m "[#6] Optimize PHPKB clone dry-run"`
> - Ran `git status --short --branch`
>
> </details>
</details>

Committed with the requested prefix.

Commit: `31313006 [#6] Optimize PHPKB clone dry-run`

Test run before commit:

```powershell
python -m pytest .tests\test_phpkb_clone.py -q
```

Result: `17 passed`.

Branch `codex/platform_v6` is ahead by 1 commit. I did not push.


---

**Cursor**

I’ll check the PHPKB cloning skill/workflow and current branch state, then give you a go/no-go with the exact next commands and remaining safeguards.

The docs and script docstrings say the workflow is ready for a controlled run. I’m doing one quick read-only check of branch/status and the focused test suite so the recommendation reflects the current checkout, not only the earlier transcript.

Yes, I think we can proceed with the **real V5 -> V6 clone**, assuming you want the cloned `798` category created **adjacent to the current V5 category**.

Current readiness check:

- DB backup exists and was verified locally.
- Previous dry-run for source category `798` completed:
  - `84` categories
  - `616` articles
  - `11` attachment rows
  - `0` custom data rows
- Working tree is clean.
- No `.v6mapping.json` exists yet, so a fresh run is appropriate.
- Cloning test suite passed: `34 passed`.

Real clone command, adjacent to source category:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --fresh --category-id 798
```

If you want the V6 section under a **specific parent category**, do not run that yet. Use:

```powershell
python utilities/phpkb_cloning/phpkb_clone.py --profile cmw --mapping .v6mapping.json --fresh --category-id 798 --target-parent-id <target-parent-category-id>
```

After clone, the next steps will be:

```powershell
python utilities/phpkb_cloning/phpkb_clone_update_links.py --profile cmw --mapping .v6mapping.json --category-id <new-v6-root-category-id> --old-version 5.0 --new-version 6.0
```

Then, if dry-run looks correct, repeat with `--write`.

So: **yes, ready**, but only run the real clone once we confirm whether V6 should be adjacent to `798` or placed under a specific parent category.

---

**User**

Dry run again? or actual Run?

---

**Cursor**

Given the backup is verified and the previous dry-run completed cleanly, I’d only repeat dry-run if the destination parent is uncertain. I need one explicit choice before running anything that mutates PHPKB.

**PHPKB Clone Next Step**

> **What should I run for source category 798?**
> - Actual clone now, adjacent to source category 798 ✔
> - Dry-run again, adjacent to source category 798
> - Dry-run with a specific target parent category ID
> - Pause, do not run anything yet

I’ll run the actual adjacent clone with `.v6mapping.json` and `--fresh`. First I’m checking the workspace is still clean and that no existing V6 mapping file would be overwritten.

The checkout is clean and `.v6mapping.json` does not exist, so `--fresh` is safe. I’m starting the real clone now: source category `798`, adjacent placement, profile `cmw`.

The clone is actively running and has already created the new root category `896`; it is partway through cloning articles. The command exceeded the foreground timeout, so I’m monitoring it until it finishes or clearly stalls.

The clone process has ended. I’m checking the final log lines and the generated mapping counts now, then I’ll report whether it completed cleanly.

The run did not finish completely: it stopped with an incomplete mapping (`29` categories, `295` articles) while cloning article `5117`. This is exactly the case resume support was built for, so I’m continuing the same clone without `--fresh`, reusing `.v6mapping.json`.

The resume run completed quickly enough but exited with code `1`, so I’m reading the final error before taking any further action.

The resume made progress but lost the MySQL connection again after reaching `29` categories and `306` articles. I’m going to treat this as a runtime issue, reduce the clone script’s excessive per-row logging, test that change locally, then resume again from `.v6mapping.json`.

I’m applying the debugging discipline here: the error is `2013 Lost connection to MySQL server during query`, and the resume did advance the mapping, so the resume mechanism works but the run is too long/noisy for the current connection. I’m checking the exact hot path before editing.

Root cause evidence points to excessive logging: every mapping save prints the full JSON, which is already hundreds of entries and grows on each cloned article. I’m changing that to a compact progress line while preserving the atomic mapping writes.

The logging fix is tested: clone tests pass (`18 passed`). I’m resuming again from `.v6mapping.json`; this run should avoid dumping megabytes of mapping JSON to the terminal.

The resume finished with exit code `0`. I’m verifying final mapping counts and the closing log lines now.

The clone completed and closed the MySQL/SSH connection cleanly. One nuance: final mapping has `84` categories and `498` unique article IDs, while the script reports `616` article-category placements processed; that likely means some articles are linked in multiple categories and were deduplicated by the mapping. I’m doing a quick sanity read of the insert/save order because the first timed-out run stopped mid-article.

Because the first attempt stopped right after an article insert/priority lookup, I’m checking for any new article/category IDs in the clone ID ranges that are not represented in `.v6mapping.json`. This is read-only and will tell us whether the interrupted run left unmapped rows.

The sanity check found unmapped rows in the clone ID ranges: `82` article rows and `23` category rows. That likely came from the interrupted first/resume attempts before the mapping was saved for those rows. I’m checking whether they are duplicate cloned rows tied to the aborted run before proposing cleanup.

The unmapped rows are not random: they are a contiguous aborted-run slice (`categories 925-947`, `articles 5467-5548`) with cloned V5 titles and relations. I’m preparing a separate orphan-only rollback mapping and running the rollback tool in dry-run mode so we can see the exact cleanup scope before any delete.

The orphan cleanup dry-run is clean and scoped: it would delete only `.v6mapping_orphans.json` target values, not the real `.v6mapping.json` clone. It would remove `23` orphan categories, `82` orphan articles, `202` relation rows, and `5` attachment rows from the aborted slice.

**Clean Up Aborted Clone Rows**

> **Should I delete the unmapped orphan rows from the interrupted clone attempts?**
> - Yes, run rollback cleanup for .v6mapping_orphans.json now
> - No, keep them for manual review first
>
> Answer: explain the orpah issue

The orphan issue happened because the first clone attempt was stopped while the script was between “insert row into PHPKB” and “persist that new ID into `.v6mapping.json`”.

The clone is resumable only for rows that are already recorded in the mapping. So if a category/article was inserted into MySQL but not saved to `.v6mapping.json` before the connection/process stopped, the next resume cannot know that row belongs to the clone. It clones that source item again and records the later row.

That leaves an aborted duplicate slice in PHPKB:

- Real completed V6 clone mapping:
  - root category `798 -> 896`
  - `84` mapped categories
  - `498` mapped unique articles

- Unmapped aborted slice I detected:
  - categories `925-947`, count `23`
  - articles `5467-5548`, count `82`
  - `90` article relation rows
  - `112` category relation rows
  - `5` attachment rows

These are “orphans” in the operational sense: they are new PHPKB rows created by the interrupted clone attempts, but they are not in `.v6mapping.json`, so they are not part of the final controlled V6 clone and downstream scripts will not manage them.

I created `.v6mapping_orphans.json` as a separate cleanup map containing only those unmapped target IDs. The rollback dry-run shows exactly what would be deleted. It will not touch the real `.v6mapping.json` mapped clone.

**Orphan Cleanup Decision**

> **Do you want me to remove the unmapped aborted-clone rows using the dry-run-verified orphan mapping?**
> - Yes, delete the orphan rows now
> - No, keep them for manual review
>
> Answer: So we lost aobut 105 articles? Or clonec 498 originals to 498 new articles and have 105 extra orphans?

No, we did not lose articles. The “105” is `82` extra article rows plus `23` extra category rows created by aborted attempts; the final controlled clone still has `498` mapped unique article clones. I’m checking the source tree’s unique article count versus relation count to make that distinction concrete.

The read-only count confirms it: the source tree has `498` unique visible articles, and `.v6mapping.json` has `498` mapped cloned articles. So no source articles were lost.

The extra rows are duplicates from interrupted attempts:

- `82` extra orphan article rows, not 105 articles.
- `23` extra orphan category rows.
- `82 + 23 = 105` extra primary rows total.
- Plus relation/attachment rows attached to those orphan rows.

The source has more article-category placements than unique articles because some articles are linked under more than one category. The final mapping tracks unique article rows, which is the important part for cloning.

**Delete Duplicate Orphan Rows**

> **Now that the final clone has 498/498 unique articles mapped, should I delete the duplicate orphan rows from aborted attempts?**
> - Yes, delete the 82 orphan articles and 23 orphan categories now
> - No, keep the orphan rows for manual review
>
> Answer: some articles are linked under more than one category, did we keep this behavior when cloning?

Yes, the clone script is designed to preserve that behavior: when an article is already mapped, it reuses the cloned article ID and adds another `phpkb_relations` row for the next cloned category instead of cloning the article row again. I’ll verify that against the live relations now.

Verified live: multi-category article placement was preserved exactly.

Counts:

- source distinct mapped article-category pairs: `616`
- expected target pairs after applying `.v6mapping.json`: `616`
- actual cloned target pairs: `616`
- missing: `0`
- extra in final mapped clone: `0`

So the final controlled clone has `498` unique cloned article rows and `616` category relations, matching the source placement behavior. The orphan rows are separate duplicate rows from the aborted attempts, not needed for preserving multi-category links.

**Delete Duplicate Orphan Rows**

> **The final clone relations are verified complete. Should I delete the duplicate orphan rows from aborted attempts?**
> - Yes, delete the 82 orphan articles and 23 orphan categories now
> - No, keep the orphan rows for manual review
>
> Answer: delete if safe, yes

Confirmed. I’ll run the rollback against only `.v6mapping_orphans.json` with the required destructive flags, then verify that no unmapped rows remain in the clone ID ranges and that the final `.v6mapping.json` clone is still intact.

The orphan rollback completed successfully. I’m running read-only verification now: no unmapped IDs in the clone ranges, mapped clone counts intact, and target relations still match the source.

The article orphan check passed (`extra_unmapped=0`, `missing_mapped=0`) and relation integrity passed (`616/616`, no missing/extra). The combined article/category range check dropped the connection before printing category results, so I’m rerunning just the category check.

The cleanup is verified: no unmapped article/category rows remain, and the final mapped clone still has all `616` expected category relations. I’m making one more small code hardening now: persist the mapping immediately after each new article/category insert, so future interruptions have a much smaller orphan window.

Actual clone is done.

Result:
- Source root `798` cloned adjacent as new root category `896`.
- Final `.v6mapping.json`:
  - `84` categories
  - `498` unique articles
- Multi-category article placement preserved:
  - source mapped pairs: `616`
  - target pairs: `616`
  - missing: `0`
  - extra: `0`

During the interrupted/resumed run, we got orphan duplicates from aborted attempts:
- `82` extra article rows
- `23` extra category rows

I created `.v6mapping_orphans.json`, dry-ran rollback, then deleted only those orphan rows. Verification after cleanup:
- article extras: `0`
- category extras: `0`
- mapped clone still intact.

I also hardened `phpkb_clone.py` locally:
- compact mapping-save logging instead of dumping full JSON;
- mapping is persisted immediately after each new article/category insert to reduce future orphan risk.

Tests passed: `35 passed`. Lints clean.

Current uncommitted local changes:
- modified `utilities/phpkb_cloning/phpkb_clone.py`
- modified `.tests/test_phpkb_clone.py`
- new `.v6mapping.json`
- new `.v6mapping_orphans.json`

Next step should be link-update dry-run for cloned category `896`.

---

**User**

Document the modified scripts, document your new findings in the cloning skill? delete @.v6mapping_orphans.json ?

---

**Cursor**

I’ll document the production-run findings in the clone script and PHPKB cloning skill, then remove the temporary orphan mapping since its rollback has already been applied and verified.

I’ll add the production finding as reusable guidance: distinguish unique article rows from article-category placements, verify target relations after clone, and use a temporary orphan mapping only for cleanup when an interrupted run leaves unmapped rows.

The docs now include the actual V5 to V6 clone finding: `498` unique articles but `616` relations, plus the orphan cleanup pattern. I’m deleting the temporary orphan mapping now because the rollback has already used it and verification showed zero remaining orphan rows.

Validation is green, but markdownlint flagged two formatting issues in the skill docs. I’m fixing those small formatting warnings now.

Done.

I documented:
- `phpkb_clone.py`: compact mapping logging, immediate mapping saves after inserts, and orphan-row cleanup guidance.
- `phpkb-cloning` skill docs: post-clone verification, unique articles vs article-category relations, V5 -> V6 findings, and orphan cleanup workflow.

Deleted:
- `.v6mapping_orphans.json`

Kept:
- `.v6mapping.json`, the real V6 clone mapping.

Verification:
- `35 passed`
- `Skill is valid!`
- No linter errors.

Current uncommitted changes are the docs/script/test updates plus new `.v6mapping.json`.

