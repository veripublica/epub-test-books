# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-data-urls/data-url-img-foreign/data-url-img-foreign.epub: A BMP as a data URL in img.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-data-urls/data-url-img-foreign/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-data-urls/data-url-img-foreign"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A BMP as a data URL in img',
        description='An img element has a data URL holding a BMP and has no fallback. Does a validator reject it?',
        subject="EPUB 3.3 publication resources")
    files = pv.book_has_image(epub3.package(info, content=doc(rv.img(rv.gray_bmp_url()))))
    out = eb.write_epub(info.book_dir / "data-url-img-foreign.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
