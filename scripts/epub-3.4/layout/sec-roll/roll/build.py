# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.4/layout/sec-roll/roll/roll.epub: rendition:layout roll (valid).

The EPUB 3 template, with the change for this set, following EPUB 3.4.

Run: python3 scripts/epub-3.4/layout/sec-roll/roll/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import encodedmedia as em  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402,F401
import minifont as mf  # noqa: E402,F401
import navvariants as nv  # noqa: E402,F401
import packagevariants as pv  # noqa: E402,F401
import resourcevariants as rv  # noqa: E402,F401

SET = "epub-3.4/layout/sec-roll/roll"


def main() -> None:
    info = eb.load_set(
        SET, title='rendition:layout roll (valid)',
        description='The package sets rendition:layout to roll, and both spine documents have a viewport meta tag. Does a validator accept the book?',
        subject="EPUB 3.4 fixed layouts")
    files = lv.fixed(epub3, info, layout="roll")
    out = eb.write_epub(info.book_dir / "roll.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
