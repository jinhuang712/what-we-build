"""Put one blank line around headings, fences, tables and lists in Markdown files.

Usage: python3 blank_lines.py FILE.md [FILE.md ...]

It adds missing blank lines and collapses runs of blank lines outside code
fences. Every non-blank line stays as it was: the script checks that before it
writes, and stops with an error when it would not.
"""
import re
import sys

LIST = re.compile(r"^(\s*)([-*+]|\d+\.)\s")


def kind(line):
    s = line.rstrip("\n")
    if not s.strip():
        return "blank"
    if s.startswith("```"):
        return "fence"
    if s.startswith("#"):
        return "heading"
    if s.startswith("|"):
        return "table"
    if LIST.match(s):
        return "list"
    if s.startswith((" ", "\t")):
        return "indent"
    return "text"


def fix(lines):
    out = []
    in_fence = False
    prev = "blank"
    for line in lines:
        k = kind(line)
        if in_fence:
            out.append(line)
            if k == "fence":
                in_fence = False
                prev = "fence-end"
            continue
        if k == "blank":
            # Collapse runs of blank lines outside fences to one.
            if prev != "blank":
                out.append(line)
            prev = "blank"
            continue
        need_blank = False
        if prev != "blank" and out:
            if k in ("heading", "fence"):
                need_blank = True
            elif prev in ("heading", "fence-end"):
                need_blank = True
            elif k == "table" and prev != "table":
                need_blank = True
            elif prev == "table" and k != "table":
                need_blank = True
            elif k == "list" and prev == "text":
                need_blank = True
            elif k == "text" and prev in ("list", "indent"):
                need_blank = True
        if need_blank:
            out.append("\n")
        out.append(line)
        if k == "fence":
            in_fence = True
        prev = k
    return out


for path in sys.argv[1:]:
    with open(path) as f:
        old = f.readlines()
    new = fix(old)
    assert [l for l in old if l.strip()] == [l for l in new if l.strip()], path
    with open(path, "w") as f:
        f.writelines(new)
    print(f"{path}: {len(old)} -> {len(new)}")
