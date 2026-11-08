# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-zipreqs/filename-not-utf8/filename-not-utf8.epub: A file name not encoded as UTF-8.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `filename_not_utf8()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-zipreqs/filename-not-utf8/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-zipreqs/filename-not-utf8"


def main() -> None:
    info = eb.load_set(
        SET, title='A file name not encoded as UTF-8',
        description="The content document's name holds the byte 0x81 (u with diaeresis in CP437, the old ZIP default), and the entry's UTF-8 flag is clear. Does a validator reject the container?",
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "filename-not-utf8.epub"
    out.write_bytes(ov.filename_not_utf8(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
