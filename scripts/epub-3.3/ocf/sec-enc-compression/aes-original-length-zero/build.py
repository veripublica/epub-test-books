# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-enc-compression/aes-original-length-zero/aes-original-length-zero.epub: A Compression element with OriginalLength="0".

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py.

Run: python3 scripts/epub-3.3/ocf/sec-enc-compression/aes-original-length-zero/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-enc-compression/aes-original-length-zero"


def main() -> None:
    info = eb.load_set(
        SET, title='A Compression element with OriginalLength="0"',
        description='OEBPS/content.xhtml is Deflate-compressed, then encrypted, and its Compression property gives OriginalLength="0". Does a validator reject the book?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "aes-original-length-zero.epub"
    out.write_bytes(ov.aes_original_length_zero(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
