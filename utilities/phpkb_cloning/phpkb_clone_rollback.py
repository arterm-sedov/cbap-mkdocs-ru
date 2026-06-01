"""Rollback helper for rows created by `phpkb_clone.py`.

Use this only when a clone run went wrong and the cloned PHPKB rows must be
removed. The script reads a clone mapping JSON and deletes only the mapped
target IDs, that is, values from `mapping["Articles"]` and
`mapping["Categories"]`. It never deletes source IDs from the mapping keys.

Safety model:
- dry-run by default;
- `--write` is required for DB deletes;
- `--confirm-delete-cloned-content` is also required with `--write`;
- deletes article-owned rows before articles/categories;
- deletes categories after article relations are gone;
- uses parameterized numeric ID lists.

Tables cleaned:
- `phpkb_attachments` for mapped article IDs;
- `phpkb_custom_data` for mapped article IDs;
- `phpkb_relations` for mapped article IDs or mapped category IDs;
- `phpkb_articles` for mapped article IDs;
- `phpkb_categories` for mapped category IDs.
"""

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.graceful_interrupt import ensure_cleanup
from tools.ssh_kb_ru import establish_connection_interactive


DEFAULT_MAPPING_FILE = ".mapping.json"


@dataclass(frozen=True)
class DeleteStep:
    label: str
    table: str
    where: str
    ids: tuple[str, ...]


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Delete PHPKB rows created by a clone run, using mapped target IDs."
    )
    parser.add_argument(
        "--profile",
        choices=("cmw", "cmwlab"),
        help="PHPKB server profile. Defaults to SERVER_PROFILE from .env.",
    )
    parser.add_argument(
        "--mapping",
        default=DEFAULT_MAPPING_FILE,
        help=f"Clone mapping JSON. Default: {DEFAULT_MAPPING_FILE}",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Delete rows from PHPKB. Without this flag, the script only reports counts.",
    )
    parser.add_argument(
        "--confirm-delete-cloned-content",
        action="store_true",
        help="Required with --write to confirm destructive rollback.",
    )
    return parser.parse_args(argv)


def load_mapping(path):
    with Path(path).open("r", encoding="utf-8") as mapping_file:
        return json.load(mapping_file)


def normalize_numeric_ids(ids):
    normalized = []
    for value in ids:
        value = str(value).strip()
        if not value:
            continue
        if not value.isdigit():
            raise ValueError(f"Mapping contains a non-numeric cloned ID: {value}")
        normalized.append(value)
    return tuple(sorted(set(normalized), key=int, reverse=True))


def mapped_target_ids(mapping, section):
    return normalize_numeric_ids((mapping.get(section) or {}).values())


def build_delete_steps(mapping):
    article_ids = mapped_target_ids(mapping, "Articles")
    category_ids = mapped_target_ids(mapping, "Categories")

    return [
        DeleteStep("attachments", "phpkb_attachments", "article_id", article_ids),
        DeleteStep("custom data", "phpkb_custom_data", "article_id", article_ids),
        DeleteStep("article relations", "phpkb_relations", "article_id", article_ids),
        DeleteStep("category relations", "phpkb_relations", "category_id", category_ids),
        DeleteStep("articles", "phpkb_articles", "article_id", article_ids),
        DeleteStep("categories", "phpkb_categories", "category_id", category_ids),
    ]


def placeholders(ids):
    return ", ".join(["%s"] * len(ids))


def execute_step(cursor, step, write=False):
    if not step.ids:
        return 0

    where_clause = f"`{step.where}` IN ({placeholders(step.ids)})"
    cursor.execute(f"SELECT COUNT(*) FROM `{step.table}` WHERE {where_clause}", step.ids)
    count = cursor.fetchone()[0]

    if write and count:
        cursor.execute(f"DELETE FROM `{step.table}` WHERE {where_clause}", step.ids)

    return count


def run_rollback(connection, mapping, write=False):
    cursor = connection.cursor(buffered=True)
    report = []

    for step in build_delete_steps(mapping):
        count = execute_step(cursor, step, write)
        report.append({"label": step.label, "table": step.table, "where": step.where, "count": count})

    if write and hasattr(connection, "commit"):
        connection.commit()

    return report


def print_report(mapping_path, report, write=False):
    mode = "write" if write else "dry-run"
    print(f"Mapping: {mapping_path}")
    print(f"Mode: {mode}")
    print("\nRollback plan:")
    for item in report:
        print(f"  {item['label']}: {item['count']} row(s) in {item['table']} by {item['where']}")


def main(argv=None):
    args = parse_args(argv)
    if args.write and not args.confirm_delete_cloned_content:
        raise SystemExit("--write requires --confirm-delete-cloned-content")

    mapping = load_mapping(args.mapping)
    connection = None
    server = None

    try:
        connection, server = establish_connection_interactive(args.profile)
        report = run_rollback(connection, mapping, write=args.write)
        print_report(args.mapping, report, write=args.write)
    finally:
        ensure_cleanup(connection, server)


if __name__ == "__main__":
    main()
