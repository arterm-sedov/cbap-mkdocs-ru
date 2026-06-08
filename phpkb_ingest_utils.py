"""Deterministic helpers for building AI ingestion bundles from Markdown."""

from pathlib import Path

import tiktoken


TOKEN_THRESHOLDS = [
    (1_000_000, "M"),
    (1_000, "k"),
]


def read_markdown_file(path):
    """Read an imported Markdown file as text and fail loudly on invalid encoding."""
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise UnicodeError(f"Markdown file is not valid UTF-8: {path}") from exc


def iter_markdown_files(folder):
    root = Path(folder)
    if not root.exists():
        raise FileNotFoundError(f"Input folder does not exist: {folder}")
    return sorted(root.rglob("*.md"), key=lambda path: path.relative_to(root).as_posix().lower())


def build_tree(root, files):
    root = Path(root)
    lines = ["Directory structure:"]

    def add_directory(path, prefix="", is_last=True):
        connector = "└── " if is_last else "├── "
        name = f"{path.name}/" if path.is_dir() else path.name
        lines.append(f"{prefix}{connector}{name}")
        if not path.is_dir():
            return

        children = sorted(
            [child for child in path.iterdir() if child.is_dir() or child.suffix == ".md"],
            key=lambda child: (child.is_dir(), child.name.lower()),
        )
        child_prefix = f"{prefix}{'    ' if is_last else '│   '}"
        for index, child in enumerate(children):
            add_directory(child, child_prefix, index == len(children) - 1)

    add_directory(root)
    return "\n".join(lines)


def build_content(root, files):
    root = Path(root)
    blocks = []
    for path in files:
        relative = path.relative_to(root).as_posix()
        blocks.append(
            "\n".join(
                [
                    "=" * 48,
                    f"FILE: {relative}",
                    "=" * 48,
                    read_markdown_file(path),
                ]
            )
        )
    return "\n\n".join(blocks)


def format_token_count(text):
    """Return a token estimate formatted like gitingest."""
    encoding = tiktoken.get_encoding("o200k_base")
    total_tokens = len(encoding.encode(text, disallowed_special=()))
    for threshold, suffix in TOKEN_THRESHOLDS:
        if total_tokens >= threshold:
            return f"{total_tokens / threshold:.1f}{suffix}"
    return str(total_tokens)


def build_summary(files, tree, content):
    return "\n".join(
        [
            f"Files analyzed: {len(files)}",
            f"Estimated tokens: {format_token_count(tree + content)}",
        ]
    )
