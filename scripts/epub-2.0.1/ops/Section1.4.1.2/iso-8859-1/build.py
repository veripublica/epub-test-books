# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.4.1.2/iso-8859-1/iso-8859-1.epub: A content document in ISO-8859-1.

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.4.1.2/iso-8859-1/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.4.1.2/iso-8859-1"


def main() -> None:
    info = eb.load_set(
        SET, title='A content document in ISO-8859-1',
        description='content.xhtml is encoded in ISO-8859-1 and declares it. Does a validator reject it?',
        subject="EPUB 2.0.1 content documents")
    files = ov.content(epub2.package(info, content=ov.doc(epub2, '    <p>Caf\u00e9.</p>')), lambda d: ov.encoded(d, 'ISO-8859-1', 'iso-8859-1'))
    out = eb.write_epub(info.book_dir / "iso-8859-1.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
