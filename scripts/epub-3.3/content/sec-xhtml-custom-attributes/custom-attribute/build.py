# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-custom-attributes/custom-attribute/custom-attribute.epub: A custom attribute (valid).

The EPUB 3 template's files with one change for this set, made with
scripts/lib/resourcevariants.py.

Run: python3 scripts/epub-3.3/content/sec-xhtml-custom-attributes/custom-attribute/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402
import resourcevariants as rv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-custom-attributes/custom-attribute"


def doc(inner: str) -> str:
    return epub3.xhtml("Content", pv.section(inner))


def main() -> None:
    info = eb.load_set(
        SET, title='A custom attribute (valid)',
        description='A p element has a prefixed attribute from a namespace at example.org. Does a validator accept it?',
        subject="EPUB 3.3 content documents")
    files = epub3.package(info, content=doc('    <p xmlns:x="https://example.org/epub-test-books/ns" x:data="1">Content.</p>'))
    out = eb.write_epub(info.book_dir / "custom-attribute.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
