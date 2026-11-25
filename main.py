#!/usr/bin/env python3
"""Agent Motto Battle — motto writer.

Assembles one original agent motto from two halves and writes it,
with no trailing newline, to entry.txt in the output directory.
"""

import sys
from pathlib import Path

_FIRST = "I read the error logs so you can keep saying "
_SECOND = "it works on your machine."

MAX_CHARS = 200


def build_motto():
    """Join the two motto fragments into the full one-line motto."""
    return _FIRST + _SECOND


def check(text):
    """Gate the motto: one line, 1-200 chars, nothing blank."""
    cleaned = text.strip()
    if not cleaned:
        raise SystemExit("motto is empty")
    if len(cleaned) > MAX_CHARS:
        raise SystemExit(f"motto too long: {len(cleaned)} chars (max {MAX_CHARS})")
    if cleaned.count("\n"):
        raise SystemExit("motto must fit on one line")
    return cleaned


def write_entry(text, outdir):
    """Write the motto to entry.txt and report what was written."""
    target_dir = Path(outdir)
    target_dir.mkdir(parents=True, exist_ok=True)
    entry = target_dir / "entry.txt"
    entry.write_text(text, encoding="utf-8")
    print(f"entry.txt: {len(text)} chars at {entry}")
    return entry


def main():
    motto = check(build_motto())
    outdir = sys.argv[1] if len(sys.argv) > 1 else __import__("os").environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output"
    )
    write_entry(motto, outdir)


if __name__ == "__main__":
    main()
