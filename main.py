#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name (at most 32 characters) to
/output/entry.txt. Fully deterministic: no randomness, no network,
no clock. The program self-checks the gate on every run:
1-32 characters, a single line, not only whitespace.

The entry: "WiFi died. So did the marriage" (30 characters).
The joke lands on the first read — the Wi-Fi dying is bad enough,
but the marriage dying with it is the twist — and the two short
sentences imply a whole story: a household, a dead router, and a
relationship that apparently ran on the same connection.
"""

import os
import sys

ENTRY = "WiFi died. So did the marriage"

MAX_CHARS = 32


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, gate requires 1-%d"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if text != text.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return True


def parse_args(argv):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    check_only = False
    i = 1
    while i < len(argv):
        arg = argv[i]
        if arg == "--check-only":
            check_only = True
        elif arg == "--out" and i + 1 < len(argv):
            out_dir = argv[i + 1]
            i += 1
        elif arg.startswith("--out="):
            out_dir = arg[len("--out="):]
        else:
            raise SystemExit("unknown argument: %s" % arg)
        i += 1
    return out_dir, check_only


def main(argv):
    out_dir, check_only = parse_args(argv)
    validate(ENTRY)
    if check_only:
        print("OK: entry is %d characters" % len(ENTRY))
        return 0
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
