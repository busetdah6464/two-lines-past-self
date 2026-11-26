#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt:
line 1 warns the past self about one specific moment (one sentence),
line 2 says in one sentence why that moment mattered and what changed.
Deterministic, stdlib only, no network. Running it twice yields
byte-identical output.
"""

import os

LINES = [
    "Don't trade your battered red bicycle for Rizky's cracked phone behind the school canteen in October 2016.",
    "That bike was the only way across the flooded road to your sister's recital, and losing it meant you missed the one song she ever sang for you.",
]

TEXT = "\n".join(LINES) + "\n"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
