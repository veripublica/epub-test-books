# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/selectors-4/sub-pseudo-elements/double-pseudo-element/double-pseudo-element.epub: Two pseudo-elements in a row, p::before::before (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/selectors-4/sub-pseudo-elements/double-pseudo-element/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "selectors-4/sub-pseudo-elements/double-pseudo-element"
CSS = 'p::before::before { margin: 0; }\n'


def main() -> None:
    info = eb.load_set(
        SET, title='Two pseudo-elements in a row, p::before::before (valid)',
        description='style.css holds p::before::before { margin: 0; }. Does a validator accept the book?',
        subject='Selectors Level 4')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    extra = [("style", "style.css", "text/css", "", CSS.encode("utf-8"))]
    files = epub3.package(info, content=content, extra=extra)
    out = eb.write_epub(info.book_dir / "double-pseudo-element.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
