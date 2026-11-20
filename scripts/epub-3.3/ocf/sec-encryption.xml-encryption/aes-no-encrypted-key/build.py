# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-encryption.xml-encryption/aes-no-encrypted-key/aes-no-encrypted-key.epub: A content document encrypted with AES-128-CBC, with no EncryptedKey (valid).

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py.

Run: python3 scripts/epub-3.3/ocf/sec-encryption.xml-encryption/aes-no-encrypted-key/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-encryption.xml-encryption/aes-no-encrypted-key"


def main() -> None:
    info = eb.load_set(
        SET, title='A content document encrypted with AES-128-CBC, with no EncryptedKey (valid)',
        description='OEBPS/content.xhtml is encrypted, and META-INF/encryption.xml has an EncryptedData for it but no EncryptedKey. Does a validator accept the book?',
        subject='EPUB 3.3 OCF')
    out = info.book_dir / "aes-no-encrypted-key.epub"
    out.write_bytes(ov.aes_no_encrypted_key(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
