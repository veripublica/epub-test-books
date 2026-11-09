# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/resources/sec-file-urls/file-url-hyperlink/file-url-hyperlink.epub: A file URL as a hyperlink.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/resources/sec-file-urls/file-url-hyperlink/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/resources/sec-file-urls/file-url-hyperlink"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A file URL as a hyperlink',
        description='An a element in the content document has a file URL as its href. Does a validator reject it?',
        subject="EPUB 3.3 publication resources")
    files = epub3.package(info, content=doc('    <p><a href="file:///tmp/extra.xhtml">A link</a></p>'))
    out = eb.write_epub(info.book_dir / "file-url-hyperlink.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
