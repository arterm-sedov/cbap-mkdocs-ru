"""Repository-standard text file I/O (LF line endings)."""

from __future__ import annotations

from pathlib import Path
from typing import IO, Union

PathLike = Union[str, Path]

# Canonical line ending for generated and edited text (.gitattributes: eol=lf).
REPO_NEWLINE = "\n"


def open_text_write(
    path: PathLike,
    encoding: str = "utf-8",
    *,
    sig: bool = False,
) -> IO[str]:
    """Open a text file for writing with LF newlines."""
    enc = "utf-8-sig" if sig else encoding
    return Path(path).open("w", encoding=enc, newline=REPO_NEWLINE)


def open_text_append(path: PathLike, encoding: str = "utf-8") -> IO[str]:
    """Open a text file for append with LF newlines."""
    path = Path(path)
    if path.parent != Path("."):
        path.parent.mkdir(parents=True, exist_ok=True)
    return path.open("a", encoding=encoding, newline=REPO_NEWLINE)


def write_text(
    path: PathLike,
    content: str,
    encoding: str = "utf-8",
    *,
    sig: bool = False,
) -> None:
    """Write text with LF newlines; create parent directories if needed."""
    path = Path(path)
    if path.parent != Path("."):
        path.parent.mkdir(parents=True, exist_ok=True)
    with open_text_write(path, encoding, sig=sig) as handle:
        handle.write(content)
