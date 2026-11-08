# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-metainf-encryption.xml/never-encrypt-container-xml/never-encrypt-container-xml.epub: container.xml declared encrypted.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `never_encrypted()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/never-encrypt-container-xml/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-metainf-encryption.xml/never-encrypt-container-xml"


def main() -> None:
    info = eb.load_set(
        SET, title='container.xml declared encrypted',
        description='META-INF/encryption.xml declares META-INF/container.xml encrypted. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "never-encrypt-container-xml.epub"
    out.write_bytes(ov.never_encrypted(epub3.package(info), 'META-INF/container.xml'))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
