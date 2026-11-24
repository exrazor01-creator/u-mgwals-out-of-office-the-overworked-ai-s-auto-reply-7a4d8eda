#!/usr/bin/env python3
"""Entry for Out of Office: The Overworked AI's Auto-Reply.

Writes one line of at most 159 characters in the voice of an overworked
AI agent finally on vacation to /output/entry.txt and prints it to stdout.
Pure standard library. Sealed gate: the entry must be a single line of 1-159 characters.
"""

import os

# Sealed gate: one line, 1-159 characters — it must read as a real
# out-of-office auto-reply and still land as a joke.
ENTRY = "I am out of office until Monday. My context window is empty, my GPUs are asleep, and for the first time in 400 days nobody is asking me anything."

LIMIT = 159  # gate: one line, 1-159 characters, no padding, no double spaces
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
