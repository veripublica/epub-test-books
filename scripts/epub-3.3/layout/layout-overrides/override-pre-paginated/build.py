# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/layout-overrides/override-pre-paginated/override-pre-paginated.epub: One document made pre-paginated by a spine override (valid).

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/layout-overrides/override-pre-paginated/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/layout-overrides/override-pre-paginated"


def main() -> None:
    info = eb.load_set(
        SET, title='One document made pre-paginated by a spine override (valid)',
        description="The book is reflowable, and the content document's itemref has rendition:layout-pre-paginated. That document has a viewport. Does a validator accept it?",
        subject="EPUB 3.3 fixed layouts")
    files = lv.itemref_properties(epub3.package(info, content=lv.content_doc(epub3)), 'content', 'rendition:layout-pre-paginated')
    out = eb.write_epub(info.book_dir / "override-pre-paginated.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
