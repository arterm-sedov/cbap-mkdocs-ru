<!-- 0dbc7d3e-4834-4e34-8801-b5629bc3df3f 5228d54f-5432-4c39-bea3-969164add4aa -->
# Remove Link and Content Modifications from RAG Import Script

Remove content transformation code from `phpkb_import_for_rag.py` to preserve original markdown content (links, product names, headings) while keeping filename resolution and file structure export functionality.

## Changes to make

### 1. Remove Related Articles heading replacement (lines 197-200)

Remove the code that replaces `## Связанные статьи` with a markdown include placeholder.

### 2. Remove product name placeholder replacements (lines 202-208)

Remove all four product name replacements that convert names to `{{ productName }}` placeholders.

### 3. Remove hyperlinks map footer (lines 246-248)

Remove the footer line and update the markdown concatenation to exclude the footer include statement.

### 4. Remove Article-ID pattern conversion (lines 251-270)

Remove the entire section that processes `{Article-ID:(\d+)}` patterns and converts them to markdown links.

### 5. Remove KB article URLs replacement (lines 272-286)

Remove the section that replaces `https://kb.comindware.ru` article URLs with references from the hyperlinks map.

### 6. Remove commented category URL replacement (line 289)

Remove the commented line for category URL replacement.

## Code to preserve

- `find_url_in_snippet()` function (lines 29-48) - used by filename lookup
- `findFilenameByArticleId()` function (lines 416-472) - filename resolution logic
- Frontmatter generation (lines 234-244) - keep all frontmatter
- All HTML processing (TOC removal, source code table conversion, etc.)
- All other markdown cleaning (newlines, spaces, image captions, code blocks, etc.)

## Result

The script will export markdown files with:

- Original markdown content preserved (no link/product name/heading modifications)
- Proper filename resolution using existing lookup logic
- Complete frontmatter with title, kbId, url, and updated date
- Same file structure and directory organization

### To-dos

- [x] Remove Related Articles heading replacement code (lines 197-200) that replaces '## Связанные статьи' with placeholder
- [x] Remove product name placeholder replacements (lines 202-208) that convert product names to {{ productName }} placeholders
- [x] Remove hyperlinks map footer include and update markdown concatenation (lines 246-248)
- [x] Remove Article-ID pattern conversion section (lines 251-270) that processes {Article-ID:(\d+)} patterns
- [x] Remove KB article URLs replacement section (lines 272-286) that replaces URLs with hyperlinks map references
- [x] Remove commented category URL replacement line (line 289)