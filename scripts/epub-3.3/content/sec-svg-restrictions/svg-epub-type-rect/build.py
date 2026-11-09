# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-svg-restrictions/svg-epub-type-rect/svg-epub-type-rect.epub: epub:type on an SVG rect (valid).

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-svg-restrictions/svg-epub-type-rect/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-svg-restrictions/svg-epub-type-rect"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='epub:type on an SVG rect (valid)',
        description='An inline SVG rect element has epub:type. Does a validator accept it?',
        subject="EPUB 3.3 content documents")
    files = rv.content_properties(pv.book_has_image(epub3.package(info, content=doc(rv.inline_svg('<rect epub:type="chapter" width="40" height="40" fill="gray"/>')))), "svg")
    out = eb.write_epub(info.book_dir / "svg-epub-type-rect.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
