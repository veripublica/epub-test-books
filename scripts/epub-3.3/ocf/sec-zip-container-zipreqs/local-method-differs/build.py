# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-zipreqs/local-method-differs/local-method-differs.epub: Local header says stored, central header says deflated (valid).

The EPUB 3 template is built for this set, then one byte change is made to
the finished ZIP (scripts/lib/zippatch.py).

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-zipreqs/local-method-differs/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import zippatch as zp  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-zipreqs/local-method-differs"


def main() -> None:
    info = eb.load_set(
        SET, title='Local header says stored, central header says deflated (valid)',
        description='The local header of OEBPS/content.xhtml gives compression method 0 (stored). Its central directory header keeps method 8 (deflated), and the data is deflated. Does a validator accept the container?',
        subject="EPUB 3.3 OCF ZIP container", contributor="epubveri")
    out = info.book_dir / "local-method-differs.epub"
    eb.write_epub(out, epub3.package(info))
    book = out.read_bytes()
    out.write_bytes(zp.local_method_stored(book, "OEBPS/content.xhtml"))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
