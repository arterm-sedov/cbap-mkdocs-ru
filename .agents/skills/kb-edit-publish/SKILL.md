---
name: kb-edit-publish
description: Use when editing an existing KB article (docs/ru/**/*.md with kbId), rebuilding PHPKB HTML export, publishing to PHPKB, and committing. Covers the full edit→rebuild→publish→commit cycle. Triggers on "edit article", "update article", "republish", "rebuild and publish", "sync to PHPKB", or any task modifying an existing docs/ru Markdown file that has a kbId.
---

# Edit, Rebuild, Publish, Commit

End-to-end workflow for updating existing KB articles.

## Prerequisites

- The article must already exist under `docs/ru/` and have a `kbId:` in its frontmatter.
- The repo virtual environment `.venv` must be functional (load `python-env-setup` skill if not).
- `.env` file configured (copy `.env.example` → `.env` and fill in the profile values). Required for all publish and image-sync steps — not just ingestion. See `.env.example` for the full variable list and `phpkb-ingestion` skill for details.

## Source code reference

Platform behavior may need verification against the companion source repo. Clone or pull it alongside this repo if needed. Search it with `rg` (ripgrep) to understand feature implementation, then transfer findings into the KB article. Never paste raw source code into articles — explain behavior in user-facing language.

## Workflow

### 1. Edit the Markdown

Edit the file under `docs/ru/`. Follow all formatting rules from AGENTS.md (links, lists, italic/bold, tags, anchors, HTML entities).

### 2. Rebuild the PHPKB HTML export

```powershell
.\.venv\Scripts\python.exe -m mkdocs build -f mkdocs_for_kb_import_ru.yml
```

Wait for "Documentation built in N seconds". Warnings about missing anchors are non-fatal.

### 3. Verify the export changed

```powershell
git diff --name-only for_kb_import_ru/
```

Confirm the expected HTML file(s) appear in the diff.

### 4. Publish to PHPKB

Extract the `kb-id` from the generated HTML, then publish:

```powershell
# Extract kb-id
Select-String -Path for_kb_import_ru\<path>.html -Pattern 'kb-id="(\d+)"' |
  ForEach-Object { $_.Matches.Groups[1].Value } | Select-Object -First 1

# Publish (the --yes flag skips interactive confirmation prompts)
.\.venv\Scripts\python.exe phpkb_update_articles.py --profile cmw --article-id <kb-id> --yes
```

Confirm "Updated article <kb-id>" in the output.

### 5. Commit and push

Stage both the source Markdown and the generated HTML:

```powershell
git add docs/ru/<edited-file>.md for_kb_import_ru/<matching-export>.html
git commit -m "[#<ticket>] <concise description>"
git push
```

Use the commit message format from the `cmwhelp-commit` skill. Extract the ticket number from the branch name or recent commits.

### 6. Sync platform assets (optional)

If the edited article includes new or updated images, sync them to the PHPKB static assets repo.

**Requires `.env`** with `CMW_KB_REPO_PATH` and `CMW_SSH_*` configured (see Prerequisites above and `phpkb-ingestion` skill for details). Without `.env`, these scripts will fail.

```bash
# Copy images and auto-commit-push to PHPKB repo
python3 phpkb_copy_images.py --git

# Also pull on production server after push
python3 phpkb_copy_images.py --git --pull

# Specify a different version (default: v6.0)
python3 phpkb_copy_images.py --version v5.0 --git --pull
```

## Troubleshooting

- **Build fails**: check `install/requirements.txt`, verify `.venv` with `.\.venv\Scripts\python.exe -c "import mkdocs"`.
- **Publish fails with "Found content for article" but no update**: verify `kbId:` in the Markdown frontmatter matches the expected PHPKB article.
- **SSH connection refused**: check SSH config and key, or use `--profile cmw` which reads from the stored credentials.
- **Image sync fails with "CMW_KB_REPO_PATH not set" or "SSH_HOST not set"**: `.env` is missing or incomplete. Copy `.env.example` → `.env` and fill in all variables for your profile. See Prerequisites above.
