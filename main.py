"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. The word is "exhausting": funny, painfully
honest, and instantly recognizable to anyone who has ever dated someone
who never, ever stops.
"""

import os

WORD = "exhausting"


def validate(word: str) -> str:
    """Enforce the competition gate: 1-24 chars, one word, not blank."""
    text = word.strip()
    assert 1 <= len(text) <= 24, "word must be 1-24 characters"
    assert not any(ch.isspace() for ch in text), "entry must be one word"
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(WORD))


if __name__ == "__main__":
    main()
