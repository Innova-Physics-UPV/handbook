#!/usr/bin/env python3
"""Convert between the chapters in src/ and a single reading copy.

  python3 scripts/reading-copy.py build [OUT.md]   src/ -> one file, in SUMMARY order
  python3 scripts/reading-copy.py split IN.md      one file -> src/, matched by chapter title

The reading copy is for review, or for editing the whole book in one place.
After a split, run `mdbook build` and `scripts/check-style.sh`, and read
`git diff` before committing. src/ remains the source of truth.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SEP = "\n\n---\n\n"
NOTE = ("> **Reading copy.** Every chapter of the handbook in book order, in one file. "
        "Generated from `src/` with `scripts/reading-copy.py build`.")


def chapter_files():
    """Chapter files in the order SUMMARY.md lists them."""
    summary = (SRC / "SUMMARY.md").read_text(encoding="utf-8")
    return [SRC / name for name in re.findall(r"\]\(([^)]+\.md)\)", summary)]


def title(text):
    match = re.search(r"^# (.+)$", text, re.M)
    return match.group(1).strip() if match else None


def build(out):
    parts = [path.read_text(encoding="utf-8").strip() for path in chapter_files()]
    Path(out).write_text(NOTE + SEP + SEP.join(parts) + "\n", encoding="utf-8")
    print(f"wrote {out}")


def split(path):
    text = Path(path).read_text(encoding="utf-8")
    by_title = {}
    for chapter in chapter_files():
        by_title[title(chapter.read_text(encoding="utf-8"))] = chapter
    starts = [m.start() for m in re.finditer(r"^# ", text, re.M)]
    if not starts:
        sys.exit("No chapters found: each chapter starts with a level-1 heading.")
    chunks, unknown, seen = [], [], set()
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        chunk = re.sub(r"\n-{3,}\s*$", "", text[start:end].rstrip()).rstrip() + "\n"
        name = title(chunk)
        if name not in by_title:
            unknown.append(name)
        elif name in seen:
            sys.exit(f"Chapter title appears twice: {name}")
        seen.add(name)
        chunks.append((name, chunk))
    if unknown:
        sys.exit("No chapter file has the title: " + "; ".join(unknown)
                 + ". Rename the heading in src/ or add the chapter to src/SUMMARY.md first.")
    for name, chunk in chunks:
        target = by_title[name]
        if target.read_text(encoding="utf-8") != chunk:
            target.write_text(chunk, encoding="utf-8")
            print(f"updated {target.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "build":
        build(sys.argv[2] if len(sys.argv) > 2 else "reading-copy.md")
    elif len(sys.argv) == 3 and sys.argv[1] == "split":
        split(sys.argv[2])
    else:
        sys.exit(__doc__)
