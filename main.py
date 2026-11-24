"""One-Liner Marathon entry: write a single one-line comedy joke to entry.txt.

The joke is a fixed line: the setup promises obedience to advice, the
punchline breaks it in the most literal way possible, in one breath.
No input, no randomness, no network, no time: the same line every run.
"""

LINE = "My horoscope told me to avoid impulse decisions, so I bought it framed."


def _validate(line):
    """Mirror the competition gate: 1-280 chars, exactly one line, not blank."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not (1 <= len(line) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(line))
    if line.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    line.encode("utf-8")
    return line


def main():
    import os

    line = _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        raise RuntimeError("entry.txt did not round-trip byte for byte")
    # Re-check the gate on what is actually on disk, not just on the
    # in-memory line: the file the judge reads is what must pass.
    _validate(back)
    if back.count("\n") + back.count("\r") != 0:
        raise RuntimeError("entry.txt must hold exactly one line")
    print("%s (%d chars)" % (line, len(line)))


if __name__ == "__main__":
    main()
