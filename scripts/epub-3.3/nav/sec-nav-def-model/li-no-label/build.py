# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/nav/sec-nav-def-model/li-no-label/li-no-label.epub: A navigation list item with no label.

The EPUB 3 template's files with one change to the navigation document, made
with scripts/lib/navvariants.py.

Run: python3 scripts/epub-3.3/nav/sec-nav-def-model/li-no-label/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import navvariants as nv  # noqa: E402

SET = "epub-3.3/nav/sec-nav-def-model/li-no-label"


def main() -> None:
    info = eb.load_set(
        SET, title='A navigation list item with no label',
        description='A list item in the toc nav holds only an ol, with no a or span before it. Does a validator reject it?',
        subject="EPUB 3.3 navigation document")
    files = nv.li_no_label(epub3.package(info))
    out = eb.write_epub(info.book_dir / "li-no-label.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
