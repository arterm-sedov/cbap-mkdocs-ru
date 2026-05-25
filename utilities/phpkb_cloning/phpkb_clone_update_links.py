"""Post-clone PHPKB DB link updater.

Use this after `phpkb_clone.py` has created cloned categories/articles and
written a mapping JSON with `Articles` and `Categories` sections.

Core behavior:
- remaps article references in `phpkb_articles.article_content`:
  `data-value="..."`, `Article-ID:...`, and `article.php?id=...`;
- remaps category references in `phpkb_articles.article_content`:
  `category.php?id=...`;
- updates `phpkb_articles.article_title` and `article_content` only when
  changes are found.

CLI mode is designed for scripted annual migrations:
- dry-run by default;
- pass `--write` to update PHPKB rows;
- pass `--category-id` to update a category tree, or repeat `--article-id`
  for selected articles;
- pass `--old-version 5.0 --new-version 6.0` for V5 to V6 text migration;
- pass `--replace-product-names` only when legacy product-name cleanup is
  still needed.

No-argument mode preserves the older interactive workflow, including prompted
`4.7` to `5.0` replacements for the historical V4.7 to V5 migration.
"""

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.graceful_interrupt import ensure_cleanup, safe_input
from tools.ssh_kb_ru import establish_connection_interactive

try:
    from pathvalidate import sanitize_filename
except ImportError:
    def sanitize_filename(value):
        return str(value)


TOTAL_PAGES_UPDATED = 0
CONNECTION = None
MAPPING = {}
DEFAULT_MAPPING_FILE = ".mapping.json"


@dataclass
class UpdateOptions:
    mapping: dict
    dry_run: bool = True
    replace_product_names: bool = False
    old_version: str | None = None
    new_version: str | None = None
    prompt_version: bool = False


def numeric_id(value):
    value = str(value).strip()
    if not value.isdigit():
        raise argparse.ArgumentTypeError(f"Expected numeric ID, got: {value}")
    return value


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Update cloned PHPKB article/category links using a mapping JSON.",
    )
    parser.add_argument(
        "--profile",
        choices=("cmw", "cmwlab"),
        help="PHPKB server profile. Defaults to SERVER_PROFILE from .env.",
    )
    parser.add_argument(
        "--mapping",
        default=DEFAULT_MAPPING_FILE,
        help=f"Mapping JSON with Articles/Categories sections. Default: {DEFAULT_MAPPING_FILE}",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--category-id", type=numeric_id, help="Update this category and all descendants.")
    mode.add_argument("--article-id", action="append", type=numeric_id, help="Update one article. Can be used multiple times.")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to PHPKB. CLI mode is dry-run unless this flag is set.",
    )
    parser.add_argument(
        "--replace-product-names",
        action="store_true",
        help="Also replace legacy product names: BAP -> Platform and Architect -> «Архитектор».",
    )
    parser.add_argument("--old-version", help="Version string to replace, e.g. 5.0.")
    parser.add_argument("--new-version", help="Replacement version string, e.g. 6.0.")
    return parser.parse_args(argv)


def has_cli_action(args):
    return bool(args.category_id or args.article_id)


def load_mapping_json(mapping_file=DEFAULT_MAPPING_FILE):
    with open(mapping_file, "r", encoding="utf-8") as mapping_json_file:
        mapping_json_file_content = mapping_json_file.read()
        return json.loads(mapping_json_file_content) if mapping_json_file_content else {}


def normalize_mapping(mapping):
    return {str(source_id): str(target_id) for source_id, target_id in (mapping or {}).items()}


def replace_pattern(content, pattern, replacement):
    updated, count = re.subn(pattern, replacement, content, flags=re.MULTILINE)
    return updated, count


def remap_phpkb_links(article_content, mapping):
    changes = []
    article_mapping = normalize_mapping(mapping.get("Articles"))
    category_mapping = normalize_mapping(mapping.get("Categories"))

    for old_article_id, new_article_id in article_mapping.items():
        replacements = (
            (fr'data-value="{re.escape(old_article_id)}"', f'data-value="{new_article_id}"', "article marker"),
            (fr"Article-ID:{re.escape(old_article_id)}(?!\d)", f"Article-ID:{new_article_id}", "article marker"),
            (fr"article\.php\?id={re.escape(old_article_id)}(?!\d)", f"article.php?id={new_article_id}", "article link"),
        )
        for pattern, replacement, label in replacements:
            article_content, count = replace_pattern(article_content, pattern, replacement)
            if count:
                changes.append(f"Replaced {count} {label}(s) {old_article_id} -> {new_article_id}")

    for old_category_id, new_category_id in category_mapping.items():
        article_content, count = replace_pattern(
            article_content,
            fr"category\.php\?id={re.escape(old_category_id)}(?!\d)",
            f"category.php?id={new_category_id}",
        )
        if count:
            changes.append(f"Replaced {count} category link(s) {old_category_id} -> {new_category_id}")

    return article_content, changes


def replace_product_names(article_content, article_title):
    changes = []

    article_content, content_count = replace_pattern(
        article_content,
        "Comindware Business Application Platform",
        "Comindware Platform",
    )
    article_title, title_count = replace_pattern(
        article_title,
        "Comindware Business Application Platform",
        "Comindware Platform",
    )
    if content_count:
        changes.append(f"Replaced {content_count} product name occurrence(s) in article content")
    if title_count:
        changes.append(f"Replaced {title_count} product name occurrence(s) in article title")

    article_content, architect_count = replace_pattern(
        article_content,
        r"(Comindware )?Architect",
        "«Архитектор»",
    )
    if architect_count:
        changes.append(f"Replaced {architect_count} Architect occurrence(s) in article content")

    return article_content, article_title, changes


def replace_version_text(article_content, article_title, old_version, new_version, prompt=False):
    if not old_version or not new_version:
        return article_content, article_title, []

    changes = []
    version_pattern = re.escape(old_version)

    if re.search(version_pattern, article_title):
        new_article_title = re.sub(version_pattern, new_version, article_title)
        if not prompt or safe_input(f"Replace {article_title} with {new_article_title} ? Y/N").lower() == "y":
            article_title = new_article_title
            changes.append(f"Replaced {old_version} with {new_version} in article title")

    if prompt:
        line_pattern = re.compile(fr"(^.*)({version_pattern})(.*$)", flags=re.MULTILINE)
        for result in list(line_pattern.finditer(article_content)):
            found_line = result.group(0)
            print(f"Found line: {found_line}")
            if safe_input(f"Replace {old_version} with {new_version} ? Y/N").lower() == "y":
                replaced_line = re.sub(version_pattern, new_version, found_line)
                article_content = article_content.replace(found_line, replaced_line, 1)
                changes.append(f"Replaced {old_version} with {new_version} in article content: {replaced_line}")
    else:
        article_content, content_count = replace_pattern(article_content, version_pattern, new_version)
        if content_count:
            changes.append(
                f"Replaced {content_count} {old_version} occurrence(s) with {new_version} in article content"
            )

    return article_content, article_title, changes


def migrate_article_content(article_content, article_title, options):
    updated_content, changes = remap_phpkb_links(article_content, options.mapping)

    updated_title = article_title
    if options.replace_product_names:
        updated_content, updated_title, product_changes = replace_product_names(updated_content, updated_title)
        changes.extend(product_changes)

    updated_content, updated_title, version_changes = replace_version_text(
        updated_content,
        updated_title,
        options.old_version,
        options.new_version,
        prompt=options.prompt_version,
    )
    changes.extend(version_changes)

    return updated_content, updated_title, changes


def updateArticleLinks(article_id, options=None):
    options = options or UpdateOptions(
        mapping=MAPPING,
        dry_run=False,
        replace_product_names=True,
        old_version="4.7",
        new_version="5.0",
        prompt_version=True,
    )

    c = CONNECTION.cursor()
    c.execute(
        """
            SELECT article_content, article_title from phpkb_articles WHERE article_id=%s;
            """,
        (article_id,),
    )

    result = c.fetchone()
    if not result:
        print(f"Article {article_id} not found.")
        return False

    article_content = html.unescape(result[0])
    article_title = result[1]
    updated_content, updated_title, changes = migrate_article_content(article_content, article_title, options)

    if not changes:
        print(f"Article {article_id}: no changes")
        return False

    for change in changes:
        print(change)

    if options.dry_run:
        print(f"Article {article_id}: dry-run, SQL update skipped")
        return True

    print("Executing SQL")
    c.execute(
        """
            UPDATE phpkb_articles
            SET article_title=%s,
            article_content=%s
            WHERE article_id=%s;
            """,
        (updated_title, html.escape(updated_content), article_id),
    )
    return True


def fetchCategory(category_id):
    c = CONNECTION.cursor()
    c.execute(
        """
            SELECT category_id, category_name, parent_id
            FROM phpkb_categories
            WHERE category_id = %s
            """,
        (category_id,),
    )
    return c.fetchone()


def fetchCategories(show="yes", status="public", language_id=2, parent_id=""):
    c = CONNECTION.cursor()
    c.execute(
        """
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories
            WHERE
            -- category_show filter intentionally disabled for post-clone updates.
            -- category_status filter intentionally disabled for post-clone updates.
            -- AND
            phpkb_categories.language_id = %s
            AND parent_id = %s
            """,
        (language_id, parent_id),
    )
    return c.fetchall()


def updateCategoryChildren(parent, options=None):
    c = CONNECTION.cursor(buffered=True)

    category_id = parent[0]
    title = parent[1]

    c.execute(
        """
            SELECT DISTINCT category_id, category_name, parent_id
            FROM phpkb_categories
            WHERE
            -- category_show='yes'
            -- AND category_status = 'public'
            -- AND
            phpkb_categories.language_id = 2
            AND parent_id = %s
            """,
        (category_id,),
    )
    children = c.fetchall()
    print(f"\n-----\n\nCategory {category_id}. {title}. Children: {children}\n")
    print(f"Updating articles from Category {category_id}. {title}.")
    updateArticlesInCategory(category_id, options)
    for child in children:
        updateCategoryChildren(child, options)
    return children


def updateArticlesInCategory(category_id, options=None):
    c = CONNECTION.cursor(buffered=True)
    c.execute(
        """
            SELECT DISTINCT phpkb_articles.article_id, phpkb_articles.article_content, phpkb_articles.article_title
            FROM phpkb_articles, phpkb_relations, phpkb_categories
            WHERE
            -- article_show='yes'
            -- AND
            phpkb_relations.category_id = %s
            AND phpkb_relations.article_id = phpkb_articles.article_id
            """,
        (category_id,),
    )

    articles = c.fetchall()
    global TOTAL_PAGES_UPDATED
    pages = 0
    for article_id, _content, title in articles:
        sanitized_title = sanitize_filename(title)
        filename = f"{article_id} - {sanitized_title}"
        print("    Updating article: " + filename)
        pages += 1
        updateArticleLinks(article_id, options)
    TOTAL_PAGES_UPDATED += pages
    print(f"\nUpdated {pages} articles, total {TOTAL_PAGES_UPDATED}\n\n-----\n")
    return pages


def listCategories(categories):
    index = 1
    for category_id, title, _parent_id in categories:
        print(f"{index}. {category_id}. {title}")
        index += 1


def run_cli(args):
    options = UpdateOptions(
        mapping=MAPPING,
        dry_run=not args.write,
        replace_product_names=args.replace_product_names,
        old_version=args.old_version,
        new_version=args.new_version,
        prompt_version=False,
    )

    mode = "write" if args.write else "dry-run"
    print(f"Mode: {mode}")
    if args.old_version or args.new_version:
        if not (args.old_version and args.new_version):
            raise ValueError("Use --old-version and --new-version together.")
        print(f"Version replacement: {args.old_version} -> {args.new_version}")
    if args.replace_product_names:
        print("Product name replacements: enabled")

    if args.category_id:
        category = fetchCategory(args.category_id)
        if not category:
            print(f"Category {args.category_id} not found.")
            return False
        updateCategoryChildren(category, options)
        return True

    for article_id in args.article_id or ():
        updateArticleLinks(article_id, options)
    return True


def run_interactive():
    updateChildren = ""
    categoryId = ""
    parent_category = ""
    categoryChoice = ""

    print("\nRoot categories:\n")

    while updateChildren != "y":
        categoryChoice = ""
        categories = fetchCategories(parent_id=categoryId)
        if parent_category:
            print("\nParent: {}. {}\n".format(categoryId, categoryTitle))
        if len(categories) > 1:
            parent_category = categories[0]
            listCategories(categories)
            print("\n---------\n")

            if updateChildren.isnumeric() and int(updateChildren) <= len(categories):
                categoryChoice = int(updateChildren) - 1
                updateChildren = "y"
            else:
                while not (categoryChoice.isnumeric() and int(categoryChoice) <= len(categories)):
                    categoryChoice = safe_input("Choose category to browse (1 to {})".format(len(categories)))
                    if categoryChoice.isnumeric() and int(categoryChoice) <= len(categories):
                        categoryChoice = int(categoryChoice) - 1
                        break
                    categoryChoice = ""
                    print("Wrong category choice")

            categoryId = categories[categoryChoice][0]
            categoryTitle = categories[categoryChoice][1]
            childrenCategories = fetchCategories(parent_id=categoryId)
            childrenCategoriesNumber = len(childrenCategories)

            print("\nChosen category: {} {}".format(categoryId, categoryTitle))
            if childrenCategoriesNumber > 0:
                print("\nIt has {} child categories:\n".format(childrenCategoriesNumber))
                listCategories(childrenCategories)
                updateChildren = safe_input(
                    "\nEnter `Y` to update the category and all its child categories and articles. \n"
                    " Or choose a category to browse (1 to {})".format(childrenCategoriesNumber)
                ).lower()
            else:
                print("\nIt has no child categories")
                updateChildren = safe_input(
                    "\nEnter `Y` to update the category and all articles from this category."
                ).lower()
                if updateChildren != "y":
                    print("Updated nothing")
                    break

    else:
        if categories[categoryChoice]:
            updateCategoryChildren(categories[categoryChoice])


def main(argv=None):
    global CONNECTION
    global MAPPING

    args = parse_args(argv)
    MAPPING = load_mapping_json(args.mapping)
    if not MAPPING:
        print(f"Empty {args.mapping}")
        sys.exit(1)

    server = None
    try:
        CONNECTION, server = establish_connection_interactive(args.profile)
        if has_cli_action(args):
            run_cli(args)
        else:
            run_interactive()
    except KeyboardInterrupt:
        pass
    finally:
        ensure_cleanup(CONNECTION, server)


if __name__ == "__main__":
    main()
