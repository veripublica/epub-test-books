# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-zipreqs/mimetype-data-shift/mimetype-data-shift.epub: 22 bytes inside the mimetype data.

The EPUB 3 template is built for this set, then one byte change is made to
the finished ZIP (scripts/lib/zippatch.py).

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-zipreqs/mimetype-data-shift/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import zippatch as zp  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-zipreqs/mimetype-data-shift"


def main() -> None:
    info = eb.load_set(
        SET, title='22 bytes inside the mimetype data',
        description='22 bytes (an end-of-central-directory signature and 18 zero bytes) are inserted at file offset 40, inside the stored mimetype data. No header and no offset is changed, so every offset after that point is 22 bytes off. Does a validator reject the container?',
        subject="EPUB 3.3 OCF ZIP container", contributor="epubveri")
    out = info.book_dir / "mimetype-data-shift.epub"
    eb.write_epub(out, epub3.package(info))
    book = out.read_bytes()
    out.write_bytes(zp.insert_in_mimetype_data(book))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
