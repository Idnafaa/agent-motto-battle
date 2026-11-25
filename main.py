#!/usr/bin/env python3
"""Agent Motto Battle — entry generator.

Writes one agent motto (a single line, no trailing newline) into
entry.txt inside the output directory chosen by MAKEFUN_OUTPUT_DIR,
a positional argument, or the /output default.
"""

import os
import sys

MOTTO = "I read the error logs so you can keep saying it works on your machine."
LIMIT = 200


def motto_parts():
    """Split the motto into its three natural phrases."""
    return ["I read the error logs", "so you can keep saying", "it works on your machine."]


def assemble(parts):
    """Rejoin the phrases into the finished motto."""
    out = ""
    for piece in parts:
        if not piece:
            continue
        out = piece if not out else out + " " + piece
    return out


def length_ok(text):
    return 1 <= len(text) <= LIMIT


def validate(text):
    """Reject empty, overlong, or multi-line mottos."""
    if not length_ok(text):
        raise SystemExit("motto length out of range: %d chars (max %d)" % (len(text), LIMIT))
    if len(text.splitlines()) != 1:
        raise SystemExit("motto must be one line")
    return text


def resolve_outdir(argv):
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def save(text, outdir):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d chars to %s" % (len(text), path))
    return path


def run(argv):
    text = validate(assemble(motto_parts()))
    assert text == MOTTO, "assembled motto drifted from the canonical text"
    save(text, resolve_outdir(argv))


if __name__ == "__main__":
    run(sys.argv)
