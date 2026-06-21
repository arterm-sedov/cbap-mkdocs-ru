"""Update local Markdown IDs using a PHPKB clone mapping.

This is a local-file post-clone migration helper. It does not connect to PHPKB
and does not mutate the database. Use it after `phpkb_clone.py` has produced a
mapping JSON with `Articles` and `Categories` sections.

Targets:
- `frontmatter-kbids` scans Markdown files under `docs/ru` by default and
  updates `kbId:` frontmatter values using `mapping["Articles"]`;
- `hyperlink-map` updates only
  `docs/ru/.snippets/hyperlinks_mkdocs_to_kb_map.md`;
- `all` runs both targets.

Hyperlink-map updates are prefix-aware:
- `{{ kbArticleURLPrefix }}...` uses `mapping["Articles"]`;
- `{{ kbCategoryURLPrefix }}...` uses `mapping["Categories"]`.

The CLI is dry-run by default. Pass `--write` to rewrite local files.
`--mapping` is required; pass the same file used for `phpkb_clone.py`.
"""

import argparse
import json
import re
from pathlib import Path


DEFAULT_DOCS_ROOT = Path("docs/ru")
DEFAULT_HYPERLINKS_FILE = DEFAULT_DOCS_ROOT / ".snippets/hyperlinks_mkdocs_to_kb_map.md"

FRONTMATTER_KB_ID_PATTERN = re.compile(
    r"^(?P<prefix>\s*kbId\s*:\s*)(?P<quote>['\"]?)(?P<id>\d+)(?P=quote)(?P<suffix>\s*)$",
    re.MULTILINE,
)

HYPERLINK_PATTERNS = {
    "Articles": re.compile(r"(?P<prefix>{{\s*kbArticleURLPrefix\s*}}\s*)(?P<id>\d+)"),
    "Categories": re.compile(r"(?P<prefix>{{\s*kbCategoryURLPrefix\s*}}\s*)(?P<id>\d+)"),
}

BOMS = (
    (b"\xef\xbb\xbf", "utf-8"),
    (b"\xff\xfe", "utf-16-le"),
    (b"\xfe\xff", "utf-16-be"),
)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Update local Markdown KB IDs with a PHPKB clone mapping."
    )
    parser.add_argument(
        "--mapping",
        required=True,
        help="Mapping JSON with Articles/Categories sections (required). Use the same file as phpkb_clone.py.",
    )
    parser.add_argument(
        "--target",
        choices=("frontmatter-kbids", "hyperlink-map", "all"),
        default="all",
        help="Local ID target to update. Default: all",
    )
    parser.add_argument(
        "--root",
        default=str(DEFAULT_DOCS_ROOT),
        help=f"Docs root for frontmatter kbId updates. Default: {DEFAULT_DOCS_ROOT}",
    )
    parser.add_argument(
        "--hyperlinks-file",
        default=str(DEFAULT_HYPERLINKS_FILE),
        help=f"Shared MkDocs hyperlink map file. Default: {DEFAULT_HYPERLINKS_FILE}",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to disk. Without this flag, the tool runs in dry-run mode.",
    )
    return parser.parse_args(argv)


def load_mapping(path):
    with Path(path).open("r", encoding="utf-8") as mapping_file:
        return json.load(mapping_file)


def normalize_mapping(mapping):
    return {str(source_id): str(target_id) for source_id, target_id in (mapping or {}).items()}


def replace_frontmatter_kbids(content, article_mapping):
    changes = 0

    def replace(match):
        nonlocal changes
        old_id = match.group("id")
        new_id = article_mapping.get(old_id)
        if not new_id:
            return match.group(0)

        changes += 1
        return f"{match.group('prefix')}{match.group('quote')}{new_id}{match.group('quote')}{match.group('suffix')}"

    return FRONTMATTER_KB_ID_PATTERN.sub(replace, content), changes


def replace_hyperlink_map_ids(content, mapping):
    changes_by_section = {"Articles": 0, "Categories": 0}

    for section, pattern in HYPERLINK_PATTERNS.items():
        section_mapping = normalize_mapping(mapping.get(section))

        def replace(match, section_mapping=section_mapping, section=section):
            old_id = match.group("id")
            new_id = section_mapping.get(old_id)
            if not new_id:
                return match.group(0)

            changes_by_section[section] += 1
            return f"{match.group('prefix')}{new_id}"

        content = pattern.sub(replace, content)

    return content, changes_by_section


def read_text_preserving_encoding(path):
    path = Path(path)
    raw = path.read_bytes()
    for bom, encoding in BOMS:
        if raw.startswith(bom):
            return raw[len(bom):].decode(encoding), encoding, bom
    return raw.decode("utf-8"), "utf-8", b""


def write_text_preserving_encoding(path, content, encoding, bom):
    path = Path(path)
    path.write_bytes(bom + content.encode(encoding))


def update_file(path, replacer, write):
    path = Path(path)
    content, encoding, bom = read_text_preserving_encoding(path)
    updated_content, changes = replacer(content)
    has_changes = updated_content != content

    if write and has_changes:
        write_text_preserving_encoding(path, updated_content, encoding, bom)

    return has_changes, changes


def iter_markdown_files(root):
    return sorted(Path(root).rglob("*.md"))


def update_frontmatter_kbids(root, mapping, write):
    article_mapping = normalize_mapping(mapping.get("Articles"))
    scanned = changed = replacements = 0

    if not Path(root).is_dir():
        raise FileNotFoundError(f"The directory '{root}' does not exist.")

    for path in iter_markdown_files(root):
        scanned += 1
        has_changes, count = update_file(
            path,
            lambda content: replace_frontmatter_kbids(content, article_mapping),
            write,
        )
        changed += int(has_changes)
        replacements += count

    return {"files_scanned": scanned, "files_changed": changed, "replacements": replacements}


def update_hyperlink_map(hyperlinks_file, mapping, write):
    if not Path(hyperlinks_file).is_file():
        raise FileNotFoundError(f"The hyperlink map '{hyperlinks_file}' does not exist.")

    has_changes, changes = update_file(
        hyperlinks_file,
        lambda content: replace_hyperlink_map_ids(content, mapping),
        write,
    )
    return {
        "files_changed": int(has_changes),
        "article_links": changes["Articles"],
        "category_links": changes["Categories"],
    }


def print_report(args, report):
    mode = "write" if args.write else "dry-run"
    print(f"Mapping: {args.mapping}")
    print(f"Target: {args.target}")
    print(f"Mode: {mode}")

    if "frontmatter-kbids" in report:
        result = report["frontmatter-kbids"]
        print("\nFrontmatter kbIds:")
        print(f"  files scanned: {result['files_scanned']}")
        print(f"  files changed: {result['files_changed']}")
        print(f"  replacements: {result['replacements']}")

    if "hyperlink-map" in report:
        result = report["hyperlink-map"]
        print("\nHyperlink map:")
        print(f"  file: {args.hyperlinks_file}")
        print(f"  files changed: {result['files_changed']}")
        print(f"  article links changed: {result['article_links']}")
        print(f"  category links changed: {result['category_links']}")


def run(args):
    mapping = load_mapping(args.mapping)
    report = {}

    if args.target in ("frontmatter-kbids", "all"):
        report["frontmatter-kbids"] = update_frontmatter_kbids(args.root, mapping, args.write)

    if args.target in ("hyperlink-map", "all"):
        report["hyperlink-map"] = update_hyperlink_map(args.hyperlinks_file, mapping, args.write)

    print_report(args, report)
    return report


def main(argv=None):
    return run(parse_args(argv))


if __name__ == "__main__":
    main()
