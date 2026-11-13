# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-two-terms/epub-type-two-terms.epub: epub:type with two terms (valid).

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `type_two_terms()`.

Run: python3 scripts/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-two-terms/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-structural-semantics/epub-type-two-terms"


def main() -> None:
    info = eb.load_set(
        SET, title='epub:type with two terms (valid)',
        description='content.xhtml has epub:type="chapter bodymatter". Does a validator accept the book?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "epub-type-two-terms.epub", xv.type_two_terms(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
