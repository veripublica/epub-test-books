# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/package/sec-itemref-elem/itemref-no-idref/itemref-no-idref.epub: an itemref without idref.

The EPUB 3 template's files with one change to the package document, made by
scripts/lib/packagevariants.py.

Run: python3 scripts/epub-3.3/package/sec-itemref-elem/itemref-no-idref/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import packagevariants as pv  # noqa: E402

SET = "epub-3.3/package/sec-itemref-elem/itemref-no-idref"


def main() -> None:
    info = eb.load_set(
        SET, title='An itemref without idref',
        description="The spine has one extra itemref with no idref attribute. The template's two itemrefs stay, so every document is still in the spine. Does a validator reject it?",
        subject="EPUB 3.3 package document")
    out = eb.write_epub(info.book_dir / "itemref-no-idref.epub", pv.itemref_no_idref(epub3.package(info)))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
