import re
import os
import sys

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'ru')

FILES_TO_SKIP = {
    '5020-change_collection_statuses_end_task.md',
    '5004-change_task_status.md',
}

FILE_MAP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'ru', '.snippets', 'hyperlinks_mkdocs_to_kb_map.md')

REPLACEMENTS = [
    # Variant A: ", Comindware.Entities entities" in signatures (handles variable whitespace)
    (re.compile(r',\s+Comindware\.Entities entities'), ''),
    # Variant C: ", [Comindware.Entities entities]" (bracket optional param)
    (re.compile(r',\s*\[Comindware\.Entities entities\]'), ''),
]

VARIANT_B_RE = re.compile(r'^\s*Comindware\.Entities entities //.*$', re.MULTILINE)

def remove_variant_b_lines(text):
    return VARIANT_B_RE.sub('', text)

def apply_replacements(text):
    text = remove_variant_b_lines(text)
    for pattern, replacement in REPLACEMENTS:
        text = pattern.sub(replacement, text)
    return text

def validate_text(text, filepath):
    issues = []
    if 'Comindware.Entities entities' in text:
        issues.append('  WARNING: Still contains "Comindware.Entities entities"')
    if '( , )' in text or ',\n)' in text:
        issues.append('  WARNING: Orphaned dangling comma')
    return issues

def main():
    total_changed = 0
    total_files = 0
    changed_files = []

    for root, dirs, files in os.walk(DOCS_DIR):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            if fname in FILES_TO_SKIP:
                continue

            filepath = os.path.join(root, fname)

            with open(filepath, 'r', encoding='utf-8') as f:
                original = f.read()

            modified = apply_replacements(original)

            if original == modified:
                continue

            relpath = os.path.relpath(filepath, DOCS_DIR)
            issues = validate_text(modified, relpath)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified)

            total_files += 1
            total_changed += 1
            changed_files.append(relpath)
            print(f'  MODIFIED: {relpath}')
            for issue in issues:
                print(issue)

    print(f'\n{"="*50}')
    print(f'Total files modified: {total_files}')

    if not changed_files:
        print('No files were modified.')
        return

    print(f'\nModified files:')
    for f in sorted(changed_files):
        print(f'  - {f}')

if __name__ == '__main__':
    main()
