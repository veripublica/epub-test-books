# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-itemref-elem/itemref-unknown/itemref-unknown.epub: An itemref naming no item.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-itemref-elem/itemref-unknown/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-itemref-elem/itemref-unknown"


def main() -> None:
    info = eb.load_set(
        SET, title='An itemref naming no item',
        description='One extra itemref has an idref that no manifest item has. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = pv.itemref_unknown(epub3.package(info))
    out = eb.write_epub(info.book_dir / "itemref-unknown.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
