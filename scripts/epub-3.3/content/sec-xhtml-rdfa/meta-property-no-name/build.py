# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-rdfa/meta-property-no-name/meta-property-no-name.epub: A meta with RDFa property and content and no name (valid).

The EPUB 3 template, with one element added to content.xhtml by
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-xhtml-rdfa/meta-property-no-name/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-rdfa/meta-property-no-name"
HEAD = '<meta property="dcterms:title" content="A test book."/>'
BODY = None


def main() -> None:
    info = eb.load_set(
        SET, title='A meta with RDFa property and content and no name (valid)',
        description='content.xhtml has <meta property="dcterms:title" content="A test book."/> in its head. Does a validator accept the book?',
        subject="EPUB 3.3 content documents")
    content = epub3.xhtml("Content", pv.section(BODY or '    <p class="x">Content.</p>'))
    if HEAD:
        content = rv.head_add(content, HEAD)
    out = eb.write_epub(info.book_dir / "meta-property-no-name.epub", epub3.package(info, content=content))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
