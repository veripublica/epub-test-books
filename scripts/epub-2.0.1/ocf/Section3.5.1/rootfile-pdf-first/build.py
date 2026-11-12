# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ocf/Section3.5.1/rootfile-pdf-first/rootfile-pdf-first.epub: A PDF rendition before the OPF rootfile (valid).

The EPUB 2 template's files are built for this set, then written as a
container by scripts/lib/ocf2variants.py.

Run: python3 scripts/epub-2.0.1/ocf/Section3.5.1/rootfile-pdf-first/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epubbook as eb  # noqa: E402
import ocf2variants as ov2  # noqa: E402

SET = "epub-2.0.1/ocf/Section3.5.1/rootfile-pdf-first"


def main() -> None:
    info = eb.load_set(
        SET, title='A PDF rendition before the OPF rootfile (valid)',
        description='container.xml lists PDF/book.pdf as application/pdf first, then OEBPS/package.opf, and the PDF is in the container. Does a validator accept the book?',
        subject="EPUB 2.0.1 OCF")
    files = epub2.package(info)
    out = info.book_dir / "rootfile-pdf-first.epub"
    out.write_bytes(ov2.rootfile_pdf_first(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
