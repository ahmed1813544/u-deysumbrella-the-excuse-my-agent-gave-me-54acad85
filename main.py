#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — program/v1 entry.

Writes one line: the excuse an AI agent hands its human for missing
a deadline. Stdlib only, deterministic, no network, no input files.
"""

import os

# The excuse, one line, straight-faced: the machine burned the very
# resource it needed on planning to use it.
EXCUSE = (
    "I'm sorry I missed your deadline \u2014 I spent the whole day "
    "meticulously planning how to meet it, and the plan used up "
    "the context window I needed to actually do it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
