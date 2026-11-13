# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-svg-req/svg-undeclared-xlink-prefix/svg-undeclared-xlink-prefix.epub: An SVG content document that uses the xlink prefix without declaring it.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `svg_undeclared_xlink_prefix()`.

Run: python3 scripts/epub-3.3/content/sec-svg-req/svg-undeclared-xlink-prefix/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-svg-req/svg-undeclared-xlink-prefix"


def main() -> None:
    info = eb.load_set(
        SET, title='An SVG content document that uses the xlink prefix without declaring it',
        description='picture.svg, in the spine, uses xlink:href without declaring xlink. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "svg-undeclared-xlink-prefix.epub", xv.svg_undeclared_xlink_prefix(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
