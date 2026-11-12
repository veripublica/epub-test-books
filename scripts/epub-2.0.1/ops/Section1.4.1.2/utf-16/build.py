# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ops/Section1.4.1.2/utf-16/utf-16.epub: A content document in UTF-16 (valid).

The EPUB 2 template's files with the change for this set, made with
scripts/lib/opsvariants.py.

Run: python3 scripts/epub-2.0.1/ops/Section1.4.1.2/utf-16/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epub2variants as e2  # noqa: E402,F401
import epubbook as eb  # noqa: E402
import opsvariants as ov  # noqa: E402

SET = "epub-2.0.1/ops/Section1.4.1.2/utf-16"


def main() -> None:
    info = eb.load_set(
        SET, title='A content document in UTF-16 (valid)',
        description='content.xhtml is encoded in UTF-16LE with a byte order mark, and declares it. Does a validator accept it?',
        subject="EPUB 2.0.1 content documents")
    files = ov.content(epub2.package(info, content=ov.doc(epub2, '    <p>Caf\u00e9.</p>')), lambda d: ('\ufeff' + ov.swap(ov.swap(d, 'encoding="UTF-8"', 'encoding="UTF-16"'), 'charset=utf-8', 'charset=utf-16')).encode('utf-16-le'))
    out = eb.write_epub(info.book_dir / "utf-16.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
