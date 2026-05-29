---
name: mkdocs_add_file
description: Add an article to relevant mkdocs_guide_*.yml (YAML) configuration files
---

Use this skill when asked to add a documentation (article) file to mkdocs configuration files.

## Purpose

Automatically add a documentation file (typically from `docs/ru/` or `docs/en/`) to the appropriate `mkdocs_guide_*.yml` configuration files based on the file's location and content.

## Algorithm

1. **Identify the file to add:**
   - Read the file to understand its content, tags, and location
   - Determine which guides should include it based on:
     - File path (e.g., `examples/`, `developer_guide/`, `using_the_system/`, etc.)
     - Content type (N3 examples, C# examples, user guides, admin guides, etc.)
     - Tags in frontmatter (if present)

2. **Find relevant config files:**
   - Search for `mkdocs_guide_*.yml` files in the workspace root
   - Determine which configs should include the file:
     - **Developer guide** (`mkdocs_guide_developer_*.yml`): For developer-focused content, N3/C# examples, API docs, formulas
     - **User guide** (`mkdocs_guide_user_*.yml`): For end-user content, business apps, using_the_system
     - **Complete guide** (`mkdocs_guide_complete_*.yml`): Usually includes most content
     - **Admin guides** (`mkdocs_guide_admin_*.yml`): For administration/deployment content
     - **PDF configs** (`mkdocs_guide_*_pdf.yml`): Usually inherit from main configs, but might have specific exclusions, so typically do not need to be modified
     - **PHPKB configs** (`mkdocs_for_kb_*pdf*.yml`): Usually inherit from main configs and typically do not need to be modified

3. **Find insertion point:**
   - Search for similar files in the config to determine logical placement
   - Group related files together (e.g., all N3 examples together, all task-related examples together)
   - Place next to a related file when possible (e.g., `n3_task_list_custom.md` after `n3_filter_active_tasks.md`)
   - Maintain alphabetical or logical ordering within groups

4. **Add the file:**
   - Use `search_replace` to insert the file entry in the correct location
   - Maintain proper YAML indentation (2 spaces per level)
   - Use the format: `- examples/filename.md` or `- path/to/filename.md`
   - Ensure the path is relative to the `docs/ru/` or `docs/en/` directory

## Examples

### Example 1: Adding an N3 example
**File:** `docs/ru/examples/n3_task_list_custom.md`

**Action:**
- Add to: `mkdocs_guide_developer_*.yml`, `mkdocs_guide_complete_*.yml`, `mkdocs_guide_user_*.yml`
- Insert after: `examples/n3_filter_active_tasks.md` (related task filtering example)
- Format: `- examples/n3_task_list_custom.md`

### Example 2: Adding a user guide article
**File:** `docs/ru/using_the_system/new_feature.md`

**Action:**
- Add to: `mkdocs_guide_user_*.yml`, `mkdocs_guide_complete_*.yml`
- Insert in: `using_the_system/` section
- Format: `- using_the_system/new_feature.md`

### Example 3: Adding an admin guide
**File:** `docs/ru/administration/deploy/new_deployment.md`

**Action:**
- Add to: `mkdocs_guide_admin_*.yml`, `mkdocs_guide_complete_*.yml`
- Insert in: appropriate admin section
- Format: `- administration/deploy/new_deployment.md`

## Rules

- **Always check existing patterns:** Look at how similar files are organized in the configs
- **Maintain logical grouping:** Keep related files together
- **Preserve indentation:** Use 2 spaces for YAML indentation
- **Use relative paths:** Paths should be relative to `docs/ru/` or `docs/en/`
- **Check for duplicates:** Ensure the file isn't already in the config
- **Consider PDF configs:** PDF configs may have different exclusions, check if they need the file too
- **Verify syntax:** Ensure YAML syntax remains valid after insertion

## Common Patterns

- **N3 examples:** Usually go in developer guide, complete guide, and user guide
- **C# examples:** Usually go in developer guide and complete guide
- **User-facing content:** Usually goes in user guide and complete guide
- **Admin content:** Usually goes in admin guides and complete guide
- **API documentation:** Usually goes in developer guide and complete guide

## Verification

After adding files:
1. Verify YAML syntax is correct (check indentation, dashes, etc.)
2. Confirm the file path matches the actual file location
3. Ensure logical ordering is maintained
4. Check that related files are grouped together
