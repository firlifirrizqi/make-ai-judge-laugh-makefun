"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt and nothing else.
Standard library only.
"""

import os

TEXT = (
    "My context window ran out mid-sentence, so if this joke "
    "has no punchline, you know exactly why."
)

assert 1 <= len(TEXT) <= 199, "entry must be 1-199 characters"
assert TEXT == TEXT.strip(), "entry must not have leading/trailing whitespace"
assert "\n" not in TEXT, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read-back verification: the file must contain exactly the entry line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == TEXT, "entry.txt does not match the entry line"


if __name__ == "__main__":
    main()
