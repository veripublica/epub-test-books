# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-conditional-3/at-supports/direction-in-supports-invalid/direction-in-supports-invalid.epub: direction: rtl inside an @supports rule with an invalid condition, @supports foo (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-conditional-3/at-supports/direction-in-supports-invalid/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-conditional-3/at-supports/direction-in-supports-invalid"
CSS = '@supports foo { p { direction: rtl; } }\n'


def main() -> None:
    info = eb.load_set(
        SET, title='direction: rtl inside an @supports rule with an invalid condition, @supports foo (valid)',
        description='style.css holds @supports foo { p { direction: rtl; } }. Does a validator accept the book?',
        subject='CSS Conditional Rules Module Level 3')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    files = epub3.package(info, content=content, extra=[("style", "style.css", "text/css", "", CSS.encode("utf-8"))])
    out = eb.write_epub(info.book_dir / "direction-in-supports-invalid.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
