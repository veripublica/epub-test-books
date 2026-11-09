# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-mathml-missing/property-mathml-missing.epub: MathML without the mathml property.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-mathml-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-mathml-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='MathML without the mathml property',
        description='The content document has MathML, and its manifest item has no mathml property. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = epub3.package(info, content=epub3.xhtml("Content", pv.section("    <p><math xmlns=\"http://www.w3.org/1998/Math/MathML\" alttext=\"x\"><mi>x</mi></math></p>")))
    out = eb.write_epub(info.book_dir / "property-mathml-missing.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
