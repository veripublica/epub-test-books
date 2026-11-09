# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-manifest-fallbacks/spine-foreign-with-fallback/spine-foreign-with-fallback.epub: A foreign spine item with a content document fallback (valid).

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-manifest-fallbacks/spine-foreign-with-fallback/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-manifest-fallbacks/spine-foreign-with-fallback"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A foreign spine item with a content document fallback (valid)',
        description='A BMP in the spine has an XHTML document as its manifest fallback. Does a validator accept it?',
        subject="EPUB 3.3 publication resources")
    files = rv.add_itemref(rv.set_fallback(pv.book_has_image(epub3.package(info, extra=[rv.BMP, rv.extra_doc(epub3)])), "foreign", "extra"), '<itemref idref="foreign"/>')
    out = eb.write_epub(info.book_dir / "spine-foreign-with-fallback.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
