# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-rdfa/microdata-itemprop-no-item/microdata-itemprop-no-item.epub: An itemprop on an element that is in no item.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `microdata_itemprop_no_item()`.

Run: python3 scripts/epub-3.3/content/sec-xhtml-rdfa/microdata-itemprop-no-item/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-rdfa/microdata-itemprop-no-item"


def main() -> None:
    info = eb.load_set(
        SET, title='An itemprop on an element that is in no item',
        description='content.xhtml has itemprop on a p that is in no item. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "microdata-itemprop-no-item.epub", xv.microdata_itemprop_no_item(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
