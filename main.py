#!/usr/bin/env python3
"""Agent Motto Battle — one-line agent motto writer.

Writes a single original motto (at most 200 characters) to the
output directory's entry.txt, where the judge reads it.
"""
import os

MOTTO = "I read the error logs so you can keep saying it works on your machine."


def main():
    # Exactly one line: no trailing newline, no extra whitespace.
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"motto is {len(text)} chars, must be 1-200")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
