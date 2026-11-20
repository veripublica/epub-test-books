# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.4.1.2/meta-content-only/meta-content-only.epub: A meta with content and no name or http-equiv in an EPUB 2 content document (valid).

The EPUB 2 template, with one element added to the head of content.xhtml by
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.4.1.2/meta-content-only/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.4.1.2/meta-content-only"
HEAD = '<meta content="true"/>'


def main() -> None:
    info = eb.load_set(
        SET, title='A meta with content and no name or http-equiv in an EPUB 2 content document (valid)',
        description='content.xhtml has <meta content="true"/> in its head. Does a validator accept the book?',
        subject="EPUB 2.0.1 content documents")
    files = epub2.package(info, content=ov.doc(epub2, '    <p>Content.</p>', head=[HEAD]))
    out = eb.write_epub(info.book_dir / "meta-content-only.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
