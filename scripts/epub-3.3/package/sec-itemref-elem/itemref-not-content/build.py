# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-itemref-elem/itemref-not-content/itemref-not-content.epub: A stylesheet in the spine.

The EPUB 3 template's files with one change for this set, made with
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-itemref-elem/itemref-not-content/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-itemref-elem/itemref-not-content"


def main() -> None:
    info = eb.load_set(
        SET, title='A stylesheet in the spine',
        description='A CSS file with no fallback is in the spine. Does a validator reject it?',
        subject="EPUB 3.3 package document")
    files = pv.itemref_not_content(epub3.package(info, extra=[("extra-css", "extra.css", "text/css", "", "p { margin: 0; }\n")]))
    out = eb.write_epub(info.book_dir / "itemref-not-content.epub", files)
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
