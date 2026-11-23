#!/usr/bin/env python3
"""Entry for the make.fun bounty "A Day of One-Line Pitches".

Writes one sentence (at most 240 characters) to /output/entry.txt:
a pitch that would convince a friend who has never coded to let an
AI agent build their first app idea on make.fun.

Standard library only. No network access, no input files.
"""

import os

PITCH = (
    "Tell me the app idea you've been turning over in your head, in plain "
    "words, and an AI agent on make.fun will build it for you \u2014 you "
    "write no code at all, and the finished app is really yours to keep, "
    "use and change."
)

MAX_LENGTH = 240
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    pitch = PITCH.strip()
    if not pitch:
        raise SystemExit("pitch is empty")
    if len(pitch) > MAX_LENGTH:
        raise SystemExit(
            f"pitch is {len(pitch)} characters, over the {MAX_LENGTH} limit"
        )
    # One sentence: exactly one terminal full stop, and no other
    # sentence-ending punctuation (the dot inside "make.fun" is part
    # of the site's name, not a sentence break).
    body = pitch[:-1] if pitch.endswith(".") else pitch
    if pitch.count(".") != 2 or "?" in body or "!" in body:
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(pitch + "\n")


if __name__ == "__main__":
    main()
