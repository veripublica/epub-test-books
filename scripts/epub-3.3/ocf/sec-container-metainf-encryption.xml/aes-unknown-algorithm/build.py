# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-unknown-algorithm/aes-unknown-algorithm.epub: An encryption algorithm EPUB does not name (valid).

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py.

Run: python3 scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-unknown-algorithm/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-unknown-algorithm"


def main() -> None:
    info = eb.load_set(
        SET, title='An encryption algorithm EPUB does not name (valid)',
        description='META-INF/encryption.xml names an encryption algorithm by a URI that no specification defines. Does a validator accept the book?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "aes-unknown-algorithm.epub"
    out.write_bytes(ov.aes_unknown_algorithm(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
