# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-fallbacks-img/picture-img-src-foreign/picture-img-src-foreign.epub: A foreign img inside picture.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-fallbacks-img/picture-img-src-foreign/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-fallbacks-img/picture-img-src-foreign"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A foreign img inside picture',
        description='An img inside picture references a BMP that has a manifest fallback. Does a validator reject it?',
        subject="EPUB 3.3 publication resources")
    files = rv.set_fallback(pv.book_has_image(epub3.package(info, content=doc('    <p><picture><img src="image.bmp" alt="A small gray square."/></picture></p>'), extra=[rv.BMP, rv.JPG])), "foreign", "image")
    out = eb.write_epub(info.book_dir / "picture-img-src-foreign.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
