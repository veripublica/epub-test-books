# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-css-req/style-attribute-direction/style-attribute-direction.epub: direction: rtl in a style attribute.

The EPUB 3 template with the body below, made with scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-css-req/style-attribute-direction/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-css-req/style-attribute-direction"
BODY = '    <p style="direction: rtl">Content.</p>'
SVG = False


def main() -> None:
    info = eb.load_set(
        SET, title='direction: rtl in a style attribute',
        description='content.xhtml holds <p style="direction: rtl">Content.</p>. Does a validator reject the book?',
        subject='EPUB 3.3 content documents')
    content = epub3.xhtml("Content", pv.section(BODY))
    files = []
    for name, data in epub3.package(info, content=content):
        if name == "OEBPS/package.opf" and SVG:
            data = rv.swap(data, 'href="content.xhtml" media-type="application/xhtml+xml"/>',
                           'href="content.xhtml" media-type="application/xhtml+xml" properties="svg"/>')
        files.append((name, data))
    out = eb.write_epub(info.book_dir / "style-attribute-direction.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
