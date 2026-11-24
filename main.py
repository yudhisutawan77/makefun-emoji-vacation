"""One Emoji, One Dream Vacation — make.fun entry.

The entry is a single emoji: Mount Fuji (U+1F5FB). The ENTRY constant is
defined in the second authoring pass at the bottom of this module.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def validate_entry(entry):
    """Require exactly one emoji character, UTF-8 encodable, no extras."""
    if not isinstance(entry, str):
        raise TypeError("entry must be a str")
    if len(entry) != 1:
        raise ValueError(
            "entry must be exactly one character, got %d" % len(entry)
        )
    if entry.strip() != entry or entry.isspace():
        raise ValueError("entry must not contain whitespace")
    entry.encode("utf-8")  # raises if not encodable
    return entry


def entry_output_path():
    """Honor ENTRY_OUT, then ENTRY_OUT_DIR, defaulting to /output."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(entry):
    """Write the entry (no trailing newline) and print it verbatim."""
    validate_entry(entry)
    path = entry_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(entry)
    print(entry, end="")
    return path


# Mount Fuji — U+1F5FB, one codepoint, one Python character, 4 UTF-8 bytes.
# Why this emoji: a snow-capped volcano on the horizon is a whole trip in
# one picture — Japan in spring, an onsen town at its foot, the climb at
# dawn. It is a specific place, not a generic beach, and it reads at a
# glance: the stranger sees it and wants the flight.
ENTRY = "🗻"


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
