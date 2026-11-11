# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/orientation/orientation-with-refines/orientation-with-refines.epub: rendition:orientation with refines.

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/orientation/orientation-with-refines/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/orientation/orientation-with-refines"


def main() -> None:
    info = eb.load_set(
        SET, title='rendition:orientation with refines',
        description='The rendition:orientation meta element has refines="#content". Does a validator reject it?',
        subject="EPUB 3.3 fixed layouts")
    files = lv.add_meta(lv.fixed(epub3, info), 'rendition:orientation', 'landscape', ' refines="#content"')
    out = eb.write_epub(info.book_dir / "orientation-with-refines.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
