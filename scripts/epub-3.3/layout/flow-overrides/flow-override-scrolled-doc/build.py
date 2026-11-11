# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/flow-overrides/flow-override-scrolled-doc/flow-override-scrolled-doc.epub: A scrolled document in a paginated book (valid).

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/flow-overrides/flow-override-scrolled-doc/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/flow-overrides/flow-override-scrolled-doc"


def main() -> None:
    info = eb.load_set(
        SET, title='A scrolled document in a paginated book (valid)',
        description="The package sets rendition:flow to paginated, and the about document's itemref has rendition:flow-scrolled-doc. Does a validator accept it?",
        subject="EPUB 3.3 reflowable layouts")
    files = lv.itemref_properties(lv.add_meta(epub3.package(info), 'rendition:flow', 'paginated'), 'about', 'rendition:flow-scrolled-doc')
    out = eb.write_epub(info.book_dir / "flow-override-scrolled-doc.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
