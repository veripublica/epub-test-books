# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-enc-compression/compression-method-9/compression-method-9.epub: A Compression property with Method 9.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py.

Run: python3 scripts/epub-3.3/ocf/sec-enc-compression/compression-method-9/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-enc-compression/compression-method-9"


def main() -> None:
    info = eb.load_set(
        SET, title='A Compression property with Method 9',
        description='The Compression property in META-INF/encryption.xml gives Method="9". Does a validator reject the book?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "compression-method-9.epub"
    out.write_bytes(ov.aes_compressed_first(epub3.package(info), method=9))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
