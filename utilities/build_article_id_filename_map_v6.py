"""Build .article_id_filename_map_v6.json for PHPKB import.

Articles: gap-fill stems for cloned V6 ids without a docs/ru file.
Categories: short ASCII folder slugs inferred from docs/ru paths, hyperlinks,
and the V5 phpkb_content tree (to avoid long Cyrillic directory names).
"""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_RU = REPO_ROOT / "docs" / "ru"
HYPERLINKS_FILE = DOCS_RU / ".snippets" / "hyperlinks_mkdocs_to_kb_map.md"
V6_MAPPING_FILE = REPO_ROOT / ".v6mapping.json"
V5_MAP_FILE = REPO_ROOT / ".article_id_filename_map_v5.json"
V5_IMPORT_ROOT = (
    REPO_ROOT
    / "phpkb_content"
    / "798. Версия 5.0. Текущая рекомендованная"
)
OUTPUT_FILE = REPO_ROOT / ".article_id_filename_map_v6.json"

KB_ID_PATTERN = re.compile(r"^kbId:\s*(\S+)", re.MULTILINE)
HYPERLINK_ARTICLE_PATTERN = re.compile(
    r"^\[([^\]]+)\]:\s*\{\{\s*kbArticleURLPrefix\s*\}\}\s*(\d+)\s*$",
    re.MULTILINE,
)
HYPERLINK_CATEGORY_PATTERN = re.compile(
    r"^\[([^\]]+)\]:\s*\{\{\s*kbCategoryURLPrefix\s*\}\}\s*(\d+)\s*$",
    re.MULTILINE,
)
LEGACY_PREFIX_PATTERN = re.compile(r"^(\d+)-(.+)$")
V5_CATEGORY_DIR_PATTERN = re.compile(r"^(\d+)\.")
V5_ARTICLE_FILE_PATTERN = re.compile(r"^(\d+)-(.+)$")

MANUAL_CATEGORY_SLUGS = {
    "896": "platform_v6",
}


def normalize_import_stem(article_id, stem):
    """Drop legacy numeric prefix when it is not the current PHPKB article id."""
    article_id = str(article_id)
    stem = str(stem).strip()
    match = LEGACY_PREFIX_PATTERN.match(stem)
    if match and match.group(1) != article_id:
        return match.group(2)
    return stem


def load_json(path):
    path = Path(path)
    if not path.exists() or path.stat().st_size == 0:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def scan_docs_kbids():
    by_kb_id = {}
    by_kb_id_dir = {}
    for path in DOCS_RU.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError):
            continue
        match = KB_ID_PATTERN.search(text)
        if not match:
            continue
        kb_id = match.group(1)
        by_kb_id[kb_id] = path.stem
        rel_dir = path.parent.relative_to(DOCS_RU)
        by_kb_id_dir[kb_id] = "/".join(rel_dir.parts)
    return by_kb_id, by_kb_id_dir


def scan_hyperlink_anchors():
    if not HYPERLINKS_FILE.is_file():
        return {}, {}
    content = HYPERLINKS_FILE.read_text(encoding="utf-8-sig")
    articles = {
        str(article_id): anchor.strip()
        for anchor, article_id in HYPERLINK_ARTICLE_PATTERN.findall(content)
    }
    categories = {}
    for anchor, category_id in HYPERLINK_CATEGORY_PATTERN.findall(content):
        slug = anchor.strip()
        if slug.endswith("_cat"):
            slug = slug[: -len("_cat")]
        categories[str(category_id)] = slug
    return articles, categories


def cloned_v6_ids_without_docs(docs_by_kb_id, clone_articles):
    clone_v6 = set(clone_articles.values())
    return sorted(clone_v6 - set(docs_by_kb_id.keys()), key=int)


def build_gap_map():
    clone_articles = load_json(V6_MAPPING_FILE).get("Articles", {})
    v5_map = load_json(V5_MAP_FILE)
    docs_by_kb_id, _docs_dirs = scan_docs_kbids()
    hyperlinks, _category_links = scan_hyperlink_anchors()
    rev_v5 = {str(v6_id): str(v5_id) for v5_id, v6_id in clone_articles.items()}

    gap_ids = cloned_v6_ids_without_docs(docs_by_kb_id, clone_articles)
    gap_map = {}

    for v6_id in gap_ids:
        v5_id = rev_v5.get(v6_id)
        stem = None

        for candidate_id in (v6_id, v5_id):
            if not candidate_id:
                continue
            anchor = hyperlinks.get(candidate_id)
            if anchor:
                stem = anchor
                break

        if not stem and v5_id and v5_id in v5_map:
            stem = v5_map[v5_id]

        if not stem and v5_id and v5_id in docs_by_kb_id:
            stem = docs_by_kb_id[v5_id]

        if stem:
            gap_map[v6_id] = normalize_import_stem(v6_id, stem)

    return gap_map, gap_ids


def _docs_path_leaf(path):
    """Last segment of a docs/ru relative path (one hierarchy level, no parent churn)."""
    if not path:
        return None
    return path.split("/")[-1]


def _find_v5_category_dir(v5_category_id):
    if not V5_IMPORT_ROOT.is_dir():
        return None
    prefix = f"{v5_category_id}."
    for path in V5_IMPORT_ROOT.rglob("*"):
        if path.is_dir() and path.name.startswith(prefix):
            return path
    return None


def _stems_from_v5_category_dir(v5_category_id):
    category_dir = _find_v5_category_dir(v5_category_id)
    if not category_dir:
        return []
    stems = []
    for md_path in category_dir.glob("*.md"):
        match = V5_ARTICLE_FILE_PATTERN.match(md_path.stem)
        if match:
            stems.append(match.group(2))
    return stems


def _collect_v5_category_doc_paths(v6_article_map, docs_dirs):
    v5_paths = defaultdict(list)
    if not V5_IMPORT_ROOT.is_dir():
        return v5_paths

    for md_path in V5_IMPORT_ROOT.rglob("*.md"):
        match = V5_ARTICLE_FILE_PATTERN.match(md_path.name)
        if not match:
            continue
        v5_article_id = match.group(1)
        v6_article_id = v6_article_map.get(v5_article_id)
        if not v6_article_id:
            continue
        doc_path = docs_dirs.get(str(v6_article_id))
        if not doc_path:
            continue

        v5_category_id = None
        for part in md_path.relative_to(V5_IMPORT_ROOT).parts[:-1]:
            category_match = V5_CATEGORY_DIR_PATTERN.match(part)
            if category_match:
                v5_category_id = category_match.group(1)
        if v5_category_id:
            v5_paths[v5_category_id].append(doc_path)
    return v5_paths


def _collect_v5_category_parents():
    """Map v5 category id -> v5 parent category id from imported folder nesting."""
    parents = {}
    if not V5_IMPORT_ROOT.is_dir():
        return parents
    for path in V5_IMPORT_ROOT.rglob("*"):
        if not path.is_dir():
            continue
        match = V5_CATEGORY_DIR_PATTERN.match(path.name)
        if not match:
            continue
        category_id = match.group(1)
        parent_id = None
        if path.parent != V5_IMPORT_ROOT:
            parent_match = V5_CATEGORY_DIR_PATTERN.match(path.parent.name)
            if parent_match:
                parent_id = parent_match.group(1)
        parents[category_id] = parent_id
    return parents


def _infer_slug_from_paths(paths):
    """Infer folder slug from the dominant docs/ru path (leaf segment only)."""
    if not paths:
        return None
    counter = Counter(paths)
    best_path, _count = counter.most_common(1)[0]
    return _docs_path_leaf(best_path)


def _disambiguate_duplicate_slugs(category_slugs):
    """Resolve slug collisions only among categories with the same PHPKB parent."""
    clone_categories = load_json(V6_MAPPING_FILE).get("Categories", {})
    v5_parents = _collect_v5_category_parents()
    v6_parent = {}
    for v5_id, v6_id in clone_categories.items():
        parent_v5 = v5_parents.get(str(v5_id))
        parent_v6 = clone_categories.get(str(parent_v5)) if parent_v5 else None
        v6_parent[str(v6_id)] = str(parent_v6) if parent_v6 is not None else ""

    v6_to_v5 = {str(v6_id): str(v5_id) for v5_id, v6_id in clone_categories.items()}

    def sibling_slug_groups():
        groups = defaultdict(list)
        for category_id, slug in category_slugs.items():
            groups[(v6_parent.get(category_id, ""), slug)].append(category_id)
        return groups

    for _pass in range(3):
        changed = False
        for (_parent_id, slug), category_ids in sibling_slug_groups().items():
            if len(category_ids) < 2:
                continue
            for category_id in category_ids:
                v5_id = v6_to_v5.get(category_id)
                if not v5_id:
                    continue
                stems = _stems_from_v5_category_dir(v5_id)
                if len(stems) == 1 and category_slugs[category_id] != stems[0]:
                    category_slugs[category_id] = stems[0]
                    changed = True
        if not changed:
            break

    for (_parent_id, slug), category_ids in sibling_slug_groups().items():
        if len(category_ids) < 2:
            continue
        for category_id in category_ids:
            category_slugs[category_id] = f"{slug}_{category_id}"


def build_category_map():
    clone_categories = load_json(V6_MAPPING_FILE).get("Categories", {})
    v6_article_map = load_json(V6_MAPPING_FILE).get("Articles", {})
    _, docs_dirs = scan_docs_kbids()
    _article_links, hyperlink_categories = scan_hyperlink_anchors()
    v5_doc_paths = _collect_v5_category_doc_paths(v6_article_map, docs_dirs)

    category_slugs = dict(MANUAL_CATEGORY_SLUGS)

    for v5_id, v6_id in clone_categories.items():
        v6_key = str(v6_id)
        if v6_key in category_slugs:
            continue
        if v6_key in hyperlink_categories:
            category_slugs[v6_key] = hyperlink_categories[v6_key]
            continue

        paths = v5_doc_paths.get(str(v5_id), [])
        slug = _infer_slug_from_paths(paths)
        if not slug:
            stems = _stems_from_v5_category_dir(str(v5_id))
            if len(stems) == 1:
                slug = stems[0]
        if slug:
            category_slugs[v6_key] = slug

    _disambiguate_duplicate_slugs(category_slugs)
    return dict(sorted(category_slugs.items(), key=lambda item: int(item[0])))


def main():
    gap_map, gap_ids = build_gap_map()
    category_map = build_category_map()
    payload = {
        "Articles": dict(sorted(gap_map.items(), key=lambda item: int(item[0]))),
        "Categories": category_map,
    }
    OUTPUT_FILE.write_text(
        json.dumps(payload, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(gap_map)} article gap entries and "
        f"{len(category_map)} category folder slugs to {OUTPUT_FILE}"
    )
    if gap_ids:
        missing = [article_id for article_id in gap_ids if article_id not in gap_map]
        if missing:
            print("No stem found for:", ", ".join(missing))


if __name__ == "__main__":
    main()
