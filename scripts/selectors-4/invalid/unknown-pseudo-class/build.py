# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/selectors-4/invalid/unknown-pseudo-class/unknown-pseudo-class.epub: A selector with an unknown pseudo-class, p:foo (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/selectors-4/invalid/unknown-pseudo-class/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "selectors-4/invalid/unknown-pseudo-class"
CSS = 'p:foo { margin: 0; }\n'


def main() -> None:
    info = eb.load_set(
        SET, title='A selector with an unknown pseudo-class, p:foo (valid)',
        description='style.css holds p:foo { margin: 0; }. Does a validator accept the book?',
        subject='Selectors Level 4')
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    extra = [("style", "style.css", "text/css", "", CSS.encode("utf-8"))]
    files = epub3.package(info, content=content, extra=extra)
    out = eb.write_epub(info.book_dir / "unknown-pseudo-class.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
