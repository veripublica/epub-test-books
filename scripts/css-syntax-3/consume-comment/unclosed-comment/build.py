# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/css-syntax-3/consume-comment/unclosed-comment/unclosed-comment.epub: A stylesheet that ends inside a comment (valid).

The EPUB 3 template with one linked stylesheet, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/css-syntax-3/consume-comment/unclosed-comment/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "css-syntax-3/consume-comment/unclosed-comment"
CSS = 'p { margin: 0; }\n/* open'


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet that ends inside a comment (valid)',
        description='style.css holds p { margin: 0; }, then /* open with no */ before the end of the file. Does a validator accept the book?',
        subject="CSS Syntax Level 3")
    content = rv.head_link(epub3.xhtml("Content", pv.section('    <p class="x">Content.</p>')), "style.css")
    files = epub3.package(info, content=content, extra=[("style", "style.css", "text/css", "", CSS.encode("utf-8"))])
    out = eb.write_epub(info.book_dir / "unclosed-comment.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
