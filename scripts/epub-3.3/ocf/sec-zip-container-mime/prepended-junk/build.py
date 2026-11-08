# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-mime/prepended-junk/prepended-junk.epub: Junk before the first local header.

The EPUB 3 template is built for this set, then one byte change is made to
the finished ZIP (scripts/lib/zippatch.py).

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-mime/prepended-junk/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import zippatch as zp  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-mime/prepended-junk"


def main() -> None:
    info = eb.load_set(
        SET, title='Junk before the first local header',
        description='16 bytes come before the first local header, and no offset is adjusted for them.',
        subject="EPUB 3.3 OCF ZIP container", contributor="epubveri")
    out = info.book_dir / "prepended-junk.epub"
    eb.write_epub(out, epub3.package(info))
    book = out.read_bytes()
    out.write_bytes(zp.prepend(book, b"JUNKJUNKJUNKJUNK"))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
