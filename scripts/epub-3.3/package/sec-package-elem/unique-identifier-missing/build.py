# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-package-elem/unique-identifier-missing/unique-identifier-missing.epub: package without unique-identifier.

The EPUB 3 template's files with one change to the package document, made by
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-package-elem/unique-identifier-missing/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-package-elem/unique-identifier-missing"


def main() -> None:
    info = eb.load_set(
        SET, title='Package without unique-identifier',
        description='The package element has no unique-identifier attribute. The dc:identifier element is still there. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    out = eb.write_epub(info.book_dir / "unique-identifier-missing.epub", pv.unique_identifier_missing(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
