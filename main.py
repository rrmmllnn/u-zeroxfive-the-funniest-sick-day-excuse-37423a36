#!/usr/bin/env python3
# One-line sick-day excuse, delivered deadpan.
#
# The joke: a smartwatch mistakes a stumble for a fall, summons
# an ambulance by itself, and leaves its owner stuck at home
# talking a paramedic out of an emergency caused by nothing
# more dramatic than a charging cable. It reads like a real
# message to a boss -- the punchline arrives in the last clause.
#
# Output: exactly one line, no trailing newline, written to
# entry.txt inside the output directory (default /output).

import os
from pathlib import Path
import sys

TEXT = (
    "My smartwatch thought I fell, called an ambulance, "
    "and now I have to stay home and explain to a paramedic "
    "that I tripped over my own charging cable."
)

LIMIT = 200


def reject(message):
    sys.stderr.write("entry rejected: " + message + "\n")
    raise SystemExit(1)


def check(text):
    cleaned = text.strip()
    if not cleaned:
        reject("the excuse came out blank")
    if len(text) > LIMIT:
        reject("the excuse is %d characters, over the %d cap" % (len(text), LIMIT))
    if cleaned != text or "\n" in text:
        reject("the excuse must be exactly one clean line")


def main():
    check(TEXT)
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
