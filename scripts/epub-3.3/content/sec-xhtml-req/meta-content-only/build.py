# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-req/meta-content-only/meta-content-only.epub: A meta with content and no name, http-equiv, charset or itemprop.

The EPUB 3 template, with one element added to content.xhtml by
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-xhtml-req/meta-content-only/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-req/meta-content-only"
HEAD = '<meta content="true"/>'
BODY = None


def main() -> None:
    info = eb.load_set(
        SET, title='A meta with content and no name, http-equiv, charset or itemprop',
        description='content.xhtml has <meta content="true"/> in its head. Does a validator reject the book?',
        subject="EPUB 3.3 content documents")
    content = epub3.xhtml("Content", pv.section(BODY or '    <p class="x">Content.</p>'))
    if HEAD:
        content = rv.head_add(content, HEAD)
    out = eb.write_epub(info.book_dir / "meta-content-only.epub", epub3.package(info, content=content))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
