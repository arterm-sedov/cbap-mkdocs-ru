#!/usr/bin/env python3
"""
Combine multiple Markdown files into a single logical reference document.

Features:
- H1 for the document, H2 for each source file as a section
- Demotes headings inside each source file by one level (only outside code fences)
- Optional auto-generated Table of Contents from section titles
- Sensible defaults for file list and output path; overridable via CLI

Usage examples:
  python tools/combine_n3_references.py \
    --output docs/ru/developer_guide/n3/.references/n3_reference_combined.md

  python tools/combine_n3_references.py \
    --title "N3 Reference — Combined" --toc \
    docs/ru/developer_guide/n3/.references/n3_examples_collection.md [...]

Notes for maintainers:
- This script is intentionally verbose and explicit for readability.
- It preserves Comindware authoring nuances by not altering anchors/attributes.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable, List, Tuple


# Default ordered list of source Markdown files (relative to repo root)
DEFAULT_SOURCES: List[str] = [
    "docs/ru/developer_guide/n3/.references/n3_example_collection_last_item.md",
    "docs/ru/developer_guide/n3/.references/n3_presentation_summary_notebook_lm.md",
    "docs/ru/developer_guide/n3/.references/n3_tutorial_plan_angelina_t.md",
    "docs/ru/developer_guide/n3/.references/n3_video_transcript_complete_notebook_lm.md",
    "docs/ru/developer_guide/n3/.references/presentation_converted_from_pdf.md",
    "docs/ru/developer_guide/n3/.references/n3_examples_collection.md",
    "docs/ru/developer_guide/n3/.references/n3_lecture_transcript_2025.08.21.md",
    "docs/ru/.snippers/attribute_document_add_file_n3.md",
    "docs/ru/.snippers/attribute_document_get_file_n3.md",
    "docs/ru/.snippers/attribute_enum_compare_value_n3.md",
    "docs/ru/.snippets/attribute_enum_filter_value_n3.md",
    "docs/ru/.snippets/attribute_enum_get_data_localized_n3.md",
    "docs/ru/.snippets/attribute_enum_get_data_n3.md",
    "docs/ru/.snippets/attribute_enum_set_value_n3.md",
]

DEFAULT_OUTPUT: str = (
    "docs/ru/developer_guide/n3/.references/n3_reference_combined.md"
)


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text_file(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def slugify_for_anchor(text: str) -> str:
    """Very simple slug for Markdown hash links, keeping Cyrillic characters.

    - Lowercase
    - Replace spaces with '-'
    - Remove characters that commonly break anchors
    """
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^\w\-\u0400-\u04FF]", "", text)
    return text


def extract_first_h1(markdown_text: str) -> str | None:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def demote_headings(markdown_text: str) -> str:
    """Demote headings by one level outside of fenced code blocks.

    - "# " becomes "## ", "## " becomes "### ", etc.
    - Leaves lines with fewer than 1 leading '#' unchanged (e.g., plain text)
    - Preserves code fences (``` and ~~~) and everything inside as-is
    """
    lines = markdown_text.splitlines()
    in_fence = False
    fence_pattern = re.compile(r"^\s*(```|~~~)")

    def demote(line: str) -> str:
        if not line.startswith("#"):
            return line
        # Count leading '#'
        m = re.match(r"^(#+)(\s*)(.*)$", line)
        if not m:
            return line
        hashes, space, rest = m.groups()
        return "#" + hashes + space + rest

    out: List[str] = []
    for line in lines:
        if fence_pattern.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
        else:
            out.append(demote(line))
    return "\n".join(out)


@dataclass
class Section:
    title: str
    anchor: str
    body: str


def build_sections(paths: Iterable[str]) -> List[Section]:
    sections: List[Section] = []
    for path in paths:
        if not os.path.exists(path):
            print(f"[WARN] File not found, skipping: {path}", file=sys.stderr)
            continue
        raw = read_text_file(path)
        title = extract_first_h1(raw) or os.path.splitext(os.path.basename(path))[0]
        body = demote_headings(raw)
        anchor = slugify_for_anchor(title)
        sections.append(Section(title=title, anchor=anchor, body=body))
    return sections


def render_document(title: str, sections: List[Section], toc: bool) -> str:
    parts: List[str] = []
    parts.append(f"# {title}")
    parts.append(
        "\n> Автосборка: этот документ сгенерирован из нескольких исходных файлов. "
        "Не редактируйте содержимое ниже вручную — изменяйте исходные файлы.\n"
    )

    if toc and sections:
        parts.append("\n## Оглавление")
        for s in sections:
            parts.append(f"- [{s.title}](#{s.anchor})")

    for s in sections:
        parts.append("")
        parts.append(f"## {s.title}")
        parts.append("")
        parts.append(s.body)

    # Ensure newline at EOF
    out = "\n".join(parts)
    if not out.endswith("\n"):
        out += "\n"
    return out


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Combine multiple Markdown files into a single logical reference."
        )
    )
    parser.add_argument(
        "sources",
        nargs="*",
        help=(
            "Ordered list of source .md files. When omitted, a default curated"
            " list for N3 references is used."
        ),
    )
    parser.add_argument(
        "--output",
        "-o",
        default=DEFAULT_OUTPUT,
        help=f"Output Markdown file (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--title",
        "-t",
        default="N3 Reference — Combined",
        help="Document title (H1)",
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="Include an auto-generated table of contents (section-level)",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    sources = args.sources if args.sources else DEFAULT_SOURCES

    sections = build_sections(sources)
    if not sections:
        print("No input sections were found. Nothing to do.", file=sys.stderr)
        return 2

    document = render_document(title=args.title, sections=sections, toc=args.toc)
    write_text_file(args.output, document)
    print(f"Wrote: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))


