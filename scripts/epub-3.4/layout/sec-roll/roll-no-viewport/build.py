# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.4/layout/sec-roll/roll-no-viewport/roll-no-viewport.epub: rendition:layout roll, with no viewport in content.xhtml (invalid).

The EPUB 3 template, with the change for this set, following EPUB 3.4.

Run: python3 scripts/epub-3.4/layout/sec-roll/roll-no-viewport/build.py
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

SET = "epub-3.4/layout/sec-roll/roll-no-viewport"


def main() -> None:
    info = eb.load_set(
        SET, title='rendition:layout roll, with no viewport in content.xhtml (invalid)',
        description='The package sets rendition:layout to roll, but content.xhtml has no viewport meta tag. Does a validator reject the book?',
        subject="EPUB 3.4 fixed layouts")
    files = lv.fixed(epub3, info, content=lv.content_doc(epub3, viewport=None), layout="roll")
    out = eb.write_epub(info.book_dir / "roll-no-viewport.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
