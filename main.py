#!/usr/bin/env python3
"""Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp line, at most 200 characters, that excuses the
writer from a pointless work meeting or Zoom call, to entry.txt.

Deterministic: the same line every run, no network, no secrets, no
reading anything outside this repository. Stdlib only, Python 3.13.
"""

import os
import sys

LINE = "I'm skipping the meeting about meeting overload \u2014 my absence is the only agenda item we've actually completed."


def main() -> int:
    # Self-gate, mirroring the bounty gate: the entry is only valid as
    # UTF-8 text of 1 to 200 characters, not only whitespace. Fail loudly
    # instead of writing an entry the judge would never see.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        print("error: LINE must be 1-200 non-blank characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
