# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/layout-overrides/override-reflowable/override-reflowable.epub: Both documents made reflowable by spine overrides (valid).

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/layout-overrides/override-reflowable/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/layout-overrides/override-reflowable"


def main() -> None:
    info = eb.load_set(
        SET, title='Both documents made reflowable by spine overrides (valid)',
        description='The book is pre-paginated, and both spine items have rendition:layout-reflowable, so neither needs a viewport. Neither has one. Does a validator accept it?',
        subject="EPUB 3.3 fixed layouts")
    files = lv.itemref_properties(lv.itemref_properties(lv.fixed(epub3, info, content=epub3.content_doc(), about=False), 'content', 'rendition:layout-reflowable'), 'about', 'rendition:layout-reflowable')
    out = eb.write_epub(info.book_dir / "override-reflowable.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
