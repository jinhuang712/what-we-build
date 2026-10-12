"""Report relative Markdown links and #anchors that do not resolve.

Usage: python3 check_links.py FILE.md [FILE.md ...]

Checks [text](target) links whose target is a relative path, a path with
#anchor, or a bare #anchor. Anchors follow GitHub's heading slugs. Links in
code spans and fenced code blocks are skipped. External links are skipped.
Exits 1 when any link is broken.
"""
import os
import re
import sys

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
CODE_SPAN = re.compile(r"`+[^`]*`+")


def slug(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def lines_outside_fences(path):
    in_fence = False
    with open(path, encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
                continue
            if not in_fence:
                yield number, line


_anchor_cache = {}


def anchors(path):
    if path not in _anchor_cache:
        seen = {}
        found = set()
        for _, line in lines_outside_fences(path):
            m = HEADING.match(line)
            if not m:
                continue
            base = slug(m.group(2))
            n = seen.get(base, 0)
            found.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
        _anchor_cache[path] = found
    return _anchor_cache[path]


def check(path):
    broken = []
    folder = os.path.dirname(os.path.abspath(path))
    for number, line in lines_outside_fences(path):
        for target in LINK.findall(CODE_SPAN.sub("", line)):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            file_part, _, anchor = target.partition("#")
            target_path = os.path.normpath(os.path.join(folder, file_part)) if file_part else os.path.abspath(path)
            if not os.path.exists(target_path):
                broken.append((number, target, "missing file"))
                continue
            if anchor and target_path.endswith(".md") and anchor.lower() not in anchors(target_path):
                broken.append((number, target, "missing anchor"))
    return broken


def main(paths):
    failed = False
    for path in paths:
        for number, target, why in check(path):
            print(f"{path}:{number}: {target} ({why})")
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
