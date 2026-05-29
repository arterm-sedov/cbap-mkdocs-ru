#!/usr/bin/env python3
"""
Synchronize Markdown files from a PHPKB export tree into the MkDocs docs tree by kbId.

Rules:
- Match files by YAML front matter field `kbId` (normalized to string; lenient fallback extraction is used if YAML parsing fails).
- If a kbId exists in destination, consider it present (duplicates allowed but logged; first occurrence used).
- If a kbId exists in source but is missing in destination, copy the first occurrence from source.
- Never overwrite any existing file in destination.
- Destination folder resolution for a missing source file S:
  1) Try to find a neighbor (another .md in the same source directory) whose kbId exists in destination.
     If found, place S into that neighbor's destination directory (lexicographically smallest directory if multiple).
  2) If no neighbor found, place S under `--dst/--import-subdir/<relative_path_from_src_root>`.

Output:
- Writes a lean CSV log to `--log` (default: saved as `phpkb_sync.log` in this script's directory) with header:
  level,action,kbId,src,dst,reason
  Relative `--log` paths are resolved against the script's directory.
- Prints a concise summary to stdout.

Arguments:
- --src: source root (default: phpkb_content/798. Версия 5.0. Текущая рекомендованная)
- --dst: destination root (default: docs/ru)
- --import-subdir: fallback subdirectory under destination root (default: _imported_kb)
- --log: path to CSV log (default: script_dir/phpkb_sync.log)

Dependencies:
- python-frontmatter (pip install python-frontmatter)
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
import re
from pathlib import Path
import shutil
from typing import Dict, List, Optional, Set, Tuple


try:
    import frontmatter  # type: ignore
except Exception as exc:  # pragma: no cover
    sys.stderr.write(
        "Missing dependency: python-frontmatter. Install with: pip install python-frontmatter\n"
    )
    raise


@dataclass
class FileInfo:
    root: Path
    rel_path: Path
    abs_path: Path
    kbid: Optional[str]
    parse_error: Optional[str] = None


def normalize_kbid(value) -> Optional[str]:
    if value is None:
        return None
    # Normalize ints and strings to canonical string without surrounding whitespace
    try:
        text = str(value).strip()
    except Exception:
        return None
    return text or None


def find_md_files(root: Path) -> List[Path]:
    return [p for p in root.rglob("*.md") if p.is_file()]


def _fallback_extract_kbid(file_path: Path) -> Optional[str]:
    """Fallback, lenient kbId extractor reading raw front matter without YAML parsing.

    Strategy:
    - Read small head of file.
    - If a front matter block delimited by --- exists at the top, scan only inside it.
    - Else scan the first 50 non-empty lines for a line like `kbId: <value>`.
    - Return normalized kbId or None.
    """
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None

    head = text.splitlines()
    if not head:
        return None

    kbid_value: Optional[str] = None
    start_idx = None
    end_idx = None

    if head[0].strip() == "---":
        # find closing ---
        for i in range(1, min(len(head), 200)):
            if head[i].strip() == "---":
                start_idx = 1
                end_idx = i
                break
    # If front matter block found, search within it
    search_lines: List[str]
    if start_idx is not None and end_idx is not None:
        search_lines = head[start_idx:end_idx]
    else:
        # Fallback: scan first 50 lines for a kbId: pattern
        search_lines = head[:50]

    kb_pattern = re.compile(r"^\s*kbId\s*:\s*(\S.+?)\s*$")
    for line in search_lines:
        m = kb_pattern.match(line)
        if m:
            raw = m.group(1).strip().strip('"\'')
            # keep only the first token until a comment-like fragment
            raw = raw.split(" #")[0].strip()
            kbid_value = normalize_kbid(raw)
            break

    return kbid_value


def parse_kbid_for_file(root: Path, file_path: Path) -> FileInfo:
    rel_path = file_path.relative_to(root)
    try:
        post = frontmatter.load(file_path)
        kbid = normalize_kbid(post.get("kbId"))
        if not kbid:
            # try fallback even if YAML parsed but kbId absent
            kbid = _fallback_extract_kbid(file_path)
        return FileInfo(root=root, rel_path=rel_path, abs_path=file_path, kbid=kbid)
    except Exception as exc:
        # Try fallback kbId extraction despite YAML parse failure
        kbid_fb = _fallback_extract_kbid(file_path)
        if kbid_fb:
            return FileInfo(root=root, rel_path=rel_path, abs_path=file_path, kbid=kbid_fb, parse_error=None)
        return FileInfo(root=root, rel_path=rel_path, abs_path=file_path, kbid=None, parse_error=str(exc))


def first_occurrence_map(files: List[FileInfo]) -> Tuple[Dict[str, FileInfo], Dict[str, List[FileInfo]]]:
    """Return map of kbId->first FileInfo and duplicates map kbId->list of extra FileInfo."""
    # Sort deterministically by relative path string
    sorted_files = sorted([f for f in files if f.kbid], key=lambda f: str(f.rel_path))
    first: Dict[str, FileInfo] = {}
    dups: Dict[str, List[FileInfo]] = {}
    for info in sorted_files:
        assert info.kbid is not None
        if info.kbid not in first:
            first[info.kbid] = info
        else:
            dups.setdefault(info.kbid, []).append(info)
    return first, dups


def build_kbid_presence(files: List[FileInfo]) -> Set[str]:
    return {f.kbid for f in files if f.kbid}  # type: ignore


def find_neighbors_in_target(
    src_file: FileInfo,
    src_dir_files: List[FileInfo],
    dst_first_by_kbid: Dict[str, FileInfo],
) -> Optional[Path]:
    """Return destination directory Path for neighbor-based placement, or None if not found.

    Strategy: among neighbors (same directory as src_file) with kbId present in destination,
    choose the neighbor whose destination relative path is lexicographically smallest.
    """
    candidates: List[Tuple[str, Path]] = []
    for neighbor in src_dir_files:
        if neighbor.rel_path == src_file.rel_path:
            continue
        if not neighbor.kbid:
            continue
        dst_neighbor = dst_first_by_kbid.get(neighbor.kbid)
        if not dst_neighbor:
            continue
        candidates.append((str(dst_neighbor.rel_path), dst_neighbor.rel_path.parent))
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[0])
    return candidates[0][1]


def write_log_row(writer: csv.writer, level: str, action: str, kbid: Optional[str], src: Optional[Path], dst: Optional[Path], reason: str = "") -> None:
    writer.writerow([
        level,
        action,
        kbid or "",
        src.as_posix() if src else "",
        dst.as_posix() if dst else "",
        reason,
    ])


def main() -> int:
    # Resolve script directory for default log location
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description="Sync Markdown files by kbId from PHPKB export to MkDocs docs tree")
    parser.add_argument("--src", default=str(Path("phpkb_content") / "798. Версия 5.0. Текущая рекомендованная"), help="Source root directory")
    parser.add_argument("--dst", default=str(Path("docs") / "ru"), help="Destination root directory")
    parser.add_argument("--import-subdir", default="_imported_kb", help="Fallback subdirectory under destination root")
    parser.add_argument("--log", default=str(script_dir / "phpkb_sync.log"), help="Path to CSV log file (default saved in script directory)")

    args = parser.parse_args()

    src_root = Path(args.src).resolve()
    dst_root = Path(args.dst).resolve()
    import_subdir = Path(args.import_subdir)
    log_arg = Path(args.log)
    if log_arg.is_absolute():
        log_path = log_arg.resolve()
    else:
        # Save relative log paths in the script directory by default
        log_path = (script_dir / log_arg).resolve()

    if not src_root.exists() or not src_root.is_dir():
        sys.stderr.write(f"Source directory not found: {src_root}\n")
        return 2
    if not dst_root.exists() or not dst_root.is_dir():
        sys.stderr.write(f"Destination directory not found: {dst_root}\n")
        return 2

    # Prepare logging
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_file = log_path.open("w", newline="", encoding="utf-8")
    writer = csv.writer(log_file)
    writer.writerow(["level", "action", "kbId", "src", "dst", "reason"])  # header

    # Scan source and destination
    src_paths = find_md_files(src_root)
    dst_paths = find_md_files(dst_root)

    src_infos = [parse_kbid_for_file(src_root, p) for p in src_paths]
    dst_infos = [parse_kbid_for_file(dst_root, p) for p in dst_paths]

    # Log parse errors and no-kbid files (lean: only source no-kbid; destination no-kbid suppressed)
    for info in src_infos:
        if info.parse_error:
            write_log_row(writer, "WARN", "error_parse_src", None, info.rel_path, None, info.parse_error)
        elif not info.kbid:
            write_log_row(writer, "WARN", "no_kbid_src", None, info.rel_path, None, "no kbId in front matter")
    for info in dst_infos:
        if info.parse_error:
            write_log_row(writer, "WARN", "error_parse_dst", None, info.rel_path, None, info.parse_error)

    # Build first-occurrence maps and duplicates
    src_first, src_dups = first_occurrence_map(src_infos)
    dst_first, dst_dups = first_occurrence_map(dst_infos)

    for kbid, dup_list in src_dups.items():
        kept = src_first[kbid].rel_path
        for info in dup_list:
            write_log_row(writer, "WARN", "duplicate_source_skip", kbid, info.rel_path, None, f"first_kept={kept.as_posix()}")
    for kbid, dup_list in dst_dups.items():
        kept = dst_first[kbid].rel_path
        for info in dup_list:
            write_log_row(writer, "WARN", "duplicate_target_present", kbid, info.rel_path, kept, "target has multiple files for this kbId")

    src_kbids = set(src_first.keys())
    dst_kbids = set(dst_first.keys())
    missing_kbids = sorted(src_kbids - dst_kbids)

    # Index source files by directory for neighbor lookup
    src_dir_to_files: Dict[Path, List[FileInfo]] = {}
    for info in src_infos:
        src_dir_to_files.setdefault(info.rel_path.parent, []).append(info)

    copied = 0
    skipped_exists = 0
    total_missing = len(missing_kbids)

    for kbid in missing_kbids:
        src_info = src_first[kbid]
        src_dir_files = src_dir_to_files.get(src_info.rel_path.parent, [])
        neighbor_dst_dir_rel = find_neighbors_in_target(src_info, src_dir_files, dst_first)

        if neighbor_dst_dir_rel is not None:
            dst_rel = neighbor_dst_dir_rel / src_info.rel_path.name
        else:
            # fallback to import-subdir preserving source relative path
            dst_rel = Path(import_subdir) / src_info.rel_path

        dst_abs = dst_root / dst_rel
        if dst_abs.exists():
            # Never overwrite; skip
            skipped_exists += 1
            write_log_row(writer, "INFO", "skip_exists", kbid, src_info.rel_path, dst_rel, "destination file already exists")
            continue

        # ensure directory exists and copy
        dst_abs.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_info.abs_path, dst_abs)
        copied += 1
        write_log_row(writer, "INFO", "copied", kbid, src_info.rel_path, dst_rel, "")

    # Summary to stdout and log tail as comments
    summary_lines = [
        f"Scanned source files: {len(src_infos)}",
        f"Scanned destination files: {len(dst_infos)}",
        f"Source kbIds (unique): {len(src_kbids)}",
        f"Destination kbIds (unique): {len(dst_kbids)}",
        f"Missing kbIds to copy: {total_missing}",
        f"Copied: {copied}",
        f"Skipped (exists): {skipped_exists}",
        f"Log written to: {log_path}",
    ]

    # Print concise summary
    print("\n".join(summary_lines))

    # Also append summary as commented rows to the log (keeps log lean but self-contained)
    log_file.write("# " + " | ".join(summary_lines) + "\n")
    log_file.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


