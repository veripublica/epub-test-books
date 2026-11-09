# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-item-elem/item-href-path-absolute/item-href-path-absolute.epub: a manifest href starting with /.

The EPUB 3 template's files with one change to the package document, made by
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-item-elem/item-href-path-absolute/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-item-elem/item-href-path-absolute"


def main() -> None:
    info = eb.load_set(
        SET, title='A manifest href starting with /',
        description="A manifest item's href is /OEBPS/content.xhtml, which still resolves to the right file. Does a validator reject the form of the URL?",
        subject="EPUB 3.3 package document")
    out = eb.write_epub(info.book_dir / "item-href-path-absolute.epub", pv.item_href_path_absolute(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
