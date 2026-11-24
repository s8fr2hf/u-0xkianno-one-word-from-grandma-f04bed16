"""One Word From Grandma: write the entry word to the output directory.

The word is the one grandma would text about AI: HALP -- her typo for
HELP, sent the moment the robot confuses her. Warm, baffled, funny,
and unmistakably a grandma texting.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        word = f.read().strip()
    if not word or not (1 <= len(word) <= 30):
        print("entry must be 1-30 characters", file=sys.stderr)
        return 1
    if not word.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in word):
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(out_path, 0o644)
    print("wrote %s (%d chars)" % (out_path, len(word)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
