# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/ocf/sec-container-metainf-encryption.xml/package-document-obfuscated/package-document-obfuscated.epub: The package document obfuscated.

The EPUB 3 template's files are built for this set, then written as a
container by scripts/lib/ocfvariants.py `package_document_obfuscated()`.

Run: python3 scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/package-document-obfuscated/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import ocfvariants as ov  # noqa: E402

SET = "epub-3.3/ocf/sec-container-metainf-encryption.xml/package-document-obfuscated"


def main() -> None:
    info = eb.load_set(
        SET, title='The package document obfuscated',
        description='OEBPS/package.opf, the package document, is obfuscated with the font obfuscation algorithm and listed in META-INF/encryption.xml. Does a validator reject it?',
        subject="EPUB 3.3 OCF")
    out = info.book_dir / "package-document-obfuscated.epub"
    out.write_bytes(ov.package_document_obfuscated(info, epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
