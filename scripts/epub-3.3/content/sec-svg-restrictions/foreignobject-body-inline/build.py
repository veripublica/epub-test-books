# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-svg-restrictions/foreignobject-body-inline/foreignobject-body-inline.epub: A body in inline SVG foreignObject.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-svg-restrictions/foreignobject-body-inline/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-svg-restrictions/foreignobject-body-inline"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A body in inline SVG foreignObject',
        description='Inline SVG has a foreignObject holding a body. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    files = rv.content_properties(pv.book_has_image(epub3.package(info, content=doc(rv.inline_svg('<foreignObject width="40" height="40"><body xmlns="http://www.w3.org/1999/xhtml"><p>Text</p></body></foreignObject>')))), "svg")
    out = eb.write_epub(info.book_dir / "foreignobject-body-inline.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
