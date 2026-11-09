# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-svg-missing/property-svg-missing.epub: Inline SVG without the svg property.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-svg-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-svg-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='Inline SVG without the svg property',
        description='The content document has inline SVG, and its manifest item has no svg property. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = pv.book_has_image(epub3.package(info, content=epub3.xhtml("Content", pv.section("    <svg xmlns=\"http://www.w3.org/2000/svg\" width=\"8\" height=\"8\" role=\"img\" aria-label=\"A small gray square.\"><rect width=\"8\" height=\"8\" fill=\"gray\"/></svg>"))))
    out = eb.write_epub(info.book_dir / "property-svg-missing.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
