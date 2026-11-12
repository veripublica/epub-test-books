# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/app-viewport-meta-syntax/viewport-space-separator/viewport-space-separator.epub: A viewport with only a space as separator (valid).

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-space-separator/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/app-viewport-meta-syntax/viewport-space-separator"


def main() -> None:
    info = eb.load_set(
        SET, title='A viewport with only a space as separator (valid)',
        description='The viewport of content.xhtml is width=1200 height=600, with no comma. Does a validator accept it?',
        subject="EPUB 3.3 fixed layouts")
    files = lv.fixed(epub3, info, content=lv.content_doc(epub3, viewport='width=1200 height=600'))
    out = eb.write_epub(info.book_dir / "viewport-space-separator.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
