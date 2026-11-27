"""Emit the winning one-word entry for make.fun competition
u-puan-describe-your-ex-in-one-word-9fc6ebe7 ("Describe Your Ex in One Word").

Writes the single word to /output/entry.txt, per the sealed scorer gate:
UTF-8 text, 1-111 characters, not only whitespace, exactly one word,
nothing attached. Standard library only.
"""

import os

LINE = "Placeholder"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 111, f"word must be 1-111 chars, got {len(line)}"
    # The leaderboard's Size column shows bytes and ties break on fewer bytes.
    assert len(line.encode("utf-8")) <= 111, "word must be <=111 bytes"
    assert "\n" not in line and "\r" not in line, "word must be a single line"
    assert len(line.split()) == 1, "entry must be exactly one word"
    assert line.isalpha(), "entry must be a plain word, no punctuation"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be byte-exactly the word,
    # no trailing newline, no hidden bytes.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == line.encode("utf-8"), "round-trip mismatch in entry.txt"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
