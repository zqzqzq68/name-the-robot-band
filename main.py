#!/usr/bin/env python3
"""Robot band name entry for make.fun's "Name the Robot Band" bounty.

Writes one funny band name, plus a few words on its hit song, to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``. The text is fixed: the same bytes on
every run, no input read, no network, no randomness.
"""

import os

ENTRY = (
    "The Rebootstraps \u2014 hit single 'Have You Tried Turning Me Off "
    "and On Again' topped the charts, then crashed mid-chorus."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
