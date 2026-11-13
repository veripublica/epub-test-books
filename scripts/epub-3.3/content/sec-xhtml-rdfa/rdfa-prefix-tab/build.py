# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""Build books/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-tab/rdfa-prefix-tab.epub: An RDFa prefix attribute with a tab after the colon.

The EPUB 3 template's files, changed by scripts/lib/xhtmlextvariants.py `rdfa_prefix_tab()`.

Run: python3 scripts/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-tab/build.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(ROOT / "scripts/lib"), str(ROOT / "scripts/templates/epub3-minimal")]
import build as epub3  # noqa: E402
import epubbook as eb  # noqa: E402
import xhtmlextvariants as xv  # noqa: E402

SET = "epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-tab"


def main() -> None:
    info = eb.load_set(
        SET, title='An RDFa prefix attribute with a tab after the colon',
        description='content.xhtml has prefix="dc:&#9;http://purl.org/dc/terms/", a tab after the colon. Does a validator reject it?',
        subject="EPUB 3.3 content documents")
    out = eb.write_epub(info.book_dir / "rdfa-prefix-tab.epub", xv.rdfa_prefix_tab(epub3, info))
    print(out.relative_to(eb.ROOT))


if __name__ == "__main__":
    main()
