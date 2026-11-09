# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-svg-restrictions/standalone-foreignobject-two-bodies/standalone-foreignobject-two-bodies.epub: Two body elements in a standalone SVG foreignObject.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-svg-restrictions/standalone-foreignobject-two-bodies/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-svg-restrictions/standalone-foreignobject-two-bodies"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='Two body elements in a standalone SVG foreignObject',
        description='An SVG content document has a foreignObject holding two body elements. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    files = rv.add_itemref(pv.book_has_image(epub3.package(info, extra=[rv.standalone_svg('<foreignObject width="40" height="40"><body xmlns="http://www.w3.org/1999/xhtml"><p>One</p></body><body xmlns="http://www.w3.org/1999/xhtml"><p>Two</p></body></foreignObject>')])), '<itemref idref="picture"/>')
    out = eb.write_epub(info.book_dir / "standalone-foreignobject-two-bodies.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
