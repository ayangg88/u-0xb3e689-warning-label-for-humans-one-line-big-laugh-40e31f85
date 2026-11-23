#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry - a single-line safety warning label for human beings,
at most 160 characters, funny first and plausible second - to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR when the harness sets it).
The output is deterministic: the same label on every run.
"""

import os

LABEL = "WARNING: This human will say 'I'm fine' while visibly falling apart. Do not ask twice."

assert 1 <= len(LABEL) <= 160, "label must be 1-160 characters"
assert "\n" not in LABEL, "label must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LABEL)
    except OSError:
        # No writable output mount (e.g. a local run): write beside the script.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LABEL)


if __name__ == "__main__":
    main()
