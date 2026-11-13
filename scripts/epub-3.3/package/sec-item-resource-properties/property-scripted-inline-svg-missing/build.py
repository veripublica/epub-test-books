# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-resource-properties/property-scripted-inline-svg-missing/property-scripted-inline-svg-missing.epub: A script inside inline SVG, without the scripted property.

The EPUB 3 template's files, changed by scripts/lib/scriptvariants.py `scripted_inline_svg_missing()`.

Run: python3 scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-inline-svg-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import scriptvariants as sv  # noqa: E402

SET = "epub-3.3/package/sec-item-resource-properties/property-scripted-inline-svg-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='A script inside inline SVG, without the scripted property',
        description='content.xhtml has inline SVG with a script element, and the svg property but not scripted. Does a validator reject it?',
        subject="EPUB 3.3 scripting")
    out = eb.write_epub(info.book_dir / "property-scripted-inline-svg-missing.epub", sv.scripted_inline_svg_missing(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
