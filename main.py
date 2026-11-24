#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line (<=140 chars) in which a robot vacuum explains why
it missed a spot, to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Standard library only.
"""

import os

EXCUSE = (
    "My cliff sensor mistook the rug's shadow for a staircase, "
    "so I filed the corner as a death trap and spent the run hiding from it."
)


def main() -> None:
    # Self-check the gate before writing: one line, 1-140 chars.
    assert "\n" not in EXCUSE and 1 <= len(EXCUSE) <= 140, (
        f"excuse fails gate: {len(EXCUSE)} chars"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
