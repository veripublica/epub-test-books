# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-package-elem/package-version-wrong/package-version-wrong.epub: package version="3.1".

The EPUB 3 template's files with one change to the package document, made by
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-package-elem/package-version-wrong/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-package-elem/package-version-wrong"


def main() -> None:
    info = eb.load_set(
        SET, title='Package version="3.1"',
        description='The package element says version="3.1". Does a validator reject it?',
        subject="EPUB 3.3 package document")
    out = eb.write_epub(info.book_dir / "package-version-wrong.epub", pv.package_version_wrong(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
