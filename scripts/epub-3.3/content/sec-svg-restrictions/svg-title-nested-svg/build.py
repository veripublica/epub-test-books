# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-svg-restrictions/svg-title-nested-svg/svg-title-nested-svg.epub: An svg element inside an SVG title.

The EPUB 3 template's files with one change for this set.

Run: python3 scripts/epub-3.3/content/sec-svg-restrictions/svg-title-nested-svg/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-svg-restrictions/svg-title-nested-svg"


def main() -> None:
    info = eb.load_set(
        SET, title='An svg element inside an SVG title',
        description='An inline SVG title holds an svg element. Does a validator reject it?',
        subject='EPUB 3.3 content documents')
    files = rv.content_properties(pv.book_has_image(epub3.package(info, content=epub3.xhtml("Content", pv.section(rv.inline_svg('<title><svg xmlns="http://www.w3.org/2000/svg"/></title>'))))), "svg")
    out = eb.write_epub(info.book_dir / "svg-title-nested-svg.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
