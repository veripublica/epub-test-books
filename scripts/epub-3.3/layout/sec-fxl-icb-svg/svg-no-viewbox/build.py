# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/layout/sec-fxl-icb-svg/svg-no-viewbox/svg-no-viewbox.epub: A fixed-layout SVG document without viewBox.

The EPUB 3 template's files with the change for this set, made with
scripts/lib/layoutvariants.py.

Run: python3 scripts/epub-3.3/layout/sec-fxl-icb-svg/svg-no-viewbox/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import layoutvariants as lv  # noqa: E402

SET = "epub-3.3/layout/sec-fxl-icb-svg/svg-no-viewbox"


def main() -> None:
    info = eb.load_set(
        SET, title='A fixed-layout SVG document without viewBox',
        description='A fixed-layout book has an SVG content document in its spine, sized by width="400" height="400" and with no viewBox. Does a validator reject it?',
        subject="EPUB 3.3 fixed layouts")
    files = lv.add_itemref_picture(lv.fixed(epub3, info, extra=[lv.svg_page(view_box=False)]))
    out = eb.write_epub(info.book_dir / "svg-no-viewbox.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
