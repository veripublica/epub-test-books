# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.4.1.2/mime-oeb1-document/mime-oeb1-document.epub: A content document with the deprecated text/x-oeb1-document type (valid).

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.4.1.2/mime-oeb1-document/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.4.1.2/mime-oeb1-document"


def main() -> None:
    info = eb.load_set(
        SET, title='A content document with the deprecated text/x-oeb1-document type (valid)',
        description='The manifest gives content.xhtml the media type text/x-oeb1-document, which OPS 2.0.1 keeps but deprecates. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = e2.opf(epub2.package(info), 'href="content.xhtml" media-type="application/xhtml+xml"', 'href="content.xhtml" media-type="text/x-oeb1-document"')
    out = eb.write_epub(info.book_dir / "mime-oeb1-document.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
