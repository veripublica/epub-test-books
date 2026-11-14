# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-filenames/filename-256-bytes/filename-256-bytes.epub: A file name of 256 bytes.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `filename_256_bytes()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-filenames/filename-256-bytes/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-filenames/filename-256-bytes"


def main() -> None:
    info = eb.load_set(
        SET, title='A file name of 256 bytes',
        description='OEBPS/content.xhtml is renamed to a name of 256 bytes (250 as and .xhtml), and the manifest and the navigation document point to it. Does a validator reject the book?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "filename-256-bytes.epub"
    out.write_bytes(ov.filename_256_bytes(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
