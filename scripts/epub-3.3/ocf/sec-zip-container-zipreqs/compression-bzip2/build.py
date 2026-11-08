# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-zip-container-zipreqs/compression-bzip2/compression-bzip2.epub: An entry compressed with bzip2.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `compression_bzip2()`.

Run: python3 scripts/epub-3.3/ocf/sec-zip-container-zipreqs/compression-bzip2/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-zip-container-zipreqs/compression-bzip2"


def main() -> None:
    info = eb.load_set(
        SET, title='An entry compressed with bzip2',
        description='One entry, the content document, is compressed with bzip2 (ZIP method 12) instead of Deflate. Does a validator reject the container?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "compression-bzip2.epub"
    out.write_bytes(ov.compression_bzip2(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
