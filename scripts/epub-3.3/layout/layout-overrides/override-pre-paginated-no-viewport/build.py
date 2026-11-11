# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/layout-overrides/override-pre-paginated-no-viewport/override-pre-paginated-no-viewport.epub: A spine override to pre-paginated, with no viewport.

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/layout-overrides/override-pre-paginated-no-viewport/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/layout-overrides/override-pre-paginated-no-viewport"


def main() -> None:
    info = eb.load_set(
        SET, title='A spine override to pre-paginated, with no viewport',
        description="The book is reflowable, and the content document's itemref has rendition:layout-pre-paginated, but that document has no viewport. Does a validator reject it?",
        subject="EPUB 3.3 fixed layouts")
    files = lv.itemref_properties(epub3.package(info), 'content', 'rendition:layout-pre-paginated')
    out = eb.write_epub(info.book_dir / "override-pre-paginated-no-viewport.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
