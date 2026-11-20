# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-rdfa/meta-itemprop-in-item/meta-itemprop-in-item.epub: A meta with itemprop and content inside an item (valid).

The EPUB 3 template, with one element added to content.xhtml by
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-xhtml-rdfa/meta-itemprop-in-item/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-rdfa/meta-itemprop-in-item"
HEAD = None
BODY = '    <div itemscope="" itemtype="https://schema.org/Book"><meta itemprop="name" content="A test book."/></div>'


def main() -> None:
    info = eb.load_set(
        SET, title='A meta with itemprop and content inside an item (valid)',
        description='content.xhtml has <div itemscope="" itemtype="https://schema.org/Book"><meta itemprop="name" content="A test book."/></div> in its body. Does a validator accept the book?',
        subject="EPUB 3.3 content documents")
    content = epub3.xhtml("Content", pv.section(BODY or '    <p class="x">Content.</p>'))
    if HEAD:
        content = rv.head_add(content, HEAD)
    out = eb.write_epub(info.book_dir / "meta-itemprop-in-item.epub", epub3.package(info, content=content))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
