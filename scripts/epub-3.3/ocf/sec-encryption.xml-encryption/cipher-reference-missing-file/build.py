# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-encryption.xml-encryption/cipher-reference-missing-file/cipher-reference-missing-file.epub: An encryption.xml entry for a file that is not in the container.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `cipher_reference_missing()`.

Run: python3 scripts/epub-3.3/ocf/sec-encryption.xml-encryption/cipher-reference-missing-file/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-encryption.xml-encryption/cipher-reference-missing-file"


def main() -> None:
    info = eb.load_set(
        SET, title='An encryption.xml entry for a file that is not in the container',
        description='META-INF/encryption.xml declares OEBPS/secret.xhtml encrypted, and the container has no such file. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "cipher-reference-missing-file.epub"
    out.write_bytes(ov.cipher_reference_missing(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
