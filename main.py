#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — one unsent confession, two lines.

Writes the confession to /output/entry.txt. Pure standard library,
deterministic: the same bytes on every run.
"""

import os

TO_LINE = "To: the girl in the blue coat at the bus stop"
MESSAGE_LINE = (
    "I practised saying hello for six months and the day I finally did, "
    "you weren't there."
)


def main() -> None:
    entry = TO_LINE + "\n" + MESSAGE_LINE
    # Gate: /output/entry.txt must be 1-260 chars in total and the message
    # line at most 200 chars. Fewer bytes wins the tie-break, so the entry
    # carries no trailing newline.
    assert 1 <= len(entry) <= 260, f"entry is {len(entry)} chars"
    assert len(MESSAGE_LINE) <= 200, f"message is {len(MESSAGE_LINE)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
