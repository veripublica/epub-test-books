# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-elem/media-type-image-jpg/media-type-image-jpg.epub: a JPEG declared as image/jpg.

The EPUB 3 template's files with one change to the package document, made by
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-item-elem/media-type-image-jpg/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import minijpeg  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-item-elem/media-type-image-jpg"


def main() -> None:
    info = eb.load_set(
        SET, title='A JPEG declared as image/jpg',
        description='A generated JPEG shown in a content document is declared in the manifest as image/jpg instead of image/jpeg. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    body = ("    <section id=\"content\" epub:type=\"chapter\" role=\"doc-chapter\">\n"
            "    <h1>Content</h1>\n"
            "    <p><img src=\"image.jpg\" alt=\"A small gray square.\"/></p>\n"
            "    </section>")
    files = epub3.package(info, content=epub3.xhtml("Content", body),
                          extra=[("image", "image.jpg", "image/jpg", "", minijpeg.gray_jpeg())])
    out = eb.write_epub(info.book_dir / "media-type-image-jpg.epub", pv.book_has_image(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
