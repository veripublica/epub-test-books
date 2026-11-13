# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Run both verifiers on every .epub in a set folder and keep their output.

    python3 scripts/check.py books/templates/epub3-minimal

For each book, writes next to it:
    <book>.epubveri-<version>.txt    epubveri -i <book> -u --advisory
    <book>.epubcheck-<version>.txt   epubcheck <book> -u

Old outputs are never edited (CONTRIBUTING §5). If a file for this version
already exists and the new run differs, the script stops and says so, so the
difference is looked at instead of overwritten. Paths in the output are made
relative to the set folder, so the files do not depend on where the
repository is checked out.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


def version(cmd: list[str], pattern: str) -> str:
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    m = re.search(pattern, out)
    if not m:
        raise SystemExit(f"cannot read the version from {' '.join(cmd)}")
    return m.group(1)


def run(cmd: list[str], cwd: Path) -> str:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, cwd=cwd)
    text = p.stdout
    return text.rstrip("\n") + f"\n[exit {p.returncode}]\n"


ALTERNATIVES = re.compile(r"must be a string matching the regular expression .*$")
SPLIT = re.compile(r", (?=must be )| or (?=must be )")


def same_but_order(a: str, b: str) -> bool:
    """True if a and b differ only in the order epubcheck lists the patterns
    of a "must be a string matching the regular expression ..." message.
    epubcheck 5.4.0 does not list them in a fixed order from run to run."""
    def norm(text: str) -> str:
        return ALTERNATIVES.sub(
            lambda m: " | ".join(sorted(SPLIT.split(m.group(0)))), text)
    al, bl = a.splitlines(), b.splitlines()
    return len(al) == len(bl) and all(
        x == y or norm(x) == norm(y) for x, y in zip(al, bl))


def keep(path: Path, text: str) -> str:
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if old == text:
            return "unchanged"
        if same_but_order(old, text):
            return "unchanged (epubcheck listed the same patterns in another order)"
        raise SystemExit(f"{path}: a new run differs from the kept output; "
                         "look at the difference, do not overwrite")
    path.write_text(text, encoding="utf-8")
    return "written"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    folder = Path(sys.argv[1]).resolve()
    books = sorted(folder.glob("*.epub"))
    if not books:
        raise SystemExit(f"no .epub in {folder}")
    v_veri = version(["epubveri", "-V"], r"epubveri (\S+)")
    v_check = version(["epubcheck", "--version"], r"EPUBCheck v(\S+)")
    for book in books:
        n = book.name
        for tool, ver, cmd in (
            ("epubveri", v_veri, ["epubveri", "-i", n, "-u", "--advisory"]),
            ("epubcheck", v_check, ["epubcheck", n, "-u"]),
        ):
            out = folder / f"{book.stem}.{tool}-{ver}.txt"
            text = run(cmd, folder)
            print(f"{out.name}: {keep(out, text)}")
            lines = text.strip().splitlines()
            summary = [ln for ln in lines if "Messages:" in ln or "VALID" in ln]
            print("   " + (summary[-1] if summary else lines[-1]))


if __name__ == "__main__":
    main()
