# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-2.0.1/ocf/Section4/compression-bzip2/compression-bzip2.epub: A file compressed with BZIP2.

The EPUB 2 template's files are built for this set, then written as a
container by scripts/lib/ocf2variants.py.

Run: python3 scripts/epub-2.0.1/ocf/Section4/compression-bzip2/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub2-minimal")]
import build as epub2  # noqa: E402
import epubbook as eb  # noqa: E402
import ocf2variants as ov2  # noqa: E402

SET = "epub-2.0.1/ocf/Section4/compression-bzip2"


def main() -> None:
    info = eb.load_set(
        SET, title='A file compressed with BZIP2',
        description='OEBPS/content.xhtml is compressed with BZIP2 (method 12). Does a validator reject the book?',
        subject="EPUB 2.0.1 OCF")
    files = epub2.package(info)
    out = info.book_dir / "compression-bzip2.epub"
    out.write_bytes(ov2.compression_bzip2(files))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
